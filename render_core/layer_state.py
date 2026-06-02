from __future__ import annotations

from typing import Any


def build_layer_runtime_snapshot_input(
    *,
    frame_index: int,
    visible_layers: list[object],
    selected_layer_semantic_target: Any,
    dirty_flags: dict[str, object],
    defer_vector_overlays: Any,
    composition_steps: list[dict[str, object]],
    source: str,
) -> dict[str, object]:
    return {
        "frame_index": frame_index,
        "visible_layers": visible_layers,
        "selected_layer_semantic_target": selected_layer_semantic_target,
        "dirty_flags": dirty_flags,
        "defer_vector_overlays": defer_vector_overlays,
        "composition_steps": composition_steps,
        "source": source,
    }
