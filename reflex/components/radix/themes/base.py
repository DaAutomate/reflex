"""Base classes for radix-themes components."""

from __future__ import annotations

from typing import Any, Literal

from reflex.components import Component
from reflex.components.tags import Tag
from reflex.utils import imports
from reflex.vars import Var

LiteralAlign = Literal["start", "center", "end", "baseline", "stretch"]
LiteralJustify = Literal["start", "center", "end", "between"]
LiteralSize = Literal[
    "1", "2", "3", "4", "5", "6", "7", "8", "9", 1, 2, 3, 4, 5, 6, 7, 8, 9
]
LiteralVariant = Literal["classic", "solid", "soft", "surface", "outline", "ghost"]
LiteralAppearance = Literal["inherit", "light", "dark"]
LiteralGrayColor = Literal["gray", "mauve", "slate", "sage", "olive", "sand", "auto"]
LiteralPanelBackground = Literal["solid", "transparent"]
LiteralRadius = Literal["none", "small", "medium", "large", "full"]
LiteralScaling = Literal["90%", "95%", "100%", "105%", "110%"]
LiteralAccentColor = Literal[
    "tomato",
    "red",
    "ruby",
    "crimson",
    "pink",
    "plum",
    "purple",
    "violet",
    "iris",
    "indigo",
    "blue",
    "cyan",
    "teal",
    "jade",
    "green",
    "grass",
    "brown",
    "orange",
    "sky",
    "mint",
    "lime",
    "yellow",
    "amber",
    "gold",
    "bronze",
    "gray",
]


class CommonMarginProps(Component):
    """Many radix-themes elements accept shorthand margin props."""

    # Margin: "0" - "9"
    m: Var[LiteralSize]

    # Margin horizontal: "0" - "9"
    mx: Var[LiteralSize]

    # Margin vertical: "0" - "9"
    my: Var[LiteralSize]

    # Margin top: "0" - "9"
    mt: Var[LiteralSize]

    # Margin right: "0" - "9"
    mr: Var[LiteralSize]

    # Margin bottom: "0" - "9"
    mb: Var[LiteralSize]

    # Margin left: "0" - "9"
    ml: Var[LiteralSize]


class RadixThemesComponent(Component):
    """Base class for all @radix-ui/themes components."""

    library = "@radix-ui/themes@^2.0.0"

    @classmethod
    def create(
        cls,
        *children,
        color: Var[str] = None,  # type: ignore
        color_scheme: Var[LiteralAccentColor] = None,  # type: ignore
        **props,
    ) -> Component:
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            color: map to CSS default color property.
            color_scheme: map to radix color property.
            **props: Component properties.

        Returns:
            A new component instance.
        """
        if color is not None:
            style = props.get("style", {})
            style["color"] = color
            props["style"] = style
        if color_scheme is not None:
            props["color"] = color_scheme
        component = super().create(*children, **props)
        if component.library is None:
            component.library = RadixThemesComponent.__fields__["library"].default
        component.alias = "RadixThemes" + (
            component.tag or component.__class__.__name__
        )
        return component

    @classmethod
    def get_fields(cls) -> dict[str, Any]:
        """Get the pydantic fields for the component.

        Returns:
            Mapping of field name to ModelField instance.
        """
        fields = super().get_fields()
        if "color_scheme" in fields:
            # Treat "color" as a direct prop, so the translation of reflex "color_scheme"
            # to "color" does not put the "color_scheme" value into the "style" prop.
            fields["color"] = fields.pop("color_scheme")
            fields["color"].required = False
        return fields

    @staticmethod
    def _get_app_wrap_components() -> dict[tuple[int, str], Component]:
        return {
            (45, "RadixThemesColorModeProvider"): RadixThemesColorModeProvider.create(),
        }


class Theme(RadixThemesComponent):
    """A theme provider for radix components.

    This should be applied as `App.theme` to apply the theme to all radix
    components in the app with the given settings.

    It can also be used in a normal page to apply specified properties to all
    child elements as an override of the main theme.
    """

    tag = "Theme"

    # Whether to apply the themes background color to the theme node.
    has_background: Var[bool]

    # Override light or dark mode theme: "inherit" | "light" | "dark"
    appearance: Var[LiteralAppearance]

    # The color used for default buttons, typography, backgrounds, etc
    accent_color: Var[LiteralAccentColor]

    # The shade of gray
    gray_color: Var[LiteralGrayColor]

    # Whether panel backgrounds are transparent: "solid" | "transparent" (default)
    panel_background: Var[LiteralPanelBackground]

    # Element border radius: "none" | "small" | "medium" | "large" | "full"
    radius: Var[LiteralRadius]

    # Scale of all theme items: "90%" | "95%" | "100%" | "105%" | "110%"
    scaling: Var[LiteralScaling]

    def _get_imports(self) -> imports.ImportDict:
        return imports.merge_imports(
            super()._get_imports(),
            {
                "": [
                    imports.ImportVar(tag="@radix-ui/themes/styles.css", install=False)
                ],
                "/utils/theme.js": [
                    imports.ImportVar(tag="theme", is_default=True),
                ],
            },
        )

    def _render(self, props: dict[str, Any] | None = None) -> Tag:
        tag = super()._render(props)
        tag.add_props(
            css=Var.create(
                "{{...theme.styles.global[':root'], ...theme.styles.global.body}}",
                _var_is_local=False,
            ),
        )
        return tag


class ThemePanel(RadixThemesComponent):
    """Visual editor for creating and editing themes.

    Include as a child component of Theme to use in your app.
    """

    tag = "ThemePanel"

    default_open: Var[bool]


class RadixThemesColorModeProvider(Component):
    """Next-themes integration for radix themes components."""

    library = "/components/reflex/radix_themes_color_mode_provider.js"
    tag = "RadixThemesColorModeProvider"
    is_default = True


class RadixThemesComponentPropsOverride(Component):
    """Class to override props of radix components."""

    @classmethod
    def create(
        cls,
        *children,
        **props,
    ) -> Component:
        """Create a new component instance.

        Args:
            *children: Child components.
            **props: Component properties.

        Returns:
            A new component instance.
        """
        props = cls._convert_props_to_designated_types(props)
        return super().create(*children, **props)

    @classmethod
    def _get_props_to_convert(cls):
        """Get the list of props whose values we want to
        cast.

        Returns:
            list of props.
        """
        return ["size"]

    @classmethod
    def _convert_props_to_designated_types(
        cls, props: dict[str, Any]
    ) -> dict[str, Any]:
        """Convert the prop values to their designated types(strings
        for this use case).

        We do this to ensure that the radix props that take integer strings
        (eg, "1" instead 1) allow the int representation in the API.

        Args:
            props: The Component's properties.

        """
        for prop in cls._get_props_to_convert():
            if prop in props:
                prop_value = props[prop]
                prop_value = Var.create(prop_value)._replace(_var_type=str)
                props[prop] = prop_value
        return props
