# Dynamic Point LOD View-frame Presentation Count Minimal Extraction Gate

## Gate scope

This gate creates `render_core/dynamic_point_presentation_count_boundary.py` as a minimal descriptor, contract, and ledger helper for presentation count semantics.

The helper owns only cooled labels and contract packets for `visible_count`, `rendered_count`, `rendered_lower_than_visible`, source-lineage guard status, and frame/leak stop-line ledgers. It does not move runtime behavior, projection formula, mask formula, sampling formula, renderer behavior, frame buffer state, or artifact writing.

## Evidence read

- `scripts/validate_displaytools_dynamic_point_presentation_count_import_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_presentation_count_minimal_extraction_planning.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_presentation_count_import_boundary.py`
- `docs/DOCS_INDEX.zh-TW.md`

## Helpers introduced

- `build_dynamic_point_visible_count_contract_descriptor`
- `build_dynamic_point_rendered_count_contract_descriptor`
- `build_dynamic_point_presentation_reduction_candidate_descriptor`
- `build_dynamic_point_presentation_count_source_lineage_guard_descriptor`
- `build_dynamic_point_presentation_count_stop_line_ledger`
- `dynamic_point_presentation_count_boundary_descriptor`
- `dynamic_point_presentation_count_planning_bundle`

## Helper summary

| Helper | Role | Boundary |
|---|---|---|
| `build_dynamic_point_visible_count_contract_descriptor` | Records `visible_count` and `visible_count_observation` as presentation count contract fields. | Not source completeness. |
| `build_dynamic_point_rendered_count_contract_descriptor` | Records `rendered_count` and `rendered_count_observation` as presentation count contract fields. | Not frame truth. |
| `build_dynamic_point_presentation_reduction_candidate_descriptor` | Records `rendered_lower_than_visible` as `sampling_or_presentation_reduction_candidate`. | Not source loss. |
| `build_dynamic_point_presentation_count_source_lineage_guard_descriptor` | Records `source_lineage_integrity_token` as guard-only semantics. | No source mutation. |
| `build_dynamic_point_presentation_count_stop_line_ledger` | Records `frame_visible_not_observed` and `transparent_globe_leak_not_inferred`. | No leak inference or leak fix. |
| `dynamic_point_presentation_count_boundary_descriptor` | Records helper-wide owned labels and blocked actions. | Descriptor, contract, and ledger only. |
| `dynamic_point_presentation_count_planning_bundle` | Bundles helper outputs and non-authorization flags. | No runtime, formula, renderer, frame, source-loss, or readiness authorization. |

## Required labels retained as data

- `visible_count`
- `rendered_count`
- `visible_count_observation`
- `rendered_count_observation`
- `rendered_lower_than_visible`
- `sampling_or_presentation_reduction_candidate`
- `presentation_count_contract`
- `source_lineage_integrity_token`
- `source_loss_not_inferred`
- `frame_visible_not_observed`
- `transparent_globe_leak_not_inferred`
- `visual_correctness_not_claimed`
- `readiness_not_claimed`

All labels are data strings or dictionary keys, not executable references.

## Semantic decisions

- `visible_count` is a contract field, not source completeness.
- `rendered_count` is a contract field, not frame truth.
- `rendered_count < visible_count` remains only a reduction candidate.
- Reduction candidate semantics do not infer source loss.
- `frame_visible_not_observed` does not infer transparent globe leak behavior.
- `transparent_globe_leak_not_inferred` is not a leak fix claim.
- The helper does not claim visual correctness, coordinate correctness, readiness, visual parity, or safe extraction.

## Checker result expectation

The helper is expected to pass `scripts/validate_displaytools_dynamic_point_presentation_count_import_boundary.py render_core\dynamic_point_presentation_count_boundary.py` because it is AST-only safe data and does not import or call monolith, runtime, renderer, frame buffer, dataframe, formula, writer, live source, or cache/database surfaces.

## Boundary statement

Minimal descriptor, contract, and ledger-only dynamic point LOD view-frame presentation count extraction gate. No checker modification, no runtime probe change, no `taichi_global_bathymetry.py` change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no projection, mask, or sampling formula movement, no source-loss interpretation, no transparent globe leak inference, no coordinate or visual correctness claim, no visual parity claim, no readiness claim, no leak-fix claim, no RRKAL-wide methodology promotion, and no push.

## Final classification

`c3_displaytools_dynamic_point_lod_view_frame_presentation_count_minimal_extraction_gate_committed_for_o1_review_no_push`
