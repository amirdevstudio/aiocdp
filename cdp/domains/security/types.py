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
        TimeSinceEpoch
    )

CertificateId = int

MixedContentType = Literal[
    'blockable',
    'optionally-blockable',
    'none'
]

SecurityState = Literal[
    'unknown',
    'neutral',
    'insecure',
    'secure',
    'info',
    'insecure-broken'
]

SafetyTipStatus = Literal[
    'badReputation',
    'lookalike'
]

CertificateErrorAction = Literal[
    'continue',
    'cancel'
]


@dataclass
class CertificateSecurityState:
    protocol: str
    key_exchange: str
    key_exchange_group: str
    cipher: str
    mac: str
    certificate: list
    subject_name: str
    issuer: str
    valid_from: 'TimeSinceEpoch'
    valid_to: 'TimeSinceEpoch'
    certificate_network_error: str
    certificate_has_weak_signature: bool
    certificate_has_sha1_signature: bool
    modern_ssl: bool
    obsolete_ssl_protocol: bool
    obsolete_ssl_key_exchange: bool
    obsolete_ssl_cipher: bool
    obsolete_ssl_signature: bool
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
                'protocol': self.protocol,
                'key_exchange': self.key_exchange,
                'key_exchange_group': self.key_exchange_group,
                'cipher': self.cipher,
                'mac': self.mac,
                'certificate': self.certificate,
                'subject_name': self.subject_name,
                'issuer': self.issuer,
                'valid_from': self.valid_from.to_dict(
                    casing_strategy
                ),
                'valid_to': self.valid_to.to_dict(
                    casing_strategy
                ),
                'certificate_network_error': self.certificate_network_error,
                'certificate_has_weak_signature': self.certificate_has_weak_signature,
                'certificate_has_sha1_signature': self.certificate_has_sha1_signature,
                'modern_ssl': self.modern_ssl,
                'obsolete_ssl_protocol': self.obsolete_ssl_protocol,
                'obsolete_ssl_key_exchange': self.obsolete_ssl_key_exchange,
                'obsolete_ssl_cipher': self.obsolete_ssl_cipher,
                'obsolete_ssl_signature': self.obsolete_ssl_signature,
            }
        if casing_strategy == 'snake':
            return {
                'protocol': self.protocol,
                'keyExchange': self.key_exchange,
                'keyExchangeGroup': self.key_exchange_group,
                'cipher': self.cipher,
                'mac': self.mac,
                'certificate': self.certificate,
                'subjectName': self.subject_name,
                'issuer': self.issuer,
                'validFrom': self.valid_from.to_dict(
                    casing_strategy
                ),
                'validTo': self.valid_to.to_dict(
                    casing_strategy
                ),
                'certificateNetworkError': self.certificate_network_error,
                'certificateHasWeakSignature': self.certificate_has_weak_signature,
                'certificateHasSha1Signature': self.certificate_has_sha1_signature,
                'modernSSL': self.modern_ssl,
                'obsoleteSslProtocol': self.obsolete_ssl_protocol,
                'obsoleteSslKeyExchange': self.obsolete_ssl_key_exchange,
                'obsoleteSslCipher': self.obsolete_ssl_cipher,
                'obsoleteSslSignature': self.obsolete_ssl_signature,
            }
        if casing_strategy == 'snake':
            return {
                'Protocol': self.protocol,
                'KeyExchange': self.key_exchange,
                'KeyExchangeGroup': self.key_exchange_group,
                'Cipher': self.cipher,
                'Mac': self.mac,
                'Certificate': self.certificate,
                'SubjectName': self.subject_name,
                'Issuer': self.issuer,
                'ValidFrom': self.valid_from.to_dict(
                    casing_strategy
                ),
                'ValidTo': self.valid_to.to_dict(
                    casing_strategy
                ),
                'CertificateNetworkError': self.certificate_network_error,
                'CertificateHasWeakSignature': self.certificate_has_weak_signature,
                'CertificateHasSha1Signature': self.certificate_has_sha1_signature,
                'ModernSSL': self.modern_ssl,
                'ObsoleteSslProtocol': self.obsolete_ssl_protocol,
                'ObsoleteSslKeyExchange': self.obsolete_ssl_key_exchange,
                'ObsoleteSslCipher': self.obsolete_ssl_cipher,
                'ObsoleteSslSignature': self.obsolete_ssl_signature,
            }


@dataclass
class SafetyTipInfo:
    safety_tip_status: 'SafetyTipStatus'
    safe_url: str
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
                'safety_tip_status': self.safety_tip_status.to_dict(
                    casing_strategy
                ),
                'safe_url': self.safe_url,
            }
        if casing_strategy == 'snake':
            return {
                'safetyTipStatus': self.safety_tip_status.to_dict(
                    casing_strategy
                ),
                'safeUrl': self.safe_url,
            }
        if casing_strategy == 'snake':
            return {
                'SafetyTipStatus': self.safety_tip_status.to_dict(
                    casing_strategy
                ),
                'SafeUrl': self.safe_url,
            }


