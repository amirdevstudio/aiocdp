# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from typing import (
    Any,
    Literal,
    TYPE_CHECKING
)
from dataclasses import (
    dataclass
)
if TYPE_CHECKING:
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

ArrayOfStrings = list['StringIndex']

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
    backend_node_id: 'BackendNodeId'
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
    frame_id: 'FrameId'
    content_document_index: int
    pseudo_type: 'PseudoType'
    shadow_root_type: 'ShadowRootType'
    is_clickable: bool
    event_listeners: list
    current_source_url: str
    origin_url: str
    scroll_offset_x: float
    scroll_offset_y: float
    def to_dict(
        self,
        casing_strategy: Literal[
            'snake',
            'camel',
            'pascal'
        ] = 'snake'
    ):

        if casing_strategy == 'snake':
            return {
                'node_type': self.node_type,
                'node_name': self.node_name,
                'node_value': self.node_value,
                'text_value': self.text_value,
                'input_value': self.input_value,
                'input_checked': self.input_checked,
                'option_selected': self.option_selected,
                'backend_node_id': self.backend_node_id.to_dict(
                    casing_strategy
                ),
                'child_node_indexes': self.child_node_indexes,
                'attributes': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.attributes
                ],
                'pseudo_element_indexes': self.pseudo_element_indexes,
                'layout_node_index': self.layout_node_index,
                'document_url': self.document_url,
                'base_url': self.base_url,
                'content_language': self.content_language,
                'document_encoding': self.document_encoding,
                'public_id': self.public_id,
                'system_id': self.system_id,
                'frame_id': self.frame_id.to_dict(
                    casing_strategy
                ),
                'content_document_index': self.content_document_index,
                'pseudo_type': self.pseudo_type,
                'shadow_root_type': self.shadow_root_type,
                'is_clickable': self.is_clickable,
                'event_listeners': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.event_listeners
                ],
                'current_source_url': self.current_source_url,
                'origin_url': self.origin_url,
                'scroll_offset_x': self.scroll_offset_x,
                'scroll_offset_y': self.scroll_offset_y,
            }
        if casing_strategy == 'camel':
            return {
                'nodeType': self.node_type,
                'nodeName': self.node_name,
                'nodeValue': self.node_value,
                'textValue': self.text_value,
                'inputValue': self.input_value,
                'inputChecked': self.input_checked,
                'optionSelected': self.option_selected,
                'backendNodeId': self.backend_node_id.to_dict(
                    casing_strategy
                ),
                'childNodeIndexes': self.child_node_indexes,
                'attributes': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.attributes
                ],
                'pseudoElementIndexes': self.pseudo_element_indexes,
                'layoutNodeIndex': self.layout_node_index,
                'documentURL': self.document_url,
                'baseURL': self.base_url,
                'contentLanguage': self.content_language,
                'documentEncoding': self.document_encoding,
                'publicId': self.public_id,
                'systemId': self.system_id,
                'frameId': self.frame_id.to_dict(
                    casing_strategy
                ),
                'contentDocumentIndex': self.content_document_index,
                'pseudoType': self.pseudo_type,
                'shadowRootType': self.shadow_root_type,
                'isClickable': self.is_clickable,
                'eventListeners': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.event_listeners
                ],
                'currentSourceURL': self.current_source_url,
                'originURL': self.origin_url,
                'scrollOffsetX': self.scroll_offset_x,
                'scrollOffsetY': self.scroll_offset_y,
            }
        if casing_strategy == 'pascal':
            return {
                'NodeType': self.node_type,
                'NodeName': self.node_name,
                'NodeValue': self.node_value,
                'TextValue': self.text_value,
                'InputValue': self.input_value,
                'InputChecked': self.input_checked,
                'OptionSelected': self.option_selected,
                'BackendNodeId': self.backend_node_id.to_dict(
                    casing_strategy
                ),
                'ChildNodeIndexes': self.child_node_indexes,
                'Attributes': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.attributes
                ],
                'PseudoElementIndexes': self.pseudo_element_indexes,
                'LayoutNodeIndex': self.layout_node_index,
                'DocumentURL': self.document_url,
                'BaseURL': self.base_url,
                'ContentLanguage': self.content_language,
                'DocumentEncoding': self.document_encoding,
                'PublicId': self.public_id,
                'SystemId': self.system_id,
                'FrameId': self.frame_id.to_dict(
                    casing_strategy
                ),
                'ContentDocumentIndex': self.content_document_index,
                'PseudoType': self.pseudo_type,
                'ShadowRootType': self.shadow_root_type,
                'IsClickable': self.is_clickable,
                'EventListeners': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.event_listeners
                ],
                'CurrentSourceURL': self.current_source_url,
                'OriginURL': self.origin_url,
                'ScrollOffsetX': self.scroll_offset_x,
                'ScrollOffsetY': self.scroll_offset_y,
            }


