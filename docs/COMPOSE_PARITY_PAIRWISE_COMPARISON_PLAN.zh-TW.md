# Compose Parity Pairwise Comparison Plan

## TL;DR

This document designs the future baseline-vs-candidate pairwise parity evidence shape for compose execution.

It is docs/evidence-only. It does not modify `taichi_global_bathymetry.py`, Qt code, metadata schema, output behavior, runtime merge, or renderer artifacts.

Current state:

- Contract-only parity scripts exist.
- Artifact diff contract exists.
- Pairwise queue / skip / dispatch / timing / metadata comparators do not exist yet.
- Visual parity is not ready.
- Interactive FPS readiness is not claimed.

## Inputs and current references

This plan builds on:

- `docs\COMPOSE_EXECUTION_SOURCE_MAP.zh-TW.md`
- `docs\COMPOSE_EXECUTION_PARITY_GATE.zh-TW.md`
- `docs\COMPOSE_PARITY_CONTRACT_ONLY_EVIDENCE_PACKET.zh-TW.md`
- `scripts\render_compose_parity_smoke.ps1 -ContractOnly`
- `scripts\render_compose_parity_artifacts.ps1 -ContractOnly`
- `scripts\inspect_render_plan_review_packet.ps1 -ContractOnly`

Current contract-only scripts prove contract availability only. They do not produce baseline/candidate renderer artifacts and do not prove visual parity.

## Pairwise evidence model

Future comparison must always use two explicit sides:

| Side | Meaning | Current expected source |
| ---- | ------- | ----------------------- |
| `baseline` | Current sequential compose execution and metadata. | Existing renderer path before movement. |
| `candidate` | Proposed moved/refactored compose path. | Future opt-in candidate path only after review. |

The comparison packet should not infer a candidate from production runtime behavior. Candidate execution must be opt-in, named, and disabled by default.

Proposed top-level packet:

```json
{
  "schema": "rrkal_displaytools.compose_parity_pairwise_comparison.v1",
  "source": "future_pairwise_comparator",
  "mode": "contract_only|metadata_pair|artifact_pair",
  "baseline": {},
  "candidate": {},
  "comparisons": {},
  "missing_evidence": [],
  "runtime_merge_enabled": false,
  "metadata_schema_changed": false,
  "output_behavior_changed": false,
  "generated_artifacts_staged": false,
  "visual_parity_ready": false,
  "interactive_fps_claimed": false
}
```

## A. Queue pairwise comparison

Goal:

Verify queue construction is equivalent for the same runtime state.

Required baseline fields:

- `schema`
- `source`
- `composition_step_count`
- `executable_step_count`
- `skipped_step_count`
- `queue`
- `skipped_steps`
- `compose_run_count`
- `compose_merge_candidate_run_count`

Required candidate fields:

- same fields as baseline

Comparison keys:

- queue length
- queue step ids
- queue step kinds
- `source_order`
- `queue_order`
- `compose_queue_reason`
- compose run count
- merge candidate count

Pass condition:

- baseline and candidate queue fields match exactly for the same runtime input packet.

Missing evidence now:

- no candidate queue packet
- no pairwise queue comparator command

Future command path:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\compare_compose_pairwise_packet.ps1 -ContractOnly -Branch queue
```

Status:

`planned_missing_comparator`

## B. Skip reason pairwise comparison

Goal:

Verify skipped steps remain skipped for the same reason.

Required skip reasons:

- `malformed_step`
- `hidden_layer`
- `missing_overlay`
- `transparent_overlay`

Required comparison fields:

- `source_order`
- `id`
- `kind`
- `reason`

Pass condition:

- skipped step count matches
- skipped step ids match
- skipped reasons match
- no candidate-only skip reason appears without review

Missing evidence now:

- no baseline/candidate skip reason pair
- no skip reason diff command

Future command path:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\compare_compose_pairwise_packet.ps1 -ContractOnly -Branch skip
```

Status:

`planned_missing_comparator`

## C. Dispatch path pairwise comparison

Goal:

Verify the future candidate path would choose the same dispatch for each queued step.

Required dispatch branches:

- `runtime_blend`
- `alpha_blend`
- `alpha_compose`
- `runtime_overlay`
- `style_profile_postprocess`
- `skip`

Required fields per step:

- `step_id`
- `layer_id`
- `kind`
- `blend_mode`
- `requires_overlay`
- `overlay_present`
- `dispatch`
- `skip_reason`
- `phase_id`
- `apply_helper`

Pass condition:

- baseline and candidate dispatch packets match for every compared step.
- no candidate dispatch branch becomes executable unless the baseline also executes it.

Missing evidence now:

- dispatch packet contract exists
- no pairwise dispatch packet comparison exists