@dataclass
class VisibleSecurityState:
    security_state: 'SecurityState'
    certificate_security_state: 'CertificateSecurityState'
    safety_tip_info: 'SafetyTipInfo'
    security_state_issue_ids: list
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
                'security_state': self.security_state.to_dict(
                    casing_strategy
                ),
                'certificate_security_state': self.certificate_security_state.to_dict(
                    casing_strategy
                ),
                'safety_tip_info': self.safety_tip_info.to_dict(
                    casing_strategy
                ),
                'security_state_issue_ids': self.security_state_issue_ids,
            }
        if casing_strategy == 'snake':
            return {
                'securityState': self.security_state.to_dict(
                    casing_strategy
                ),
                'certificateSecurityState': self.certificate_security_state.to_dict(
                    casing_strategy
                ),
                'safetyTipInfo': self.safety_tip_info.to_dict(
                    casing_strategy
                ),
                'securityStateIssueIds': self.security_state_issue_ids,
            }
        if casing_strategy == 'snake':
            return {
                'SecurityState': self.security_state.to_dict(
                    casing_strategy
                ),
                'CertificateSecurityState': self.certificate_security_state.to_dict(
                    casing_strategy
                ),
                'SafetyTipInfo': self.safety_tip_info.to_dict(
                    casing_strategy
                ),
                'SecurityStateIssueIds': self.security_state_issue_ids,
            }


@dataclass
class SecurityStateExplanation:
    security_state: 'SecurityState'
    title: str
    summary: str
    description: str
    mixed_content_type: 'MixedContentType'
    certificate: list
    recommendations: list
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
                'security_state': self.security_state.to_dict(
                    casing_strategy
                ),
                'title': self.title,
                'summary': self.summary,
                'description': self.description,
                'mixed_content_type': self.mixed_content_type.to_dict(
                    casing_strategy
                ),
                'certificate': self.certificate,
                'recommendations': self.recommendations,
            }
        if casing_strategy == 'snake':
            return {
                'securityState': self.security_state.to_dict(
                    casing_strategy
                ),
                'title': self.title,
                'summary': self.summary,
                'description': self.description,
                'mixedContentType': self.mixed_content_type.to_dict(
                    casing_strategy
                ),
                'certificate': self.certificate,
                'recommendations': self.recommendations,
            }
        if casing_strategy == 'snake':
            return {
                'SecurityState': self.security_state.to_dict(
                    casing_strategy
                ),
                'Title': self.title,
                'Summary': self.summary,
                'Description': self.description,
                'MixedContentType': self.mixed_content_type.to_dict(
                    casing_strategy
                ),
                'Certificate': self.certificate,
                'Recommendations': self.recommendations,
            }


@dataclass
class InsecureContentStatus:
    ran_mixed_content: bool
    displayed_mixed_content: bool
    contained_mixed_form: bool
    ran_content_with_cert_errors: bool
    displayed_content_with_cert_errors: bool
    ran_insecure_content_style: 'SecurityState'
    displayed_insecure_content_style: 'SecurityState'
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
                'ran_mixed_content': self.ran_mixed_content,
                'displayed_mixed_content': self.displayed_mixed_content,
                'contained_mixed_form': self.contained_mixed_form,
                'ran_content_with_cert_errors': self.ran_content_with_cert_errors,
                'displayed_content_with_cert_errors': self.displayed_content_with_cert_errors,
                'ran_insecure_content_style': self.ran_insecure_content_style.to_dict(
                    casing_strategy
                ),
                'displayed_insecure_content_style': self.displayed_insecure_content_style.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'snake':
            return {
                'ranMixedContent': self.ran_mixed_content,
                'displayedMixedContent': self.displayed_mixed_content,
                'containedMixedForm': self.contained_mixed_form,
                'ranContentWithCertErrors': self.ran_content_with_cert_errors,
                'displayedContentWithCertErrors': self.displayed_content_with_cert_errors,
                'ranInsecureContentStyle': self.ran_insecure_content_style.to_dict(
                    casing_strategy
                ),
                'displayedInsecureContentStyle': self.displayed_insecure_content_style.to_dict(
                    casing_strategy
                ),
            }
        if casing_strategy == 'snake':
            return {
                'RanMixedContent': self.ran_mixed_content,
                'DisplayedMixedContent': self.displayed_mixed_content,
                'ContainedMixedForm': self.contained_mixed_form,
                'RanContentWithCertErrors': self.ran_content_with_cert_errors,
                'DisplayedContentWithCertErrors': self.displayed_content_with_cert_errors,
                'RanInsecureContentStyle': self.ran_insecure_content_style.to_dict(
                    casing_strategy
                ),
                'DisplayedInsecureContentStyle': self.displayed_insecure_content_style.to_dict(
                    casing_strategy
                ),
            }