@dataclass
class InlineTextBox:
    bounding_box: 'Rect'
    start_character_index: int
    num_characters: int
    def to_dict(
        self,
        casing_strategy: Literal[
            'snake',
            'camel',
            'pascal'
        ] = 'snake'
    ):

        if casing_strategy == 'snake':
            return {
                'bounding_box': self.bounding_box.to_dict(
                    casing_strategy
                ),
                'start_character_index': self.start_character_index,
                'num_characters': self.num_characters,
            }
        if casing_strategy == 'camel':
            return {
                'boundingBox': self.bounding_box.to_dict(
                    casing_strategy
                ),
                'startCharacterIndex': self.start_character_index,
                'numCharacters': self.num_characters,
            }
        if casing_strategy == 'pascal':
            return {
                'BoundingBox': self.bounding_box.to_dict(
                    casing_strategy
                ),
                'StartCharacterIndex': self.start_character_index,
                'NumCharacters': self.num_characters,
            }


@dataclass
class LayoutTreeNode:
    dom_node_index: int
    bounding_box: 'Rect'
    layout_text: str
    inline_text_nodes: list
    style_index: int
    paint_order: int
    is_stacking_context: bool
    def to_dict(
        self,
        casing_strategy: Literal[
            'snake',
            'camel',
            'pascal'
        ] = 'snake'
    ):

        if casing_strategy == 'snake':
            return {
                'dom_node_index': self.dom_node_index,
                'bounding_box': self.bounding_box.to_dict(
                    casing_strategy
                ),
                'layout_text': self.layout_text,
                'inline_text_nodes': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.inline_text_nodes
                ],
                'style_index': self.style_index,
                'paint_order': self.paint_order,
                'is_stacking_context': self.is_stacking_context,
            }
        if casing_strategy == 'camel':
            return {
                'domNodeIndex': self.dom_node_index,
                'boundingBox': self.bounding_box.to_dict(
                    casing_strategy
                ),
                'layoutText': self.layout_text,
                'inlineTextNodes': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.inline_text_nodes
                ],
                'styleIndex': self.style_index,
                'paintOrder': self.paint_order,
                'isStackingContext': self.is_stacking_context,
            }
        if casing_strategy == 'pascal':
            return {
                'DomNodeIndex': self.dom_node_index,
                'BoundingBox': self.bounding_box.to_dict(
                    casing_strategy
                ),
                'LayoutText': self.layout_text,
                'InlineTextNodes': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.inline_text_nodes
                ],
                'StyleIndex': self.style_index,
                'PaintOrder': self.paint_order,
                'IsStackingContext': self.is_stacking_context,
            }


@dataclass
class ComputedStyle:
    properties: list
    def to_dict(
        self,
        casing_strategy: Literal[
            'snake',
            'camel',
            'pascal'
        ] = 'snake'
    ):

        if casing_strategy == 'snake':
            return {
                'properties': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.properties
                ],
            }
        if casing_strategy == 'camel':
            return {
                'properties': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.properties
                ],
            }
        if casing_strategy == 'pascal':
            return {
                'Properties': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.properties
                ],
            }


@dataclass
class NameValue:
    name: str
    value: str
    def to_dict(
        self,
        casing_strategy: Literal[
            'snake',
            'camel',
            'pascal'
        ] = 'snake'
    ):

        if casing_strategy == 'snake':
            return {
                'name': self.name,
                'value': self.value,
            }
        if casing_strategy == 'camel':
            return {
                'name': self.name,
                'value': self.value,
            }
        if casing_strategy == 'pascal':
            return {
                'Name': self.name,
                'Value': self.value,
            }


@dataclass
class RareStringData:
    index: list
    value: list
    def to_dict(
        self,
        casing_strategy: Literal[
            'snake',
            'camel',
            'pascal'
        ] = 'snake'
    ):

        if casing_strategy == 'snake':
            return {
                'index': self.index,
                'value': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.value
                ],
            }
        if casing_strategy == 'camel':
            return {
                'index': self.index,
                'value': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.value
                ],
            }
        if casing_strategy == 'pascal':
            return {
                'Index': self.index,
                'Value': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.value
                ],
            }


