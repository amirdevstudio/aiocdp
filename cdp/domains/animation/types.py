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
        BackendNodeId
    )
    from cdp.domains.runtime.types import (
        RemoteObject
    )


@dataclass
class Animation:
    id: str
    name: str
    paused_state: bool
    play_state: str
    playback_rate: float
    start_time: float
    current_time: float
    type: str
    source: 'AnimationEffect'
    css_id: str
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
                'id': self.id_,
                'name': self.name,
                'paused_state': self.paused_state,
                'play_state': self.play_state,
                'playback_rate': self.playback_rate,
                'start_time': self.start_time,
                'current_time': self.current_time,
                'type': self.type_,
                'source': self.source.to_dict(
                    casing_strategy
                ),
                'css_id': self.css_id,
            }
        if casing_strategy == 'camel':
            return {
                'id': self.id_,
                'name': self.name,
                'pausedState': self.paused_state,
                'playState': self.play_state,
                'playbackRate': self.playback_rate,
                'startTime': self.start_time,
                'currentTime': self.current_time,
                'type': self.type_,
                'source': self.source.to_dict(
                    casing_strategy
                ),
                'cssId': self.css_id,
            }
        if casing_strategy == 'pascal':
            return {
                'Id': self.id_,
                'Name': self.name,
                'PausedState': self.paused_state,
                'PlayState': self.play_state,
                'PlaybackRate': self.playback_rate,
                'StartTime': self.start_time,
                'CurrentTime': self.current_time,
                'Type': self.type_,
                'Source': self.source.to_dict(
                    casing_strategy
                ),
                'CssId': self.css_id,
            }


@dataclass
class AnimationEffect:
    delay: float
    end_delay: float
    iteration_start: float
    iterations: float
    duration: float
    direction: str
    fill: str
    backend_node_id: 'BackendNodeId'
    keyframes_rule: 'KeyframesRule'
    easing: str
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
                'delay': self.delay,
                'end_delay': self.end_delay,
                'iteration_start': self.iteration_start,
                'iterations': self.iterations,
                'duration': self.duration,
                'direction': self.direction,
                'fill': self.fill,
                'backend_node_id': self.backend_node_id.to_dict(
                    casing_strategy
                ),
                'keyframes_rule': self.keyframes_rule.to_dict(
                    casing_strategy
                ),
                'easing': self.easing,
            }
        if casing_strategy == 'camel':
            return {
                'delay': self.delay,
                'endDelay': self.end_delay,
                'iterationStart': self.iteration_start,
                'iterations': self.iterations,
                'duration': self.duration,
                'direction': self.direction,
                'fill': self.fill,
                'backendNodeId': self.backend_node_id.to_dict(
                    casing_strategy
                ),
                'keyframesRule': self.keyframes_rule.to_dict(
                    casing_strategy
                ),
                'easing': self.easing,
            }
        if casing_strategy == 'pascal':
            return {
                'Delay': self.delay,
                'EndDelay': self.end_delay,
                'IterationStart': self.iteration_start,
                'Iterations': self.iterations,
                'Duration': self.duration,
                'Direction': self.direction,
                'Fill': self.fill,
                'BackendNodeId': self.backend_node_id.to_dict(
                    casing_strategy
                ),
                'KeyframesRule': self.keyframes_rule.to_dict(
                    casing_strategy
                ),
                'Easing': self.easing,
            }


@dataclass
class KeyframesRule:
    name: str
    keyframes: list
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
                'keyframes': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.keyframes
                ],
            }
        if casing_strategy == 'camel':
            return {
                'name': self.name,
                'keyframes': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.keyframes
                ],
            }
        if casing_strategy == 'pascal':
            return {
                'Name': self.name,
                'Keyframes': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.keyframes
                ],
            }


@dataclass
class KeyframeStyle:
    offset: str
    easing: str
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
                'offset': self.offset,
                'easing': self.easing,
            }
        if casing_strategy == 'camel':
            return {
                'offset': self.offset,
                'easing': self.easing,
            }
        if casing_strategy == 'pascal':
            return {
                'Offset': self.offset,
                'Easing': self.easing,
            }


@dataclass
class GetCurrentTimeReturnT:
    current_time: float


@dataclass
class GetPlaybackRateReturnT:
    playback_rate: float


@dataclass
class ResolveAnimationReturnT:
    remote_object: 'RemoteObject'
