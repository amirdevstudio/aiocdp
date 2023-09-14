from dataclasses import (
    dataclass
)
from cdp.domains.dom.types import (
    BackendNodeId,
    PseudoType,
    Rect,
    ShadowRootType
)
from cdp.domains.page.types import (
    FrameId
)

StringIndex = int

Rectangle = list[float]


@dataclass
class DOMNode:
    node_type: int
    node_name: str
    node_value: str
    text_value: str
    input_value: str
    input_checked: bool
    option_selected: bool
    backend_node_id: "BackendNodeId"
    child_node_indexes: list
    attributes: list
    pseudo_element_indexes: list
    layout_node_index: int
    document_url: str
    base_url: str
    content_language: str
    document_encoding: str
    public_id: str
    system_id: str
    frame_id: "FrameId"
    content_document_index: int
    pseudo_type: "PseudoType"
    shadow_root_type: "ShadowRootType"
    is_clickable: bool
    event_listeners: list
    current_source_url: str
    origin_url: str
    scroll_offset_x: float
    scroll_offset_y: float


@dataclass
class InlineTextBox:
    bounding_box: "Rect"
    start_character_index: int
    num_characters: int


@dataclass
class LayoutTreeNode:
    dom_node_index: int
    bounding_box: "Rect"
    layout_text: str
    inline_text_nodes: list
    style_index: int
    paint_order: int
    is_stacking_context: bool


@dataclass
class ComputedStyle:
    properties: list


@dataclass
class NameValue:
    name: str
    value: str


@dataclass
class RareStringData:
    index: list
    value: list


@dataclass
class RareBooleanData:
    index: list


@dataclass
class RareIntegerData:
    index: list
    value: list


@dataclass
class DocumentSnapshot:
    document_url: "StringIndex"
    title: "StringIndex"
    base_url: "StringIndex"
    content_language: "StringIndex"
    encoding_name: "StringIndex"
    public_id: "StringIndex"
    system_id: "StringIndex"
    frame_id: "StringIndex"
    nodes: "NodeTreeSnapshot"
    layout: "LayoutTreeSnapshot"
    text_boxes: "TextBoxSnapshot"
    scroll_offset_x: float
    scroll_offset_y: float
    content_width: float
    content_height: float


@dataclass
class NodeTreeSnapshot:
    parent_index: list
    node_type: list
    shadow_root_type: "RareStringData"
    node_name: list
    node_value: list
    backend_node_id: list
    attributes: list
    text_value: "RareStringData"
    input_value: "RareStringData"
    input_checked: "RareBooleanData"
    option_selected: "RareBooleanData"
    content_document_index: "RareIntegerData"
    pseudo_type: "RareStringData"
    pseudo_identifier: "RareStringData"
    is_clickable: "RareBooleanData"
    current_source_url: "RareStringData"
    origin_url: "RareStringData"


@dataclass
class LayoutTreeSnapshot:
    node_index: list
    styles: list
    bounds: list
    text: list
    stacking_contexts: "RareBooleanData"
    paint_orders: list
    offset_rects: list
    scroll_rects: list
    client_rects: list
    blended_background_colors: list
    text_color_opacities: list


@dataclass
class TextBoxSnapshot:
    layout_index: list
    bounds: list
    start: list
    length: list


@dataclass
class GetSnapshotReturnT:
    dom_nodes: list
    layout_tree_nodes: list
    computed_styles: list


@dataclass
class CaptureSnapshotReturnT:
    documents: list
    strings: list
