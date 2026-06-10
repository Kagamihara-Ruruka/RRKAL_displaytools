# Dynamic Point Grafting Path Minimal Evidence Gate

本 gate 是 docs/test-only 的最小接枝路徑證據盤點。目標是用 5/29 root import 與 current 21k 的靜態證據，窮舉 dynamic point 從 source 到 projection、overlay、mask、compose、presentation 的最小路徑，並固定 occlusion 與 computed-but-hidden 的責任邊界。

本 gate 不執行 runtime，不 import 舊版或 current runtime，不搬移 projection、flip、mask 公式，不修改 renderer 行為，不宣稱座標正確、視覺正確、透明地球穿透已修復、readiness 或 safe-to-extract。

## 證據來源

| slice | evidence | status |
| --- | --- | --- |
| 5/29 root import | `d90b6451e9b8db32defa7a096e6aff31a2ff49be:taichi_global_bathymetry.py` | static read only |
| current 21k | `L:\RRKAL_displaytools\taichi_global_bathymetry.py` | static scan only |
| early runtime pipeline characterization | `tests/test_displaytools_early_runtime_pipeline_characterization.py` and docs | static read only |
| view-frame occlusion settlement | settlement, ablation-conditioned token trace, core-lineage validation gates | static read only |

5/29 root import 的靜態切片可觀察到 `AISSource`、`AircraftSource`、`normalize_ais_frame`、`normalize_aircraft_frame`、`project_ais_to_screen`、`project_aircraft_to_screen`、`current_projected`、`current_sampled_projected`、`AISDatashaderOverlay`、`AircraftDatashaderOverlay`、`mask_overlay_to_globe`、`globe_mask`、`alpha_compose`、`frame_rgba`、`visible_count`、`rendered_count` 與 `horizon_eps`。

current 21k 仍可觀察到同一條接枝鏈，並新增更明確的 `adaptive_sampling`、`ais_sample_ratio`、`aircraft_sample_ratio` 與 presentation 計數路徑。這表示 dynamic point 更像後期 graft 到既有 globe/view-frame core，而不是 5/10 或 5/12 原生地核。

## Phase A: minimal path inventory

| path | 5/29 evidence | current evidence | expected role | responsible layer |
| --- | --- | --- | --- | --- |
| `ais_source_to_projected_path` | present | present | AIS source payload reaches projected dynamic point graft seam | `projection_grafting` |
| `adsb_source_to_projected_path` | present | present | ADS-B source payload reaches projected dynamic point graft seam | `projection_grafting` |
| `projected_to_sampled_path` | present | present | computed projected points feed sampling policy | `sampling_policy` |
| `sampled_to_datashader_overlay_path` | present | present | sampled points feed overlay rendering surface | `datashader_overlay` |
| `overlay_to_globe_mask_path` | present | present | overlay alpha is constrained by globe mask visibility seam | `globe_mask_occlusion` |
| `masked_overlay_to_alpha_compose_path` | present | present | masked overlays enter composition without changing source identity | `alpha_composition` |
| `compose_to_frame_rgba_path` | present | present | composition result becomes frame surface reference | `presentation_counting` |
| `presentation_counts_path` | present | present | computed and sampled counts are presentation observations | `presentation_counting` |
| `horizon_epsilon_occlusion_path` | present | present | horizon and mask seam remains a visibility fault candidate | `fault_candidate` |
| `computed_but_hidden_path` | present | present | point can exist while visibility is hidden by mask or presentation policy | `globe_mask_occlusion` |

Every path keeps `source_lineage_can_be_mutated = false`, `visual_correctness_claimed = false`, and `coordinate_correctness_claimed = false`.

## Phase B: responsibility boundary

| responsibility | local boundary |
| --- | --- |
| `source_lineage` | `AISSource` and `AircraftSource` identify provider presence only |
| `payload_normalization` | `normalize_ais_frame` and `normalize_aircraft_frame` shape payloads before projection grafting |
| `projection_grafting` | `project_ais_to_screen` and `project_aircraft_to_screen` attach dynamic payloads to the existing screen seam |
| `sampling_policy` | `current_projected` to `current_sampled_projected`, plus sample ratio and adaptive sampling labels |
| `datashader_overlay` | `AISDatashaderOverlay` and `AircraftDatashaderOverlay` render overlay surfaces |
| `globe_mask_occlusion` | `mask_overlay_to_globe` and `globe_mask` own visibility suppression semantics |
| `alpha_composition` | `alpha_compose` and transparent composition join masked overlays into frame output |
| `presentation_counting` | `visible_count`, `rendered_count`, and `frame_rgba` report presentation state |
| `fault_candidate` | transparent globe leak candidate sits around `horizon_eps`, `globe_mask`, overlay masking, and composition seam |

Preliminary boundary is strong enough to show dynamic point is grafted to view-frame core. Occlusion responsibility is localized only partially because static evidence cannot prove runtime visibility behavior without executing renderer. The unresolved leak remains a fault candidate, not a fix claim.

## Phase C: computed-but-hidden model

| state | definition |
| --- | --- |
| `computed` | exists in source lineage or `current_projected` |
| `sampled` | exists in `current_sampled_projected` |
| `rendered` | included in datashader overlay path |
| `hidden` | alpha suppressed by `globe_mask` or presentation policy |
| `missing` | absent from source lineage |

Rules fixed by this gate:

- `hidden != missing`
- `occluded != source_lineage_loss`
- `LOD sampling != source_lineage_mutation`

This model supports the prior settlement conclusion that visibility is not existence. A computed point can be hidden without being removed from provider lineage.

## Phase D: decision output

| decision | value |
| --- | --- |
| `dynamic_point_grafting_path_inventory_passed` | true |
| `dynamic_point_native_early_core` | false |
| `dynamic_point_grafted_to_view_frame_core` | true |
| `occlusion_responsibility_localized` | partial |
| `computed_but_hidden_model_supported` | true |
| `transparent_globe_leak_fault_model` | `unresolved_candidate` |
| `runtime_characterization_planning_candidate` | true |
| `runtime_characterization_authorized` | false |
| `source_movement_authorized` | false |
| `formula_movement_authorized` | false |
| `visual_correctness_claimed` | false |
| `coordinate_correctness_claimed` | false |
| `token_trace_global_methodology_authorized` | false |
| `semantic_seismic_tomography_global_methodology_authorized` | false |

## Recommended next gate

Recommended next gate is `dynamic_point_occlusion_responsibility_boundary_gate`.

Reason: the source, projection, sampling, overlay, mask, compose, and presentation path is clear enough for grafting evidence. The occlusion seam is only partially localized because transparent globe leakage still needs a narrower static responsibility boundary before runtime characterization planning is useful.

## Boundary statement

Docs/test-only dynamic point grafting path minimal evidence gate. No helper module creation, no source movement, no production source change, no checker script change, no monolith import, no runtime execution, no Taichi/Qt/VisPy/Datashader/Matplotlib runtime execution, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no projection/flip/mask formula movement, no renderer behavior change, no compose order change, no metadata/output schema change, no coordinate/visual correctness claim, no transparent-globe leak fix claim, no runtime characterization authorization, no global methodology promotion, no runtime merge enablement, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim.
