# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from dataclasses import (
    dataclass,
    field
)
from typing import (
    TYPE_CHECKING
)
from cdp.domains.accessibility.domain import (
    Accessibility
)
from cdp.domains.animation.domain import (
    Animation
)
from cdp.domains.audits.domain import (
    Audits
)
from cdp.domains.autofill.domain import (
    Autofill
)
from cdp.domains.background_service.domain import (
    BackgroundService
)
from cdp.domains.browser.domain import (
    Browser
)
from cdp.domains.css.domain import (
    CSS
)
from cdp.domains.cache_storage.domain import (
    CacheStorage
)
from cdp.domains.cast.domain import (
    Cast
)
from cdp.domains.dom.domain import (
    DOM
)
from cdp.domains.dom_debugger.domain import (
    DOMDebugger
)
from cdp.domains.event_breakpoints.domain import (
    EventBreakpoints
)
from cdp.domains.dom_snapshot.domain import (
    DOMSnapshot
)
from cdp.domains.dom_storage.domain import (
    DOMStorage
)
from cdp.domains.database.domain import (
    Database
)
from cdp.domains.device_orientation.domain import (
    DeviceOrientation
)
from cdp.domains.emulation.domain import (
    Emulation
)
from cdp.domains.headless_experimental.domain import (
    HeadlessExperimental
)
from cdp.domains.io.domain import (
    IO
)
from cdp.domains.indexed_db.domain import (
    IndexedDB
)
from cdp.domains.input.domain import (
    Input
)
from cdp.domains.inspector.domain import (
    Inspector
)
from cdp.domains.layer_tree.domain import (
    LayerTree
)
from cdp.domains.log.domain import (
    Log
)
from cdp.domains.memory.domain import (
    Memory
)
from cdp.domains.network.domain import (
    Network
)
from cdp.domains.overlay.domain import (
    Overlay
)
from cdp.domains.page.domain import (
    Page
)
from cdp.domains.performance.domain import (
    Performance
)
from cdp.domains.performance_timeline.domain import (
    PerformanceTimeline
)
from cdp.domains.security.domain import (
    Security
)
from cdp.domains.service_worker.domain import (
    ServiceWorker
)
from cdp.domains.storage.domain import (
    Storage
)
from cdp.domains.system_info.domain import (
    SystemInfo
)
from cdp.domains.target.domain import (
    Target
)
from cdp.domains.tethering.domain import (
    Tethering
)
from cdp.domains.tracing.domain import (
    Tracing
)
from cdp.domains.fetch.domain import (
    Fetch
)
from cdp.domains.web_audio.domain import (
    WebAudio
)
from cdp.domains.web_authn.domain import (
    WebAuthn
)
from cdp.domains.media.domain import (
    Media
)
from cdp.domains.device_access.domain import (
    DeviceAccess
)
from cdp.domains.preload.domain import (
    Preload
)
from cdp.domains.fed_cm.domain import (
    FedCm
)
from cdp.domains.console.domain import (
    Console
)
from cdp.domains.debugger.domain import (
    Debugger
)
from cdp.domains.heap_profiler.domain import (
    HeapProfiler
)
from cdp.domains.profiler.domain import (
    Profiler
)
from cdp.domains.runtime.domain import (
    Runtime
)
from cdp.domains.schema.domain import (
    Schema
)
if TYPE_CHECKING:
    from cdp.target.target import (
        Target
    )


