# Dynamic Point LOD View-frame Frame Visibility Stop-Line Planning Gate

## Gate 性質

本 gate 根據第二刀 sampling、visibility、count 判讀結果，規劃 frame visibility 與 transparent-globe leak 的 stop-line。它不修改 probe script，不新增 runtime execution，不呼叫 `render_if_needed`，不建立 controller，不執行 renderer，不讀 `frame_rgba` 或 frame buffer，也不產生 artifact。

目標是防止後續 adapter 或 contract extraction 誤碰 renderer、frame buffer、artifact writer 或 leak claim。

## Evidence read

- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_runtime_probe_result_interpretation.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_SAMPLING_VISIBILITY_RUNTIME_PROBE_RESULT_INTERPRETATION_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_probe_script_update.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_SAMPLING_VISIBILITY_PROBE_SCRIPT_UPDATE_GATE.zh-TW.md`
- `scripts/dynamic_point_lod_view_frame_one_shot_runtime_probe.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_runtime_probe.py`
- `tests/test_displaytools_dynamic_point_occlusion_responsibility_boundary.py`
- `tests/test_displaytools_dynamic_point_view_frame_occlusion_structure_settlement.py`
- current `taichi_global_bathymetry.py` static scan for frame and renderer stop-line terms

## Static scan summary

Static scan found the following stop-line surfaces in current monolith context:

- `frame_rgba`
- `render_if_needed`
- `alpha_compose`
- `write_preview_frame_png`
- `Image.fromarray`
- renderer and controller surfaces

These are static evidence only. This gate does not import the monolith, does not execute renderer, and does not read frame buffers.

## Frame stop-line matrix

| surface | classification | planning meaning |
| --- | --- | --- |
| `frame_visible_token` | `not_observed_stop_line` | second probe kept frame visibility as `not_observed` |
| `frame_rgba_buffer` | `forbidden_runtime_surface` | frame buffer read remains blocked |
| `render_if_needed` | `forbidden_runtime_surface` | render entry remains blocked |
| `controller_instantiation` | `forbidden_runtime_surface` | controller construction remains blocked |
| `renderer_execution` | `forbidden_runtime_surface` | renderer and GUI execution remain blocked |
| `alpha_compose_path` | `future_authorization_candidate` | may be mapped later without formula movement |
| `write_preview_frame_png` | `forbidden_runtime_surface` | artifact-writing surface remains blocked |
| `output_path_save` | `forbidden_runtime_surface` | output save path remains blocked |
| `transparent_globe_leak_behavior` | `fault_not_inferred` | leak behavior remains unobserved and cannot be inferred |

## Observed classification

Observed by the previous probe chain:

- projection seam
- aircraft projection seam
- mask seam
- sampling token
- visible and rendered count
- source lineage guard

## Not observed classification

Still not observed:

- frame visibility
- `frame_rgba`
- `render_if_needed`
- controller
- renderer
- transparent-globe leak behavior

## Leak claim guard

This gate fixes the following guard:

```text
transparent_globe_leak_inferred = false
transparent_globe_leak_fix_claimed = false
frame_visibility_observed = false
frame_buffer_read = false
renderer_executed = false
```

Sampling/count/mask observation does not imply frame behavior. Frame not observed does not imply leak evidence.

## Future authorization decision tree

Three future routes remain possible:

| route | next gate | note |
| --- | --- | --- |
| conservative route | `dynamic_point_lod_view_frame_frame_visibility_stop_line_closure_gate` | close frame and leak stop-lines before extraction planning |
| acceleration route | `dynamic_point_lod_view_frame_sampling_visibility_adapter_extraction_planning_gate` | plan adapter extraction around observed sampling, count, and mask surfaces |
| runtime route | `dynamic_point_lod_view_frame_frame_visibility_probe_authorization_review_gate` | review whether any frame visibility probe may be authorized later |

## Recommended next gate

Recommended next gate:

`dynamic_point_lod_view_frame_sampling_visibility_adapter_extraction_planning_gate`

Reason: sampling, count, and mask are already observable with source-lineage guard intact. Frame and leak remain stop-lines, but they should not block planning around the observed andesite bridge surfaces. This recommendation does not authorize extraction, runtime execution, renderer access, frame buffer read, or leak claim.

## Decision output

```text
frame_visibility_stop_line_planning_passed = true
frame_stop_line_matrix_defined = true
current_evidence_classification_defined = true
leak_claim_guard_defined = true
future_authorization_decision_tree_defined = true
frame_visibility_observed = false
frame_buffer_read = false
renderer_executed = false
controller_instantiated = false
render_if_needed_called = false
artifact_generation_authorized = false
formula_change_authorized = false
renderer_behavior_change_authorized = false
compose_order_change_authorized = false
transparent_globe_leak_inferred = false
transparent_globe_leak_fix_claimed = false
coordinate_correctness_claimed = false
visual_correctness_claimed = false
readiness_claimed = false
recommended_next_gate = dynamic_point_lod_view_frame_sampling_visibility_adapter_extraction_planning_gate
```

## Boundary statement

Docs/test-only dynamic point LOD view-frame frame visibility stop-line planning gate. No probe script change, no new runtime execution, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no formula or renderer behavior change, no correctness/readiness/leak-fix claim, and no push.
