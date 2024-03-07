"""Element classes. This is an auto-generated file. Do not edit. See ../generate.py."""
from typing import Optional, Union

from reflex.vars import Var

from .base import BaseHTML


class A(BaseHTML):  # Inherits common attributes from BaseMeta
    """Display the 'a' element."""

    tag: str = "a"

    # Specifies that the target (the file specified in the href attribute) will be downloaded when a user clicks on the hyperlink.
    download: Optional[Var[Union[str, int, bool]]] = None

    # Specifies the URL of the page the link goes to
    href: Optional[Var[Union[str, int, bool]]] = None

    # Specifies the language of the linked document
    href_lang: Optional[Var[Union[str, int, bool]]] = None

    # Specifies what media/device the linked document is optimized for
    media: Optional[Var[Union[str, int, bool]]] = None

    # Specifies which referrer is sent when fetching the resource
    ping: Optional[Var[Union[str, int, bool]]] = None

    # Specifies the relationship between the current document and the linked document
    referrer_policy: Optional[Var[Union[str, int, bool]]] = None

    # Specifies the relationship between the linked document and the current document
    rel: Optional[Var[Union[str, int, bool]]] = None

    # Specifies the shape of the area
    shape: Optional[Var[Union[str, int, bool]]] = None

    # Specifies where to open the linked document
    target: Optional[Var[Union[str, int, bool]]] = None


class Abbr(BaseHTML):
    """Display the abbr element."""

    tag: str = "abbr"


class B(BaseHTML):
    """Display the b element."""

    tag: str = "b"


class Bdi(BaseHTML):
    """Display the bdi element."""

    tag: str = "bdi"


class Bdo(BaseHTML):
    """Display the bdo element."""

    tag: str = "bdo"


class Br(BaseHTML):
    """Display the br element."""

    tag: str = "br"


class Cite(BaseHTML):
    """Display the cite element."""

    tag: str = "cite"


class Code(BaseHTML):
    """Display the code element."""

    tag: str = "code"


class Data(BaseHTML):
    """Display the data element."""

    tag: str = "data"

    # Specifies the machine-readable translation of the data element.
    value: Optional[Var[Union[str, int, bool]]] = None


class Dfn(BaseHTML):
    """Display the dfn element."""

    tag: str = "dfn"


class Em(BaseHTML):
    """Display the em element."""

    tag: str = "em"


class I(BaseHTML):  # noqa: E742
    """Display the i element."""

    tag: str = "i"


class Kbd(BaseHTML):
    """Display the kbd element."""

    tag: str = "kbd"


class Mark(BaseHTML):
    """Display the mark element."""

    tag: str = "mark"


class Q(BaseHTML):
    """Display the q element."""

    tag: str = "q"

    # Specifies the source URL of the quote.
    cite: Optional[Var[Union[str, int, bool]]] = None


class Rp(BaseHTML):
    """Display the rp element."""

    tag: str = "rp"


class Rt(BaseHTML):
    """Display the rt element."""

    tag: str = "rt"


class Ruby(BaseHTML):
    """Display the ruby element."""

    tag: str = "ruby"


class S(BaseHTML):
    """Display the s element."""

    tag: str = "s"


class Samp(BaseHTML):
    """Display the samp element."""

    tag: str = "samp"


class Small(BaseHTML):
    """Display the small element."""

    tag: str = "small"


class Span(BaseHTML):
    """Display the span element."""

    tag: str = "span"


class Strong(BaseHTML):
    """Display the strong element."""

    tag: str = "strong"


class Sub(BaseHTML):
    """Display the sub element."""

    tag: str = "sub"


class Sup(BaseHTML):
    """Display the sup element."""

    tag: str = "sup"


class Time(BaseHTML):
    """Display the time element."""

    tag: str = "time"

    # Specifies the date and/or time of the element.
    date_time: Optional[Var[Union[str, int, bool]]] = None


class U(BaseHTML):
    """Display the u element."""

    tag: str = "u"


class Wbr(BaseHTML):
    """Display the wbr element."""

    tag: str = "wbr"
