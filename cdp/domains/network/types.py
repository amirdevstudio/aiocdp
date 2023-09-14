from dataclasses import (
    dataclass
)
from typing import (
    Literal
)
from cdp.domains.security.types import (
    CertificateId,
    MixedContentType,
    SecurityState
)
from cdp.domains.runtime.types import (
    StackTrace
)
from cdp.domains.network.types import (
    Headers,
    TimeSinceEpoch
)
from cdp.domains.io.types import (
    StreamHandle
)
from cdp.domains.emulation.types import (
    UserAgentMetadata
)
from cdp.domains.page.types import (
    FrameId
)

LoaderId = str

RequestId = str

InterceptionId = str

TimeSinceEpoch = float

MonotonicTime = float

ReportId = str

ResourceType = Literal[
    "Document",
    "Stylesheet",
    "Image",
    "Media",
    "Font",
    "Script",
    "TextTrack",
    "XHR",
    "Fetch",
    "Prefetch",
    "EventSource",
    "WebSocket",
    "Manifest",
    "SignedExchange",
    "Ping",
    "CSPViolationReport",
    "Preflight",
    "Other"
]

ErrorReason = Literal[
    "Failed",
    "Aborted",
    "TimedOut",
    "AccessDenied",
    "ConnectionClosed",
    "ConnectionReset",
    "ConnectionRefused",
    "ConnectionAborted",
    "ConnectionFailed",
    "NameNotResolved",
    "InternetDisconnected",
    "AddressUnreachable",
    "BlockedByClient",
    "BlockedByResponse"
]

ConnectionType = Literal[
    "none",
    "cellular2g",
    "cellular3g",
    "cellular4g",
    "bluetooth",
    "ethernet",
    "wifi",
    "wimax",
    "other"
]

CookieSameSite = Literal[
    "Strict",
    "Lax",
    "None"
]

CookiePriority = Literal[
    "Low",
    "Medium",
    "High"
]

CookieSourceScheme = Literal[
    "Unset",
    "NonSecure",
    "Secure"
]

ResourcePriority = Literal[
    "VeryLow",
    "Low",
    "Medium",
    "High",
    "VeryHigh"
]

CertificateTransparencyCompliance = Literal[
    "unknown",
    "not-compliant",
    "compliant"
]

BlockedReason = Literal[
    "other",
    "csp",
    "mixed-content",
    "origin",
    "inspector",
    "subresource-filter",
    "content-type",
    "coep-frame-resource-needs-coep-header",
    "coop-sandboxed-iframe-cannot-navigate-to-coop-page",
    "corp-not-same-origin",
    "corp-not-same-origin-after-defaulted-to-same-origin-by-coep",
    "corp-not-same-site"
]

CorsError = Literal[
    "DisallowedByMode",
    "InvalidResponse",
    "WildcardOriginNotAllowed",
    "MissingAllowOriginHeader",
    "MultipleAllowOriginValues",
    "InvalidAllowOriginValue",
    "AllowOriginMismatch",
    "InvalidAllowCredentials",
    "CorsDisabledScheme",
    "PreflightInvalidStatus",
    "PreflightDisallowedRedirect",
    "PreflightWildcardOriginNotAllowed",
    "PreflightMissingAllowOriginHeader",
    "PreflightMultipleAllowOriginValues",
    "PreflightInvalidAllowOriginValue",
    "PreflightAllowOriginMismatch",
    "PreflightInvalidAllowCredentials",
    "PreflightMissingAllowExternal",
    "PreflightInvalidAllowExternal",
    "PreflightMissingAllowPrivateNetwork",
    "PreflightInvalidAllowPrivateNetwork",
    "InvalidAllowMethodsPreflightResponse",
    "InvalidAllowHeadersPreflightResponse",
    "MethodDisallowedByPreflightResponse",
    "HeaderDisallowedByPreflightResponse",
    "RedirectContainsCredentials",
    "InsecurePrivateNetwork",
    "InvalidPrivateNetworkAccess",
    "UnexpectedPrivateNetworkAccess",
    "NoCorsRedirectModeNotFollow",
    "PreflightMissingPrivateNetworkAccessId",
    "PreflightMissingPrivateNetworkAccessName",
    "PrivateNetworkAccessPermissionUnavailable",
    "PrivateNetworkAccessPermissionDenied"
]

