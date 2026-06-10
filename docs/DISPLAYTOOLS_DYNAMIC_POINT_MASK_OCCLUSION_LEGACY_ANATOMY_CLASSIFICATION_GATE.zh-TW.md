# Dynamic Point Mask / Occlusion Legacy Anatomy Classification Gate

## 目的

本 gate 將 dynamic point mask / occlusion 剩餘候選整理成 legacy anatomy / semantic fossil 分類圖。目標是分清楚哪些是 observed need、哪些是 approximate runtime patch、哪些是可繼承語意、哪些是理型胚胎，哪些必須保留為 granite stop-line。

本 gate 不建立 mask visibility helper、不建立 occlusion responsibility helper、不建立 occluding body helper、不建立 checker，也不把舊 `mask` 實作制度化為新的 c_3 interface。

## Evidence read

本 gate 使用以下 static evidence：

- `render_core/dynamic_point_sampling_visibility_boundary.py`
- `render_core/dynamic_point_presentation_count_boundary.py`
- `render_core/dynamic_point_computed_but_hidden_boundary.py`
- `render_core/dynamic_point_source_lineage_guard_boundary.py`
- `render_core/dynamic_point_presentation_reduction_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_boundary_helpers.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_presentation_count_boundary_helpers.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_computed_but_hidden_boundary_helpers.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_source_lineage_guard_boundary_helpers.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_presentation_reduction_boundary_helpers.py`
- `tests/test_displaytools_dynamic_point_occlusion_responsibility_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_frame_visibility_stop_line_planning.py`
- `docs/DOCS_INDEX.zh-TW.md`

## Static scan summary

Static scan scope：

```text
taichi_global_bathymetry.py
render_core
tests
docs
scripts
```

Scan terms：

```text
mask
occlusion
horizon
alpha
compose
globe_mask
mask_overlay_to_globe
frame_rgba
render_if_needed
visible
hidden
source_lineage
rendered_count
visible_count
projection
screen_bounds
AIS
contour
water
overlay
```

Scan result is static evidence only. No runtime execution, no renderer execution, no probe execution, and no formula movement occurred.

Summary：

- legacy mask seams are observed in static evidence;
- layered overlay vocabulary is observed;
- frame, alpha, compose, and renderer-adjacent surfaces remain stop-lines;
- source-lineage guards are already extracted as data-only semantics;
- no classification requires formula movement.

## Classification taxonomy

Every row uses one of these labels：

- `modern_semantic_interface_candidate`
- `ediacaran_semantic_fossil`
- `ideal_form_embryo`
- `legacy_runtime_patch`
- `approximate_function_from_observed_need`
- `granite_anatomy_evidence`
- `granite_stop_line`
- `deprecated_behavior_fossil`
- `not_enough_evidence`

## Classification matrix summary

| Surface | Classification | Summary |
| --- | --- | --- |
| `backside_ais_leak_observed_need` | `approximate_function_from_observed_need` | Backside AIS penetration is observed need, not correctness proof. |
| `earth_body_as_occluder_ideal_embryo` | `ideal_form_embryo` | Earth body as occluder is valuable ideal-form embryo. |
| `legacy_mask_patch_lineage` | `legacy_runtime_patch` | Current mask is approximate runtime patch, not new interface. |
| `layered_overlay_visibility_pressure` | `modern_semantic_interface_candidate` | Overlay visibility pressure supports future layered visibility language. |
| `contour_water_overlay_mask_pressure` | `approximate_function_from_observed_need` | Contour, water, and overlay layers add observed pressure. |
| `mask_overlay_to_globe_legacy_seam` | `legacy_runtime_patch` | Existing seam is implementation path, not ideal form. |
| `globe_mask_visibility_gate` | `ediacaran_semantic_fossil` | Useful early visibility semantics tied to old vocabulary. |
| `horizon_or_projection_visibility_pressure` | `granite_anatomy_evidence` | Near projection and horizon formula anatomy. |
| `alpha_compose_entanglement` | `granite_stop_line` | Renderer and compose adjacent. |
| `frame_visibility_stop_line` | `granite_stop_line` | Frame visibility remains unobserved. |
| `transparent_globe_leak_fault_candidate` | `granite_stop_line` | Fault candidate remains not inferred and not fixed. |
| `source_lineage_non_mutation_guard` | `modern_semantic_interface_candidate` | Source lineage must not be changed by visibility state. |
| `sampling_visibility_interaction` | `modern_semantic_interface_candidate` | Existing extracted token/count/mask interaction evidence. |
| `presentation_count_interaction` | `modern_semantic_interface_candidate` | Count semantics are contract fields, not frame truth. |
| `computed_but_hidden_interaction` | `modern_semantic_interface_candidate` | Computed and hidden separates existence from visibility. |
| `presentation_reduction_interaction` | `modern_semantic_interface_candidate` | Rendered lower than visible remains reduction candidate only. |
| `future_layered_occluding_body_visibility_contract_candidate` | `ideal_form_embryo` | Future implementation-neutral layered occluding body contract candidate. |

