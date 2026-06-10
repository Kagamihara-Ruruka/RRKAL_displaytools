# Dynamic Point LOD View-frame Sampling Visibility Followup Probe Design Gate

## Gate 性質

本 gate 把 sampling、visibility、count 跟進 probe 從規劃矩陣冷卻成可實作的 probe design。它不修改 probe script，不執行新的 runtime probe，不修改 production source，不呼叫 `render_if_needed`，不建立 controller，不執行 renderer 或 GUI，不讀 frame buffer，不寫 artifact。

## Evidence read

- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_followup_planning.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_SAMPLING_VISIBILITY_FOLLOWUP_PLANNING_GATE.zh-TW.md`
- `scripts/dynamic_point_lod_view_frame_one_shot_runtime_probe.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_runtime_probe.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_ONE_SHOT_RUNTIME_PROBE_EXECUTION_GATE.zh-TW.md`
- `docs/DOCS_INDEX.zh-TW.md`

## Tokens to observe next

The next probe design should observe:

- `sampled_visible_token`
- `visible_count_observation`
- `rendered_count_observation`
- `mask_visible_token`
- `source_lineage_integrity_token`

## Tokens still not observed next

The next probe design still does not observe:

- `frame_visible_token`
- `transparent_globe_leak_behavior`
- `render_if_needed`
- controller and renderer path

These stay out because they would require frame, controller, renderer, or higher-risk visibility surfaces.

## Minimal synthetic cases

| case | purpose |
| --- | --- |
| `full_sample_case` | baseline sampled token and count observation |
| `reduced_sample_case` | sampled versus rendered count reduction observation |
| `mask_visible_true` | mask-visible path preservation |
| `mask_visible_false_synthetic` | synthetic globe-mask suppression observation |
| `source_lineage_guard_case` | source lineage guard remains stable under sampling labels |

Every case remains synthetic-only, one-shot, stdout-only, and artifact-free.

## Probe script update design

The next gate may consider updating:

```text
scripts/dynamic_point_lod_view_frame_one_shot_runtime_probe.py
```

Potential future update scope:

- add dry-planned sampling visibility cases
- emit `sampled_visible_token` from synthetic sampling case
- emit `visible_count_observation` from synthetic count case
- emit `rendered_count_observation` from synthetic count case
- preserve `mask_visible_token` observation
- preserve `source_lineage_integrity_token` observation

This gate does not make that update.

Future update must not include:

- `render_if_needed` call
- controller instantiation
- renderer execution
- frame buffer read
- artifact write
- formula mutation
- renderer behavior mutation
- compose order mutation

## Oracle design

| condition | verdict |
| --- | --- |
| projected true plus sampled false | `sampling_responsibility_candidate` |
| visible count greater than rendered count | `sampling_or_presentation_reduction_candidate` |
| overlay true plus mask false | `globe_mask_responsibility_candidate` |
| source lineage changed | `source_lineage_pollution_fail` |
| source true plus frame not observed | `still_not_leak_evidence` |

The final rule is important: source presence without frame observation is not transparent-globe leak evidence.

## Decision output

```text
probe_design_gate_passed = true
tokens_to_observe_next_defined = true
tokens_still_not_observed_next_defined = true
minimal_synthetic_cases_defined = true
oracle_design_defined = true
probe_script_update_needed_next = true
this_gate_modifies_probe_script = false
new_runtime_execution_authorized = false
production_source_change_authorized = false
render_if_needed_authorized = false
controller_instantiation_authorized = false
renderer_execution_authorized = false
frame_buffer_read_authorized = false
artifact_generation_authorized = false
formula_change_authorized = false
renderer_behavior_change_authorized = false
compose_order_change_authorized = false
coordinate_correctness_claimed = false
visual_correctness_claimed = false
transparent_globe_leak_fix_claimed = false
readiness_claimed = false
recommended_next_gate = dynamic_point_lod_view_frame_sampling_visibility_probe_script_update_gate
```

## Recommended next gate

Recommended next gate is `dynamic_point_lod_view_frame_sampling_visibility_probe_script_update_gate`.

That gate may consider whether to update the existing probe script. This gate does not authorize a new runtime execution.

## Boundary statement

Docs/test-only dynamic point LOD view-frame sampling / visibility followup probe design gate. No new runtime execution, no probe script change, no production source change, no render_if_needed call, no controller instantiation, no renderer or GUI execution, no frame buffer read, no artifact generation, no formula or renderer behavior change, no correctness/readiness/leak-fix claim, and no push.
