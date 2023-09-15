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
if TYPE_CHECKING:
    from cdp.domains.runtime.types import (
        RemoteObject
    )
    from cdp.domains.storage.types import (
        StorageBucket
    )


@dataclass
class DatabaseWithObjectStores:
    name: str
    version: float
    object_stores: list
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
                'version': self.version,
                'object_stores': _.to_dict(
                    casing_strategy
                )_object_stores,
            }
        if casing_strategy == 'snake':
            return {
                'name': self.name,
                'version': self.version,
                'objectStores': _.to_dict(
                    casing_strategy
                )_object_stores,
            }
        if casing_strategy == 'snake':
            return {
                'Name': self.name,
                'Version': self.version,
                'ObjectStores': _.to_dict(
                    casing_strategy
                )_object_stores,
            }


@dataclass
class ObjectStore:
    name: str
    key_path: 'KeyPath'
    auto_increment: bool
    indexes: list
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
                'key_path': self.key_path.to_dict(
                    casing_strategy
                ),
                'auto_increment': self.auto_increment,
                'indexes': _.to_dict(
                    casing_strategy
                )_indexes,
            }
        if casing_strategy == 'snake':
            return {
                'name': self.name,
                'keyPath': self.key_path.to_dict(
                    casing_strategy
                ),
                'autoIncrement': self.auto_increment,
                'indexes': _.to_dict(
                    casing_strategy
                )_indexes,
            }
        if casing_strategy == 'snake':
            return {
                'Name': self.name,
                'KeyPath': self.key_path.to_dict(
                    casing_strategy
                ),
                'AutoIncrement': self.auto_increment,
                'Indexes': _.to_dict(
                    casing_strategy
                )_indexes,
            }


@dataclass
class ObjectStoreIndex:
    name: str
    key_path: 'KeyPath'
    unique: bool
    multi_entry: bool
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
                'key_path': self.key_path.to_dict(
                    casing_strategy
                ),
                'unique': self.unique,
                'multi_entry': self.multi_entry,
            }
        if casing_strategy == 'snake':
            return {
                'name': self.name,
                'keyPath': self.key_path.to_dict(
                    casing_strategy
                ),
                'unique': self.unique,
                'multiEntry': self.multi_entry,
            }
        if casing_strategy == 'snake':
            return {
                'Name': self.name,
                'KeyPath': self.key_path.to_dict(
                    casing_strategy
                ),
                'Unique': self.unique,
                'MultiEntry': self.multi_entry,
            }


@dataclass
class Key:
    type: str
    number: float
    string: str
    date: float
    array: list
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
                'type': self.type_,
                'number': self.number,
                'string': self.string,
                'date': self.date,
                'array': _.to_dict(
                    casing_strategy
                )_array,
            }
        if casing_strategy == 'snake':
            return {
                'type': self.type_,
                'number': self.number,
                'string': self.string,
                'date': self.date,
                'array': _.to_dict(
                    casing_strategy
                )_array,
            }
        if casing_strategy == 'snake':
            return {
                'Type': self.type_,
                'Number': self.number,
                'String': self.string,
                'Date': self.date,
                'Array': _.to_dict(
                    casing_strategy
                )_array,
            }


@dataclass
class KeyRange:
    lower: 'Key'
    upper: 'Key'
    lower_open: bool
    upper_open: bool
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
                'lower': self.lower.to_dict(
                    casing_strategy
                ),
                'upper': self.upper.to_dict(
                    casing_strategy
                ),
                'lower_open': self.lower_open,
                'upper_open': self.upper_open,
            }
        if casing_strategy == 'snake':
            return {
                'lower': self.lower.to_dict(
                    casing_strategy
                ),
                'upper': self.upper.to_dict(
                    casing_strategy
                ),
                'lowerOpen': self.lower_open,
                'upperOpen': self.upper_open,
            }
        if casing_strategy == 'snake':
            return {
                'Lower': self.lower.to_dict(
                    casing_strategy
                ),
                'Upper': self.upper.to_dict(
                    casing_strategy
                ),
                'LowerOpen': self.lower_open,
                'UpperOpen': self.upper_open,
            }


@dataclass
class DataEntry:
    key: 'RemoteObject'
    primary_key: 'RemoteObject'
    value: 'RemoteObject'
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
                'key': self.key.to_dict(
                    casing_strategy
                ),
                'primary_key': self.primary_key.to_dict(
                    casing_strategy
                ),
                'value': self.value.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'snake':
            return {
                'key': self.key.to_dict(
                    casing_strategy
                ),
                'primaryKey': self.primary_key.to_dict(
                    casing_strategy
                ),
                'value': self.value.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'snake':
            return {
                'Key': self.key.to_dict(
                    casing_strategy
                ),
                'PrimaryKey': self.primary_key.to_dict(
                    casing_strategy
                ),
                'Value': self.value.to_dict(
                    casing_strategy
                ),
            }


@dataclass
class KeyPath:
    type: str
    string: str
    array: list
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
                'type': self.type_,
                'string': self.string,
                'array': self.array,
            }
        if casing_strategy == 'snake':
            return {
                'type': self.type_,
                'string': self.string,
                'array': self.array,
            }
        if casing_strategy == 'snake':
            return {
                'Type': self.type_,
                'String': self.string,
                'Array': self.array,
            }


@dataclass
class RequestDataReturnT:
    object_store_data_entries: list
    has_more: bool


@dataclass
class GetMetadataReturnT:
    entries_count: float
    key_generator_value: float


@dataclass
class RequestDatabaseReturnT:
    database_with_object_stores: 'DatabaseWithObjectStores'


@dataclass
class RequestDatabaseNamesReturnT:
    database_names: list
