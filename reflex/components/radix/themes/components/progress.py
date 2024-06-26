"""Progress from Radix Themes."""

from typing import Literal

from reflex.components.component import Component
from reflex.vars import Var

from ..base import LiteralAccentColor, RadixThemesComponent


class Progress(RadixThemesComponent):
    """A progress bar component."""

    tag = "Progress"

    # The value of the progress bar: 0 to max (default 100)
    value: Var[int]

    # The maximum progress value.
    max: Var[int]

    # The size of the progress bar: "1" | "2" | "3"
    size: Var[Literal["1", "2", "3"]]

    # The variant of the progress bar: "classic" | "surface" | "soft"
    variant: Var[Literal["classic", "surface", "soft"]]

    # The color theme of the progress bar
    color_scheme: Var[LiteralAccentColor]

    # Whether to render the progress bar with higher contrast color against background
    high_contrast: Var[bool]

    # Override theme radius for progress bar: "none" | "small" | "medium" | "large" | "full"
    radius: Var[Literal["none", "small", "medium", "large", "full"]]

    # The duration of the progress bar animation. Once the duration times out, the progress bar will start an indeterminate animation.
    duration: Var[str]

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create a Progress component.

        Args:
            *children: The children of the component.
            **props: The properties of the component.

        Returns:
            The Progress Component.

        """
        props.setdefault("width", "100%")
        return super().create(*children, **props)


progress = Progress.create
