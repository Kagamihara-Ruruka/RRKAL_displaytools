# Generic Import Boundary JSON Profile Shadow Checker Pilot Gate

## Gate summary

本 gate 建立第一版 JSON profile 驅動的 generic import-boundary checker。這個 checker 僅用於 L1 shadow validation，不替代任何手寫 checker，不作為正式阻塞 gate，不宣稱 profile 是產品 schema 或 runtime config。

## Scope

- 新增 generic AST-only checker：`scripts/validate_displaytools_import_boundary_from_profile.py`
- 新增 JSON profile fixture：`tests/fixtures/import_boundary_profiles/dynamic_point_payload_coordinate_quality.profile.json`
- 新增 shadow parity tests：`tests/test_displaytools_generic_import_boundary_profile.py`
- 以 `render_core/dynamic_point_payload_coordinate_quality_boundary.py` 作為 shadow pilot target。
- 既有手寫 checker 仍是 source of truth。

## Generic checker behavior

Generic checker 只做靜態 AST parsing：

- 讀取 JSON profile。
- 不 import target。
- 不 execute target。
- 支援 missing candidate JSON PASS。
- 支援 syntax error JSON nonzero。
- 支援 profile negative self-test snippets。
- 區分 allowed string labels 與 executable forbidden references。
- 檢查 `Import`、`ImportFrom`、`Name`、`Attribute`、`Call`、`FunctionDef`、`AsyncFunctionDef`、`ClassDef`。

## JSON profile summary

Profile capability：

```text
capability = dynamic_point_payload_coordinate_quality
target = render_core/dynamic_point_payload_coordinate_quality_boundary.py
trust_level = L1_shadow
blocking = false
handwritten_checker_is_source_of_truth = true
replacement_authorized = false
runtime_render_invoked = false
runtime_merge_enabled = false
readiness_claimed = false
```

Profile 內容從既有手寫 checker 的 allowed labels、forbidden families、negative snippets 派生，用於 parity 實驗，不用於替代手寫 checker。

## Parity result

Shadow pilot 固定以下 parity：

- generic checker on candidate target：PASS
- handwritten checker on same target：PASS
- generic checker negative self-test：PASS
- handwritten checker negative self-test：PASS
- generic missing target behavior：`not_applicable_candidate_missing` 且 PASS
- allowed string labels 作為資料時 PASS
- import/name/attribute/call/declaration executable reference 命中 forbidden families 時 FAIL

## Forbidden family coverage

Profile 覆蓋：

- monolith
- live source
- cache/database IO
- runtime dataframe
- projection formula
- controller selection
- renderer host
- hot path
- artifact metadata

## Decision output

```text
generic_profile_shadow_checker_pilot_passed = true
trust_level = L1_shadow
blocking = false
handwritten_checker_is_source_of_truth = true
replacement_authorized = false
runtime_render_invoked = false
runtime_merge_enabled = false
readiness_claimed = false
recommended_next_gate = generic_import_boundary_profile_second_shadow_target_gate
```

## Explicit exclusions

本 gate 不修改既有手寫 checker，不替代任何 checker，不刪除 checker script，不修改 `render_core/*.py`，不修改 `taichi_global_bathymetry.py`，不新增 production helper，不移動 source，不讓 generic checker 成為 hard gate，不把 JSON profile 宣稱為產品 schema 或 runtime config。

## Boundary statement

Tooling/docs-only generic import-boundary JSON profile shadow checker pilot. L1 shadow only, non-blocking, handwritten checker remains source of truth, no replacement authorization, no production helper creation, no source movement, no existing checker removal or behavior replacement, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix/safe-to-extract claim.
