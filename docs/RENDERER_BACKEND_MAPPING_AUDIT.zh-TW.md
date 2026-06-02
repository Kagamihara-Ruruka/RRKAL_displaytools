# Renderer Backend Mapping / Decomposition Audit

Date: 2026-06-02
Scope: `RRKAL_displaytools` only
Status: active decomposition map

This audit maps the current renderer preview/demo path from UI or script action to backend entrypoint, render plan, metadata, profiler evidence, and preview artifacts. It is intended to make the current backend flow easier to explain before the next decomposition slice.

## Boundary

- This document does not grant cross-repo work.
- RRKAL / `APIkeys_collection` remains responsible for dataset discovery, download, import, manifest, cache governance, and asset lifecycle.
- `RRKAL_displaytools` owns renderer-facing display controls, preview evidence, render metadata, profiler evidence, and visualization contracts.
- Runtime merge remains disabled.
- Metadata schema must remain `rrkal_displaytools.renderer_output_metadata.v1` unless a separate review approves a schema change.
- Current repeated quick-render evidence measures process-per-frame startup / preview stability, not interactive in-process FPS readiness.

## Backend mapping table

| UI action / future control | Backend entrypoint | Render plan / LayerRenderState dependency | Layer / overlay affected | Metadata field emitted | Profiler / timing evidence | Preview artifact | Current gap / risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Quick render evidence | `scripts/render_quick_smoke.ps1` -> `py -3 taichi_global_bathymetry.py --headless --once --demo-closed-loop` | `HybridRenderController.render_if_needed(force=True)` then `compile_layer_render_plan()` | Globe, grid, stars, ocean material, terrain contours, scale; quick script disables lake/river/border/maritime/aircraft/pin layers | `.metadata.json` with `schema`, `render_ms`, `visible_layers`, `layer_render_plan`, `layer_render_plan_summary` | `layer_render_plan.phase_timing_runtime.phase_timing_ms`, `slowest_phase_id`, `bottleneck_recommendation` | `state/showcase/quick_smoke.png`, `state/showcase/quick_smoke_preview_frame.png` | Single frame only; useful for artifact demo, not FPS readiness |
| Repeated quick render evidence | `scripts/render_repeated_quick_smoke.ps1` wrapping quick render | Reads each generated metadata sidecar; no renderer behavior change | Same as quick render per child process | `state/showcase/repeated_quick_smoke*/summary.json` summarizes metadata | Per-frame `render_ms`, `prepare_batches_ms`, `compose_overlays_ms`, `slowest_phase_id`, recommendation | `frame_XX.png`, `preview_XX.png` under ignored `state/showcase/repeated_quick_smoke*` | Process-per-frame evidence; does not prove in-process warm-frame FPS |
| Layer enable / disable | Qt panel / profile args -> `layer_visible` and `refresh_layer_runtime_state()` | `layer_render_plan_runtime_snapshot()` records `dirty_flags`, visible layers, selected semantic target | All layer ids in `layer_visible`; overlay path depends on layer kind | `layer_visible`, `visible_layers`, `layer_render_plan.runtime_snapshot` | Dirty flags influence batch decisions and execution phases | Same preview/output path if render is requested | UI mapping is broad; authoritative geospatial identity remains separate |
| Hydrology layers | Args/profile layer state -> `_render_hydrology_if_needed()` | Hydrology view key, vector overlay cache, `HydrologyRenderLODProfile`, composition steps | `lakes`, `rivers`, `lake_overlay_rgba`, `river_overlay_rgba` | `visible_layers`, `layer_visible`, `layer_render_plan.batch_decisions`, `runtime_snapshot` | `prepare_batches` includes hydrology overlay preparation when active | Output/preview PNG if render requested | Quick evidence disables hydrology; separate hydrology LOD inspector covers contract readiness |
| Boundary / borders / maritime layers | Args/profile layer state -> `_render_boundaries_if_needed()` | Boundary view key, vector overlay cache, boundary highlight state, composition steps | `borders`, `territorial_sea`, `eez`, `high_seas`, `boundary_layer_rgba`, `boundary_overlay_rgba` | `boundary_highlight`, `layer_render_plan`, `layer_render_plan_summary` | `prepare_batches` includes boundary overlay preparation when active | Output/preview PNG if render requested | Authoritative polygon / open-line area identity is pending backend geometry work |
| AIS / traffic overlay | `refresh_ais_if_due()`, projection, datashader overlay render | Runtime snapshot and composition steps include `ais_overlay` when visible | `overlay_rgba`, `current_projected`, sampled projected data | `visible_layers`, `layer_render_plan.apply_path`, `batch_decisions` | `prepare_batches` includes projection/sampling/rendering when active | Output/preview PNG if render requested | Live data/network behavior is outside quick synthetic evidence |
| Grid / stars | `TaichiGlobeRenderer.render()` and `render_stars()` | Globe dirty state and Taichi render path before render plan composition | Globe base frame, star pass | `visible_layers`, `basemap_lod`, `render_ms` | Part of `prepare_batches` in current phase timing | Output/preview PNG | First-frame Taichi / base globe cost dominates current evidence |
| Contours / scale | Rendered through existing globe/overlay composition path and layer visibility | Render plan composition steps and visible layer state | `contours`, `scale` | `layer_visible`, `layer_opacity`, `layer_render_plan` | Phase timing reports total prepare/compose, not individual contour/scale costs | Output/preview PNG | More granular sub-phase timing is not yet extracted |
| LOD counters | Runtime optimization review helpers and `layer_render_plan_performance` contract | `runtime_pressure_snapshot`, `layer_render_state`, `lod_counters` packets | LOD bucket, visible vector records, cache/defer counters | `renderer_output_metadata.policies.lod_counters` when emitted through capability/handoff surfaces | Inspector and smoke contract evidence; actual quick metadata focuses on phase timing | No direct image artifact; tied to metadata/inspectors | Actual runtime LOD counter evidence is still less direct than phase timing |
| Metadata summary | `write_output_metadata()` and `build_layer_render_plan_metadata_summary()` | Uses compiled layer render plan or compiles one if missing | All visible layers and selected layer state | `layer_render_plan_summary`, full `layer_render_plan` | Contains phase timing runtime and bottleneck recommendation when available | `.metadata.json` sidecar | Builder still lives in monolith-facing path and should be separated carefully |
| FPS / timing / bottleneck report | `render_if_needed()` builds `phase_timing_ms`, then `build_layer_render_plan_phase_timing_runtime_packet()` | Depends on render phases: prepare, compose, postprocess, future single-pass candidate | Whole render frame | `layer_render_plan.phase_timing_runtime` | `render_ms`, `prepare_batches`, `compose_overlays`, `slowest_phase_id`, recommendation | Summary scripts copy timing from metadata | The current main bottleneck remains `prepare_batches`; interactive FPS is not established |

