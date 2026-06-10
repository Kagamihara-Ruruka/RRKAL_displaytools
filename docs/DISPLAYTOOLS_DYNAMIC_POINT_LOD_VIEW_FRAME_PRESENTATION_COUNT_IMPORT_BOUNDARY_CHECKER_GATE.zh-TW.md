# Dynamic Point LOD View-Frame Presentation Count Import-Boundary Checker Gate

## Gate scope

本 gate 建立 `presentation_count_contract` 專用 AST import-boundary checker。它只保護未來 `render_core/dynamic_point_presentation_count_boundary.py` 的 label、contract、ledger 邊界，不建立 helper，不修改 runtime probe，不修改既有 sampling visibility checker。

## Checker target

Default future target:

```text
render_core/dynamic_point_presentation_count_boundary.py
```

Checker path:

```text
scripts/validate_displaytools_dynamic_point_presentation_count_import_boundary.py
```

目前 target missing 時必須 PASS，狀態為 `not_applicable_candidate_missing`，`candidate_exists = false`，`boundary_passed = true`，`violations = []`。

## Checker behavior

- AST-only。
- 不 import target。
- 不 execute target。
- missing target PASS。
- syntax error JSON fail 並回傳 nonzero exit。
- 檢查 `Import`、`ImportFrom`、`Name`、`Attribute`、`Call`、`FunctionDef`、`AsyncFunctionDef`、`ClassDef`。
- allowed string-label distinction 已建立。
- `--self-test-negative` 覆蓋所有 forbidden family。

## Allowed string labels

以下 label 只允許作為 data string 通過：

- `visible_count`
- `rendered_count`
- `visible_count_observation`
- `rendered_count_observation`
- `rendered_lower_than_visible`
- `sampling_or_presentation_reduction_candidate`
- `presentation_count_contract`
- `source_lineage_integrity_token`
- `frame_visible_not_observed`
- `transparent_globe_leak_not_inferred`
- `source_loss_not_inferred`
- `visual_correctness_not_claimed`
- `readiness_not_claimed`

如果這些 label 作為 executable reference、function、class、call 或 attribute，checker 會以 `label_executable_reference` 阻擋。

## Forbidden family coverage

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
- `dataframe_runtime`
- `live_source`
- `cache_database_io`
- `source_loss_interpretation`
- `transparent_globe_leak_inference`
- `correctness_claim`
- `visual_parity_claim`
- `readiness_claim`
- `transparent_globe_leak_fix_claim`
- `label_executable_reference`

## Negative self-test result

`--self-test-negative` 覆蓋 monolith import、runtime probe call/name、`render_if_needed`、controller class/name、renderer attribute/call/name、`frame_rgba`、artifact writer、`Image.fromarray`、`.save`、projection formula call/name、mask formula call/name、sampling formula movement call/name、pandas/numpy/datashader runtime、live source、cache/database IO、source-loss interpretation、transparent-globe leak inference、correctness claim、visual parity claim、readiness claim、transparent-globe leak fix claim、clean synthetic candidate PASS、allowed string labels PASS。

## Existing sampling visibility checker unchanged

本 gate 參考既有 sampling visibility checker 的 AST-only pattern，但未修改該 checker。presentation count checker 是專用 checker，因為 count contract 必須防止 `rendered_count < visible_count` 被推成 source loss、frame truth、visual correctness 或 transparent-globe leak inference。

## Boundary statement

Tooling/test/docs-only dynamic point LOD view-frame presentation count import-boundary checker gate. No helper creation, no `render_core/dynamic_point_presentation_count_boundary.py` creation, no existing sampling visibility checker change, no runtime probe change, no `taichi_global_bathymetry` change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no formula movement, no source-loss interpretation, no transparent-globe leak inference, no correctness/visual parity/readiness/leak-fix claim, no RRKAL-wide methodology promotion, and no push.

## Final classification

`c3_displaytools_dynamic_point_lod_view_frame_presentation_count_import_boundary_checker_gate_committed_for_o1_review_no_push`