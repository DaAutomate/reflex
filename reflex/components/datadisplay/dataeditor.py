"""Data Editor component from glide-data-grid."""
from __future__ import annotations

from typing import Any, Callable, Dict, List, Literal, Optional, Union

from reflex.base import Base
from reflex.components.component import Component, NoSSRComponent
from reflex.components.literals import LiteralRowMarker
from reflex.utils import console, format, imports, types
from reflex.utils.serializers import serializer
from reflex.vars import ImportVar, Var, get_unique_variable_name

LiteralDataEditorGridColumnIcons = Literal[
    "headerRowID",
    "headerCode",
    "headerNumber",
    "headerString",
    "headerBoolean",
    "headerAudioUri",
    "headerVideoUri",
    "headerEmoji",
    "headerImage",
    "headerUri",
    "headerPhone",
    "headerMarkdown",
    "headerDate",
    "headerTime",
    "headerEmail",
    "headerReference",
    "headerIfThenElse",
    "headerSingleValue",
    "headerLookup",
    "headerTextTemplate",
    "headerMath",
    "headerRollup",
    "headerJoinStrings",
    "headerSplitString",
    "headerGeoDistance",
    "headerArray",
    "rowOwnerOverlay",
    "protectedColumnOverlay",
]
LiteralDataEditorColumnStyle = Literal["normal", "highlight"]


class DataEditorProp(Base):
    """Base class for Data Editor custom prop class."""

    def dict(self) -> dict:
        """Retrieve dict and format keys to camel case.

        Returns:
            Formatted dict.
        """
        res = super().dict()
        return {format.to_camel_case(k): v for k, v in res.items() if v is not None}


class DataEditorTheme(DataEditorProp):
    """The theme for the DataEditor component."""

    accent_color: Optional[str]
    accent_fg: Optional[str]
    accent_light: Optional[str]
    base_font_style: Optional[str]
    bg_bubble: Optional[str]
    bg_bubble_selected: Optional[str]
    bg_cell: Optional[str]
    bg_cell_medium: Optional[str]
    bg_header: Optional[str]
    bg_header_has_focus: Optional[str]
    bg_header_hovered: Optional[str]
    bg_icon_header: Optional[str]
    bg_search_result: Optional[str]
    border_color: Optional[str]
    cell_horizontal_padding: Optional[int]
    cell_vertical_padding: Optional[int]
    drilldown_border: Optional[str]
    editor_font_size: Optional[str]
    fg_icon_header: Optional[str]
    font_family: Optional[str]
    header_bottom_border_color: Optional[str]
    header_font_style: Optional[str]
    horizontal_border_color: Optional[str]
    line_height: Optional[int]
    link_color: Optional[str]
    text_bubble: Optional[str]
    text_dark: Optional[str]
    text_group_header: Optional[str]
    text_header: Optional[str]
    text_header_selected: Optional[str]
    text_light: Optional[str]
    text_medium: Optional[str]


class TrailingRowOptions(DataEditorProp):
    """Trailing Row options."""

    hint: Optional[str]
    add_icon: Optional[str]
    target_column: Optional[int]
    theme_override: Optional[DataEditorTheme]
    disabled: Optional[bool]


class DataEditorColumn(DataEditorProp):
    """Column."""

    title: str
    id: Optional[str]
    type_: str = "str"
    group: Optional[str]
    icon: Optional[LiteralDataEditorGridColumnIcons]
    overlay_icon: Optional[LiteralDataEditorGridColumnIcons]
    has_menu: Optional[bool]
    grow: Optional[int]
    style: Optional[LiteralDataEditorColumnStyle]
    theme_override: Optional[DataEditorTheme]
    trailing_row_options: Optional[TrailingRowOptions]
    grow_offset: Optional[int]


