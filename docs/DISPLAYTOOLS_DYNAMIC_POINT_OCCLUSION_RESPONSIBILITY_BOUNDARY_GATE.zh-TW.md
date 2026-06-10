# Dynamic Point Occlusion Responsibility Boundary Gate

本 gate 是 docs/test-only 的 dynamic point occlusion responsibility boundary 與 Good Hope milestone decision。它不是 bug fix gate，也不是 runtime probe gate。目標是在不執行 runtime、不搬移 projection、flip、mask 公式、不改 renderer 或 compose order 的前提下，把 dynamic point 為什麼看不見的責任分區固定到足以進入 runtime characterization planning。

## Evidence read

本 gate 只使用靜態證據：

- `tests/test_displaytools_dynamic_point_grafting_path_minimal_evidence.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_GRAFTING_PATH_MINIMAL_EVIDENCE_GATE.zh-TW.md`
- `tests/test_displaytools_early_runtime_pipeline_characterization.py`
- `docs/DISPLAYTOOLS_EARLY_RUNTIME_PIPELINE_CHARACTERIZATION_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_view_frame_occlusion_structure_settlement.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_VIEW_FRAME_OCCLUSION_STRUCTURE_SETTLEMENT_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_view_frame_occlusion_ablation_conditioned_token_trace.py`
- `tests/test_displaytools_dynamic_point_view_frame_occlusion_token_trace_lithology_transition.py`
- `tests/test_displaytools_dynamic_point_view_frame_occlusion_core_lineage_validation.py`
- 5/29 root import static slice
- current 21k static slice

靜態 scan 覆蓋 `project_ais_to_screen`、`project_aircraft_to_screen`、`horizon_eps`、`z2`、`mask`、`screen_x`、`screen_y`、`current_projected`、`current_sampled_projected`、`AISDatashaderOverlay`、`AircraftDatashaderOverlay`、`globe_mask`、`mask_overlay_to_globe`、`alpha_compose`、`frame_rgba`、`visible_count`、`rendered_count`、`hidden` 與 `visibility`。

## Phase A: responsibility boundary matrix

| candidate | responsible layer | can hide point | can delete source lineage | runtime characterization later |
| --- | --- | --- | --- | --- |
| `projection_horizon_filter` | `projection_grafting` | true | false | true |
| `screen_bounds_filter` | `projection_grafting` | true | false | true |
| `sampling_policy_filter` | `sampling_policy` | true | false | true |
| `datashader_overlay_render` | `datashader_overlay` | true | false | true |
| `globe_mask_alpha_gate` | `globe_mask_occlusion` | true | false | true |
| `alpha_compose_visibility_gate` | `alpha_composition` | true | false | true |
| `presentation_counting_surface` | `presentation_counting` | false | false | false |
| `source_lineage_non_responsibility` | `source_lineage_guard` | false | false | false |
| `transparent_globe_leak_fault_seam` | `fault_candidate_seam` | true | false | true |

責任分區結論：

- Projection horizon 與 screen bounds 可以讓 point 不進入 projected-visible surface，但不能刪除 source lineage。
- Sampling policy 可以讓 point 不進入 sampled-visible surface，但不能把 source 改成 missing。
- Datashader overlay 與 globe mask alpha gate 是 visibility surface，不是 provider 或 cache surface。
- Alpha compose visibility gate 只影響 frame output，不改 source identity。
- Presentation counting surface 回報 `visible_count`、`rendered_count`、`frame_rgba`，不擁有 occlusion source truth。
- Source lineage 明確排除在 visibility responsibility 之外。

## Phase B: occlusion semantics

| semantic | definition |
| --- | --- |
| `projected_visible` | passes projection horizon and screen bounds filters |
| `sampled_visible` | survives sampling policy |
| `overlay_rendered` | included in datashader overlay |
| `mask_visible` | survives `globe_mask` alpha gate |
| `frame_visible` | survives alpha composition and presentation |
| `source_present` | exists in source lineage |

Required invariants:

- `source_present` can be true while `frame_visible` is false
- `projected_visible` can be false without source lineage loss
- `sampled_visible` can be false without missing source
- `mask_visible` can be false without deleting point identity
- transparent globe leak is a seam fault candidate, not fixed

這些 invariants 把「資料還在」和「畫面上可見」分開。Occluded point 不等於 missing source。LOD sampling 也不等於 source lineage mutation。

## Phase C: transparent globe leak fault boundary

Transparent globe leak 的可能責任候選固定為：

- `projection_horizon_filter_fault`
- `screen_bounds_filter_fault`
- `globe_mask_alpha_fault`
- `overlay_mask_shape_fault`
- `alpha_compose_order_fault`
- `presentation_stale_state_fault`
- `not_source_lineage_fault`

Fault boundary output:

| decision | value |
| --- | --- |
| `transparent_globe_leak_fault_model` | `seam_fault_candidate` |
| `source_lineage_fault` | false |
| `fix_authorized` | false |
| `runtime_characterization_required` | true |

這裡只把 fault seam 釘住，不宣稱修復，不宣稱 visual correctness，也不授權 runtime characterization。

## Phase D: Good Hope milestone

Good Hope milestone criteria:

| criterion | status |
| --- | --- |
| `grafting_path_is_known` | true |
| `occlusion_responsibility_is_partitioned` | true |
| `source_lineage_excluded_from_visibility_responsibility` | true |
| `computed_but_hidden_model_supported` | true |
| `transparent_globe_leak_localized_to_seam_fault_candidates` | true |
| `next_action_is_planning_not_implementation` | true |

Milestone decision:

| decision | value |
| --- | --- |
| `good_hope_milestone_reached` | true |
| `exploration_phase_complete_for_dynamic_point_view_frame_occlusion` | true |
| `ready_for_runtime_characterization_planning` | true |
| `runtime_characterization_authorized` | false |
| `surgical_implementation_authorized` | false |

Good Hope milestone 的意思是探索期可以轉入 runtime characterization planning。它不代表可以跑 runtime，不代表可以改 formula，不代表可以修 transparent globe leak，也不代表可以做 surgical implementation。

## Recommended next gate

Recommended next gate is `dynamic_point_lod_view_frame_runtime_characterization_planning_gate`.

原因是 grafting path 已知，occlusion responsibility 已分區，source lineage 已排除 visibility responsibility，computed-but-hidden model 已支持，transparent globe leak 已定位為 seam fault candidate。下一步應設計 runtime characterization plan，而不是直接執行 runtime 或修改 source。

## Boundary statement

Docs/test-only dynamic point occlusion responsibility boundary gate and Good Hope milestone decision. No helper module creation, no source movement, no production source change, no checker script change, no monolith import, no runtime execution, no Taichi/Qt/VisPy/Datashader/Matplotlib runtime execution, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no projection/flip/mask formula movement, no renderer behavior change, no compose order change, no metadata/output schema change, no coordinate/visual correctness claim, no transparent-globe leak fix claim, no runtime characterization authorization, no surgical implementation authorization, no global methodology promotion, no runtime merge enablement, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim.
