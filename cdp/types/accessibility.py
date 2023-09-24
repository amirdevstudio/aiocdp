# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.
from cdp.types import (
    dom,
    runtime
)
from cdp.types import page
from typing import (
    Any,
    Literal,
    NotRequired,
    TypedDict
)

AXNodeId = str

AXValueType = Literal[
    'boolean',
    'tristate',
    'booleanOrUndefined',
    'idref',
    'idrefList',
    'integer',
    'node',
    'nodeList',
    'number',
    'string',
    'computedString',
    'token',
    'tokenList',
    'domRelation',
    'role',
    'internalRole',
    'valueUndefined'
]

AXValueSourceType = Literal[
    'attribute',
    'implicit',
    'style',
    'contents',
    'placeholder',
    'relatedElement'
]

AXValueNativeSourceType = Literal[
    'description',
    'figcaption',
    'label',
    'labelfor',
    'labelwrapped',
    'legend',
    'rubyannotation',
    'tablecaption',
    'title',
    'other'
]

AXPropertyName = Literal[
    'busy',
    'disabled',
    'editable',
    'focusable',
    'focused',
    'hidden',
    'hiddenRoot',
    'invalid',
    'keyshortcuts',
    'settable',
    'roledescription',
    'live',
    'atomic',
    'relevant',
    'root',
    'autocomplete',
    'hasPopup',
    'level',
    'multiselectable',
    'orientation',
    'multiline',
    'readonly',
    'required',
    'valuemin',
    'valuemax',
    'valuetext',
    'checked',
    'expanded',
    'modal',
    'pressed',
    'selected',
    'activedescendant',
    'controls',
    'describedby',
    'details',
    'errormessage',
    'flowto',
    'labelledby',
    'owns'
]


class AXValueSource(TypedDict):
    type: 'AXValueSourceType'
    value: NotRequired['AXValue']
    attribute: NotRequired[str]
    attribute_value: NotRequired['AXValue']
    superseded: NotRequired[bool]
    native_source: NotRequired['AXValueNativeSourceType']
    native_source_value: NotRequired['AXValue']
    invalid: NotRequired[bool]
    invalid_reason: NotRequired[str]


class AXRelatedNode(TypedDict):
    backend_dom_node_id: 'dom.BackendNodeId'
    idref: NotRequired[str]
    text: NotRequired[str]


class AXProperty(TypedDict):
    name: 'AXPropertyName'
    value: 'AXValue'


class AXValue(TypedDict):
    type: 'AXValueType'
    value: NotRequired[Any]
    related_nodes: NotRequired[list]
    sources: NotRequired[list]


class AXNode(TypedDict):
    node_id: 'AXNodeId'
    ignored: bool
    ignored_reasons: NotRequired[list]
    role: NotRequired['AXValue']
    chrome_role: NotRequired['AXValue']
    name: NotRequired['AXValue']
    description: NotRequired['AXValue']
    value: NotRequired['AXValue']
    properties: NotRequired[list]
    parent_id: NotRequired['AXNodeId']
    child_ids: NotRequired[list]
    backend_dom_node_id: NotRequired['dom.BackendNodeId']
    frame_id: NotRequired['page.FrameId']


class GetPartialAXTreeParamsT(TypedDict):
    node_id: NotRequired['dom.NodeId']
    backend_node_id: NotRequired['dom.BackendNodeId']
    object_id: NotRequired['runtime.RemoteObjectId']
    fetch_relatives: NotRequired[bool]


class GetFullAXTreeParamsT(TypedDict):
    depth: NotRequired[int]
    frame_id: NotRequired['page.FrameId']


class GetRootAXNodeParamsT(TypedDict):
    frame_id: NotRequired['page.FrameId']


class GetAXNodeAndAncestorsParamsT(TypedDict):
    node_id: NotRequired['dom.NodeId']
    backend_node_id: NotRequired['dom.BackendNodeId']
    object_id: NotRequired['runtime.RemoteObjectId']


class GetChildAXNodesParamsT(TypedDict):
    id: 'AXNodeId'
    frame_id: NotRequired['page.FrameId']


class QueryAXTreeParamsT(TypedDict):
    node_id: NotRequired['dom.NodeId']
    backend_node_id: NotRequired['dom.BackendNodeId']
    object_id: NotRequired['runtime.RemoteObjectId']
    accessible_name: NotRequired[str]
    role: NotRequired[str]


class GetPartialAXTreeReturnT(TypedDict):
    nodes: list


class GetFullAXTreeReturnT(TypedDict):
    nodes: list


class GetRootAXNodeReturnT(TypedDict):
    node: 'AXNode'


class GetAXNodeAndAncestorsReturnT(TypedDict):
    nodes: list


class GetChildAXNodesReturnT(TypedDict):
    nodes: list


class QueryAXTreeReturnT(TypedDict):
    nodes: list


class LoadCompleteEventT(TypedDict):
    name: Literal['load_complete']
    params: 'LoadCompleteParamsT'


class NodesUpdatedEventT(TypedDict):
    name: Literal['nodes_updated']
    params: 'NodesUpdatedParamsT'


class LoadCompleteParamsT(TypedDict):
    root: 'AXNode'


class NodesUpdatedParamsT(TypedDict):
    nodes: list