ServiceWorkerResponseSource = Literal[
    "cache-storage",
    "http-cache",
    "fallback-code",
    "network"
]

TrustTokenOperationType = Literal[
    "Issuance",
    "Redemption",
    "Signing"
]

AlternateProtocolUsage = Literal[
    "alternativeJobWonWithoutRace",
    "alternativeJobWonRace",
    "mainJobWonRace",
    "mappingMissing",
    "broken",
    "dnsAlpnH3JobWonWithoutRace",
    "dnsAlpnH3JobWonRace",
    "unspecifiedReason"
]

SetCookieBlockedReason = Literal[
    "SecureOnly",
    "SameSiteStrict",
    "SameSiteLax",
    "SameSiteUnspecifiedTreatedAsLax",
    "SameSiteNoneInsecure",
    "UserPreferences",
    "ThirdPartyBlockedInFirstPartySet",
    "SyntaxError",
    "SchemeNotSupported",
    "OverwriteSecure",
    "InvalidDomain",
    "InvalidPrefix",
    "UnknownError",
    "SchemefulSameSiteStrict",
    "SchemefulSameSiteLax",
    "SchemefulSameSiteUnspecifiedTreatedAsLax",
    "SamePartyFromCrossPartyContext",
    "SamePartyConflictsWithOtherAttributes",
    "NameValuePairExceedsMaxSize",
    "DisallowedCharacter"
]

CookieBlockedReason = Literal[
    "SecureOnly",
    "NotOnPath",
    "DomainMismatch",
    "SameSiteStrict",
    "SameSiteLax",
    "SameSiteUnspecifiedTreatedAsLax",
    "SameSiteNoneInsecure",
    "UserPreferences",
    "ThirdPartyBlockedInFirstPartySet",
    "UnknownError",
    "SchemefulSameSiteStrict",
    "SchemefulSameSiteLax",
    "SchemefulSameSiteUnspecifiedTreatedAsLax",
    "SamePartyFromCrossPartyContext",
    "NameValuePairExceedsMaxSize"
]

InterceptionStage = Literal[
    "Request",
    "HeadersReceived"
]

SignedExchangeErrorField = Literal[
    "signatureSig",
    "signatureIntegrity",
    "signatureCertUrl",
    "signatureCertSha256",
    "signatureValidityUrl",
    "signatureTimestamps"
]

ContentEncoding = Literal[
    "deflate",
    "gzip",
    "br",
    "zstd"
]

PrivateNetworkRequestPolicy = Literal[
    "Allow",
    "BlockFromInsecureToMorePrivate",
    "WarnFromInsecureToMorePrivate",
    "PreflightBlock",
    "PreflightWarn"
]

IPAddressSpace = Literal[
    "Local",
    "Private",
    "Public",
    "Unknown"
]

CrossOriginOpenerPolicyValue = Literal[
    "SameOrigin",
    "SameOriginAllowPopups",
    "RestrictProperties",
    "UnsafeNone",
    "SameOriginPlusCoep",
    "RestrictPropertiesPlusCoep"
]

CrossOriginEmbedderPolicyValue = Literal[
    "None",
    "Credentialless",
    "RequireCorp"
]

ContentSecurityPolicySource = Literal[
    "HTTP",
    "Meta"
]

ReportStatus = Literal[
    "Queued",
    "Pending",
    "MarkedForRemoval",
    "Success"
]


