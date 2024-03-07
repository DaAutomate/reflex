"""Alert components."""
from typing import Optional

from reflex.components.chakra import (
    ChakraComponent,
    LiteralAlertVariant,
    LiteralStatus,
)
from reflex.components.component import Component
from reflex.vars import Var


class Alert(ChakraComponent):
    """An alert feedback box."""

    tag: str = "Alert"

    # The status of the alert ("success" | "info" | "warning" | "error")
    status: Optional[Var[LiteralStatus]] = None

    # "subtle" | "left-accent" | "top-accent" | "solid"
    variant: Optional[Var[LiteralAlertVariant]] = None

    @classmethod
    def create(
        cls, *children, icon=True, title="Alert title", desc=None, **props
    ) -> Component:
        """Create an alert component.

        Args:
            *children: The children of the component.
            icon: The icon of the alert.
            title: The title of the alert.
            desc: The description of the alert
            **props: The properties of the component.

        Returns:
            The alert component.
        """
        if len(children) == 0:
            children = []

            if icon:
                children.append(AlertIcon.create())

            children.append(AlertTitle.create(title))

            if desc:
                children.append(AlertDescription.create(desc))

        return super().create(*children, **props)


class AlertIcon(ChakraComponent):
    """An icon displayed in the alert."""

    tag: str = "AlertIcon"


class AlertTitle(ChakraComponent):
    """The title of the alert."""

    tag: str = "AlertTitle"


class AlertDescription(ChakraComponent):
    """AlertDescription composes the Box component."""

    tag: str = "AlertDescription"
