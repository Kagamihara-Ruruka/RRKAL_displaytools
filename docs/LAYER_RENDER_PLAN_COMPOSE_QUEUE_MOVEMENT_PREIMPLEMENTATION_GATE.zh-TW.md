# Layer Render Plan Compose Queue Movement Preimplementation Gate

## TL;DR

This gate defines the import boundary for a possible future compose queue helper module:

- candidate path: `render_core/layer_render_plan_compose_queue.py`
- current status: candidate module is not created in this slice
- validator: `scripts/validate_layer_render_plan_compose_queue_import_boundary.py`

The checker is a static AST validator. It does not import or execute the target module.

## Candidate future module

Proposed only:

- `render_core/layer_render_plan_compose_queue.py`

Allowed future behavior:

- pure dict/list helpers only
- no controller object
- no ndarray object
- no artifact path
- no metadata sidecar writer
- no runtime merge enablement
- no pixel equivalence claim

## Missing candidate behavior

Because the candidate helper module does not exist yet, the checker must treat the default target as not applicable:

- `candidate_exists=false`
- `status=not_applicable_candidate_missing`
- `boundary_passed=true`
- exit code `0`

This behavior only means there is no candidate file to validate yet. It does not approve movement.

## Forbidden dependencies

The future helper must not import or reference renderer/controller symbols:

- `taichi_global_bathymetry`
- `HybridRenderController`
- `TaichiGlobeRenderer`
- `QtHybridWindow`
- `VisPyHybridViewer`

It must not import runtime/UI/GPU families:

- `taichi`
- `PyQt6`
- `PySide6`
- `vispy`

It must not import pixel/ndarray/datashader families:

- `numpy`
- `pandas`
- `datashader`
- `render_core.render_plan`
- `alpha_compose`
- `alpha_blend_compose`
- `alpha_compose_transparent`
- `merge_alpha_compose_overlay_run`
- `apply_layer_render_plan_composition`
- `apply_layer_render_plan_merged_candidate_composition`

It must not import artifact or metadata writers:

- `render_core.preview`
- `write_preview_frame_png`
- `render_core.metadata`
- `build_renderer_output_metadata_payload`
- `write_compose_parity_artifacts`

It must not import parser, normalizer, provider, source, or cache modules:

- `render_core.dataframe_normalizers`
- `normalize_ais_frame`
- `normalize_aircraft_frame`
- `dataframe_from_text`
- `dataframe_from_json`
- `dataframe_from_jsonl`
- `dataframe_from_geojson`
- `dataframe_from_nmea`
- provider/source/loader/fetch/download/cache module keywords

It must not import sibling policy classes:

- `PointOverlayBudgetPolicy`
- `DatashaderSamplingPolicy`
- `LayerRenderBudgetPolicy`
- `AdaptiveRenderQualityPolicy`

Important boundary:

- `render_core.render_plan` is currently a mixed surface. It contains pure packet helpers, but it also imports `numpy` and contains alpha composition helpers.
- A future compose queue helper must not import back from `render_core.render_plan`.
- If queue packet movement is later authorized, required pure dependencies must move with the queue helper or receive their own reviewed boundary gate.

## Before/after requirements for any future movement

Before any movement:

1. `tests.test_layer_render_plan_compose_queue` must pass.
2. The import-boundary checker must pass on the candidate helper path.
3. The candidate helper must remain pure dict/list logic.
4. The candidate helper must not introduce controller, renderer, UI, ndarray, artifact, metadata, parser, normalizer, provider, or sibling-policy dependencies.

After any future movement:

1. The monolith diff must be limited to import/delegation if movement is authorized later.
2. The queue fixture gate must pass before and after.
3. Generated artifact audit must remain clean.
4. Metadata schema and output behavior must remain unchanged.
5. Runtime merge must remain disabled unless separately authorized.

## Not authorized in this slice

- helper module creation
- compose queue source movement
- controller method movement
- renderer hot path change
- alpha/ndarray behavior change
- artifact writer change
- metadata writer change
- output behavior change
- runtime merge enablement

## Boundary statement

Tooling/docs-only movement preimplementation gate. No candidate helper module creation, no compose queue extraction, no controller instantiation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output behavior change, no runtime merge enablement, and no pixel-equivalence claim.
