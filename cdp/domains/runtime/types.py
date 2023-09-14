from dataclasses import (
    dataclass
)

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
    unserializable_value: "UnserializableValue"
    description: str
    object_id: "RemoteObjectId"
    preview: "ObjectPreview"
    custom_preview: "CustomPreview"


@dataclass
class CustomPreview:
    header: str
    body_getter_id: "RemoteObjectId"


@dataclass
class ObjectPreview:
    type: str
    subtype: str
    description: str
    overflow: bool
    properties: list
    entries: list


@dataclass
class PropertyPreview:
    name: str
    type: str
    value: str
    value_preview: "ObjectPreview"
    subtype: str


@dataclass
class EntryPreview:
    key: "ObjectPreview"
    value: "ObjectPreview"


@dataclass
class PropertyDescriptor:
    name: str
    value: "RemoteObject"
    writable: bool
    get: "RemoteObject"
    set: "RemoteObject"
    configurable: bool
    enumerable: bool
    was_thrown: bool
    is_own: bool
    symbol: "RemoteObject"


@dataclass
class InternalPropertyDescriptor:
    name: str
    value: "RemoteObject"


@dataclass
class PrivatePropertyDescriptor:
    name: str
    value: "RemoteObject"


@dataclass
class CallArgument:
    value: Any
    unserializable_value: "UnserializableValue"
    object_id: "RemoteObjectId"


@dataclass
class ExecutionContextDescription:
    id: "ExecutionContextId"
    origin: str
    name: str
    aux_data: object


@dataclass
class ExceptionDetails:
    exception_id: int
    text: str
    line_number: int
    column_number: int
    script_id: "ScriptId"
    url: str
    stack_trace: "StackTrace"
    exception: "RemoteObject"
    execution_context_id: "ExecutionContextId"


@dataclass
class CallFrame:
    function_name: str
    script_id: "ScriptId"
    url: str
    line_number: int
    column_number: int


@dataclass
class StackTrace:
    description: str
    call_frames: list
    parent: "StackTrace"
    parent_id: "StackTraceId"


@dataclass
class StackTraceId:
    id: str
    debugger_id: "UniqueDebuggerId"


@dataclass
class AwaitPromiseReturnT:
    result: "RemoteObject"
    exception_details: "ExceptionDetails"


@dataclass
class CallFunctionOnReturnT:
    result: "RemoteObject"
    exception_details: "ExceptionDetails"


@dataclass
class CompileScriptReturnT:
    script_id: "ScriptId"
    exception_details: "ExceptionDetails"


@dataclass
class EvaluateReturnT:
    result: "RemoteObject"
    exception_details: "ExceptionDetails"


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
    exception_details: "ExceptionDetails"


@dataclass
class GlobalLexicalScopeNamesReturnT:
    names: list


@dataclass
class QueryObjectsReturnT:
    objects: "RemoteObject"


@dataclass
class RunScriptReturnT:
    result: "RemoteObject"
    exception_details: "ExceptionDetails"
