"""Markdown component."""

import textwrap
from typing import Callable, Dict, List, Union

from reflex.compiler import utils
from reflex.components.component import Component, Style
from reflex.components.datadisplay.list import ListItem, OrderedList, UnorderedList
from reflex.components.navigation import Link
from reflex.components.tags.tag import Tag
from reflex.components.typography.heading import Heading
from reflex.components.typography.text import Text
from reflex.utils import console, imports, types
from reflex.vars import BaseVar, ImportVar, Var

# Special vars used in the component map.
children_var = Var.create_safe("children", is_local=False)
props_var = Var.create_safe("...props", is_local=False)

# Component Mapping
def get_base_component_map() -> dict[str, Callable]:
    """Get the base component map.

    Returns:
        The base component map.
    """
    from reflex.components.datadisplay.code import Code

    return {
        "h1": lambda value: Heading.create(value, as_="h1", size="2xl"),
        "h2": lambda value: Heading.create(value, as_="h2", size="xl"),
        "h3": lambda value: Heading.create(value, as_="h3", size="lg"),
        "h4": lambda value: Heading.create(value, as_="h4", size="md"),
        "h5": lambda value: Heading.create(value, as_="h5", size="sm"),
        "h6": lambda value: Heading.create(value, as_="h6", size="xs"),
        "p": lambda value: Text.create(value),
        "ul": lambda value: UnorderedList.create(value),  # type: ignore
        "ol": lambda value: OrderedList.create(value),  # type: ignore
        "li": lambda value: ListItem.create(value),
        "a": lambda value: Link.create(value),
        "code": lambda value: Code.create(value),
    }


class Markdown(Component):
    """A markdown component."""

    library = "react-markdown@^8.0.7"

    tag = "ReactMarkdown"

    is_default = True

    # The component map from a tag to a lambda that creates a component.
    component_map: Dict[str, Callable] = {}

    # Custom styles for the markdown (deprecated in v0.2.9).
    custom_styles: Var[Dict[str, Style]]

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create a markdown component.

        Args:
            *children: The children of the component.
            **props: The properties of the component.

        Returns:
            The markdown component.
        """
        assert len(children) == 1 and types._isinstance(
            children[0], Union[str, Var]
        ), "Markdown component must have exactly one child containing the markdown source."

        # Custom styles are deprecated.
        if "custom_styles" in props:
            console.deprecate(
                "rx.markdown custom_styles",
                "Use the component_map prop instead.",
                "0.2.9",
                "0.2.10",
            )

        # Update the base component map with the custom component map.
        component_map = {**get_base_component_map(), **props.pop("component_map", {})}

        # Get the markdown source.
        src = children[0]
        if isinstance(src, str):
            src = textwrap.dedent(src)
        return super().create(src, component_map=component_map, **props)

    def _get_imports(self) -> imports.ImportDict:
        # Import here to avoid circular imports.
        from reflex.components.datadisplay.code import Code, CodeBlock

        imports = super()._get_imports()

        # Special markdown imports.
        imports.update(
            {
                "": {ImportVar(tag="katex/dist/katex.min.css")},
                "rehype-katex@^6.0.3": {ImportVar(tag="rehypeKatex", is_default=True)},
                "remark-math@^5.1.1": {ImportVar(tag="remarkMath", is_default=True)},
                "rehype-raw@^6.1.1": {ImportVar(tag="rehypeRaw", is_default=True)},
                "remark-gfm@^3.0.1": {ImportVar(tag="remarkGfm", is_default=True)},
            }
        )

        # Get the imports for each component.
        for component in self.component_map.values():
            imports = utils.merge_imports(
                imports, component(Var.create("")).get_imports()
            )

        # Get the imports for the code components.
        imports = utils.merge_imports(
            imports, CodeBlock.create(theme="light")._get_imports()
        )
        imports = utils.merge_imports(imports, Code.create()._get_imports())
        return imports

    def format_component(self, tag: str) -> str:
        """Format a component for rendering in the component map.

        Args:
            tag: The tag of the component.

        Returns:
            The formatted component.
        """
        comp = self.component_map[tag]
        return str(
            comp(children_var)
            .set(special_props={props_var})
            .add_style(self.custom_attrs.get(tag, {}))
        ).replace("\n", " ")

    def format_component_map(self) -> dict[str, str]:
        """Format the component map for rendering.

        Returns:
            The formatted component map.
        """
        # Import here to avoid circular imports.
        from reflex.components.datadisplay.code import CodeBlock

        components = {
            tag: f"{{({{{children_var.name}, {props_var.name}}}) => {self.format_component(tag)}}}"
            for tag in self.component_map
        }
        components[
            "code"
        ] = f"""{{({{node, inline, className, children, ...props}}) => {{
    const match = (className || '').match(/language-(?<lang>.*)/);
    return !inline ? (
        <{CodeBlock().tag}
        children={{String(children)}}
        language={{match ? match[1] : ''}}
        style={{light}}
        {{...props}}
        />
    ) : (
        {self.format_component("code")}
    );
      }}}}""".replace(
            "\n", " "
        )
        return components

    def _render(self) -> Tag:
        # Get the component map.
        component_map = self.format_component_map()

        # Return the tag.
        return (
            super()
            ._render()
            .add_props(
                components=component_map,
                remark_plugins=BaseVar(name="[remarkMath, remarkGfm]", type_=List[str]),
                rehype_plugins=BaseVar(
                    name="[rehypeKatex, rehypeRaw]", type_=List[str]
                ),
            )
            .remove_props("componentMap")
        )
