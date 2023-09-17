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
if TYPE_CHECKING:
    from cdp.target.connection import (
        IFutureResponse
    )


@dataclass
class DeviceOrientation(BaseDomain):
    def clear_device_orientation_override(
            self
    ) -> 'IFutureResponse[None]':
        params = {}

        return self._send_command(
            'DeviceOrientation.clearDeviceOrientationOverride',
            params,
            False
        )

    def set_device_orientation_override(
            self,
            alpha: 'float',
            beta: 'float',
            gamma: 'float'
    ) -> 'IFutureResponse[None]':
        params = {
            'alpha': alpha,
            'beta': beta,
            'gamma': gamma,
        }

        return self._send_command(
            'DeviceOrientation.setDeviceOrientationOverride',
            params,
            False
        )
