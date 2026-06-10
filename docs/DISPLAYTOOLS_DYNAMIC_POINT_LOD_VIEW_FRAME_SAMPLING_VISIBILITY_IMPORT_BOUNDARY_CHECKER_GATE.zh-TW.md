# Dynamic Point LOD View-frame Sampling Visibility Import-Boundary Checker Gate

## Gate 性質

本 gate 建立 sampling / visibility adapter extraction 的專用 AST import-boundary checker。目標是先替未來 helper 入口加上靜態邊界，避免 helper 把 projection formula、renderer runtime、frame buffer、artifact writer、controller 或 `render_if_needed` 帶進 sampling / visibility 安山岩橋接層。

本 gate 只建立 tooling / test / docs。它不建立 helper module，不建立 `render_core/dynamic_point_sampling_visibility_boundary.py`，不修改 production source，不修改 runtime probe，不執行 runtime。

## Default future target

Checker 預設目標為：

```text
render_core/dynamic_point_sampling_visibility_boundary.py
```

該目標目前可以不存在。目標不存在時，checker 必須回傳 not applicable PASS，而不是阻塞後續 docs/test gate。

## Checker behavior

Checker 行為固定如下：

- AST-only。
- 不 import target。
- 不 execute target。
- missing target PASS。
- syntax error JSON fail 且 nonzero exit。
- 檢查 `ast.Import`。
- 檢查 `ast.ImportFrom`。
- 檢查 `ast.Name`。
- 檢查 `ast.Attribute`。
- 檢查 `ast.Call`。
- 檢查 `ast.FunctionDef`。
- 檢查 `ast.AsyncFunctionDef`。
- 檢查 `ast.ClassDef`。

Missing target 的預期 JSON 行為：

```json
{
  "candidate_exists": false,
  "status": "not_applicable_candidate_missing",
  "boundary_passed": true,
  "violations": []
}
```

## Forbidden family coverage

Checker 至少覆蓋下列 forbidden family：

- `monolith`
- `projection_formula`
- `mask_formula`
- `sampling_formula_movement`
- `renderer_runtime`
- `frame_buffer`
- `controller_runtime`
- `render_if_needed`
- `artifact_writer`
- `live_source`
- `cache_database_io`
- `dataframe_runtime`
- `runtime_probe`
- `correctness_claim`
- `readiness_claim`
- `transparent_globe_leak_fix_claim`

這些 family 對應的是可執行引用、runtime surface、artifact surface 或 claim drift，不是單純文字資料。

## Forbidden executable references

Negative self-test 必須能偵測下列型態：

- `import taichi_global_bathymetry`
- `from taichi_global_bathymetry import render_if_needed`
- `project_ais_to_screen(...)`
- `project_aircraft_to_screen(...)`
- `mask_overlay_to_globe(...)`
- `alpha_compose(...)`
- `frame_rgba`
- `Image.fromarray(...)`
- `.save(...)`
- `write_preview_frame_png(...)`
- `HybridRenderController`
- `TaichiGlobeRenderer`
- `renderer.render(...)`
- `pd.DataFrame(...)`
- `np.asarray(...)`
- `read_url_text(...)`
- `AISSource`
- `AircraftSource`
- `coordinate_correctness_claimed`
- `visual_correctness_claimed`
- `readiness_claimed`
- `transparent_globe_leak_fix_claimed`

## Allowed string-label distinction

下列文字若只作為資料字串，可以通過：

- `sampled_visible_token`
- `visible_count_observation`
- `rendered_count_observation`
- `mask_visible_token`
- `source_lineage_integrity_token`
- `frame_visible_not_observed`
- `sampling_or_presentation_reduction_candidate`
- `globe_mask_responsibility_candidate`
- `source_lineage_guard`
- `frame_visibility_stop_line`
- `transparent_globe_leak_not_inferred`

此區分很重要：本 gate 阻斷的是可執行引用與越界宣稱，不阻斷 descriptor / contract 需要保存的 label 資料。

## Allowed future helper surface

乾淨 candidate 可以定義下列 descriptor / contract function name：

- `build_dynamic_point_sampling_visibility_observation_descriptor`
- `build_dynamic_point_visibility_count_contract_descriptor`
- `build_dynamic_point_mask_visibility_contract_descriptor`
- `build_dynamic_point_sampling_reduction_contract_descriptor`
- `build_dynamic_point_frame_visibility_stop_line_descriptor`
- `dynamic_point_sampling_visibility_boundary_descriptor`
- `dynamic_point_sampling_visibility_planning_bundle`

這些 name 僅代表未來 helper 的 label / contract / descriptor surface，不授權 helper creation，不授權 formula movement，不授權 runtime merge。

## Expected checker result

- Missing target returns PASS as not applicable。
- Clean synthetic candidate returns PASS。
- Forbidden import returns FAIL。
- Forbidden name returns FAIL。
- Forbidden attribute returns FAIL。
- Forbidden call returns FAIL。
- Forbidden function / class declaration returns FAIL。
- Syntax error returns JSON FAIL。
- Allowed string labels return PASS。
- Negative self-test detects all forbidden families。
- Checker default target is correct。
- Checker does not import target。

## Boundary statement

Tooling/test/docs-only dynamic point LOD view-frame sampling / visibility import-boundary checker gate. No helper creation, no production source change, no runtime probe change, no runtime execution, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no formula movement, no correctness/readiness/leak-fix claim, no generic checker trust-level change, and no push.

## Recommended next gate

```text
dynamic_point_lod_view_frame_sampling_visibility_minimal_extraction_gate
```
