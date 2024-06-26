"""Next.js script wrappers and inline script functionality.

https://nextjs.org/docs/app/api-reference/components/script
"""

from __future__ import annotations

from reflex.components.component import Component
from reflex.event import EventHandler
from reflex.vars import Var


class Script(Component):
    """Next.js script component.

    Note that this component differs from reflex.components.base.document.NextScript
    in that it is intended for use with custom and user-defined scripts.

    It also differs from reflex.components.base.link.ScriptTag, which is the plain
    HTML <script> tag which does not work when rendering a component.
    """

    library = "next/script"
    tag = "Script"
    is_default = True

    # Required unless inline script is used
    src: Var[str]

    # When the script will execute: afterInteractive | beforeInteractive | lazyOnload
    strategy: Var[str] = "afterInteractive"  # type: ignore

    # Triggered when the script is loading
    on_load: EventHandler[lambda: []]

    # Triggered when the script has loaded
    on_ready: EventHandler[lambda: []]

    # Triggered when the script has errored
    on_error: EventHandler[lambda: []]

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create an inline or user-defined script.

        If a string is provided as the first child, it will be rendered as an inline script
        otherwise the `src` prop must be provided.

        The following event triggers are provided:

        on_load: Execute code after the script has finished loading.
        on_ready: Execute code after the script has finished loading and every
            time the component is mounted.
        on_error: Execute code if the script fails to load.

        Args:
            *children: The children of the component.
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            ValueError: when neither children nor `src` are specified.

        """
        if not children and not props.get("src"):
            raise ValueError("Must provide inline script or `src` prop.")
        return super().create(*children, **props)


script = Script.create
