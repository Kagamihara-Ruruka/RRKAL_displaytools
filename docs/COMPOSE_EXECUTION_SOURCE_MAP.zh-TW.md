# Compose Execution Source Map

## TL;DR

This document maps the current `HybridRenderController.apply_layer_render_plan_composition()` flow before any compose behavior movement.

It is docs/evidence-only:

- no renderer code change
- no Qt code change
- no smoke artifact generation
- no alpha blending change
- no layer ordering change
- no runtime merge enablement
- no metadata schema change
- no output behavior change
- no ViewCard or Odoriba implementation

Current conclusion:

`render_core.render_plan` already owns many compose packets and contracts, but `taichi_global_bathymetry.py` still owns the live sequential compose execution. The next safe action remains source mapping and parity planning, not behavior movement.

## Current source locations

| Concern | Current owner | Product evidence |
| ------- | ------------- | ---------------- |
| Runtime state scan for compose queue | `HybridRenderController.layer_render_plan_compose_queue()` | Reads visibility, overlay presence, and overlay transparency from live controller state. |
| Queue and skip packet construction | `render_core.render_plan.build_layer_render_plan_compose_queue_packet_from_states()` | Pure packet construction after controller-collected runtime state. |
| Compose run grouping | `render_core.render_plan.build_layer_render_plan_compose_runs()` | Groups adjacent queue entries and marks merge candidates. |
| Parity contract | `render_core.render_plan.build_layer_render_plan_compose_run_parity_contract()` | Keeps runtime merge disabled and requires visual parity before merge. |
| Dispatch packet | `render_core.layer_render_plan_composition_dispatch.build_layer_render_plan_composition_dispatch_packet()`; re-exported by `render_core.render_plan` | Maps action kind and overlay presence to dispatch decision. |
| Live pixel execution | `HybridRenderController.apply_layer_render_plan_composition()` | Applies runtime blend, alpha blend, alpha compose, runtime overlay, and style postprocess. |
| Timing packet | `render_core.layer_render_plan_residual_packet_surfaces.build_layer_render_plan_composition_timing_packet()`; re-exported by `render_core.render_plan` | Normalizes controller-measured phase timing. |
| Phase timing runtime packet | `render_core.render_plan.build_layer_render_plan_phase_timing_runtime_packet()` | Selects slowest phase and bottleneck recommendation. |
| Metadata summary | `render_core.layer_render_plan_cache_diagnostics.build_layer_render_plan_metadata_summary()`; re-exported by `render_core.render_plan` | Summarizes compiled plan and phase timing without replacing full metadata. |

## A. `apply_layer_render_plan_composition()` source flow

Current live flow:

1. Starts from `self.globe_rgba`.
2. Selects `steps` from the caller, or falls back to `self.layer_render_plan_composition_steps()`.
3. Builds a style postprocess packet from `args.style_profile`.
4. Initializes per-phase timing collection.
5. Checks opt-in `runtime_blend_timing`.
6. Iterates each plan step.
7. Skips malformed non-dict steps.
8. Builds an apply action via `build_layer_render_plan_composition_apply_action(step)`.
9. Resolves the live overlay via `self.layer_render_plan_step_overlay(step)`.
10. Builds a dispatch packet via `build_layer_render_plan_composition_dispatch_packet(action, overlay is not None)`.
11. Executes exactly one dispatch branch:
    - `runtime_blend` -> `self.compose_runtime_blend(frame, layer_id, overlay)`
    - `alpha_blend` -> `alpha_blend_compose(frame, overlay, blend_mode)`
    - `alpha_compose` -> `alpha_compose(frame, overlay)`
    - `runtime_overlay` -> `self.compose_runtime_overlay(frame, layer_id, overlay)`
    - `style_profile_postprocess` -> `apply_style_profile(frame, style_profile)`
12. Accumulates elapsed time into `compose_overlays` or `postprocess`.
13. Builds `layer_render_step_timing_packet`.
14. Stores `self.layer_render_step_timing_ms`.
15. If runtime blend timing is enabled, stores `self.runtime_blend_timing_packet`.
16. Returns the composed `frame`.

Important boundary:

The function executes pixels. It is not a safe first extraction target.

Classification:

`do_not_touch_behavior`

## B1. Queue building

Current queue build is split:

- Controller stage: `HybridRenderController.layer_render_plan_compose_queue()`
- Pure packet stage: `render_core.render_plan.build_layer_render_plan_compose_queue_packet_from_states()`

Controller-owned live reads:

- step kind
- layer visibility
- overlay lookup
- overlay alpha transparency

`render_core`-owned packet decisions:

- queue entries
- skipped steps
- queue order
- source order
- compose queue reason
- compose runs
- merge candidate count
- parity contract

This is already partially extracted, but not fully decoupled because overlay lookup and visibility semantics remain controller-owned.

Classification:

`already_partially_extracted`

## B2. Skip reasons

Current skip reasons in `render_core.render_plan.build_layer_render_plan_compose_queue_entries()`:

| Reason | Meaning | Behavior risk |
| ------ | ------- | ------------- |
| `malformed_step` | Input step was not a dict. | Low for docs; behavior should not move without smoke. |
| `hidden_layer` | Runtime state marked the layer invisible. | Medium; visibility semantics come from controller and UI state. |
| `missing_overlay` | Overlay was not present for an overlay-requiring step. | Medium; overlay lookup remains live controller behavior. |
| `transparent_overlay` | Overlay alpha channel contains no visible pixels. | Medium; transparency skip affects whether work is executed. |

