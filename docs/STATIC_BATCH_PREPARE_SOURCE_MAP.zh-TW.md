# Static Batch Prepare Source Map

Date: 2026-06-03
Scope: `RRKAL_displaytools` only
Status: source-map before prepare-batch cache work

This document maps the current `prepare_batches` phase before any further performance behavior change. It is a docs-only checkpoint: it does not change renderer output, metadata schema, cache behavior, runtime merge state, or generated artifacts.

## Boundary

- `RRKAL_displaytools` owns renderer-facing preview evidence, render-plan timing, layer state, vector overlay cache evidence, and visualization contracts.
- RRKAL / `APIkeys_collection` owns dataset discovery, download, import, manifest/cache governance, and asset lifecycle.
- This source-map is not a cross-repo contract and does not authorize RendererSkinAsset, compression, RRKAL Core, or low-latency preview work.
- Runtime merge remains disabled.
- Renderer output metadata schema remains `rrkal_displaytools.renderer_output_metadata.v1`.

## Current prepare_batches flow

| Sub-phase | Current code location | Current state / cache | Dirty trigger | Risk before moving |
| --- | --- | --- | --- | --- |
| Runtime state refresh | `render_if_needed()` calls `refresh_layer_runtime_state()` | Layer runtime state file, selected layer, opacity, blend and visibility | Runtime state mtime or timeline playback | Medium; file ack and no-op detection are coupled to controller |
| Globe render | `render_if_needed()` globe branch | `globe_rgba`, `globe_mask`, Taichi renderer state | `force` or `globe_dirty` | High; Taichi state and mask output must not move without image parity |
| AIS projection/render | `project_ais_to_screen()`, `_sample_projected_frame()`, `overlay_renderer.render()` | `current_projected`, `current_sampled_projected`, `overlay_rgba` | `overlay_dirty`, data refresh, camera/projection changes | Medium/High; datashader/sample policy and render budget are coupled |
| Aircraft projection/render | `project_aircraft_to_screen()`, aircraft renderer | `current_aircraft_projected`, `aircraft_overlay_rgba` | aircraft layer visibility, data refresh, camera/projection changes | Medium; layer availability and sampling differ from AIS |
| Pin projection/render | `project_pins_to_screen()`, `render_pin_overlay()` | `current_pin_projections`, `pin_overlay_rgba` | pin layer visibility, pin records, camera/projection changes | Medium; picking and occlusion are tied to projections |
| Vehicle icon overlay | `render_vehicle_icon_overlay()` | `vehicle_icon_overlay_rgba` | vehicle icon layer visibility, projected traffic state | Medium; depends on both AIS and aircraft sampled state |
| Vector overlay defer gate | render budget decision in `render_if_needed()` | `vector_overlay_cache_deferred`, dirty flags preserved | `defer_vector_overlays` and not forced | Medium; defer behavior must preserve dirty flags for a later frame |
| Hydrology vector cache | `_current_hydrology_view_key()`, `_lookup_vector_overlay_cache()`, `_render_hydrology_if_needed()` | `lake_overlay_rgba`, `river_overlay_rgba`, `hydrology_view_key` | `hydrology_dirty`, view key change, force | Medium; cache key includes visibility, overlay identity, view and style state |
| Boundary vector cache | `_current_boundary_view_key()`, `_lookup_vector_overlay_cache()`, `_render_boundaries_if_needed()` | `boundary_overlay_rgba`, `boundary_layer_rgba`, hover highlight state | `boundary_dirty`, `boundary_hover_dirty`, view key change, force | Medium/High; hover phase and per-boundary layer buffers are coupled |
| Compile plan after prepare | `compile_layer_render_plan()` | compiled plan, cache key, invalidation and timing metadata | always after prepare branch | Low/Medium; helper seams exist, but cache behavior must remain unchanged |

## Existing cache/defer evidence

Current controller-owned cache evidence:

- `vector_overlay_cache`
- `vector_overlay_cache_order`
- `vector_overlay_cache_hits`
- `vector_overlay_cache_misses`
- `vector_overlay_cache_deferred`
- `_cache_vector_overlay()`
- `_lookup_vector_overlay_cache()`
- `_vector_cache_limit()`

Current render-plan / metadata evidence:

- `phase_timing_ms.prepare_batches`
- `phase_timing_ms.compose_overlays`
- `slowest_phase_id`
- `bottleneck_recommendation.recommended_next_action`
- repeated quick smoke `summary.json`

## Safe next helper boundary

Implemented helper name:

- `render_core.batch_prepare.build_prepare_batch_cache_evidence()`

Current first implementation:

- Build a serializable evidence packet from already-collected counters and dirty flags.
- Do not decide cache reuse.
- Do not read or write overlay arrays.
- Do not mutate dirty flags.
- Do not render hydrology, boundaries, traffic, pins, icons, globe or preview frames.
- Do not change cache key shape.
- Do not change timing fields or metadata schema.

Candidate payload shape:

```python
{
    "vector_overlay_cache_entries": 0,
    "vector_overlay_cache_limit": 0,
    "vector_overlay_cache_hits": 0,
    "vector_overlay_cache_misses": 0,
    "vector_overlay_cache_deferred": 0,
    "dirty_flags": {...},
    "prepare_phase": "evidence_only",
    "recommended_next_action": "measure_static_batch_reuse_candidate",
}
```

## Stop conditions before behavior work

- Stop if image output parity needs manual comparison.
- Stop if cache key output changes.
- Stop if dirty flag semantics change.
- Stop if vector overlay cache ownership moves out of the controller adapter.
- Stop if overlay arrays enter `render_core`.
- Stop if renderer metadata schema changes.
- Stop if runtime merge is enabled.
- Stop if generated `state/` artifacts become staged.

## Validation for a future helper slice

- `py -3 -m py_compile taichi_global_bathymetry.py render_core\render_plan.py`
- `powershell -NoProfile -ExecutionPolicy Bypass -File scripts\render_quick_smoke.ps1`
- `powershell -NoProfile -ExecutionPolicy Bypass -File scripts\render_repeated_quick_smoke.ps1 -Frames 3`
- `powershell -NoProfile -ExecutionPolicy Bypass -File scripts\smoke.ps1`
- `git diff --check`
- Confirm generated `state/` artifacts remain ignored.
