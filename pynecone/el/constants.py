# Sourced from https://developer.mozilla.org/en-US/docs/Web/HTML/Element.
from collections import defaultdict

from pynecone.utils import to_snake_case


ELEMENTS = """
html base head link meta style title body address article aside
footer header h1 h2 h3 h4 h5 h6 main nav section blockquote dd
div dl dt figcaption figure hr li menu ol p pre ul a abbr b bdi
bdo br cite code data dfn em i kbd mark q rp rt ruby s samp
small span strong sub sup time u var wbr area audio img map
track video embed iframe object picture portal source svg math
canvas noscript script del ins caption col colgroup table tbody
td tfoot th thead tr button datalist fieldset form input label
legend meter optgroup option output progress select textarea
details dialog summary slot template
""".split()

# Sources:
# - https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes
# - https://github.com/facebook/react/blob/d1ad984db1591b131d16739a24dee4ba44886a09/packages/react-dom-bindings/src/shared/DOMProperty.js.
# TODO: Support data-* and aria-* attributes.

PROP_TO_ELEMENTS = {
    "accept": ["form", "input"],
    "accept-charset": ["form"],
    "accesskey": ELEMENTS,
    "action": ["form"],
    "align": [
        "applet",
        "caption",
        "col",
        "colgroup",
        "hr",
        "iframe",
        "img",
        "table",
        "tbody",
        "td",
        "tfoot",
        "th",
        "thead",
        "tr",
    ],
    "allow": ["iframe"],
    "alt": ["applet", "area", "img", "input"],
    "async": ["script"],
    "autocapitalize": ELEMENTS,
    "autocomplete": ["form", "input", "select", "textarea"],
    "autofocus": ["button", "input", "keygen", "select", "textarea"],
    "autoplay": ["audio", "video"],
    "background": ["body", "table", "td", "th"],
    "bgcolor": [
        "body",
        "col",
        "colgroup",
        "marquee",
        "table",
        "tbody",
        "tfoot",
        "td",
        "th",
        "tr",
    ],
    "border": ["img", "object", "table"],
    "buffered": ["audio", "video"],
    "capture": ["input"],
    "challenge": ["keygen"],
    "charset": ["meta", "script"],
    "checked": ["input"],
    "cite": ["blockquote", "del", "ins", "q"],
    "class": ELEMENTS,
    "code": ["applet"],
    "codebase": ["applet"],
    "color": ["font", "hr"],
    "cols": ["textarea"],
    "colspan": ["td", "th"],
    "content": ["meta"],
    "contenteditable": ELEMENTS,
    "contextmenu": ELEMENTS,
    "controls": ["audio", "video"],
    "coords": ["area"],
    "crossorigin": ["audio", "img", "link", "script", "video"],
    "csp": ["iframe"],
    "data": ["object"],
    "datetime": ["del", "ins", "time"],
    "decoding": ["img"],
    "default": ["track"],
    "defer": ["script"],
    "dir": ELEMENTS,
    "dirname": ["input", "textarea"],
    "disabled": [
        "button",
        "fieldset",
        "input",
        "keygen",
        "optgroup",
        "option",
        "select",
        "textarea",
    ],
    "download": ["a", "area"],
    "draggable": ELEMENTS,
    "enctype": ["form"],
    "enterkeyhint": ELEMENTS,
    "for": ["label", "output"],
    "form": [
        "button",
        "fieldset",
        "input",
        "keygen",
        "label",
        "meter",
        "object",
        "output",
        "progress",
        "select",
        "textarea",
    ],
    "formaction": ["button", "input"],
    "formenctype": ["button", "input"],
    "formmethod": ["button", "input"],
    "formnovalidate": ["button", "input"],
    "formtarget": ["button", "input"],
    "headers": ["td", "th"],
    "height": ["canvas", "embed", "iframe", "img", "input", "object", "video"],
    "hidden": ELEMENTS,
    "high": ["meter"],
    "href": ["a", "area", "base", "link"],
    "hreflang": ["a", "area", "link"],
    "http-equiv": ["meta"],
    "icon": ["command"],
    "id": ELEMENTS,
    "integrity": ["link", "script"],
    "intrinsicsize": ["img"],
    "inputmode": ELEMENTS,
    "ismap": ["img"],
    "itemprop": ELEMENTS,
    "keytype": ["keygen"],
    "kind": ["track"],
    "label": ["optgroup", "option", "track"],
    "lang": ELEMENTS,
    "language": ["script"],
    "loading": ["img", "iframe"],
    "list": ["input"],
    "loop": ["audio", "bgsound", "marquee", "video"],
    "low": ["meter"],
    "manifest": ["html"],
    "max": ["input", "meter", "progress"],
    "maxlength": ["input", "textarea"],
    "minlength": ["input", "textarea"],
    "media": ["a", "area", "link", "source", "style"],
    "method": ["form"],
    "min": ["input", "meter"],
    "multiple": ["input", "select"],
    "muted": ["audio", "video"],
    "name": [
        "button",
        "form",
        "fieldset",
        "iframe",
        "input",
        "keygen",
        "object",
        "output",
        "select",
        "textarea",
        "map",
        "meta",
        "param",
    ],
    "novalidate": ["form"],
    "open": ["details", "dialog"],
    "optimum": ["meter"],
    "pattern": ["input"],
    "ping": ["a", "area"],
    "placeholder": ["input", "textarea"],
    "playsinline": ["video"],
    "poster": ["video"],
    "preload": ["audio", "video"],
    "readonly": ["input", "textarea"],
    "referrerpolicy": ["a", "area", "iframe", "img", "link", "script"],
    "rel": ["a", "area", "link"],
    "required": ["input", "select", "textarea"],
    "reversed": ["ol"],
    "role": ELEMENTS,
    "rows": ["textarea"],
    "rowspan": ["td", "th"],
    "sandbox": ["iframe"],
    "scope": ["th"],
    "scoped": ["style"],
    "selected": ["option"],
    "shape": ["a", "area"],
    "size": ["input", "select"],
    "sizes": ["link", "img", "source"],
    "slot": ELEMENTS,
    "span": ["col", "colgroup"],
    "spellcheck": ELEMENTS,
    "src": [
        "audio",
        "embed",
        "iframe",
        "img",
        "input",
        "script",
        "source",
        "track",
        "video",
    ],
    "srcdoc": ["iframe"],
    "srclang": ["track"],
    "srcset": ["img", "source"],
    "start": ["ol"],
    "step": ["input"],
    "style": ELEMENTS,
    "summary": ["table"],
    "tabindex": ELEMENTS,
    "target": ["a", "area", "base", "form"],
    "title": ELEMENTS,
    "translate": ELEMENTS,
    "type": [
        "button",
        "input",
        "embed",
        "object",
        "ol",
        "script",
        "source",
        "style",
        "menu",
        "link",
    ],
    "usemap": ["img", "input", "object"],
    "value": [
        "button",
        "data",
        "input",
        "li",
        "meter",
        "option",
        "progress",
        "param",
    ],
    "width": ["canvas", "embed", "iframe", "img", "input", "object", "video"],
    "wrap": ["textarea"],
}

