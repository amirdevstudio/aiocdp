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
if TYPE_CHECKING:
    from cdp.target.connection import (
        IResponse
    )


@dataclass
class PerformanceTimeline(BaseDomain):
    def enable(
            self,
            event_types: list
    ) -> IResponse[None]:
        params = {
            'eventTypes': event_types,
        }

        return self._send_command(
            'PerformanceTimeline.enable',
            params,
            False
        )
