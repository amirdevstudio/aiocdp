from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.dom.types import (
    BackendNodeId,
    Rect
)
from cdp.domains.layer_tree.types import (
    StickyPositionConstraint,
    SnapshotId,
    LayerId
)


@dataclass
class LayerTree(BaseDomain):
    def compositing_reasons(
        self,
        layer_id: LayerId
    ):
        params = {
            "layerId": layer_id,
        }

        return self._send_command(
            "LayerTree.compositingReasons",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "LayerTree.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "LayerTree.enable",
            params
        )

    def load_snapshot(
        self,
        tiles: list
    ):
        params = {
            "tiles": tiles,
        }

        return self._send_command(
            "LayerTree.loadSnapshot",
            params
        )

    def make_snapshot(
        self,
        layer_id: LayerId
    ):
        params = {
            "layerId": layer_id,
        }

        return self._send_command(
            "LayerTree.makeSnapshot",
            params
        )

    def profile_snapshot(
        self,
        snapshot_id: SnapshotId,
        min_repeat_count: MaybeUndefined[int],
        min_duration: MaybeUndefined[float],
        clip_rect: MaybeUndefined[Rect]
    ):
        params = {
            "snapshotId": snapshot_id,
        }

        if is_defined(
            min_repeat_count
        ):
            params["minRepeatCount"] = min_repeat_count

        if is_defined(
            min_duration
        ):
            params["minDuration"] = min_duration

        if is_defined(
            clip_rect
        ):
            params["clipRect"] = clip_rect

        return self._send_command(
            "LayerTree.profileSnapshot",
            params
        )

    def release_snapshot(
        self,
        snapshot_id: SnapshotId
    ):
        params = {
            "snapshotId": snapshot_id,
        }

        return self._send_command(
            "LayerTree.releaseSnapshot",
            params
        )

    def replay_snapshot(
        self,
        snapshot_id: SnapshotId,
        from_step: MaybeUndefined[int],
        to_step: MaybeUndefined[int],
        scale: MaybeUndefined[float]
    ):
        params = {
            "snapshotId": snapshot_id,
        }

        if is_defined(
            from_step
        ):
            params["fromStep"] = from_step

        if is_defined(
            to_step
        ):
            params["toStep"] = to_step

        if is_defined(
            scale
        ):
            params["scale"] = scale

        return self._send_command(
            "LayerTree.replaySnapshot",
            params
        )

    def snapshot_command_log(
        self,
        snapshot_id: SnapshotId
    ):
        params = {
            "snapshotId": snapshot_id,
        }

        return self._send_command(
            "LayerTree.snapshotCommandLog",
            params
        )
