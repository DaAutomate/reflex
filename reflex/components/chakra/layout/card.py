"""Chakra Card component."""
from typing import Optional

from reflex.components.chakra import (
    ChakraComponent,
    LiteralCardVariant,
    LiteralColorScheme,
    LiteralTagSize,
)
from reflex.components.component import Component
from reflex.vars import Var


class CardHeader(ChakraComponent):
    """The wrapper that contains a card's header."""

    tag: str = "CardHeader"


class CardBody(ChakraComponent):
    """The wrapper that houses the card's main content."""

    tag: str = "CardBody"


class CardFooter(ChakraComponent):
    """The footer that houses the card actions."""

    tag: str = "CardFooter"


class Card(ChakraComponent):
    """The parent wrapper that provides context for its children."""

    tag: str = "Card"

    # [required] The flex alignment of the card
    align: Optional[Var[str]] = None

    # [required] The flex direction of the card
    direction: Optional[Var[str]] = None

    # [required] The flex distribution of the card
    justify: Optional[Var[str]] = None

    # The visual color appearance of the component.
    # options: "whiteAlpha" | "blackAlpha" | "gray" | "red" | "orange" | "yellow" |
    #  "green" | "teal" | "blue" | "cyan" | "purple" | "pink" | "linkedin" |
    #  "facebook" | "messenger" | "whatsapp" | "twitter" | "telegram"
    # default: "gray"
    color_scheme: Optional[Var[LiteralColorScheme]] = None

    # The size of the Card
    # options: "sm" | "md" | "lg"
    # default: "md"
    size: Optional[Var[LiteralTagSize]] = None

    # The variant of the Card
    # options: "elevated" | "outline" | "filled" | "unstyled"
    # default: "elevated"
    variant: Optional[Var[LiteralCardVariant]] = None

    @classmethod
    def create(
        cls,
        body: Component,
        *,
        header: Optional[Component] = None,
        footer: Optional[Component] = None,
        **props,
    ) -> Component:
        """Creates a Chakra Card with a body and optionally header and/or footer, and returns it.
        If header, body or footer are not already instances of Chead, Cbody or Cfoot respectively,
        they will be wrapped as such for layout purposes. If you want to modify their props,
        e.g. padding_left, you should wrap them yourself.

        Args:
            body (Component): The main content of the Card that will be created.
            header (Optional[Component]): The header of the Card.
            footer (Optional[Component]): The footer of the Card.
            props: The properties to be passed to the component.

        Returns:
            The `create()` method returns a Card object.
        """
        children = []
        param_to_component_class = (
            (header, CardHeader),
            (body, CardBody),
            (footer, CardFooter),
        )

        for param, component_class in param_to_component_class:
            if isinstance(param, component_class):
                children.append(param)
            elif param is not None:
                children.append(component_class.create(param))

        return super().create(*children, **props)
