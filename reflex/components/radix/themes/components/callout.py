"""Interactive components provided by @radix-ui/themes."""
from typing import Literal, Optional, Union

import reflex as rx
from reflex import el
from reflex.components.component import Component, ComponentNamespace
from reflex.components.lucide.icon import Icon
from reflex.vars import Var

from ..base import (
    LiteralAccentColor,
    RadixThemesComponent,
)

CalloutVariant = Literal["soft", "surface", "outline"]


class CalloutRoot(el.Div, RadixThemesComponent):
    """Groups Icon and Text parts of a Callout."""

    tag: str = "Callout.Root"

    # Change the default rendered element for the one passed as a child, merging their props and behavior.
    as_child: Optional[Var[bool]] = None

    # Size "1" - "3"
    size: Optional[Var[Literal["1", "2", "3"]]] = None

    # Variant of button: "soft" | "surface" | "outline"
    variant: Optional[Var[CalloutVariant]] = None

    # Override theme color for button
    color_scheme: Optional[Var[LiteralAccentColor]] = None

    # Whether to render the button with higher contrast color against background
    high_contrast: Optional[Var[bool]] = None


class CalloutIcon(el.Div, RadixThemesComponent):
    """Provides width and height for the icon associated with the callout."""

    tag: str = "Callout.Icon"


class CalloutText(el.P, RadixThemesComponent):
    """Renders the callout text. This component is based on the p element."""

    tag: str = "Callout.Text"


class Callout(CalloutRoot):
    """A short message to attract user's attention."""

    # The text of the callout.
    text: Optional[Var[str]] = None

    # The icon of the callout.
    icon: Optional[Var[str]] = None

    @classmethod
    def create(cls, text: Union[str, Var[str]], **props) -> Component:
        """Create a callout component.

        Args:
            text: The text of the callout.
            **props: The properties of the component.

        Returns:
            The callout component.
        """
        return CalloutRoot.create(
            (
                CalloutIcon.create(Icon.create(tag=props["icon"]))
                if "icon" in props
                else rx.fragment()
            ),
            CalloutText.create(text),
            **props,
        )


class CalloutNamespace(ComponentNamespace):
    """Callout components namespace."""

    root = staticmethod(CalloutRoot.create)
    icon = staticmethod(CalloutIcon.create)
    text = staticmethod(CalloutText.create)
    __call__ = staticmethod(Callout.create)


callout = CalloutNamespace()
