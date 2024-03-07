"""A highlight component."""
from typing import Dict, List, Optional

from reflex.components.chakra import ChakraComponent
from reflex.components.tags import Tag
from reflex.vars import Var


class Highlight(ChakraComponent):
    """Highlights a specific part of a string."""

    tag: str = "Highlight"

    # A query for the text to highlight. Can be a string or a list of strings.
    query: Optional[Var[List[str]]] = None

    # The style of the content.
    # Note: styles and style are different prop.
    styles: Var[Dict] = {"px": "2", "py": "1", "rounded": "full", "bg": "teal.100"}  # type: ignore

    def _render(self) -> Tag:
        return super()._render().add_props(styles=self.style)
