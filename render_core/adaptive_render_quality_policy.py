"""Adaptive render quality policy scalar recommendations.

This module is intentionally independent from renderer, Qt, Taichi, parser,
normalizer, provider, metadata, and artifact writer modules.
"""

from __future__ import annotations


class AdaptiveRenderQualityPolicy:
    def decision(self, width: int, height: int, render_ms: float | None, lod: str, target_fps: float = 30.0) -> dict:
        width = max(1, int(width))
        height = max(1, int(height))
        pixels = width * height
        target_ms = 1000.0 / max(1.0, float(target_fps))
        render_ms = None if render_ms is None else max(0.0, float(render_ms))
        pressure = 1.0 if render_ms is None else render_ms / target_ms
        if pressure <= 1.15:
            scale = 1.0
            overlay_budget = "full"
        elif pressure <= 2.0:
            scale = 0.85
            overlay_budget = "reduced overlays"
        elif pressure <= 4.0:
            scale = 0.70
            overlay_budget = "sample realtime overlays"
        else:
            scale = 0.55
            overlay_budget = "aggressive realtime sampling"
        if pixels >= 6_000_000 and scale > 0.85:
            scale = 0.85
            overlay_budget = "large-display guardrail"
        return {
            "width": width,
            "height": height,
            "pixels": pixels,
            "lod": lod,
            "render_ms": render_ms,
            "target_fps": float(target_fps),
            "target_ms": target_ms,
            "pressure": pressure,
            "suggested_render_scale": scale,
            "overlay_budget": overlay_budget,
        }

    def text(self, width: int, height: int, render_ms: float | None, lod: str, target_fps: float = 30.0) -> str:
        decision = self.decision(width, height, render_ms, lod, target_fps)
        render_ms_text = "unknown" if decision["render_ms"] is None else f"{decision['render_ms']:.2f} ms"
        lines = [
            "Adaptive render quality policy",
            "",
            f"- canvas: {decision['width']} x {decision['height']}",
            f"- pixels: {decision['pixels']:,}",
            f"- lod: {decision['lod']}",
            f"- last render: {render_ms_text}",
            f"- target fps: {decision['target_fps']:.1f}",
            f"- pressure: {decision['pressure']:.2f}x",
            f"- suggested render scale: {decision['suggested_render_scale']:.2f}",
            f"- overlay budget: {decision['overlay_budget']}",
            "",
            "Rule: this policy reports recommendations only; it does not silently degrade scientific output.",
        ]
        return "\n".join(lines)
