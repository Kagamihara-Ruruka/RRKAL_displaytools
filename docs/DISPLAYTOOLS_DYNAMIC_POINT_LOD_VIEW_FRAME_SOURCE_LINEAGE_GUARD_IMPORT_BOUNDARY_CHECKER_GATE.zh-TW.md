# Dynamic Point LOD View-Frame Source-Lineage Guard Import-Boundary Checker Gate

## 目的

本 gate 建立 `source_lineage_guard_contract` 的專用 AST import-boundary checker。它保護未來 `render_core/dynamic_point_source_lineage_guard_boundary.py` helper 只能承載 source identity、lineage guard、raw/row transitional label 與 stop-line ledger，不得偷渡 runtime、renderer、formula、real source、source mutation、c_1 直連或 c_4/Odoriba bypass。

本 gate 是 checker creation only，不建立 helper，不修改 `render_core`，不修改 runtime probe，不修改 `taichi_global_bathymetry.py`，也不改 existing checker 行為。

## Evidence read

- `tests/test_displaytools_dynamic_point_lod_view_frame_source_lineage_guard_import_boundary_checker_planning.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_source_lineage_guard_contract_planning.py`
- `scripts/validate_displaytools_dynamic_point_computed_but_hidden_import_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_computed_but_hidden_import_boundary.py`
- `docs/DOCS_INDEX.zh-TW.md`

## Checker behavior

Checker path:

```text
scripts/validate_displaytools_dynamic_point_source_lineage_guard_import_boundary.py
```

Default target:

```text
render_core/dynamic_point_source_lineage_guard_boundary.py
```

Behavior:

- AST-only
- target imported = false
- target executed = false
- missing target passes as `not_applicable_candidate_missing`
- syntax error returns JSON fail with nonzero exit
- checks `ast.Import`, `ast.ImportFrom`, `ast.Name`, `ast.Attribute`, `ast.Call`, `ast.FunctionDef`, `ast.AsyncFunctionDef`, `ast.ClassDef`
- `--self-test-negative` covers all forbidden families
- clean synthetic candidate passes
- allowed string-label sample passes
- executable reference using allowed label vocabulary fails

## Missing target behavior

When `render_core/dynamic_point_source_lineage_guard_boundary.py` is missing, checker returns:

```text
candidate_exists = false
status = not_applicable_candidate_missing
boundary_passed = true
violations = []
```

This gate does not create `render_core/dynamic_point_source_lineage_guard_boundary.py`.

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

These labels pass only as string data. The same vocabulary fails as executable names, function/class declarations, calls, or attributes.

## Forbidden family coverage

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

## Controlled raw-row seam treatment

The checker allows `controlled_raw_row_compatibility_seam` as a string label. It does not authorize runtime use of a raw/row seam.

The boundary remains:

- controlled raw/row compatibility seam may exist as transitional compatibility label
- controlled raw/row compatibility seam must not mutate source identity
- controlled raw/row compatibility seam must not become direct c_1 integration
- controlled raw/row compatibility seam must remain future c_4/Odoriba handoff material
- raw-row seam runtime authorization = false

## c_4/Odoriba mediation boundary

This checker blocks direct c_3-to-c_1 integration vocabulary and c_4/Odoriba bypass vocabulary as executable references. It preserves future c_4/Odoriba language mediation as the required path for cross-organ integration.

## Decision output

- `source_lineage_guard_import_boundary_checker_created = true`
- `target_imported = false`
- `target_executed = false`
- `missing_target_passes = true`
- `syntax_error_json_fail = true`
- `negative_self_test_passed = true`
- `allowed_string_label_distinction_preserved = true`
- `helper_creation_authorized = false`
- `runtime_execution_authorized = false`
- `source_lineage_mutation_authorized = false`
- `direct_c1_integration_authorized = false`
- `c4_odoriba_bypass_authorized = false`
- `controlled_raw_row_compatibility_seam_label_allowed = true`
- `controlled_raw_row_compatibility_seam_runtime_authorized = false`

## Recommended next gate

```text
dynamic_point_lod_view_frame_source_lineage_guard_minimal_extraction_planning_gate
```

## Boundary statement

Tooling/test/docs-only dynamic point LOD view-frame source-lineage guard import-boundary checker gate. Checker creation only; no helper creation, no `render_core/dynamic_point_source_lineage_guard_boundary.py` creation, no `render_core` behavior change, no runtime probe change, no `taichi_global_bathymetry.py` change, no existing checker behavior change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no formula movement, no real AIS/ADS-B/SQL/WebSocket/cache/database read, no source-lineage mutation, no hidden-as-missing interpretation, no reduced-count-as-source-loss interpretation, no occluded-as-source-loss interpretation, no raw-row seam runtime authorization, no raw-row seam promotion to mature c_1 integration, no direct c_3-to-c_1 dependency authorization, no c_4/Odoriba bypass, no transparent-globe leak inference, no correctness or visual parity claim, no readiness claim, no leak-fix claim, no RRKAL-wide methodology promotion, and no push.
