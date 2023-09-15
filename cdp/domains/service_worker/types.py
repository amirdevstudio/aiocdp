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
    from cdp.domains.target.types import (
        TargetID
    )

RegistrationID = str

ServiceWorkerVersionRunningStatus = Literal[
    'stopped',
    'starting',
    'running',
    'stopping'
]

ServiceWorkerVersionStatus = Literal[
    'new',
    'installing',
    'installed',
    'activating',
    'activated',
    'redundant'
]


@dataclass
class ServiceWorkerRegistration:
    registration_id: 'RegistrationID'
    scope_url: str
    is_deleted: bool
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
                'registration_id': self.registration_id.to_dict(
                    casing_strategy
                ),
                'scope_url': self.scope_url,
                'is_deleted': self.is_deleted,
            }
        if casing_strategy == 'snake':
            return {
                'registrationId': self.registration_id.to_dict(
                    casing_strategy
                ),
                'scopeURL': self.scope_url,
                'isDeleted': self.is_deleted,
            }
        if casing_strategy == 'snake':
            return {
                'RegistrationId': self.registration_id.to_dict(
                    casing_strategy
                ),
                'ScopeURL': self.scope_url,
                'IsDeleted': self.is_deleted,
            }


@dataclass
class ServiceWorkerVersion:
    version_id: str
    registration_id: 'RegistrationID'
    script_url: str
    running_status: 'ServiceWorkerVersionRunningStatus'
    status: 'ServiceWorkerVersionStatus'
    script_last_modified: float
    script_response_time: float
    controlled_clients: list
    target_id: 'TargetID'
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
                'version_id': self.version_id,
                'registration_id': self.registration_id.to_dict(
                    casing_strategy
                ),
                'script_url': self.script_url,
                'running_status': self.running_status.to_dict(
                    casing_strategy
                ),
                'status': self.status.to_dict(
                    casing_strategy
                ),
                'script_last_modified': self.script_last_modified,
                'script_response_time': self.script_response_time,
                'controlled_clients': _.to_dict(
                    casing_strategy
                )_controlled_clients,
                'target_id': self.target_id.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'snake':
            return {
                'versionId': self.version_id,
                'registrationId': self.registration_id.to_dict(
                    casing_strategy
                ),
                'scriptURL': self.script_url,
                'runningStatus': self.running_status.to_dict(
                    casing_strategy
                ),
                'status': self.status.to_dict(
                    casing_strategy
                ),
                'scriptLastModified': self.script_last_modified,
                'scriptResponseTime': self.script_response_time,
                'controlledClients': _.to_dict(
                    casing_strategy
                )_controlled_clients,
                'targetId': self.target_id.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'snake':
            return {
                'VersionId': self.version_id,
                'RegistrationId': self.registration_id.to_dict(
                    casing_strategy
                ),
                'ScriptURL': self.script_url,
                'RunningStatus': self.running_status.to_dict(
                    casing_strategy
                ),
                'Status': self.status.to_dict(
                    casing_strategy
                ),
                'ScriptLastModified': self.script_last_modified,
                'ScriptResponseTime': self.script_response_time,
                'ControlledClients': _.to_dict(
                    casing_strategy
                )_controlled_clients,
                'TargetId': self.target_id.to_dict(
                    casing_strategy
                ),
            }


@dataclass
class ServiceWorkerErrorMessage:
    error_message: str
    registration_id: 'RegistrationID'
    version_id: str
    source_url: str
    line_number: int
    column_number: int
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
                'error_message': self.error_message,
                'registration_id': self.registration_id.to_dict(
                    casing_strategy
                ),
                'version_id': self.version_id,
                'source_url': self.source_url,
                'line_number': self.line_number,
                'column_number': self.column_number,
            }
        if casing_strategy == 'snake':
            return {
                'errorMessage': self.error_message,
                'registrationId': self.registration_id.to_dict(
                    casing_strategy
                ),
                'versionId': self.version_id,
                'sourceURL': self.source_url,
                'lineNumber': self.line_number,
                'columnNumber': self.column_number,
            }
        if casing_strategy == 'snake':
            return {
                'ErrorMessage': self.error_message,
                'RegistrationId': self.registration_id.to_dict(
                    casing_strategy
                ),
                'VersionId': self.version_id,
                'SourceURL': self.source_url,
                'LineNumber': self.line_number,
                'ColumnNumber': self.column_number,
            }
