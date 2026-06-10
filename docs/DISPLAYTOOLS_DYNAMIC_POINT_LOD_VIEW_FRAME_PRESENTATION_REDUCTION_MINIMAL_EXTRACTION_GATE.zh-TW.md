# Dynamic Point LOD View-Frame Presentation Reduction Minimal Extraction Gate

## 目的

本 gate 建立 `presentation_reduction` 最小 descriptor / contract / ledger helper，將 `rendered_count < visible_count` 冷卻成可維護語意面。此 helper 只描述語意，不代表 source loss、frame truth、renderer/frame/projection/mask/formula 行為，也不宣稱 correctness、readiness 或 performance。

## Files created

- `render_core/dynamic_point_presentation_reduction_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_presentation_reduction_boundary_helpers.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_PRESENTATION_REDUCTION_MINIMAL_EXTRACTION_GATE.zh-TW.md`

## Helper summary

Helper module：

```text
render_core/dynamic_point_presentation_reduction_boundary.py
```

此 module 僅使用 stdlib `__future__`，不 import monolith、runtime probe、pandas、NumPy、Datashader、Taichi、PyQt、VisPy、Matplotlib、renderer、frame buffer、real source、SQL/cache/database 或 formula helper。

所有 helper output 只允許 nested `dict`、`list`、scalar。

## Exact helper names

- `build_dynamic_point_presentation_reduction_candidate_descriptor`
- `build_dynamic_point_rendered_lower_than_visible_contract_descriptor`
- `build_dynamic_point_presentation_reduction_sampling_reference_descriptor`
- `build_dynamic_point_presentation_reduction_source_guard_descriptor`
- `build_dynamic_point_presentation_reduction_stop_line_ledger`
- `dynamic_point_presentation_reduction_boundary_descriptor`
- `dynamic_point_presentation_reduction_planning_bundle`

## Semantic assertions

- `rendered_count < visible_count` is classified as `presentation_or_sampling_reduction_candidate`.
- `rendered_count < visible_count` is not source loss.
- `rendered_count < visible_count` is not frame truth.
- `rendered_count < visible_count` is not transparent-globe leak inference.
- `rendered_count < visible_count` is not visual correctness.
- `rendered_count < visible_count` is not readiness.
- `rendered_count < visible_count` is not performance claim.
- `presentation_count_boundary_reference` is a string data reference, not runtime dependency.
- `sampling_visibility_boundary_reference` is a string data reference, not formula dependency.
- `source_lineage_guarded_by_source_lineage_guard_boundary` keeps source lineage impact as none / guarded / no mutation.
- `frame_visible_not_observed` remains a stop-line label.

## Checker result

Dedicated checker：

```text
scripts\validate_displaytools_dynamic_point_presentation_reduction_import_boundary.py
```

Expected result for the new helper：PASS.

The helper is deliberately compatible with the checker by keeping allowed labels as string data and avoiding executable references to those labels.

## Forbidden interpretation summary

The helper does not authorize or claim:

- runtime execution
- runtime probe change
- `render_if_needed`
- controller / renderer / GUI / frame buffer read
- artifact generation
- projection / mask / sampling / alpha-compose formula movement
- real AIS / ADS-B / SQL / WebSocket / cache / database read
- source-lineage mutation
- source-loss interpretation
- frame-truth claim
- transparent-globe leak inference or fix claim
- correctness or visual parity claim
- readiness claim
- performance claim
- c_4/Odoriba bypass

## Decision output

```text
presentation_reduction_minimal_extraction_passed = true
helper_created = true
checker_passed = true
dict_list_scalar_only = true
runtime_execution_authorized = false
source_lineage_mutation_authorized = false
source_loss_interpretation_authorized = false
frame_truth_claim_authorized = false
transparent_globe_leak_inferred = false
transparent_globe_leak_fix_claimed = false
visual_correctness_claimed = false
readiness_claimed = false
performance_claimed = false
c4_odoriba_bypass_authorized = false
```

## Boundary statement

Minimal descriptor, contract, and ledger-only dynamic point LOD view-frame presentation reduction extraction gate. No checker modification, no runtime probe change, no `taichi_global_bathymetry.py` change, no existing `render_core` helper change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no projection, mask, sampling, or alpha-compose formula movement, no real AIS/ADS-B/SQL/WebSocket/cache/database read, no source-lineage mutation, no source-loss interpretation, no frame-truth claim, no transparent-globe leak inference or fix claim, no correctness or visual parity claim, no readiness claim, no performance claim, no c_4/Odoriba bypass, and no push.
