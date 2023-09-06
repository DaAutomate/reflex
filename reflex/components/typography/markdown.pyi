"""Stub file for markdown.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import List, Dict, Optional, Callable, Union, overload
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventHandler, EventChain, EventSpec

components_by_tag: Dict[str, Callable]

class Markdown(Component):
    @overload
    @classmethod
    def create(cls, *children, lib_dependencies: Optional[List[str]] = None, custom_styles: Optional[Dict[str, Style]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "Markdown": ...  # type: ignore
