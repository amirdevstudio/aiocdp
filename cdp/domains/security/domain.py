from cdp.domains.base import (
    BaseDomain
)
from dataclasses import (
    dataclass
)
from cdp.domains.security.types import (
    CertificateErrorAction
)
from cdp.utils import (
    is_defined,
    UNDEFINED
)


@dataclass
class Security(BaseDomain):
    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Security.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Security.enable",
            params
        )

    def set_ignore_certificate_errors(
        self,
        ignore: bool
    ):
        params = {
            "ignore": ignore,
        }

        return self._send_command(
            "Security.setIgnoreCertificateErrors",
            params
        )

    def handle_certificate_error(
        self,
        event_id: int,
        action: CertificateErrorAction
    ):
        params = {
            "eventId": event_id,
            "action": action,
        }

        return self._send_command(
            "Security.handleCertificateError",
            params
        )

    def set_override_certificate_errors(
        self,
        override: bool
    ):
        params = {
            "override": override,
        }

        return self._send_command(
            "Security.setOverrideCertificateErrors",
            params
        )

