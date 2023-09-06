"""Stub file for button.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Union, overload, Optional, List
from reflex.components.component import Component
from reflex.components.libs.chakra import ChakraComponent
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventHandler, EventChain, EventSpec

class Button(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, icon_spacing: Optional[Union[Var[int], int]] = None, is_active: Optional[Union[Var[bool], bool]] = None, is_disabled: Optional[Union[Var[bool], bool]] = None, is_full_width: Optional[Union[Var[bool], bool]] = None, is_loading: Optional[Union[Var[bool], bool]] = None, loading_text: Optional[Union[Var[str], str]] = None, size: Optional[Union[Var[str], str]] = None, variant: Optional[Union[Var[str], str]] = None, color_scheme: Optional[Union[Var[str], str]] = None, type_: Optional[Union[Var[str], str]] = None, invalid_children: Optional[List[str]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "Button":  # type: ignore
        """Create the component.

               Args:
                   *children: The children of the component.
                   icon_spacing: The space between the button icon and label.
                   is_active: If true, the button will be styled in its active state.
                   is_disabled: If true, the button will be styled in its disabled state.
                   is_full_width: If true, the button will take up the full width of its container.
                   is_loading: If true, the button will show a spinner.
                   loading_text: The label to show in the button when isLoading is true If no text is passed, it only shows the spinner.
                   size: "lg" | "md" | "sm" | "xs"
                   variant: "ghost" | "outline" | "solid" | "link" | "unstyled"
                   color_scheme: Built in color scheme for ease of use.
        Options:
        "whiteAlpha" | "blackAlpha" | "gray" | "red" | "orange" | "yellow" | "green" | "teal" | "blue" | "cyan"
        | "purple" | "pink" | "linkedin" | "facebook" | "messenger" | "whatsapp" | "twitter" | "telegram"
                   type_: The type of button.
                   invalid_children: Components that are not allowed as children.
                   **props: The props of the component.

               Returns:
                   The component.

               Raises:
                   TypeError: If an invalid child is passed.
        """
        ...

class ButtonGroup(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, is_attached: Optional[Union[Var[bool], bool]] = None, is_disabled: Optional[Union[Var[bool], bool]] = None, spacing: Optional[Union[Var[int], int]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "ButtonGroup":  # type: ignore
        """Create the component.

        Args:
            *children: The children of the component.
            is_attached: If true, the borderRadius of button that are direct children will be altered to look flushed together.
            is_disabled: If true, all wrapped button will be disabled.
            spacing: The spacing between the buttons.
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...
