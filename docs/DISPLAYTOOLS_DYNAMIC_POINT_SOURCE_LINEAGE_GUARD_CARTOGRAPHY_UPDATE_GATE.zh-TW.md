# Dynamic Point Source-Lineage Guard Cartography Update Gate

## 目標

本 gate 更新 dynamic point LOD / view-frame 安山岩語意海圖，把已抽出的 `source_lineage_guard_boundary` 納入 extracted andesite inventory。這是 docs/test-only cartography update，不新增 helper、不新增 checker、不修改 `render_core`、不碰 runtime。

## Evidence read

- `render_core/dynamic_point_source_lineage_guard_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_source_lineage_guard_boundary_helpers.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_SOURCE_LINEAGE_GUARD_MINIMAL_EXTRACTION_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_post_computed_but_hidden_cartography_update.py`
- `tests/test_displaytools_dynamic_point_post_computed_but_hidden_next_bridge_selection.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_source_lineage_guard_contract_planning.py`

## Updated cartography summary

Extracted andesite inventory now includes four descriptor / contract / ledger surfaces:

- `sampling_visibility_boundary`
- `presentation_count_boundary`
- `computed_but_hidden_boundary`
- `source_lineage_guard_boundary`

`source_lineage_guard_boundary` classification:

```text
extracted_andesite_bridge_guard_descriptor_contract_ledger
```

This fourth surface acts as a guard bridge across already extracted and future candidate semantics.

## Source-lineage guard protection map

`source_lineage_guard_boundary` protects:

- sampling visibility
- presentation count
- computed-but-hidden
- future mask visibility
- future occlusion responsibility
- raw-row compatibility seam as label / ledger / handoff only

It does not authorize source-lineage mutation, runtime source reads, direct c_3-to-c_1 integration, or c_4/Odoriba bypass.

## Remaining candidate matrix

Remaining andesite candidates after this cartography update:

- `occlusion_responsibility_contract`
  - Reason: source guard now lowers source-loss drift, but mask/formula/frame stop-lines still require sequencing.
  - Stop condition: stop if occlusion is treated as source-lineage loss or requires mask formula movement.
- `mask_visibility_contract`
  - Reason: mask-visible semantics are partially cooled and now protected from source deletion drift.
  - Stop condition: stop if mask hidden is interpreted as missing source or requires formula movement.
- `presentation_reduction_contract`
  - Reason: reduction semantics are cooled and source guard keeps rendered lower than visible from becoming source loss.
  - Stop condition: stop if rendered lower than visible is treated as source loss.

## Granite stop-line inventory

These remain granite / stop-line surfaces:

- `frame_visibility_surface`
- `transparent_globe_leak_fault`
- `controller_renderer_frame_buffer_runtime`
- `render_if_needed_runtime`
- `projection_mask_sampling_alpha_formula_surfaces`

No frame visibility, transparent-globe leak behavior, controller, renderer, frame buffer, `render_if_needed`, or formula movement is authorized by this gate.

## c_4/Odoriba and raw-row seam boundary

- `c4_odoriba_mediation_required = true`
- `direct_c3_to_c1_dependency_authorized = false`
- `c4_odoriba_bypass_authorized = false`
- `raw_row_seam_runtime_authorized = false`

The raw-row seam remains transitional label / ledger / handoff material. It is not runtime integration and not mature c_1 integration.

## Decision output

- `cartography_update_passed = true`
- `source_lineage_guard_boundary_registered = true`
- `extracted_andesite_surface_count = 4`
- `remaining_candidate_count = 3`
- `granite_stop_line_count = 5`
- `dependency_cycle_watch_enabled = true`
- `next_bridge_selection_required = true`
- `c4_odoriba_mediation_required = true`
- `direct_c3_to_c1_dependency_authorized = false`
- `c4_odoriba_bypass_authorized = false`
- `raw_row_seam_runtime_authorized = false`

## Recommended next gate

```text
dynamic_point_lod_view_frame_post_source_lineage_guard_next_bridge_selection_gate
```

## Boundary statement

Docs/test-only dynamic point source-lineage guard cartography update gate. No helper creation, no checker creation or checker modification, no `render_core` change, no runtime probe change, no `taichi_global_bathymetry.py` change, no `render_if_needed`, no controller, no renderer, no GUI, no frame buffer read, no artifact generation, no formula movement, no real AIS/ADS-B/SQL/WebSocket/cache/database read, no source-lineage mutation, no raw-row seam runtime authorization, no direct c_3-to-c_1 integration, no c_4/Odoriba bypass, no transparent-globe leak inference or fix claim, no correctness or visual parity claim, no readiness claim, no RRKAL-wide methodology promotion, and no push.