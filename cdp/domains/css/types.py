from dataclasses import (
    dataclass
)
from typing import (
    Literal
)
from cdp.domains.dom.types import (
    BackendNodeId,
    LogicalAxes,
    NodeId,
    PhysicalAxes,
    PseudoType
)
from cdp.domains.page.types import (
    FrameId
)

StyleSheetId = str

StyleSheetOrigin = Literal[
    "injected",
    "user-agent",
    "inspector",
    "regular"
]

CSSRuleType = Literal[
    "MediaRule",
    "SupportsRule",
    "ContainerRule",
    "LayerRule",
    "ScopeRule",
    "StyleRule"
]


@dataclass
class PseudoElementMatches:
    pseudo_type: "PseudoType"
    pseudo_identifier: str
    matches: list


@dataclass
class InheritedStyleEntry:
    inline_style: "CSSStyle"
    matched_css_rules: list


@dataclass
class InheritedPseudoElementMatches:
    pseudo_elements: list


@dataclass
class RuleMatch:
    rule: "CSSRule"
    matching_selectors: list


@dataclass
class Value:
    text: str
    range: "SourceRange"
    specificity: "Specificity"


@dataclass
class Specificity:
    a: int
    b: int
    c: int


@dataclass
class SelectorList:
    selectors: list
    text: str


@dataclass
class CSSStyleSheetHeader:
    style_sheet_id: "StyleSheetId"
    frame_id: "FrameId"
    source_url: str
    source_map_url: str
    origin: "StyleSheetOrigin"
    title: str
    owner_node: "BackendNodeId"
    disabled: bool
    has_source_url: bool
    is_inline: bool
    is_mutable: bool
    is_constructed: bool
    start_line: float
    start_column: float
    length: float
    end_line: float
    end_column: float
    loading_failed: bool


@dataclass
class CSSRule:
    style_sheet_id: "StyleSheetId"
    selector_list: "SelectorList"
    nesting_selectors: list
    origin: "StyleSheetOrigin"
    style: "CSSStyle"
    media: list
    container_queries: list
    supports: list
    layers: list
    scopes: list
    rule_types: list


@dataclass
class RuleUsage:
    style_sheet_id: "StyleSheetId"
    start_offset: float
    end_offset: float
    used: bool


@dataclass
class SourceRange:
    start_line: int
    start_column: int
    end_line: int
    end_column: int


@dataclass
class ShorthandEntry:
    name: str
    value: str
    important: bool


@dataclass
class CSSComputedStyleProperty:
    name: str
    value: str


@dataclass
class CSSStyle:
    style_sheet_id: "StyleSheetId"
    css_properties: list
    shorthand_entries: list
    css_text: str
    range: "SourceRange"


@dataclass
class CSSProperty:
    name: str
    value: str
    important: bool
    implicit: bool
    text: str
    parsed_ok: bool
    disabled: bool
    range: "SourceRange"
    longhand_properties: list


@dataclass
class CSSMedia:
    text: str
    source: str
    source_url: str
    range: "SourceRange"
    style_sheet_id: "StyleSheetId"
    media_list: list


@dataclass
class MediaQuery:
    expressions: list
    active: bool


@dataclass
class MediaQueryExpression:
    value: float
    unit: str
    feature: str
    value_range: "SourceRange"
    computed_length: float


@dataclass
class CSSContainerQuery:
    text: str
    range: "SourceRange"
    style_sheet_id: "StyleSheetId"
    name: str
    physical_axes: "PhysicalAxes"
    logical_axes: "LogicalAxes"


@dataclass
class CSSSupports:
    text: str
    active: bool
    range: "SourceRange"
    style_sheet_id: "StyleSheetId"


@dataclass
class CSSScope:
    text: str
    range: "SourceRange"
    style_sheet_id: "StyleSheetId"


@dataclass
class CSSLayer:
    text: str
    range: "SourceRange"
    style_sheet_id: "StyleSheetId"


