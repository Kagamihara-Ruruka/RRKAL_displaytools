# Dynamic Point LOD View-frame Computed-But-Hidden Contract Planning Gate

## Gate scope

This gate plans a future `computed_but_hidden_contract` helper candidate. It is docs/test-only and does not create a helper, checker, runtime adapter, probe expansion, renderer path, frame-buffer read, or formula movement.

The planning question is narrow: a dynamic point can be source-present and computed, while still hidden from visibility. Hidden is not missing, and occluded is not source-lineage loss.

## Evidence read

- `tests/test_displaytools_dynamic_point_lod_view_frame_post_presentation_count_next_bridge_selection.py`
- `tests/test_displaytools_dynamic_point_presentation_count_cartography_update.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_boundary_helpers.py`
- `tests/test_displaytools_dynamic_point_occlusion_responsibility_boundary.py`
- `tests/test_displaytools_dynamic_point_grafting_path_minimal_evidence.py`
- `tests/test_displaytools_dynamic_point_view_frame_occlusion_structure_settlement.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_frame_visibility_stop_line_planning.py`
- Static scan terms for computed, hidden, missing, occluded, source lineage, frame visibility, transparent globe, renderer, mask, and presentation count surfaces.

## Planned targets

| Target | Status |
|---|---|
| `render_core/dynamic_point_computed_but_hidden_boundary.py` | planned only |
| `scripts/validate_displaytools_dynamic_point_computed_but_hidden_import_boundary.py` | planned only |

Helper creation and checker creation are not authorized by this gate.

## Contract labels

- `source_present_token`
- `computed_point_token`
- `hidden_visibility_token`
- `frame_visible_not_observed`
- `hidden_is_not_missing`
- `occluded_is_not_source_lineage_loss`
- `computed_but_hidden_contract`
- `transparent_globe_leak_not_inferred`

## Stop-line ledger

- Frame visibility is not observed.
- Frame buffer read is blocked.
- Renderer execution is blocked.
- Transparent globe leak is not inferred.
- Source loss is not inferred.

## Planning matrix summary

| Surface | Allowed role | Forbidden interpretation |
|---|---|---|
| `source_present_token` | lineage presence label | visibility hidden does not delete source |
| `computed_point_token` | computed presence label | computed does not claim coordinate correctness |
| `hidden_visibility_token` | hidden visibility label | hidden is not missing |
| `frame_visible_not_observed` | stop-line label | frame truth is not claimed |
| `hidden_is_not_missing` | semantic guard label | hidden as missing |
| `occluded_is_not_source_lineage_loss` | source-lineage guard label | occluded as source lineage loss |
| `transparent_globe_leak_not_inferred` | fault stop-line label | transparent globe leak inference or fix |

## Decision output

- `computed_but_hidden_contract_planning_gate_passed = true`
- `computed_but_hidden_helper_candidate_supported = true`
- `descriptor_contract_ledger_candidate = true`
- `helper_creation_authorized = false`
- `checker_creation_authorized = false`
- `render_core_change_authorized = false`
- `runtime_probe_change_authorized = false`
- `taichi_global_bathymetry_change_authorized = false`
- `render_if_needed_authorized = false`
- `controller_renderer_frame_buffer_authorized = false`
- `artifact_generation_authorized = false`
- `formula_movement_authorized = false`
- `hidden_as_missing_authorized = false`
- `source_lineage_loss_interpretation_authorized = false`
- `transparent_globe_leak_inferred = false`
- `coordinate_correctness_claimed = false`
- `visual_parity_claimed = false`
- `readiness_claimed = false`
- `transparent_globe_leak_fix_claimed = false`
- `rrkal_wide_methodology_authorized = false`

## Recommended next gate

`dynamic_point_lod_view_frame_computed_but_hidden_import_boundary_checker_planning_gate`

## Boundary statement

Docs/test-only dynamic point LOD view-frame computed-but-hidden contract planning gate. No helper creation, no checker creation, no `render_core` change, no runtime probe change, no `taichi_global_bathymetry` change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no formula movement, no hidden-as-missing interpretation, no source-lineage-loss interpretation, no transparent-globe leak inference, no correctness/visual parity/readiness/leak-fix claim, no RRKAL-wide methodology promotion, and no push.

## Final classification

`c3_displaytools_dynamic_point_lod_view_frame_computed_but_hidden_contract_planning_gate_committed_for_o1_review_no_push`