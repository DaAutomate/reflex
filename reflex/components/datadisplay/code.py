"""A code component."""

from typing import Dict, Optional, Union

from reflex.components.component import Component
from reflex.components.forms import Button
from reflex.components.layout import Box
from reflex.components.libs.chakra import (
    ChakraComponent,
    LiteralCodeBlockTheme,
    LiteralCodeLanguage,
)
from reflex.components.media import Icon
from reflex.event import set_clipboard
from reflex.style import Style
from reflex.utils import format, imports
from reflex.vars import ImportVar, Var


class CodeBlock(Component):
    """A code block."""

    library = "react-syntax-highlighter@15.5.0"

    tag = "PrismAsyncLight"

    alias = "SyntaxHighlighter"

    # The theme to use ("light" or "dark").
    theme: Var[LiteralCodeBlockTheme] = "prism"

    # The language to use.
    language: Var[LiteralCodeLanguage] = "python"

    # If this is enabled line numbers will be shown next to the code block.
    show_line_numbers: Var[bool]

    # The starting line number to use.
    starting_line_number: Var[int]

    # Whether to wrap long lines.
    wrap_long_lines: Var[bool]

    # A custom style for the code block.
    custom_style: Dict[str, str] = {}

    # Props passed down to the code tag.
    code_tag_props: Var[Dict[str, str]]

    def _get_imports(self) -> imports.ImportDict:
        merged_imports = super()._get_imports()
        merged_imports = imports.merge_imports(
            merged_imports,
            {
                f"react-syntax-highlighter/dist/cjs/styles/prism/{self.theme._var_name}": {
                    ImportVar(
                        tag=format.to_camel_case(self.theme._var_name),
                        is_default=True,
                        install=False,
                    )
                }
            },
            {
                f"react-syntax-highlighter/dist/cjs/languages/prism/{self.language._var_name}": {
                    ImportVar(
                        tag=format.to_camel_case(self.language._var_name),
                        is_default=True,
                        install=False,
                    )
                }
            },
        )
        return merged_imports

    def _get_custom_code(self) -> str | None:
        return f"{self.alias}.registerLanguage('{self.language._var_name}', {format.to_camel_case(self.language._var_name)})"

    @classmethod
    def create(
        cls,
        *children,
        can_copy: Optional[bool] = False,
        copy_button: Optional[Union[bool, Component]] = None,
        **props,
    ):
        """Create a text component.

        Args:
            *children: The children of the component.
            can_copy: Whether a copy button should appears.
            copy_button: A custom copy button to override the default one.
            **props: The props to pass to the component.

        Returns:
            The text component.
        """
        # This component handles style in a special prop.
        custom_style = props.pop("custom_style", {})

        # react-syntax-highlighter doesnt have an explicit "light" theme so we use the default
        # prism theme to ensure code compatibility
        if "theme" in props and props["theme"] == "light":
            props["theme"] = "prism"

        if can_copy:
            code = children[0]
            copy_button = (  # type: ignore
                copy_button
                if copy_button is not None
                else Button.create(
                    Icon.create(tag="copy"),
                    on_click=set_clipboard(code),
                    style={"position": "absolute", "top": "0.5em", "right": "0"},
                )
            )
            custom_style.update({"padding": "1em 3.2em 1em 1em"})
        else:
            copy_button = None

        # Transfer style props to the custom style prop.
        for key, value in props.items():
            if key not in cls.get_fields():
                custom_style[key] = value

        # Create the component.
        code_block = super().create(
            *children,
            **props,
            custom_style=Style(custom_style),
        )

        if copy_button:
            return Box.create(code_block, copy_button, position="relative")
        else:
            return code_block

    def _add_style(self, style):
        self.custom_style.update(style)  # type: ignore

    def _render(self):
        out = super()._render()
        out.add_props(
            style=Var.create(
                format.to_camel_case(self.theme._var_name), _var_is_local=False
            )
        ).remove_props("theme")
        return out


class Code(ChakraComponent):
    """Used to display inline code."""

    tag = "Code"
