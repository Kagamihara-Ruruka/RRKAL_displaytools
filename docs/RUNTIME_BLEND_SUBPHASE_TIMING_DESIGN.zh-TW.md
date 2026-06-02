# Runtime Blend Subphase Timing Design

Date: 2026-06-03
Scope: `RRKAL_displaytools` renderer performance evidence only
Status: design/evidence-only; no renderer optimization authorized

## Purpose

This note records what would be needed to measure `runtime_blend` subphase timing after checkpoint `9fc7b14 test: add runtime blend assessment evidence`.

Current evidence shows `compose_overlays` pressure is runtime-blend-dominant by run count, but the renderer still exposes only aggregate `compose_overlays` and `postprocess` timings. This document is a design boundary, not an implementation approval.

## Historical assumptions vs runtime_blend subphase timing design

Still hold:

- Quick smoke is single-frame artifact evidence, not interactive FPS evidence.
- Repeated quick smoke is process-per-frame evidence, not in-process warm-frame FPS evidence.
- Runtime merge remains disabled.
- Renderer output metadata schema remains `rrkal_displaytools.renderer_output_metadata.v1`.
- No renderer behavior, pixel output, alpha semantics or layer ordering may change without a separate review.

Superseded by runtime_blend evidence:

- Alpha-collapse is not the immediate compose target for the current evidence set because default and high-density warm evidence both have `multi_step_alpha_compose_run_count=0`.
- The next compose investigation target is runtime-blend timing, not alpha-compose collapse.

Requires parity before behavior changes:

- Any runtime-blend optimization, composition collapse, array-copy reduction, mask rewrite, blend-mode rewrite or layer-order change requires output parity protection before it can be committed.
- Timing instrumentation that only records measurements may be lower risk, but it still touches renderer execution code and needs an explicit review slice.

Current work remains design/evidence-only:

- No runtime-blend optimization is implemented.
- No Taichi renderer core instrumentation is implemented.
- No metadata schema migration is implemented.
- Generated `state/` evidence remains local and ignored.

## Current code-path inspection

| Concern | Current location | Finding |
| --- | --- | --- |
| Runtime-blend step generation | `render_core.render_plan.build_layer_render_plan_composition_steps()` | Hydrology (`lakes`, `rivers`) and boundary/maritime (`borders`, `territorial_sea`, `eez`, `high_seas`) steps are emitted as `kind=runtime_blend`. |
| Queue filtering | `HybridRenderController.layer_render_plan_compose_queue()` plus `render_core.render_plan.build_layer_render_plan_compose_queue_packet_from_states()` | Hidden, missing, transparent or empty overlays are removed before execution evidence. |
| Execution | `HybridRenderController.apply_layer_render_plan_composition()` | Each queued step is dispatched sequentially. `runtime_blend` calls `HybridRenderController.compose_runtime_blend()`. |
| Current timing | `HybridRenderController.apply_layer_render_plan_composition()` and `render_core.render_plan.build_layer_render_plan_composition_timing_packet()` | Timing is aggregated by phase id, so all runtime-blend work is folded into `compose_overlays`. |
| Output metadata | `HybridRenderController.compile_layer_render_plan()` / metadata sidecar | Existing metadata exposes queue/run facts and aggregate phase timing, not per-step elapsed time. |

## Subphase timing field feasibility

| Candidate field | Feasibility | Notes |
| --- | --- | --- |
| `runtime_blend_total_ms` | Requires non-invasive renderer instrumentation review | Can be summed from per-step timing around `compose_runtime_blend()`, but not available script-side today. |
| `runtime_blend_step_count` | Available now from metadata | Already derivable from compose queue/run counts. |
| `runtime_blend_step_timings` | Requires renderer core instrumentation | Needs per-step timing in `apply_layer_render_plan_composition()`. |
| `runtime_blend_layer_kind_counts` | Script-side derivable | Current evidence can infer hydrology/boundary vector overlay kinds from layer ids. |
| `runtime_blend_layer_step_names` | Available now from metadata | Queue entries expose ids/layer ids. |
| `runtime_blend_array_copy_ms` | Risky / not recommended now | Would require deeper instrumentation inside blend helpers and may be noisy without profiling support. |
| `runtime_blend_mask_prepare_ms` | Requires renderer core instrumentation | Not currently separated from overlay preparation or blend execution. |
| `runtime_blend_rasterize_ms` | Requires renderer core instrumentation | Rasterization is not isolated in current compose timing. |
| `runtime_blend_blend_ms` | Requires renderer core instrumentation | The blend call can be timed, but changing helper internals should be a later reviewed slice. |
| `runtime_blend_postprocess_ms` | Available as aggregate `postprocess`, not runtime-blend-specific | Current postprocess timing is style-profile level, not per runtime-blend step. |
| `runtime_blend_unknown_ms` | Script-side derivable after instrumentation exists | Without per-step timing, unknown runtime-blend residual cannot be computed. |

## Safest timing insertion points

Safe design candidate:

- Add an opt-in timing packet inside `HybridRenderController.apply_layer_render_plan_composition()`.
- Measure each dispatch branch with `time.perf_counter()` using existing `action`, `dispatch_packet`, `layer_id`, `kind`, `phase_id` and queue order.
- Keep the sequential compose path unchanged.
- Store results in a new internal timing packet for analysis scripts to read.

Risky insertion points:

- Inside `alpha_blend_compose()` or `alpha_compose()`, because timing there does not know layer ids or queue order.
- Inside `compose_runtime_blend()` if it requires changing blend semantics, overlay opacity handling or output arrays.
- Around overlay generation/rasterization helpers if the goal is compose-only subphase timing.

## Parity and safety gate recommendation

Future runtime-blend timing instrumentation should require:

- `o_1` review before commit.
- Explicit opt-in measurement mode or clearly output-neutral metadata path.
- `render_quick_smoke.ps1`.
- `render_repeated_quick_smoke.ps1 -Frames 3`.
- `render_warm_frame_smoke.ps1`.
- `render_warm_frame_smoke.ps1 -HighDensityCompose`.
- `smoke.ps1`.
- `git diff --check`.
- Generated artifact ignore audit.
- Metadata schema review if any `.metadata.json` field is added or changed.
- Pixel parity check before any optimization, merge, blend rewrite, array-copy rewrite or layer-order change.

Decision classification: `requires_non_invasive_instrumentation_review`.
