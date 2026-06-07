"""Layer render budget policy scalar decisions.

This module is intentionally independent from renderer, Qt, Taichi, parser,
normalizer, provider, metadata, and artifact writer modules.
"""

from __future__ import annotations


LAYER_RENDER_COSTS = {
    "globe": 10,
    "clouds": 9,
    "ice": 5,
    "forest": 5,
    "contours": 7,
    "lakes": 6,
    "rivers": 7,
    "borders": 6,
    "territorial_sea": 7,
    "eez": 7,
    "high_seas": 7,
    "ais": 8,
    "aircraft": 8,
    "vehicle_icons": 4,
    "scale": 1,
}


class LayerRenderBudgetPolicy:
    VECTOR_LAYER_IDS = {"lakes", "rivers", "borders", "territorial_sea", "eez", "high_seas"}

    def decision(
        self,
        width: int,
        height: int,
        render_ms: float | None,
        lod: str,
        target_fps: float,
        interaction_active: bool,
        layer_visible: dict | None,
    ) -> dict:
        target_ms = 1000.0 / max(1.0, float(target_fps))
        current_ms = float(render_ms or 0.0)
        visible = layer_visible or {}
        visible_cost = sum(
            LAYER_RENDER_COSTS.get(layer_id, 1)
            for layer_id, enabled in visible.items()
            if enabled
        )
        vector_cost = sum(
            LAYER_RENDER_COSTS.get(layer_id, 1)
            for layer_id in self.VECTOR_LAYER_IDS
            if visible.get(layer_id, False)
        )
        megapixels = max(1.0, (int(width) * int(height)) / 1_000_000.0)
        pressure = current_ms / max(target_ms, 1e-6) if current_ms > 0.0 else 0.0
        heavy_canvas = megapixels >= 3.0
        over_budget = current_ms > target_ms * 1.08 if current_ms > 0.0 else False
        defer_vector_overlays = bool(interaction_active and over_budget and vector_cost > 0)
        prefer_static_cache = bool(over_budget and (heavy_canvas or vector_cost >= 12))
        if defer_vector_overlays:
            vector_cache_degrees = 0.45
            vector_cache_zoom_step = 0.025
            vector_point_stride = 5
        elif interaction_active and prefer_static_cache:
            vector_cache_degrees = 0.18
            vector_cache_zoom_step = 0.014
            vector_point_stride = 4
        elif prefer_static_cache:
            vector_cache_degrees = 0.08
            vector_cache_zoom_step = 0.008
            vector_point_stride = 3 if lod in {"global", "continental"} else 2
        elif lod == "global" and heavy_canvas:
            vector_cache_degrees = 0.012
            vector_cache_zoom_step = 0.002
            vector_point_stride = 2
        else:
            vector_cache_degrees = 0.004
            vector_cache_zoom_step = 0.001
            vector_point_stride = 1
        state = "over-budget" if over_budget else "within-budget"
        if current_ms <= 0.0:
            state = "warming-up"
        return {
            "state": state,
            "target_ms": float(target_ms),
            "current_ms": float(current_ms),
            "pressure": float(pressure),
            "megapixels": float(megapixels),
            "visible_cost": int(visible_cost),
            "vector_cost": int(vector_cost),
            "heavy_canvas": bool(heavy_canvas),
            "interaction_active": bool(interaction_active),
            "defer_vector_overlays": bool(defer_vector_overlays),
            "prefer_static_cache": bool(prefer_static_cache),
            "vector_cache_degrees": float(vector_cache_degrees),
            "vector_cache_zoom_step": float(vector_cache_zoom_step),
            "vector_point_stride": int(vector_point_stride),
            "lod": str(lod),
        }

    def text(
        self,
        width: int,
        height: int,
        render_ms: float | None,
        lod: str,
        target_fps: float,
        interaction_active: bool,
        layer_visible: dict | None,
    ) -> str:
        decision = self.decision(width, height, render_ms, lod, target_fps, interaction_active, layer_visible)
        lines = [
            "Render budget policy",
            "",
            f"- state: {decision['state']}",
            f"- target: {decision['target_ms']:.2f} ms/frame",
            f"- current: {decision['current_ms']:.2f} ms/frame",
            f"- pressure: {decision['pressure']:.2f}x",
            f"- canvas: {decision['megapixels']:.2f} MP",
            f"- visible layer cost: {decision['visible_cost']}",
            f"- vector layer cost: {decision['vector_cost']}",
            f"- interaction active: {decision['interaction_active']}",
            f"- defer vector overlays while dragging: {decision['defer_vector_overlays']}",
            f"- prefer static/vector cache: {decision['prefer_static_cache']}",
            f"- vector camera quantum: {decision['vector_cache_degrees']:.3f} deg / zoom {decision['vector_cache_zoom_step']:.4f}",
            f"- vector point stride: every {decision['vector_point_stride']} point(s)",
            "",
            "Rule: while dragging and over budget, keep the last vector overlay frame and recompute it after interaction settles.",
        ]
        return "\n".join(lines)
