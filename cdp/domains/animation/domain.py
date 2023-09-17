# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from cdp.domains.base import (
    BaseDomain
)
from dataclasses import (
    dataclass
)
from cdp.utils import (
    is_defined,
    UNDEFINED
)
from typing import (
    TYPE_CHECKING
)
from cdp.domains.mapper import (
    from_dict
)
from cdp.domains.animation.types import (
    GetCurrentTimeReturnT,
    GetPlaybackRateReturnT,
    ResolveAnimationReturnT
)
if TYPE_CHECKING:
    from cdp.target.connection import (
        IResponse
    )


@dataclass
class Animation(BaseDomain):
    def disable(
            self
    ) -> IResponse[None]:
        params = {}

        return self._send_command(
            'Animation.disable',
            params,
            False
        )

    def enable(
            self
    ) -> IResponse[None]:
        params = {}

        return self._send_command(
            'Animation.enable',
            params,
            False
        )

    def get_current_time(
            self,
            id_: str
    ) -> IResponse['GetCurrentTimeReturnT']:
        params = {
            'id': id_,
        }

        return self._send_command(
            'Animation.getCurrentTime',
            params,
            True,
            lambda data: from_dict(
                GetCurrentTimeReturnT,
                data,
                'camel'
            )
        )

    def get_playback_rate(
            self
    ) -> IResponse['GetPlaybackRateReturnT']:
        params = {}

        return self._send_command(
            'Animation.getPlaybackRate',
            params,
            True,
            lambda data: from_dict(
                GetPlaybackRateReturnT,
                data,
                'camel'
            )
        )

    def release_animations(
            self,
            animations: list
    ) -> IResponse[None]:
        params = {
            'animations': animations,
        }

        return self._send_command(
            'Animation.releaseAnimations',
            params,
            False
        )

    def resolve_animation(
            self,
            animation_id: str
    ) -> IResponse['ResolveAnimationReturnT']:
        params = {
            'animationId': animation_id,
        }

        return self._send_command(
            'Animation.resolveAnimation',
            params,
            True,
            lambda data: from_dict(
                ResolveAnimationReturnT,
                data,
                'camel'
            )
        )

    def seek_animations(
            self,
            animations: list,
            current_time: float
    ) -> IResponse[None]:
        params = {
            'animations': animations,
            'currentTime': current_time,
        }

        return self._send_command(
            'Animation.seekAnimations',
            params,
            False
        )

    def set_paused(
            self,
            animations: list,
            paused: bool
    ) -> IResponse[None]:
        params = {
            'animations': animations,
            'paused': paused,
        }

        return self._send_command(
            'Animation.setPaused',
            params,
            False
        )

    def set_playback_rate(
            self,
            playback_rate: float
    ) -> IResponse[None]:
        params = {
            'playbackRate': playback_rate,
        }

        return self._send_command(
            'Animation.setPlaybackRate',
            params,
            False
        )

    def set_timing(
            self,
            animation_id: str,
            duration: float,
            delay: float
    ) -> IResponse[None]:
        params = {
            'animationId': animation_id,
            'duration': duration,
            'delay': delay,
        }

        return self._send_command(
            'Animation.setTiming',
            params,
            False
        )
