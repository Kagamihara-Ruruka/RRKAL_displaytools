# Dynamic Point LOD View-frame Computed-But-Hidden Import-Boundary Checker Planning Gate

## Gate scope

This gate plans the dedicated AST import-boundary checker for a future computed-but-hidden helper. It does not create the checker, does not create the helper, and does not change `render_core`, runtime probe code, existing checker scripts, or `taichi_global_bathymetry.py`.

The planned checker protects one semantic boundary: hidden is not missing, and occluded is not source-lineage loss. Frame, renderer, alpha-compose, formula, source, and leak surfaces remain blocked.

## Evidence read

- `tests/test_displaytools_dynamic_point_lod_view_frame_computed_but_hidden_contract_planning.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_post_presentation_count_next_bridge_selection.py`
- `tests/test_displaytools_dynamic_point_presentation_count_cartography_update.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_boundary_helpers.py`
- `tests/test_displaytools_dynamic_point_occlusion_responsibility_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_frame_visibility_stop_line_planning.py`
- `scripts/validate_displaytools_dynamic_point_presentation_count_import_boundary.py` as pattern reference only
- Required static scan for computed-but-hidden labels, frame, renderer, controller, alpha-compose, source-lineage-loss, and missing surfaces.

## Future targets, planned only

| Target | Status |
|---|---|
| `render_core/dynamic_point_computed_but_hidden_boundary.py` | planned only |
| `scripts/validate_displaytools_dynamic_point_computed_but_hidden_import_boundary.py` | planned only |

Checker creation and helper creation are not authorized by this gate.

## Allowed labels

- `source_present_token`
- `computed_point_token`
- `hidden_visibility_token`
- `frame_visible_not_observed`
- `hidden_is_not_missing`
- `occluded_is_not_source_lineage_loss`
- `computed_but_hidden_contract`
- `transparent_globe_leak_not_inferred`
- `source_loss_not_inferred`
- `frame_buffer_read_blocked`
- `renderer_execution_blocked`
- `readiness_not_claimed`

These labels may pass only as string data. The same labels must fail if used as executable names, functions, classes, calls, or attributes.

## Forbidden families

- `monolith`
- `runtime_probe`
- `render_if_needed`
- `controller_runtime`
- `renderer_runtime`
- `frame_buffer`
- `artifact_writer`
- `projection_formula`
- `mask_formula`
- `sampling_formula_movement`
- `alpha_compose_formula`
- `dataframe_runtime`
- `live_source`
- `cache_database_io`
- `hidden_as_missing_interpretation`
- `source_lineage_loss_interpretation`
- `transparent_globe_leak_inference`
- `correctness_claim`
- `visual_parity_claim`
- `readiness_claim`
- `transparent_globe_leak_fix_claim`
- `label_executable_reference`

## Checker expectations

- AST-only.
- Do not import target.
- Do not execute target.
- Missing target passes as `not_applicable_candidate_missing`.
- Syntax error returns JSON fail with nonzero exit.
- Inspect `ast.Import`, `ast.ImportFrom`, `ast.Name`, `ast.Attribute`, `ast.Call`, `ast.FunctionDef`, `ast.AsyncFunctionDef`, and `ast.ClassDef`.
- Allowed labels pass only as string data.
- Allowed labels fail as executable references.
- Negative self-test must cover every forbidden family.

## Decision output

- `computed_but_hidden_import_boundary_checker_planning_gate_passed = true`
- `future_helper_target_defined = true`
- `future_checker_target_defined = true`
- `allowed_labels_defined = true`
- `forbidden_families_defined = true`
- `checker_expectation_defined = true`
- `missing_target_behavior_defined = true`
- `negative_self_test_expectation_defined = true`
- `checker_creation_authorized = false`
- `helper_creation_authorized = false`
- `render_core_change_authorized = false`
- `existing_checker_modification_authorized = false`
- `runtime_probe_change_authorized = false`
- `taichi_global_bathymetry_change_authorized = false`
- `render_if_needed_authorized = false`
- `controller_renderer_frame_buffer_authorized = false`
- `artifact_generation_authorized = false`
- `formula_movement_authorized = false`
- `hidden_as_missing_authorized = false`
- `source_lineage_loss_interpretation_authorized = false`
- `transparent_globe_leak_inference_authorized = false`
- `coordinate_correctness_claimed = false`
- `visual_parity_claimed = false`
- `readiness_claimed = false`
- `transparent_globe_leak_fix_claimed = false`
- `rrkal_wide_methodology_authorized = false`

## Recommended next gate

`dynamic_point_lod_view_frame_computed_but_hidden_import_boundary_checker_gate`

## Boundary statement

Docs/test-only dynamic point LOD view-frame computed-but-hidden import-boundary checker planning gate. No checker creation, no helper creation, no `render_core` change, no existing checker modification, no runtime probe change, no `taichi_global_bathymetry` change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no formula movement, no hidden-as-missing interpretation, no source-lineage-loss interpretation, no transparent-globe leak inference, no correctness/visual parity/readiness/leak-fix claim, no RRKAL-wide methodology promotion, and no push.

## Final classification

`c3_displaytools_dynamic_point_lod_view_frame_computed_but_hidden_import_boundary_checker_planning_gate_committed_for_o1_review_no_push`