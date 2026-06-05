# Compose Execution Parity Gate

## TL;DR

This document designs the future parity gate required before moving or changing compose execution.

It is docs/evidence-only. It does not touch the renderer hot path, Qt code, metadata schema, output behavior, alpha blending, layer ordering, runtime merge, CanvasStrategy, ViewCard consumption, or Odoriba handoff.

The gate exists because `docs\COMPOSE_EXECUTION_SOURCE_MAP.zh-TW.md` shows a split boundary:

- `render_core.render_plan` already builds queue, run, dispatch, timing, summary, and parity packets.
- `taichi_global_bathymetry.py::HybridRenderController.apply_layer_render_plan_composition()` still executes live pixels.

No compose execution movement should proceed until the branches below have evidence.

## Current evidence surfaces

| Evidence surface | What it can prove now | What it cannot prove yet |
| ---------------- | --------------------- | ------------------------ |
| `docs\COMPOSE_EXECUTION_SOURCE_MAP.zh-TW.md` | Current source ownership and branch map. | Pixel equivalence after movement. |
| `render_core.render_plan.build_layer_render_plan_compose_queue_packet_from_states()` | Queue/skip packet shape after controller-collected runtime state. | That a moved controller runtime state scan is behavior-equivalent. |
| `render_core.render_plan.build_layer_render_plan_compose_runs()` | Compose run grouping and merge candidate metadata. | That merge execution is visually equivalent. |
| `render_core.render_plan.build_layer_render_plan_compose_run_parity_contract()` | Runtime merge remains disabled and parity is required. | That parity artifacts already exist. |
| `scripts\render_compose_parity_smoke.ps1 -ContractOnly` | Contract mode can report required artifact fields without rendering. | Actual pixel diff. |
| `scripts\render_compose_parity_artifacts.ps1 -ContractOnly` | Artifact runner contract and required outputs. | Actual rendered baseline/candidate artifact correctness. |
| `scripts\inspect_render_plan_review_packet.ps1 -ContractOnly` | Review packet includes parity fields and runtime merge disabled status. | Runtime behavior equivalence. |

## Gate branches

### A. Queue building parity

Purpose:

Confirm that the moved or refactored queue builder produces the same queue packet as the current controller path.

Must compare:

- source step count
- queue entry count
- skipped step count
- `source_order`
- `queue_order`
- `compose_queue_reason`
- step ids
- step kinds
- layer ids
- compose run count
- merge candidate count

Required evidence before code movement:

- current controller queue packet
- candidate queue packet
- structural diff report
- no metadata schema drift
- no runtime merge enablement

Pass condition:

- Queue packet fields match for the same runtime state snapshot.
- Any intentionally excluded volatile field is named and reviewed before commit.

Current status:

`missing_runtime_snapshot_pair_evidence`

### B. Skip reason parity

Purpose:

Confirm skipped steps are classified the same way before and after movement.

Skip reasons to preserve:

- `malformed_step`
- `hidden_layer`
- `missing_overlay`
- `transparent_overlay`

Required evidence:

- skipped step list before movement
- skipped step list after movement
- reason-by-step comparison
- visibility and overlay-present inputs recorded in the evidence packet

Pass condition:

- Same skipped step ids and same reasons for the same source order.

Current status:

`missing_skip_reason_pair_evidence`

### C. Dispatch path parity

Purpose:

Confirm dispatch decisions match the current behavior before any execution path is moved.

Dispatch branches to preserve:

- `runtime_blend`
- `alpha_blend`
- `alpha_compose`
- `runtime_overlay`
- `style_profile_postprocess`
- `skip`

Required evidence:

- action packet
- dispatch packet
- overlay-present flag
- selected dispatch
- skip reason when dispatch is `skip`

Pass condition:

- Same action and dispatch packet for each queued step.
- No new dispatch branch becomes executable without review.

Current status:

`contract_only_dispatch_packet_exists`

### D. Timing packet parity

Purpose:

Confirm measurement output is compatible after movement, without using timing as proof of visual correctness.

Fields to preserve:

- `rrkal_displaytools.layer_render_plan_composition_timing.v1`
- `phase_timing_ms`
- `compose_overlays_ms`
- `postprocess_ms`
- `runtime_optimization_applied=false`
- broader `rrkal_displaytools.layer_render_plan_phase_timing_runtime.v1`

Required evidence:

- schema presence
- phase ids present
- timing unit remains milliseconds
- slowest phase and bottleneck recommendation are still derived from phase timing

Pass condition:

- Timing packet shape remains compatible.
- Timing values may vary, but fields and units must not drift.

Current status:

`contract_surface_exists_needs_runtime_pair_evidence`

### E. Metadata summary parity

Purpose:

Confirm metadata sidecar compatibility after compose movement.

Fields to preserve:

- renderer metadata schema `rrkal_displaytools.renderer_output_metadata.v1`
- full `layer_render_plan`
- `layer_render_plan_summary`
- `compose_queue_count`
- `compose_queue_skipped_count`
- `compose_run_count`
- `compose_merge_candidate_run_count`
- `runtime_optimization_applied`
- `slowest_phase_id`

Required evidence:

- baseline `.metadata.json`
- candidate `.metadata.json`
- schema check
- summary field comparison
- no output metadata path change

Pass condition:

- Renderer metadata schema unchanged.
- Summary fields remain present and type-compatible.

Current status:

`metadata_summary_exists_needs_candidate_comparison`

### F. Alpha blending / layer ordering parity

Purpose:

Prevent visual drift from alpha math, blend mode handling, or layer order changes.

Required artifacts:

- baseline sequential frame RGBA
- candidate moved/refactored frame RGBA
- renderer output metadata
- artifact diff manifest

Required diff fields:

- `visual_parity_passed`
- `max_abs_diff`
- `changed_pixel_count`
- image dimensions
- runtime merge enabled flag

Pass condition:

- `visual_parity_passed=true`
- `max_abs_diff=0`
- `changed_pixel_count=0`
- dimensions match
- runtime merge remains disabled unless separately approved

Current script support:

- `scripts\render_compose_parity_smoke.ps1` can run contract-only or artifact diff mode.
- `scripts\render_compose_parity_artifacts.ps1` defines expected baseline/candidate artifact paths.

Current status:

`artifact_diff_gate_defined_not_executed_in_this_task`

### G. Generated artifact audit

Purpose:

Prevent parity PNG/JSON artifacts from entering commits.

Generated paths to treat as local evidence only:

- `state\compose_parity\baseline_sequential_frame_rgba.png`
- `state\compose_parity\merged_candidate_frame_rgba.png`
- `state\compose_parity\renderer_output_metadata.json`
- `state\compose_parity\compose_parity_artifact_runner.json`
- `state\compose_parity\render_compose_parity_smoke_manifest.json`
- `state\render_compose_parity_smoke_manifest.json`

Required audit before commit:

- `git status --short --branch`
- `git diff --cached --name-only`
- confirm no `state/` PNG or JSON is staged

Pass condition:

- Docs/code changes may be staged.
- Generated `state/` PNG/JSON artifacts are not staged.

Current status:

`required_before_any_future_parity_commit`

### H. Missing tests / missing evidence

Missing before compose movement:

- no pairwise queue packet comparison command
- no pairwise skip reason comparison command
- no pairwise dispatch packet comparison command
- no candidate compose executor artifact path
- no automated metadata baseline-vs-candidate sidecar comparison
- no UI/event-loop evidence, which is outside this gate
- no approval to enable runtime merge

Recommended future evidence-only work:

1. Add a contract-only queue/skip/dispatch comparison packet design.
2. Add a docs-only checklist for baseline/candidate artifact naming.
3. Only after o_1/u_o review, add an opt-in artifact generator that does not change default render behavior.

## Existing smoke/test/script inventory

| Script | Safe mode for this gate | Writes artifacts? | Current role |
| ------ | ----------------------- | ----------------- | ------------ |
| `scripts\render_compose_parity_smoke.ps1` | `-ContractOnly` | no renderer artifacts in contract-only mode | Declares parity contract and artifact diff fields. |
| `scripts\render_compose_parity_artifacts.ps1` | `-ContractOnly` | no artifact directories in contract-only mode | Declares artifact runner and precommit gate. |
| `scripts\inspect_render_plan_review_packet.ps1` | `-ContractOnly` | no renderer artifacts in contract-only mode | Exposes review packet fields and runtime merge disabled status. |
| `scripts\smoke.ps1` | not run in this task | may exercise broader repo checks | Validates many contracts, but is outside this docs-only gate run. |

## Not authorized by this gate design

This document does not authorize:

- editing `taichi_global_bathymetry.py`
- editing Qt code
- changing renderer behavior
- changing alpha blending
- changing layer ordering
- enabling runtime merge
- changing metadata schema
- changing output pixels
- implementing CanvasStrategy
- implementing ViewCard consumption
- implementing Odoriba handoff
- claiming interactive FPS readiness

## Future minimum gate packet

A future parity packet should be machine-readable and include:

```json
{
  "schema": "rrkal_displaytools.compose_execution_parity_gate.v1",
  "queue_parity": "pass|fail|not_run",
  "skip_reason_parity": "pass|fail|not_run",
  "dispatch_path_parity": "pass|fail|not_run",
  "timing_packet_compatibility": "pass|fail|not_run",
  "metadata_summary_compatibility": "pass|fail|not_run",
  "visual_parity_passed": false,
  "max_abs_diff": null,
  "changed_pixel_count": null,
  "runtime_merge_enabled": false,
  "metadata_schema_changed": false,
  "output_behavior_changed": false,
  "generated_artifacts_staged": false,
  "interactive_fps_claimed": false
}
```

This packet is a proposal only. It is not implemented by this checkpoint.

## Final classification

`c3_compose_execution_parity_gate_design_complete_l2_no_push`

Boundary statement:

This is a docs/evidence-only compose execution parity gate design. It maps future parity requirements for queue building, skip reasons, dispatch path, timing packets, metadata summary, alpha blending, layer ordering, and generated artifacts. It does not modify renderer code, Qt code, renderer behavior, metadata schema, output behavior, runtime merge, CanvasStrategy, ViewCard consumption, or Odoriba handoff.
