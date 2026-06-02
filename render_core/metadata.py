from __future__ import annotations

import datetime
from typing import Any


def build_renderer_output_metadata_payload(
    *,
    output_file: str,
    frame_index: int,
    width: int,
    height: int,
    style_profile: str,
    topography_source: object,
    data_mode: object,
    ui_backend: object,
    basemap_lod: str,
    render_ms: float,
    visible_layers: list[str],
    layer_visible: dict[str, bool],
    layer_opacity: dict[str, int],
    layer_blend_mode: dict[str, str],
    selected_layer_semantic_target: object,
    last_layer_pick_result: dict[str, object],
    boundary_highlight: dict[str, object],
    layer_render_plan: dict[str, object],
    layer_render_plan_summary: dict[str, object],
    closed_loop_status: dict[str, object],
    rrkal_data_manifest_ref: str,
) -> dict[str, Any]:
    return {
        "schema": "rrkal_displaytools.renderer_output_metadata.v1",
        "created_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "output_file": output_file,
        "renderer": "taichi_global_bathymetry",
        "frame_index": int(frame_index),
        "width": int(width),
        "height": int(height),
        "style_profile": style_profile,
        "topography_source": topography_source,
        "data_mode": data_mode,
        "ui_backend": ui_backend,
        "basemap_lod": basemap_lod,
        "render_ms": float(render_ms),
        "visible_layers": visible_layers,
        "layer_visible": layer_visible,
        "layer_opacity": layer_opacity,
        "layer_blend_mode": layer_blend_mode,
        "selected_layer_semantic_target": selected_layer_semantic_target,
        "last_layer_pick_result": last_layer_pick_result,
        "boundary_highlight": boundary_highlight,
        "layer_render_plan": layer_render_plan,
        "layer_render_plan_summary": layer_render_plan_summary,
        "closed_loop_status": closed_loop_status,
        "rrkal_data_manifest_ref": rrkal_data_manifest_ref,
        "rrkal_data_manifest_ref_boundary": (
            "Reference-only; displaytools records the RRKAL manifest reference but does not discover, "
            "download, validate, import, or govern it."
        ),
        "rrkal_boundary": {
            "displaytools_owns": ["renderer output artifact", "visual layer state", "render metadata sidecar"],
            "rrkal_owns": ["dataset discovery", "download/import/install registry", "manifest/cache governance"],
        },
    }
