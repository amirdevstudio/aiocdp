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


@dataclass
class ConsoleMessage:
    source: str
    level: str
    text: str
    url: str
    line: int
    column: int
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
                'url': self.url,
                'line': self.line,
                'column': self.column,
            }
        if casing_strategy == 'snake':
            return {
                'source': self.source,
                'level': self.level,
                'text': self.text,
                'url': self.url,
                'line': self.line,
                'column': self.column,
            }
        if casing_strategy == 'snake':
            return {
                'Source': self.source,
                'Level': self.level,
                'Text': self.text,
                'Url': self.url,
                'Line': self.line,
                'Column': self.column,
            }
