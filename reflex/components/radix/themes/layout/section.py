"""Declarative layout and common spacing props."""
from __future__ import annotations

from typing import Literal, Optional

from reflex import el
from reflex.vars import Var

from ..base import RadixThemesComponent

LiteralSectionSize = Literal["1", "2", "3"]


class Section(el.Section, RadixThemesComponent):
    """Denotes a section of page content."""

    tag: str = "Section"

    # The size of the section: "1" - "3" (default "3")
    size: Optional[Var[LiteralSectionSize]] = None
