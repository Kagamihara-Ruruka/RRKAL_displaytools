# Layer Render Plan Residual Packet Surfaces Fixture Parity Gate

## Scope

This is a test/docs-only fixture parity gate for the remaining non-alpha, non-apply-path packet surfaces in `render_core/render_plan.py`.

Covered helpers:

- `build_layer_render_plan_runtime_snapshot`
- `select_layer_render_plan_composition_input`
- `build_layer_render_plan_style_postprocess_packet`
- `build_layer_render_plan_composition_timing_packet`
- `build_layer_render_plan_composition_steps`
- `build_layer_render_plan_batch_decisions`

Explicitly excluded helpers:

- `alpha_compose`
- `alpha_blend_compose`
- `alpha_compose_transparent`
- `build_layer_render_plan_apply_path`

## Fixture Matrix

| Surface | Evidence pinned | Boundary |
| --- | --- | --- |
| Runtime snapshot | Exact key set, frame index coercion, visible layer count, dirty flag passthrough, batch target order, compose order, false runtime optimization flag | `single_pass_target` remains a future label only |
| Composition input selector | `None`, malformed, `compose_queue`, and `composition_steps` branches | Selects existing data only; no composition execution |
| Style postprocess packet | Exact key set, style profile passthrough, `apply_helper` label, false runtime optimization flag | Pixel postprocess remains outside this gate |
| Composition timing packet | Numeric coercion, 3-decimal rounding, non-numeric skip, default phase totals, input order | Timing packet only; no performance readiness claim |
| Composition steps | Boundary-layer selected path, boundary aggregate path, fixed layer order, style postprocess always present | Step list only; no alpha formula test |
| Batch decisions | Clean reuse, global dirty, dirty flag branches, invalidation scope, postprocess decision, malformed entry skip | Decision packet only; no batch execution |
| Bundle-level guards | Deterministic repeat calls, dict/list/scalar output, excluded helper names kept out, no runtime merge or pixel-equivalence claim | No source movement |

## False-Leaf Warnings

- `composition_steps` includes alpha and runtime labels as data, but this gate does not test alpha behavior.
- `batch_decisions` names rebuild/reuse decisions, but it does not validate renderer cache lifecycle or batch execution.
- `runtime_snapshot` includes `single_pass_target`, but that remains a future label only.
- `style_postprocess_packet` includes `apply_helper`, but the label is not executed.
- `composition_timing_packet` normalizes measured numbers, but it does not authorize performance readiness.

## Required Validation

```powershell
py -3 -m unittest tests.test_layer_render_plan_residual_packet_surfaces
py -3 -m unittest tests.test_layer_render_plan_compiled_reused_packets
py -3 -m unittest tests.test_layer_render_plan_adapter_preflight
py -3 -m unittest tests.test_generated_artifact_audit
py -3 -B scripts\generated_artifact_audit_leaf_provider.py
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\inspect_render_plan_compose_source_map.ps1
git diff --check
```

Full smoke is not required for this fixture-only slice unless source-map or smoke-visible contracts change.

## Boundary Statement

Test/docs-only residual render_plan packet surface fixture gate. No source movement, no helper module creation, no alpha/apply path behavior test or change, no controller/renderer/Qt/VisPy/Taichi runtime execution, no metadata sidecar writer change, no artifact writer execution, no metadata/output schema change, no runtime merge enablement, and no pixel-equivalence/performance/readiness claim.
