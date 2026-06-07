# Layer Render Plan Residual Packet Surfaces Movement Preimplementation Gate

## Scope

This gate has been consumed by the minimal movement slice for the residual packet helper module:

- Current helper path: `render_core/layer_render_plan_residual_packet_surfaces.py`
- Compatibility owner: `render_core/render_plan.py` imports and re-exports these symbols.

The movement was limited to the covered dict/list/scalar packet helpers. It did not include alpha helpers or `build_layer_render_plan_apply_path`.

## Moved helper family

The checker boundary corresponds to these packet/list helpers:

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

## Allowed ownership

The helper may own dict/list/scalar residual packet construction only.

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

For this physical ownership split and any later adjustment:

1. `tests.test_layer_render_plan_residual_packet_surfaces` must pass.
2. `tests.test_layer_render_plan_residual_packet_surfaces_import_boundary` must pass.
3. `scripts/validate_layer_render_plan_residual_packet_surfaces_import_boundary.py` must pass on `render_core/layer_render_plan_residual_packet_surfaces.py`.
4. Source-map and smoke-visible ownership must be updated if physical source ownership changes.
5. Alpha helpers and `build_layer_render_plan_apply_path` must remain excluded unless a separate o_1-reviewed gate authorizes a different slice.

## Boundary Statement

Residual packet surfaces movement gate consumed by minimal helper extraction. No alpha/apply path behavior test or change, no controller/renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no pixel-equivalence/performance/readiness claim.
