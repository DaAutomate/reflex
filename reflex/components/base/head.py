"""The head component."""

from reflex.components.component import Component, MemoizationLeaf


class NextHeadLib(Component):
    """Header components."""

    library: str = "next/head"


class Head(NextHeadLib, MemoizationLeaf):
    """Head Component."""

    tag: str = "NextHead"

    is_default: bool = True
