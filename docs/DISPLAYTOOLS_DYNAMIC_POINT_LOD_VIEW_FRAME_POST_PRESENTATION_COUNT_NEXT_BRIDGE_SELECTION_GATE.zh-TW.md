# Dynamic Point LOD View-Frame Post-Presentation-Count Next Bridge Selection Gate

## Gate 範圍

本 gate 在 presentation count helper 已完成抽離並更新海圖後，重新選擇下一個 dynamic point andesite bridge 目標。

本 gate 只做 docs/test-only 選擇判斷，不建立 helper，不建立 checker，不修改 `render_core`，不修改 runtime probe，不碰 `taichi_global_bathymetry.py`，也不碰 `render_if_needed`、controller、renderer、frame buffer、artifact writer 或公式。

## Evidence read

- `docs/DISPLAYTOOLS_DYNAMIC_POINT_PRESENTATION_COUNT_CARTOGRAPHY_UPDATE_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_presentation_count_cartography_update.py`
- `render_core/dynamic_point_presentation_count_boundary.py`
- `render_core/dynamic_point_sampling_visibility_boundary.py`
- `tests/test_displaytools_dynamic_point_occlusion_responsibility_boundary.py`
- `tests/test_displaytools_dynamic_point_view_frame_occlusion_structure_settlement.py`
- `tests/test_displaytools_dynamic_point_grafting_path_minimal_evidence.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_frame_visibility_stop_line_planning.py`

## Candidate comparison summary

重新比較七個候選：

- `computed_but_hidden_contract`
- `occlusion_responsibility_contract`
- `source_lineage_guard_contract`
- `projection_shadow_interface_contract`
- `frame_visibility_stop_line_closure`
- `transparent_globe_leak_fault_review`
- `presentation_count_contract_followup`

## Selected candidate

```text
computed_but_hidden_contract
```

選擇理由：

- presentation count 已經完成抽離，不能再重複打一艘已沉的船。
- `computed_but_hidden_contract` 可以把「點仍然存在且可能已計算，但被 presentation / occlusion 隱藏」固定成資料合約。
- 這個合約不需要讀 frame buffer，不需要 renderer，不需要 `render_if_needed`，不需要公式移動。
- 它能繼續強化「hidden 不是 missing」與「occluded 不是 source lineage loss」這兩條防線。

## Deferred candidates

- `presentation_count_contract_followup`: 已抽離，暫不重打。
- `source_lineage_guard_contract`: 已有 source lineage helper 與 guard 語意，暫作既有防線。
- `occlusion_responsibility_contract`: 很有價值，但更靠近 mask / alpha / frame seam，先延後。
- `projection_shadow_interface_contract`: 屬於 core-interface-only，不是這輪 andesite extraction target。
- `frame_visibility_stop_line_closure`: 需要 frame authorization，暫不進入。
- `transparent_globe_leak_fault_review`: 仍是 unresolved fault review，不進行 leak inference 或 fix claim。

## Decision output

```text
post_presentation_count_next_bridge_selection_gate_passed = true
candidate_matrix_defined = true
candidate_count = 7
presentation_count_already_extracted = true
selected_candidate = computed_but_hidden_contract
selected_candidate_suitable_as_next_gate = true
rejected_or_deferred_count = 6
frame_visibility_remains_stop_line = true
transparent_globe_leak_not_inferred = true
source_loss_interpretation_authorized = false
production_source_change_authorized = false
helper_creation_authorized = false
checker_creation_authorized = false
runtime_probe_change_authorized = false
render_if_needed_authorized = false
controller_renderer_frame_buffer_authorized = false
artifact_generation_authorized = false
formula_movement_authorized = false
coordinate_correctness_claimed = false
visual_parity_claimed = false
readiness_claimed = false
transparent_globe_leak_fix_claimed = false
rrkal_wide_methodology_authorized = false
```

## Recommended next gate

```text
dynamic_point_lod_view_frame_computed_but_hidden_contract_planning_gate
```

下一步應先規劃 computed-but-hidden 的 contract helper 與 import-boundary checker，不直接進入 renderer、frame 或透明地球 leak surface。

## Boundary statement

Docs/test-only dynamic point LOD view-frame post-presentation-count next bridge selection gate. No helper creation, no checker creation, no `render_core` change, no runtime probe change, no `taichi_global_bathymetry` change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no formula movement, no source-loss interpretation, no transparent-globe leak inference, no correctness/visual parity/readiness/leak-fix claim, no RRKAL-wide methodology promotion, and no push.
