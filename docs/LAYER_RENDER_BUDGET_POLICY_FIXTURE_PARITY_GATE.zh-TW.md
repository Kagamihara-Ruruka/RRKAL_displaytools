# LayerRenderBudgetPolicy Fixture Parity Gate

## TL;DR

This gate locks the current `LayerRenderBudgetPolicy.decision()` and `LayerRenderBudgetPolicy.text()` behavior with focused fixtures before any future policy movement is discussed.

Cut-out note: No monolith source extracted in this slice.

This is a test/docs gate only. It does not authorize policy extraction, helper creation, renderer movement, performance claims, output behavior changes, visual parity claims, UI readiness claims, or runtime merge.

## Static evidence

Target:

- `taichi_global_bathymetry.py:5086` in the current file.
- Class: `LayerRenderBudgetPolicy`.
- Methods: `decision()`, `text()`.

Observed dependencies:

- Inputs are scalar canvas size, render timing, lod, target fps, interaction flag, and a layer visibility map.
- Global dependency: `LAYER_RENDER_COSTS`.
- Local class registry: `VECTOR_LAYER_IDS`.
- No renderer/controller object is accepted.
- No Qt, VisPy, or Taichi runtime reference is observed in the class body.
- No file/cache/artifact read or write is observed.
- No metadata schema or output image behavior is touched.

## Fixture matrix

| fixture | expected branch / behavior |
| --- | --- |
| warming-up timing | `render_ms=None` yields `state="warming-up"` and default vector cache quantum |
| under-budget static layers | static visible cost is summed and no vector deferral/cache preference is selected |
| over-budget vector layers | visible/vector costs from `LAYER_RENDER_COSTS` select static cache preference |
| regional over-budget vector layers | regional/local non-interactive static-cache branch uses vector point stride `2` |
| dragging over budget | interaction plus vector over-budget branch defers vector overlays |
| heavy canvas interaction without vector cost | over-budget interaction plus heavy canvas but no vector cost uses `0.18` / `0.014` / stride `4` |
| global heavy canvas | within-budget global heavy canvas uses global vector quantum |
| unknown visible layer | unknown layer cost falls back to `1` |
| decision output keys | exact key set is pinned |
| deterministic repeat call | same input returns same output |
| text output | split-line order, numeric formatting, boolean wording, and rule line are pinned |

## Current fixture evidence

Focused tests exist in `tests/test_layer_render_budget_policy.py`.

They prove only that the current policy object behavior is observable through import-level fixtures. They do not prove renderer behavior, output image behavior, metadata behavior, UI behavior, or performance improvement.

## False-leaf warnings

- `LayerRenderBudgetPolicy` is higher risk than `PointOverlayBudgetPolicy` and `DatashaderSamplingPolicy` because it depends on the global `LAYER_RENDER_COSTS` map.
- Future movement would need to move, duplicate, or rebuild `LAYER_RENDER_COSTS` in a reviewed way.
- Fixture parity does not approve extraction.
- Do not combine this with renderer timing, compose execution, metadata schema, or output behavior work in the same slice.

## Recommended next step

If this gate is accepted, the next low-risk step is a movement preimplementation gate or import-boundary checker for a future `LayerRenderBudgetPolicy` helper module.

Do not extract the policy in the same checkpoint as this fixture gate.

## Boundary statement

Test/docs-only LayerRenderBudgetPolicy fixture parity gate. No policy extraction, no helper module creation, no renderer/Qt/Taichi runtime execution, no metadata/output behavior change, no performance claim, no visual parity readiness claim.
