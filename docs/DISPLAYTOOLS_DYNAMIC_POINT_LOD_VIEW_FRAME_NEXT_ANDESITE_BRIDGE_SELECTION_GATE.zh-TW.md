# Dynamic Point LOD View-frame Next Andesite Bridge Selection Gate

## Gate 性質

本 gate 只做下一刀候選選擇。Sampling / visibility 小邊界已經抽離，本 gate 比較剩餘 dynamic point surface，選出下一個最合理的安山岩橋接層候選，並明確排除仍屬地核、花崗岩或 frame stop-line 的 surface。

本 gate 不新增 helper，不新增 checker，不修改 `render_core`，不修改 runtime probe，不碰 `taichi_global_bathymetry.py`。

## Evidence read

- sampling visibility cartography update
- sampling visibility minimal boundary
- frame visibility stop-line planning
- sampling visibility runtime probe result interpretation
- occlusion responsibility boundary
- view-frame occlusion structure settlement
- grafting path minimal evidence
- projection interface shadow gate
- earlier dynamic point cartography gates

## Candidate comparison matrix summary

| candidate | classification | risk | blast radius | next action |
| --- | --- | --- | --- | --- |
| `presentation_count_contract` | andesite bridge descriptor / contract candidate | low | small | select for next gate |
| `source_lineage_guard_contract` | already guarded descriptor / contract surface | low | small | defer as already guarded |
| `computed_but_hidden_contract` | andesite bridge contract candidate | medium | small | defer as already guarded |
| `occlusion_responsibility_contract` | andesite bridge contract candidate near runtime seam | medium | medium | defer as already guarded |
| `projection_shadow_interface_contract` | core interface only | medium high | medium | defer as projection interface only |
| `frame_visibility_stop_line_closure` | not observed frame stop-line | high | large | defer until frame authorization |
| `transparent_globe_leak_fault_review` | unresolved not inferred fault | high | large | defer as fault review |

## Selected next andesite bridge candidate

Selected candidate:

```text
presentation_count_contract
```

Selection reason:

- It has direct second-probe evidence for `visible_count_observation` and `rendered_count_observation`.
- It can be described as descriptor / contract / ledger data.
- It does not need renderer, controller, frame buffer, or `render_if_needed`.
- It does not need projection, mask, or sampling formula movement.
- It does not need correctness, visual parity, readiness, or leak-fix claims.
- Its expected blast radius is small.
- It continues reducing dynamic point local decomposition entropy after the sampling / visibility helper extraction.

## Rejected or deferred candidates

- `source_lineage_guard_contract`: deferred because source lineage already has guard evidence and is not the next entropy reducer.
- `computed_but_hidden_contract`: deferred because it depends on frame-visible stop-line language and should follow presentation count contract.
- `occlusion_responsibility_contract`: deferred because it is closer to mask / alpha / frame seams.
- `projection_shadow_interface_contract`: deferred because it is core interface only and must not move projection formulas.
- `frame_visibility_stop_line_closure`: deferred because it would pressure frame buffer, renderer, controller, or `render_if_needed`.
- `transparent_globe_leak_fault_review`: deferred because leak behavior is not inferred and no fix claim is allowed.

## Decision output

```text
next_andesite_bridge_selection_gate_passed = true
candidate_matrix_defined = true
candidate_count = 7
selected_candidate = presentation_count_contract
selected_candidate_suitable_as_next_gate = true
rejected_or_deferred_count = 6
frame_visibility_remains_stop_line = true
transparent_globe_leak_not_inferred = true
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
dynamic_point_lod_view_frame_presentation_count_contract_planning_gate
```

## Boundary statement

Docs/test-only dynamic point LOD view-frame next andesite bridge selection gate. No helper creation, no checker creation, no render_core change, no runtime probe change, no taichi_global_bathymetry change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no formula movement, no correctness/visual parity/readiness/leak-fix claim, no RRKAL-wide methodology promotion, and no push.