Style profile postprocess is queued with `compose_queue_reason=postprocess_required`.

Executable overlays are queued with `compose_queue_reason=executable_overlay`.

Classification:

`requires_parity_before_move`

## B3. Dispatch path

`build_layer_render_plan_composition_apply_action()` maps step kind to intended helper:

| Kind | Apply helper |
| ---- | ------------ |
| `runtime_blend` | `HybridRenderController.compose_runtime_blend` |
| `alpha_blend` | `alpha_blend_compose` |
| `alpha_compose` | `alpha_compose` |
| `runtime_overlay` | `HybridRenderController.compose_runtime_overlay` |
| `style_profile_postprocess` | `apply_style_profile` |

`build_layer_render_plan_composition_dispatch_packet()` then chooses:

- `style_profile_postprocess` when kind is postprocess.
- `skip` with `missing_overlay` when an overlay is required but absent.
- the matching overlay dispatch for runtime/alpha kinds.
- `skip` with `unknown_apply_action` for unknown kinds.

The dispatch packet is a contract surface. The actual dispatch remains in `apply_layer_render_plan_composition()`.

Classification:

`contract_only`

## B4. Timing packet

`apply_layer_render_plan_composition()` measures elapsed time around each executed step and accumulates by phase:

- `compose_overlays`
- `postprocess`

`build_layer_render_plan_composition_timing_packet()` normalizes these values into:

- `schema=rrkal_displaytools.layer_render_plan_composition_timing.v1`
- `phase_timing_ms`
- `phase_ids`
- `measured_phase_count`
- `compose_overlays_ms`
- `postprocess_ms`
- `runtime_optimization_applied=false`

`render_if_needed()` then copies `compose_overlays` and `postprocess` into the broader `phase_timing_ms` packet and builds `rrkal_displaytools.layer_render_plan_phase_timing_runtime.v1`.

Timing evidence can identify bottlenecks. It does not authorize optimization.

Classification:

`evidence_only_candidate`

## B5. Metadata summary

`write_output_metadata()` writes the renderer sidecar through `build_renderer_output_metadata_payload()` and includes:

- full `layer_render_plan`
- `layer_render_plan_summary`

`build_layer_render_plan_metadata_summary()` summarizes:

- full plan schema
- cache status and reuse decision
- visible layer count
- composition step count
- compose queue count
- skipped queue count
- compose run count
- merge candidate run count
- execution phase count
- phase timing status
- slowest phase
- runtime optimization flag

Boundary:

The summary is not a replacement for full `layer_render_plan`. It is a compact metadata aid for debugging and evidence review.

Classification:

`already_partially_extracted`

## B6. Parity requirements

Current compose parity contract:

- runtime merge is explicitly disabled.
- merge candidates are only adjacent `alpha_compose` runs.
- merge is blocked until visual parity passes.
- required comparison is sequential compose queue vs merged candidate RGBA diff.
- required tolerance is `max_abs_diff=0` and `changed_pixel_count=0`.
- contract references `scripts\render_compose_parity_smoke.ps1`.

Current docs also require parity before:

- alpha blending changes
- layer ordering changes
- runtime merge
- runtime blend optimization
- array-copy reduction
- blend-mode rewrite
- output pixel behavior change

Classification:

`requires_parity_before_move`

## Source-flow table

| Stage | Live behavior? | Current owner | Move risk | Next safe action |
| ----- | -------------- | ------------- | --------- | ---------------- |
| Composition step creation | no direct pixels | controller + `render_core.layer_render_plan_residual_packet_surfaces`; re-exported by `render_core.render_plan` | medium | map inputs before moving |
| Runtime state scan | reads live controller state | controller | medium | keep controller-owned until state contract is stronger |
| Queue packet | packet only | `render_core.render_plan` | low/medium | keep contract stable |
| Skip reason packet | packet only, behavior-sensitive meaning | `render_core.render_plan` | medium | use as evidence, not optimization |
| Compose run grouping | packet only | `render_core.render_plan` | low | use for parity planning |
| Dispatch packet | packet only | `render_core.render_plan` | low/medium | keep separate from execution |
| Pixel dispatch execution | yes | controller | high | do not move without parity |
| Timing normalization | packet only | `render_core.layer_render_plan_residual_packet_surfaces`; re-exported by `render_core.render_plan` | low | evidence-only improvements possible |
| Metadata summary | packet only | `render_core.render_plan` | low | keep schema stable |

## Safe next candidate zones

The next safe zones remain docs/evidence or pure packet boundaries:

1. Add a contract-only compose queue inspector that reads existing metadata and reports queue/run/skip counts.
2. Refresh render-plan compile source map after any future packet helper extraction.
3. Add wording-only parity checklist updates before any compose behavior review.

Do not start runtime merge, alpha collapse, or blend-path optimization from this source map.

## Stop conditions before implementation

Stop if any future slice requires:

- editing `taichi_global_bathymetry.py`
- changing alpha blend math
- changing layer ordering
- enabling runtime merge
- changing metadata schema
- changing output pixels
- launching Qt
- implementing ViewCard consumption
- implementing Odoriba handoff
- treating renderer timing as interactive FPS readiness

## Final classification

`c3_compose_execution_source_map_complete_l2_no_push`

Boundary statement:

This is a docs-only compose execution source map. It maps queue building, skip reasons, dispatch path, timing packets, metadata summary, and parity requirements. It does not modify renderer code, Qt code, smoke scripts, alpha blending, layer ordering, runtime merge, metadata schema, output behavior, ViewCard consumption, or Odoriba integration.
