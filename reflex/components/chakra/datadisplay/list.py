"""List components."""
from __future__ import annotations

from typing import Optional

from reflex.components.chakra import ChakraComponent
from reflex.components.component import Component
from reflex.components.core.foreach import Foreach
from reflex.vars import Var

class List(ChakraComponent):
    """Display a list of items."""

    tag: str = "List"

    # The space between each list item
    spacing: Optional[Var[str]] = None

    # Shorthand prop for listStylePosition
    style_position: Optional[Var[str]] = None

    # Shorthand prop for listStyleType
    style_type: Optional[Var[str]] = None

    @classmethod
    def __class_getitem__(cls, item):
        """This method is just a hacky workaround to stop pydantic v2 from complaining.

        Args:
            item: The type of the list items.

        Returns:
            The list component.
        """
        return cls

    @classmethod
    def create(
        cls, *children, items: list | Var[list] | None = None, **props
    ) -> Component:
        """Create a list component.

        Args:
            *children: The children of the component.
            items: A list of items to add to the list.
            **props: The properties of the component.

        Returns:
            The list component.
        """
        if len(children) == 0:
            if isinstance(items, Var):
                children = [Foreach.create(items, ListItem.create)]
            else:
                children = [ListItem.create(item) for item in items or []]
        return super().create(*children, **props)


class ListItem(ChakraComponent):
    """A single list item."""

    tag: str = "ListItem"


class OrderedList(List):
    """An ordered list component with numbers."""

    tag: str = "OrderedList"


class UnorderedList(List):
    """An unordered list component with bullets."""

    tag: str = "UnorderedList"
