# Dynamic Point LOD View-Frame Source-Lineage Guard Minimal Extraction Planning Gate

## 目標

本 gate 規劃 `source_lineage_guard_contract` 的最小 helper extraction。它只定義 future descriptor / contract / ledger helper families，不建立 helper、不修改 checker、不碰 runtime。目標是讓 dynamic point 的 source identity 不被 sampling、presentation、hidden、mask、occlusion 或 raw-row compatibility seam 污染。

## Evidence read

- `tests/test_displaytools_dynamic_point_lod_view_frame_source_lineage_guard_import_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_source_lineage_guard_import_boundary_checker_planning.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_source_lineage_guard_contract_planning.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_boundary_helpers.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_presentation_count_boundary_helpers.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_computed_but_hidden_boundary_helpers.py`
- `docs/DOCS_INDEX.zh-TW.md`
- `scripts/validate_displaytools_dynamic_point_source_lineage_guard_import_boundary.py`

## Future helper target

Planned only:

```text
render_core/dynamic_point_source_lineage_guard_boundary.py
```

本 gate 不建立此 helper。planning test 只驗證 target path 與 authorization decision，不把 future helper 永久不存在寫成 filesystem assertion。

## Required checker

Required checker already exists:

```text
scripts/validate_displaytools_dynamic_point_source_lineage_guard_import_boundary.py
```

Checker protection decision:

- `required_checker_available = true`
- AST-only checker remains the required guard.
- Missing target remains `not_applicable_candidate_missing`.
- Target import / execution remains forbidden.
- Checker modification is not authorized in this gate.

## Planned helper families

- `build_dynamic_point_source_identity_contract_descriptor`
- `build_dynamic_point_source_lineage_integrity_descriptor`
- `build_dynamic_point_payload_identity_guard_descriptor`
- `build_dynamic_point_sampling_source_guard_descriptor`
- `build_dynamic_point_presentation_count_source_guard_descriptor`
- `build_dynamic_point_hidden_visibility_source_guard_descriptor`
- `build_dynamic_point_mask_occlusion_source_guard_descriptor`
- `build_dynamic_point_raw_row_compatibility_seam_descriptor`
- `build_dynamic_point_source_lineage_guard_stop_line_ledger`
- `dynamic_point_source_lineage_guard_boundary_descriptor`
- `dynamic_point_source_lineage_guard_planning_bundle`

Each planned family is descriptor / contract / ledger-only. Helper creation remains unauthorized.

## Output shape decision

Allowed future helper outputs:

- nested `dict`
- `list`
- scalar values

Forbidden future helper outputs:

- callable
- runtime object
- dataframe
- renderer buffer
- file handle
- network object
- SQL/cache object
- live source object
- c_1 object
- c_4/Odoriba object

## Raw-row compatibility seam treatment

The 21k raw/row seam is recognized only as transitional c_3 compensation material:

- `controlled_raw_row_compatibility_seam_label_allowed = true`
- `controlled_raw_row_compatibility_seam_runtime_authorized = false`
- `developmental_compensation_surface_recognized = true`
- `future_c4_odoriba_handoff_material = true`
- `raw_row_seam_promoted_to_mature_c1_integration = false`

This keeps the seam visible as a label / ledger / handoff surface without authorizing direct source reads or c_1 integration.

## c_4/Odoriba mediation boundary

- `c4_odoriba_mediation_required = true`
- `direct_c1_integration_authorized = false`
- `direct_c3_to_c1_dependency_authorized = false`
- `c4_odoriba_bypass_authorized = false`

Future cross-organ integration must pass through c_4/Odoriba mediation. This gate does not authorize c_3 to bind directly to c_1.

## Protected existing surfaces

The planned helper protects these already extracted andesite surfaces from source-loss drift:

- `sampling_visibility_boundary`
- `presentation_count_boundary`
- `computed_but_hidden_boundary`

It also prepares a shared guard for later mask and occlusion contracts without moving formulas or entering renderer/runtime surfaces.

## Decision output

- `source_lineage_guard_minimal_extraction_planning_passed = true`
- `required_checker_available = true`
- `source_lineage_guard_helper_candidate_supported = true`
- `descriptor_contract_ledger_candidate = true`
- `helper_creation_authorized = false`
- `checker_modification_authorized = false`
- `runtime_execution_authorized = false`
- `source_lineage_mutation_authorized = false`
- `controlled_raw_row_compatibility_seam_label_allowed = true`
- `controlled_raw_row_compatibility_seam_runtime_authorized = false`
- `direct_c1_integration_authorized = false`
- `c4_odoriba_mediation_required = true`
- `dependency_cycle_watch_enabled = true`

## Forbidden interpretation summary

- hidden is not missing.
- reduced count is not source loss.
- occluded is not source-lineage loss.
- raw-row compatibility seam is not runtime authorization.
- raw-row compatibility seam is not mature c_1 integration.
- c_4/Odoriba mediation is not optional for future cross-organ integration.
- transparent-globe leak is not inferred.
- correctness, visual parity, readiness, and leak fix are not claimed.
- This remains a c_3 local dynamic point planning surface, not RRKAL-wide methodology.

## Recommended next gate

```text
dynamic_point_lod_view_frame_source_lineage_guard_minimal_extraction_gate
```

## Boundary statement

Docs/test-only dynamic point LOD view-frame source-lineage guard minimal extraction planning gate. No helper creation, no `render_core/dynamic_point_source_lineage_guard_boundary.py` creation, no checker modification, no `render_core` change, no runtime probe change, no `taichi_global_bathymetry.py` change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no formula movement, no real AIS/ADS-B/SQL/WebSocket/cache/database read, no source-lineage mutation, no hidden-as-missing interpretation, no reduced-count-as-source-loss interpretation, no occluded-as-source-loss interpretation, no raw-row seam runtime authorization, no raw-row seam promotion to mature c_1 integration, no direct c_3-to-c_1 dependency authorization, no c_4/Odoriba bypass, no transparent-globe leak inference, no correctness or visual parity claim, no readiness claim, no leak-fix claim, no RRKAL-wide methodology promotion, and no push.
