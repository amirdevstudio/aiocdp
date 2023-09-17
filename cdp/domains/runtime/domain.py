# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from cdp.domains.base import (
    BaseDomain
)
from dataclasses import (
    dataclass
)
from cdp.utils import (
    is_defined,
    UNDEFINED
)
from typing import (
    TYPE_CHECKING
)
from cdp.domains.mapper import (
    from_dict,
    to_dict
)
from cdp.domains.runtime.types import (
    AwaitPromiseReturnT,
    CallFunctionOnReturnT,
    CompileScriptReturnT,
    EvaluateReturnT,
    ExecutionContextId,
    GetHeapUsageReturnT,
    GetIsolateIdReturnT,
    GetPropertiesReturnT,
    GlobalLexicalScopeNamesReturnT,
    QueryObjectsReturnT,
    RemoteObjectId,
    RunScriptReturnT,
    ScriptId,
    TimeDelta
)
if TYPE_CHECKING:
    from cdp.target.connection import (
        IFutureResponse
    )


@dataclass
class Runtime(BaseDomain):
    def await_promise(
            self,
            promise_object_id: 'RemoteObjectId',
            return_by_value: 'bool' = UNDEFINED,
            generate_preview: 'bool' = UNDEFINED
    ) -> 'IFutureResponse[AwaitPromiseReturnT]':
        params = {
            'promiseObjectId': promise_object_id,
        }

        if is_defined(return_by_value):
            params['returnByValue'] = return_by_value

        if is_defined(generate_preview):
            params['generatePreview'] = generate_preview

        return self._send_command(
            'Runtime.awaitPromise',
            params,
            True,
            lambda data: from_dict(
                AwaitPromiseReturnT,
                data,
                'camel'
            )
        )

    def call_function_on(
            self,
            function_declaration: 'str',
            object_id: 'RemoteObjectId' = UNDEFINED,
            arguments: 'list' = UNDEFINED,
            silent: 'bool' = UNDEFINED,
            return_by_value: 'bool' = UNDEFINED,
            generate_preview: 'bool' = UNDEFINED,
            user_gesture: 'bool' = UNDEFINED,
            await_promise: 'bool' = UNDEFINED,
            execution_context_id: 'ExecutionContextId' = UNDEFINED,
            object_group: 'str' = UNDEFINED
    ) -> 'IFutureResponse[CallFunctionOnReturnT]':
        params = {
            'functionDeclaration': function_declaration,
        }

        if is_defined(object_id):
            params['objectId'] = object_id

        if is_defined(arguments):
            params['arguments'] = [
                to_dict(item, 'camel')
                for item in arguments
            ]

        if is_defined(silent):
            params['silent'] = silent

        if is_defined(return_by_value):
            params['returnByValue'] = return_by_value

        if is_defined(generate_preview):
            params['generatePreview'] = generate_preview

        if is_defined(user_gesture):
            params['userGesture'] = user_gesture

        if is_defined(await_promise):
            params['awaitPromise'] = await_promise

        if is_defined(execution_context_id):
            params['executionContextId'] = execution_context_id

        if is_defined(object_group):
            params['objectGroup'] = object_group

        return self._send_command(
            'Runtime.callFunctionOn',
            params,
            True,
            lambda data: from_dict(
                CallFunctionOnReturnT,
                data,
                'camel'
            )
        )

    def compile_script(
            self,
            expression: 'str',
            source_url: 'str',
            persist_script: 'bool',
            execution_context_id: 'ExecutionContextId' = UNDEFINED
    ) -> 'IFutureResponse[CompileScriptReturnT]':
        params = {
            'expression': expression,
            'sourceURL': source_url,
            'persistScript': persist_script,
        }

        if is_defined(execution_context_id):
            params['executionContextId'] = execution_context_id

        return self._send_command(
            'Runtime.compileScript',
            params,
            True,
            lambda data: from_dict(
                CompileScriptReturnT,
                data,
                'camel'
            )
        )

    def disable(
            self
    ) -> 'IFutureResponse[None]':
        params = {}

        return self._send_command(
            'Runtime.disable',
            params,
            False
        )

    def discard_console_entries(
            self
    ) -> 'IFutureResponse[None]':
        params = {}

        return self._send_command(
            'Runtime.discardConsoleEntries',
            params,
            False
        )

    def enable(
            self
    ) -> 'IFutureResponse[None]':
        params = {}

        return self._send_command(
            'Runtime.enable',
            params,
            False
        )

    def evaluate(
            self,
            expression: 'str',
            object_group: 'str' = UNDEFINED,
            include_command_line_api: 'bool' = UNDEFINED,
            silent: 'bool' = UNDEFINED,
            context_id: 'ExecutionContextId' = UNDEFINED,
            return_by_value: 'bool' = UNDEFINED,
            generate_preview: 'bool' = UNDEFINED,
            user_gesture: 'bool' = UNDEFINED,
            await_promise: 'bool' = UNDEFINED,
            throw_on_side_effect: 'bool' = UNDEFINED,
            timeout: 'TimeDelta' = UNDEFINED
    ) -> 'IFutureResponse[EvaluateReturnT]':
        params = {
            'expression': expression,
        }

        if is_defined(object_group):
            params['objectGroup'] = object_group

        if is_defined(include_command_line_api):
            params['includeCommandLineAPI'] = include_command_line_api

        if is_defined(silent):
            params['silent'] = silent

        if is_defined(context_id):
            params['contextId'] = context_id

        if is_defined(return_by_value):
            params['returnByValue'] = return_by_value

        if is_defined(generate_preview):
            params['generatePreview'] = generate_preview

        if is_defined(user_gesture):
            params['userGesture'] = user_gesture

        if is_defined(await_promise):
            params['awaitPromise'] = await_promise

        if is_defined(throw_on_side_effect):
            params['throwOnSideEffect'] = throw_on_side_effect

        if is_defined(timeout):
            params['timeout'] = timeout

        return self._send_command(
            'Runtime.evaluate',
            params,
            True,
            lambda data: from_dict(
                EvaluateReturnT,
                data,
                'camel'
            )
        )

    def get_isolate_id(
            self
    ) -> 'IFutureResponse[GetIsolateIdReturnT]':
        params = {}

        return self._send_command(
            'Runtime.getIsolateId',
            params,
            True,
            lambda data: from_dict(
                GetIsolateIdReturnT,
                data,
                'camel'
            )
        )

    def get_heap_usage(
            self
    ) -> 'IFutureResponse[GetHeapUsageReturnT]':
        params = {}

        return self._send_command(
            'Runtime.getHeapUsage',
            params,
            True,
            lambda data: from_dict(
                GetHeapUsageReturnT,
                data,
                'camel'
            )
        )

    def get_properties(
            self,
            object_id: 'RemoteObjectId',
            own_properties: 'bool' = UNDEFINED,
            accessor_properties_only: 'bool' = UNDEFINED,
            generate_preview: 'bool' = UNDEFINED
    ) -> 'IFutureResponse[GetPropertiesReturnT]':
        params = {
            'objectId': object_id,
        }

        if is_defined(own_properties):
            params['ownProperties'] = own_properties

        if is_defined(accessor_properties_only):
            params['accessorPropertiesOnly'] = accessor_properties_only

        if is_defined(generate_preview):
            params['generatePreview'] = generate_preview

        return self._send_command(
            'Runtime.getProperties',
            params,
            True,
            lambda data: from_dict(
                GetPropertiesReturnT,
                data,
                'camel'
            )
        )

    def global_lexical_scope_names(
            self,
            execution_context_id: 'ExecutionContextId' = UNDEFINED
    ) -> 'IFutureResponse[GlobalLexicalScopeNamesReturnT]':
        params = {}

        if is_defined(execution_context_id):
            params['executionContextId'] = execution_context_id

        return self._send_command(
            'Runtime.globalLexicalScopeNames',
            params,
            True,
            lambda data: from_dict(
                GlobalLexicalScopeNamesReturnT,
                data,
                'camel'
            )
        )

    def query_objects(
            self,
            prototype_object_id: 'RemoteObjectId',
            object_group: 'str' = UNDEFINED
    ) -> 'IFutureResponse[QueryObjectsReturnT]':
        params = {
            'prototypeObjectId': prototype_object_id,
        }

        if is_defined(object_group):
            params['objectGroup'] = object_group

        return self._send_command(
            'Runtime.queryObjects',
            params,
            True,
            lambda data: from_dict(
                QueryObjectsReturnT,
                data,
                'camel'
            )
        )

    def release_object(
            self,
            object_id: 'RemoteObjectId'
    ) -> 'IFutureResponse[None]':
        params = {
            'objectId': object_id,
        }

        return self._send_command(
            'Runtime.releaseObject',
            params,
            False
        )

    def release_object_group(
            self,
            object_group: 'str'
    ) -> 'IFutureResponse[None]':
        params = {
            'objectGroup': object_group,
        }

        return self._send_command(
            'Runtime.releaseObjectGroup',
            params,
            False
        )

    def run_if_waiting_for_debugger(
            self
    ) -> 'IFutureResponse[None]':
        params = {}

        return self._send_command(
            'Runtime.runIfWaitingForDebugger',
            params,
            False
        )

    def run_script(
            self,
            script_id: 'ScriptId',
            execution_context_id: 'ExecutionContextId' = UNDEFINED,
            object_group: 'str' = UNDEFINED,
            silent: 'bool' = UNDEFINED,
            include_command_line_api: 'bool' = UNDEFINED,
            return_by_value: 'bool' = UNDEFINED,
            generate_preview: 'bool' = UNDEFINED,
            await_promise: 'bool' = UNDEFINED
    ) -> 'IFutureResponse[RunScriptReturnT]':
        params = {
            'scriptId': script_id,
        }

        if is_defined(execution_context_id):
            params['executionContextId'] = execution_context_id

        if is_defined(object_group):
            params['objectGroup'] = object_group

        if is_defined(silent):
            params['silent'] = silent

        if is_defined(include_command_line_api):
            params['includeCommandLineAPI'] = include_command_line_api

        if is_defined(return_by_value):
            params['returnByValue'] = return_by_value

        if is_defined(generate_preview):
            params['generatePreview'] = generate_preview

        if is_defined(await_promise):
            params['awaitPromise'] = await_promise

        return self._send_command(
            'Runtime.runScript',
            params,
            True,
            lambda data: from_dict(
                RunScriptReturnT,
                data,
                'camel'
            )
        )

    def set_async_call_stack_depth(
            self,
            max_depth: 'int'
    ) -> 'IFutureResponse[None]':
        params = {
            'maxDepth': max_depth,
        }

        return self._send_command(
            'Runtime.setAsyncCallStackDepth',
            params,
            False
        )

    def set_custom_object_formatter_enabled(
            self,
            enabled: 'bool'
    ) -> 'IFutureResponse[None]':
        params = {
            'enabled': enabled,
        }

        return self._send_command(
            'Runtime.setCustomObjectFormatterEnabled',
            params,
            False
        )

    def set_max_call_stack_size_to_capture(
            self,
            size: 'int'
    ) -> 'IFutureResponse[None]':
        params = {
            'size': size,
        }

        return self._send_command(
            'Runtime.setMaxCallStackSizeToCapture',
            params,
            False
        )

    def terminate_execution(
            self
    ) -> 'IFutureResponse[None]':
        params = {}

        return self._send_command(
            'Runtime.terminateExecution',
            params,
            False
        )

    def add_binding(
            self,
            name: 'str',
            execution_context_id: 'ExecutionContextId' = UNDEFINED
    ) -> 'IFutureResponse[None]':
        params = {
            'name': name,
        }

        if is_defined(execution_context_id):
            params['executionContextId'] = execution_context_id

        return self._send_command(
            'Runtime.addBinding',
            params,
            False
        )

    def remove_binding(
            self,
            name: 'str'
    ) -> 'IFutureResponse[None]':
        params = {
            'name': name,
        }

        return self._send_command(
            'Runtime.removeBinding',
            params,
            False
        )
