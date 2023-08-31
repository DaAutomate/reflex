"""Stub file for menu.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Optional, List, Union, overload, Set, Any
from reflex.components.libs.chakra import ChakraComponent
from reflex.vars import Var
from reflex.event import EventChain

class Menu(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, button, items, arrow_padding: Optional[Union[Var[int], int]] = None, auto_select: Optional[Union[Var[bool], bool]] = None, boundary: Optional[Union[Var[str], str]] = None, close_on_blur: Optional[Union[Var[bool], bool]] = None, close_on_select: Optional[Union[Var[bool], bool]] = None, default_is_open: Optional[Union[Var[bool], bool]] = None, direction: Optional[Union[Var[str], str]] = None, flip: Optional[Union[Var[bool], bool]] = None, gutter: Optional[Union[Var[int], int]] = None, is_lazy: Optional[Union[Var[bool], bool]] = None, lazy_behavior: Optional[Union[Var[str], str]] = None, is_open: Optional[Union[Var[bool], bool]] = None, match_width: Optional[Union[Var[bool], bool]] = None, placement: Optional[Union[Var[str], str]] = None, prevent_overflow: Optional[Union[Var[bool], bool]] = None, strategy: Optional[Union[Var[str], str]] = None, **props) -> "Menu": ...  # type: ignore

class MenuButton(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, variant: Optional[Union[Var[str], str]] = None, invalid_children: Optional[List[str]] = None, as_: Optional[Union[Var[str], str]] = None, **props) -> "MenuButton": ...  # type: ignore

class MenuList(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "MenuList": ...  # type: ignore

class MenuItem(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, close_on_select: Optional[Union[Var[bool], bool]] = None, command: Optional[Union[Var[str], str]] = None, command_spacing: Optional[Union[Var[int], int]] = None, is_disabled: Optional[Union[Var[bool], bool]] = None, is_focusable: Optional[Union[Var[bool], bool]] = None, **props) -> "MenuItem": ...  # type: ignore

class MenuItemOption(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, close_on_select: Optional[Union[Var[bool], bool]] = None, command: Optional[Union[Var[str], str]] = None, command_spacing: Optional[Union[Var[int], int]] = None, is_checked: Optional[Union[Var[bool], bool]] = None, is_disabled: Optional[Union[Var[bool], bool]] = None, is_focusable: Optional[Union[Var[bool], bool]] = None, type_: Optional[Union[Var[str], str]] = None, value: Optional[Union[Var[str], str]] = None, **props) -> "MenuItemOption": ...  # type: ignore

class MenuGroup(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "MenuGroup": ...  # type: ignore

class MenuOptionGroup(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, type_: Optional[Union[Var[str], str]] = None, value: Optional[Union[Var[str], str]] = None, **props) -> "MenuOptionGroup": ...  # type: ignore

class MenuDivider(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "MenuDivider": ...  # type: ignore
