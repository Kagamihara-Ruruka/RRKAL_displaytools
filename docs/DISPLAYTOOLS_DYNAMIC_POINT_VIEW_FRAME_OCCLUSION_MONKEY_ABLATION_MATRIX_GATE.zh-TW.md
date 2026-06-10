# Dynamic Point View-Frame Occlusion Monkey Ablation Matrix Gate

## Gate 目的

本 gate 建立 dynamic point view-frame、LOD、occlusion 的 docs/test-only 猴子消融矩陣。它只畫清楚 rotation、zoom、LOD、globe angle、projection shadow、occlusion、presentation、source lineage 之間的因果邊界，為後續 runtime characterization probe 做準備。

本 gate 不執行 renderer，不執行 dynamic point runtime，不建立 helper，不修改 checker，不讀取或搬移 projection、flip、mask formula。

## 語意鏈

```text
rotation / zoom
-> LOD policy
-> globe angle / view frame
-> projection shadow
-> occlusion policy
-> presentation
```

核心邊界：

```text
dynamic point existence / computation
!=
dynamic point visibility / presentation
```

也就是：

- 點可以仍然被計算，但被遮蔽。
- 遮蔽不是 source filter。
- LOD 是 presentation/render policy，不是 provider lineage。
- rotation/zoom 改變的是 view-frame state，不是資料來源。
- globe angle 是 visibility/occlusion 的上游語意，不是 dynamic point provider 本身。

## Matrix pins

- `zoom_state_pin`
- `rotation_state_pin`
- `lod_policy_pin`
- `globe_angle_frame_pin`
- `projection_shadow_pin`
- `occlusion_policy_pin`
- `presentation_policy_pin`
- `source_lineage_integrity_pin`
- `computed_but_hidden_point_pin`
- `transparent_globe_leak_fault_pin`

每個 pin 覆蓋：

- `null_mode`
- `tripwire_mode`
- `trace_mode`
- `substitute_mode`

## Causal expectations

- `zoom_state_pin` 可影響 `lod_policy`。
- `rotation_state_pin` 可影響 `globe_angle_frame`。
- `lod_policy_pin` 可影響 presentation load / sampling label。
- `globe_angle_frame_pin` 可影響 occlusion decision。
- `projection_shadow_pin` 只允許 label/reference/ledger，不允許公式。
- `occlusion_policy_pin` 可影響 visibility，不可改 source lineage。
- `presentation_policy_pin` 可影響 rendered visibility，不可改 provider/cache/database。
- `source_lineage_integrity_pin` 不應被 LOD/occlusion mutation 改變。
- `computed_but_hidden_point_pin` 必須保留點存在但不可見的語意。
- `transparent_globe_leak_fault_pin` 必須記錄背面點穿透地球作為 fault，不宣稱已修復。

## Computed-but-hidden conclusion

`computed_but_hidden_point_pin` 固定以下判斷：dynamic point 的存在與計算，不等於它在目前 view-frame 中必須可見。若 occlusion 或 presentation 隱藏點，不可把它重新分類為 source missing、provider filtered 或 lineage lost。

## Transparent globe leak fault status

`transparent_globe_leak_fault_pin` 只記錄 transparent-globe leak risk。此 gate 不宣稱背面點遮蔽已修復，不宣稱 visual correctness，也不執行 renderer 驗證。

## Classification output

```text
matrix_gate_passed = true
view_frame_occlusion_planning_candidate = true
runtime_probe_candidate = true
runtime_probe_authorized = false
helper_module_creation_authorized = false
source_movement_authorized = false
formula_movement_authorized = false
renderer_runtime_authorized = false
coordinate_correctness_claimed = false
visual_correctness_claimed = false
performance_claimed = false
readiness_claimed = false
recommended_next_gate = dynamic_point_view_frame_occlusion_core_lineage_validation_gate
```

## 下一步

建議下一張做 `dynamic_point_view_frame_occlusion_core_lineage_validation_gate`。它應先驗證 view-frame / occlusion 是否真屬 core lineage interface，而不是直接啟動 runtime probe。

## Boundary statement

Docs/test-only dynamic point view-frame occlusion monkey ablation matrix gate. No helper module creation, no source movement, no production source change, no checker script change, no generic checker trust-level change, no generic checker blocking behavior change, no generic profile change, no monolith import, no runtime execution, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula read/copy/movement/change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no coordinate/visual correctness claim, no performance claim, no transparent-globe leak fix claim, no runtime probe authorization, no runtime merge enablement, and no readiness/visual parity/bug-fix/safe-to-extract claim.
