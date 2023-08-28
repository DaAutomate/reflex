"""reflex.testing - tools for testing reflex apps."""
from __future__ import annotations

import contextlib
import dataclasses
import inspect
import os
import pathlib
import platform
import re
import signal
import socket
import socketserver
import subprocess
import textwrap
import threading
import time
import types
from http.server import SimpleHTTPRequestHandler
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
    Optional,
    Type,
    TypeVar,
    Union,
    cast,
)

import psutil
import uvicorn

import reflex
import reflex.reflex
import reflex.utils.build
import reflex.utils.exec
import reflex.utils.prerequisites
import reflex.utils.processes
from reflex.app import EventNamespace

try:
    from selenium import webdriver  # pyright: ignore [reportMissingImports]
    from selenium.webdriver.remote.webdriver import (  # pyright: ignore [reportMissingImports]
        WebDriver,
    )

    if TYPE_CHECKING:
        from selenium.webdriver.remote.webelement import (  # pyright: ignore [reportMissingImports]
            WebElement,
        )

    has_selenium = True
except ImportError:
    has_selenium = False

DEFAULT_TIMEOUT = 10
POLL_INTERVAL = 0.25
FRONTEND_LISTENING_MESSAGE = re.compile(r"ready started server on.*, url: (.*:[0-9]+)$")
FRONTEND_POPEN_ARGS = {}
T = TypeVar("T")
TimeoutType = Optional[Union[int, float]]

if platform.system == "Windows":
    FRONTEND_POPEN_ARGS["creationflags"] = subprocess.CREATE_NEW_PROCESS_GROUP  # type: ignore
else:
    FRONTEND_POPEN_ARGS["start_new_session"] = True


# borrowed from py3.11
class chdir(contextlib.AbstractContextManager):
    """Non thread-safe context manager to change the current working directory."""

    def __init__(self, path):
        """Prepare contextmanager.

        Args:
            path: the path to change to
        """
        self.path = path
        self._old_cwd = []

    def __enter__(self):
        """Save current directory and perform chdir."""
        self._old_cwd.append(os.getcwd())
        os.chdir(self.path)

    def __exit__(self, *excinfo):
        """Change back to previous directory on stack.

        Args:
            excinfo: sys.exc_info captured in the context block
        """
        os.chdir(self._old_cwd.pop())


