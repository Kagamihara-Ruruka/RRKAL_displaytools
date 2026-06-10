# Dynamic Point Post Computed-But-Hidden Cartography Update Gate

## Gate 結論

本 gate 只更新 dynamic point LOD / view-frame 海圖，不新增 helper、不新增 checker、不修改 `render_core`。`computed_but_hidden_boundary` 已納入已抽離安山岩語意面，並與既有 `sampling_visibility_boundary`、`presentation_count_boundary` 並列為可維護 descriptor / contract / ledger surface。

## 已抽離安山岩語意面

- `sampling_visibility_boundary`: 承載 `sampled_visible_token`、`visible_count_observation`、`rendered_count_observation`、`mask_visible_token`、`source_lineage_integrity_token`。
- `presentation_count_boundary`: 承載 `visible_count`、`rendered_count`、`rendered_lower_than_visible`、`sampling_or_presentation_reduction_candidate`，且不推論 source loss。
- `computed_but_hidden_boundary`: 承載 `source_present_token`、`computed_point_token`、`hidden_visibility_token`、`hidden_is_not_missing`、`occluded_is_not_source_lineage_loss`、`transparent_globe_leak_not_inferred`。

## Granite stop-line inventory

- `frame_visibility_surface`: frame visibility 仍未觀測。
- `transparent_globe_leak_fault`: transparent globe leak 仍未推論，也未修復。
- `controller_renderer_frame_buffer_runtime`: controller、renderer、frame buffer 仍是 runtime stop-line。
- `render_if_needed_runtime`: `render_if_needed` 仍不可呼叫。
- `projection_mask_sampling_formula_surfaces`: projection、mask、sampling、alpha-compose 公式仍不可搬移。

## Remaining candidate matrix

- `source_lineage_guard_contract`: 可進入下一輪 selection，但需避免把 hidden 或 occluded 解釋成 source loss。
- `occlusion_responsibility_contract`: 可進入下一輪 selection，但 mask / formula / frame truth 必須保持阻擋。
- `mask_visibility_contract`: 可進入下一輪 selection，但只能保留 mask-visible label contract。
- `presentation_reduction_contract`: 可進入下一輪 selection，但 `rendered_count < visible_count` 只能保留為 reduction candidate。
- `frame_visibility_stop_line_closure`: 保留 stop-line closure route，不作為安山岩抽離候選。
- `transparent_globe_leak_fault_review`: 保留 fault review route，不作為安山岩抽離候選。

## Decision output

- `cartography_update_passed = true`
- `computed_but_hidden_boundary_registered = true`
- `extracted_andesite_surface_count = 3`
- `remaining_andesite_candidate_count = 4`
- `granite_stop_line_count = 5`
- `dependency_cycle_watch_enabled = true`
- `next_bridge_selection_required = true`
- `recommended_next_gate = dynamic_point_lod_view_frame_post_computed_but_hidden_next_bridge_selection_gate`

## Boundary statement

Docs/test-only dynamic point post-computed-but-hidden cartography update gate. No helper creation, no checker creation, no `render_core` change, no runtime probe change, no `taichi_global_bathymetry.py` change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no formula movement, no hidden-as-missing interpretation, no source-lineage-loss interpretation, no transparent-globe leak inference, no correctness or visual parity claim, no readiness claim, no leak-fix claim, no RRKAL-wide methodology promotion, and no push.

## Final classification

`c3_displaytools_dynamic_point_post_computed_but_hidden_cartography_update_gate_committed_for_o1_review_no_push`