## Render flow map

1. Script or UI selects a renderer path.
2. `scripts/render_quick_smoke.ps1` calls `taichi_global_bathymetry.py` with `--headless --once --demo-closed-loop`, an output PNG path, and a preview frame path.
3. `main()` applies demo defaults, initializes Taichi, creates `HybridRenderController`, and calls `render_if_needed(force=True)` for headless/once mode.
4. `HybridRenderController.__init__()` loads synthetic/topography inputs, masks, star cache, layer defaults, runtime state files, and overlay buffers.
5. `render_if_needed()` refreshes runtime state, timeline state, AIS/aircraft state, and LOD.
6. `render_if_needed()` computes `changed`, builds an initial `layer_render_plan_runtime_snapshot()`, and enters the prepare phase.
7. Prepare phase renders the globe base frame through `TaichiGlobeRenderer`, projects / samples traffic data, prepares optional overlays, and updates hydrology / boundary overlays when not deferred.
8. `compile_layer_render_plan()` builds composition steps, runtime snapshot, compose queue, cache key, invalidation reasons, batch decisions, apply path, execution summary, phase timing contract, and adapter payload.
9. `apply_layer_render_plan_composition()` applies runtime blend, alpha blend/compose, runtime overlays, and style profile postprocess in the current sequential composition path.
10. `render_if_needed()` records `prepare_batches`, `compose_overlays`, `postprocess`, total render time, and `phase_timing_runtime`.
11. If output is requested, `write_output_metadata()` writes the PNG sidecar using `rrkal_displaytools.renderer_output_metadata.v1`.
12. `write_preview_frame_if_due()` writes the file-based preview frame.
13. `scripts/render_repeated_quick_smoke.ps1` repeats the quick path and builds an ignored local `summary.json` from the metadata sidecars.

