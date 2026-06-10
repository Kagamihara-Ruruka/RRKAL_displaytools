# Dynamic Point Projection Interface Shadow Import-Boundary Checker Gate

## Gate 目的

本 gate 建立 `dynamic_point_projection_interface_shadow` 專用 AST-only import-boundary checker。目標是保護未來的 `render_core\dynamic_point_projection_interface_shadow_boundary.py`，避免 shadow interface helper 偷帶 projection、flip、mask、renderer frame、hot path 或 correctness claim。

本 gate 只做 tooling/docs/test。它不建立 helper target，不修改 `render_core`，不修改 monolith，不移動 source，不修改 generic checker 或 profile。

## Anchors

- base camp rollback anchor: `ad38dbe`
- projection shadow source: `6289c60`
- planning source: `a72d141`
- creation-order counterexample source: `53afb98`

## Checker behavior

- Static AST-only。
- 不 import target。
- 不 execute target。
- 預設 target: `render_core\dynamic_point_projection_interface_shadow_boundary.py`。
- target missing 時 PASS。
- syntax error 時輸出 JSON 並 fail。
- 支援 `--self-test-negative`。
- 檢查 `ast.Import`、`ast.ImportFrom`、`ast.Name`、`ast.Attribute`、`ast.Call`、`ast.FunctionDef`、`ast.AsyncFunctionDef`、`ast.ClassDef`。
- 字串標籤作為 data 時允許；同樣 vocabulary 作為 import、name、attribute、call 或 declaration 時阻斷。

## Missing candidate behavior

```json
{
  "candidate_exists": false,
  "status": "not_applicable_candidate_missing",
  "boundary_passed": true,
  "violations": []
}
```

## Forbidden family coverage

Checker 覆蓋下列 forbidden family：

- `monolith`
- `projection_formula`
- `longitude_flip_formula`
- `latitude_flip_formula`
- `mask_formula`
- `renderer_frame_transform`
- `runtime_renderer_host`
- `dynamic_point_screen_projection_execution`
- `hot_path_alpha_apply_composition`
- `controller_selection`
- `dataframe_runtime`
- `live_source`
- `artifact_metadata`
- `coordinate_correctness_claim`
- `visual_correctness_claim`

## Allowed string-label distinction

下列 label 可作為字串資料存在：

- `source_coordinate_space`
- `target_coordinate_space`
- `projection_policy_ref`
- `flip_policy_ref`
- `mask_policy_ref`
- `frame_sync_ref`
- `consumer_surface`
- `uncertainty_label`
- `evidence_refs`
- `formula_behavior_not_executed`
- `coordinate_correctness_not_claimed`
- `visual_correctness_not_claimed`
- `core_interface_only`
- `shadow_contract`
- `stop_condition_ledger`

若上述內容以 executable reference 形式出現，checker 會依 forbidden family 阻斷。這保留 shadow contract 的 label-only 能力，但不允許 formula、runtime、correctness 或 renderer coupling 進入 helper。

## Negative self-test

`--self-test-negative` 會檢查每個 forbidden family 都能被擋下，並同時確認 allowed string labels 作為資料時仍可 PASS。輸出包含：

```json
{
  "negative_self_test_passed": true,
  "all_forbidden_snippets_detected": true
}
```

## Generic checker status

Generic JSON profile checker 不變：

- trust level 仍是 `L1_shadow`
- blocking 仍是 `false`
- replacement 未授權
- profile 未修改

本 gate 不替代 generic checker，也不讓 generic checker 成為正式 hard gate。

## 為什麼這不是 helper extraction

`projection_flip_mask_sync` 是 core-interface-only surface。此 checker 只建立入口安檢門，不建立 `dynamic_point_projection_interface_shadow_boundary.py`，也不讀取、複製、移動或改寫 projection、flip、mask formula。未來若建立 shadow helper，也只能承載 label/reference/ledger，不可宣稱 coordinate correctness 或 visual correctness。

## Boundary statement

Tooling/docs-only dynamic point projection interface shadow import-boundary checker gate. No helper module creation, no source movement, no production helper target creation, no generic checker trust-level change, no generic checker blocking behavior change, no generic profile change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula read/copy/movement/change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no cross-organ integration implementation, no coordinate/visual correctness claim, no runtime merge enablement, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim.
