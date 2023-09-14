from dataclasses import (
    dataclass
)
from cdp.domains.page.types import (
    FrameId
)
from cdp.domains.browser.types import (
    BrowserContextID
)

TargetID = str

SessionID = str


@dataclass
class TargetInfo:
    target_id: "TargetID"
    type: str
    title: str
    url: str
    attached: bool
    opener_id: "TargetID"
    can_access_opener: bool
    opener_frame_id: "FrameId"
    browser_context_id: "BrowserContextID"
    subtype: str


@dataclass
class FilterEntry:
    exclude: bool
    type: str


@dataclass
class RemoteLocation:
    host: str
    port: int


@dataclass
class AttachToTargetReturnT:
    session_id: "SessionID"


@dataclass
class AttachToBrowserTargetReturnT:
    session_id: "SessionID"


@dataclass
class CloseTargetReturnT:
    success: bool


@dataclass
class CreateBrowserContextReturnT:
    browser_context_id: "BrowserContextID"


@dataclass
class GetBrowserContextsReturnT:
    browser_context_ids: list


@dataclass
class CreateTargetReturnT:
    target_id: "TargetID"


@dataclass
class GetTargetInfoReturnT:
    target_info: "TargetInfo"


@dataclass
class GetTargetsReturnT:
    target_infos: list
