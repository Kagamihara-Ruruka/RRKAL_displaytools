# Dynamic Point Projection Interface Shadow Import-Boundary Planning Gate

本文件是 docs/test-only import-boundary planning gate。它只規劃未來 dynamic point projection interface shadow helper 的安檢門，不建立 checker script，不建立 helper module，也不移動 source。

## Anchor

- Base camp rollback anchor：`ad38dbe`
- Local pattern source：`60cded8`
- Shadow source：`6289c60`

## Future target and checker names

- Future helper target：`render_core\dynamic_point_projection_interface_shadow_boundary.py`
- Future checker script：`scripts\validate_displaytools_dynamic_point_projection_interface_shadow_import_boundary.py`

這兩個只是 future path。此 slice 不建立任何一個檔案。

## 為什麼這不是 checker implementation

Checker implementation 會建立 script、CLI 行為、JSON schema 與 negative self-test。這張 gate 只先固定 vocabulary 與預期行為，避免下一張 checker gate 漏掉 projection、flip、mask、renderer runtime 或 coordinate correctness claim。

## Forbidden vocabulary

未來 checker 至少必須阻擋下列 family：

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

這些 family 代表公式、runtime、hot path、schema 或 correctness claim，不能出現在 shadow helper 的 executable references、imports、calls 或 declarations 中。

## Allowed string-label and data distinction

下列字串允許作為資料 label：

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

允許的資料面只限：

- label-only policy refs
- static evidence refs
- interface field names
- uncertainty labels
- consumer expectation descriptors
- stop-condition ledger
- no callable formula refs
- no renderer buffer refs

若同樣語彙以 import、name、attribute、call、function/class declaration 形式出現，未來 checker 應依 forbidden family 判斷。

## Planned AST coverage

未來 checker 至少應檢查：

- `ast.Import`
- `ast.ImportFrom`
- `ast.Name`
- `ast.Attribute`
- `ast.Call`
- `ast.FunctionDef`
- `ast.AsyncFunctionDef`
- `ast.ClassDef`

## Missing target behavior

未來 helper target 缺席時，checker 應輸出 JSON 並 PASS：

- `candidate_exists = false`
- `status = not_applicable_candidate_missing`
- `boundary_passed = true`
- `exit_code = 0`

## Negative self-test expectation

未來 checker 必須有 negative self-test，且要覆蓋所有 forbidden families。這是為了避免 shadow helper 偷帶公式、renderer runtime、controller runtime、dataframe runtime、metadata writer 或 correctness claim。

## Generic checker status

Generic checker 仍維持：

- `trust_level = L1_shadow`
- `blocking = false`
- `replacement_authorized = false`
- `profile_change_authorized = false`

本 gate 不修改 generic checker，不新增 profile，不提升 generic checker 權限。

## 為什麼 projection/flip/mask formula 不可出現在 helper

`projection_flip_mask_sync` 仍是 `core_interface_only` surface。Shadow helper 的職責只能是 label/reference/ledger，不是公式。若 helper 含 projection、longitude flip、latitude flip、mask 或 screen projection execution，就會從 interface shadow 變成公式移植，違反本系列 gate 的核心邊界。

## Decision output

- `planning_gate_passed = true`
- `checker_creation_authorized = false`
- `helper_creation_authorized = false`
- `source_movement_authorized = false`
- `formula_movement_authorized = false`
- `generic_checker_blocking = false`
- `generic_checker_replacement_authorized = false`
- `runtime_merge_enabled = false`
- `coordinate_correctness_claimed = false`
- `visual_correctness_claimed = false`
- `readiness_claimed = false`
- `recommended_next_gate = dynamic_point_projection_interface_shadow_import_boundary_checker_gate`

## 下一步建議

推薦下一張 gate：

`dynamic_point_projection_interface_shadow_import_boundary_checker_gate`

下一張若執行，才可建立 checker script；本張只完成 planning。

## Boundary statement

Docs/test-only dynamic point projection interface shadow import-boundary planning gate. No helper module creation, no source movement, no production source change, no checker script creation, no checker script change, no generic checker trust-level change, no generic checker blocking behavior change, no generic profile change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula read/copy/movement/change, no renderer/Qt/VisPy/Taichi runtime execution, no controller selection/picker/hit-test mutation, no metadata/output schema change, no cross-organ integration implementation, no runtime merge enablement, no coordinate/visual correctness claim, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim.