@dataclass
class Domains:
    accessibility: Accessibility = field(init=False)
    animation: Animation = field(init=False)
    audits: Audits = field(init=False)
    autofill: Autofill = field(init=False)
    background_service: BackgroundService = field(init=False)
    browser: Browser = field(init=False)
    css: CSS = field(init=False)
    cache_storage: CacheStorage = field(init=False)
    cast: Cast = field(init=False)
    dom: DOM = field(init=False)
    dom_debugger: DOMDebugger = field(init=False)
    event_breakpoints: EventBreakpoints = field(init=False)
    dom_snapshot: DOMSnapshot = field(init=False)
    dom_storage: DOMStorage = field(init=False)
    database: Database = field(init=False)
    device_orientation: DeviceOrientation = field(init=False)
    emulation: Emulation = field(init=False)
    headless_experimental: HeadlessExperimental = field(init=False)
    io: IO = field(init=False)
    indexed_db: IndexedDB = field(init=False)
    input: Input = field(init=False)
    inspector: Inspector = field(init=False)
    layer_tree: LayerTree = field(init=False)
    log: Log = field(init=False)
    memory: Memory = field(init=False)
    network: Network = field(init=False)
    overlay: Overlay = field(init=False)
    page: Page = field(init=False)
    performance: Performance = field(init=False)
    performance_timeline: PerformanceTimeline = field(init=False)
    security: Security = field(init=False)
    service_worker: ServiceWorker = field(init=False)
    storage: Storage = field(init=False)
    system_info: SystemInfo = field(init=False)
    target: Target = field(init=False)
    tethering: Tethering = field(init=False)
    tracing: Tracing = field(init=False)
    fetch: Fetch = field(init=False)
    web_audio: WebAudio = field(init=False)
    web_authn: WebAuthn = field(init=False)
    media: Media = field(init=False)
    device_access: DeviceAccess = field(init=False)
    preload: Preload = field(init=False)
    fed_cm: FedCm = field(init=False)
    console: Console = field(init=False)
    debugger: Debugger = field(init=False)
    heap_profiler: HeapProfiler = field(init=False)
    profiler: Profiler = field(init=False)
    runtime: Runtime = field(init=False)
    schema: Schema = field(init=False)
    target: 'Target'

    def __post_init__(
        self
    ):
        self.accessibility = Accessibility(self.target)
        self.animation = Animation(self.target)
        self.audits = Audits(self.target)
        self.autofill = Autofill(self.target)
        self.background_service = BackgroundService(self.target)
        self.browser = Browser(self.target)
        self.css = CSS(self.target)
        self.cache_storage = CacheStorage(self.target)
        self.cast = Cast(self.target)
        self.dom = DOM(self.target)
        self.dom_debugger = DOMDebugger(self.target)
        self.event_breakpoints = EventBreakpoints(self.target)
        self.dom_snapshot = DOMSnapshot(self.target)
        self.dom_storage = DOMStorage(self.target)
        self.database = Database(self.target)
        self.device_orientation = DeviceOrientation(self.target)
        self.emulation = Emulation(self.target)
        self.headless_experimental = HeadlessExperimental(self.target)
        self.io = IO(self.target)
        self.indexed_db = IndexedDB(self.target)
        self.input = Input(self.target)
        self.inspector = Inspector(self.target)
        self.layer_tree = LayerTree(self.target)
        self.log = Log(self.target)
        self.memory = Memory(self.target)
        self.network = Network(self.target)
        self.overlay = Overlay(self.target)
        self.page = Page(self.target)
        self.performance = Performance(self.target)
        self.performance_timeline = PerformanceTimeline(self.target)
        self.security = Security(self.target)
        self.service_worker = ServiceWorker(self.target)
        self.storage = Storage(self.target)
        self.system_info = SystemInfo(self.target)
        self.target = Target(self.target)
        self.tethering = Tethering(self.target)
        self.tracing = Tracing(self.target)
        self.fetch = Fetch(self.target)
        self.web_audio = WebAudio(self.target)
        self.web_authn = WebAuthn(self.target)
        self.media = Media(self.target)
        self.device_access = DeviceAccess(self.target)
        self.preload = Preload(self.target)
        self.fed_cm = FedCm(self.target)
        self.console = Console(self.target)
        self.debugger = Debugger(self.target)
        self.heap_profiler = HeapProfiler(self.target)
        self.profiler = Profiler(self.target)
        self.runtime = Runtime(self.target)
        self.schema = Schema(self.target)