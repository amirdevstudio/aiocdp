from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

GraphObjectId = str

NodeType = str

ParamType = str

ContextType = Literal[
    "realtime",
    "offline"
]

ContextState = Literal[
    "suspended",
    "running",
    "closed"
]

ChannelCountMode = Literal[
    "clamped-max",
    "explicit",
    "max"
]

ChannelInterpretation = Literal[
    "discrete",
    "speakers"
]

AutomationRate = Literal[
    "a-rate",
    "k-rate"
]


@dataclass
class ContextRealtimeData:
    current_time: float
    render_capacity: float
    callback_interval_mean: float
    callback_interval_variance: float


@dataclass
class BaseAudioContext:
    context_id: "GraphObjectId"
    context_type: "ContextType"
    context_state: "ContextState"
    realtime_data: "ContextRealtimeData"
    callback_buffer_size: float
    max_output_channel_count: float
    sample_rate: float


@dataclass
class AudioListener:
    listener_id: "GraphObjectId"
    context_id: "GraphObjectId"


@dataclass
class AudioNode:
    node_id: "GraphObjectId"
    context_id: "GraphObjectId"
    node_type: "NodeType"
    number_of_inputs: float
    number_of_outputs: float
    channel_count: float
    channel_count_mode: "ChannelCountMode"
    channel_interpretation: "ChannelInterpretation"


@dataclass
class AudioParam:
    param_id: "GraphObjectId"
    node_id: "GraphObjectId"
    context_id: "GraphObjectId"
    param_type: "ParamType"
    rate: "AutomationRate"
    default_value: float
    min_value: float
    max_value: float


@dataclass
class GetRealtimeDataReturnT:
    realtime_data: "ContextRealtimeData"
