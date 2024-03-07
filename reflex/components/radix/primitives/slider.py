"""Radix slider components."""
from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional

from reflex.components.component import Component, ComponentNamespace
from reflex.components.radix.primitives.base import RadixPrimitiveComponentWithClassName
from reflex.style import Style
from reflex.vars import Var

LiteralSliderOrientation = Literal["horizontal", "vertical"]
LiteralSliderDir = Literal["ltr", "rtl"]


class SliderComponent(RadixPrimitiveComponentWithClassName):
    """Base class for all @radix-ui/react-slider components."""

    library: str = "@radix-ui/react-slider@^1.1.2"


class SliderRoot(SliderComponent):
    """The Slider component comtaining all slider parts."""

    tag: str = "Root"
    alias: str = "RadixSliderRoot"

    default_value: Optional[Var[List[int]]] = None

    value: Optional[Var[List[int]]] = None

    name: Optional[Var[str]] = None

    disabled: Optional[Var[bool]] = None

    orientation: Optional[Var[LiteralSliderOrientation]] = None

    dir: Optional[Var[LiteralSliderDir]] = None

    inverted: Optional[Var[bool]] = None

    min: Optional[Var[int]] = None

    max: Optional[Var[int]] = None

    step: Optional[Var[int]] = None

    min_steps_between_thumbs: Optional[Var[int]] = None

    def get_event_triggers(self) -> Dict[str, Any]:
        """Event triggers for radix slider primitive.

        Returns:
            The triggers for event supported by radix primitives.
        """
        return {
            **super().get_event_triggers(),
            "on_value_change": lambda e0: [e0],  # trigger for all change of a thumb
            "on_value_commit": lambda e0: [e0],  # trigger when thumb is released
        }

    def _apply_theme(self, theme: Component):
        self.style = Style(
            {
                "position": "relative",
                "display": "flex",
                "align_items": "center",
                "user_select": "none",
                "touch_action": "none",
                "width": "200px",
                "height": "20px",
                "&[data-orientation='vertical']": {
                    "flex_direction": "column",
                    "width": "20px",
                    "height": "100px",
                },
                **self.style,
            }
        )


class SliderTrack(SliderComponent):
    """A Slider Track component."""

    tag: str = "Track"
    alias: str = "RadixSliderTrack"

    def _apply_theme(self, theme: Component):
        self.style = Style(
            {
                "position": "relative",
                "flex_grow": "1",
                "background_color": "black",
                "border_radius": "9999px",
                "height": "3px",
                "&[data-orientation='vertical']": {
                    "width": "3px",
                },
                **self.style,
            }
        )


class SliderRange(SliderComponent):
    """A SliderRange component."""

    tag: str = "Range"
    alias: str = "RadixSliderRange"

    def _apply_theme(self, theme: Component):
        self.style = Style(
            {
                "position": "absolute",
                "background_color": "white",
                "height": "100%",
                "&[data-orientation='vertical']": {
                    "width": "100%",
                },
                **self.style,
            }
        )


class SliderThumb(SliderComponent):
    """A SliderThumb component."""

    tag: str = "Thumb"
    alias: str = "RadixSliderThumb"

    def _apply_theme(self, theme: Component):
        self.style = Style(
            {
                "display": "block",
                "width": "20px",
                "height": "20px",
                "background_color": "black",
                "box_shadow": "0 2px 10px black",
                "border_radius": "10px",
                "&:hover": {
                    "background_color": "gray",
                },
                "&:focus": {
                    "outline": "none",
                    "box_shadow": "0 0 0 4px gray",
                },
                **self.style,
            }
        )


class Slider(ComponentNamespace):
    """High level API for slider."""

    root = staticmethod(SliderRoot.create)
    track = staticmethod(SliderTrack.create)
    range = staticmethod(SliderRange.create)
    thumb = staticmethod(SliderThumb.create)

    @staticmethod
    def __call__(**props) -> Component:
        """High level API for slider.

        Args:
            **props: The props of the slider.

        Returns:
            A slider component.
        """
        track = SliderTrack.create(SliderRange.create())
        # if default_value is not set, the thumbs will not render properly but the slider will still work
        if "default_value" in props:
            children = [
                track,
                *[SliderThumb.create() for _ in props.get("default_value", [])],
            ]
        else:
            children = [
                track,
                #     Foreach.create(props.get("value"), lambda e: SliderThumb.create()),  # foreach doesn't render Thumbs properly
            ]

        return SliderRoot.create(*children, **props)


slider = Slider()
