# Layer Render Plan Composition Dispatch Fixture Parity Gate

## TL;DR

This fixture gate pins the current dict packet behavior of composition action and dispatch helpers in `render_core.render_plan`.

Target helpers:

- `build_layer_render_plan_composition_apply_action`
- `build_layer_render_plan_composition_dispatch_packet`

This gate does not execute composition. Dispatch values are packet labels only; they are not runtime behavior evidence.

## Fixture matrix

| Case | Expected evidence |
| --- | --- |
| unknown kind | `apply_helper=unknown_apply_helper`, dispatch skips with `unknown_apply_action` |
| missing overlay | overlay-required action dispatches `skip` with `missing_overlay` |
| runtime blend | dispatch label is `runtime_blend` and `should_apply=True` when overlay is present |
| alpha blend | dispatch label is `alpha_blend`; blend mode is preserved |
| alpha compose | dispatch label is `alpha_compose` |
| runtime overlay | dispatch label is `runtime_overlay` |
| style postprocess | dispatch label is `style_profile_postprocess` and phase is `postprocess` |
| exact packet key set | top-level dispatch packet keys are pinned |
| deterministic repeat call | same input returns the same action and dispatch packets |
| no execution claim | packet does not report pixel equivalence, visual parity, runtime merge, or performance state |

## Import and runtime boundary

The focused tests import only pure helpers from `render_core.render_plan`.

They do not instantiate:

- `HybridRenderController`
- `TaichiGlobeRenderer`
- `QtHybridWindow`
- `VisPyHybridViewer`

They do not call:

- `apply_layer_render_plan_composition`
- `merge_alpha_compose_overlay_run`
- `apply_layer_render_plan_merged_candidate_composition`
- artifact writers
- metadata sidecar writers

They do not use:

- real overlays
- ndarray pixel buffers
- rendered RGBA frames
- filesystem artifact paths

## What this gate proves

- Action packet mapping from `kind` to helper label is observable without controller state.
- Dispatch packet skip/apply labels are observable without runtime execution.
- Missing overlay and unknown action skip reasons are pinned.
- Style postprocess packet labels remain distinct from overlay composition labels.

## What this gate does not prove

- It does not prove pixel equivalence.
- It does not prove alpha formula behavior.
- It does not prove runtime composition behavior.
- It does not prove metadata sidecar behavior.
- It does not authorize helper movement.
- It does not enable runtime merge.

## Future movement boundary

Before any future movement of these helpers:

1. Keep this fixture gate passing before and after.
2. Add an import-boundary checker if a new helper module is proposed.
3. Keep action/dispatch packet labels separate from execution behavior.
4. Keep composition hot path and artifact writer paths outside this gate.
5. Keep metadata schema and output behavior unchanged.

## Boundary statement

Test/docs-only composition dispatch packet fixture gate. No helper extraction, no controller instantiation, no renderer/Qt/VisPy/Taichi runtime execution, no ndarray alpha formula test/change, no artifact writer execution, no metadata/output behavior change, no runtime merge enablement, and no pixel-equivalence/performance/readiness claim.
