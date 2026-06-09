# Dynamic Point Projection Interface Shadow Gate

本文件是 docs/test-only projection interface shadow gate。它使用 dynamic point 內部已允許的 `L2_local_pattern` 岩性模型，將 `projection_flip_mask_sync` 導向 shadow/interface 設計，而不是 projection extraction。

本 gate 不搬 projection、flip、mask 公式，不讀取或執行 Taichi projection/render pipeline，不執行 renderer，也不建立 production interface。

## Anchor 與 local pattern source

- Base camp rollback anchor：`ad38dbe`
- Local pattern source：`60cded8`
- Target surface：`projection_flip_mask_sync`
- Current lithology：`core_interface_only`

`projection_flip_mask_sync` 被視為 `core_interface_only`，因為它連到 projection、flip、mask、renderer frame transform 與 dynamic point screen projection 的核心壓力區。這類 surface 不適合用 source movement 處理，只能先建立 shadow contract candidate。

## 為什麼這不是 projection extraction

Projection extraction 會要求搬移或重寫 projection、longitude flip、latitude flip、mask、renderer frame transform 或 dynamic point screen projection execution。這些行為都屬於 formula/runtime surface，本 gate 明確禁止。

Shadow contract 只定義未來 interface 可能需要哪些欄位，以及 consumer 應期待什麼 label/reference。它不連接真實 formula，也不驗證 coordinate correctness 或 visual correctness。

## Shadow contract candidate fields

候選欄位如下：

- `source_coordinate_space`：dynamic point 原始 lon/lat payload 的 label。
- `target_coordinate_space`：renderer screen 或 globe frame 的 label。
- `projection_policy_ref`：label-only projection policy reference。
- `flip_policy_ref`：label-only longitude/latitude flip policy reference。
- `mask_policy_ref`：label-only mask policy reference。
- `frame_sync_ref`：label-only frame sync reference。
- `consumer_surface`：dynamic point projection consumer descriptor。
- `uncertainty_label`：標示 formula behavior 未執行。
- `evidence_refs`：指向既有 lithology、semantic、correlation、static scan gate。

這些欄位只是 docs/test packet 欄位，不是 production schema，也不是 implementation authorization。

## Consumer expectations

- Dynamic point projection peer 只能期待 stable label reference，不可期待 callable projection formula。
- Dynamic point mask peer 只能期待 mask policy label，不可期待 mask formula 或 renderer buffer。
- Future shadow contract test 只能期待 deterministic dict/list/scalar 欄位，不可期待 runtime projection execution。

## Forbidden formula/runtime surfaces

- projection formula
- longitude flip formula
- latitude flip formula
- mask formula
- renderer frame transform
- Taichi / VisPy / Qt runtime execution
- dynamic point screen projection execution
- hot path alpha/apply/composition coupling

## Allowed label/reference surfaces

- label-only policy references
- static evidence refs
- interface field names
- uncertainty labels
- consumer expectation descriptors
- stop-condition ledger

## Interface invariants

- `projection_formula_moved = false`
- `flip_formula_moved = false`
- `mask_formula_moved = false`
- `renderer_runtime_invoked = false`
- `source_movement_authorized = false`
- `helper_module_creation_authorized = false`
- `runtime_merge_enabled = false`
- `generic_checker_blocking = false`
- `readiness_claimed = false`
- `shadow_contract_is_not_implementation_authorization = true`

## Evidence limits

- 靜態掃描只提供 dependency pressure evidence。
- Projection formula 未讀取、未搬移、未修改。
- Flip formula 未讀取、未搬移、未修改。
- Mask formula 未讀取、未搬移、未修改。
- Renderer runtime 未執行。
- Coordinate correctness 不宣稱。
- Visual correctness 不宣稱。

## 下一步建議

推薦下一張 gate：

`dynamic_point_projection_interface_shadow_import_boundary_planning_gate`

理由：若未來要把 shadow contract 推進到 helper 或 checker 階段，應先規劃 import-boundary 與 forbidden formula vocabulary，而不是直接建立 production interface。

## Explicit exclusions

- 不建立 helper module。
- 不移動 source。
- 不修改 production source。
- 不修改 checker script。
- 不升級 generic checker trust level。
- 不讓 generic checker 變成 blocking。
- 不新增或修改 generic profile。
- 不 import monolith。
- 不執行 SQL、WebSocket、live-source。
- 不讀 real AIS、ADS-B、cache、database。
- 不引入 pandas、datashader、numpy runtime。
- 不搬移或修改 projection、flip、mask formula。
- 不執行 renderer、Qt、VisPy、Taichi runtime。
- 不修改 controller selection、picker、hit-test。
- 不修改 metadata/output schema。
- 不實作 cross-organ integration。
- 不啟用 runtime merge。
- 不宣稱 coordinate correctness。
- 不宣稱 visual correctness。
- 不宣稱 readiness、performance、visual parity、bug-fix、safe-to-extract。

## Boundary statement

Docs/test-only dynamic point projection interface shadow gate. No helper module creation, no source movement, no production source change, no checker script change, no generic checker trust-level change, no generic checker blocking behavior change, no generic profile change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula movement or change, no renderer/Qt/VisPy/Taichi runtime execution, no controller selection/picker/hit-test mutation, no metadata/output schema change, no cross-organ integration implementation, no runtime merge enablement, no coordinate/visual correctness claim, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim.
