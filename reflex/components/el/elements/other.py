"""Element classes. This is an auto-generated file. Do not edit. See ../generate.py."""
from typing import Optional, Union

from reflex.vars import Var as Var

from .base import BaseHTML


class Details(BaseHTML):
    """Display the details element."""

    tag: str = "details"

    # Indicates whether the details will be visible (expanded) to the user
    open: Optional[Var[Union[str, int, bool]]] = None


class Dialog(BaseHTML):
    """Display the dialog element."""

    tag: str = "dialog"

    # Indicates whether the dialog is active and can be interacted with
    open: Optional[Var[Union[str, int, bool]]] = None


class Summary(BaseHTML):
    """Display the summary element."""

    tag: str = "summary"
    # No unique attributes, only common ones are inherited; used as a summary or caption for a <details> element


class Slot(BaseHTML):
    """Display the slot element."""

    tag: str = "slot"
    # No unique attributes, only common ones are inherited; used as a placeholder inside a web component


class Template(BaseHTML):
    """Display the template element."""

    tag: str = "template"
    # No unique attributes, only common ones are inherited; used for declaring fragments of HTML that can be cloned and inserted in the document


class Math(BaseHTML):
    """Display the math element."""

    tag: str = "math"
    # No unique attributes, only common ones are inherited; used for displaying mathematical expressions


class Html(BaseHTML):
    """Display the html element."""

    tag: str = "html"

    # Specifies the URL of the document's cache manifest (obsolete in HTML5)
    manifest: Optional[Var[Union[str, int, bool]]] = None
