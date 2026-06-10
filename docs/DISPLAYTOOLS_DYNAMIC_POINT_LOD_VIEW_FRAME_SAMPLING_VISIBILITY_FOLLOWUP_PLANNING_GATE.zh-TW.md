# Dynamic Point LOD View-frame Sampling Visibility Followup Planning Gate

## Gate 性質

本 gate 根據第一次 one-shot synthetic runtime probe interpretation，規劃下一輪 sampling、visibility、count 跟進 probe。它只做設計冷卻，不新增 runtime probe，不修改 probe script，不執行新 probe，不呼叫 `render_if_needed`，不建立 controller，不執行 renderer 或 GUI，不寫 artifact。

## Evidence read

- `scripts/dynamic_point_lod_view_frame_one_shot_runtime_probe.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_runtime_probe.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_ONE_SHOT_RUNTIME_PROBE_EXECUTION_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_runtime_probe_result_interpretation.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_ONE_SHOT_RUNTIME_PROBE_RESULT_INTERPRETATION_GATE.zh-TW.md`
- runtime probe execution authorization review
- dry harness and static wiring evidence

## Phase A: previous result absorption

Observed:

- `project_ais_to_screen_called = true`
- `project_aircraft_to_screen_called = true`
- `mask_overlay_to_globe_called = true`
- `source_lineage_integrity_token = true`
- `projected_visible_token = true`
- `overlay_rendered_token = true`
- `mask_visible_token = true`

Not observed:

- `sampled_visible_token`
- `frame_visible_token`
- `visible_count_observation`
- `rendered_count_observation`
- `transparent_globe_leak_behavior`
- `render_if_needed`
- controller and renderer path

## Phase B: selected followup matrix

This gate defines a selected matrix, not a full Cartesian product.

| entrypoint candidate | token candidate | condition candidate | expected observation |
| --- | --- | --- | --- |
| `existing_projection_mask_probe_path` | `projected_visible_token` | `mask_visible_true` | projection and mask path remains observable |
| `sampling_adapter_candidate` | `sampled_visible_token` | `sample_ratio_full` | sampling visibility candidate |
| `sampling_adapter_candidate` | `sampled_visible_token` | `sample_ratio_reduced` | sampling reduction candidate |
| `sampling_adapter_candidate` | `sampled_visible_token` | `adaptive_sampling_disabled` | sampling baseline candidate |
| `sampling_adapter_candidate` | `sampled_visible_token` | `adaptive_sampling_enabled_label_only` | adaptive sampling label candidate |
| `count_observation_candidate` | `visible_count_observation` | `sample_ratio_full` | visible count candidate |
| `count_observation_candidate` | `rendered_count_observation` | `sample_ratio_reduced` | rendered count candidate |
| `frame_visibility_stop_line` | `frame_visible_token` | `frame_visibility_not_authorized` | stop before frame buffer or renderer |
| `existing_projection_mask_probe_path` | `mask_visible_token` | `mask_visible_false_synthetic` | synthetic mask hidden candidate |
| `render_if_needed_stop_line` | `source_lineage_integrity_token` | `frame_visibility_not_authorized` | `render_if_needed` remains blocked |

Every row keeps `probe_behavior_change_authorized = false`.

## Phase C: allowed and forbidden followup strategy

Allowed for planning:

- synthetic data only
- one-shot only
- stdout-only packet
- no persistent artifact
- no live source
- no DB, cache, or WebSocket
- no GUI interaction
- no controller instantiation unless a future gate explicitly authorizes it

Forbidden:

- call `render_if_needed`
- execute renderer
- read frame buffer
- write PNG, runtime JSON, or state
- change projection, mask, sampling, or compose formula
- change renderer behavior
- claim coordinate correctness
- claim visual correctness
- claim transparent-globe leak fix
- claim readiness or safe-to-extract

## Phase D: oracle planning

Planned oracle rules:

| condition | verdict |
| --- | --- |
| projected true plus sampled false | `sampling_responsibility_candidate` |
| sampled true plus overlay false | `overlay_render_responsibility_candidate` |
| overlay true plus mask false | `globe_mask_responsibility_candidate` |
| mask false plus frame true | `transparent_globe_leak_candidate` |
| source true plus frame false | `computed_but_hidden_supported` |
| source lineage changed | `source_lineage_pollution_fail` |
| visible count observed but rendered count not observed | `count_surface_partial` |
| rendered count lower than visible count | `sampling_or_presentation_reduction_candidate` |

These are planning rules only. They do not execute runtime and do not prove visual or coordinate correctness.

## Phase E: next executable probe authorization draft

Recommended next gate:

```text
dynamic_point_lod_view_frame_sampling_visibility_followup_probe_design_gate
```

Only that future gate may consider whether to create or modify a probe harness. This gate does not authorize probe expansion, renderer execution, `render_if_needed`, controller instantiation, or artifact writes.

## Decision output

```text
planning_gate_passed = true
previous_probe_result_absorbed = true
followup_matrix_defined = true
oracle_planning_defined = true
next_probe_design_cooled = true
runtime_probe_expansion_authorized = false
probe_harness_creation_authorized = false
production_source_change_authorized = false
render_if_needed_authorized = false
controller_instantiation_authorized = false
renderer_execution_authorized = false
artifact_generation_authorized = false
formula_change_authorized = false
renderer_behavior_change_authorized = false
coordinate_correctness_claimed = false
visual_correctness_claimed = false
transparent_globe_leak_fix_claimed = false
readiness_claimed = false
recommended_next_gate = dynamic_point_lod_view_frame_sampling_visibility_followup_probe_design_gate
```

## Boundary statement

Docs/test-only dynamic point LOD view-frame sampling / visibility followup planning gate. No runtime probe expansion, no probe harness creation, no production source change, no renderer execution, no controller instantiation, no artifact generation, no formula or renderer behavior change, no correctness/readiness/fix claim, and no push.