@dataclass
class ResourceTiming:
    request_time: float
    proxy_start: float
    proxy_end: float
    dns_start: float
    dns_end: float
    connect_start: float
    connect_end: float
    ssl_start: float
    ssl_end: float
    worker_start: float
    worker_ready: float
    worker_fetch_start: float
    worker_respond_with_settled: float
    send_start: float
    send_end: float
    push_start: float
    push_end: float
    receive_headers_start: float
    receive_headers_end: float


@dataclass
class PostDataEntry:
    bytes: str


@dataclass
class Request:
    url: str
    url_fragment: str
    method: str
    headers: "Headers"
    post_data: str
    has_post_data: bool
    post_data_entries: list
    mixed_content_type: "MixedContentType"
    initial_priority: "ResourcePriority"
    referrer_policy: str
    is_link_preload: bool
    trust_token_params: "TrustTokenParams"
    is_same_site: bool


@dataclass
class SignedCertificateTimestamp:
    status: str
    origin: str
    log_description: str
    log_id: str
    timestamp: float
    hash_algorithm: str
    signature_algorithm: str
    signature_data: str


@dataclass
class SecurityDetails:
    protocol: str
    key_exchange: str
    key_exchange_group: str
    cipher: str
    mac: str
    certificate_id: "CertificateId"
    subject_name: str
    san_list: list
    issuer: str
    valid_from: "TimeSinceEpoch"
    valid_to: "TimeSinceEpoch"
    signed_certificate_timestamp_list: list
    certificate_transparency_compliance: "CertificateTransparencyCompliance"
    server_signature_algorithm: int
    encrypted_client_hello: bool


@dataclass
class CorsErrorStatus:
    cors_error: "CorsError"
    failed_parameter: str


@dataclass
class TrustTokenParams:
    operation: "TrustTokenOperationType"
    refresh_policy: str
    issuers: list


@dataclass
class Response:
    url: str
    status: int
    status_text: str
    headers: "Headers"
    headers_text: str
    mime_type: str
    request_headers: "Headers"
    request_headers_text: str
    connection_reused: bool
    connection_id: float
    remote_ip_address: str
    remote_port: int
    from_disk_cache: bool
    from_service_worker: bool
    from_prefetch_cache: bool
    encoded_data_length: float
    timing: "ResourceTiming"
    service_worker_response_source: "ServiceWorkerResponseSource"
    response_time: "TimeSinceEpoch"
    cache_storage_cache_name: str
    protocol: str
    alternate_protocol_usage: "AlternateProtocolUsage"
    security_state: "SecurityState"
    security_details: "SecurityDetails"


@dataclass
class WebSocketRequest:
    headers: "Headers"


@dataclass
class WebSocketResponse:
    status: int
    status_text: str
    headers: "Headers"
    headers_text: str
    request_headers: "Headers"
    request_headers_text: str


@dataclass
class WebSocketFrame:
    opcode: float
    mask: bool
    payload_data: str


@dataclass
class CachedResource:
    url: str
    type: "ResourceType"
    response: "Response"
    body_size: float


@dataclass
class Initiator:
    type: str
    stack: "StackTrace"
    url: str
    line_number: float
    column_number: float
    request_id: "RequestId"


@dataclass
class Cookie:
    name: str
    value: str
    domain: str
    path: str
    expires: float
    size: int
    http_only: bool
    secure: bool
    session: bool
    same_site: "CookieSameSite"
    priority: "CookiePriority"
    same_party: bool
    source_scheme: "CookieSourceScheme"
    source_port: int
    partition_key: str
    partition_key_opaque: bool


@dataclass
class BlockedSetCookieWithReason:
    blocked_reasons: list
    cookie_line: str
    cookie: "Cookie"


@dataclass
class BlockedCookieWithReason:
    blocked_reasons: list
    cookie: "Cookie"


@dataclass
class CookieParam:
    name: str
    value: str
    url: str
    domain: str
    path: str
    secure: bool
    http_only: bool
    same_site: "CookieSameSite"
    expires: "TimeSinceEpoch"
    priority: "CookiePriority"
    same_party: bool
    source_scheme: "CookieSourceScheme"
    source_port: int
    partition_key: str


