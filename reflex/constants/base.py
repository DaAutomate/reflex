"""Base file for constants that don't fit any other categories."""

from __future__ import annotations

import os
import platform
from enum import Enum
from types import SimpleNamespace

from platformdirs import PlatformDirs

# importlib is only available for Python 3.8+ so we need the backport for Python 3.7
try:
    from importlib import metadata
except ImportError:
    import importlib_metadata as metadata  # pyright: ignore[reportMissingImports]


IS_WINDOWS = platform.system() == "Windows"


class DIRS(SimpleNamespace):
    """Various directories/paths used by Reflex."""

    # The frontend directories in a project.
    # The web folder where the NextJS app is compiled to.
    WEB = ".web"
    # The name of the assets directory.
    APP_ASSETS = "assets"
    # The name of the utils file.
    UTILS = "utils"
    # The name of the output static directory.
    STATIC = "_static"
    # The name of the state file.
    STATE_PATH = "/".join([UTILS, "state"])
    # The name of the components file.
    COMPONENTS_PATH = "/".join([UTILS, "components"])
    # The directory where the app pages are compiled to.
    WEB_PAGES = os.path.join(WEB, "pages")
    # The directory where the static build is located.
    WEB_STATIC = os.path.join(WEB, STATIC)
    # The directory where the utils file is located.
    WEB_UTILS = os.path.join(WEB, UTILS)
    # The directory where the assets are located.
    WEB_ASSETS = os.path.join(WEB, "public")
    # The env json file.
    ENV_JSON = os.path.join(WEB, "env.json")


class REFLEX(SimpleNamespace):
    """Base constants concerning Reflex."""

    # App names and versions.
    # The name of the Reflex package.
    MODULE_NAME = "reflex"
    # The current version of Reflex.
    VERSION = metadata.version(MODULE_NAME)

    # The reflex json file.
    JSON = os.path.join(DIRS.WEB, "reflex.json")

    # Files and directories used to init a new project.
    # The directory to store reflex dependencies.
    DIR = (
        # on windows, we use C:/Users/<username>/AppData/Local/reflex.
        # on macOS, we use ~/Library/Application Support/reflex.
        # on linux, we use ~/.local/share/reflex.
        PlatformDirs(MODULE_NAME, False).user_data_dir
    )
    # The root directory of the reflex library.

    ROOT_DIR = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )


class TEMPLATE(SimpleNamespace):
    """Constants related to Templates."""

    class KIND(str, Enum):
        """The templates to use for the app."""

        DEFAULT = "default"
        COUNTER = "counter"

    class DIR(SimpleNamespace):
        """Folders used by the template system of Reflex."""

        # The template directory used during reflex init.
        BASE = os.path.join(REFLEX.ROOT_DIR, REFLEX.MODULE_NAME, ".templates")
        # The web subdirectory of the template directory.
        WEB_TEMPLATE = os.path.join(BASE, "web")
        # The assets subdirectory of the template directory.
        ASSETS_TEMPLATE = os.path.join(BASE, DIRS.APP_ASSETS)
        # The jinja template directory.
        JINJA_TEMPLATE = os.path.join(BASE, "jinja")


class NEXT(SimpleNamespace):
    """Constants related to NextJS."""

    # The NextJS config file
    CONFIG_FILE = "next.config.js"
    # The sitemap config file.
    SITEMAP_CONFIG_FILE = os.path.join(DIRS.WEB, "next-sitemap.config.js")
    # The node modules directory.
    NODE_MODULES = "node_modules"
    # The package lock file.
    PACKAGE_LOCK = "package-lock.json"


# Color mode variables
class COLOR_MODE(SimpleNamespace):
    """Constants related to ColorMode."""

    NAME = "colorMode"
    USE = "useColorMode"
    TOGGLE = "toggleColorMode"


# Env modes
class ENV(str, Enum):
    """The environment modes."""

    DEV = "dev"
    PROD = "prod"


# Log levels
class LOG_LEVEL(str, Enum):
    """The log levels."""

    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

    def __le__(self, other: LOG_LEVEL) -> bool:
        """Compare log levels.

        Args:
            other: The other log level.

        Returns:
            True if the log level is less than or equal to the other log level.
        """
        levels = list(LOG_LEVEL)
        return levels.index(self) <= levels.index(other)


# Server socket configuration variables
POLLING_MAX_HTTP_BUFFER_SIZE = 1000 * 1000


class PING(SimpleNamespace):
    """PING constants."""

    # The 'ping' interval
    INTERVAL = 25
    # The 'ping' timeout
    TIMEOUT = 120


# Keys in the client_side_storage dict
COOKIES = "cookies"
LOCAL_STORAGE = "local_storage"

# If this env var is set to "yes", App.compile will be a no-op
SKIP_COMPILE_ENV_VAR = "__REFLEX_SKIP_COMPILE"

# Testing variables.
# Testing os env set by pytest when running a test case.
PYTEST_CURRENT_TEST = "PYTEST_CURRENT_TEST"
