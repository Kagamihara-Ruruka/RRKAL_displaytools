# Dynamic Point LOD View-Frame Source-Lineage Guard Minimal Extraction Gate

## 目標

本 gate 建立 `source_lineage_guard` 的最小可維護語意 helper，將 dynamic point source identity / lineage guard 冷卻為 descriptor / contract / ledger-only surface。此 helper 保護 sampling、presentation count、computed-hidden、mask、occlusion 與 raw-row compatibility seam，不讓這些 visibility 或 presentation 狀態污染 source identity。

## Files changed

- `render_core/dynamic_point_source_lineage_guard_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_source_lineage_guard_boundary_helpers.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_SOURCE_LINEAGE_GUARD_MINIMAL_EXTRACTION_GATE.zh-TW.md`
- `docs/DOCS_INDEX.zh-TW.md`

## Helper summary

新增 helper 是 data-only boundary。它只輸出 nested `dict`、`list`、scalar values。它不 import monolith、不 import runtime / renderer / dataframe / real-source libraries、不讀 frame buffer、不呼叫 formula、不寫 artifact。

## Exact helper names

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

## Source identity invariants

- `source_present_token` means source presence, not frame visibility.
- `source_label` is lineage label, not mature c_1 asset object.
- `point_id` is identity token, not renderer identity.
- `source_lineage_integrity_token` must remain stable across sampling, presentation count, hidden visibility, mask visibility, and occlusion visibility labels.
- sampling does not mutate source.
- presentation count does not mutate source.
- hidden visibility does not mutate source.
- mask visibility does not mutate source.
- occlusion visibility does not mutate source.
- reduced count is not source loss.
- hidden is not missing.
- occluded is not source-lineage loss.

## Raw-row seam treatment

The helper recognizes these labels:

- `controlled_raw_row_compatibility_seam`
- `developmental_compensation_surface`
- `future_c4_odoriba_handoff_material`

These are label / ledger / handoff material only. They do not authorize runtime execution, real source reads, mature c_1 integration, direct c_3-to-c_1 dependency, or c_4/Odoriba bypass.

## c_4/Odoriba mediation boundary

- `c4_odoriba_mediation_required = true`
- `direct_c1_integration_authorized = false`
- `direct_c3_to_c1_dependency_authorized = false`
- `c4_odoriba_bypass_authorized = false`

Future cross-organ integration remains mediated by c_4/Odoriba.

## Decision output

- `source_lineage_guard_minimal_extraction_passed = true`
- `helper_created = true`
- `checker_passed = true`
- `dict_list_scalar_only = true`
- `runtime_execution_authorized = false`
- `source_lineage_mutation_authorized = false`
- `controlled_raw_row_compatibility_seam_label_allowed = true`
- `controlled_raw_row_compatibility_seam_runtime_authorized = false`
- `direct_c1_integration_authorized = false`
- `c4_odoriba_mediation_required = true`
- `c4_odoriba_bypass_authorized = false`
- `dependency_cycle_watch_enabled = true`

## Forbidden interpretation summary

- hidden is not missing.
- reduced count is not source loss.
- occluded is not source-lineage loss.
- raw-row compatibility seam is not runtime authorization.
- raw-row compatibility seam is not mature c_1 integration.
- direct c_3-to-c_1 dependency remains unauthorized.
- c_4/Odoriba bypass remains unauthorized.
- transparent-globe leak is not inferred.
- correctness, visual parity, readiness, and leak fix are not claimed.
- This is not promoted into RRKAL-wide methodology.

## Checker result

Required checker:

```text
scripts/validate_displaytools_dynamic_point_source_lineage_guard_import_boundary.py
```

Expected target:

```text
render_core/dynamic_point_source_lineage_guard_boundary.py
```

The helper is intended to pass the checker as descriptor / contract / ledger-only data.

## Recommended next gate

```text
dynamic_point_source_lineage_guard_cartography_update_gate
```

## Boundary statement

Minimal descriptor, contract, and ledger-only dynamic point LOD view-frame source-lineage guard extraction gate. No checker modification, no runtime probe change, no `taichi_global_bathymetry.py` change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no formula movement, no real AIS/ADS-B/SQL/WebSocket/cache/database read, no source-lineage mutation, no hidden-as-missing interpretation, no reduced-count-as-source-loss interpretation, no occluded-as-source-loss interpretation, no raw-row seam runtime authorization, no raw-row seam promotion to mature c_1 integration, no direct c_3-to-c_1 dependency authorization, no c_4/Odoriba bypass, no transparent-globe leak inference, no correctness or visual parity claim, no readiness claim, no leak-fix claim, no RRKAL-wide methodology promotion, and no push.