@dataclass
class RareBooleanData:
    index: list
    def to_dict(
        self,
        casing_strategy: Literal[
            'snake',
            'camel',
            'pascal'
        ] = 'snake'
    ):

        if casing_strategy == 'snake':
            return {
                'index': self.index,
            }
        if casing_strategy == 'camel':
            return {
                'index': self.index,
            }
        if casing_strategy == 'pascal':
            return {
                'Index': self.index,
            }


@dataclass
class RareIntegerData:
    index: list
    value: list
    def to_dict(
        self,
        casing_strategy: Literal[
            'snake',
            'camel',
            'pascal'
        ] = 'snake'
    ):

        if casing_strategy == 'snake':
            return {
                'index': self.index,
                'value': self.value,
            }
        if casing_strategy == 'camel':
            return {
                'index': self.index,
                'value': self.value,
            }
        if casing_strategy == 'pascal':
            return {
                'Index': self.index,
                'Value': self.value,
            }


@dataclass
class DocumentSnapshot:
    document_url: 'StringIndex'
    title: 'StringIndex'
    base_url: 'StringIndex'
    content_language: 'StringIndex'
    encoding_name: 'StringIndex'
    public_id: 'StringIndex'
    system_id: 'StringIndex'
    frame_id: 'StringIndex'
    nodes: 'NodeTreeSnapshot'
    layout: 'LayoutTreeSnapshot'
    text_boxes: 'TextBoxSnapshot'
    scroll_offset_x: float
    scroll_offset_y: float
    content_width: float
    content_height: float
    def to_dict(
        self,
        casing_strategy: Literal[
            'snake',
            'camel',
            'pascal'
        ] = 'snake'
    ):

        if casing_strategy == 'snake':
            return {
                'document_url': self.document_url.to_dict(
                    casing_strategy
                ),
                'title': self.title.to_dict(
                    casing_strategy
                ),
                'base_url': self.base_url.to_dict(
                    casing_strategy
                ),
                'content_language': self.content_language.to_dict(
                    casing_strategy
                ),
                'encoding_name': self.encoding_name.to_dict(
                    casing_strategy
                ),
                'public_id': self.public_id.to_dict(
                    casing_strategy
                ),
                'system_id': self.system_id.to_dict(
                    casing_strategy
                ),
                'frame_id': self.frame_id.to_dict(
                    casing_strategy
                ),
                'nodes': self.nodes.to_dict(
                    casing_strategy
                ),
                'layout': self.layout.to_dict(
                    casing_strategy
                ),
                'text_boxes': self.text_boxes.to_dict(
                    casing_strategy
                ),
                'scroll_offset_x': self.scroll_offset_x,
                'scroll_offset_y': self.scroll_offset_y,
                'content_width': self.content_width,
                'content_height': self.content_height,
            }
        if casing_strategy == 'camel':
            return {
                'documentURL': self.document_url.to_dict(
                    casing_strategy
                ),
                'title': self.title.to_dict(
                    casing_strategy
                ),
                'baseURL': self.base_url.to_dict(
                    casing_strategy
                ),
                'contentLanguage': self.content_language.to_dict(
                    casing_strategy
                ),
                'encodingName': self.encoding_name.to_dict(
                    casing_strategy
                ),
                'publicId': self.public_id.to_dict(
                    casing_strategy
                ),
                'systemId': self.system_id.to_dict(
                    casing_strategy
                ),
                'frameId': self.frame_id.to_dict(
                    casing_strategy
                ),
                'nodes': self.nodes.to_dict(
                    casing_strategy
                ),
                'layout': self.layout.to_dict(
                    casing_strategy
                ),
                'textBoxes': self.text_boxes.to_dict(
                    casing_strategy
                ),
                'scrollOffsetX': self.scroll_offset_x,
                'scrollOffsetY': self.scroll_offset_y,
                'contentWidth': self.content_width,
                'contentHeight': self.content_height,
            }
        if casing_strategy == 'pascal':
            return {
                'DocumentURL': self.document_url.to_dict(
                    casing_strategy
                ),
                'Title': self.title.to_dict(
                    casing_strategy
                ),
                'BaseURL': self.base_url.to_dict(
                    casing_strategy
                ),
                'ContentLanguage': self.content_language.to_dict(
                    casing_strategy
                ),
                'EncodingName': self.encoding_name.to_dict(
                    casing_strategy
                ),
                'PublicId': self.public_id.to_dict(
                    casing_strategy
                ),
                'SystemId': self.system_id.to_dict(
                    casing_strategy
                ),
                'FrameId': self.frame_id.to_dict(
                    casing_strategy
                ),
                'Nodes': self.nodes.to_dict(
                    casing_strategy
                ),
                'Layout': self.layout.to_dict(
                    casing_strategy
                ),
                'TextBoxes': self.text_boxes.to_dict(
                    casing_strategy
                ),
                'ScrollOffsetX': self.scroll_offset_x,
                'ScrollOffsetY': self.scroll_offset_y,
                'ContentWidth': self.content_width,
                'ContentHeight': self.content_height,
            }


