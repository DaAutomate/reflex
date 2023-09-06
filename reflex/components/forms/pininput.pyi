"""Stub file for pininput.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Dict, Optional, Union, overload
from reflex.components.component import Component
from reflex.components.libs.chakra import ChakraComponent
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventHandler, EventChain, EventSpec

class PinInput(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, value: Optional[Union[Var[str], str]] = None, auto_focus: Optional[Union[Var[bool], bool]] = None, default_value: Optional[Union[Var[str], str]] = None, error_border_color: Optional[Union[Var[str], str]] = None, focus_border_color: Optional[Union[Var[str], str]] = None, id_: Optional[Union[Var[str], str]] = None, length: Optional[Union[Var[int], int]] = None, is_disabled: Optional[Union[Var[bool], bool]] = None, is_invalid: Optional[Union[Var[bool], bool]] = None, manage_focus: Optional[Union[Var[bool], bool]] = None, mask: Optional[Union[Var[bool], bool]] = None, placeholder: Optional[Union[Var[str], str]] = None, type_: Optional[Union[Var[str], str]] = None, variant: Optional[Union[Var[str], str]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_complete: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_change: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "PinInput": ...  # type: ignore

class PinInputField(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, index: Optional[Union[Var[int], int]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "PinInputField": ...  # type: ignore
