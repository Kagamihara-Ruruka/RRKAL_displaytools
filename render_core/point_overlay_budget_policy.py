from __future__ import annotations


class PointOverlayBudgetPolicy:
    def decision(
        self,
        layer: str,
        point_count: int,
        width: int,
        height: int,
        render_ms: float | None,
        lod: str,
        target_fps: float,
        interaction_active: bool,
    ) -> dict:
        target_ms = 1000.0 / max(1.0, float(target_fps))
        current_ms = float(render_ms or 0.0)
        count = max(0, int(point_count))
        megapixels = max(1.0, (int(width) * int(height)) / 1_000_000.0)
        pressure = current_ms / max(target_ms, 1e-6) if current_ms > 0.0 else 0.0
        over_budget = current_ms > target_ms * 1.08 if current_ms > 0.0 else False
        dense = count >= 75_000
        very_dense = count >= 250_000
        sample_ratio_cap = 1.0
        reason = "full-quality"
        if interaction_active and over_budget:
            if very_dense:
                sample_ratio_cap = 0.10
            elif dense:
                sample_ratio_cap = 0.18
            else:
                sample_ratio_cap = 0.35
            reason = "drag-over-budget"
        elif interaction_active and megapixels >= 3.0:
            sample_ratio_cap = 0.40 if dense else 0.65
            reason = "drag-large-canvas"
        elif over_budget and very_dense:
            sample_ratio_cap = 0.22
            reason = "steady-over-budget-very-dense"
        elif over_budget and dense:
            sample_ratio_cap = 0.35
            reason = "steady-over-budget-dense"
        elif lod == "global" and megapixels >= 4.0 and dense:
            sample_ratio_cap = 0.55
            reason = "global-large-canvas"
        return {
            "layer": str(layer),
            "point_count": int(count),
            "target_ms": float(target_ms),
            "current_ms": float(current_ms),
            "pressure": float(pressure),
            "megapixels": float(megapixels),
            "interaction_active": bool(interaction_active),
            "over_budget": bool(over_budget),
            "dense": bool(dense),
            "very_dense": bool(very_dense),
            "sample_ratio_cap": float(max(0.01, min(sample_ratio_cap, 1.0))),
            "reason": reason,
            "lod": str(lod),
        }

    def text(
        self,
        decisions: dict,
    ) -> str:
        lines = [
            "Point overlay budget policy",
            "",
            "Rule: AIS/ADS-B stay screen-space correct while interaction lowers sample ratio under pressure.",
        ]
        for layer, decision in decisions.items():
            lines.extend(
                [
                    "",
                    f"[{layer}]",
                    f"- points: {int(decision.get('point_count', 0)):,}",
                    f"- reason: {decision.get('reason', 'unknown')}",
                    f"- pressure: {float(decision.get('pressure', 0.0)):.2f}x",
                    f"- sample ratio cap: {float(decision.get('sample_ratio_cap', 1.0)):.2f}",
                    f"- interaction active: {bool(decision.get('interaction_active', False))}",
                ]
            )
        return "\n".join(lines)
