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


@dataclass
class Metric:
    name: str
    value: float


@dataclass
class GetMetricsReturnT:
    metrics: list