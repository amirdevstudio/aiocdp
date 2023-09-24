# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.
from cdp.types import (
    dom
)
from cdp.types import page, network
from typing import (
    Literal,
    NotRequired,
    TypedDict
)


class LargestContentfulPaint(TypedDict):
    render_time: 'network.TimeSinceEpoch'
    load_time: 'network.TimeSinceEpoch'
    size: float
    element_id: NotRequired[str]
    url: NotRequired[str]
    node_id: NotRequired['dom.BackendNodeId']


class LayoutShiftAttribution(TypedDict):
    previous_rect: 'dom.Rect'
    current_rect: 'dom.Rect'
    node_id: NotRequired['dom.BackendNodeId']


class LayoutShift(TypedDict):
    value: float
    had_recent_input: bool
    last_input_time: 'network.TimeSinceEpoch'
    sources: list


class TimelineEvent(TypedDict):
    frame_id: 'page.FrameId'
    type: str
    name: str
    time: 'network.TimeSinceEpoch'
    duration: NotRequired[float]
    lcp_details: NotRequired['LargestContentfulPaint']
    layout_shift_details: NotRequired['LayoutShift']


class EnableParamsT(TypedDict):
    event_types: list


class TimelineEventAddedEventT(TypedDict):
    name: Literal['timeline_event_added']
    params: 'TimelineEventAddedParamsT'


class TimelineEventAddedParamsT(TypedDict):
    event: 'TimelineEvent'