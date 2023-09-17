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
from cdp.domains.system_info.types import (
    GetFeatureStateReturnT,
    GetInfoReturnT,
    GetProcessInfoReturnT
)
if TYPE_CHECKING:
    from cdp.target.connection import (
        IResponse
    )


@dataclass
class SystemInfo(BaseDomain):
    def get_info(
            self
    ) -> IResponse['GetInfoReturnT']:
        params = {}

        return self._send_command(
            'SystemInfo.getInfo',
            params,
            True,
            lambda data: from_dict(
                GetInfoReturnT,
                data,
                'camel'
            )
        )

    def get_feature_state(
            self,
            feature_state: str
    ) -> IResponse['GetFeatureStateReturnT']:
        params = {
            'featureState': feature_state,
        }

        return self._send_command(
            'SystemInfo.getFeatureState',
            params,
            True,
            lambda data: from_dict(
                GetFeatureStateReturnT,
                data,
                'camel'
            )
        )

    def get_process_info(
            self
    ) -> IResponse['GetProcessInfoReturnT']:
        params = {}

        return self._send_command(
            'SystemInfo.getProcessInfo',
            params,
            True,
            lambda data: from_dict(
                GetProcessInfoReturnT,
                data,
                'camel'
            )
        )
