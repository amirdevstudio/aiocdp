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

SerializedStorageKey = str

Item = list[str]


@dataclass
class StorageId:
    security_origin: str
    storage_key: 'SerializedStorageKey'
    is_local_storage: bool


@dataclass
class GetDOMStorageItemsReturnT:
    entries: list