@dataclasses.dataclass
class AppHarness:
    """AppHarness executes a reflex app in-process for testing."""

    app_name: str
    app_source: Optional[types.FunctionType | types.ModuleType]
    app_path: pathlib.Path
    app_module_path: pathlib.Path
    app_module: Optional[types.ModuleType] = None
    app_instance: Optional[reflex.App] = None
    frontend_process: Optional[subprocess.Popen] = None
    frontend_url: Optional[str] = None
    backend_thread: Optional[threading.Thread] = None
    backend: Optional[uvicorn.Server] = None
    _frontends: list["WebDriver"] = dataclasses.field(default_factory=list)

    @classmethod
    def create(
        cls,
        root: pathlib.Path,
        app_source: Optional[types.FunctionType | types.ModuleType] = None,
        app_name: Optional[str] = None,
    ) -> "AppHarness":
        """Create an AppHarness instance at root.

        Args:
            root: the directory that will contain the app under test.
            app_source: if specified, the source code from this function or module is used
                as the main module for the app. If unspecified, then root must already
                contain a working reflex app and will be used directly.
            app_name: provide the name of the app, otherwise will be derived from app_source or root.

        Returns:
            AppHarness instance
        """
        if app_name is None:
            if app_source is None:
                app_name = root.name.lower()
            else:
                app_name = app_source.__name__.lower()
        return cls(
            app_name=app_name,
            app_source=app_source,
            app_path=root,
            app_module_path=root / app_name / f"{app_name}.py",
        )

    def _initialize_app(self):
        self.app_path.mkdir(parents=True, exist_ok=True)
        if self.app_source is not None:
            # get the source from a function or module object
            source_code = textwrap.dedent(
                "".join(inspect.getsource(self.app_source).splitlines(True)[1:]),
            )
            with chdir(self.app_path):
                reflex.reflex.init(
                    name=self.app_name,
                    template=reflex.constants.Template.DEFAULT,
                    loglevel=reflex.constants.LogLevel.INFO,
                )
                self.app_module_path.write_text(source_code)
        with chdir(self.app_path):
            # ensure config and app are reloaded when testing different app
            reflex.config.get_config(reload=True)
            self.app_module = reflex.utils.prerequisites.get_app(reload=True)
        self.app_instance = self.app_module.app

    def _start_backend(self):
        if self.app_instance is None:
            raise RuntimeError("App was not initialized.")
        self.backend = uvicorn.Server(
            uvicorn.Config(
                app=self.app_instance.api,
                host="127.0.0.1",
                port=0,
            )
        )
        self.backend_thread = threading.Thread(target=self.backend.run)
        self.backend_thread.start()

    def _start_frontend(self):
        # Set up the frontend.
        with chdir(self.app_path):
            config = reflex.config.get_config()
            config.api_url = "http://{0}:{1}".format(
                *self._poll_for_servers().getsockname(),
            )
            reflex.utils.build.setup_frontend(self.app_path)

        # Start the frontend.
        self.frontend_process = reflex.utils.processes.new_process(
            [reflex.utils.prerequisites.get_package_manager(), "run", "dev"],
            cwd=self.app_path / reflex.constants.WEB_DIR,
            env={"PORT": "0"},
            **FRONTEND_POPEN_ARGS,
        )

    def _wait_frontend(self):
        while self.frontend_url is None:
            line = (
                self.frontend_process.stdout.readline()  # pyright: ignore [reportOptionalMemberAccess]
            )
            if not line:
                break
            print(line)  # for pytest diagnosis
            m = FRONTEND_LISTENING_MESSAGE.search(line)
            if m is not None:
                self.frontend_url = m.group(1)
                break
        if self.frontend_url is None:
            raise RuntimeError("Frontend did not start")

    def start(self) -> "AppHarness":
        """Start the backend in a new thread and dev frontend as a separate process.

        Returns:
            self
        """
        self._initialize_app()
        self._start_backend()
        self._start_frontend()
        self._wait_frontend()
        return self

    def __enter__(self) -> "AppHarness":
        """Contextmanager protocol for `start()`.

        Returns:
            Instance of AppHarness after calling start()
        """
        return self.start()

    def stop(self) -> None:
        """Stop the frontend and backend servers."""
        if self.backend is not None:
            self.backend.should_exit = True
        if self.frontend_process is not None:
            # https://stackoverflow.com/a/70565806
            frontend_children = psutil.Process(self.frontend_process.pid).children(
                recursive=True,
            )
            if platform.system() == "Windows":
                self.frontend_process.terminate()
            else:
                pgrp = os.getpgid(self.frontend_process.pid)
                os.killpg(pgrp, signal.SIGTERM)
            # kill any remaining child processes
            for child in frontend_children:
                # It's okay if the process is already gone.
                with contextlib.suppress(psutil.NoSuchProcess):
                    child.terminate()
            _, still_alive = psutil.wait_procs(frontend_children, timeout=3)
            for child in still_alive:
                # It's okay if the process is already gone.
                with contextlib.suppress(psutil.NoSuchProcess):
                    child.kill()
            # wait for main process to exit
            self.frontend_process.communicate()
        if self.backend_thread is not None:
            self.backend_thread.join()
        for driver in self._frontends:
            driver.quit()

    def __exit__(self, *excinfo) -> None:
        """Contextmanager protocol for `stop()`.

        Args:
            excinfo: sys.exc_info captured in the context block
        """
        self.stop()

    @staticmethod
    def _poll_for(
        target: Callable[[], T],
        timeout: TimeoutType = None,
        step: TimeoutType = None,
    ) -> T | bool:
        """Generic polling logic.

        Args:
            target: callable that returns truthy if polling condition is met.
            timeout: max polling time
            step: interval between checking target()

        Returns:
            return value of target() if truthy within timeout
            False if timeout elapses
        """
        if timeout is None:
            timeout = DEFAULT_TIMEOUT
        if step is None:
            step = POLL_INTERVAL
        deadline = time.time() + timeout
        while time.time() < deadline:
            success = target()
            if success:
                return success
            time.sleep(step)
        return False

    def _poll_for_servers(self, timeout: TimeoutType = None) -> socket.socket:
        """Poll backend server for listening sockets.

        Args:
            timeout: how long to wait for listening socket.

        Returns:
            first active listening socket on the backend

        Raises:
            RuntimeError: when the backend hasn't started running
            TimeoutError: when server or sockets are not ready
        """
        if self.backend is None:
            raise RuntimeError("Backend is not running.")
        backend = self.backend
        # check for servers to be initialized
        if not self._poll_for(
            target=lambda: getattr(backend, "servers", False),
            timeout=timeout,
        ):
            raise TimeoutError("Backend servers are not initialized.")
        # check for sockets to be listening
        if not self._poll_for(
            target=lambda: getattr(backend.servers[0], "sockets", False),
            timeout=timeout,
        ):
            raise TimeoutError("Backend is not listening.")
        return backend.servers[0].sockets[0]

    def frontend(self, driver_clz: Optional[Type["WebDriver"]] = None) -> "WebDriver":
        """Get a selenium webdriver instance pointed at the app.

        Args:
            driver_clz: webdriver.Chrome (default), webdriver.Firefox, webdriver.Safari,
                webdriver.Edge, etc

        Returns:
            Instance of the given webdriver navigated to the frontend url of the app.

        Raises:
            RuntimeError: when selenium is not importable or frontend is not running
        """
        if not has_selenium:
            raise RuntimeError(
                "Frontend functionality requires `selenium` to be installed, "
                "and it could not be imported."
            )
        if self.frontend_url is None:
            raise RuntimeError("Frontend is not running.")
        driver = driver_clz() if driver_clz is not None else webdriver.Chrome()
        driver.get(self.frontend_url)
        self._frontends.append(driver)
        return driver

    async def emit_state_updates(self) -> list[Any]:
        """Send any backend state deltas to the frontend.

        Returns:
            List of awaited response from each EventNamespace.emit() call.

        Raises:
            RuntimeError: when the app hasn't started running
        """
        if self.app_instance is None or self.app_instance.sio is None:
            raise RuntimeError("App is not running.")
        event_ns: EventNamespace = cast(
            EventNamespace,
            self.app_instance.sio.namespace_handlers["/event"],
        )
        pending: list[Coroutine[Any, Any, Any]] = []
        for state in self.app_instance.state_manager.states.values():
            delta = state.get_delta()
            if delta:
                update = reflex.state.StateUpdate(delta=delta, events=[], final=True)
                state._clean()
                # Emit the event.
                pending.append(
                    event_ns.emit(
                        str(reflex.constants.SocketEvent.EVENT),
                        update.json(),
                        to=state.get_sid(),
                    ),
                )
        responses = []
        for request in pending:
            responses.append(await request)
        return responses

    def poll_for_content(
        self,
        element: "WebElement",
        timeout: TimeoutType = None,
        exp_not_equal: str = "",
    ) -> str:
        """Poll element.text for change.

        Args:
            element: selenium webdriver element to check
            timeout: how long to poll element.text
            exp_not_equal: exit the polling loop when the element text does not match

        Returns:
            The element text when the polling loop exited

        Raises:
            TimeoutError: when the timeout expires before text changes
        """
        if not self._poll_for(
            target=lambda: element.text != exp_not_equal,
            timeout=timeout,
        ):
            raise TimeoutError(
                f"{element} content remains {exp_not_equal!r} while polling.",
            )
        return element.text

    def poll_for_value(
        self,
        element: "WebElement",
        timeout: TimeoutType = None,
        exp_not_equal: str = "",
    ) -> Optional[str]:
        """Poll element.get_attribute("value") for change.

        Args:
            element: selenium webdriver element to check
            timeout: how long to poll element value attribute
            exp_not_equal: exit the polling loop when the value does not match

        Returns:
            The element value when the polling loop exited

        Raises:
            TimeoutError: when the timeout expires before value changes
        """
        if not self._poll_for(
            target=lambda: element.get_attribute("value") != exp_not_equal,
            timeout=timeout,
        ):
            raise TimeoutError(
                f"{element} content remains {exp_not_equal!r} while polling.",
            )
        return element.get_attribute("value")

    def poll_for_clients(self, timeout: TimeoutType = None) -> dict[str, reflex.State]:
        """Poll app state_manager for any connected clients.

        Args:
            timeout: how long to wait for client states

        Returns:
            active state instances when the polling loop exited

        Raises:
            RuntimeError: when the app hasn't started running
            TimeoutError: when the timeout expires before any states are seen
        """
        if self.app_instance is None:
            raise RuntimeError("App is not running.")
        state_manager = self.app_instance.state_manager
        if not self._poll_for(
            target=lambda: state_manager.states,
            timeout=timeout,
        ):
            raise TimeoutError("No states were observed while polling.")
        return state_manager.states


