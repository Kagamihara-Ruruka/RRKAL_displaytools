# Dynamic Point View-Frame Occlusion Core-Lineage Validation Gate

## Gate 目的

本 gate 驗證 dynamic point 的 view-frame、LOD、globe-angle、occlusion 鏈路是否屬於早期 globe/view-frame 地核語意延續到 dynamic point。它只建立 docs/test-only validation fixture，不跑 renderer，不跑 dynamic point runtime，不建立 helper，不移動公式。

要驗證的鏈路：

```text
rotation / zoom
-> LOD policy
-> globe angle / view frame
-> projection shadow
-> occlusion policy
-> presentation
```

核心問題是：這條鏈是 dynamic point 後期沉積岩，還是早期 globe/view-frame 地核語意延續到 dynamic point。此 gate 的結論是：目前 static evidence 支持 core-lineage view-frame semantics，因此後續不能走普通 helper extraction，只能走 shadow/interface 與 runtime characterization planning。

## Anchors

- base camp rollback anchor: `ad38dbe`
- dynamic point lithology L2 local pattern source: `60cded8`
- projection shadow source: `6289c60`
- projection shadow planning: `a67a685`
- view-frame occlusion monkey matrix: `8b5cac7`
- creation-order counterexample source: `53afb98`

## Optional history query

本 gate 嘗試讀取 `taichi_global_bathymetry.py` 的 git history log 與 reverse rev-list。查詢成功，記錄為：

```text
history_query_attempted = true
history_query_limited = false
runtime_execution_performed = false
```

歷史詞彙只提供 age pressure，不單獨判決岩性。

## Evidence dimensions

| dimension | summary | conclusion |
| --- | --- | --- |
| `historical_age_pressure` | rotation、zoom、LOD、frame、angle、projection、mask、visibility 類詞不是晚期 dynamic point descriptor 獨有。 | supports core-lineage |
| `dependency_depth_pressure` | 鏈路靠近 renderer、projection、frame、hot path 與 presentation。 | supports core-lineage |
| `monkey_ablation_response` | `8b5cac7` 將 view-frame / LOD / occlusion / presentation 與 source lineage 分離。 | supports core-lineage |
| `semantic_reconstruction_pressure` | dynamic point 較像接入既有 view-frame law，而不是自己發明整套 visibility law。 | supports core-lineage |

## Surface classification matrix

| surface | semantic classification | recommended strategy |
| --- | --- | --- |
| `zoom_rotation_view_state` | `core_lineage_view_frame_semantics` | shadow interface and runtime characterization planning only |
| `lod_policy` | `presentation_policy_surface` | runtime characterization candidate without runtime authorization |
| `globe_angle_frame_state` | `core_lineage_view_frame_semantics` | core interface shadow, not formula extraction |
| `projection_shadow` | `core_interface_only` | shadow interface with checker guard |
| `occlusion_policy` | `runtime_characterization_candidate` | runtime characterization planning after core-lineage validation |
| `presentation_policy` | `presentation_policy_surface` | presentation policy characterization without runtime merge |
| `source_lineage_integrity` | `source_lineage_guard` | keep guarded against LOD/occlusion mutation |
| `computed_but_hidden_point` | `runtime_characterization_candidate` | characterize without claiming runtime correctness |
| `transparent_globe_leak_fault` | `unresolved_static_fault` | record fault and plan observation without fix claim |

## Core-lineage support decision

```text
view_frame_occlusion_core_lineage_supported = true
ordinary_helper_extraction_authorized = false
shadow_interface_path_required = true
runtime_characterization_candidate = true
runtime_characterization_authorized = false
formula_movement_authorized = false
renderer_runtime_authorized = false
coordinate_correctness_claimed = false
visual_correctness_claimed = false
performance_claimed = false
transparent_globe_leak_fix_claimed = false
recommended_next_gate = dynamic_point_lod_view_frame_runtime_characterization_planning_gate
```

## Transparent globe leak fault

`transparent_globe_leak_fault` 仍是 unresolved static fault。此 gate 不宣稱背面點遮蔽已修復，不宣稱 visual correctness，不執行 renderer，也不授權 runtime characterization。

## Boundary statement

Docs/test-only dynamic point view-frame occlusion core-lineage validation gate. No helper module creation, no source movement, no production source change, no checker script change, no generic checker trust-level change, no generic checker blocking behavior change, no generic profile change, no monolith import, no runtime execution, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula read/copy/movement/change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no coordinate/visual correctness claim, no performance claim, no transparent-globe leak fix claim, no runtime characterization authorization, no runtime merge enablement, and no readiness/visual parity/bug-fix/safe-to-extract claim.
