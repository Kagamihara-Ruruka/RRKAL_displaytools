# Layer Render Plan Residual Packet Surfaces Movement Preimplementation Gate

## Scope

This is a tooling/docs-only movement preimplementation gate for a possible future helper module:

- Future candidate path: `render_core/layer_render_plan_residual_packet_surfaces.py`
- Current physical owner: `render_core/render_plan.py`

No helper module is created in this slice and no source is moved.

## Future helper family

The future checker boundary corresponds to these packet/list helpers:

- `build_layer_render_plan_runtime_snapshot`
- `select_layer_render_plan_composition_input`
- `build_layer_render_plan_style_postprocess_packet`
- `build_layer_render_plan_composition_timing_packet`
- `build_layer_render_plan_composition_steps`
- `build_layer_render_plan_batch_decisions`

Explicitly excluded:

- `alpha_compose`
- `alpha_blend_compose`
- `alpha_compose_transparent`
- `build_layer_render_plan_apply_path`

## Allowed future ownership

A future helper may own dict/list/scalar residual packet construction only.

String labels such as `alpha_blend`, `runtime_blend`, `apply_helper`, `HybridRenderController.apply_layer_render_plan_composition`, and `future_unified_taichi_render_plan` may remain as packet data when they preserve existing behavior. These labels do not authorize imports, callable references, controller access, pixel operations, or runtime execution.

## Forbidden dependencies

The import-boundary checker rejects:

- monolith/controller imports or direct controller/runtime class and method references
- Qt, VisPy, Taichi, numpy, pandas, datashader, and pyais dependencies
- `render_core.render_plan` imports
- alpha helper dependencies
- `build_layer_render_plan_apply_path`
- extracted sibling helper module imports
- metadata sidecar writer or artifact writer dependencies
- provider, source, loader, fetch, download, or cache lifecycle module dependencies
- parser or normalizer imports
- existing policy helper modules/classes

## Movement requirements

Before any future physical movement:

1. `tests.test_layer_render_plan_residual_packet_surfaces` must pass before and after.
2. `tests.test_layer_render_plan_residual_packet_surfaces_import_boundary` must pass.
3. `scripts/validate_layer_render_plan_residual_packet_surfaces_import_boundary.py` must pass on the candidate helper module.
4. Source-map and smoke-visible ownership must be updated if physical source ownership changes.
5. Alpha helpers and `build_layer_render_plan_apply_path` must remain excluded unless a separate o_1-reviewed gate authorizes a different slice.

## Boundary Statement

Tooling/docs-only residual packet surfaces import-boundary checker and movement preimplementation gate. No helper module creation, no source movement, no alpha/apply path behavior test or change, no controller/renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no pixel-equivalence/performance/readiness claim.
