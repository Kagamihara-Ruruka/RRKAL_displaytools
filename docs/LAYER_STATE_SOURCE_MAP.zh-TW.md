# Layer State Source Map

Date: 2026-06-03
Scope: `RRKAL_displaytools` only
Status: source-map before implementation

This document maps the current layer-state inputs that feed renderer metadata, `LayerRenderState`-adjacent contracts, and render-plan runtime snapshots. It is intentionally docs-only: it does not move controller behavior, change renderer output, enable runtime merge, or alter metadata schemas.

## Boundary

- `RRKAL_displaytools` owns renderer-facing layer visibility, opacity, blend, selected layer state, dirty flags, preview evidence, and render metadata sidecars.
- RRKAL / `APIkeys_collection` owns dataset discovery, download, import, manifest/cache governance, and authoritative asset lifecycle.
- This source-map is not a data contract for RRKAL and does not authorize cross-repo work.
- Runtime merge remains disabled.
- Renderer output metadata schema remains `rrkal_displaytools.renderer_output_metadata.v1`.

## Current source map

| Layer-state concern | Current source | Downstream consumer | Dirty / timing effect | Extraction risk |
| --- | --- | --- | --- | --- |
| Layer visibility defaults | `HybridRenderController.__init__()` initializes `self.layer_visible` | UI layer list, metadata, `layer_render_plan_runtime_snapshot()` | Initial layer stack controls render composition | Medium because defaults mirror CLI/profile args |
| Layer visibility mutation | `set_layer_visible()` | Qt layer controls, render plan runtime snapshot, quick metadata | Sets `globe_dirty`, `overlay_dirty`, `hydrology_dirty`, or `boundary_dirty` depending on layer id | Medium because each layer family has different dirty semantics |
| Layer opacity | `set_layer_opacity()`, `layer_opacity_percent()` | Runtime overlay alpha, metadata `layer_opacity`, selected layer target | Can set overlay, hydrology, boundary, scale, contour or globe dirty flags | Medium because opacity can map to args, runtime overlays, hydrology, boundary or globe |
| Layer blend | `set_layer_blend_mode()`, `layer_blend_mode()` | Runtime blend, metadata `layer_blend_mode`, boundary aggregate blend | Sets `overlay_dirty` for runtime overlay blend layers | Low/Medium because only supported runtime overlay layers should move first |
| Selected semantic target | `set_selected_layer_semantic_target()` | `selected_layer_semantic_target`, layer pick state, metadata sidecar | Does not directly render but affects UI diagnostics and scoped picking | Medium because invalid layer state is represented, not rejected |
| Runtime state file input | `refresh_layer_runtime_state()` | Visibility, opacity, blend, selected layer, acknowledgements | Marks changed state and may skip invalid/no-op updates | Medium/High because file mtime, ack, no-op detection and error reporting are coupled |
| Dirty flag snapshot | `layer_render_plan_runtime_snapshot()` | `build_layer_render_plan_runtime_snapshot()` in `render_core.render_plan` | Captures `force`, `changed`, `globe_dirty`, `overlay_dirty`, `hydrology_dirty`, `boundary_dirty`, `boundary_hover_dirty` | Medium because flags reflect both UI and renderer refresh phases |
| Runtime snapshot builder | `render_core.render_plan.build_layer_render_plan_runtime_snapshot()` | Compiled layer render plan and metadata sidecar | Pure packet assembly after controller collects inputs | Low; already in `render_core` |
| Cache key inputs | `build_layer_render_plan_cache_key()` | Compiled plan reuse / invalidation | Includes visible layers, selected semantic target, dirty flags, boundary ids, opacity and blend | Medium because changing shape can affect reuse evidence |

## Current render-plan flow

1. UI/profile/runtime file changes controller state.
2. Controller setters update layer state and mark dirty flags.
3. `render_if_needed()` calls `refresh_layer_runtime_state()`.
4. `render_if_needed()` builds `changed` from `force`, `globe_dirty`, and `overlay_dirty`.
5. `layer_render_plan_runtime_snapshot()` collects visible layers, selected target, dirty flags and composition steps.
6. `render_core.render_plan.build_layer_render_plan_runtime_snapshot()` returns the serializable runtime snapshot packet.
7. `compile_layer_render_plan()` uses the runtime snapshot to compute cache key, invalidation reasons, batch decisions, execution phases and metadata summary.
8. `write_output_metadata()` writes full `layer_render_plan` and `layer_render_plan_summary`.

## Safe extraction boundary

The next helper should not move setter behavior. A safe first implementation candidate is a pure collector payload with this shape:

```python
{
    "visible_layers": [...],
    "selected_layer_semantic_target": ...,
    "dirty_flags": {...},
    "defer_vector_overlays": ...,
    "composition_steps": [...],
}
```

Recommended helper name:

- `render_core.layer_state.build_layer_runtime_snapshot_input()`

Allowed first use:

- `layer_render_plan_runtime_snapshot()` may call the helper after controller-local values are collected.
- The helper should only normalize and package values.
- It must not read files, mutate `self`, mark dirty flags, inspect Qt widgets, render frames, or write artifacts.

## Stop conditions before implementation

- Stop if runtime state file acknowledgement must move.
- Stop if dirty flag semantics need to change.
- Stop if selected layer invalid-state handling needs new behavior.
- Stop if cache key shape changes.
- Stop if renderer metadata schema changes.
- Stop if generated `state/` artifacts become staged.

## Validation for the future helper slice

- `py -3 -m py_compile taichi_global_bathymetry.py render_core\render_plan.py`
- `powershell -NoProfile -ExecutionPolicy Bypass -File scripts\render_quick_smoke.ps1`
- `powershell -NoProfile -ExecutionPolicy Bypass -File scripts\render_repeated_quick_smoke.ps1 -Frames 3`
- `powershell -NoProfile -ExecutionPolicy Bypass -File scripts\smoke.ps1`
- `git diff --check`
- Confirm generated `state/` artifacts remain ignored.
