"""Datashader sampling policy scalar decisions.

This module is intentionally independent from renderer, Qt, Taichi, parser,
normalizer, provider, metadata, and artifact writer modules.
"""

from __future__ import annotations


class DatashaderSamplingPolicy:
    LOD_BUDGETS = {
        "global": 250_000,
        "continental": 500_000,
        "regional": 900_000,
        "local": 1_250_000,
    }

    def decision(self, records: int, lod: str, user_scale: float = 1.0, realtime: bool = True) -> dict:
        records = max(0, int(records))
        budget = int(self.LOD_BUDGETS.get(lod, self.LOD_BUDGETS["global"]))
        user_scale = max(0.05, float(user_scale))
        effective_budget = max(1, int(budget * user_scale))
        if not realtime:
            effective_budget = max(effective_budget, records)
        fraction = 1.0 if records <= effective_budget else effective_budget / max(1, records)
        return {
            "lod": lod,
            "records": records,
            "base_budget": budget,
            "effective_budget": effective_budget,
            "sample_fraction": max(0.001, min(1.0, fraction)),
            "strategy": "aggregate-all" if fraction >= 1.0 else "pre-sample-then-aggregate",
            "realtime": realtime,
        }

    def text(self, ais_records: int, aircraft_records: int, lod: str, ais_scale: float, aircraft_scale: float, mode: str) -> str:
        realtime = mode == "realtime"
        ais = self.decision(ais_records, lod, ais_scale, realtime)
        aircraft = self.decision(aircraft_records, lod, aircraft_scale, realtime)
        lines = [
            "Datashader sampling policy",
            "",
            f"- mode: {mode}",
            f"- lod: {lod}",
            "",
            "AIS:",
            f"- records: {ais['records']}",
            f"- effective budget: {ais['effective_budget']}",
            f"- sample fraction: {ais['sample_fraction']:.4f}",
            f"- strategy: {ais['strategy']}",
            "",
            "ADS-B:",
            f"- records: {aircraft['records']}",
            f"- effective budget: {aircraft['effective_budget']}",
            f"- sample fraction: {aircraft['sample_fraction']:.4f}",
            f"- strategy: {aircraft['strategy']}",
            "",
            "Rule: Datashader should aggregate all points when affordable; sampling is a realtime FPS valve.",
        ]
        return "\n".join(lines)
