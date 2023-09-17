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
    from_dict,
    to_dict
)
from cdp.domains.memory.types import (
    GetAllTimeSamplingProfileReturnT,
    GetBrowserSamplingProfileReturnT,
    GetDOMCountersReturnT,
    GetSamplingProfileReturnT,
    PressureLevel
)
if TYPE_CHECKING:
    from cdp.target.connection import (
        IFutureResponse
    )


@dataclass
class Memory(BaseDomain):
    def get_dom_counters(
            self
    ) -> 'IFutureResponse[GetDOMCountersReturnT]':
        params = {}

        return self._send_command(
            'Memory.getDOMCounters',
            params,
            True,
            lambda data: from_dict(
                GetDOMCountersReturnT,
                data,
                'camel'
            )
        )

    def prepare_for_leak_detection(
            self
    ) -> 'IFutureResponse[None]':
        params = {}

        return self._send_command(
            'Memory.prepareForLeakDetection',
            params,
            False
        )

    def forcibly_purge_java_script_memory(
            self
    ) -> 'IFutureResponse[None]':
        params = {}

        return self._send_command(
            'Memory.forciblyPurgeJavaScriptMemory',
            params,
            False
        )

    def set_pressure_notifications_suppressed(
            self,
            suppressed: 'bool'
    ) -> 'IFutureResponse[None]':
        params = {
            'suppressed': suppressed,
        }

        return self._send_command(
            'Memory.setPressureNotificationsSuppressed',
            params,
            False
        )

    def simulate_pressure_notification(
            self,
            level: 'PressureLevel'
    ) -> 'IFutureResponse[None]':
        params = {
            'level': level,
        }

        return self._send_command(
            'Memory.simulatePressureNotification',
            params,
            False
        )

    def start_sampling(
            self,
            sampling_interval: 'int' = UNDEFINED,
            suppress_randomness: 'bool' = UNDEFINED
    ) -> 'IFutureResponse[None]':
        params = {}

        if is_defined(sampling_interval):
            params['samplingInterval'] = sampling_interval

        if is_defined(suppress_randomness):
            params['suppressRandomness'] = suppress_randomness

        return self._send_command(
            'Memory.startSampling',
            params,
            False
        )

    def stop_sampling(
            self
    ) -> 'IFutureResponse[None]':
        params = {}

        return self._send_command(
            'Memory.stopSampling',
            params,
            False
        )

    def get_all_time_sampling_profile(
            self
    ) -> 'IFutureResponse[GetAllTimeSamplingProfileReturnT]':
        params = {}

        return self._send_command(
            'Memory.getAllTimeSamplingProfile',
            params,
            True,
            lambda data: from_dict(
                GetAllTimeSamplingProfileReturnT,
                data,
                'camel'
            )
        )

    def get_browser_sampling_profile(
            self
    ) -> 'IFutureResponse[GetBrowserSamplingProfileReturnT]':
        params = {}

        return self._send_command(
            'Memory.getBrowserSamplingProfile',
            params,
            True,
            lambda data: from_dict(
                GetBrowserSamplingProfileReturnT,
                data,
                'camel'
            )
        )

    def get_sampling_profile(
            self
    ) -> 'IFutureResponse[GetSamplingProfileReturnT]':
        params = {}

        return self._send_command(
            'Memory.getSamplingProfile',
            params,
            True,
            lambda data: from_dict(
                GetSamplingProfileReturnT,
                data,
                'camel'
            )
        )