## Observed need vs approximate patch

Backside AIS penetration is an observed need. It is not proof of coordinate correctness, visual correctness, or transparent-globe leak fix. The legacy `mask` path is an approximate runtime patch created in response to that need, not the ideal c_3 interface itself.

## Ideal-form embryo

The useful ideal is not the legacy mask function. The useful ideal embryo is `layered_occluding_body_visibility_contract`: an implementation-neutral language where earth, contour, water, overlay, and dynamic points can be classified as layered visibility surfaces without binding the prototype to old runtime patch seams.

## Layered visibility pressure

Contour, water, overlay, mask, and dynamic point visibility pressure indicate a layered visibility problem. This supports future ideal-form planning, but does not authorize direct helper extraction for mask or occlusion in this gate.

## Granite stop-line summary

The following remain granite stop-lines：

- `frame_visibility_stop_line`
- `alpha_compose_entanglement`
- `transparent_globe_leak_fault_candidate`
- renderer / controller / frame buffer runtime
- `render_if_needed` runtime
- projection / mask / sampling / alpha-compose formula surfaces

## Prototype implication

Future prototype work should not directly consume the legacy `mask` implementation as a new interface. It should first correct the ideal form and plan an implementation-neutral layered occluding body visibility contract. Source lineage must remain protected and must not be rewritten by mask, occlusion, reduction, or hidden states.

## Decision output

```text
mask_occlusion_legacy_anatomy_classification_passed = true
direct_mask_helper_extraction_authorized = false
direct_occlusion_helper_extraction_authorized = false
legacy_mask_implementation_is_ideal_form = false
occluding_body_visibility_ideal_embryo_supported = true
layered_visibility_pressure_supported = true
prototype_interface_candidate_requires_ideal_form_correction = true
transparent_globe_leak_inferred = false
visual_correctness_claimed = false
readiness_claimed = false
```

Additional closed flags：

```text
direct_prototype_interface_authorized = false
transparent_globe_leak_fix_claimed = false
coordinate_correctness_claimed = false
performance_claimed = false
runtime_execution_authorized = false
formula_movement_authorized = false
c4_odoriba_bypass_authorized = false
```

## Recommended next gate

```text
dynamic_point_layered_occluding_body_visibility_contract_planning_gate
```

## Boundary statement

Docs/test-only dynamic point mask / occlusion legacy anatomy classification gate. No helper creation, no checker creation, no `render_core` change, no runtime probe change, no `taichi_global_bathymetry.py` change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no projection/mask/sampling/alpha-compose formula movement, no real AIS/ADS-B/SQL/WebSocket/cache/database read, no source-lineage mutation, no direct mask or occlusion helper extraction authorization, no legacy mask implementation ideal-form claim, no direct prototype interface authorization, no transparent-globe leak inference or fix claim, no coordinate/visual correctness claim, no readiness/performance claim, no c_4/Odoriba bypass, and no push.