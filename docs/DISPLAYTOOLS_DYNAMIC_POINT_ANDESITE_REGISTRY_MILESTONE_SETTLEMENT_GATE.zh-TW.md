# Dynamic Point Andesite Registry Milestone Settlement Gate

## 目的

本 gate 是 docs/test-only 里程碑收束。它把 dynamic point / LOD / view-frame 已抽出的安山岩語意面正式入冊，並把 mask / occlusion 相關殘餘面分成語意化石、理型胚胎、近似功能、舊 runtime patch 與花崗岩 stop-line。

本 gate 不建立 helper、不建立 checker、不修改 runtime，也不授權新 c_3 prototype 直接接 legacy mask 實作。

## Evidence read

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
- `tests/test_displaytools_dynamic_point_mask_occlusion_legacy_anatomy_classification.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_MASK_OCCLUSION_LEGACY_ANATOMY_CLASSIFICATION_GATE.zh-TW.md`
- `docs/DOCS_INDEX.zh-TW.md`

## Registry categories

- `modern_semantic_interface`
- `ediacaran_semantic_fossil`
- `ideal_form_embryo`
- `approximate_function_from_observed_need`
- `legacy_runtime_patch`
- `granite_anatomy_evidence`
- `granite_stop_line`
- `prototype_interface_candidate_after_translation`
- `not_prototype_interface_without_correction`

## Modern semantic interface inventory

以下五個 surface 已是 descriptor / contract / ledger-only helper，可作為已抽出的現代語意面，但仍需翻譯後才能成為新 c_3 prototype 的 final API。

| surface | settlement classification | prototype implication |
| --- | --- | --- |
| `sampling_visibility_boundary` | `modern_semantic_interface` | 可提供 sampling / visibility token 與 count 觀測語意，但不是 renderer truth。 |
| `presentation_count_boundary` | `modern_semantic_interface` | 可提供 `visible_count` / `rendered_count` contract field，但不是 source completeness 或 frame truth。 |
| `computed_but_hidden_boundary` | `modern_semantic_interface` | 固定 hidden 不是 missing，occluded 不是 source-lineage loss。 |
| `source_lineage_guard_boundary` | `modern_semantic_interface` | 保護 source identity 不被 sampling、presentation、hidden、mask、occlusion 或 raw-row seam 改寫。 |
| `presentation_reduction_boundary` | `modern_semantic_interface` | 固定 `rendered_count < visible_count` 只是 presentation / sampling reduction candidate。 |

`modern_semantic_interface_count = 5`

## Ediacaran semantic fossil and anatomy material

| surface | settlement classification | meaning |
| --- | --- | --- |
| `legacy_mask_patch_lineage` | `legacy_runtime_patch` | 舊 mask 是 observed need 下的近似 runtime patch，不是理型本身。 |
| `mask_overlay_to_globe_legacy_seam` | `legacy_runtime_patch` | 可當 anatomy evidence，不可直接成為新 prototype interface。 |
| `globe_mask_visibility_gate` | `ediacaran_semantic_fossil` | 保留早期 visibility 語意化石，需翻譯。 |
| `occlusion_responsibility_legacy_path` | `ediacaran_semantic_fossil` | 可提供 responsibility 語意線索，但不可直接抽成 runtime path。 |
| `backside_ais_leak_observed_need` | `approximate_function_from_observed_need` | 背面 AIS 穿透是 observed need，不是 correctness proof。 |

## Ideal-form embryo inventory

| surface | settlement classification | implication |
| --- | --- | --- |
| `earth_body_as_occluder_ideal_embryo` | `ideal_form_embryo` | 地球作為遮擋體是有價值的理型胚胎。 |
| `layered_occluding_body_visibility_contract_candidate` | `ideal_form_embryo` | 未來應以 implementation-neutral layered visibility contract 表達。 |
| `layered_visibility_pressure` | `ideal_form_embryo` | contour、water、overlay、dynamic point 共同證明這是 layered visibility problem。 |

## Granite stop-line inventory

以下 surface 保持 stop-line，不在本 milestone 授權抽離或執行。

- `frame_visibility_surface`
- `transparent_globe_leak_fault`
- `controller_renderer_frame_buffer_runtime`
- `render_if_needed_runtime`
- `projection_mask_sampling_alpha_formula_surfaces`
- `alpha_compose_entanglement`
- `horizon_or_projection_visibility_pressure`

## Required conclusions

```text
andesite_registry_milestone_reached = true
cutting_phase_for_clear_andesite_surfaces_complete = true
remaining_mask_occlusion_direct_extraction_authorized = false
mask_occlusion_requires_ideal_form_translation = true
modern_semantic_interface_count = 5
ediacaran_semantic_fossil_classification_completed = true
granite_stop_line_registry_completed = true
new_c3_prototype_should_consume_translated_semantics = true
new_c3_prototype_should_not_consume_legacy_mask_directly = true
temporary_operational_backdoor_allowed_future_planning_only = true
graphics_prior_structure_needed = true
universal_display_framework_direction_supported = true
runtime_replacement_authorized = false
readiness_claimed = false
```

## Strategic phase shift

Current phase shifts from:

```text
semantic reconstruction / andesite cutting
```

to:

```text
ideal-form translation / graphics prior structure / new c_3 prototype methodology
```

這表示清楚安山岩語意面造冊已達成里程碑。後續重點不應繼續把 legacy mask 直接切成新接口，而應先建立圖形學先驗結構與 implementation-neutral 語言。

## Prototype implication

- Existing 5 semantic interfaces are useful but still require translation before becoming final prototype API.
- Mask / occlusion is Ediacaran fossil plus ideal-form embryo, not direct final interface.
- Future c_3 should target implementation-neutral `layered_occluding_body_visibility_contract`, not legacy `mask`.
- Temporary earth / AIS operational backdoor may be planned later, but must be modular, removable, and explicitly non-ideal-form.

## Boundary statement

Docs/test-only dynamic point andesite registry milestone settlement gate. No helper creation, no checker creation, no existing helper or checker modification, no `render_core` change, no runtime probe change, no `taichi_global_bathymetry.py` change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no projection/mask/sampling/alpha-compose formula movement, no real AIS/ADS-B/SQL/WebSocket/cache/database read, no source-lineage mutation, no direct mask or occlusion helper extraction authorization, no legacy mask implementation ideal-form claim, no direct prototype final-interface authorization without translation, no temporary operational backdoor implementation, no transparent-globe leak inference or fix claim, no coordinate/visual correctness claim, no readiness/performance claim, no runtime replacement authorization, no c_4/Odoriba bypass, and no push.

## Final classification

```text
c3_displaytools_dynamic_point_andesite_registry_milestone_settlement_gate_committed_for_o1_review_no_push
```