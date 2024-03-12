"""Stub file for reflex/components/datadisplay/code.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
import re
from typing import Dict, Literal, Optional, Union
from reflex.components.chakra.forms import Button
from reflex.components.chakra.layout import Box
from reflex.components.chakra.media import Icon
from reflex.components.component import Component
from reflex.components.core.cond import color_mode_cond
from reflex.event import set_clipboard
from reflex.style import Style
from reflex.utils import format, imports
from reflex.utils.imports import ImportVar
from reflex.vars import Var

LiteralCodeBlockTheme = Literal[
    "a11y-dark",
    "atom-dark",
    "cb",
    "coldark-cold",
    "coldark-dark",
    "coy",
    "coy-without-shadows",
    "darcula",
    "dark",
    "dracula",
    "duotone-dark",
    "duotone-earth",
    "duotone-forest",
    "duotone-light",
    "duotone-sea",
    "duotone-space",
    "funky",
    "ghcolors",
    "gruvbox-dark",
    "gruvbox-light",
    "holi-theme",
    "hopscotch",
    "light",
    "lucario",
    "material-dark",
    "material-light",
    "material-oceanic",
    "night-owl",
    "nord",
    "okaidia",
    "one-dark",
    "one-light",
    "pojoaque",
    "prism",
    "shades-of-purple",
    "solarized-dark-atom",
    "solarizedlight",
    "synthwave84",
    "tomorrow",
    "twilight",
    "vs",
    "vs-dark",
    "vsc-dark-plus",
    "xonokai",
    "z-touch",
]
LiteralCodeLanguage = Literal[
    "abap",
    "abnf",
    "actionscript",
    "ada",
    "agda",
    "al",
    "antlr4",
    "apacheconf",
    "apex",
    "apl",
    "applescript",
    "aql",
    "arduino",
    "arff",
    "asciidoc",
    "asm6502",
    "asmatmel",
    "aspnet",
    "autohotkey",
    "autoit",
    "avisynth",
    "avro-idl",
    "bash",
    "basic",
    "batch",
    "bbcode",
    "bicep",
    "birb",
    "bison",
    "bnf",
    "brainfuck",
    "brightscript",
    "bro",
    "bsl",
    "c",
    "cfscript",
    "chaiscript",
    "cil",
    "clike",
    "clojure",
    "cmake",
    "cobol",
    "coffeescript",
    "concurnas",
    "coq",
    "core",
    "cpp",
    "crystal",
    "csharp",
    "cshtml",
    "csp",
    "css",
    "css-extras",
    "csv",
    "cypher",
    "d",
    "dart",
    "dataweave",
    "dax",
    "dhall",
    "diff",
    "django",
    "dns-zone-file",
    "docker",
    "dot",
    "ebnf",
    "editorconfig",
    "eiffel",
    "ejs",
    "elixir",
    "elm",
    "erb",
    "erlang",
    "etlua",
    "excel-formula",
    "factor",
    "false",
    "firestore-security-rules",
    "flow",
    "fortran",
    "fsharp",
    "ftl",
    "gap",
    "gcode",
    "gdscript",
    "gedcom",
    "gherkin",
    "git",
    "glsl",
    "gml",
    "gn",
    "go",
    "go-module",
    "graphql",
    "groovy",
    "haml",
    "handlebars",
    "haskell",
    "haxe",
    "hcl",
    "hlsl",
    "hoon",
    "hpkp",
    "hsts",
    "http",
    "ichigojam",
    "icon",
    "icu-message-format",
    "idris",
    "iecst",
    "ignore",
    "index",
    "inform7",
    "ini",
    "io",
    "j",
    "java",
    "javadoc",
    "javadoclike",
    "javascript",
    "javastacktrace",
    "jexl",
    "jolie",
    "jq",
    "js-extras",
    "js-templates",
    "jsdoc",
    "json",
    "json5",
    "jsonp",
    "jsstacktrace",
    "jsx",
    "julia",
    "keepalived",
    "keyman",
    "kotlin",
    "kumir",
    "kusto",
    "latex",
    "latte",
    "less",
    "lilypond",
    "liquid",
    "lisp",
    "livescript",
    "llvm",
    "log",
    "lolcode",
    "lua",
    "magma",
    "makefile",
    "markdown",
    "markup",
    "markup-templating",
    "matlab",
    "maxscript",
    "mel",
    "mermaid",
    "mizar",
    "mongodb",
    "monkey",
    "moonscript",
    "n1ql",
    "n4js",
    "nand2tetris-hdl",
    "naniscript",
    "nasm",
    "neon",
    "nevod",
    "nginx",
    "nim",
    "nix",
    "nsis",
    "objectivec",
    "ocaml",
    "opencl",
    "openqasm",
    "oz",
    "parigp",
    "parser",
    "pascal",
    "pascaligo",
    "pcaxis",
    "peoplecode",
    "perl",
    "php",
    "php-extras",
    "phpdoc",
    "plsql",
    "powerquery",
    "powershell",
    "processing",
    "prolog",
    "promql",
    "properties",
    "protobuf",
    "psl",
    "pug",
    "puppet",
    "pure",
    "purebasic",
    "purescript",
    "python",
    "q",
    "qml",
    "qore",
    "qsharp",
    "r",
    "racket",
    "reason",
    "regex",
    "rego",
    "renpy",
    "rest",
    "rip",
    "roboconf",
    "robotframework",
    "ruby",
    "rust",
    "sas",
    "sass",
    "scala",
    "scheme",
    "scss",
    "shell-session",
    "smali",
    "smalltalk",
    "smarty",
    "sml",
    "solidity",
    "solution-file",
    "soy",
    "sparql",
    "splunk-spl",
    "sqf",
    "sql",
    "squirrel",
    "stan",
    "stylus",
    "swift",
    "systemd",
    "t4-cs",
    "t4-templating",
    "t4-vb",
    "tap",
    "tcl",
    "textile",
    "toml",
    "tremor",
    "tsx",
    "tt2",
    "turtle",
    "twig",
    "typescript",
    "typoscript",
    "unrealscript",
    "uorazor",
    "uri",
    "v",
    "vala",
    "vbnet",
    "velocity",
    "verilog",
    "vhdl",
    "vim",
    "visual-basic",
    "warpscript",
    "wasm",
    "web-idl",
    "wiki",
    "wolfram",
    "wren",
    "xeora",
    "xml-doc",
    "xojo",
    "xquery",
    "yaml",
    "yang",
    "zig",
]

class CodeBlock(Component):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        can_copy: Optional[bool] = False,
        copy_button: Optional[Union[bool, Component]] = None,
        theme: Optional[
            Union[
                Var[
                    Literal[
                        "a11y-dark",
                        "atom-dark",
                        "cb",
                        "coldark-cold",
                        "coldark-dark",
                        "coy",
                        "coy-without-shadows",
                        "darcula",
                        "dark",
                        "dracula",
                        "duotone-dark",
                        "duotone-earth",
                        "duotone-forest",
                        "duotone-light",
                        "duotone-sea",
                        "duotone-space",
                        "funky",
                        "ghcolors",
                        "gruvbox-dark",
                        "gruvbox-light",
                        "holi-theme",
                        "hopscotch",
                        "light",
                        "lucario",
                        "material-dark",
                        "material-light",
                        "material-oceanic",
                        "night-owl",
                        "nord",
                        "okaidia",
                        "one-dark",
                        "one-light",
                        "pojoaque",
                        "prism",
                        "shades-of-purple",
                        "solarized-dark-atom",
                        "solarizedlight",
                        "synthwave84",
                        "tomorrow",
                        "twilight",
                        "vs",
                        "vs-dark",
                        "vsc-dark-plus",
                        "xonokai",
                        "z-touch",
                    ]
                ],
                Literal[
                    "a11y-dark",
                    "atom-dark",
                    "cb",
                    "coldark-cold",
                    "coldark-dark",
                    "coy",
                    "coy-without-shadows",
                    "darcula",
                    "dark",
                    "dracula",
                    "duotone-dark",
                    "duotone-earth",
                    "duotone-forest",
                    "duotone-light",
                    "duotone-sea",
                    "duotone-space",
                    "funky",
                    "ghcolors",
                    "gruvbox-dark",
                    "gruvbox-light",
                    "holi-theme",
                    "hopscotch",
                    "light",
                    "lucario",
                    "material-dark",
                    "material-light",
                    "material-oceanic",
                    "night-owl",
                    "nord",
                    "okaidia",
                    "one-dark",
                    "one-light",
                    "pojoaque",
                    "prism",
                    "shades-of-purple",
                    "solarized-dark-atom",
                    "solarizedlight",
                    "synthwave84",
                    "tomorrow",
                    "twilight",
                    "vs",
                    "vs-dark",
                    "vsc-dark-plus",
                    "xonokai",
                    "z-touch",
                ],
            ]
        ] = None,
        language: Optional[
            Union[
                Var[
                    Literal[
                        "abap",
                        "abnf",
                        "actionscript",
                        "ada",
                        "agda",
                        "al",
                        "antlr4",
                        "apacheconf",
                        "apex",
                        "apl",
                        "applescript",
                        "aql",
                        "arduino",
                        "arff",
                        "asciidoc",
                        "asm6502",
                        "asmatmel",
                        "aspnet",
                        "autohotkey",
                        "autoit",
                        "avisynth",
                        "avro-idl",
                        "bash",
                        "basic",
                        "batch",
                        "bbcode",
                        "bicep",
                        "birb",
                        "bison",
                        "bnf",
                        "brainfuck",
                        "brightscript",
                        "bro",
                        "bsl",
                        "c",
                        "cfscript",
                        "chaiscript",
                        "cil",
                        "clike",
                        "clojure",
                        "cmake",
                        "cobol",
                        "coffeescript",
                        "concurnas",
                        "coq",
                        "core",
                        "cpp",
                        "crystal",
                        "csharp",
                        "cshtml",
                        "csp",
                        "css",
                        "css-extras",
                        "csv",
                        "cypher",
                        "d",
                        "dart",
                        "dataweave",
                        "dax",
                        "dhall",
                        "diff",
                        "django",
                        "dns-zone-file",
                        "docker",
                        "dot",
                        "ebnf",
                        "editorconfig",
                        "eiffel",
                        "ejs",
                        "elixir",
                        "elm",
                        "erb",
                        "erlang",
                        "etlua",
                        "excel-formula",
                        "factor",
                        "false",
                        "firestore-security-rules",
                        "flow",
                        "fortran",
                        "fsharp",
                        "ftl",
                        "gap",
                        "gcode",
                        "gdscript",
                        "gedcom",
                        "gherkin",
                        "git",
                        "glsl",
                        "gml",
                        "gn",
                        "go",
                        "go-module",
                        "graphql",
                        "groovy",
                        "haml",
                        "handlebars",
                        "haskell",
                        "haxe",
                        "hcl",
                        "hlsl",
                        "hoon",
                        "hpkp",
                        "hsts",
                        "http",
                        "ichigojam",
                        "icon",
                        "icu-message-format",
                        "idris",
                        "iecst",
                        "ignore",
                        "index",
                        "inform7",
                        "ini",
                        "io",
                        "j",
                        "java",
                        "javadoc",
                        "javadoclike",
                        "javascript",
                        "javastacktrace",
                        "jexl",
                        "jolie",
                        "jq",
                        "js-extras",
                        "js-templates",
                        "jsdoc",
                        "json",
                        "json5",
                        "jsonp",
                        "jsstacktrace",
                        "jsx",
                        "julia",
                        "keepalived",
                        "keyman",
                        "kotlin",
                        "kumir",
                        "kusto",
                        "latex",
                        "latte",
                        "less",
                        "lilypond",
                        "liquid",
                        "lisp",
                        "livescript",
                        "llvm",
                        "log",
                        "lolcode",
                        "lua",
                        "magma",
                        "makefile",
                        "markdown",
                        "markup",
                        "markup-templating",
                        "matlab",
                        "maxscript",
                        "mel",
                        "mermaid",
                        "mizar",
                        "mongodb",
                        "monkey",
                        "moonscript",
                        "n1ql",
                        "n4js",
                        "nand2tetris-hdl",
                        "naniscript",
                        "nasm",
                        "neon",
                        "nevod",
                        "nginx",
                        "nim",
                        "nix",
                        "nsis",
                        "objectivec",
                        "ocaml",
                        "opencl",
                        "openqasm",
                        "oz",
                        "parigp",
                        "parser",
                        "pascal",
                        "pascaligo",
                        "pcaxis",
                        "peoplecode",
                        "perl",
                        "php",
                        "php-extras",
                        "phpdoc",
                        "plsql",
                        "powerquery",
                        "powershell",
                        "processing",
                        "prolog",
                        "promql",
                        "properties",
                        "protobuf",
                        "psl",
                        "pug",
                        "puppet",
                        "pure",
                        "purebasic",
                        "purescript",
                        "python",
                        "q",
                        "qml",
                        "qore",
                        "qsharp",
                        "r",
                        "racket",
                        "reason",
                        "regex",
                        "rego",
                        "renpy",
                        "rest",
                        "rip",
                        "roboconf",
                        "robotframework",
                        "ruby",
                        "rust",
                        "sas",
                        "sass",
                        "scala",
                        "scheme",
                        "scss",
                        "shell-session",
                        "smali",
                        "smalltalk",
                        "smarty",
                        "sml",
                        "solidity",
                        "solution-file",
                        "soy",
                        "sparql",
                        "splunk-spl",
                        "sqf",
                        "sql",
                        "squirrel",
                        "stan",
                        "stylus",
                        "swift",
                        "systemd",
                        "t4-cs",
                        "t4-templating",
                        "t4-vb",
                        "tap",
                        "tcl",
                        "textile",
                        "toml",
                        "tremor",
                        "tsx",
                        "tt2",
                        "turtle",
                        "twig",
                        "typescript",
                        "typoscript",
                        "unrealscript",
                        "uorazor",
                        "uri",
                        "v",
                        "vala",
                        "vbnet",
                        "velocity",
                        "verilog",
                        "vhdl",
                        "vim",
                        "visual-basic",
                        "warpscript",
                        "wasm",
                        "web-idl",
                        "wiki",
                        "wolfram",
                        "wren",
                        "xeora",
                        "xml-doc",
                        "xojo",
                        "xquery",
                        "yaml",
                        "yang",
                        "zig",
                    ]
                ],
                Literal[
                    "abap",
                    "abnf",
                    "actionscript",
                    "ada",
                    "agda",
                    "al",
                    "antlr4",
                    "apacheconf",
                    "apex",
                    "apl",
                    "applescript",
                    "aql",
                    "arduino",
                    "arff",
                    "asciidoc",
                    "asm6502",
                    "asmatmel",
                    "aspnet",
                    "autohotkey",
                    "autoit",
                    "avisynth",
                    "avro-idl",
                    "bash",
                    "basic",
                    "batch",
                    "bbcode",
                    "bicep",
                    "birb",
                    "bison",
                    "bnf",
                    "brainfuck",
                    "brightscript",
                    "bro",
                    "bsl",
                    "c",
                    "cfscript",
                    "chaiscript",
                    "cil",
                    "clike",
                    "clojure",
                    "cmake",
                    "cobol",
                    "coffeescript",
                    "concurnas",
                    "coq",
                    "core",
                    "cpp",
                    "crystal",
                    "csharp",
                    "cshtml",
                    "csp",
                    "css",
                    "css-extras",
                    "csv",
                    "cypher",
                    "d",
                    "dart",
                    "dataweave",
                    "dax",
                    "dhall",
                    "diff",
                    "django",
                    "dns-zone-file",
                    "docker",
                    "dot",
                    "ebnf",
                    "editorconfig",
                    "eiffel",
                    "ejs",
                    "elixir",
                    "elm",
                    "erb",
                    "erlang",
                    "etlua",
                    "excel-formula",
                    "factor",
                    "false",
                    "firestore-security-rules",
                    "flow",
                    "fortran",
                    "fsharp",
                    "ftl",
                    "gap",
                    "gcode",
                    "gdscript",
                    "gedcom",
                    "gherkin",
                    "git",
                    "glsl",
                    "gml",
                    "gn",
                    "go",
                    "go-module",
                    "graphql",
                    "groovy",
                    "haml",
                    "handlebars",
                    "haskell",
                    "haxe",
                    "hcl",
                    "hlsl",
                    "hoon",
                    "hpkp",
                    "hsts",
                    "http",
                    "ichigojam",
                    "icon",
                    "icu-message-format",
                    "idris",
                    "iecst",
                    "ignore",
                    "index",
                    "inform7",
                    "ini",
                    "io",
                    "j",
                    "java",
                    "javadoc",
                    "javadoclike",
                    "javascript",
                    "javastacktrace",
                    "jexl",
                    "jolie",
                    "jq",
                    "js-extras",
                    "js-templates",
                    "jsdoc",
                    "json",
                    "json5",
                    "jsonp",
                    "jsstacktrace",
                    "jsx",
                    "julia",
                    "keepalived",
                    "keyman",
                    "kotlin",
                    "kumir",
                    "kusto",
                    "latex",
                    "latte",
                    "less",
                    "lilypond",
                    "liquid",
                    "lisp",
                    "livescript",
                    "llvm",
                    "log",
                    "lolcode",
                    "lua",
                    "magma",
                    "makefile",
                    "markdown",
                    "markup",
                    "markup-templating",
                    "matlab",
                    "maxscript",
                    "mel",
                    "mermaid",
                    "mizar",
                    "mongodb",
                    "monkey",
                    "moonscript",
                    "n1ql",
                    "n4js",
                    "nand2tetris-hdl",
                    "naniscript",
                    "nasm",
                    "neon",
                    "nevod",
                    "nginx",
                    "nim",
                    "nix",
                    "nsis",
                    "objectivec",
                    "ocaml",
                    "opencl",
                    "openqasm",
                    "oz",
                    "parigp",
                    "parser",
                    "pascal",
                    "pascaligo",
                    "pcaxis",
                    "peoplecode",
                    "perl",
                    "php",
                    "php-extras",
                    "phpdoc",
                    "plsql",
                    "powerquery",
                    "powershell",
                    "processing",
                    "prolog",
                    "promql",
                    "properties",
                    "protobuf",
                    "psl",
                    "pug",
                    "puppet",
                    "pure",
                    "purebasic",
                    "purescript",
                    "python",
                    "q",
                    "qml",
                    "qore",
                    "qsharp",
                    "r",
                    "racket",
                    "reason",
                    "regex",
                    "rego",
                    "renpy",
                    "rest",
                    "rip",
                    "roboconf",
                    "robotframework",
                    "ruby",
                    "rust",
                    "sas",
                    "sass",
                    "scala",
                    "scheme",
                    "scss",
                    "shell-session",
                    "smali",
                    "smalltalk",
                    "smarty",
                    "sml",
                    "solidity",
                    "solution-file",
                    "soy",
                    "sparql",
                    "splunk-spl",
                    "sqf",
                    "sql",
                    "squirrel",
                    "stan",
                    "stylus",
                    "swift",
                    "systemd",
                    "t4-cs",
                    "t4-templating",
                    "t4-vb",
                    "tap",
                    "tcl",
                    "textile",
                    "toml",
                    "tremor",
                    "tsx",
                    "tt2",
                    "turtle",
                    "twig",
                    "typescript",
                    "typoscript",
                    "unrealscript",
                    "uorazor",
                    "uri",
                    "v",
                    "vala",
                    "vbnet",
                    "velocity",
                    "verilog",
                    "vhdl",
                    "vim",
                    "visual-basic",
                    "warpscript",
                    "wasm",
                    "web-idl",
                    "wiki",
                    "wolfram",
                    "wren",
                    "xeora",
                    "xml-doc",
                    "xojo",
                    "xquery",
                    "yaml",
                    "yang",
                    "zig",
                ],
            ]
        ] = None,
        code: Optional[Union[Var[str], str]] = None,
        show_line_numbers: Optional[Union[Var[bool], bool]] = None,
        starting_line_number: Optional[Union[Var[int], int]] = None,
        wrap_long_lines: Optional[Union[Var[bool], bool]] = None,
        custom_style: Optional[Dict[str, str]] = None,
        code_tag_props: Optional[Union[Var[Dict[str, str]], Dict[str, str]]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props,
    ) -> "CodeBlock":
        """Create a text component.

        Args:
            *children: The children of the component.
            can_copy: Whether a copy button should appears.
            copy_button: A custom copy button to override the default one.
            theme: The theme to use ("light" or "dark").
            language: The language to use.
            code: The code to display.
            show_line_numbers: If this is enabled line numbers will be shown next to the code block.
            starting_line_number: The starting line number to use.
            wrap_long_lines: Whether to wrap long lines.
            custom_style: A custom style for the code block.
            code_tag_props: Props passed down to the code tag.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props to pass to the component.

        Returns:
            The text component.
        """
        ...
