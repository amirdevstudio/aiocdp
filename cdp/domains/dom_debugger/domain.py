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
from cdp.domains.dom_debugger.types import (
    DOMBreakpointType,
    GetEventListenersReturnT
)
from cdp.domains.runtime.types import (
    RemoteObjectId
)
from cdp.domains.dom.types import (
    NodeId
)
if TYPE_CHECKING:
    from cdp.target.connection import (
        IFutureResponse
    )


@dataclass
class DOMDebugger(BaseDomain):
    def get_event_listeners(
            self,
            object_id: 'RemoteObjectId',
            depth: 'int' = UNDEFINED,
            pierce: 'bool' = UNDEFINED
    ) -> 'IFutureResponse[GetEventListenersReturnT]':
        params = {
            'objectId': object_id,
        }

        if is_defined(depth):
            params['depth'] = depth

        if is_defined(pierce):
            params['pierce'] = pierce

        return self._send_command(
            'DOMDebugger.getEventListeners',
            params,
            True,
            lambda data: from_dict(
                GetEventListenersReturnT,
                data,
                'camel'
            )
        )

    def remove_dom_breakpoint(
            self,
            node_id: 'NodeId',
            type_: 'DOMBreakpointType'
    ) -> 'IFutureResponse[None]':
        params = {
            'nodeId': node_id,
            'type': type_,
        }

        return self._send_command(
            'DOMDebugger.removeDOMBreakpoint',
            params,
            False
        )

    def remove_event_listener_breakpoint(
            self,
            event_name: 'str',
            target_name: 'str' = UNDEFINED
    ) -> 'IFutureResponse[None]':
        params = {
            'eventName': event_name,
        }

        if is_defined(target_name):
            params['targetName'] = target_name

        return self._send_command(
            'DOMDebugger.removeEventListenerBreakpoint',
            params,
            False
        )

    def remove_instrumentation_breakpoint(
            self,
            event_name: 'str'
    ) -> 'IFutureResponse[None]':
        params = {
            'eventName': event_name,
        }

        return self._send_command(
            'DOMDebugger.removeInstrumentationBreakpoint',
            params,
            False
        )

    def remove_xhr_breakpoint(
            self,
            url: 'str'
    ) -> 'IFutureResponse[None]':
        params = {
            'url': url,
        }

        return self._send_command(
            'DOMDebugger.removeXHRBreakpoint',
            params,
            False
        )

    def set_break_on_csp_violation(
            self,
            violation_types: 'list'
    ) -> 'IFutureResponse[None]':
        params = {
            'violationTypes': violation_types,
        }

        return self._send_command(
            'DOMDebugger.setBreakOnCSPViolation',
            params,
            False
        )

    def set_dom_breakpoint(
            self,
            node_id: 'NodeId',
            type_: 'DOMBreakpointType'
    ) -> 'IFutureResponse[None]':
        params = {
            'nodeId': node_id,
            'type': type_,
        }

        return self._send_command(
            'DOMDebugger.setDOMBreakpoint',
            params,
            False
        )

    def set_event_listener_breakpoint(
            self,
            event_name: 'str',
            target_name: 'str' = UNDEFINED
    ) -> 'IFutureResponse[None]':
        params = {
            'eventName': event_name,
        }

        if is_defined(target_name):
            params['targetName'] = target_name

        return self._send_command(
            'DOMDebugger.setEventListenerBreakpoint',
            params,
            False
        )

    def set_instrumentation_breakpoint(
            self,
            event_name: 'str'
    ) -> 'IFutureResponse[None]':
        params = {
            'eventName': event_name,
        }

        return self._send_command(
            'DOMDebugger.setInstrumentationBreakpoint',
            params,
            False
        )

    def set_xhr_breakpoint(
            self,
            url: 'str'
    ) -> 'IFutureResponse[None]':
        params = {
            'url': url,
        }

        return self._send_command(
            'DOMDebugger.setXHRBreakpoint',
            params,
            False
        )