class SimpleHTTPRequestHandlerCustomErrors(SimpleHTTPRequestHandler):
    """SimpleHTTPRequestHandler with custom error page handling."""

    def __init__(self, *args, error_page_map: dict[str, pathlib.Path], **kwargs):
        """Initialize the handler.

        Args:
            error_page_map: map of error code to error page path
        """
        self.error_page_map = error_page_map
        super().__init__(*args, **kwargs)

    def send_error(
        self, code: int, message: str | None = None, explain: str | None = None
    ) -> None:
        """Send the error page for the given error code.

        If the code matches a custom error page, then message and explain are
        ignored.

        Args:
            code: the error code
            message: the error message
            explain: the error explanation
        """
        error_page = self.error_page_map.get(code)
        if error_page:
            self.send_response(code, message)
            self.send_header("Connection", "close")
            body = error_page.read_bytes()
            self.send_header("Content-Type", self.error_content_type)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            super().send_error(code, message, explain)


class Subdir404TCPServer(socketserver.TCPServer):
    """TCPServer for SimpleHTTPRequestHandlerCustomErrors that serves from a subdir."""

    def __init__(
        self,
        *args,
        root: pathlib.Path,
        error_page_map: dict[str, pathlib.Path] | None,
        **kwargs,
    ):
        """Initialize the server.

        Args:
            root: the root directory to serve from
            error_page_map: map of error code to error page path
        """
        self.root = root
        self.error_page_map = error_page_map
        super().__init__(*args, **kwargs)

    def finish_request(self, request, client_address):
        """Finish one request by instantiating RequestHandlerClass."""
        self.RequestHandlerClass(
            request,
            client_address,
            self,
            directory=str(self.root),
            error_page_map=self.error_page_map,
        )


