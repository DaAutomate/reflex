"""Interactive components provided by @radix-ui/themes."""
from typing import List, Literal, Optional

from reflex import el
from reflex.components.component import ComponentNamespace
from reflex.vars import Var

from ..base import (
    RadixThemesComponent,
)


class TableRoot(el.Table, RadixThemesComponent):
    """A semantic table for presenting tabular data."""

    tag: str = "Table.Root"

    # The size of the table: "1" | "2" | "3"
    size: Optional[Var[Literal["1", "2", "3"]]] = None

    # The variant of the table
    variant: Optional[Var[Literal["surface", "ghost"]]] = None


class TableHeader(el.Thead, RadixThemesComponent):
    """The header of the table defines column names and other non-data elements."""

    tag: str = "Table.Header"

    _invalid_children: List[str] = ["TableBody"]

    _valid_parents: List[str] = ["TableRoot"]


class TableRow(el.Tr, RadixThemesComponent):
    """A row containing table cells."""

    tag: str = "Table.Row"

    # The alignment of the row
    align: Optional[Var[Literal["start", "center", "end", "baseline"]]] = None

    _invalid_children: List[str] = ["TableBody", "TableHeader", "TableRow"]


class TableColumnHeaderCell(el.Th, RadixThemesComponent):
    """A table cell that is semantically treated as a column header."""

    tag: str = "Table.ColumnHeaderCell"

    # The justification of the column
    justify: Optional[Var[Literal["start", "center", "end"]]] = None

    _invalid_children: List[str] = [
        "TableBody",
        "TableHeader",
        "TableRow",
        "TableCell",
        "TableColumnHeaderCell",
        "TableRowHeaderCell",
    ]


class TableBody(el.Tbody, RadixThemesComponent):
    """The body of the table contains the data rows."""

    tag: str = "Table.Body"

    _invalid_children: List[str] = [
        "TableHeader",
        "TableRowHeaderCell",
        "TableColumnHeaderCell",
        "TableCell",
    ]

    _valid_parents: List[str] = ["TableRoot"]


class TableCell(el.Td, RadixThemesComponent):
    """A cell containing data."""

    tag: str = "Table.Cell"

    # The justification of the column
    justify: Optional[Var[Literal["start", "center", "end"]]] = None

    _invalid_children: List[str] = [
        "TableBody",
        "TableHeader",
        "TableRowHeaderCell",
        "TableColumnHeaderCell",
        "TableCell",
    ]


class TableRowHeaderCell(el.Th, RadixThemesComponent):
    """A table cell that is semantically treated as a row header."""

    tag: str = "Table.RowHeaderCell"

    # The justification of the column
    justify: Optional[Var[Literal["start", "center", "end"]]] = None

    _invalid_children: List[str] = [
        "TableBody",
        "TableHeader",
        "TableRow",
        "TableCell",
        "TableColumnHeaderCell",
        "TableRowHeaderCell",
    ]


class Table(ComponentNamespace):
    """Table components namespace."""

    root = staticmethod(TableRoot.create)
    header = staticmethod(TableHeader.create)
    body = staticmethod(TableBody.create)
    row = staticmethod(TableRow.create)
    cell = staticmethod(TableCell.create)
    column_header_cell = staticmethod(TableColumnHeaderCell.create)
    row_header_cell = staticmethod(TableRowHeaderCell.create)


table = Table()
