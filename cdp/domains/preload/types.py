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
        from cdp.domains.network.types import (
        LoaderId,
        RequestId
    )
        from cdp.domains.dom.types import (
        BackendNodeId
    )

RuleSetId = str

RuleSetErrorType = Literal[
    'SourceIsNotJsonObject',
    'InvalidRulesSkipped'
]

SpeculationAction = Literal[
    'Prefetch',
    'Prerender'
]

SpeculationTargetHint = Literal[
    'Blank',
    'Self'
]

PrerenderFinalStatus = Literal[
    'Activated',
    'Destroyed',
    'LowEndDevice',
    'InvalidSchemeRedirect',
    'InvalidSchemeNavigation',
    'InProgressNavigation',
    'NavigationRequestBlockedByCsp',
    'MainFrameNavigation',
    'MojoBinderPolicy',
    'RendererProcessCrashed',
    'RendererProcessKilled',
    'Download',
    'TriggerDestroyed',
    'NavigationNotCommitted',
    'NavigationBadHttpStatus',
    'ClientCertRequested',
    'NavigationRequestNetworkError',
    'MaxNumOfRunningPrerendersExceeded',
    'CancelAllHostsForTesting',
    'DidFailLoad',
    'Stop',
    'SslCertificateError',
    'LoginAuthRequested',
    'UaChangeRequiresReload',
    'BlockedByClient',
    'AudioOutputDeviceRequested',
    'MixedContent',
    'TriggerBackgrounded',
    'MemoryLimitExceeded',
    'DataSaverEnabled',
    'HasEffectiveUrl',
    'ActivatedBeforeStarted',
    'InactivePageRestriction',
    'StartFailed',
    'TimeoutBackgrounded',
    'CrossSiteRedirectInInitialNavigation',
    'CrossSiteNavigationInInitialNavigation',
    'SameSiteCrossOriginRedirectNotOptInInInitialNavigation',
    'SameSiteCrossOriginNavigationNotOptInInInitialNavigation',
    'ActivationNavigationParameterMismatch',
    'ActivatedInBackground',
    'EmbedderHostDisallowed',
    'ActivationNavigationDestroyedBeforeSuccess',
    'TabClosedByUserGesture',
    'TabClosedWithoutUserGesture',
    'PrimaryMainFrameRendererProcessCrashed',
    'PrimaryMainFrameRendererProcessKilled',
    'ActivationFramePolicyNotCompatible',
    'PreloadingDisabled',
    'BatterySaverEnabled',
    'ActivatedDuringMainFrameNavigation',
    'PreloadingUnsupportedByWebContents',
    'CrossSiteRedirectInMainFrameNavigation',
    'CrossSiteNavigationInMainFrameNavigation',
    'SameSiteCrossOriginRedirectNotOptInInMainFrameNavigation',
    'SameSiteCrossOriginNavigationNotOptInInMainFrameNavigation',
    'MemoryPressureOnTrigger',
    'MemoryPressureAfterTriggered',
    'PrerenderingDisabledByDevTools',
    'ResourceLoadBlockedByClient',
    'SpeculationRuleRemoved',
    'ActivatedWithAuxiliaryBrowsingContexts'
]

PreloadingStatus = Literal[
    'Pending',
    'Running',
    'Ready',
    'Success',
    'Failure',
    'NotSupported'
]

PrefetchStatus = Literal[
    'PrefetchAllowed',
    'PrefetchFailedIneligibleRedirect',
    'PrefetchFailedInvalidRedirect',
    'PrefetchFailedMIMENotSupported',
    'PrefetchFailedNetError',
    'PrefetchFailedNon2XX',
    'PrefetchFailedPerPageLimitExceeded',
    'PrefetchEvicted',
    'PrefetchHeldback',
    'PrefetchIneligibleRetryAfter',
    'PrefetchIsPrivacyDecoy',
    'PrefetchIsStale',
    'PrefetchNotEligibleBrowserContextOffTheRecord',
    'PrefetchNotEligibleDataSaverEnabled',
    'PrefetchNotEligibleExistingProxy',
    'PrefetchNotEligibleHostIsNonUnique',
    'PrefetchNotEligibleNonDefaultStoragePartition',
    'PrefetchNotEligibleSameSiteCrossOriginPrefetchRequiredProxy',
    'PrefetchNotEligibleSchemeIsNotHttps',
    'PrefetchNotEligibleUserHasCookies',
    'PrefetchNotEligibleUserHasServiceWorker',
    'PrefetchNotEligibleBatterySaverEnabled',
    'PrefetchNotEligiblePreloadingDisabled',
    'PrefetchNotFinishedInTime',
    'PrefetchNotStarted',
    'PrefetchNotUsedCookiesChanged',
    'PrefetchProxyNotAvailable',
    'PrefetchResponseUsed',
    'PrefetchSuccessfulButNotUsed',
    'PrefetchNotUsedProbeFailed'
]


@dataclass
class RuleSet:
    id: 'RuleSetId'
    loader_id: 'LoaderId'
    source_text: str
    backend_node_id: 'BackendNodeId'
    url: str
    request_id: 'RequestId'
    error_type: 'RuleSetErrorType'
    error_message: str


@dataclass
class PreloadingAttemptKey:
    loader_id: 'LoaderId'
    action: 'SpeculationAction'
    url: str
    target_hint: 'SpeculationTargetHint'


@dataclass
class PreloadingAttemptSource:
    key: 'PreloadingAttemptKey'
    rule_set_ids: list
    node_ids: list