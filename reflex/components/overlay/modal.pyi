"""Stub file for modal.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Union, overload, Set, Optional
from reflex.components.libs.chakra import ChakraComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain

class Modal(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, header: Optional[Union[Component, str]] = None, body: Optional[Union[Component, str]] = None, footer: Optional[Union[Component, str]] = None, close_button: Optional[Component] = None, is_open: Optional[Union[Var[bool], bool]] = None, allow_pinch_zoom: Optional[Union[Var[bool], bool]] = None, auto_focus: Optional[Union[Var[bool], bool]] = None, block_scroll_on_mount: Optional[Union[Var[bool], bool]] = None, close_on_esc: Optional[Union[Var[bool], bool]] = None, close_on_overlay_click: Optional[Union[Var[bool], bool]] = None, is_centered: Optional[Union[Var[bool], bool]] = None, lock_focus_across_frames: Optional[Union[Var[bool], bool]] = None, motion_preset: Optional[Union[Var[str], str]] = None, preserve_scroll_bar_gap: Optional[Union[Var[bool], bool]] = None, return_focus_on_close: Optional[Union[Var[bool], bool]] = None, size: Optional[Union[Var[str], str]] = None, use_inert: Optional[Union[Var[bool], bool]] = None, **props) -> "Modal": ...  # type: ignore

class ModalOverlay(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "ModalOverlay": ...  # type: ignore

class ModalHeader(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "ModalHeader": ...  # type: ignore

class ModalFooter(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "ModalFooter": ...  # type: ignore

class ModalContent(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "ModalContent": ...  # type: ignore

class ModalBody(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "ModalBody": ...  # type: ignore

class ModalCloseButton(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "ModalCloseButton": ...  # type: ignore
