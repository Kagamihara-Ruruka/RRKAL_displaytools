# Dynamic Point Post Computed-But-Hidden Next Bridge Selection Gate

## Gate 結論

本 gate 只做下一個安山岩橋接層選擇，不建立 helper、不建立 checker、不修改 `render_core`。根據 post-computed-but-hidden cartography，下一個最值得進入 planning 的語意面是 `source_lineage_guard_contract`。

## Candidate comparison matrix

| candidate | classification | selectability | runtime risk | formula risk | frame / renderer risk | dependency-cycle risk | next action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `source_lineage_guard_contract` | preferred andesite guard contract candidate | selected | low | low | low | reduces cycle risk across extracted surfaces | select for contract planning |
| `occlusion_responsibility_contract` | andesite candidate near mask formula boundary | deferred | medium | medium | medium | overlaps mask and hidden contracts | defer until source lineage guard is planned |
| `mask_visibility_contract` | andesite candidate partly covered by sampling visibility | deferred | low | medium | low | overlaps occlusion contract | defer until guard boundary is selected |
| `presentation_reduction_contract` | andesite candidate partly covered by presentation count | deferred | low | low | low | low | defer as lower entropy than source guard |
| `frame_visibility_stop_line_closure` | granite stop-line candidate | granite stop-line | high | medium | high | near frame runtime | defer to stop-line route |
| `transparent_globe_leak_fault_review` | granite fault review stop-line candidate | granite stop-line | high | medium | high | near fault and visual claims | defer to fault review route |

## Selection reason

`source_lineage_guard_contract` protects the three extracted andesite surfaces:

- `sampling_visibility_boundary`
- `presentation_count_boundary`
- `computed_but_hidden_boundary`

It directly reduces dependency-cycle risk by preventing hidden, reduced, or occluded states from drifting into source-loss interpretation. It does not need runtime, frame buffer, renderer, controller, `render_if_needed`, or formula movement.

## Deferred candidates

- `occlusion_responsibility_contract`: useful, but should wait until source lineage guard planning is explicit.
- `mask_visibility_contract`: useful, but mask hidden must not become source deletion.
- `presentation_reduction_contract`: already partly cooled, but lower urgency than the shared source guard.

## Granite stop-line candidates

- `frame_visibility_stop_line_closure`: remains blocked by frame / renderer / `render_if_needed` risk.
- `transparent_globe_leak_fault_review`: remains blocked because leak behavior is not inferred and no fix claim is allowed.

## Decision output

- `next_bridge_selection_passed = true`
- `selected_next_bridge_candidate = source_lineage_guard_contract`
- `deferred_candidate_count = 3`
- `granite_stop_line_candidate_count = 2`
- `dependency_cycle_watch_enabled = true`
- `source_lineage_guard_priority_reviewed = true`
- `runtime_execution_authorized = false`
- `helper_creation_authorized = false`
- `checker_creation_authorized = false`
- `recommended_next_gate = dynamic_point_lod_view_frame_source_lineage_guard_contract_planning_gate`

## Boundary statement

Docs/test-only dynamic point post-computed-but-hidden next bridge selection gate. No helper creation, no checker creation, no `render_core` change, no runtime probe change, no `taichi_global_bathymetry.py` change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no formula movement, no hidden-as-missing interpretation, no source-lineage-loss interpretation, no transparent-globe leak inference, no correctness or visual parity claim, no readiness claim, no leak-fix claim, no RRKAL-wide methodology promotion, and no push.

## Final classification

`c3_displaytools_dynamic_point_post_computed_but_hidden_next_bridge_selection_gate_committed_for_o1_review_no_push`
