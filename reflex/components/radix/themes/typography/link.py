"""Components for rendering heading.
from typing import Optional
https://www.radix-ui.com/themes/docs/theme/typography.
"""
from __future__ import annotations

from typing import Literal, Optional

from reflex.components.component import Component, MemoizationLeaf
from reflex.components.core.cond import cond
from reflex.components.el.elements.inline import A
from reflex.components.next.link import NextLink
from reflex.utils import imports
from reflex.vars import Var

from ..base import (
    LiteralAccentColor,
    RadixThemesComponent,
)
from .base import (
    LiteralTextSize,
    LiteralTextTrim,
    LiteralTextWeight,
)

LiteralLinkUnderline = Literal["auto", "hover", "always"]

next_link = NextLink.create()


class Link(RadixThemesComponent, A, MemoizationLeaf):
    """A semantic element for navigation between pages."""

    tag: str = "Link"

    # Change the default rendered element for the one passed as a child, merging their props and behavior.
    as_child: Optional[Var[bool]] = None

    # Text size: "1" - "9"
    size: Optional[Var[LiteralTextSize]] = None

    # Thickness of text: "light" | "regular" | "medium" | "bold"
    weight: Optional[Var[LiteralTextWeight]] = None

    # Removes the leading trim space: "normal" | "start" | "end" | "both"
    trim: Optional[Var[LiteralTextTrim]] = None

    # Sets the visibility of the underline affordance: "auto" | "hover" | "always"
    underline: Optional[Var[LiteralLinkUnderline]] = None

    # Overrides the accent color inherited from the Theme.
    color_scheme: Optional[Var[LiteralAccentColor]] = None

    # Whether to render the text with higher contrast color
    high_contrast: Optional[Var[bool]] = None

    # If True, the link will open in a new tab
    is_external: Optional[Var[bool]] = None

    def _get_imports(self) -> imports.ImportDict:
        return {**super()._get_imports(), **next_link._get_imports()}

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create a Link component.

        Args:
            *children: The children of the component.
            **props: The props of the component.

        Raises:
            ValueError: in case of missing children

        Returns:
            Component: The link component
        """
        is_external = props.pop("is_external", None)
        if is_external is not None:
            props["target"] = cond(is_external, "_blank", "")
        if props.get("href") is not None:
            if not len(children):
                raise ValueError("Link without a child will not display")
            if "as_child" not in props:
                # Extract props for the NextLink, the rest go to the Link/A element.
                known_next_link_props = NextLink.get_props()
                next_link_props = {}
                for prop in props.copy():
                    if prop in known_next_link_props:
                        next_link_props[prop] = props.pop(prop)
                # If user does not use `as_child`, by default we render using next_link to avoid page refresh during internal navigation
                return super().create(
                    NextLink.create(*children, **next_link_props),
                    as_child=True,
                    **props,
                )
        return super().create(*children, **props)
