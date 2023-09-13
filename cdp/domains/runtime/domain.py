from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.runtime.types import (
    Timestamp,
    StackTrace,
    RemoteObject,
    TimeDelta,
    StackTraceId,
    ExceptionDetails,
    ExecutionContextDescription,
    UniqueDebuggerId,
    ScriptId,
    ExecutionContextId,
    CustomPreview,
    RemoteObjectId,
    ObjectPreview,
    UnserializableValue
)


@dataclass
class Runtime(BaseDomain):
    def await_promise(
        self,
        promise_object_id: RemoteObjectId,
        return_by_value: MaybeUndefined[bool],
        generate_preview: MaybeUndefined[bool]
    ):
        params = {
            "promiseObjectId": promise_object_id,
        }

        if is_defined(
            return_by_value
        ):
            params["returnByValue"] = return_by_value

        if is_defined(
            generate_preview
        ):
            params["generatePreview"] = generate_preview

        return self._send_command(
            "Runtime.awaitPromise",
            params
        )

    def call_function_on(
        self,
        function_declaration: str,
        object_id: MaybeUndefined[RemoteObjectId],
        arguments: MaybeUndefined[list],
        silent: MaybeUndefined[bool],
        return_by_value: MaybeUndefined[bool],
        generate_preview: MaybeUndefined[bool],
        user_gesture: MaybeUndefined[bool],
        await_promise: MaybeUndefined[bool],
        execution_context_id: MaybeUndefined[ExecutionContextId],
        object_group: MaybeUndefined[str]
    ):
        params = {
            "functionDeclaration": function_declaration,
        }

        if is_defined(
            object_id
        ):
            params["objectId"] = object_id

        if is_defined(
            arguments
        ):
            params["arguments"] = arguments

        if is_defined(
            silent
        ):
            params["silent"] = silent

        if is_defined(
            return_by_value
        ):
            params["returnByValue"] = return_by_value

        if is_defined(
            generate_preview
        ):
            params["generatePreview"] = generate_preview

        if is_defined(
            user_gesture
        ):
            params["userGesture"] = user_gesture

        if is_defined(
            await_promise
        ):
            params["awaitPromise"] = await_promise

        if is_defined(
            execution_context_id
        ):
            params["executionContextId"] = execution_context_id

        if is_defined(
            object_group
        ):
            params["objectGroup"] = object_group

        return self._send_command(
            "Runtime.callFunctionOn",
            params
        )

    def compile_script(
        self,
        expression: str,
        source_url: str,
        persist_script: bool,
        execution_context_id: MaybeUndefined[ExecutionContextId]
    ):
        params = {
            "expression": expression,
            "sourceURL": source_url,
            "persistScript": persist_script,
        }

        if is_defined(
            execution_context_id
        ):
            params["executionContextId"] = execution_context_id

        return self._send_command(
            "Runtime.compileScript",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Runtime.disable",
            params
        )

    def discard_console_entries(
        self
    ):
        params = {}

        return self._send_command(
            "Runtime.discardConsoleEntries",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Runtime.enable",
            params
        )

    def evaluate(
        self,
        expression: str,
        object_group: MaybeUndefined[str],
        include_command_line_api: MaybeUndefined[bool],
        silent: MaybeUndefined[bool],
        context_id: MaybeUndefined[ExecutionContextId],
        return_by_value: MaybeUndefined[bool],
        generate_preview: MaybeUndefined[bool],
        user_gesture: MaybeUndefined[bool],
        await_promise: MaybeUndefined[bool],
        throw_on_side_effect: MaybeUndefined[bool],
        timeout: MaybeUndefined[TimeDelta]
    ):
        params = {
            "expression": expression,
        }

        if is_defined(
            object_group
        ):
            params["objectGroup"] = object_group

        if is_defined(
            include_command_line_api
        ):
            params["includeCommandLineAPI"] = include_command_line_api

        if is_defined(
            silent
        ):
            params["silent"] = silent

        if is_defined(
            context_id
        ):
            params["contextId"] = context_id

        if is_defined(
            return_by_value
        ):
            params["returnByValue"] = return_by_value

        if is_defined(
            generate_preview
        ):
            params["generatePreview"] = generate_preview

        if is_defined(
            user_gesture
        ):
            params["userGesture"] = user_gesture

        if is_defined(
            await_promise
        ):
            params["awaitPromise"] = await_promise

        if is_defined(
            throw_on_side_effect
        ):
            params["throwOnSideEffect"] = throw_on_side_effect

        if is_defined(
            timeout
        ):
            params["timeout"] = timeout

        return self._send_command(
            "Runtime.evaluate",
            params
        )

    def get_isolate_id(
        self
    ):
        params = {}

        return self._send_command(
            "Runtime.getIsolateId",
            params
        )

    def get_heap_usage(
        self
    ):
        params = {}

        return self._send_command(
            "Runtime.getHeapUsage",
            params
        )

    def get_properties(
        self,
        object_id: RemoteObjectId,
        own_properties: MaybeUndefined[bool],
        accessor_properties_only: MaybeUndefined[bool],
        generate_preview: MaybeUndefined[bool]
    ):
        params = {
            "objectId": object_id,
        }

        if is_defined(
            own_properties
        ):
            params["ownProperties"] = own_properties

        if is_defined(
            accessor_properties_only
        ):
            params["accessorPropertiesOnly"] = accessor_properties_only

        if is_defined(
            generate_preview
        ):
            params["generatePreview"] = generate_preview

        return self._send_command(
            "Runtime.getProperties",
            params
        )

    def global_lexical_scope_names(
        self,
        execution_context_id: MaybeUndefined[ExecutionContextId]
    ):
        params = {}

        if is_defined(
            execution_context_id
        ):
            params["executionContextId"] = execution_context_id

        return self._send_command(
            "Runtime.globalLexicalScopeNames",
            params
        )

    def query_objects(
        self,
        prototype_object_id: RemoteObjectId,
        object_group: MaybeUndefined[str]
    ):
        params = {
            "prototypeObjectId": prototype_object_id,
        }

        if is_defined(
            object_group
        ):
            params["objectGroup"] = object_group

        return self._send_command(
            "Runtime.queryObjects",
            params
        )

    def release_object(
        self,
        object_id: RemoteObjectId
    ):
        params = {
            "objectId": object_id,
        }

        return self._send_command(
            "Runtime.releaseObject",
            params
        )

    def release_object_group(
        self,
        object_group: str
    ):
        params = {
            "objectGroup": object_group,
        }

        return self._send_command(
            "Runtime.releaseObjectGroup",
            params
        )

    def run_if_waiting_for_debugger(
        self
    ):
        params = {}

        return self._send_command(
            "Runtime.runIfWaitingForDebugger",
            params
        )

    def run_script(
        self,
        script_id: ScriptId,
        execution_context_id: MaybeUndefined[ExecutionContextId],
        object_group: MaybeUndefined[str],
        silent: MaybeUndefined[bool],
        include_command_line_api: MaybeUndefined[bool],
        return_by_value: MaybeUndefined[bool],
        generate_preview: MaybeUndefined[bool],
        await_promise: MaybeUndefined[bool]
    ):
        params = {
            "scriptId": script_id,
        }

        if is_defined(
            execution_context_id
        ):
            params["executionContextId"] = execution_context_id

        if is_defined(
            object_group
        ):
            params["objectGroup"] = object_group

        if is_defined(
            silent
        ):
            params["silent"] = silent

        if is_defined(
            include_command_line_api
        ):
            params["includeCommandLineAPI"] = include_command_line_api

        if is_defined(
            return_by_value
        ):
            params["returnByValue"] = return_by_value

        if is_defined(
            generate_preview
        ):
            params["generatePreview"] = generate_preview

        if is_defined(
            await_promise
        ):
            params["awaitPromise"] = await_promise

        return self._send_command(
            "Runtime.runScript",
            params
        )

    def set_async_call_stack_depth(
        self,
        max_depth: int
    ):
        params = {
            "maxDepth": max_depth,
        }

        return self._send_command(
            "Runtime.setAsyncCallStackDepth",
            params
        )

    def set_custom_object_formatter_enabled(
        self,
        enabled: bool
    ):
        params = {
            "enabled": enabled,
        }

        return self._send_command(
            "Runtime.setCustomObjectFormatterEnabled",
            params
        )

    def set_max_call_stack_size_to_capture(
        self,
        size: int
    ):
        params = {
            "size": size,
        }

        return self._send_command(
            "Runtime.setMaxCallStackSizeToCapture",
            params
        )

    def terminate_execution(
        self
    ):
        params = {}

        return self._send_command(
            "Runtime.terminateExecution",
            params
        )

    def add_binding(
        self,
        name: str,
        execution_context_id: MaybeUndefined[ExecutionContextId]
    ):
        params = {
            "name": name,
        }

        if is_defined(
            execution_context_id
        ):
            params["executionContextId"] = execution_context_id

        return self._send_command(
            "Runtime.addBinding",
            params
        )

    def remove_binding(
        self,
        name: str
    ):
        params = {
            "name": name,
        }

        return self._send_command(
            "Runtime.removeBinding",
            params
        )