# Remove attributes that are already provided by Pynecone.
del PROP_TO_ELEMENTS["class"]
del PROP_TO_ELEMENTS["id"]
del PROP_TO_ELEMENTS["style"]


# Sources:
# - https://github.com/facebook/react/blob/d1ad984db1591b131d16739a24dee4ba44886a09/packages/react-dom-bindings/src/shared/possibleStandardNames.js#L22
POSSIBLE_STANDARD_NAMES = {
    "accept": "accept",
    "acceptcharset": "acceptCharset",
    "accept-charset": "acceptCharset",
    "accesskey": "accessKey",
    "action": "action",
    "allowfullscreen": "allowFullScreen",
    "alt": "alt",
    "as": "as",
    "async": "async",
    "autocapitalize": "autoCapitalize",
    "autocomplete": "autoComplete",
    "autocorrect": "autoCorrect",
    "autofocus": "autoFocus",
    "autoplay": "autoPlay",
    "autosave": "autoSave",
    "capture": "capture",
    "cellpadding": "cellPadding",
    "cellspacing": "cellSpacing",
    "challenge": "challenge",
    "charset": "charSet",
    "checked": "checked",
    "children": "children",
    "cite": "cite",
    "class": "className",
    "classid": "classID",
    "classname": "className",
    "cols": "cols",
    "colspan": "colSpan",
    "content": "content",
    "contenteditable": "contentEditable",
    "contextmenu": "contextMenu",
    "controls": "controls",
    "controlslist": "controlsList",
    "coords": "coords",
    "crossorigin": "crossOrigin",
    "dangerouslysetinnerhtml": "dangerouslySetInnerHTML",
    "data": "data",
    "datetime": "dateTime",
    "default": "default",
    "defaultchecked": "defaultChecked",
    "defaultvalue": "defaultValue",
    "defer": "defer",
    "dir": "dir",
    "disabled": "disabled",
    "disablepictureinpicture": "disablePictureInPicture",
    "disableremoteplayback": "disableRemotePlayback",
    "download": "download",
    "draggable": "draggable",
    "enctype": "encType",
    "enterkeyhint": "enterKeyHint",
    "fetchpriority": "fetchPriority",
    "for": "htmlFor",
    "form": "form",
    "formmethod": "formMethod",
    "formaction": "formAction",
    "formenctype": "formEncType",
    "formnovalidate": "formNoValidate",
    "formtarget": "formTarget",
    "frameborder": "frameBorder",
    "headers": "headers",
    "height": "height",
    "hidden": "hidden",
    "high": "high",
    "href": "href",
    "hreflang": "hrefLang",
    "htmlfor": "htmlFor",
    "httpequiv": "httpEquiv",
    "http-equiv": "httpEquiv",
    "icon": "icon",
    "id": "id",
    "imagesizes": "imageSizes",
    "imagesrcset": "imageSrcSet",
    "innerhtml": "innerHTML",
    "inputmode": "inputMode",
    "integrity": "integrity",
    "is": "is",
    "itemid": "itemID",
    "itemprop": "itemProp",
    "itemref": "itemRef",
    "itemscope": "itemScope",
    "itemtype": "itemType",
    "keyparams": "keyParams",
    "keytype": "keyType",
    "kind": "kind",
    "label": "label",
    "lang": "lang",
    "list": "list",
    "loop": "loop",
    "low": "low",
    "manifest": "manifest",
    "marginwidth": "marginWidth",
    "marginheight": "marginHeight",
    "max": "max",
    "maxlength": "maxLength",
    "media": "media",
    "mediagroup": "mediaGroup",
    "method": "method",
    "min": "min",
    "minlength": "minLength",
    "multiple": "multiple",
    "muted": "muted",
    "name": "name",
    "nomodule": "noModule",
    "nonce": "nonce",
    "novalidate": "noValidate",
    "open": "open",
    "optimum": "optimum",
    "pattern": "pattern",
    "placeholder": "placeholder",
    "playsinline": "playsInline",
    "poster": "poster",
    "preload": "preload",
    "profile": "profile",
    "radiogroup": "radioGroup",
    "readonly": "readOnly",
    "referrerpolicy": "referrerPolicy",
    "rel": "rel",
    "required": "required",
    "reversed": "reversed",
    "role": "role",
    "rows": "rows",
    "rowspan": "rowSpan",
    "sandbox": "sandbox",
    "scope": "scope",
    "scoped": "scoped",
    "scrolling": "scrolling",
    "seamless": "seamless",
    "selected": "selected",
    "shape": "shape",
    "size": "size",
    "sizes": "sizes",
    "span": "span",
    "spellcheck": "spellCheck",
    "src": "src",
    "srcdoc": "srcDoc",
    "srclang": "srcLang",
    "srcset": "srcSet",
    "start": "start",
    "step": "step",
    "style": "style",
    "summary": "summary",
    "tabindex": "tabIndex",
    "target": "target",
    "title": "title",
    "type": "type",
    "usemap": "useMap",
    "value": "value",
    "width": "width",
    "wmode": "wmode",
    "wrap": "wrap",
    "about": "about",
    "accentheight": "accentHeight",
    "accent-height": "accentHeight",
    "accumulate": "accumulate",
    "additive": "additive",
    "alignmentbaseline": "alignmentBaseline",
    "alignment-baseline": "alignmentBaseline",
    "allowreorder": "allowReorder",
    "alphabetic": "alphabetic",
    "amplitude": "amplitude",
    "arabicform": "arabicForm",
    "arabic-form": "arabicForm",
    "ascent": "ascent",
    "attributename": "attributeName",
    "attributetype": "attributeType",
    "autoreverse": "autoReverse",
    "azimuth": "azimuth",
    "basefrequency": "baseFrequency",
    "baselineshift": "baselineShift",
    "baseline-shift": "baselineShift",
    "baseprofile": "baseProfile",
    "bbox": "bbox",
    "begin": "begin",
    "bias": "bias",
    "by": "by",
    "calcmode": "calcMode",
    "capheight": "capHeight",
    "cap-height": "capHeight",
    "clip": "clip",
    "clippath": "clipPath",
    "clip-path": "clipPath",
    "clippathunits": "clipPathUnits",
    "cliprule": "clipRule",
    "clip-rule": "clipRule",
    "color": "color",
    "colorinterpolation": "colorInterpolation",
    "color-interpolation": "colorInterpolation",
    "colorinterpolationfilters": "colorInterpolationFilters",
    "color-interpolation-filters": "colorInterpolationFilters",
    "colorprofile": "colorProfile",
    "color-profile": "colorProfile",
    "colorrendering": "colorRendering",
    "color-rendering": "colorRendering",
    "contentscripttype": "contentScriptType",
    "contentstyletype": "contentStyleType",
    "cursor": "cursor",
    "cx": "cx",
    "cy": "cy",
    "d": "d",
    "datatype": "datatype",
    "decelerate": "decelerate",
    "descent": "descent",
    "diffuseconstant": "diffuseConstant",
    "direction": "direction",
    "display": "display",
    "divisor": "divisor",
    "dominantbaseline": "dominantBaseline",
    "dominant-baseline": "dominantBaseline",
    "dur": "dur",
    "dx": "dx",
    "dy": "dy",
    "edgemode": "edgeMode",
    "elevation": "elevation",
    "enablebackground": "enableBackground",
    "enable-background": "enableBackground",
    "end": "end",
    "exponent": "exponent",
    "externalresourcesrequired": "externalResourcesRequired",
    "fill": "fill",
    "fillopacity": "fillOpacity",
    "fill-opacity": "fillOpacity",
    "fillrule": "fillRule",
    "fill-rule": "fillRule",
    "filter": "filter",
    "filterres": "filterRes",
    "filterunits": "filterUnits",
    "floodopacity": "floodOpacity",
    "flood-opacity": "floodOpacity",
    "floodcolor": "floodColor",
    "flood-color": "floodColor",
    "focusable": "focusable",
    "fontfamily": "fontFamily",
    "font-family": "fontFamily",
    "fontsize": "fontSize",
    "font-size": "fontSize",
    "fontsizeadjust": "fontSizeAdjust",
    "font-size-adjust": "fontSizeAdjust",
    "fontstretch": "fontStretch",
    "font-stretch": "fontStretch",
    "fontstyle": "fontStyle",
    "font-style": "fontStyle",
    "fontvariant": "fontVariant",
    "font-variant": "fontVariant",
    "fontweight": "fontWeight",
    "font-weight": "fontWeight",
    "format": "format",
    "from": "from",
    "fx": "fx",
    "fy": "fy",
    "g1": "g1",
    "g2": "g2",
    "glyphname": "glyphName",
    "glyph-name": "glyphName",
    "glyphorientationhorizontal": "glyphOrientationHorizontal",
    "glyph-orientation-horizontal": "glyphOrientationHorizontal",
    "glyphorientationvertical": "glyphOrientationVertical",
    "glyph-orientation-vertical": "glyphOrientationVertical",
    "glyphref": "glyphRef",
    "gradienttransform": "gradientTransform",
    "gradientunits": "gradientUnits",
    "hanging": "hanging",
    "horizadvx": "horizAdvX",
    "horiz-adv-x": "horizAdvX",
    "horizoriginx": "horizOriginX",
    "horiz-origin-x": "horizOriginX",
    "ideographic": "ideographic",
    "imagerendering": "imageRendering",
    "image-rendering": "imageRendering",
    "in2": "in2",
    "in": "in",
    "inlist": "inlist",
    "intercept": "intercept",
    "k1": "k1",
    "k2": "k2",
    "k3": "k3",
    "k4": "k4",
    "k": "k",
    "kernelmatrix": "kernelMatrix",
    "kernelunitlength": "kernelUnitLength",
    "kerning": "kerning",
    "keypoints": "keyPoints",
    "keysplines": "keySplines",
    "keytimes": "keyTimes",
    "lengthadjust": "lengthAdjust",
    "letterspacing": "letterSpacing",
    "letter-spacing": "letterSpacing",
    "lightingcolor": "lightingColor",
    "lighting-color": "lightingColor",
    "limitingconeangle": "limitingConeAngle",
    "local": "local",
    "markerend": "markerEnd",
    "marker-end": "markerEnd",
    "markerheight": "markerHeight",
    "markermid": "markerMid",
    "marker-mid": "markerMid",
    "markerstart": "markerStart",
    "marker-start": "markerStart",
    "markerunits": "markerUnits",
    "markerwidth": "markerWidth",
    "mask": "mask",
    "maskcontentunits": "maskContentUnits",
    "maskunits": "maskUnits",
    "mathematical": "mathematical",
    "mode": "mode",
    "numoctaves": "numOctaves",
    "offset": "offset",
    "opacity": "opacity",
    "operator": "operator",
    "order": "order",
    "orient": "orient",
    "orientation": "orientation",
    "origin": "origin",
    "overflow": "overflow",
    "overlineposition": "overlinePosition",
    "overline-position": "overlinePosition",
    "overlinethickness": "overlineThickness",
    "overline-thickness": "overlineThickness",
    "paintorder": "paintOrder",
    "paint-order": "paintOrder",
    "panose1": "panose1",
    "panose-1": "panose1",
    "pathlength": "pathLength",
    "patterncontentunits": "patternContentUnits",
    "patterntransform": "patternTransform",
    "patternunits": "patternUnits",
    "pointerevents": "pointerEvents",
    "pointer-events": "pointerEvents",
    "points": "points",
    "pointsatx": "pointsAtX",
    "pointsaty": "pointsAtY",
    "pointsatz": "pointsAtZ",
    "prefix": "prefix",
    "preservealpha": "preserveAlpha",
    "preserveaspectratio": "preserveAspectRatio",
    "primitiveunits": "primitiveUnits",
    "property": "property",
    "r": "r",
    "radius": "radius",
    "refx": "refX",
    "refy": "refY",
    "renderingintent": "renderingIntent",
    "rendering-intent": "renderingIntent",
    "repeatcount": "repeatCount",
    "repeatdur": "repeatDur",
    "requiredextensions": "requiredExtensions",
    "requiredfeatures": "requiredFeatures",
    "resource": "resource",
    "restart": "restart",
    "result": "result",
    "results": "results",
    "rotate": "rotate",
    "rx": "rx",
    "ry": "ry",
    "scale": "scale",
    "security": "security",
    "seed": "seed",
    "shaperendering": "shapeRendering",
    "shape-rendering": "shapeRendering",
    "slope": "slope",
    "spacing": "spacing",
    "specularconstant": "specularConstant",
    "specularexponent": "specularExponent",
    "speed": "speed",
    "spreadmethod": "spreadMethod",
    "startoffset": "startOffset",
    "stddeviation": "stdDeviation",
    "stemh": "stemh",
    "stemv": "stemv",
    "stitchtiles": "stitchTiles",
    "stopcolor": "stopColor",
    "stop-color": "stopColor",
    "stopopacity": "stopOpacity",
    "stop-opacity": "stopOpacity",
    "strikethroughposition": "strikethroughPosition",
    "strikethrough-position": "strikethroughPosition",
    "strikethroughthickness": "strikethroughThickness",
    "strikethrough-thickness": "strikethroughThickness",
    "string": "string",
    "stroke": "stroke",
    "strokedasharray": "strokeDasharray",
    "stroke-dasharray": "strokeDasharray",
    "strokedashoffset": "strokeDashoffset",
    "stroke-dashoffset": "strokeDashoffset",
    "strokelinecap": "strokeLinecap",
    "stroke-linecap": "strokeLinecap",
    "strokelinejoin": "strokeLinejoin",
    "stroke-linejoin": "strokeLinejoin",
    "strokemiterlimit": "strokeMiterlimit",
    "stroke-miterlimit": "strokeMiterlimit",
    "strokewidth": "strokeWidth",
    "stroke-width": "strokeWidth",
    "strokeopacity": "strokeOpacity",
    "stroke-opacity": "strokeOpacity",
    "suppresscontenteditablewarning": "suppressContentEditableWarning",
    "suppresshydrationwarning": "suppressHydrationWarning",
    "surfacescale": "surfaceScale",
    "systemlanguage": "systemLanguage",
    "tablevalues": "tableValues",
    "targetx": "targetX",
    "targety": "targetY",
    "textanchor": "textAnchor",
    "text-anchor": "textAnchor",
    "textdecoration": "textDecoration",
    "text-decoration": "textDecoration",
    "textlength": "textLength",
    "textrendering": "textRendering",
    "text-rendering": "textRendering",
    "to": "to",
    "transform": "transform",
    "transformorigin": "transformOrigin",
    "transform-origin": "transformOrigin",
    "typeof": "typeof",
    "u1": "u1",
    "u2": "u2",
    "underlineposition": "underlinePosition",
    "underline-position": "underlinePosition",
    "underlinethickness": "underlineThickness",
    "underline-thickness": "underlineThickness",
    "unicode": "unicode",
    "unicodebidi": "unicodeBidi",
    "unicode-bidi": "unicodeBidi",
    "unicoderange": "unicodeRange",
    "unicode-range": "unicodeRange",
    "unitsperem": "unitsPerEm",
    "units-per-em": "unitsPerEm",
    "unselectable": "unselectable",
    "valphabetic": "vAlphabetic",
    "v-alphabetic": "vAlphabetic",
    "values": "values",
    "vectoreffect": "vectorEffect",
    "vector-effect": "vectorEffect",
    "version": "version",
    "vertadvy": "vertAdvY",
    "vert-adv-y": "vertAdvY",
    "vertoriginx": "vertOriginX",
    "vert-origin-x": "vertOriginX",
    "vertoriginy": "vertOriginY",
    "vert-origin-y": "vertOriginY",
    "vhanging": "vHanging",
    "v-hanging": "vHanging",
    "videographic": "vIdeographic",
    "v-ideographic": "vIdeographic",
    "viewbox": "viewBox",
    "viewtarget": "viewTarget",
    "visibility": "visibility",
    "vmathematical": "vMathematical",
    "v-mathematical": "vMathematical",
    "vocab": "vocab",
    "widths": "widths",
    "wordspacing": "wordSpacing",
    "word-spacing": "wordSpacing",
    "writingmode": "writingMode",
    "writing-mode": "writingMode",
    "x1": "x1",
    "x2": "x2",
    "x": "x",
    "xchannelselector": "xChannelSelector",
    "xheight": "xHeight",
    "x-height": "xHeight",
    "xlinkactuate": "xlinkActuate",
    "xlink:actuate": "xlinkActuate",
    "xlinkarcrole": "xlinkArcrole",
    "xlink:arcrole": "xlinkArcrole",
    "xlinkhref": "xlinkHref",
    "xlink:href": "xlinkHref",
    "xlinkrole": "xlinkRole",
    "xlink:role": "xlinkRole",
    "xlinkshow": "xlinkShow",
    "xlink:show": "xlinkShow",
    "xlinktitle": "xlinkTitle",
    "xlink:title": "xlinkTitle",
    "xlinktype": "xlinkType",
    "xlink:type": "xlinkType",
    "xmlbase": "xmlBase",
    "xml:base": "xmlBase",
    "xmllang": "xmlLang",
    "xml:lang": "xmlLang",
    "xmlns": "xmlns",
    "xml:space": "xmlSpace",
    "xmlnsxlink": "xmlnsXlink",
    "xmlns:xlink": "xmlnsXlink",
    "xmlspace": "xmlSpace",
    "y1": "y1",
    "y2": "y2",
    "y": "y",
    "ychannelselector": "yChannelSelector",
    "z": "z",
    "zoomandpan": "zoomAndPan",
} | {
    "async": "async_",
}

# Currently, PROP_TO_ELEMENTS actually contains HTML attribute names, not
# React prop names. So we normalize HTML attribute names to their React prop
# forms. (e.g. for -> htmlFor, class -> className, etc.)
PROP_TO_ELEMENTS = {
    POSSIBLE_STANDARD_NAMES.get(name, name): elements
    for name, elements in PROP_TO_ELEMENTS.items()
}

# Now, convert all the props to snake_case.
PROP_TO_ELEMENTS = {
    to_snake_case(prop): elements for prop, elements in PROP_TO_ELEMENTS.items()
}


# Invert PROP_TO_ELEMENTS to get ELEMENT_TO_PROPS. This enables easier lookup.
ELEMENT_TO_PROPS = defaultdict(list)
for prop, elements in PROP_TO_ELEMENTS.items():
    for el in elements:
        ELEMENT_TO_PROPS[el].append(prop)
