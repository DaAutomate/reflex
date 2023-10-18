"""Stub file for editor.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

import enum
from typing import Any, Dict, List, Optional, Union, overload
from reflex.base import Base
from reflex.components.component import Component
from reflex.components.component import NoSSRComponent
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventHandler, EventChain, EventSpec

class EditorButtonList(list, enum.Enum): ...
class EditorOptions(Base): ...

class Editor(NoSSRComponent):
    @overload
    @classmethod
    def create(cls, *children, lib_dependencies: Optional[List[str]] = None, lang: Optional[Union[Var[Union[Literal["en", "da", "de", "es", "fr", "ja", "ko", "pt_br", "ru", "zh_cn", "ro", "pl", "ckb", "lv", "se", "ua", "he", "it"], dict]], Union[Literal["en", "da", "de", "es", "fr", "ja", "ko", "pt_br", "ru", "zh_cn", "ro", "pl", "ckb", "lv", "se", "ua", "he", "it"], dict]]] = None, name: Optional[Union[Var[str], str]] = None, default_value: Optional[Union[Var[str], str]] = None, width: Optional[Union[Var[str], str]] = None, height: Optional[Union[Var[str], str]] = None, placeholder: Optional[Union[Var[str], str]] = None, auto_focus: Optional[Union[Var[bool], bool]] = None, set_options: Optional[Union[Var[Dict], Dict]] = None, set_all_plugins: Optional[Union[Var[bool], bool]] = None, set_contents: Optional[Union[Var[str], str]] = None, append_contents: Optional[Union[Var[str], str]] = None, set_default_style: Optional[Union[Var[str], str]] = None, disable: Optional[Union[Var[bool], bool]] = None, hide: Optional[Union[Var[bool], bool]] = None, hide_toolbar: Optional[Union[Var[bool], bool]] = None, disable_toolbar: Optional[Union[Var[bool], bool]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_change: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_copy: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_cut: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_input: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_load: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_paste: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_resize_editor: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, toggle_code_view: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, toggle_full_screen: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "Editor":  # type: ignore
        """Create an instance of Editor. No children allowed.

        Args:
            set_options(Optional[EditorOptions]): Configuration object to further configure the instance.
            **props: Any properties to be passed to the Editor

        Returns:
            An Editor instance.

        Raises:
            ValueError: If set_options is a state Var.
        """
        ...
