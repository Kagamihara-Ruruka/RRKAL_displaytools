# Dynamic Point View-Frame Occlusion Structure Settlement Gate

本 gate 是 docs/test-only 的結構定案，不是 implementation gate。它整合 view-frame occlusion 相關的猴子消融、core-lineage validation、token trace、岩性轉化、ablation-conditioned token trace，以及創世順序輔助軸，輸出後續策略邊界。

本 gate 不跑 renderer，不插 instrumentation，不建立 helper，不讀取、搬移或改寫 projection、flip、mask 公式，也不修改既有探測 gate。

## Evidence streams integrated

- `monkey_ablation_matrix_evidence`: `8b5cac7`
- `core_lineage_validation_evidence`: `bbd978d`
- `token_trace_matrix_evidence`: `373da1e`
- `token_trace_lithology_transition_evidence`: `9c0a40e`
- `ablation_conditioned_token_trace_evidence`: `c7d329c`
- `creation_order_auxiliary_axis`: `f1213c1` 與 `53afb98`

## Settlement surfaces

- `zoom_rotation_view_state`
- `lod_policy`
- `globe_angle_frame_state`
- `projection_shadow`
- `occlusion_policy`
- `presentation_policy`
- `source_lineage_integrity`
- `computed_but_hidden_point`
- `transparent_globe_leak_fault`

## Settlement matrix summary

| Surface | Settled classification | Allowed next strategy | Forbidden next strategy |
| --- | --- | --- | --- |
| `zoom_rotation_view_state` | `core_lineage_view_frame_semantics` | `runtime_characterization_planning` | ordinary helper extraction, source-lineage mutation, renderer runtime execution |
| `lod_policy` | `andesite_bridge_semantics` | `semantic_reconstruction_before_rebuild` | direct code transplant, source filter reclassification, provider/cache/database mutation |
| `globe_angle_frame_state` | `core_lineage_view_frame_semantics` | `runtime_characterization_planning` | ordinary helper extraction, coordinate correctness claim, formula movement |
| `projection_shadow` | `core_interface_only` | `shadow_interface_only` | projection, flip, or mask formula movement |
| `occlusion_policy` | `andesite_bridge_semantics` | `semantic_reconstruction_before_rebuild` | source-lineage mutation, source filter reclassification, visual correctness claim |
| `presentation_policy` | `presentation_contract_candidate` | `presentation_contract_planning` | provider data mutation, source-lineage pollution, performance claim |
| `source_lineage_integrity` | `source_lineage_guard` | `source_lineage_guard_only` | LOD, occlusion, or presentation reverse pollution |
| `computed_but_hidden_point` | `computed_but_hidden_semantics` | `presentation_contract_planning` | hidden to missing source, occlusion as source filter, source-lineage mutation |
| `transparent_globe_leak_fault` | `unresolved_static_fault` | `evidence_gap_review` | visual correctness claim, transparent globe leak fix claim, runtime probe authorization |

## Creation-order auxiliary alignment

創世順序輔助軸只用於判斷 layer depth 是否與 token path 的地層深度相符。它不是主證據，不取代猴子消融、token trace、岩性轉化或 dependency pressure，也不授權 implementation。

本 gate 固定以下邊界：

- `creation_order_auxiliary_axis_aligned = true`
- `creation_order_is_primary_evidence = false`
- `implementation_authorized_by_creation_order = false`
- `religious_correctness_claimed = false`
- `subconscious_design_intent_fully_proven = false`

## Interpretation rules

- `core_lineage_view_frame_semantics`: 只能走 `shadow_interface_only` 或 `runtime_characterization_planning`，不能 ordinary helper extraction。
- `core_interface_only`: 禁止 formula movement，只允許 reference、ledger、shadow interface。
- `andesite_bridge_semantics`: 需要 semantic reconstruction，不應直接移植舊 code。
- `presentation_contract_candidate`: 可規劃 presentation contract，但不可污染 source lineage。
- `source_lineage_guard`: 只能守住 identity，不可被 LOD、occlusion、presentation 反向修改。
- `computed_but_hidden_semantics`: hidden 不等於 missing，遮蔽不等於 source filter。
- `unresolved_static_fault`: transparent globe leak fault 保持 unresolved，不得宣稱修復。
- `forbidden_pollution_path`: 一律 stop，不得進入 runtime probe。

## Decision output

- `structure_settlement_gate_passed = true`
- `view_frame_occlusion_structure_settled = true`
- `ordinary_helper_extraction_authorized = false`
- `shadow_interface_path_required = true`
- `semantic_reconstruction_required_for_andesite = true`
- `presentation_contract_candidate_present = true`
- `source_lineage_guard_required = true`
- `runtime_characterization_planning_candidate = true`
- `runtime_characterization_authorized = false`
- `instrumentation_authorized = false`
- `helper_module_creation_authorized = false`
- `source_movement_authorized = false`
- `formula_movement_authorized = false`
- `renderer_runtime_authorized = false`
- `coordinate_correctness_claimed = false`
- `visual_correctness_claimed = false`
- `performance_claimed = false`
- `transparent_globe_leak_fix_claimed = false`
- `semantic_seismic_tomography_local_pattern_supported = true`
- `semantic_seismic_tomography_global_methodology_authorized = false`
- `creation_order_auxiliary_axis_aligned = true`
- `creation_order_is_primary_evidence = false`
- `implementation_authorized_by_creation_order = false`

## Recommended next gate

`dynamic_point_lod_view_frame_runtime_characterization_planning_gate`

下一張若要靠近 runtime，只能先做 planning gate，定義觀測邊界、允許輸出、禁止 instrumentation 污染與人工 review 條件。這不是 runtime authorization。

## Boundary statement

Docs/test-only dynamic point view-frame occlusion structure settlement gate. No helper module creation, no source movement, no production source change, no existing monkey/token/lithology/core-lineage gate change, no checker script change, no generic checker trust-level change, no generic checker blocking behavior change, no generic profile change, no monolith import, no runtime execution, no instrumentation, no `sys.settrace`, no debugger/IDE automation, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula read/copy/movement/change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no coordinate/visual correctness claim, no performance claim, no transparent-globe leak fix claim, no runtime characterization authorization, no token-trace global methodology authorization, no semantic-seismic-tomography global methodology authorization, no creation-order primary-evidence/religious-correctness claim, no runtime merge enablement, and no readiness/visual parity/bug-fix/safe-to-extract claim.
