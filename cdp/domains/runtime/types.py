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
if TYPE_CHECKING:

ScriptId = str

RemoteObjectId = str

UnserializableValue = str

ExecutionContextId = int

Timestamp = float

TimeDelta = float

UniqueDebuggerId = str


@dataclass
class RemoteObject:
    type: str
    subtype: str
    class_name: str
    value: Any
    unserializable_value: 'UnserializableValue'
    description: str
    object_id: 'RemoteObjectId'
    preview: 'ObjectPreview'
    custom_preview: 'CustomPreview'
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
                'subtype': self.subtype,
                'class_name': self.class_name,
                'value': self.value,
                'unserializable_value': self.unserializable_value.to_dict(
                    casing_strategy
                ),
                'description': self.description,
                'object_id': self.object_id.to_dict(
                    casing_strategy
                ),
                'preview': self.preview.to_dict(
                    casing_strategy
                ),
                'custom_preview': self.custom_preview.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'camel':
            return {
                'type': self.type_,
                'subtype': self.subtype,
                'className': self.class_name,
                'value': self.value,
                'unserializableValue': self.unserializable_value.to_dict(
                    casing_strategy
                ),
                'description': self.description,
                'objectId': self.object_id.to_dict(
                    casing_strategy
                ),
                'preview': self.preview.to_dict(
                    casing_strategy
                ),
                'customPreview': self.custom_preview.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'pascal':
            return {
                'Type': self.type_,
                'Subtype': self.subtype,
                'ClassName': self.class_name,
                'Value': self.value,
                'UnserializableValue': self.unserializable_value.to_dict(
                    casing_strategy
                ),
                'Description': self.description,
                'ObjectId': self.object_id.to_dict(
                    casing_strategy
                ),
                'Preview': self.preview.to_dict(
                    casing_strategy
                ),
                'CustomPreview': self.custom_preview.to_dict(
                    casing_strategy
                ),
            }


@dataclass
class CustomPreview:
    header: str
    body_getter_id: 'RemoteObjectId'
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
                'header': self.header,
                'body_getter_id': self.body_getter_id.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'camel':
            return {
                'header': self.header,
                'bodyGetterId': self.body_getter_id.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'pascal':
            return {
                'Header': self.header,
                'BodyGetterId': self.body_getter_id.to_dict(
                    casing_strategy
                ),
            }


@dataclass
class ObjectPreview:
    type: str
    subtype: str
    description: str
    overflow: bool
    properties: list
    entries: list
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
                'subtype': self.subtype,
                'description': self.description,
                'overflow': self.overflow,
                'properties': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.properties
                ],
                'entries': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.entries
                ],
            }
        if casing_strategy == 'camel':
            return {
                'type': self.type_,
                'subtype': self.subtype,
                'description': self.description,
                'overflow': self.overflow,
                'properties': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.properties
                ],
                'entries': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.entries
                ],
            }
        if casing_strategy == 'pascal':
            return {
                'Type': self.type_,
                'Subtype': self.subtype,
                'Description': self.description,
                'Overflow': self.overflow,
                'Properties': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.properties
                ],
                'Entries': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.entries
                ],
            }


@dataclass
class PropertyPreview:
    name: str
    type: str
    value: str
    value_preview: 'ObjectPreview'
    subtype: str
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
                'type': self.type_,
                'value': self.value,
                'value_preview': self.value_preview.to_dict(
                    casing_strategy
                ),
                'subtype': self.subtype,
            }
        if casing_strategy == 'camel':
            return {
                'name': self.name,
                'type': self.type_,
                'value': self.value,
                'valuePreview': self.value_preview.to_dict(
                    casing_strategy
                ),
                'subtype': self.subtype,
            }
        if casing_strategy == 'pascal':
            return {
                'Name': self.name,
                'Type': self.type_,
                'Value': self.value,
                'ValuePreview': self.value_preview.to_dict(
                    casing_strategy
                ),
                'Subtype': self.subtype,
            }