@dataclass
class CSSLayerData:
    name: str
    sub_layers: list
    order: float


@dataclass
class PlatformFontUsage:
    family_name: str
    is_custom_font: bool
    glyph_count: float


@dataclass
class FontVariationAxis:
    tag: str
    name: str
    min_value: float
    max_value: float
    default_value: float


@dataclass
class FontFace:
    font_family: str
    font_style: str
    font_variant: str
    font_weight: str
    font_stretch: str
    font_display: str
    unicode_range: str
    src: str
    platform_font_family: str
    font_variation_axes: list


@dataclass
class CSSTryRule:
    style_sheet_id: "StyleSheetId"
    origin: "StyleSheetOrigin"
    style: "CSSStyle"


@dataclass
class CSSPositionFallbackRule:
    name: "Value"
    try_rules: list


@dataclass
class CSSKeyframesRule:
    animation_name: "Value"
    keyframes: list


@dataclass
class CSSPropertyRegistration:
    property_name: str
    initial_value: "Value"
    inherits: bool
    syntax: str


@dataclass
class CSSPropertyRule:
    style_sheet_id: "StyleSheetId"
    origin: "StyleSheetOrigin"
    property_name: "Value"
    style: "CSSStyle"


@dataclass
class CSSKeyframeRule:
    style_sheet_id: "StyleSheetId"
    origin: "StyleSheetOrigin"
    key_text: "Value"
    style: "CSSStyle"


@dataclass
class StyleDeclarationEdit:
    style_sheet_id: "StyleSheetId"
    range: "SourceRange"
    text: str


@dataclass
class AddRuleReturnT:
    rule: "CSSRule"


@dataclass
class CollectClassNamesReturnT:
    class_names: list


@dataclass
class CreateStyleSheetReturnT:
    style_sheet_id: "StyleSheetId"


@dataclass
class GetBackgroundColorsReturnT:
    background_colors: list
    computed_font_size: str
    computed_font_weight: str


@dataclass
class GetComputedStyleForNodeReturnT:
    computed_style: list


@dataclass
class GetInlineStylesForNodeReturnT:
    inline_style: "CSSStyle"
    attributes_style: "CSSStyle"


@dataclass
class GetMatchedStylesForNodeReturnT:
    inline_style: "CSSStyle"
    attributes_style: "CSSStyle"
    matched_css_rules: list
    pseudo_elements: list
    inherited: list
    inherited_pseudo_elements: list
    css_keyframes_rules: list
    css_position_fallback_rules: list
    css_property_rules: list
    css_property_registrations: list
    parent_layout_node_id: "NodeId"


@dataclass
class GetMediaQueriesReturnT:
    medias: list


@dataclass
class GetPlatformFontsForNodeReturnT:
    fonts: list


@dataclass
class GetStyleSheetTextReturnT:
    text: str


@dataclass
class GetLayersForNodeReturnT:
    root_layer: "CSSLayerData"


@dataclass
class TakeComputedStyleUpdatesReturnT:
    node_ids: list


@dataclass
class SetKeyframeKeyReturnT:
    key_text: "Value"


@dataclass
class SetMediaTextReturnT:
    media: "CSSMedia"


@dataclass
class SetContainerQueryTextReturnT:
    container_query: "CSSContainerQuery"


@dataclass
class SetSupportsTextReturnT:
    supports: "CSSSupports"


@dataclass
class SetScopeTextReturnT:
    scope: "CSSScope"


@dataclass
class SetRuleSelectorReturnT:
    selector_list: "SelectorList"


@dataclass
class SetStyleSheetTextReturnT:
    source_map_url: str


@dataclass
class SetStyleTextsReturnT:
    styles: list


@dataclass
class StopRuleUsageTrackingReturnT:
    rule_usage: list


@dataclass
class TakeCoverageDeltaReturnT:
    coverage: list
    timestamp: float
