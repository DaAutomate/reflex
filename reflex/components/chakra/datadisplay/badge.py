"""Badge component."""

from reflex.components.chakra import ChakraComponent, LiteralVariant
from reflex.vars import Var


class Badge(ChakraComponent):
    """A badge component."""

    library = "@chakra-ui/layout@2.3.1"

    tag = "Badge"

    # Variant of the badge ("solid" | "subtle" | "outline")
    variant: Var[LiteralVariant]

    # The color of the badge
    color_scheme: Var[str]
