from cdp.domains.base import (
    BaseDomain
)
from dataclasses import (
    dataclass
)
from cdp.domains.background_service.types import (
    ServiceName
)
from cdp.utils import (
    is_defined,
    UNDEFINED
)


@dataclass
class BackgroundService(BaseDomain):
    def start_observing(
        self,
        service: ServiceName
    ):
        params = {
            "service": service,
        }

        return self._send_command(
            "BackgroundService.startObserving",
            params
        )

    def stop_observing(
        self,
        service: ServiceName
    ):
        params = {
            "service": service,
        }

        return self._send_command(
            "BackgroundService.stopObserving",
            params
        )

    def set_recording(
        self,
        should_record: bool,
        service: ServiceName
    ):
        params = {
            "shouldRecord": should_record,
            "service": service,
        }

        return self._send_command(
            "BackgroundService.setRecording",
            params
        )

    def clear_events(
        self,
        service: ServiceName
    ):
        params = {
            "service": service,
        }

        return self._send_command(
            "BackgroundService.clearEvents",
            params
        )