## Current evidence baseline

Latest accepted checkpoints:

- `53c8464 perf: reuse static overlay batches in prepare path`
- `64af56c test: add repeated quick render evidence script`

Validated evidence paths before this audit:

- `scripts/render_repeated_quick_smoke.ps1 -Frames 3`: PASS
- `scripts/render_repeated_quick_smoke.ps1 -Frames 5`: PASS
- `scripts/render_quick_smoke.ps1`: PASS
- `scripts/smoke.ps1`: PASS

Current interpretation:

- Good enough for still-frame / preview artifact demo.
- Not evidence for interactive FPS readiness.
- Main bottleneck remains `prepare_batches`.

## Big-ball responsibility audit for `taichi_global_bathymetry.py`

| Responsibility | Current mixed location | Why it is coupled | Decomposition concern |
| --- | --- | --- | --- |
| Data / synthetic input setup | `HybridRenderController.__init__()` plus top-level loaders | Input loading, masks, star cache, runtime state, and renderer object creation happen together | Separate provider setup from renderer controller construction |
| Layer config | `__init__()`, layer setters, profile/runtime state methods | Layer defaults, profile state, runtime files, and UI-facing flags share controller state | Extract a LayerState packet builder before moving behavior |
| Layer state / runtime snapshot | `refresh_layer_runtime_state()`, `layer_render_plan_runtime_snapshot()` | Runtime files, selected layer, visible layers, dirty flags and render plan facts are collected in the controller | Low-risk extraction if kept pure and no IO moved into core |
| Render plan compilation | `compile_layer_render_plan()` | Pure-ish packet construction depends on controller overlay lookup and scalar layer facts | Continue moving pure helpers to `render_core/render_plan.py` |
| Batch prepare | `render_if_needed()` prepare phase, `_render_hydrology_if_needed()`, `_render_boundaries_if_needed()` | Globe rendering, traffic projection, overlay drawing, vector cache, and layer dirty handling share one phase | Highest current bottleneck; split measurement before behavior changes |
| Overlay drawing | Hydrology/boundary/traffic/pin/icon render helpers | Uses projection, masks, style, LOD and cache keys | Candidate for renderer-ready batch cache module |
| Overlay composition | `apply_layer_render_plan_composition()` | Current sequential path combines dispatch, blending, style postprocess and timing | Keep runtime merge disabled until parity evidence is complete |
| Cache / reuse policy | vector overlay cache helpers, compiled plan cache key helpers | Cache policy spans view keys, dirty flags, vector overlays and compiled plans | Extract policy metadata first, behavior second |
| Metadata building | `write_output_metadata()` | Builds schema payload, summary and boundary fields inside controller | Good low-risk extraction candidate if payload is byte-for-byte equivalent |
| Profiler timing | `render_if_needed()` and render plan timing helpers | Phase timing is collected inline with render behavior | Extract formatting/summary only before deeper timing changes |
| Preview artifact writing | `write_preview_frame_if_due()` and quick/repeated scripts | Image write path is embedded in controller but evidence summary is in scripts | Writer extraction is low risk if path and bytes behavior stay unchanged |
| Evidence / smoke support | `scripts/render_quick_smoke.ps1`, `scripts/render_repeated_quick_smoke.ps1`, smoke gates | Evidence scripts depend on metadata shape and artifact paths | Keep as scripts until runtime modules stabilize |
| UI-facing state surface | Qt panel, launch packets, renderer capabilities, handoff inspectors | UI reads contracts that are partly emitted from monolith state | Preserve contracts during extraction; avoid changing UI wording into integration claims |

