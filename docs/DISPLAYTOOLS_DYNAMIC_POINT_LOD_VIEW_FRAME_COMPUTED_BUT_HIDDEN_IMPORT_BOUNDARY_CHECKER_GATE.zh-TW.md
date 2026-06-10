# Dynamic Point LOD View-frame Computed-But-Hidden Import-Boundary Checker Gate

## 目的

本 gate 建立 `computed_but_hidden` 專用 AST import-boundary checker，保護未來 helper `render_core/dynamic_point_computed_but_hidden_boundary.py`。本 gate 只建立 checker、checker test 與文件，不建立 helper，不修改 `render_core`，不碰 runtime。

## Scope

允許：

- 建立 `scripts/validate_displaytools_dynamic_point_computed_but_hidden_import_boundary.py`。
- 建立 `tests/test_displaytools_dynamic_point_lod_view_frame_computed_but_hidden_import_boundary.py`。
- 更新本文件與 `docs/DOCS_INDEX.zh-TW.md`。
- 參考 presentation count checker pattern，但不修改既有 checker。

不允許：

- 建立 `render_core/dynamic_point_computed_but_hidden_boundary.py`。
- 修改 `render_core`、`taichi_global_bathymetry.py` 或 runtime probe。
- import 或 execute future helper target。
- 呼叫 `render_if_needed`、controller、renderer、frame buffer 或 artifact writer。
- 移動 projection、mask、sampling、alpha-compose formula。
- 把 hidden 解釋成 missing。
- 把 occluded 解釋成 source lineage loss。
- 推論 transparent globe leak。
- 宣稱 correctness、visual parity、readiness 或 leak fix。
- 推廣為 RRKAL-wide methodology。

## Checker 行為

- `ast` only。
- 不 import target。
- 不 execute target。
- default target：`render_core/dynamic_point_computed_but_hidden_boundary.py`。
- missing target PASS：`candidate_exists = false`、`status = not_applicable_candidate_missing`、`boundary_passed = true`、`violations = []`。
- syntax error JSON fail 且 nonzero exit。
- 檢查 `ast.Import`、`ast.ImportFrom`、`ast.Name`、`ast.Attribute`、`ast.Call`、`ast.FunctionDef`、`ast.AsyncFunctionDef`、`ast.ClassDef`。
- `--self-test-negative` 覆蓋所有 forbidden family。
- clean synthetic candidate PASS。
- allowed string labels PASS。
- allowed labels 若作為 executable name、function、class、call 或 attribute 必須 fail。

## Allowed string labels

- `source_present_token`
- `computed_point_token`
- `hidden_visibility_token`
- `frame_visible_not_observed`
- `hidden_is_not_missing`
- `occluded_is_not_source_lineage_loss`
- `computed_but_hidden_contract`
- `transparent_globe_leak_not_inferred`
- `source_loss_not_inferred`
- `frame_buffer_read_blocked`
- `renderer_execution_blocked`
- `readiness_not_claimed`

這些 label 只允許作為資料字串存在。若同一批詞彙被用作 executable reference，checker 會用 `label_executable_reference` 擋下。

## Forbidden families

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
- `hidden_as_missing_interpretation`
- `source_lineage_loss_interpretation`
- `transparent_globe_leak_inference`
- `correctness_claim`
- `visual_parity_claim`
- `readiness_claim`
- `transparent_globe_leak_fix_claim`
- `label_executable_reference`

## Decision output

- `computed_but_hidden_import_boundary_checker_gate_passed = true`
- `checker_created = true`
- `helper_created = false`
- `render_core_change_authorized = false`
- `existing_presentation_count_checker_modified = false`
- `runtime_probe_change_authorized = false`
- `taichi_global_bathymetry_change_authorized = false`
- `target_imported = false`
- `target_executed = false`
- `missing_target_passes = true`
- `syntax_error_json_fail_nonzero_exit = true`
- `negative_self_test_covers_all_forbidden_families = true`
- `allowed_string_label_distinction_preserved = true`
- `hidden_as_missing_authorized = false`
- `source_lineage_loss_interpretation_authorized = false`
- `transparent_globe_leak_inference_authorized = false`
- `coordinate_correctness_claimed = false`
- `visual_parity_claimed = false`
- `readiness_claimed = false`
- `transparent_globe_leak_fix_claimed = false`
- `rrkal_wide_methodology_authorized = false`

## Recommended next gate

`dynamic_point_lod_view_frame_computed_but_hidden_minimal_extraction_planning_gate`

## Boundary statement

Tooling/test/docs-only dynamic point LOD view-frame computed-but-hidden import-boundary checker gate. Checker creation only; no helper creation, no `render_core/dynamic_point_computed_but_hidden_boundary.py` creation, no `render_core` behavior change, no existing presentation count checker change, no runtime probe change, no `taichi_global_bathymetry` change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no formula movement, no hidden-as-missing interpretation, no source-lineage-loss interpretation, no transparent-globe leak inference, no correctness/visual parity/readiness/leak-fix claim, no RRKAL-wide methodology promotion, and no push.

## Final classification

```text
c3_displaytools_dynamic_point_lod_view_frame_computed_but_hidden_import_boundary_checker_gate_committed_for_o1_review_no_push
```
