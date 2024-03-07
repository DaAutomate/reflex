"""A AspectRatio component."""
from typing import Optional

from reflex.components.chakra import ChakraComponent
from reflex.vars import Var


class AspectRatio(ChakraComponent):
    """AspectRatio component is used to embed responsive videos and maps, etc."""

    tag: str = "AspectRatio"

    # The aspect ratio of the Box
    ratio: Optional[Var[float]] = None
