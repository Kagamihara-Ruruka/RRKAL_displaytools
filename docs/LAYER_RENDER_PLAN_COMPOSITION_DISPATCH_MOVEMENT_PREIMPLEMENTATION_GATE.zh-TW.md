# Layer Render Plan Composition Dispatch Movement Preimplementation Gate

## TL;DR

This gate defines the import boundary for a possible future composition dispatch helper module:

- candidate path: `render_core/layer_render_plan_composition_dispatch.py`
- current status: candidate module is not created in this slice
- validator: `scripts/validate_layer_render_plan_composition_dispatch_import_boundary.py`

The checker is a static AST validator. It does not import or execute the target module.

## Candidate future module

Proposed only:

- `render_core/layer_render_plan_composition_dispatch.py`

Target symbols if a later source movement is authorized:

- `build_layer_render_plan_composition_apply_action`
- `build_layer_render_plan_composition_dispatch_packet`

Allowed future behavior:

- pure dict packet labels only
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

It must not import ndarray/pixel/dataframe/datashader families:

- `numpy`
- `pandas`
- `datashader`
- `pyais`
- `render_core.render_plan`
- `alpha_compose`
- `alpha_blend_compose`
- `alpha_compose_transparent`

It must not import compose queue helpers:

- `render_core.layer_render_plan_compose_queue`
- `build_layer_render_plan_compose_queue_packet`
- `build_layer_render_plan_compose_queue_entries`
- `build_layer_render_plan_step_runtime_state`
- `build_layer_render_plan_compose_queue_packet_from_states`
- `build_layer_render_plan_compose_runs`
- `build_layer_render_plan_compose_run_parity_contract`

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

## Before/after requirements for any future movement

Before any movement:

1. `tests.test_layer_render_plan_composition_dispatch` must pass.
2. The import-boundary checker must pass on the candidate helper path.
3. The candidate helper must remain pure dict packet label logic.
4. The candidate helper must not introduce controller, renderer, UI, ndarray, artifact, metadata, parser, normalizer, provider, queue-helper, or sibling-policy dependencies.

After any future movement:

1. The source diff must be limited to import/re-export or direct helper movement.
2. The dispatch fixture gate must pass before and after.
3. Generated artifact audit must remain clean.
4. Metadata schema and output behavior must remain unchanged.
5. Runtime merge must remain disabled unless separately authorized.

## Not authorized in this slice

- helper module creation
- composition dispatch source movement
- controller method movement
- renderer hot path change
- alpha/ndarray behavior change
- artifact writer change
- metadata writer change
- output behavior change
- runtime merge enablement

## Boundary statement

Tooling/docs-only movement preimplementation gate. No candidate helper module creation, no composition dispatch extraction, no controller instantiation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output behavior change, no runtime merge enablement, and no pixel-equivalence/performance/readiness claim.
