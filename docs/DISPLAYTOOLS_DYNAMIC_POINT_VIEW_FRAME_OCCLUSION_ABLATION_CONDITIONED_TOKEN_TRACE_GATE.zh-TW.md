# Dynamic Point View-Frame Occlusion Ablation-Conditioned Token-Trace Gate

## Gate 類型

這張 gate 是 docs/test-only 的 ablation-conditioned token-trace fixture。它承接 view-frame occlusion monkey matrix、token trace matrix 與 lithology transition gate，但不修改既有 monkey、token、lithology gate，不跑 runtime、不插 instrumentation，也不建立 helper。

## 目的

本 gate 描述特定 pin 被猴子消融遮斷後，token path 會如何改變，是否被 containment 擋住，是否暴露 forbidden pollution，以及岩性轉化是否仍符合預期。

矩陣形狀如下：

```text
pin x ablation_mode x entrypoint x token
-> token_path_after_ablation
-> path_delta
-> lithology_transition_delta
-> containment_or_failure
```

## Pins covered

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

## Ablation modes

- `null_mode`
- `tripwire_mode`
- `trace_mode`
- `substitute_mode`
- `token_trace_mode`

## Entrypoint and token scenarios

- `zoom_state_pin x zoom_entry x zoom_token`
- `rotation_state_pin x rotation_entry x rotation_token`
- `lod_policy_pin x lod_policy_entry x lod_token`
- `globe_angle_frame_pin x globe_angle_frame_entry x globe_angle_token`
- `projection_shadow_pin x projection_shadow_entry x projection_policy_ref_token`
- `occlusion_policy_pin x point_payload_entry x point_id_token`
- `projection_shadow_pin x point_payload_entry x coordinate_payload_token`
- `occlusion_policy_pin x occlusion_policy_entry x occlusion_visibility_token`
- `presentation_policy_pin x presentation_policy_entry x presentation_visibility_token`
- `source_lineage_integrity_pin x source_lineage_entry x source_lineage_token`
- `transparent_globe_leak_fault_pin x presentation_policy_entry x presentation_visibility_token`

## Path delta summary

本 gate 支援 `path_preserved`、`path_blocked_by_tripwire`、`path_rerouted_to_containment`、`path_degraded_to_presentation_only`、`path_kept_source_lineage_stable`、`path_exposes_forbidden_formula_pressure`、`path_exposes_forbidden_source_lineage_pollution`、`path_requires_runtime_characterization`、`not_enough_evidence`。

重點判讀如下：

- 遮斷 `zoom_state_pin` 後，`zoom_token` 不應污染 `source_lineage`。
- 遮斷 `rotation_state_pin` 後，`rotation_token` 不應改 provider、cache、database。
- 遮斷 `lod_policy_pin` 後，`lod_token` 可退化為 presentation-only，不可變成 source filter。
- 遮斷 `globe_angle_frame_pin` 後，occlusion path 應變成 runtime characterization candidate，而不是 correctness claim。
- 遮斷 `projection_shadow_pin` 後，formula path 必須被 containment 或 forbidden pressure 標記。

## Lithology transition delta summary

本 gate 支援 `core_lineage_preserved`、`core_interface_contained`、`core_to_andesite_bridge_preserved`、`andesite_to_presentation_preserved`、`presentation_pollution_blocked`、`source_lineage_preserved`、`computed_hidden_semantics_preserved`、`unresolved_fault_preserved`、`forbidden_transition_exposed`、`runtime_characterization_needed`、`not_enough_evidence`。

這些 delta 只作為靜態判讀，不是 runtime observation，也不是 extraction authorization。

## Containment and failure summary

本 gate 支援 `contained_by_shadow_interface`、`contained_by_source_lineage_guard`、`contained_by_presentation_policy`、`contained_by_tripwire`、`requires_runtime_characterization`、`forbidden_formula_path_detected`、`forbidden_source_lineage_pollution_detected`、`unresolved_static_fault`、`not_enough_evidence`。

`projection_shadow_pin` 被遮斷時，coordinate payload 若暴露 formula pressure，必須被標成 `forbidden_formula_path_detected`。`presentation_policy_pin` 被遮斷時，presentation 若反向碰 source lineage，必須被標成 `forbidden_source_lineage_pollution_detected`。

## Source-lineage pollution guard

source lineage pollution 一律不允許。`point_id_token` 在 occlusion policy 被遮斷後仍必須保持 source lineage identity。presentation、LOD、occlusion 都不能把 hidden point 改寫成 missing source。

## Transparent globe leak fault status

`transparent_globe_leak_fault_pin` 被遮斷後仍是 unresolved static fault。本 gate 不宣稱已修復，不宣稱 visual correctness，也不授權 runtime probe。

## Decision output

- `ablation_conditioned_token_trace_gate_passed = true`
- `semantic_seismic_tomography_local_pattern_candidate = true`
- `semantic_seismic_tomography_global_methodology_authorized = false`
- `token_trace_mode_local_pilot = true`
- `token_trace_mode_global_methodology_authorized = false`
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
- `recommended_next_gate = dynamic_point_view_frame_occlusion_structure_settlement_gate`

## Evidence limits

本 gate 只使用既有 docs/test gate 與靜態掃描。它不讀取、複製、移動或改寫 projection / flip / mask formula；不執行 dynamic point runtime；不執行 renderer / Qt / VisPy / Taichi；不讀 real AIS / ADS-B / cache / database；不宣稱 coordinate correctness、visual correctness 或 performance improvement。

## Boundary statement

Docs/test-only dynamic point view-frame occlusion ablation-conditioned token-trace gate. No helper module creation, no source movement, no production source change, no existing monkey/token/lithology gate change, no checker script change, no generic checker trust-level change, no generic checker blocking behavior change, no generic profile change, no monolith import, no runtime execution, no instrumentation, no `sys.settrace`, no debugger/IDE automation, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula read/copy/movement/change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no coordinate/visual correctness claim, no performance claim, no transparent-globe leak fix claim, no runtime probe authorization, no token-trace global methodology authorization, no semantic-seismic-tomography global methodology authorization, no runtime merge enablement, and no readiness/visual parity/bug-fix/safe-to-extract claim.
