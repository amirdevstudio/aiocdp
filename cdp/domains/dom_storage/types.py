# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from dataclasses import (
    dataclass
)
from typing import (
    TYPE_CHECKING
)
from typing import (
    Any
)

SerializedStorageKey = str

Item = list[str]


@dataclass
class StorageId:
    security_origin: str
    storage_key: 'SerializedStorageKey'
    is_local_storage: bool
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
                'security_origin': self.security_origin,
                'storage_key': self.storage_key.to_dict(
                    casing_strategy
                ),
                'is_local_storage': self.is_local_storage,
            }
        if casing_strategy == 'snake':
            return {
                'securityOrigin': self.security_origin,
                'storageKey': self.storage_key.to_dict(
                    casing_strategy
                ),
                'isLocalStorage': self.is_local_storage,
            }
        if casing_strategy == 'snake':
            return {
                'SecurityOrigin': self.security_origin,
                'StorageKey': self.storage_key.to_dict(
                    casing_strategy
                ),
                'IsLocalStorage': self.is_local_storage,
            }


@dataclass
class GetDOMStorageItemsReturnT:
    entries: list