class AppHarnessProd(AppHarness):
    """AppHarnessProd executes a reflex app in-process for testing.

    In prod mode, instead of running `next dev` the app is exported as static
    files and served via the builtin python http.server with custom 404 redirect
    handling. Additionally, the backend runs in multi-worker mode.
    """

    frontend_thread: Optional[threading.Thread] = None
    frontend_server: Optional[Subdir404TCPServer] = None

    def _run_frontend(self):
        web_root = self.app_path / reflex.constants.WEB_DIR / "_static"
        error_page_map = {
            404: web_root / "404.html",
        }
        with Subdir404TCPServer(
            ("", 0),
            SimpleHTTPRequestHandlerCustomErrors,
            root=web_root,
            error_page_map=error_page_map,
        ) as self.frontend_server:
            self.frontend_url = "http://localhost:{1}".format(
                *self.frontend_server.socket.getsockname()
            )
            self.frontend_server.serve_forever()

    def _start_frontend(self):
        # Set up the frontend.
        with chdir(self.app_path):
            config = reflex.config.get_config()
            config.api_url = "http://{0}:{1}".format(
                *self._poll_for_servers().getsockname(),
            )
            reflex.reflex.export(
                zipping=False,
                frontend=True,
                backend=False,
                loglevel=reflex.constants.LogLevel.INFO,
            )

        self.frontend_thread = threading.Thread(target=self._run_frontend)
        self.frontend_thread.start()

    def _wait_frontend(self):
        self._poll_for(lambda: self.frontend_server is not None)
        if self.frontend_server is None or not self.frontend_server.socket.fileno():
            raise RuntimeError("Frontend did not start")

    def _start_backend(self):
        if self.app_instance is None:
            raise RuntimeError("App was not initialized.")
        os.environ[reflex.constants.SKIP_COMPILE_ENV_VAR] = "yes"
        self.backend = uvicorn.Server(
            uvicorn.Config(
                app=self.app_instance,
                host="127.0.0.1",
                port=0,
                workers=reflex.utils.processes.get_num_workers(),
            ),
        )
        self.backend_thread = threading.Thread(target=self.backend.run)
        self.backend_thread.start()

    def _poll_for_servers(self, timeout: TimeoutType = None) -> socket.socket:
        try:
            return super()._poll_for_servers(timeout)
        finally:
            os.environ.pop(reflex.constants.SKIP_COMPILE_ENV_VAR, None)

    def stop(self):
        """Stop the frontend python webserver."""
        super().stop()
        if self.frontend_server is not None:
            self.frontend_server.shutdown()
        if self.frontend_thread is not None:
            self.frontend_thread.join()
