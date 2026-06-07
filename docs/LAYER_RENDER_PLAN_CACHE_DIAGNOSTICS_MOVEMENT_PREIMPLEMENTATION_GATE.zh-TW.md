# Layer Render Plan Cache Diagnostics Movement Preimplementation Gate

## TL;DR

This gate defines the static import boundary for the cache diagnostics helper module.

- helper path: `render_core/layer_render_plan_cache_diagnostics.py`
- current status: helper module created by the minimal cache diagnostics movement slice
- validator: `scripts/validate_layer_render_plan_cache_diagnostics_import_boundary.py`

The checker uses Python AST parsing only. It does not import or execute the target module.

## Candidate module

Current helper module:

- `render_core/layer_render_plan_cache_diagnostics.py`

Moved symbols:

- `build_layer_render_plan_cache_key`
- `build_layer_render_plan_cache_invalidation_reasons`
- `build_layer_render_plan_cache_invalidation_scope`
- `build_layer_render_plan_metadata_summary`

Allowed future behavior:

- pure dict/list/scalar cache diagnostics logic only
- JSON cache-key string building
- invalidation reason and scope packet construction
- metadata summary packet construction without writer behavior
- no controller object
- no artifact path
- no metadata sidecar writer
- no runtime merge enablement
- no output-behavior claim

## Missing candidate behavior

When a synthetic missing path is supplied, the checker must treat it as not applicable:

- `candidate_exists=false`
- `status=not_applicable_candidate_missing`
- `boundary_passed=true`
- exit code `0`

This behavior only means there is no candidate file at that path. It does not approve additional movement.

## Consumed movement status

The minimal movement slice moved only pure cache diagnostics helpers. `render_core/render_plan.py` keeps import/re-export compatibility for existing callers.

No compiled plan packet builder, reused plan packet builder, metadata sidecar writer, artifact writer, controller method, renderer hot path, or runtime behavior moved in this slice.

## Cache word versus cache lifecycle boundary

The future helper may contain `cache` in its module name, function names, local variables, and packet fields.

The checker must not ban the literal word `cache` globally.

The checker does ban module imports that imply provider/source/download/cache lifecycle ownership, such as:

- provider modules
- source loader modules
- fetch/download modules
- cache loader/store/io/writer modules

Pure cache key and invalidation packet logic remains allowed.

## Forbidden dependencies

The future helper must not import or reference renderer/controller symbols:

- `taichi_global_bathymetry`
- `HybridRenderController`
- `TaichiGlobeRenderer`
- `QtHybridWindow`
- `VisPyHybridViewer`

It must not import runtime/UI/GPU/dataframe families:

- `taichi`
- `PyQt6`
- `PySide6`
- `vispy`
- `numpy`
- `pandas`
- `datashader`
- `pyais`

It must not import render-plan hot or adjacent helper modules:

- `render_core.render_plan`
- `render_core.layer_render_plan_compose_queue`
- `render_core.layer_render_plan_composition_dispatch`
- `alpha_compose`
- `alpha_blend_compose`
- `alpha_compose_transparent`

It must not import artifact or metadata writers:

- `render_core.preview`
- `write_preview_frame_png`
- `render_core.metadata`
- `build_renderer_output_metadata_payload`
- `write_compose_parity_artifacts`

It must not import parser, normalizer, provider, source, download, or cache lifecycle modules:

- `render_core.dataframe_normalizers`
- `normalize_ais_frame`
- `normalize_aircraft_frame`
- `dataframe_from_text`
- `dataframe_from_json`
- `dataframe_from_jsonl`
- `dataframe_from_geojson`
- `dataframe_from_nmea`
- provider/source/loader/fetch/download/cache-lifecycle module keywords

It must not import sibling policy classes:

- `PointOverlayBudgetPolicy`
- `DatashaderSamplingPolicy`
- `LayerRenderBudgetPolicy`
- `AdaptiveRenderQualityPolicy`

## Before/after requirements for any future movement

Before any movement:

1. `tests.test_layer_render_plan_cache_diagnostics` must pass.
2. The import-boundary checker must pass on the candidate helper path.
3. The candidate helper must remain pure dict/list/scalar logic.
4. The candidate helper must not introduce controller, renderer, UI, ndarray, artifact, metadata writer, parser, normalizer, provider, queue-helper, dispatch-helper, or sibling-policy dependencies.

After any future movement:

1. The source diff must be limited to import/re-export or direct helper movement.
2. The cache diagnostics fixture gate must pass before and after.
3. Generated artifact audit must remain clean.
4. Metadata schema and output behavior must remain unchanged.
5. Runtime merge must remain disabled unless separately authorized.

## Not authorized in this slice

- additional helper module creation
- additional cache diagnostics source movement
- metadata sidecar writer change
- artifact writer change
- controller method movement
- renderer hot path change
- output behavior change
- runtime merge enablement

## Boundary statement

Minimal cache diagnostics movement gate. No additional helper module creation, no additional symbol movement, no metadata sidecar writer change, no artifact writer execution, no controller instantiation, no renderer/Qt/VisPy/Taichi runtime execution, no output schema change, no runtime merge enablement, and no pixel-equivalence/performance/readiness claim.