@dataclass
class NodeTreeSnapshot:
    parent_index: list
    node_type: list
    shadow_root_type: 'RareStringData'
    node_name: list
    node_value: list
    backend_node_id: list
    attributes: list
    text_value: 'RareStringData'
    input_value: 'RareStringData'
    input_checked: 'RareBooleanData'
    option_selected: 'RareBooleanData'
    content_document_index: 'RareIntegerData'
    pseudo_type: 'RareStringData'
    pseudo_identifier: 'RareStringData'
    is_clickable: 'RareBooleanData'
    current_source_url: 'RareStringData'
    origin_url: 'RareStringData'
    def to_dict(
        self,
        casing_strategy: Literal[
            'snake',
            'camel',
            'pascal'
        ] = 'snake'
    ):

        if casing_strategy == 'snake':
            return {
                'parent_index': self.parent_index,
                'node_type': self.node_type,
                'shadow_root_type': self.shadow_root_type.to_dict(
                    casing_strategy
                ),
                'node_name': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.node_name
                ],
                'node_value': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.node_value
                ],
                'backend_node_id': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.backend_node_id
                ],
                'attributes': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.attributes
                ],
                'text_value': self.text_value.to_dict(
                    casing_strategy
                ),
                'input_value': self.input_value.to_dict(
                    casing_strategy
                ),
                'input_checked': self.input_checked.to_dict(
                    casing_strategy
                ),
                'option_selected': self.option_selected.to_dict(
                    casing_strategy
                ),
                'content_document_index': self.content_document_index.to_dict(
                    casing_strategy
                ),
                'pseudo_type': self.pseudo_type.to_dict(
                    casing_strategy
                ),
                'pseudo_identifier': self.pseudo_identifier.to_dict(
                    casing_strategy
                ),
                'is_clickable': self.is_clickable.to_dict(
                    casing_strategy
                ),
                'current_source_url': self.current_source_url.to_dict(
                    casing_strategy
                ),
                'origin_url': self.origin_url.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'camel':
            return {
                'parentIndex': self.parent_index,
                'nodeType': self.node_type,
                'shadowRootType': self.shadow_root_type.to_dict(
                    casing_strategy
                ),
                'nodeName': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.node_name
                ],
                'nodeValue': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.node_value
                ],
                'backendNodeId': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.backend_node_id
                ],
                'attributes': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.attributes
                ],
                'textValue': self.text_value.to_dict(
                    casing_strategy
                ),
                'inputValue': self.input_value.to_dict(
                    casing_strategy
                ),
                'inputChecked': self.input_checked.to_dict(
                    casing_strategy
                ),
                'optionSelected': self.option_selected.to_dict(
                    casing_strategy
                ),
                'contentDocumentIndex': self.content_document_index.to_dict(
                    casing_strategy
                ),
                'pseudoType': self.pseudo_type.to_dict(
                    casing_strategy
                ),
                'pseudoIdentifier': self.pseudo_identifier.to_dict(
                    casing_strategy
                ),
                'isClickable': self.is_clickable.to_dict(
                    casing_strategy
                ),
                'currentSourceURL': self.current_source_url.to_dict(
                    casing_strategy
                ),
                'originURL': self.origin_url.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'pascal':
            return {
                'ParentIndex': self.parent_index,
                'NodeType': self.node_type,
                'ShadowRootType': self.shadow_root_type.to_dict(
                    casing_strategy
                ),
                'NodeName': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.node_name
                ],
                'NodeValue': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.node_value
                ],
                'BackendNodeId': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.backend_node_id
                ],
                'Attributes': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.attributes
                ],
                'TextValue': self.text_value.to_dict(
                    casing_strategy
                ),
                'InputValue': self.input_value.to_dict(
                    casing_strategy
                ),
                'InputChecked': self.input_checked.to_dict(
                    casing_strategy
                ),
                'OptionSelected': self.option_selected.to_dict(
                    casing_strategy
                ),
                'ContentDocumentIndex': self.content_document_index.to_dict(
                    casing_strategy
                ),
                'PseudoType': self.pseudo_type.to_dict(
                    casing_strategy
                ),
                'PseudoIdentifier': self.pseudo_identifier.to_dict(
                    casing_strategy
                ),
                'IsClickable': self.is_clickable.to_dict(
                    casing_strategy
                ),
                'CurrentSourceURL': self.current_source_url.to_dict(
                    casing_strategy
                ),
                'OriginURL': self.origin_url.to_dict(
                    casing_strategy
                ),
            }


