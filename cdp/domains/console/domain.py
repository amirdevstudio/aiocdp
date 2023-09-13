from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.console.types import (
    ConsoleMessage
)


@dataclass
class Console(BaseDomain):
    def clear_messages(
        self
    ):
        params = {}

        return self._send_command(
            "Console.clearMessages",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Console.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Console.enable",
            params
        )