@dataclass
class EntryPreview:
    key: 'ObjectPreview'
    value: 'ObjectPreview'
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
                'value': self.value.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'camel':
            return {
                'key': self.key.to_dict(
                    casing_strategy
                ),
                'value': self.value.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'pascal':
            return {
                'Key': self.key.to_dict(
                    casing_strategy
                ),
                'Value': self.value.to_dict(
                    casing_strategy
                ),
            }


@dataclass
class PropertyDescriptor:
    name: str
    value: 'RemoteObject'
    writable: bool
    get: 'RemoteObject'
    set: 'RemoteObject'
    configurable: bool
    enumerable: bool
    was_thrown: bool
    is_own: bool
    symbol: 'RemoteObject'
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
                'value': self.value.to_dict(
                    casing_strategy
                ),
                'writable': self.writable,
                'get': self.get.to_dict(
                    casing_strategy
                ),
                'set': self.set_.to_dict(
                    casing_strategy
                ),
                'configurable': self.configurable,
                'enumerable': self.enumerable,
                'was_thrown': self.was_thrown,
                'is_own': self.is_own,
                'symbol': self.symbol.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'camel':
            return {
                'name': self.name,
                'value': self.value.to_dict(
                    casing_strategy
                ),
                'writable': self.writable,
                'get': self.get.to_dict(
                    casing_strategy
                ),
                'set': self.set_.to_dict(
                    casing_strategy
                ),
                'configurable': self.configurable,
                'enumerable': self.enumerable,
                'wasThrown': self.was_thrown,
                'isOwn': self.is_own,
                'symbol': self.symbol.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'pascal':
            return {
                'Name': self.name,
                'Value': self.value.to_dict(
                    casing_strategy
                ),
                'Writable': self.writable,
                'Get': self.get.to_dict(
                    casing_strategy
                ),
                'Set': self.set_.to_dict(
                    casing_strategy
                ),
                'Configurable': self.configurable,
                'Enumerable': self.enumerable,
                'WasThrown': self.was_thrown,
                'IsOwn': self.is_own,
                'Symbol': self.symbol.to_dict(
                    casing_strategy
                ),
            }


@dataclass
class InternalPropertyDescriptor:
    name: str
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
                'name': self.name,
                'value': self.value.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'camel':
            return {
                'name': self.name,
                'value': self.value.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'pascal':
            return {
                'Name': self.name,
                'Value': self.value.to_dict(
                    casing_strategy
                ),
            }


@dataclass
class PrivatePropertyDescriptor:
    name: str
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
                'name': self.name,
                'value': self.value.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'camel':
            return {
                'name': self.name,
                'value': self.value.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'pascal':
            return {
                'Name': self.name,
                'Value': self.value.to_dict(
                    casing_strategy
                ),
            }


@dataclass
class CallArgument:
    value: Any
    unserializable_value: 'UnserializableValue'
    object_id: 'RemoteObjectId'
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
                'value': self.value,
                'unserializable_value': self.unserializable_value.to_dict(
                    casing_strategy
                ),
                'object_id': self.object_id.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'camel':
            return {
                'value': self.value,
                'unserializableValue': self.unserializable_value.to_dict(
                    casing_strategy
                ),
                'objectId': self.object_id.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'pascal':
            return {
                'Value': self.value,
                'UnserializableValue': self.unserializable_value.to_dict(
                    casing_strategy
                ),
                'ObjectId': self.object_id.to_dict(
                    casing_strategy
                ),
            }


@dataclass
class ExecutionContextDescription:
    id: 'ExecutionContextId'
    origin: str
    name: str
    aux_data: object
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
                'id': self.id_.to_dict(
                    casing_strategy
                ),
                'origin': self.origin,
                'name': self.name,
                'aux_data': self.aux_data,
            }
        if casing_strategy == 'camel':
            return {
                'id': self.id_.to_dict(
                    casing_strategy
                ),
                'origin': self.origin,
                'name': self.name,
                'auxData': self.aux_data,
            }
        if casing_strategy == 'pascal':
            return {
                'Id': self.id_.to_dict(
                    casing_strategy
                ),
                'Origin': self.origin,
                'Name': self.name,
                'AuxData': self.aux_data,
            }


@dataclass
class ExceptionDetails:
    exception_id: int
    text: str
    line_number: int
    column_number: int
    script_id: 'ScriptId'
    url: str
    stack_trace: 'StackTrace'
    exception: 'RemoteObject'
    execution_context_id: 'ExecutionContextId'
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
                'exception_id': self.exception_id,
                'text': self.text,
                'line_number': self.line_number,
                'column_number': self.column_number,
                'script_id': self.script_id.to_dict(
                    casing_strategy
                ),
                'url': self.url,
                'stack_trace': self.stack_trace.to_dict(
                    casing_strategy
                ),
                'exception': self.exception.to_dict(
                    casing_strategy
                ),
                'execution_context_id': self.execution_context_id.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'camel':
            return {
                'exceptionId': self.exception_id,
                'text': self.text,
                'lineNumber': self.line_number,
                'columnNumber': self.column_number,
                'scriptId': self.script_id.to_dict(
                    casing_strategy
                ),
                'url': self.url,
                'stackTrace': self.stack_trace.to_dict(
                    casing_strategy
                ),
                'exception': self.exception.to_dict(
                    casing_strategy
                ),
                'executionContextId': self.execution_context_id.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'pascal':
            return {
                'ExceptionId': self.exception_id,
                'Text': self.text,
                'LineNumber': self.line_number,
                'ColumnNumber': self.column_number,
                'ScriptId': self.script_id.to_dict(
                    casing_strategy
                ),
                'Url': self.url,
                'StackTrace': self.stack_trace.to_dict(
                    casing_strategy
                ),
                'Exception': self.exception.to_dict(
                    casing_strategy
                ),
                'ExecutionContextId': self.execution_context_id.to_dict(
                    casing_strategy
                ),
            }


@dataclass
class CallFrame:
    function_name: str
    script_id: 'ScriptId'
    url: str
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
                'function_name': self.function_name,
                'script_id': self.script_id.to_dict(
                    casing_strategy
                ),
                'url': self.url,
                'line_number': self.line_number,
                'column_number': self.column_number,
            }
        if casing_strategy == 'camel':
            return {
                'functionName': self.function_name,
                'scriptId': self.script_id.to_dict(
                    casing_strategy
                ),
                'url': self.url,
                'lineNumber': self.line_number,
                'columnNumber': self.column_number,
            }
        if casing_strategy == 'pascal':
            return {
                'FunctionName': self.function_name,
                'ScriptId': self.script_id.to_dict(
                    casing_strategy
                ),
                'Url': self.url,
                'LineNumber': self.line_number,
                'ColumnNumber': self.column_number,
            }


@dataclass
class StackTrace:
    description: str
    call_frames: list
    parent: 'StackTrace'
    parent_id: 'StackTraceId'
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
                'description': self.description,
                'call_frames': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.call_frames
                ],
                'parent': self.parent.to_dict(
                    casing_strategy
                ),
                'parent_id': self.parent_id.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'camel':
            return {
                'description': self.description,
                'callFrames': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.call_frames
                ],
                'parent': self.parent.to_dict(
                    casing_strategy
                ),
                'parentId': self.parent_id.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'pascal':
            return {
                'Description': self.description,
                'CallFrames': [_.to_dict(
                    casing_strategy
                )
                    for _ in self.call_frames
                ],
                'Parent': self.parent.to_dict(
                    casing_strategy
                ),
                'ParentId': self.parent_id.to_dict(
                    casing_strategy
                ),
            }


@dataclass
class StackTraceId:
    id: str
    debugger_id: 'UniqueDebuggerId'
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
                'id': self.id_,
                'debugger_id': self.debugger_id.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'camel':
            return {
                'id': self.id_,
                'debuggerId': self.debugger_id.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'pascal':
            return {
                'Id': self.id_,
                'DebuggerId': self.debugger_id.to_dict(
                    casing_strategy
                ),
            }


@dataclass
class AwaitPromiseReturnT:
    result: 'RemoteObject'
    exception_details: 'ExceptionDetails'


@dataclass
class CallFunctionOnReturnT:
    result: 'RemoteObject'
    exception_details: 'ExceptionDetails'


@dataclass
class CompileScriptReturnT:
    script_id: 'ScriptId'
    exception_details: 'ExceptionDetails'


@dataclass
class EvaluateReturnT:
    result: 'RemoteObject'
    exception_details: 'ExceptionDetails'


@dataclass
class GetIsolateIdReturnT:
    id: str


@dataclass
class GetHeapUsageReturnT:
    used_size: float
    total_size: float


@dataclass
class GetPropertiesReturnT:
    result: list
    internal_properties: list
    private_properties: list
    exception_details: 'ExceptionDetails'


@dataclass
class GlobalLexicalScopeNamesReturnT:
    names: list


@dataclass
class QueryObjectsReturnT:
    objects: 'RemoteObject'


@dataclass
class RunScriptReturnT:
    result: 'RemoteObject'
    exception_details: 'ExceptionDetails'
