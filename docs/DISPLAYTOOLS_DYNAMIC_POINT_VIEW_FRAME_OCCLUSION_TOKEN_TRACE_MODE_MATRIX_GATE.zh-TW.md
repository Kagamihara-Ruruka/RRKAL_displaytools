# Dynamic Point View-Frame Occlusion Token-Trace Mode Matrix Gate

## Gate 類型

這張 gate 是 docs/test-only 的 dynamic point view-frame / LOD / occlusion token-trace mode matrix。它不做真正變數追蹤、不插 instrumentation、不使用 `sys.settrace`，也不執行 renderer 或 dynamic point runtime。

## 目的

本 gate 在 view-frame / LOD / occlusion 範圍內試點 `token_trace_mode`。目標是把 entrypoint、token、mode 組成矩陣，描述帶身份 token 預期可以流向哪裡，以及絕對不能污染哪些 boundary。

核心語意鏈如下：

```text
rotation / zoom
-> LOD policy
-> globe angle / view frame
-> projection shadow
-> occlusion policy
-> presentation
```

同時固定：dynamic point existence / computation 不等於 dynamic point visibility / presentation。點可以仍然被計算但被遮蔽；遮蔽不是 source filter；LOD 是 presentation/render policy，不是 provider lineage。

## A/B 方法論記錄

方案 A 是擴充既有 `trace_mode`。它可以作為低成本方法論備案，因為它只需要在既有 trace activation 上加註更多標籤。但本 gate 不採用 A 作為主要實作，因為 activation trace 無法清楚表示「哪一個身份 token」正在跨 boundary。

方案 B 是新增 `token_trace_mode`。本 gate 採用 B 作為 dynamic point view-frame / occlusion 的局部 pilot，因為 token trace 是帶身份的路徑顯影，比單純 trace activation 更精確。這不是全域 RRKAL 方法論升級，也不授權其他 subsystem 直接套用。

## Entrypoints

- `zoom_entry`
- `rotation_entry`
- `lod_policy_entry`
- `globe_angle_frame_entry`
- `projection_shadow_entry`
- `point_payload_entry`
- `occlusion_policy_entry`
- `presentation_policy_entry`
- `source_lineage_entry`

## Tokens

- `zoom_token`
- `rotation_token`
- `lod_token`
- `globe_angle_token`
- `projection_policy_ref_token`
- `point_id_token`
- `coordinate_payload_token`
- `occlusion_visibility_token`
- `presentation_visibility_token`
- `source_lineage_token`

## Modes

- `null_mode`
- `tripwire_mode`
- `trace_mode`
- `substitute_mode`
- `token_trace_mode`

## Matrix shape

測試 fixture 產生完整 Cartesian matrix：

```text
entrypoint x token x mode -> expected_path / forbidden_path / classification
```

每一列都必須保留：

- `entrypoint`
- `token`
- `mode`
- `expected_path`
- `forbidden_path`
- `classification`
- `runtime_probe_needed`
- `source_lineage_pollution_allowed`
- `coordinate_correctness_claimed`
- `visual_correctness_claimed`

所有列的 `source_lineage_pollution_allowed`、`coordinate_correctness_claimed`、`visual_correctness_claimed` 都必須是 false。

## Token trace expectation summary

- `zoom_token` 可以流向 `lod_policy` 與 `view_frame_label`，不得流向 `source_lineage`。
- `rotation_token` 可以流向 `globe_angle_frame` 與 `occlusion_decision_label`，不得流向 provider、cache、database。
- `lod_token` 可以流向 sampling / presentation labels，不得變成 source filter。
- `globe_angle_token` 可以流向 occlusion labels，不得宣稱 coordinate correctness。
- `projection_policy_ref_token` 只能是 label/reference/ledger，不得成為 formula call。
- `point_id_token` 必須保持 source lineage identity，不得因 hidden 被改成 missing。
- `coordinate_payload_token` 可被標記為 computed / hidden uncertainty，不得宣稱 projection correctness。
- `occlusion_visibility_token` 可以影響 visibility label，不得改 source lineage。
- `presentation_visibility_token` 可以影響 rendered visibility label，不得改 provider data。
- `source_lineage_token` 不應被 LOD / occlusion / presentation token 污染。

## Source-lineage pollution guard

本 gate 明確固定：LOD、occlusion、presentation token 都不能污染 source lineage。hidden point 不能被改寫成 missing point；rendered visibility 不能回寫 provider、cache、database；source lineage token 必須保持 provider lineage guard。

## Runtime probe status

`runtime_probe_candidate = true`，因為 token trace matrix 指出未來可以被 runtime characterization 觀測的路徑。但 `runtime_probe_authorized = false`，本 gate 不授權 runtime probe、不插 instrumentation、不執行 renderer，也不宣稱 transparent-globe leak 已修復。

## Decision output

- `token_trace_mode_pilot_gate_passed = true`
- `token_trace_mode_local_pilot = true`
- `token_trace_mode_global_methodology_authorized = false`
- `trace_mode_expansion_option_recorded = true`
- `runtime_probe_candidate = true`
- `runtime_probe_authorized = false`
- `instrumentation_authorized = false`
- `helper_module_creation_authorized = false`
- `source_movement_authorized = false`
- `formula_movement_authorized = false`
- `renderer_runtime_authorized = false`
- `coordinate_correctness_claimed = false`
- `visual_correctness_claimed = false`
- `performance_claimed = false`
- `transparent_globe_leak_fix_claimed = false`
- `recommended_next_gate = dynamic_point_lod_view_frame_runtime_characterization_planning_gate`

## Evidence limits

本 gate 只使用既有 docs/test gate 與靜態掃描作為 evidence。它不讀取、複製、移動或改寫 projection / flip / mask formula；不執行 dynamic point runtime；不執行 renderer / Qt / VisPy / Taichi；不讀 real AIS / ADS-B / cache / database。

## Boundary statement

Docs/test-only dynamic point view-frame occlusion token-trace mode matrix gate. No helper module creation, no source movement, no production source change, no checker script change, no generic checker trust-level change, no generic checker blocking behavior change, no generic profile change, no monolith import, no runtime execution, no instrumentation, no `sys.settrace`, no debugger/IDE automation, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula read/copy/movement/change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no coordinate/visual correctness claim, no performance claim, no transparent-globe leak fix claim, no runtime probe authorization, no token-trace global methodology authorization, no runtime merge enablement, and no readiness/visual parity/bug-fix/safe-to-extract claim.
