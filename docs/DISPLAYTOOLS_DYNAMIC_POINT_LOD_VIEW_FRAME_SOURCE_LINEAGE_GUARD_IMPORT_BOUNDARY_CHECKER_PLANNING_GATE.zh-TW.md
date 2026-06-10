# Dynamic Point LOD View-Frame Source-Lineage Guard Import-Boundary Checker Planning Gate

## 目的

本 gate 只規劃 `source_lineage_guard_contract` 的專用 import-boundary checker。目標是讓未來 helper 可以保護 dynamic point 的 source identity 與 lineage guard，但不能偷渡 runtime、renderer、frame buffer、formula、real source、跨器官接管，或把 hidden、reduced、occluded 狀態解釋成 source loss。

本 gate 不建立 checker，不建立 helper，不修改 `render_core`，不修改 runtime probe，也不碰 `taichi_global_bathymetry.py`。

## Evidence read

- `tests/test_displaytools_dynamic_point_lod_view_frame_source_lineage_guard_contract_planning.py`
- `tests/test_displaytools_dynamic_point_post_computed_but_hidden_next_bridge_selection.py`
- `tests/test_displaytools_dynamic_point_post_computed_but_hidden_cartography_update.py`
- `scripts/validate_displaytools_dynamic_point_computed_but_hidden_import_boundary.py`
- `docs/DOCS_INDEX.zh-TW.md`
- Static scan over `taichi_global_bathymetry.py`, `render_core`, `tests`, `docs`, and `scripts` for source lineage, raw/row, renderer, controller, frame, and source-loss vocabulary

## Future targets

Future helper target, planned only:

```text
render_core/dynamic_point_source_lineage_guard_boundary.py
```

Future checker target, planned only:

```text
scripts/validate_displaytools_dynamic_point_source_lineage_guard_import_boundary.py
```

## Checker planning summary

The future checker must be AST-only. It must not import or execute the target. Missing target must pass as `not_applicable_candidate_missing`. Syntax error must return JSON fail with nonzero exit. The planned AST coverage is:

- `ast.Import`
- `ast.ImportFrom`
- `ast.Name`
- `ast.Attribute`
- `ast.Call`
- `ast.FunctionDef`
- `ast.AsyncFunctionDef`
- `ast.ClassDef`

Allowed labels may pass only as string data. The same vocabulary must fail when used as executable names, functions, classes, calls, or attributes. The future negative self-test must cover every forbidden family.

## Allowed string labels

- `source_present_token`
- `source_label`
- `point_id`
- `source_lineage_integrity_token`
- `payload_identity_guard`
- `sampling_does_not_mutate_source`
- `presentation_count_does_not_mutate_source`
- `hidden_visibility_does_not_mutate_source`
- `mask_visibility_does_not_mutate_source`
- `occlusion_visibility_does_not_mutate_source`
- `reduced_count_is_not_source_loss`
- `hidden_is_not_missing`
- `occluded_is_not_source_lineage_loss`
- `controlled_raw_row_compatibility_seam`
- `developmental_compensation_surface`
- `future_c4_odoriba_handoff_material`
- `direct_c1_integration_not_authorized`

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
- `real_ais_adsb_source`
- `source_lineage_mutation`
- `hidden_as_missing_interpretation`
- `reduced_count_as_source_loss_interpretation`
- `occluded_as_source_loss_interpretation`
- `direct_c1_integration`
- `c4_odoriba_bypass`
- `transparent_globe_leak_inference`
- `correctness_claim`
- `visual_parity_claim`
- `readiness_claim`
- `transparent_globe_leak_fix_claim`
- `label_executable_reference`

## Controlled raw/row compatibility seam treatment

This gate recognizes that a controlled raw/row compatibility seam may exist as a transitional c_3 surface. That recognition is not a maturity claim and not a direct c_1 integration authorization.

The seam treatment is fixed as:

- `controlled_raw_row_compatibility_seam_recognized = true`
- `classification = transitional_c3_developmental_compensation_surface`
- `raw_row_compatibility_seam_must_not_mutate_source_identity = true`
- `raw_row_compatibility_seam_must_not_become_direct_c1_integration = true`
- `raw_row_compatibility_seam_remains_future_c4_odoriba_handoff_material = true`
- `direct_c1_integration_authorized = false`
- `c4_odoriba_mediation_required_for_future_cross_organ_integration = true`
- `mature_architecture_claimed = false`

## Decision output

- `source_lineage_guard_checker_planning_passed = true`
- `dedicated_checker_required = true`
- `existing_checker_reusable = false`
- `helper_creation_authorized = false`
- `checker_creation_authorized = false`
- `runtime_execution_authorized = false`
- `source_lineage_mutation_authorized = false`
- `controlled_raw_row_compatibility_seam_recognized = true`
- `direct_c1_integration_authorized = false`
- `c4_odoriba_mediation_required_for_future_cross_organ_integration = true`
- `transparent_globe_leak_inferred = false`
- `dependency_cycle_watch_enabled = true`

## Recommended next gate

```text
dynamic_point_lod_view_frame_source_lineage_guard_import_boundary_checker_gate
```

## Boundary statement

Docs/test-only dynamic point LOD view-frame source-lineage guard import-boundary checker planning gate. No checker creation, no helper creation, no `render_core` change, no runtime probe change, no `taichi_global_bathymetry.py` change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no formula movement, no real AIS/ADS-B/SQL/WebSocket/cache/database read, no source-lineage mutation, no hidden-as-missing interpretation, no reduced-count-as-source-loss interpretation, no occluded-as-source-loss interpretation, no raw-row compatibility seam promotion to mature c_1 integration, no direct c_3-to-c_1 dependency authorization, no c_4/Odoriba bypass, no transparent-globe leak inference, no correctness or visual parity claim, no readiness claim, no leak-fix claim, no RRKAL-wide methodology promotion, and no push.