@dataclass
class AuthChallenge:
    source: str
    origin: str
    scheme: str
    realm: str


@dataclass
class AuthChallengeResponse:
    response: str
    username: str
    password: str


@dataclass
class RequestPattern:
    url_pattern: str
    resource_type: "ResourceType"
    interception_stage: "InterceptionStage"


@dataclass
class SignedExchangeSignature:
    label: str
    signature: str
    integrity: str
    cert_url: str
    cert_sha256: str
    validity_url: str
    date: int
    expires: int
    certificates: list


@dataclass
class SignedExchangeHeader:
    request_url: str
    response_code: int
    response_headers: "Headers"
    signatures: list
    header_integrity: str


@dataclass
class SignedExchangeError:
    message: str
    signature_index: int
    error_field: "SignedExchangeErrorField"


@dataclass
class SignedExchangeInfo:
    outer_response: "Response"
    header: "SignedExchangeHeader"
    security_details: "SecurityDetails"
    errors: list


@dataclass
class ConnectTiming:
    request_time: float


@dataclass
class ClientSecurityState:
    initiator_is_secure_context: bool
    initiator_ip_address_space: "IPAddressSpace"
    private_network_request_policy: "PrivateNetworkRequestPolicy"


@dataclass
class CrossOriginOpenerPolicyStatus:
    value: "CrossOriginOpenerPolicyValue"
    report_only_value: "CrossOriginOpenerPolicyValue"
    reporting_endpoint: str
    report_only_reporting_endpoint: str


@dataclass
class CrossOriginEmbedderPolicyStatus:
    value: "CrossOriginEmbedderPolicyValue"
    report_only_value: "CrossOriginEmbedderPolicyValue"
    reporting_endpoint: str
    report_only_reporting_endpoint: str


@dataclass
class ContentSecurityPolicyStatus:
    effective_directives: str
    is_enforced: bool
    source: "ContentSecurityPolicySource"


@dataclass
class SecurityIsolationStatus:
    coop: "CrossOriginOpenerPolicyStatus"
    coep: "CrossOriginEmbedderPolicyStatus"
    csp: list


@dataclass
class ReportingApiReport:
    id: "ReportId"
    initiator_url: str
    destination: str
    type: str
    timestamp: "TimeSinceEpoch"
    depth: int
    completed_attempts: int
    body: object
    status: "ReportStatus"


@dataclass
class ReportingApiEndpoint:
    url: str
    group_name: str


@dataclass
class LoadNetworkResourcePageResult:
    success: bool
    net_error: float
    net_error_name: str
    http_status_code: float
    stream: "StreamHandle"
    headers: "Headers"


@dataclass
class LoadNetworkResourceOptions:
    disable_cache: bool
    include_credentials: bool


@dataclass
class CanClearBrowserCacheReturnT:
    result: bool


@dataclass
class CanClearBrowserCookiesReturnT:
    result: bool


@dataclass
class CanEmulateNetworkConditionsReturnT:
    result: bool


@dataclass
class GetAllCookiesReturnT:
    cookies: list


@dataclass
class GetCertificateReturnT:
    table_names: list


@dataclass
class GetCookiesReturnT:
    cookies: list


@dataclass
class GetResponseBodyReturnT:
    body: str
    base64_encoded: bool


@dataclass
class GetRequestPostDataReturnT:
    post_data: str


@dataclass
class GetResponseBodyForInterceptionReturnT:
    body: str
    base64_encoded: bool


@dataclass
class TakeResponseBodyForInterceptionAsStreamReturnT:
    stream: "StreamHandle"


@dataclass
class SearchInResponseBodyReturnT:
    result: list


@dataclass
class SetCookieReturnT:
    success: bool


@dataclass
class GetSecurityIsolationStatusReturnT:
    status: "SecurityIsolationStatus"


@dataclass
class LoadNetworkResourceReturnT:
    resource: "LoadNetworkResourcePageResult"
