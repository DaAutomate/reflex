"""Handle styling."""

from __future__ import annotations

from typing import Any

from reflex import constants
from reflex.event import EventChain
from reflex.utils import format
from reflex.utils.imports import ImportVar
from reflex.vars import BaseVar, Var, VarData

VarData.update_forward_refs()
color_mode_var_data = VarData(
    imports={
        f"/{constants.Dirs.CONTEXTS_PATH}": {ImportVar(tag="ColorModeContext")},
    },
    hooks={
        f"const [ {{{constants.ColorMode.NAME}}}, {{{constants.ColorMode.TOGGLE}}} ] = useContext(ColorModeContext)",
    },
)
color_mode = BaseVar(
    _var_name=constants.ColorMode.NAME,
    _var_type="str",
    _var_data=color_mode_var_data,
)
toggle_color_mode = BaseVar(
    _var_name=constants.ColorMode.TOGGLE,
    _var_type=EventChain,
    _var_data=color_mode_var_data,
)


def convert(style_dict):
    """Format a style dictionary.

    Args:
        style_dict: The style dictionary to format.

    Returns:
        The formatted style dictionary.
    """
    var_data = None
    out = {}
    for key, value in style_dict.items():
        key = format.to_camel_case(key)
        if isinstance(value, dict):
            out[key], new_var_data = convert(value)
        else:
            new_var = Var.create(value, _var_is_string=True)
            out[key] = str(new_var)
            new_var_data = new_var._var_data
        var_data = VarData.merge(var_data, new_var_data)
    return out, var_data


class Style(dict):
    """A style dictionary."""

    def __init__(self, style_dict: dict | None = None):
        """Initialize the style.

        Args:
            style_dict: The style dictionary.
        """
        style_dict, self._var_data = convert(style_dict or {})
        super().__init__(style_dict)

    def update(self, style_dict: dict | None, **kwargs):
        """Update the style.

        Args:
            style_dict: The style dictionary.
            kwargs: Other key value pairs to apply to the dict update.
        """
        if kwargs:
            style_dict = {**style_dict, **kwargs}
        converted_dict = type(self)(style_dict)
        self._var_data = VarData.merge(self._var_data, converted_dict._var_data)
        super().update(converted_dict)

    def __setitem__(self, key: str, value: Any):
        """Set an item in the style.

        Args:
            key: The key to set.
            value: The value to set.
        """
        _var = Var.create(value)
        self._var_data = VarData.merge(self._var_data, _var._var_data)
        super().__setitem__(key, value)