## Decomposition candidate list

| Candidate | Proposed module / helper | Current source location | Expected benefit | Risk | Test path | Output / metadata schema |
| --- | --- | --- | --- | --- | --- | --- |
| Render metadata payload builder | `render_core.metadata.build_renderer_output_metadata_payload()` | `HybridRenderController.write_output_metadata()` | Makes metadata schema ownership explicit and testable | Low | `render_quick_smoke.ps1`, metadata schema check, `smoke.ps1` | Completed; schema unchanged |
| Repeated evidence summary helper | script-local `New-RepeatedQuickSmokeSummary` helper | `scripts/render_repeated_quick_smoke.ps1` | Easier to test summary aggregation without launching renderer | Low | `render_repeated_quick_smoke.ps1 -Frames 3` | Completed; renderer metadata schema unchanged |
| Timing summary formatter | `_normalize_phase_timing_ms()` / `_select_slowest_phase()` in `render_core.render_plan` | `build_layer_render_plan_phase_timing_runtime_packet()` | Makes bottleneck reporting easier to explain and reuse | Low | quick/repeated smoke; inspect metadata | Completed; renderer metadata fields unchanged |
| Preview evidence writer | `render_core.preview.write_preview_frame_png()` | `write_preview_frame_if_due()` | Separates file output from controller logic | Low/Medium | quick smoke preview file check | Completed; output image path and preview bytes behavior unchanged |
| Layer state packet builder | `render_core.layer_state.build_layer_runtime_snapshot_input()` | `refresh_layer_runtime_state()`, `layer_render_plan_runtime_snapshot()` | Reduces UI/runtime/controller coupling | Medium | smoke, layer inspectors, quick smoke | Metadata schema unchanged |
| Render plan compile facade | `render_core.render_plan.compile_from_controller_payload()` | `compile_layer_render_plan()` | Moves plan packet assembly out of controller | Medium | render plan inspectors, smoke, quick smoke | Metadata schema unchanged |
| Static batch prepare cache | `render_core.batch_prepare` / `renderer_runtime.static_batch_cache` | `render_if_needed()`, `_render_hydrology_if_needed()`, `_render_boundaries_if_needed()` | Directly targets `prepare_batches` bottleneck | Medium/High | repeated quick smoke, quick smoke, smoke; compare metadata timing | Output image should remain equivalent; metadata schema unchanged |
| Renderer core extraction | `render_core.taichi_globe_runtime` | `TaichiGlobeRenderer` and controller render loop | Long-term module clarity | High | image parity, repeated renderer evidence, smoke | Requires explicit parity gate; do not start as first slice |

## Completed extraction status

Completed low-risk candidates:

- `render_core.metadata.build_renderer_output_metadata_payload()`
- script-local repeated quick smoke summary helper
- render-plan phase timing normalization helpers
- `render_core.preview.write_preview_frame_png()`

All completed candidates kept renderer output metadata schema unchanged, runtime merge disabled, generated `state/` artifacts ignored, and quick/repeated/smoke gates passing at their checkpoints.

## Recommended next safe step

Next candidate: layer state source-map before implementation.

Reason:

- `Layer state packet builder` is medium risk because UI state, runtime state files, dirty flags and selected semantic target share controller state.
- Start with a source-map / contract inventory, not behavior movement.
- Only after the source-map identifies a pure packet boundary should a helper extraction be attempted.
- Quick/repeated render evidence and smoke must remain the checkpoint gates.

Required gate before commit:

- `scripts/render_quick_smoke.ps1`
- `scripts/render_repeated_quick_smoke.ps1 -Frames 3`
- `scripts/smoke.ps1`
- `git diff --check`
- Confirm generated `state/` artifacts remain ignored.

## Current stop-condition status

- Renderer runtime behavior change required: no.
- Metadata schema change required: no.
- Runtime merge required: no.
- Cross-repo code required: no.
- Generated artifacts committed: no.
- Interactive FPS readiness implied: no.
