# Dynamic Point LOD View-Frame Presentation Reduction Import-Boundary Checker Planning Gate

## 目的

本 gate 為 future `render_core/dynamic_point_presentation_reduction_boundary.py` 規劃專用 AST-only import-boundary checker。它只定義 checker 應守的門，不建立 checker，不建立 helper，不修改既有 checker，也不修改 `render_core`、runtime probe 或 `taichi_global_bathymetry.py`。

核心邊界是：presentation reduction 只能表達 `rendered_count < visible_count` 的 presentation 或 sampling reduction candidate，不得漂移成 source-loss、frame-truth、transparent-globe leak、correctness、performance 或 readiness claim。

## Evidence read

本 gate 引用下列 evidence：

- `tests/test_displaytools_dynamic_point_lod_view_frame_presentation_reduction_contract_planning.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_PRESENTATION_REDUCTION_CONTRACT_PLANNING_GATE.zh-TW.md`
- `render_core/dynamic_point_presentation_count_boundary.py`
- `render_core/dynamic_point_sampling_visibility_boundary.py`
- `render_core/dynamic_point_source_lineage_guard_boundary.py`
- `scripts/validate_displaytools_dynamic_point_presentation_count_import_boundary.py`
- `scripts/validate_displaytools_dynamic_point_sampling_visibility_import_boundary.py`
- `scripts/validate_displaytools_dynamic_point_source_lineage_guard_import_boundary.py`
- `docs/DOCS_INDEX.zh-TW.md`

## Future targets

Future helper target, planned only：

```text
render_core/dynamic_point_presentation_reduction_boundary.py
```

Future checker target, planned only：

```text
scripts/validate_displaytools_dynamic_point_presentation_reduction_import_boundary.py
```

本 gate 不授權建立 helper 或 checker。

## Checker planning summary

```text
dedicated_checker_required = true
existing_checker_reusable = false
existing_checkers_pattern_reference_only = true
ast_only = true
target_imported = false
target_executed = false
missing_target_status = not_applicable_candidate_missing
missing_target_boundary_passed = true
syntax_error_json_fail = true
syntax_error_nonzero_exit = true
```

AST node coverage 必須包含：

- `Import`
- `ImportFrom`
- `Name`
- `Attribute`
- `Call`
- `FunctionDef`
- `AsyncFunctionDef`
- `ClassDef`

## Allowed string labels

下列 vocabulary 只能作為 data string 通過；若作為 executable name、function、class、call 或 attribute，future checker 必須 fail：

- `rendered_lower_than_visible`
- `presentation_or_sampling_reduction_candidate`
- `visible_count_observation`
- `rendered_count_observation`
- `source_loss_not_inferred`
- `frame_truth_not_claimed`
- `frame_visible_not_observed`
- `transparent_globe_leak_not_inferred`
- `visual_correctness_not_claimed`
- `readiness_not_claimed`
- `source_lineage_guarded_by_source_lineage_guard_boundary`
- `presentation_count_boundary_reference`
- `sampling_visibility_boundary_reference`

## Forbidden families

Future checker 必須規劃覆蓋下列 forbidden families：

- `monolith`
- `runtime_probe`
- `render_if_needed`
- `controller_runtime`
- `renderer_runtime`
- `frame_buffer`
- `artifact_writer`
- `projection_formula`
- `mask_formula`
- `sampling_formula_movement`
- `alpha_compose_formula`
- `dataframe_runtime`
- `live_source`
- `cache_database_io`
- `source_lineage_mutation`
- `source_loss_interpretation`
- `frame_truth_claim`
- `transparent_globe_leak_inference`
- `correctness_claim`
- `visual_parity_claim`
- `readiness_claim`
- `performance_claim`
- `transparent_globe_leak_fix_claim`
- `c4_odoriba_bypass`
- `label_executable_reference`

Negative self-test must cover every forbidden family.

## Planning matrix summary

| Surface | Allowed as string label | Forbidden executable reference | Forbidden drift |
| --- | --- | --- | --- |
| `rendered_lower_than_visible` | true | true | source-loss interpretation, frame-truth claim |
| `presentation_or_sampling_reduction_candidate` | true | true | runtime probe, sampling formula movement |
| `source_loss_not_inferred` | true | true | source-loss interpretation, source-lineage mutation |
| `frame_truth_not_claimed` | true | true | frame truth, frame buffer, renderer runtime |
| `transparent_globe_leak_not_inferred` | true | true | leak inference, leak-fix claim |
| `presentation_count_boundary_reference` | true | true | `render_core` change, helper creation |
| `sampling_visibility_boundary_reference` | true | true | runtime probe, formula movement |

## Existing checker reuse decision

Existing presentation-count, sampling-visibility, and source-lineage guard checkers may be used as implementation patterns only. They are not reusable as the dedicated presentation reduction checker because this surface must specifically guard the reduction relation from drifting into source loss, frame truth, leak inference, visual correctness, performance, or readiness semantics.

## Decision output

```text
presentation_reduction_checker_planning_passed = true
dedicated_checker_required = true
existing_checker_reusable = false
checker_creation_authorized = false
helper_creation_authorized = false
render_core_change_authorized = false
runtime_probe_change_authorized = false
formula_movement_authorized = false
source_loss_interpretation_authorized = false
frame_truth_claim_authorized = false
transparent_globe_leak_inferred = false
visual_correctness_claimed = false
readiness_claimed = false
```

Additional closed authorizations：

```text
checker_modification_authorized = false
taichi_global_bathymetry_change_authorized = false
render_if_needed_authorized = false
controller_renderer_frame_buffer_authorized = false
artifact_generation_authorized = false
real_source_read_authorized = false
source_lineage_mutation_authorized = false
raw_row_seam_runtime_authorized = false
direct_c3_to_c1_integration_authorized = false
c4_odoriba_bypass_authorized = false
coordinate_correctness_claimed = false
visual_parity_claimed = false
performance_claimed = false
rrkal_wide_methodology_claimed = false
```

## Recommended next gate

```text
dynamic_point_lod_view_frame_presentation_reduction_import_boundary_checker_gate
```

## Boundary statement

Docs/test-only dynamic point LOD view-frame presentation reduction import-boundary checker planning gate. No checker creation, no helper creation, no checker modification, no `render_core` change, no runtime/probe/renderer/frame/formula/source behavior change, no source-loss/frame-truth/leak/correctness/readiness/performance claim, no c_4/Odoriba bypass, and no push.
