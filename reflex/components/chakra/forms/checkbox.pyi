"""Stub file for reflex/components/chakra/forms/checkbox.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
import reflex
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from reflex.components.chakra import ChakraComponent, LiteralColorScheme, LiteralTagSize
from reflex.event import EventHandler
from reflex.vars import Var

class Checkbox(ChakraComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        color_scheme: Optional[
            Union[
                reflex.vars.Var[
                    Literal[
                        "none",
                        "gray",
                        "red",
                        "orange",
                        "yellow",
                        "green",
                        "teal",
                        "blue",
                        "cyan",
                        "purple",
                        "pink",
                        "whiteAlpha",
                        "blackAlpha",
                        "linkedin",
                        "facebook",
                        "messenger",
                        "whatsapp",
                        "twitter",
                        "telegram",
                    ]
                ],
                Literal[
                    "none",
                    "gray",
                    "red",
                    "orange",
                    "yellow",
                    "green",
                    "teal",
                    "blue",
                    "cyan",
                    "purple",
                    "pink",
                    "whiteAlpha",
                    "blackAlpha",
                    "linkedin",
                    "facebook",
                    "messenger",
                    "whatsapp",
                    "twitter",
                    "telegram",
                ],
            ]
        ] = None,
        size: Optional[
            Union[reflex.vars.Var[Literal["sm", "md", "lg"]], Literal["sm", "md", "lg"]]
        ] = None,
        is_checked: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        is_disabled: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        is_focusable: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        is_indeterminate: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        is_invalid: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        is_read_only: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        is_required: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        name: Optional[Union[reflex.vars.Var[str], str]] = None,
        value: Optional[Union[reflex.vars.Var[str], str]] = None,
        spacing: Optional[Union[reflex.vars.Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_change: Optional[
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
    ) -> "Checkbox":
        """Create the component.

        Args:
            *children: The children of the component.
            color_scheme: Color scheme for checkbox.  Options:  "whiteAlpha" | "blackAlpha" | "gray" | "red" | "orange" | "yellow" | "green" | "teal" | "blue" | "cyan"  | "purple" | "pink" | "linkedin" | "facebook" | "messenger" | "whatsapp" | "twitter" | "telegram"
            size: "sm" | "md" | "lg"
            is_checked: If true, the checkbox will be checked.
            is_disabled: If true, the checkbox will be disabled
            is_focusable: If true and is_disabled is passed, the checkbox will remain tabbable but not interactive
            is_indeterminate: If true, the checkbox will be indeterminate. This only affects the icon shown inside checkbox and does not modify the is_checked var.
            is_invalid: If true, the checkbox is marked as invalid. Changes style of unchecked state.
            is_read_only: If true, the checkbox will be readonly
            is_required: If true, the checkbox input is marked as required, and required attribute will be added
            name: The name of the input field in a checkbox (Useful for form submission).
            value: The value of the input field when checked (use is_checked prop for a bool)
            spacing: The spacing between the checkbox and its label text (0.5rem)
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

class CheckboxGroup(ChakraComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        value: Optional[Union[reflex.vars.Var[str], str]] = None,
        default_value: Optional[Union[reflex.vars.Var[str], str]] = None,
        is_disabled: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        is_native: Optional[Union[reflex.vars.Var[bool], bool]] = None,
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
    ) -> "CheckboxGroup":
        """Create the component.

        Args:
            *children: The children of the component.
            value: The value of the checkbox group
            default_value: The initial value of the checkbox group
            is_disabled: If true, all wrapped checkbox inputs will be disabled
            is_native: If true, input elements will receive checked attribute instead of isChecked. This assumes, you're using native radio inputs
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...
