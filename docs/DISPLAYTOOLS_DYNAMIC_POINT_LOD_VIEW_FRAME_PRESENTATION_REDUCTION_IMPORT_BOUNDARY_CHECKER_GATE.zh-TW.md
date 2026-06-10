# Dynamic Point LOD View-Frame Presentation Reduction Import-Boundary Checker Gate

## 目的

本 gate 建立 `presentation_reduction` 專用 AST-only import-boundary checker，用來保護 future `render_core/dynamic_point_presentation_reduction_boundary.py`。該 future helper 只能作為 descriptor / contract / ledger helper，不得偷渡 runtime、formula、renderer、frame、source-loss 或 readiness 語意。

本 gate 只建立 checker、checker test、gate doc，並更新 docs index。不建立 `render_core/dynamic_point_presentation_reduction_boundary.py`，不修改任何既有 checker，不修改 runtime probe，不修改 `taichi_global_bathymetry.py`。

## Checker behavior

Checker script：

```text
scripts/validate_displaytools_dynamic_point_presentation_reduction_import_boundary.py
```

Default target：

```text
render_core\dynamic_point_presentation_reduction_boundary.py
```

行為固定如下：

```text
ast_only = true
target_imported = false
target_executed = false
missing_target_status = not_applicable_candidate_missing
missing_target_boundary_passed = true
syntax_error_json_fail = true
syntax_error_nonzero_exit = true
```

AST node coverage：

- `Import`
- `ImportFrom`
- `Name`
- `Attribute`
- `Call`
- `FunctionDef`
- `AsyncFunctionDef`
- `ClassDef`

## Missing target behavior

若 future helper target 尚未存在，checker 回傳 JSON PASS：

```text
candidate_exists = false
status = not_applicable_candidate_missing
boundary_passed = true
violations = []
```

這是預期行為，因為本 gate 不建立 helper。

## Syntax error behavior

若 target source 有 syntax error，checker 必須輸出 JSON fail 且以 nonzero exit 結束。

## Allowed string-label distinction

下列 vocabulary 只能作為 data string 通過；若作為 executable reference、function、class、call 或 attribute，checker 必須 fail，並歸類為 `label_executable_reference`：

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

## Forbidden family coverage

Checker 覆蓋下列 forbidden families：

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

`--self-test-negative` 必須覆蓋全部 forbidden families，並確認 clean synthetic candidate PASS、allowed string labels PASS、executable label reference FAIL。

## Decision output

```text
presentation_reduction_import_boundary_checker_created = true
target_imported = false
target_executed = false
missing_target_passes = true
syntax_error_json_fail = true
negative_self_test_passed = true
allowed_string_label_distinction_preserved = true
helper_creation_authorized = false
runtime_execution_authorized = false
source_loss_interpretation_authorized = false
frame_truth_claim_authorized = false
transparent_globe_leak_inferred = false
readiness_claimed = false
performance_claimed = false
c4_odoriba_bypass_authorized = false
```

## Boundary statement

Tooling/test/docs-only dynamic point LOD view-frame presentation reduction import-boundary checker gate. Checker creation only; no helper creation, no `render_core/dynamic_point_presentation_reduction_boundary.py` creation, no existing checker behavior change, no runtime probe change, no `taichi_global_bathymetry.py` change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no formula movement, no source-loss interpretation, no frame-truth claim, no transparent-globe leak inference or fix claim, no correctness/visual parity/readiness/performance claim, no c_4/Odoriba bypass, and no push.