class DataEditor(NoSSRComponent):
    """The DataEditor Component."""

    tag = "DataEditor"
    is_default = True
    library: str = "@glideapps/glide-data-grid@^5.3.0"
    lib_dependencies: List[str] = ["lodash", "marked", "react-responsive-carousel"]

    # Number of rows.
    rows: Var[int]

    # Headers of the columns for the data grid.
    columns: Var[List[DataEditorColumn]]

    # The data.
    data: Var[List[List[Any]]]

    # The name of the callback used to find the data to display.
    get_cell_content: Var[str]

    # Allow selection for copying.
    get_cell_for_selection: Var[bool]

    # Allow paste.
    on_paste: Var[bool]

    # Controls the drawing of the focus ring.
    draw_focus_ring: Var[bool]

    # Enables or disables the overlay shadow when scrolling horizontally.
    fixed_shadow_x: Var[bool]

    # Enables or disables the overlay shadow when scrolling vertically.
    fixed_shadow_y: Var[bool]

    # The number of columns which should remain in place when scrolling horizontally. Doesn't include rowMarkers.
    freeze_columns: Var[int]

    # Controls the header of the group header row.
    group_header_height: Var[int]

    # Controls the height of the header row.
    header_height: Var[int]

    # Additional header icons:
    # header_icons: Var[Any] # (TODO: must be a map of name: svg)

    # The maximum width a column can be automatically sized to.
    max_column_auto_width: Var[int]

    # The maximum width a column can be resized to.
    max_column_width: Var[int]

    # The minimum width a column can be resized to.
    min_column_width: Var[int]

    # Determins the height of each row.
    row_height: Var[int]

    # Kind of row markers.
    row_markers: Var[LiteralRowMarker]

    # Changes the starting index for row markers.
    row_marker_start_index: Var[int]

    # Sets the width of row markers in pixels, if unset row markers will automatically size.
    row_marker_width: Var[int]

    # Enable horizontal smooth scrolling.
    smooth_scroll_x: Var[bool]

    # Enable vertical smooth scrolling.
    smooth_scroll_y: Var[bool]

    # Controls the drawing of the left hand vertical border of a column. If set to a boolean value it controls all borders.
    vertical_border: Var[bool]  # TODO: support a mapping (dict[int, bool])

    # Allow columns selections. ("none", "single", "multiple")
    column_select: Var[str]

    # Prevent diagonal scrolling.
    prevent_diagonal_scrolling: Var[bool]

    # Allow to scroll past the limit of the actual content on the horizontal axis.
    overscroll_x: Var[int]

    # Allow to scroll past the limit of the actual content on the vertical axis.
    overscroll_y: Var[int]

    # Initial scroll offset on the horizontal axis.
    scroll_offset_x: Var[int]

    # Initial scroll offset on the vertical axis.
    scroll_offset_y: Var[int]

    # global theme
    theme: Var[Union[DataEditorTheme, Dict]]

    def _get_imports(self):
        return imports.merge_imports(
            super()._get_imports(),
            {
                "": {
                    ImportVar(
                        tag=f"{format.format_library_name(self.library)}/dist/index.css"
                    )
                },
                self.library: {ImportVar(tag="GridCellKind")},
                "/utils/helpers/dataeditor.js": {
                    ImportVar(
                        tag=f"formatDataEditorCells", is_default=False, install=False
                    ),
                },
            },
        )

    def get_event_triggers(self) -> Dict[str, Callable]:
        """The event triggers of the component.

        Returns:
            The dict describing the event triggers.
        """

        def edit_sig(pos, data: dict[str, Any]):
            return [pos, data]

        return {
            "on_cell_activated": lambda pos: [pos],
            "on_cell_clicked": lambda pos: [pos],
            "on_cell_context_menu": lambda pos: [pos],
            "on_cell_edited": edit_sig,
            "on_group_header_clicked": edit_sig,
            "on_group_header_context_menu": lambda grp_idx, data: [grp_idx, data],
            "on_group_header_renamed": lambda idx, val: [idx, val],
            "on_header_clicked": lambda pos: [pos],
            "on_header_context_menu": lambda pos: [pos],
            "on_header_menu_click": lambda col, pos: [col, pos],
            "on_item_hovered": lambda pos: [pos],
            "on_delete": lambda selection: [selection],
            "on_finished_editing": lambda new_value, movement: [new_value, movement],
            "on_row_appended": lambda: [],
            "on_selection_cleared": lambda: [],
            "on_column_resize": lambda col, width: [col, width],
        }

    def _get_hooks(self) -> str | None:
        # Define the id of the component in case multiple are used in the same page.
        editor_id = get_unique_variable_name()

        # Define the name of the getData callback associated with this component and assign to get_cell_content.
        data_callback = f"getData_{editor_id}"
        self.get_cell_content = Var.create(data_callback, _var_is_local=False)  # type: ignore

        code = [f"function {data_callback}([col, row])" "{"]

        columns_path = f"{self.columns._var_full_name}"
        data_path = f"{self.data._var_full_name}"

        code.extend(
            [
                f"    return formatDataEditorCells(col, row, {columns_path}, {data_path});",
                "  }",
            ]
        )

        return "\n".join(code)

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create the DataEditor component.

        Args:
            *children: The children of the data editor.
            **props: The props of the data editor.

        Raises:
            ValueError: invalid input.

        Returns:
            The DataEditor component.&
        """
        from reflex.el.elements import Div

        columns = props.get("columns", [])
        data = props.get("data", [])
        rows = props.get("rows", None)

        # If rows is not provided, determine from data.
        if rows is None:
            props["rows"] = (
                data.length()  # BaseVar.create(value=f"{data}.length()", is_local=False)
                if isinstance(data, Var)
                else len(data)
            )

        if not isinstance(columns, Var) and len(columns):
            if (
                types.is_dataframe(type(data))
                or isinstance(data, Var)
                and types.is_dataframe(data._var_type)
            ):
                raise ValueError(
                    "Cannot pass in both a pandas dataframe and columns to the data_editor component."
                )
            else:
                if (
                    not isinstance(columns, list)
                    or isinstance(columns, list)
                    and columns
                    and not isinstance(columns[0], dict)
                ):
                    raise ValueError(
                        "Data Editor columns field should be a list of dictionaries"
                    )

                props["columns"] = [DataEditorColumn(**c) for c in columns]

        if "theme" in props:
            theme = props.get("theme")
            if isinstance(theme, Dict):
                props["theme"] = DataEditorTheme(**theme)

        # Allow by default to select a region of cells in the grid.
        props.setdefault("get_cell_for_selection", True)

        # Disable on_paste by default if not provided.
        props.setdefault("on_paste", False)

        if props.pop("get_cell_content", None) is not None:
            console.warn(
                "get_cell_content is not user configurable, the provided value will be discarded"
            )
        grid = super().create(*children, **props)
        return Div.create(
            grid,
            width=props.pop("width", "100%"),
            height=props.pop("height", "100%"),
        )

    def _get_app_wrap_components(self) -> dict[tuple[int, str], Component]:
        """Get the app wrap components for the component.

        Returns:
            The app wrap components.
        """
        from reflex.el.elements import Div

        class Portal(Div):
            def get_ref(self):
                return None

        return {(-1, "DataEditorPortal"): Portal.create(id="portal")}


# try:
#     pass

#     # def format_dataframe_values(df: DataFrame) -> list[list[Any]]:
#     #     """Format dataframe values to a list of lists.

#     #     Args:
#     #         df: The dataframe to format.

#     #     Returns:
#     #         The dataframe as a list of lists.
#     #     """
#     # return [
#     #     [str(d) if isinstance(d, (list, tuple)) else d for d in data]
#     #     for data in list(df.values.tolist())
#     # ]
#     # ...

#     # @serializer
#     # def serialize_dataframe(df: DataFrame) -> dict:
#     #     """Serialize a pandas dataframe.

#     #     Args:
#     #         df: The dataframe to serialize.

#     #     Returns:
#     #         The serialized dataframe.
#     #     """
#     # return {
#     #     "columns": df.columns.tolist(),
#     #     "data": format_dataframe_values(df),
#     # }

# except ImportError:
#     pass


@serializer
def serialize_data_editor_prop(prop: DataEditorProp) -> dict:
    """The serializer for the data editor theme.

    Args:
        prop: The prop to serialize.

    Returns:
        The serialized prop.
    """
    return prop.dict()
