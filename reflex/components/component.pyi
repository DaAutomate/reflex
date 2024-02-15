"""Stub file for reflex/components/component.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
import copy
import typing
from abc import ABC, abstractmethod
from functools import lru_cache, wraps
from hashlib import md5
from types import SimpleNamespace
from typing import (
    Any,
    Callable,
    ClassVar,
    Dict,
    Iterator,
    List,
    Optional,
    Set,
    Type,
    Union,
)
from reflex.base import Base
from reflex.compiler.templates import STATEFUL_COMPONENT
from reflex.components.tags import Tag
from reflex.constants import (
    Dirs,
    EventTriggers,
    Hooks,
    Imports,
    MemoizationDisposition,
    MemoizationMode,
    PageNames,
)
from reflex.event import (
    EventChain,
    EventHandler,
    EventSpec,
    call_event_fn,
    call_event_handler,
    get_handler_args,
)
from reflex.style import Style, format_as_emotion
from reflex.utils import console, format, imports, types
from reflex.utils.imports import ImportVar
from reflex.utils.serializers import serializer
from reflex.vars import BaseVar, Var, VarData

class BaseComponent(Base, ABC):
    children: List[BaseComponent]
    library: Optional[str]
    lib_dependencies: List[str]
    tag: Optional[str]

    @abstractmethod
    def render(self) -> dict: ...
    @abstractmethod
    def get_hooks(self) -> set[str]: ...
    @abstractmethod
    def get_imports(self) -> imports.ImportDict: ...
    @abstractmethod
    def get_dynamic_imports(self) -> set[str]: ...
    @abstractmethod
    def get_custom_code(self) -> set[str]: ...
    @abstractmethod
    def get_refs(self) -> set[str]: ...

class ComponentNamespace(SimpleNamespace): ...

def evaluate_style_namespaces(style: ComponentStyle) -> dict: ...

ComponentStyle = Dict[
    Union[str, Type[BaseComponent], Callable, ComponentNamespace], Any
]
ComponentChild = Union[types.PrimitiveType, Var, BaseComponent]

class Component(BaseComponent, ABC):
    style: Style
    event_triggers: Dict[str, Union[EventChain, Var]]
    alias: Optional[str]
    is_default: Optional[bool]
    key: Any
    id: Any
    class_name: Any
    special_props: Set[Var]
    autofocus: bool
    custom_attrs: Dict[str, Union[Var, str]]

    def get_event_triggers(self) -> Dict[str, Any]: ...
    def apply_theme(self, theme: Optional[Component]): ...
    @classmethod
    @lru_cache(maxsize=None)
    def get_props(cls) -> Set[str]: ...
    @classmethod
    @lru_cache(maxsize=None)
    def get_initial_props(cls) -> Set[str]: ...
    @classmethod
    @lru_cache(maxsize=None)
    def get_component_props(cls) -> set[str]: ...
    @classmethod
    def create(cls, *children, **props) -> Component: ...  # type: ignore
    def add_style(self, style: ComponentStyle) -> Component: ...
    def render(self) -> Dict: ...
    def get_custom_code(self) -> Set[str]: ...
    def get_dynamic_imports(self) -> Set[str]: ...
    def get_imports(self) -> imports.ImportDict: ...
    def get_hooks(self) -> Set[str]: ...
    def get_ref(self) -> str | None: ...
    def get_refs(self) -> Set[str]: ...
    def get_custom_components(
        self, seen: set[str] | None = None
    ) -> Set[CustomComponent]: ...
    @property
    def import_var(self): ...
    def get_app_wrap_components(self) -> dict[tuple[int, str], Component]: ...

class CustomComponent(Component):
    @classmethod
    def get_props(cls) -> Set[str]: ...
    def get_custom_components(
        self, seen: set[str] | None = None
    ) -> Set[CustomComponent]: ...
    def get_prop_vars(self) -> List[BaseVar]: ...
    @lru_cache(maxsize=None)
    def get_component(self) -> Component: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        component_fn: Optional[Callable[..., Component]] = None,
        props: Optional[Dict[str, Any]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "CustomComponent":
        """Create the component.

        Args:
            *children: The children of the component.
            component_fn: Use the components library.  The function that creates the component.
            props: The props of the component.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...

def custom_component(
    component_fn: Callable[..., Component]
) -> Callable[..., CustomComponent]: ...

memo = custom_component

class NoSSRComponent(Component):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "NoSSRComponent":
        """Create the component.

        Args:
            *children: The children of the component.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...

@serializer
def serialize_component(comp: Component): ...

class StatefulComponent(BaseComponent):
    tag_to_stateful_component: ClassVar[Dict[str, StatefulComponent]] = {}
    component: Component
    code: str
    references: int
    rendered_as_shared: bool

    @classmethod
    def create(cls, component: Component) -> StatefulComponent | None: ...  # type: ignore
    def get_hooks(self) -> set[str]: ...
    def get_imports(self) -> imports.ImportDict: ...
    def get_dynamic_imports(self) -> set[str]: ...
    def get_custom_code(self) -> set[str]: ...
    def get_refs(self) -> set[str]: ...
    def render(self) -> dict: ...
    @classmethod
    def compile_from(cls, component: BaseComponent) -> BaseComponent: ...

class MemoizationLeaf(Component):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "MemoizationLeaf":
        """Create a new memoization leaf component.

        Args:
            *children: The children of the component.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The memoization leaf
        """
        ...
