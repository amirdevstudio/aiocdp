from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

SubsamplingFormat = Literal[
    "yuv420",
    "yuv422",
    "yuv444"
]

ImageType = Literal[
    "jpeg",
    "webp",
    "unknown"
]


@dataclass
class GPUDevice:
    vendor_id: float
    device_id: float
    sub_sys_id: float
    revision: float
    vendor_string: str
    device_string: str
    driver_vendor: str
    driver_version: str


@dataclass
class Size:
    width: int
    height: int


@dataclass
class VideoDecodeAcceleratorCapability:
    profile: str
    max_resolution: "Size"
    min_resolution: "Size"


@dataclass
class VideoEncodeAcceleratorCapability:
    profile: str
    max_resolution: "Size"
    max_framerate_numerator: int
    max_framerate_denominator: int


@dataclass
class ImageDecodeAcceleratorCapability:
    image_type: "ImageType"
    max_dimensions: "Size"
    min_dimensions: "Size"
    subsamplings: list


@dataclass
class GPUInfo:
    devices: list
    aux_attributes: object
    feature_status: object
    driver_bug_workarounds: list
    video_decoding: list
    video_encoding: list
    image_decoding: list


@dataclass
class ProcessInfo:
    type: str
    id: int
    cpu_time: float


@dataclass
class GetInfoReturnT:
    gpu: "GPUInfo"
    model_name: str
    model_version: str
    command_line: str


@dataclass
class GetFeatureStateReturnT:
    feature_enabled: bool


@dataclass
class GetProcessInfoReturnT:
    process_info: list
