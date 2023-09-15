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
        StackTrace,
        Timestamp
    )
    from cdp.domains.network.types import (
        RequestId
    )


@dataclass
class LogEntry:
    source: str
    level: str
    text: str
    category: str
    timestamp: 'Timestamp'
    url: str
    line_number: int
    stack_trace: 'StackTrace'
    network_request_id: 'RequestId'
    worker_id: str
    args: list
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
                'source': self.source,
                'level': self.level,
                'text': self.text,
                'category': self.category,
                'timestamp': self.timestamp.to_dict(
                    casing_strategy
                ),
                'url': self.url,
                'line_number': self.line_number,
                'stack_trace': self.stack_trace.to_dict(
                    casing_strategy
                ),
                'network_request_id': self.network_request_id.to_dict(
                    casing_strategy
                ),
                'worker_id': self.worker_id,
                'args': _.to_dict(
                    casing_strategy
                )_args,
            }
        if casing_strategy == 'snake':
            return {
                'source': self.source,
                'level': self.level,
                'text': self.text,
                'category': self.category,
                'timestamp': self.timestamp.to_dict(
                    casing_strategy
                ),
                'url': self.url,
                'lineNumber': self.line_number,
                'stackTrace': self.stack_trace.to_dict(
                    casing_strategy
                ),
                'networkRequestId': self.network_request_id.to_dict(
                    casing_strategy
                ),
                'workerId': self.worker_id,
                'args': _.to_dict(
                    casing_strategy
                )_args,
            }
        if casing_strategy == 'snake':
            return {
                'Source': self.source,
                'Level': self.level,
                'Text': self.text,
                'Category': self.category,
                'Timestamp': self.timestamp.to_dict(
                    casing_strategy
                ),
                'Url': self.url,
                'LineNumber': self.line_number,
                'StackTrace': self.stack_trace.to_dict(
                    casing_strategy
                ),
                'NetworkRequestId': self.network_request_id.to_dict(
                    casing_strategy
                ),
                'WorkerId': self.worker_id,
                'Args': _.to_dict(
                    casing_strategy
                )_args,
            }


@dataclass
class ViolationSetting:
    name: str
    threshold: float
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
                'threshold': self.threshold,
            }
        if casing_strategy == 'snake':
            return {
                'name': self.name,
                'threshold': self.threshold,
            }
        if casing_strategy == 'snake':
            return {
                'Name': self.name,
                'Threshold': self.threshold,
            }
