# Render Plan Compile Source Map

Date: 2026-06-03
Scope: `RRKAL_displaytools` only
Status: source-map before compile facade extraction

This document maps `HybridRenderController.compile_layer_render_plan()` before any further behavior movement. It is a docs-only checkpoint: it does not change renderer output, metadata schema, runtime merge state, cache behavior, or generated artifacts.

## Boundary

- `RRKAL_displaytools` owns renderer-facing layer state, render-plan compilation, preview evidence, profiler metadata, and visualization contracts.
- RRKAL / `APIkeys_collection` owns dataset discovery, download, import, manifest/cache governance, and asset lifecycle.
- This source-map is not a cross-repo contract and does not authorize RendererSkinAsset, compression, or RRKAL Core work.
- Runtime merge remains disabled.
- Renderer output metadata schema remains `rrkal_displaytools.renderer_output_metadata.v1`.

## Current compile flow

| Step | Current owner | Current helper / field | Output | Extraction risk |
| --- | --- | --- | --- | --- |
| 1. Composition steps | Controller | `layer_render_plan_composition_steps()` | list of layer composition step packets | Medium; step list still depends on controller overlay attributes |
| 2. Runtime snapshot | Controller + `render_core.layer_state` + `render_core.layer_render_plan_residual_packet_surfaces`; re-exported by `render_core.render_plan` | `layer_render_plan_runtime_snapshot()` -> `build_layer_runtime_snapshot_input()` -> `build_layer_render_plan_runtime_snapshot()` | serializable runtime snapshot with visible layers, selected target and dirty flags | Low/Medium; input helper exists, but controller still owns dirty semantics |
| 3. Compose queue | Controller + `render_core.render_plan` | `layer_render_plan_compose_queue()` and `build_layer_render_plan_compose_queue_packet_from_states()` | compose queue packet and compose runs | Medium; queue still depends on overlay-array availability |
| 4. Cache key inputs | Controller + `render_core.layer_render_plan_cache_diagnostics`; re-exported by `render_core.render_plan` | `build_layer_render_plan_cache_key()` | compiled plan cache key | Medium; controller supplies style profile, boundary layer ids, opacity and blend maps |
| 5. Cache invalidation | `render_core.layer_render_plan_cache_diagnostics`; re-exported by `render_core.render_plan` | `build_layer_render_plan_cache_invalidation_reasons()` / `build_layer_render_plan_cache_invalidation_scope()` | invalidation reason list and scope list | Low; already pure after runtime snapshot and key are supplied |
| 6. Batch decisions | `render_core.layer_render_plan_residual_packet_surfaces`; re-exported by `render_core.render_plan` | `build_layer_render_plan_batch_decisions()` | rebuild/reuse decisions for batch and layer scopes | Low/Medium; output depends on dirty flags and composition steps |
| 7. Apply path and execution | `render_core.render_plan` | `build_layer_render_plan_apply_path()`, `build_layer_render_plan_execution_summary()`, `build_layer_render_plan_execution_phases()` | serializable apply path and execution plan | Low; already pure packet construction |
| 8. Timing contracts | `render_core.render_plan` | `build_layer_render_plan_phase_timing_contract()` and phase timing runtime state | phase timing contract and runtime packet | Low; runtime packet already produced elsewhere |
| 9. Adapter payload | `render_core.render_plan` | `build_layer_render_plan_adapter_payload()` | normalized controller-to-core payload | Low; already available as a primary payload contract |
| 10. Reuse / compiled packet | `render_core.layer_render_plan_compiled_reused_packets`; re-exported by `render_core.render_plan` | `build_reused_compiled_layer_render_plan_packet_from_adapter_payload()` or `build_compiled_layer_render_plan_packet_from_adapter_payload()` | compiled layer render plan | Low/Medium; reuse branch depends on controller cached key and cached plan |

## Current controller-owned inputs

`compile_layer_render_plan()` still owns these controller reads:

- `self.layer_render_plan_composition_steps()`
- `self.layer_render_plan_runtime_snapshot(...)`
- `self.layer_render_plan_compose_queue(composition_steps)`
- `self.args.style_profile`
- `self.boundary_layer_rgba`
- `self.layer_opacity_percent(layer_id)`
- `self.layer_blend_mode(layer_id)`
- `self.layer_render_plan_phase_timing_runtime`
- `self.compiled_layer_render_plan`
- `self.compiled_layer_render_plan_cache_key`
- `self.frame_index`

These reads are acceptable for the controller adapter boundary, but they should be collected into a named input packet before moving any compile behavior.

## Existing render_core seams

Already available pure helpers:

- `build_layer_render_plan_runtime_snapshot()`
- `build_layer_render_plan_cache_key()`
- `build_layer_render_plan_cache_invalidation_reasons()`
- `build_layer_render_plan_cache_invalidation_scope()`
- `build_layer_render_plan_batch_decisions()`
- `build_layer_render_plan_apply_path()`
- `build_layer_render_plan_execution_summary()`
- `build_layer_render_plan_execution_phases()`
- `build_layer_render_plan_phase_timing_contract()`
- `build_layer_render_plan_adapter_payload()`
- `build_compiled_layer_render_plan_packet_from_adapter_payload()`
- `build_reused_compiled_layer_render_plan_packet_from_adapter_payload()`

## Recommended next helper boundary

Implemented helper name:

- `render_core.render_plan.build_layer_render_plan_compile_input()`

Current first implementation:

- Package controller-collected values into a serializable compile input payload.
- Do not compute new cache decisions in the helper yet.
- Do not read controller attributes inside render_core.
- Do not move overlay-array lookup or queue construction.
- Keep adapter payload, compiled packet schema, metadata schema and runtime merge state unchanged.

Candidate payload shape:

```python
{
    "composition_steps": [...],
    "runtime_snapshot": {...},
    "compose_queue_packet": {...},
    "style_profile": "...",
    "boundary_layer_ids": [...],
    "layer_opacity": {...},
    "layer_blend": {...},
    "phase_timing_runtime": {...},
    "cached_plan_available": True,
    "previous_cache_key": "...",
    "frame_index": 0,
}
```

## Stop conditions before implementation

- Stop if cache key output changes.
- Stop if dirty flag semantics change.
- Stop if the reuse branch changes behavior.
- Stop if overlay arrays are moved into render_core.
- Stop if renderer metadata schema changes.
- Stop if runtime merge is enabled.
- Stop if generated `state/` artifacts become staged.

## Validation for the future helper slice

- `py -3 -m py_compile taichi_global_bathymetry.py render_core\render_plan.py`
- `powershell -NoProfile -ExecutionPolicy Bypass -File scripts\render_quick_smoke.ps1`
- `powershell -NoProfile -ExecutionPolicy Bypass -File scripts\render_repeated_quick_smoke.ps1 -Frames 3`
- `powershell -NoProfile -ExecutionPolicy Bypass -File scripts\smoke.ps1`
- `git diff --check`
- Confirm generated `state/` artifacts remain ignored.
