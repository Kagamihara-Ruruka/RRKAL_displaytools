# Dynamic Point LOD View-Frame Presentation Count Import-Boundary Checker Planning Gate

## Gate scope

本 gate 只規劃未來 `presentation_count_contract` helper 的專用 import-boundary checker。它不建立 checker，不建立 helper，不修改 `render_core`，也不修改既有 sampling visibility checker。

## Evidence read

- `tests/test_displaytools_dynamic_point_lod_view_frame_presentation_count_contract_planning.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_PRESENTATION_COUNT_CONTRACT_PLANNING_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_lod_view_frame_next_andesite_bridge_selection.py`
- `tests/test_displaytools_dynamic_point_sampling_visibility_cartography_update.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_boundary_helpers.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_import_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_frame_visibility_stop_line_planning.py`

## Future targets

Future helper target:

```text
render_core/dynamic_point_presentation_count_boundary.py
```

Future checker target:

```text
scripts/validate_displaytools_dynamic_point_presentation_count_import_boundary.py
```

本 gate 只記錄 target。helper creation 與 checker creation 都不授權。

## Existing checker reuse decision

現有 sampling visibility checker 只能作為 pattern reference。它不可直接重用為 presentation count checker，原因如下：

- presentation count contract 需要明確阻擋 `rendered_count < visible_count` 被解讀成 source loss。
- presentation count contract 需要明確阻擋 count observation 被解讀成 frame truth 或 visual correctness。
- presentation count contract 需要保留 `frame_visible_not_observed` 與 `transparent_globe_leak_not_inferred` 的專用 label boundary。

Decision:

- `existing_sampling_visibility_checker_reusable = false`
- `existing_checker_role = pattern_reference_only`
- `dedicated_presentation_count_checker_required = true`

## Checker expectation summary

Future checker 必須符合：

- AST-only。
- 不 import target。
- 不 execute target。
- missing target PASS。
- syntax error JSON fail。
- 檢查 `Import`、`ImportFrom`、`Name`、`Attribute`、`Call`、`FunctionDef`、`AsyncFunctionDef`、`ClassDef`。
- allowed string-label distinction 必須保留。
- negative self-test 必須覆蓋所有 forbidden family。

## Allowed labels

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

這些 label 只允許以資料字串存在。若同名或相近語意變成 executable reference、function、class、call、import 或 attribute，future checker 必須 fail。

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
- `dataframe_runtime`
- `live_source`
- `cache_database_io`
- `source_loss_interpretation`
- `transparent_globe_leak_inference`
- `correctness_claim`
- `visual_parity_claim`
- `readiness_claim`
- `transparent_globe_leak_fix_claim`

## Negative self-test expectations

Future negative self-test 必須覆蓋每一個 forbidden family。例子包含 monolith import、runtime probe reference、`render_if_needed`、controller、renderer、`frame_rgba`、artifact writer、projection formula、mask formula、sampling formula movement、dataframe runtime、live source、cache/database IO、source-loss interpretation、transparent-globe leak inference、correctness claim、visual parity claim、readiness claim、transparent-globe leak fix claim。

## Planning answers

1. 現有 sampling visibility checker 不可直接重用，只能作為 pattern reference。
2. 需要 presentation count 專用 checker。
3. checker creation 不授權。
4. helper creation 不授權。
5. future checker 可沿用 AST-only 模式。
6. allowed string labels 可作為資料通過。
7. executable reference 必須 fail。
8. 下一張 gate 應該是 checker creation gate，而不是繼續 planning。

## Creation authorization decision

- `checker_creation_authorized = false`
- `helper_creation_authorized = false`
- `render_core_change_authorized = false`
- `existing_sampling_visibility_checker_change_authorized = false`
- `runtime_probe_change_authorized = false`
- `taichi_global_bathymetry_change_authorized = false`
- `render_if_needed_authorized = false`
- `controller_renderer_frame_buffer_authorized = false`
- `artifact_generation_authorized = false`
- `formula_movement_authorized = false`
- `source_loss_interpretation_authorized = false`
- `transparent_globe_leak_inference_authorized = false`
- `coordinate_correctness_claimed = false`
- `visual_parity_claimed = false`
- `readiness_claimed = false`
- `transparent_globe_leak_fix_claimed = false`
- `rrkal_wide_methodology_authorized = false`

## Recommended next gate

`dynamic_point_lod_view_frame_presentation_count_import_boundary_checker_gate`

## Boundary statement

Docs/test-only dynamic point LOD view-frame presentation count import-boundary checker planning gate. No checker creation, no helper creation, no render_core change, no existing sampling visibility checker change, no runtime probe change, no taichi_global_bathymetry change, no render_if_needed, no controller, no renderer, no frame buffer read, no artifact generation, no formula movement, no source-loss interpretation, no transparent-globe leak inference, no correctness/visual parity/readiness/leak-fix claim, no RRKAL-wide methodology promotion, and no push.

## Final classification

`c3_displaytools_dynamic_point_lod_view_frame_presentation_count_import_boundary_checker_planning_gate_committed_for_o1_review_no_push`