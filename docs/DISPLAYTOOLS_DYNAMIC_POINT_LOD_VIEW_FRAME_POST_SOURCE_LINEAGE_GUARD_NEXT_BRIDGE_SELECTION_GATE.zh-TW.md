# Dynamic Point LOD View-Frame Post Source-Lineage Guard Next Bridge Selection Gate

## 目標

本 gate 在 `source_lineage_guard_boundary` 已入冊後，從剩餘三塊主線安山岩中選出下一個可切 bridge。這是 docs/test-only selection，不建立 helper、不建立 checker、不修改 `render_core`、不碰 runtime。

## Evidence read

- `tests/test_displaytools_dynamic_point_source_lineage_guard_cartography_update.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_SOURCE_LINEAGE_GUARD_CARTOGRAPHY_UPDATE_GATE.zh-TW.md`
- `render_core/dynamic_point_source_lineage_guard_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_source_lineage_guard_boundary_helpers.py`
- `render_core/dynamic_point_sampling_visibility_boundary.py`
- `render_core/dynamic_point_presentation_count_boundary.py`
- `render_core/dynamic_point_computed_but_hidden_boundary.py`
- sampling visibility runtime interpretation evidence
- frame visibility stop-line planning evidence
- occlusion responsibility boundary evidence
- source-lineage guard contract planning evidence

## Extracted inventory

Extracted inventory remains four surfaces:

- `sampling_visibility_boundary`
- `presentation_count_boundary`
- `computed_but_hidden_boundary`
- `source_lineage_guard_boundary`

The source-lineage guard now reduces source-loss drift for all remaining mainline candidates.

## Candidate comparison matrix

Compared exactly these three remaining candidates:

- `occlusion_responsibility_contract`
- `mask_visibility_contract`
- `presentation_reduction_contract`

Each candidate records:

- `runtime_risk`
- `formula_risk`
- `frame_stop_line_risk`
- `dependency_cycle_risk`
- `source_loss_drift_guarded_by`
- `recommended_status`

## Selection decision

Selected candidate:

```text
presentation_reduction_contract
```

Reason:

- It has the lowest runtime risk.
- It has the lowest formula risk.
- It does not require frame visibility, renderer, mask formula, or occlusion runtime.
- It clarifies `rendered_count < visible_count` as presentation or sampling reduction without source loss.
- It is not a complete duplicate of `presentation_count_boundary` because the next planning gate can narrow the reduction semantics independently while reusing the existing count evidence.

## Deferred candidates

Deferred:

- `occlusion_responsibility_contract`
  - Reason: semantically important, but closer to mask/frame/leak stop-line surfaces.
  - Stop condition: do not select if mask formula, frame visibility, renderer, or leak inference is required.
- `mask_visibility_contract`
  - Reason: near mask formula and occlusion overlap.
  - Stop condition: do not select if mask formula movement is required.

## Granite stop-line

`frame_visibility_surface` is classified as:

```text
granite_stop_line
```

It is not an andesite candidate in this gate. Frame visibility, renderer, frame buffer, `render_if_needed`, and transparent-globe leak behavior remain out of scope.

## Decision output

- `next_bridge_selection_passed = true`
- `extracted_inventory_count = 4`
- `remaining_candidate_count = 3`
- `frame_visibility_surface_classification = granite_stop_line`
- `selected_next_bridge_candidate = presentation_reduction_contract`
- `deferred_candidates = occlusion_responsibility_contract, mask_visibility_contract`
- `source_lineage_guard_reduces_source_loss_drift_for_all_candidates = true`
- `presentation_reduction_not_complete_duplicate = true`
- `runtime_execution_authorized = false`
- `helper_creation_authorized = false`
- `checker_creation_authorized = false`
- `formula_movement_authorized = false`
- `transparent_globe_leak_inferred = false`
- `readiness_claimed = false`

## Recommended next gate

```text
dynamic_point_lod_view_frame_presentation_reduction_contract_planning_gate
```

## Boundary statement

Docs/test-only dynamic point post-source-lineage-guard next bridge selection gate. No helper creation, no checker creation, no `render_core` change, no runtime/probe/renderer/frame/formula/source behavior change, no c_4/Odoriba bypass, no source-loss/leak/correctness/readiness claim, and no push.