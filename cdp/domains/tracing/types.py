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

MemoryDumpConfig = dict

StreamFormat = Literal[
    'json',
    'proto'
]

StreamCompression = Literal[
    'none',
    'gzip'
]

MemoryDumpLevelOfDetail = Literal[
    'background',
    'light',
    'detailed'
]

TracingBackend = Literal[
    'auto',
    'chrome',
    'system'
]


@dataclass
class TraceConfig:
    record_mode: str
    trace_buffer_size_in_kb: float
    enable_sampling: bool
    enable_systrace: bool
    enable_argument_filter: bool
    included_categories: list
    excluded_categories: list
    synthetic_delays: list
    memory_dump_config: 'MemoryDumpConfig'


@dataclass
class GetCategoriesReturnT:
    categories: list


@dataclass
class RequestMemoryDumpReturnT:
    dump_guid: str
    success: bool