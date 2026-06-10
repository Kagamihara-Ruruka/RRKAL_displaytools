# Dynamic Point Presentation Count Cartography Update Gate

## Gate 範圍

本 gate 更新 dynamic point local map，將 `render_core/dynamic_point_presentation_count_boundary.py` 登記為已抽離的 descriptor / contract / ledger helper。

本 gate 不建立 helper，不修改 checker，不改 runtime probe，不碰 `taichi_global_bathymetry.py`，也不碰 `render_if_needed`、controller、renderer、frame buffer、artifact writer 或公式。

## Evidence read

- `render_core/dynamic_point_presentation_count_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_presentation_count_boundary_helpers.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_PRESENTATION_COUNT_MINIMAL_EXTRACTION_GATE.zh-TW.md`
- `scripts/validate_displaytools_dynamic_point_presentation_count_import_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_presentation_count_contract_planning.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_next_andesite_bridge_selection.py`
- `tests/test_displaytools_dynamic_point_sampling_visibility_cartography_update.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_frame_visibility_stop_line_planning.py`

## Updated cartography summary

`dynamic_point_presentation_count_boundary.py` 已加入 extracted helper inventory，分類為：

```text
extracted_andesite_bridge_descriptor_contract_ledger
```

這代表 `visible_count`、`rendered_count`、`rendered_count < visible_count` 這組語意已經冷卻成可守邊界的資料合約。

這不代表 source completeness，不代表 frame truth，不代表透明地球 leak 已被推論，也不代表任何視覺正確性或 readiness。

## Extracted helper inventory delta

新增 inventory entry：

```text
surface_name = presentation_count_boundary_descriptors
path = render_core/dynamic_point_presentation_count_boundary.py
helper_kind = descriptor_contract_ledger_helper
checker = scripts/validate_displaytools_dynamic_point_presentation_count_import_boundary.py
helper_test = tests/test_displaytools_dynamic_point_lod_view_frame_presentation_count_boundary_helpers.py
cartography_status = extracted_andesite_bridge_descriptor_contract_ledger
runtime_dependency_allowed = false
source_movement_authorized = false
formula_movement_authorized = false
frame_buffer_dependency_allowed = false
source_loss_interpretation_allowed = false
```

## Dynamic point extracted helper inventory

目前 dynamic point local map 中，已登記的 descriptor / contract / ledger helper 包含：

```text
aggregate_boundary_descriptors
source_lineage_boundary_descriptors
selection_render_policy_boundary_descriptors
payload_coordinate_quality_boundary_descriptors
render_cap_adaptive_sampling_boundary_descriptors
sampling_visibility_boundary_descriptors
presentation_count_boundary_descriptors
```

## Classification update

- `presentation_count_boundary_descriptors`: 從 andesite bridge extraction candidate 更新為 extracted andesite bridge descriptor / contract / ledger。
- `visible_rendered_count_semantics`: 從 presentation count contract candidate 更新為 cooled descriptor / contract semantics。
- `rendered_lower_than_visible_semantics`: 固定為 reduction candidate，不推論 source loss。
- `frame_visibility_surface`: 維持 frame visibility stop-line。
- `transparent_globe_leak_fault`: 維持 not inferred unresolved fault。

## Remaining surfaces

仍需保留的 stop-line 與 blocked surface：

- `frame_visibility_surface`: frame_visible_token 仍未觀測，frame buffer 未讀取。
- `transparent_globe_leak_fault`: 尚未推論，也未修復。
- `projection_mask_sampling_formula_surfaces`: 仍是 granite 或 core formula stop-line。
- `controller_renderer_frame_buffer_runtime`: 仍是 granite runtime stop-line。
- `source_lineage_loss_interpretation`: count reduction 不得解釋為 source loss。

## Decision output

```text
cartography_update_gate_passed = true
presentation_count_helper_added_to_extracted_inventory = true
presentation_count_boundary_is_descriptor_contract_ledger_helper = true
presentation_count_map_delta_recorded = true
visible_rendered_count_contract_semantics_cooled = true
rendered_lower_than_visible_remains_reduction_candidate_only = true
source_loss_interpretation_authorized = false
frame_visibility_remains_stop_line = true
transparent_globe_leak_inferred = false
transparent_globe_leak_fix_claimed = false
production_source_change_authorized = false
runtime_probe_change_authorized = false
render_if_needed_authorized = false
controller_renderer_frame_buffer_authorized = false
artifact_generation_authorized = false
formula_movement_authorized = false
coordinate_correctness_claimed = false
visual_parity_claimed = false
readiness_claimed = false
rrkal_wide_methodology_authorized = false
```

## Recommended next gate

```text
dynamic_point_lod_view_frame_post_presentation_count_next_bridge_selection_gate
```

presentation count 已冷卻並登記，下一步應重新選擇剩餘 andesite bridge，而不是直接進入 frame 或 renderer surface。

## Boundary statement

Docs/test-only dynamic point presentation count cartography update gate. No helper creation, no production source change, no runtime probe change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no projection/mask/sampling formula movement, no source-loss interpretation, no transparent-globe leak inference, no correctness/visual parity/readiness/leak-fix claim, no RRKAL-wide methodology promotion, and no push.
