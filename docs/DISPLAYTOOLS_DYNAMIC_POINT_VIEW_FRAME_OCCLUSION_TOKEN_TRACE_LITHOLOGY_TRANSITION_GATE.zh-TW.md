# Dynamic Point View-Frame Occlusion Token-Trace Lithology Transition Gate

## Gate 類型

這張 gate 是 docs/test-only 的 token-trace lithology transition 判讀層。它承接 `373da1e` 的 dynamic point view-frame occlusion `token_trace_mode` local pilot，但不修改既有 token trace matrix、不跑 runtime、不插 instrumentation，也不建立 helper。

## 目的

上一張 gate 描述 token 從 entrypoint 進入後預期走到哪裡。這張 gate 增加岩性轉化判讀，把路徑翻成三個靜態欄位：

```text
expected_path
-> lithology_sequence
-> lithology_transition
-> semantic_age_inference
```

這讓 c_3 可以判斷訊號是仍在地核語意內流動、從地核進入安山岩橋、從安山岩進入 presentation，或出現 presentation 反向污染 source lineage 的禁止路徑。

## Prior gate inputs

本 gate 固定承接下列 `373da1e` 結論：

- `token_trace_mode_local_pilot = true`
- `token_trace_mode_global_methodology_authorized = false`
- `runtime_probe_candidate = true`
- `runtime_probe_authorized = false`
- `instrumentation_authorized = false`
- `source_lineage_pollution_allowed = false`

## Lithology labels

- `core_lineage`
- `core_interface_only`
- `andesite_bridge`
- `presentation_policy`
- `source_lineage_guard`
- `computed_but_hidden`
- `unresolved_static_fault`
- `forbidden_pollution`
- `not_enough_evidence`

## Lithology transitions

- `core_lineage_to_core_lineage`
- `core_lineage_to_core_interface`
- `core_lineage_to_andesite_bridge`
- `andesite_to_presentation_policy`
- `presentation_to_source_lineage_forbidden`
- `payload_to_core_formula_forbidden`
- `source_lineage_preserved`
- `computed_to_hidden_visibility`
- `fault_remains_unresolved`
- `not_enough_evidence`

## Semantic age inference labels

- `deep_core_semantics`
- `core_interface_semantics`
- `older_bridge_semantics`
- `presentation_surface_semantics`
- `source_lineage_identity_preserved`
- `visibility_not_existence_semantics`
- `forbidden_reverse_pollution`
- `unresolved_fault_semantics`
- `not_enough_evidence`

## Transition rules

`core_lineage_to_core_lineage` 表示訊號大概率在核心法則內部流動，後續策略應偏向 shadow/interface，不是普通 helper extraction。

`core_lineage_to_core_interface` 表示訊號碰到公式或 frame interface，禁止公式移動，只允許 reference/ledger。

`core_lineage_to_andesite_bridge` 表示地核語意流向較老的橋接層，該層可能適合語義重建，不宜直接移植舊 code。

`andesite_to_presentation_policy` 表示橋接層把核心視框語意轉為顯示策略，後續可考慮重建 presentation contract。

`presentation_to_source_lineage_forbidden` 表示 presentation 若反向污染 source lineage，必須立即停在 forbidden path。

`source_lineage_preserved` 表示 source identity 被保持，符合 hidden is not missing。

`computed_to_hidden_visibility` 表示點存在但不可見，不能改成 missing source。

`fault_remains_unresolved` 表示 transparent globe leak 等 fault 仍未解決，不得宣稱修復。

## Matrix rows covered

本 gate 至少覆蓋下列 token/entrypoint 組合：

- `zoom_entry x zoom_token`
- `rotation_entry x rotation_token`
- `lod_policy_entry x lod_token`
- `globe_angle_frame_entry x globe_angle_token`
- `projection_shadow_entry x projection_policy_ref_token`
- `point_payload_entry x point_id_token`
- `point_payload_entry x coordinate_payload_token`
- `occlusion_policy_entry x occlusion_visibility_token`
- `presentation_policy_entry x presentation_visibility_token`
- `source_lineage_entry x source_lineage_token`

另外保留兩個 stop-line rows：`payload_to_core_formula_forbidden` 與 `fault_remains_unresolved`，用來確保 payload 不反向碰公式，transparent globe leak 仍是 unresolved static fault。

## Semantic seismic tomography status

本 gate 可以把 `semantic_seismic_tomography` 標為 dynamic point 內部的 local pattern candidate，因為它只是在 token trace path 上加一層岩性判讀。它不能升為全域 RRKAL 方法論，也不能授權 runtime probe、source movement、helper creation 或 formula movement。

## Decision output

- `lithology_transition_gate_passed = true`
- `token_trace_mode_local_pilot = true`
- `token_trace_mode_global_methodology_authorized = false`
- `semantic_seismic_tomography_local_pattern_candidate = true`
- `semantic_seismic_tomography_global_methodology_authorized = false`
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

本 gate 只使用既有 docs/test gate 與靜態掃描。它不讀取、複製、移動或改寫 projection / flip / mask formula；不執行 dynamic point runtime；不執行 renderer / Qt / VisPy / Taichi；不讀 real AIS / ADS-B / cache / database；不宣稱 coordinate correctness 或 visual correctness。

## Boundary statement

Docs/test-only dynamic point view-frame occlusion token-trace lithology transition gate. No helper module creation, no source movement, no production source change, no existing token trace matrix change, no checker script change, no generic checker trust-level change, no generic checker blocking behavior change, no generic profile change, no monolith import, no runtime execution, no instrumentation, no `sys.settrace`, no debugger/IDE automation, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula read/copy/movement/change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no coordinate/visual correctness claim, no performance claim, no transparent-globe leak fix claim, no runtime probe authorization, no token-trace global methodology authorization, no semantic-seismic-tomography global methodology authorization, no runtime merge enablement, and no readiness/visual parity/bug-fix/safe-to-extract claim.
