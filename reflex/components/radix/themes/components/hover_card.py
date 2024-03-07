"""Interactive components provided by @radix-ui/themes."""
from typing import Any, Dict, Literal, Optional

from reflex import el
from reflex.components.component import ComponentNamespace
from reflex.constants import EventTriggers
from reflex.vars import Var

from ..base import (
    RadixThemesComponent,
    RadixThemesTriggerComponent,
)


class HoverCardRoot(RadixThemesComponent):
    """For sighted users to preview content available behind a link."""

    tag: str = "HoverCard.Root"

    # The open state of the hover card when it is initially rendered. Use when you do not need to control its open state.
    default_open: Optional[Var[bool]] = None

    # The controlled open state of the hover card. Must be used in conjunction with onOpenChange.
    open: Optional[Var[bool]] = None

    # The duration from when the mouse enters the trigger until the hover card opens.
    open_delay: Optional[Var[int]] = None

    # The duration from when the mouse leaves the trigger until the hover card closes.
    close_delay: Optional[Var[int]] = None

    def get_event_triggers(self) -> Dict[str, Any]:
        """Get the events triggers signatures for the component.

        Returns:
            The signatures of the event triggers.
        """
        return {
            **super().get_event_triggers(),
            EventTriggers.ON_OPEN_CHANGE: lambda e0: [e0],
        }


class HoverCardTrigger(RadixThemesTriggerComponent):
    """Wraps the link that will open the hover card."""

    tag: str = "HoverCard.Trigger"


class HoverCardContent(el.Div, RadixThemesComponent):
    """Contains the content of the open hover card."""

    tag: str = "HoverCard.Content"

    # The preferred side of the trigger to render against when open. Will be reversed when collisions occur and avoidCollisions is enabled.
    side: Optional[Var[Literal["top", "right", "bottom", "left"]]] = None

    # The distance in pixels from the trigger.
    side_offset: Optional[Var[int]] = None

    # The preferred alignment against the trigger. May change when collisions occur.
    align: Optional[Var[Literal["start", "center", "end"]]] = None

    # Whether or not the hover card should avoid collisions with its trigger.
    avoid_collisions: Optional[Var[bool]] = None


class HoverCard(ComponentNamespace):
    """For sighted users to preview content available behind a link."""

    root = __call__ = staticmethod(HoverCardRoot.create)
    trigger = staticmethod(HoverCardTrigger.create)
    content = staticmethod(HoverCardContent.create)


hover_card = HoverCard()