Future command path:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\compare_compose_pairwise_packet.ps1 -ContractOnly -Branch dispatch
```

Status:

`contract_exists_missing_pair_evidence`

## D. Timing packet pairwise comparison

Goal:

Keep timing packet compatibility without treating timing as visual parity.

Fields to compare structurally:

- `rrkal_displaytools.layer_render_plan_composition_timing.v1`
- `phase_timing_ms`
- `phase_ids`
- `measured_phase_count`
- `compose_overlays_ms`
- `postprocess_ms`
- `runtime_optimization_applied`

Fields allowed to vary:

- elapsed millisecond values
- slowest phase value when runtime conditions differ

Pass condition:

- schema and field shape remain compatible
- units remain milliseconds
- timing packet still reports `runtime_optimization_applied=false` unless separately approved

Missing evidence now:

- no baseline/candidate timing packet pair
- no timing compatibility comparator

Future command path:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\compare_compose_pairwise_packet.ps1 -ContractOnly -Branch timing
```

Status:

`planned_shape_comparison_only`

## E. Metadata pairwise comparison

Goal:

Ensure renderer metadata remains compatible after any future compose movement.

Required baseline/candidate sidecars:

- baseline `.metadata.json`
- candidate `.metadata.json`

Required invariant fields:

- `schema=rrkal_displaytools.renderer_output_metadata.v1`
- output file path behavior unchanged
- `layer_render_plan`
- `layer_render_plan_summary`
- `compose_queue_count`
- `compose_queue_skipped_count`
- `compose_run_count`
- `compose_merge_candidate_run_count`
- `phase_timing_status`
- `slowest_phase_id`
- `runtime_optimization_applied`

Pass condition:

- metadata schema unchanged
- required fields present on both sides
- field types compatible
- no output behavior change

Missing evidence now:

- no candidate metadata sidecar
- no metadata pair comparator command

Future command path:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\compare_compose_pairwise_packet.ps1 -ContractOnly -Branch metadata
```

Status:

`metadata_contract_exists_missing_candidate_sidecar`

## F. Artifact diff pairwise comparison

Goal:

Prove visual parity before any compose execution movement is accepted.

Required artifacts:

- `state\compose_parity\baseline_sequential_frame_rgba.png`
- `state\compose_parity\merged_candidate_frame_rgba.png`
- `state\compose_parity\renderer_output_metadata.json`
- `state\compose_parity\render_compose_parity_smoke_manifest.json`

Existing future command path:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\render_compose_parity_smoke.ps1 -BaselinePath state/compose_parity/baseline_sequential_frame_rgba.png -CandidatePath state/compose_parity/merged_candidate_frame_rgba.png -ManifestPath state/compose_parity/render_compose_parity_smoke_manifest.json -WriteManifest
```

Pass condition:

- image dimensions match
- `visual_parity_passed=true`
- `max_abs_diff=0`
- `changed_pixel_count=0`
- `runtime_merge_enabled=false` until separate approval

Important:

This artifact diff command is not run by this task. It is a future gated command path.

Status:

`artifact_diff_contract_exists_not_run`

## Generated artifact handling

Generated parity artifacts must remain local evidence only.

Never stage:

- `state\compose_parity\*.png`
- `state\compose_parity\*.json`
- `state\render_compose_parity_smoke_manifest.json`

Required audit before any future commit:

```powershell
git status --short --branch
git diff --cached --name-only -- state
```

Pass condition:

- no `state/` PNG or JSON appears in staged files.

## Future command stages

| Stage | Command type | Artifact behavior | Authorization |
| ----- | ------------ | ----------------- | ------------- |
| 0 | Existing `-ContractOnly` scripts | no renderer artifacts | allowed for docs/evidence |
| 1 | Future pairwise comparator `-ContractOnly` | no renderer artifacts | proposed, not implemented |
| 2 | Future metadata pair comparator | reads baseline/candidate sidecars only | requires candidate sidecar source review |
| 3 | Artifact diff smoke | writes ignored local manifests only when explicitly run | requires o_1/u_o review before use |
| 4 | Candidate runtime path | opt-in only, disabled by default | not authorized by this plan |

## Not authorized

This plan does not authorize:

- editing `taichi_global_bathymetry.py`
- editing Qt code
- changing renderer behavior
- changing metadata schema
- changing output behavior
- enabling runtime merge
- generating PNG/JSON artifacts into the repo
- staging `state/` artifacts
- claiming visual parity ready
- claiming interactive FPS ready
- implementing CanvasStrategy
- implementing Odoriba handoff

## Final classification

`c3_compose_parity_pairwise_comparison_plan_complete_l2_no_push`

Boundary statement:

This is a docs/evidence-only pairwise comparison plan. It defines future baseline-vs-candidate evidence shapes and command paths for queue, skip, dispatch, timing, metadata, and artifact diff parity. It does not modify renderer hot path code, Qt code, metadata schema, output behavior, runtime merge, generated artifacts, CanvasStrategy, Odoriba handoff, visual parity readiness, or interactive FPS readiness.
