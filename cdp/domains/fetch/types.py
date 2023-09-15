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
    Literal
)
from typing import (
    Any
)
if TYPE_CHECKING:
    from cdp.domains.network.types import (
        ErrorReason,
        ResourceType
    )
    from cdp.domains.io.types import (
        StreamHandle
    )

RequestId = str

RequestStage = Literal[
    'Request',
    'Response'
]


@dataclass
class RequestPattern:
    url_pattern: str
    resource_type: 'ResourceType'
    request_stage: 'RequestStage'
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
                'url_pattern': self.url_pattern,
                'resource_type': self.resource_type.to_dict(
                    casing_strategy
                ),
                'request_stage': self.request_stage.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'snake':
            return {
                'urlPattern': self.url_pattern,
                'resourceType': self.resource_type.to_dict(
                    casing_strategy
                ),
                'requestStage': self.request_stage.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'snake':
            return {
                'UrlPattern': self.url_pattern,
                'ResourceType': self.resource_type.to_dict(
                    casing_strategy
                ),
                'RequestStage': self.request_stage.to_dict(
                    casing_strategy
                ),
            }


@dataclass
class HeaderEntry:
    name: str
    value: str
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
                'value': self.value,
            }
        if casing_strategy == 'snake':
            return {
                'name': self.name,
                'value': self.value,
            }
        if casing_strategy == 'snake':
            return {
                'Name': self.name,
                'Value': self.value,
            }


@dataclass
class AuthChallenge:
    source: str
    origin: str
    scheme: str
    realm: str
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
                'origin': self.origin,
                'scheme': self.scheme,
                'realm': self.realm,
            }
        if casing_strategy == 'snake':
            return {
                'source': self.source,
                'origin': self.origin,
                'scheme': self.scheme,
                'realm': self.realm,
            }
        if casing_strategy == 'snake':
            return {
                'Source': self.source,
                'Origin': self.origin,
                'Scheme': self.scheme,
                'Realm': self.realm,
            }


@dataclass
class AuthChallengeResponse:
    response: str
    username: str
    password: str
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
                'response': self.response,
                'username': self.username,
                'password': self.password,
            }
        if casing_strategy == 'snake':
            return {
                'response': self.response,
                'username': self.username,
                'password': self.password,
            }
        if casing_strategy == 'snake':
            return {
                'Response': self.response,
                'Username': self.username,
                'Password': self.password,
            }


@dataclass
class GetResponseBodyReturnT:
    body: str
    base64_encoded: bool


@dataclass
class TakeResponseBodyAsStreamReturnT:
    stream: 'StreamHandle'
