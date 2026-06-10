# Dynamic Point LOD View-frame Sampling Visibility Adapter Extraction Planning Gate

## Gate 性質

本 gate 將已觀測到的 sampling、count、mask 安山岩橋接層冷卻成 adapter 與 contract extraction planning。它只做規劃，不建立 helper，不建立 checker，不修改 probe script，不修改 production source，也不執行新的 runtime。

frame、renderer、`render_if_needed`、`frame_rgba`、transparent-globe leak 仍然是 stop-line。此 gate 不授權觸碰這些面，也不宣稱任何 correctness、readiness 或 leak fix。

## Evidence read

- `tests/test_displaytools_dynamic_point_lod_view_frame_frame_visibility_stop_line_planning.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_FRAME_VISIBILITY_STOP_LINE_PLANNING_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_runtime_probe_result_interpretation.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_SAMPLING_VISIBILITY_RUNTIME_PROBE_RESULT_INTERPRETATION_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_probe_script_update.py`
- `scripts/dynamic_point_lod_view_frame_one_shot_runtime_probe.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_runtime_probe.py`
- `tests/test_displaytools_dynamic_point_grafting_path_minimal_evidence.py`
- `tests/test_displaytools_dynamic_point_occlusion_responsibility_boundary.py`
- `tests/test_displaytools_dynamic_point_view_frame_occlusion_structure_settlement.py`
- current `taichi_global_bathymetry.py` static scan

## Static scan summary

Static scan found current monolith terms for:

- `_effective_sample_fraction`
- `_sample_projected_frame`
- `visible_count`
- `rendered_count`
- `mask_overlay_to_globe`
- `current_projected`
- `current_sampled_projected`
- `render_if_needed`
- `frame_rgba`

The scan is static evidence only. This gate does not import or execute the monolith.

## Observed bridge evidence packet

```text
projection_seams_observed = true
mask_seam_observed = true
sampled_visible_token = true
visible_count_observation = 2
rendered_count_observation = 1
reduced_sample_supports_rendered_lt_visible = true
mask_false_supports_mask_can_hide_overlay_without_source_loss = true
source_lineage_guard_supported = true
frame_remains_not_observed = true
```

## Adapter candidate matrix

| candidate | planning classification | owns | does not own |
| --- | --- | --- | --- |
| `DynamicPointSamplingVisibilityAdapter` | `adapter_extraction_candidate` | synthetic sampling/count observation | projection formula, renderer frame output |
| `DynamicPointVisibilityCountContract` | `contract_only_candidate` | source/projected/sampled/count/mask/source-lineage fields | frame visible runtime truth |
| `DynamicPointMaskVisibilityContract` | `contract_only_candidate` | mask-visible and mask-hidden semantics | source deletion interpretation |
| `DynamicPointSamplingReductionContract` | `contract_only_candidate` | `rendered_count < visible_count` reduction semantics | source loss |
| `DynamicPointFrameVisibilityStopLineContract` | `blocked_by_frame_stop_line` | frame, renderer, leak blocked-surface ledger | frame buffer read, renderer execution, leak fix claim |

## Extraction boundary classification

This gate allows planning only:

- `DynamicPointSamplingVisibilityAdapter` may be treated as an adapter extraction candidate.
- Visibility count, mask visibility, sampling reduction, and frame stop-line contracts remain contract-only candidates.
- Projection formula is not owned by this path.
- Frame output is not owned by this path.
- Source lineage guard prevents interpreting sampling or mask as source loss.
- Renderer runtime remains blocked.

## Future helper target planning

Future helper target, not created here:

```text
render_core/dynamic_point_sampling_visibility_boundary.py
```

Candidate helper names:

- `build_dynamic_point_sampling_visibility_observation_descriptor`
- `build_dynamic_point_visibility_count_contract_descriptor`
- `build_dynamic_point_mask_visibility_contract_descriptor`
- `build_dynamic_point_sampling_reduction_contract_descriptor`
- `build_dynamic_point_frame_visibility_stop_line_descriptor`
- `dynamic_point_sampling_visibility_boundary_descriptor`
- `dynamic_point_sampling_visibility_planning_bundle`

Allowed future content is descriptor-only, contract-only, stop-line ledger, and source-lineage guard labels. Blocked future content includes projection formula, mask formula, sampling formula movement, frame buffer read, renderer runtime, and artifact write.

## Import boundary and checker need

Expected decision:

```text
new_checker_required = true
existing_checker_reusable = false
future_checker_target = scripts\validate_displaytools_dynamic_point_sampling_visibility_import_boundary.py
checker_creation_authorized = false
```

The dedicated checker is needed because this adapter candidate sits between observed sampling/count/mask semantics and blocked frame/projection/runtime surfaces. This gate only records the need. It does not create the checker.

## Acceleration decision

```text
adapter_extraction_planning_passed = true
sampling_visibility_adapter_path_supported = true
production_extraction_authorized = false
helper_creation_authorized = false
checker_creation_authorized = false
probe_script_change_authorized = false
production_source_change_authorized = false
render_if_needed_authorized = false
controller_instantiation_authorized = false
renderer_execution_authorized = false
frame_buffer_read_authorized = false
artifact_generation_authorized = false
formula_movement_authorized = false
renderer_behavior_change_authorized = false
compose_order_change_authorized = false
coordinate_correctness_claimed = false
visual_correctness_claimed = false
transparent_globe_leak_fix_claimed = false
readiness_claimed = false
next_gate = dynamic_point_lod_view_frame_sampling_visibility_import_boundary_checker_gate
```

## Recommended next gate

`dynamic_point_lod_view_frame_sampling_visibility_import_boundary_checker_gate`

下一步應先建立專用 import-boundary checker gate，再考慮 helper 或 contract 實作。這可防止 adapter planning 誤帶 projection、mask formula、frame buffer、renderer runtime 或 artifact writer。

## Boundary statement

Docs/test-only dynamic point LOD view-frame sampling / visibility adapter extraction planning gate. No helper creation, no checker creation, no probe script change, no production source change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no formula or renderer behavior change, no correctness/readiness/leak-fix claim, and no push.
