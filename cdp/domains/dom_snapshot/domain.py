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
    ShadowRootType,
    Rect,
    PseudoType
)
from cdp.domains.page.types import (
    FrameId
)
from cdp.domains.dom_snapshot.types import (
    LayoutTreeSnapshot,
    RareBooleanData,
    NodeTreeSnapshot,
    StringIndex,
    RareIntegerData,
    RareStringData,
    TextBoxSnapshot
)


@dataclass
class DOMSnapshot(BaseDomain):
    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "DOMSnapshot.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "DOMSnapshot.enable",
            params
        )

    def get_snapshot(
        self,
        computed_style_whitelist: list,
        include_event_listeners: MaybeUndefined[bool],
        include_paint_order: MaybeUndefined[bool],
        include_user_agent_shadow_tree: MaybeUndefined[bool]
    ):
        params = {
            "computedStyleWhitelist": computed_style_whitelist,
        }

        if is_defined(
            include_event_listeners
        ):
            params["includeEventListeners"] = include_event_listeners

        if is_defined(
            include_paint_order
        ):
            params["includePaintOrder"] = include_paint_order

        if is_defined(
            include_user_agent_shadow_tree
        ):
            params["includeUserAgentShadowTree"] = include_user_agent_shadow_tree

        return self._send_command(
            "DOMSnapshot.getSnapshot",
            params
        )

    def capture_snapshot(
        self,
        computed_styles: list,
        include_paint_order: MaybeUndefined[bool],
        include_dom_rects: MaybeUndefined[bool],
        include_blended_background_colors: MaybeUndefined[bool],
        include_text_color_opacities: MaybeUndefined[bool]
    ):
        params = {
            "computedStyles": computed_styles,
        }

        if is_defined(
            include_paint_order
        ):
            params["includePaintOrder"] = include_paint_order

        if is_defined(
            include_dom_rects
        ):
            params["includeDOMRects"] = include_dom_rects

        if is_defined(
            include_blended_background_colors
        ):
            params["includeBlendedBackgroundColors"] = include_blended_background_colors

        if is_defined(
            include_text_color_opacities
        ):
            params["includeTextColorOpacities"] = include_text_color_opacities

        return self._send_command(
            "DOMSnapshot.captureSnapshot",
            params
        )