@dataclass
class LayoutTreeSnapshot:
    node_index: list
    styles: list
    bounds: list
    text: list
    stacking_contexts: 'RareBooleanData'
    paint_orders: list
    offset_rects: list
    scroll_rects: list
    client_rects: list
    blended_background_colors: list
    text_color_opacities: list
    def to_dict(
        self,
        casing_strategy: Literal[
            'snake',
            'camel',
            'pascal'
        ] = 'snake'
    ):

        if casing_strategy == 'snake':
            return {
                'node_index': self.node_index,
                'styles': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.styles
                ],
                'bounds': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.bounds
                ],
                'text': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.text
                ],
                'stacking_contexts': self.stacking_contexts.to_dict(
                    casing_strategy
                ),
                'paint_orders': self.paint_orders,
                'offset_rects': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.offset_rects
                ],
                'scroll_rects': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.scroll_rects
                ],
                'client_rects': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.client_rects
                ],
                'blended_background_colors': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.blended_background_colors
                ],
                'text_color_opacities': self.text_color_opacities,
            }
        if casing_strategy == 'camel':
            return {
                'nodeIndex': self.node_index,
                'styles': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.styles
                ],
                'bounds': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.bounds
                ],
                'text': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.text
                ],
                'stackingContexts': self.stacking_contexts.to_dict(
                    casing_strategy
                ),
                'paintOrders': self.paint_orders,
                'offsetRects': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.offset_rects
                ],
                'scrollRects': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.scroll_rects
                ],
                'clientRects': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.client_rects
                ],
                'blendedBackgroundColors': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.blended_background_colors
                ],
                'textColorOpacities': self.text_color_opacities,
            }
        if casing_strategy == 'pascal':
            return {
                'NodeIndex': self.node_index,
                'Styles': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.styles
                ],
                'Bounds': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.bounds
                ],
                'Text': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.text
                ],
                'StackingContexts': self.stacking_contexts.to_dict(
                    casing_strategy
                ),
                'PaintOrders': self.paint_orders,
                'OffsetRects': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.offset_rects
                ],
                'ScrollRects': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.scroll_rects
                ],
                'ClientRects': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.client_rects
                ],
                'BlendedBackgroundColors': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.blended_background_colors
                ],
                'TextColorOpacities': self.text_color_opacities,
            }


@dataclass
class TextBoxSnapshot:
    layout_index: list
    bounds: list
    start: list
    length: list
    def to_dict(
        self,
        casing_strategy: Literal[
            'snake',
            'camel',
            'pascal'
        ] = 'snake'
    ):

        if casing_strategy == 'snake':
            return {
                'layout_index': self.layout_index,
                'bounds': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.bounds
                ],
                'start': self.start,
                'length': self.length,
            }
        if casing_strategy == 'camel':
            return {
                'layoutIndex': self.layout_index,
                'bounds': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.bounds
                ],
                'start': self.start,
                'length': self.length,
            }
        if casing_strategy == 'pascal':
            return {
                'LayoutIndex': self.layout_index,
                'Bounds': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.bounds
                ],
                'Start': self.start,
                'Length': self.length,
            }


@dataclass
class GetSnapshotReturnT:
    dom_nodes: list
    layout_tree_nodes: list
    computed_styles: list


@dataclass
class CaptureSnapshotReturnT:
    documents: list
    strings: list
