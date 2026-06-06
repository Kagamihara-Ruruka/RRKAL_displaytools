# PointOverlayBudgetPolicy Fixture Parity Gate

## TL;DR

This gate locks the current `PointOverlayBudgetPolicy.decision()` and `PointOverlayBudgetPolicy.text()` behavior with focused fixtures before any future policy movement is discussed.

This is a test/docs gate only. It does not authorize policy extraction, renderer movement, performance claims, output behavior changes, visual parity claims, UI readiness claims, or runtime merge.

## Static evidence

Target:

- `taichi_global_bathymetry.py:5242` in the current file.
- Class: `PointOverlayBudgetPolicy`.
- Methods: `decision()`, `text()`.

Observed dependencies:

- Inputs are scalar values and a plain `decisions` dict for `text()`.
- No renderer/controller object is accepted.
- No Qt, VisPy, or Taichi runtime reference is observed in the class body.
- No file/cache/artifact read or write is observed.
- No metadata schema or output image behavior is touched.
- `style_profile` is not observed in the current method signature; layer id is copied into output as a string.

## Fixture matrix

| fixture | expected branch / behavior |
| --- | --- |
| low record count under budget | `full-quality`, `sample_ratio_cap=1.0`, not dense |
| sparse record count drag over budget | `drag-over-budget`, sparse, `sample_ratio_cap=0.35` |
| medium record count drag over budget | `drag-over-budget`, dense, `sample_ratio_cap=0.18` |
| high record count drag over budget | very dense, `sample_ratio_cap=0.10` |
| steady over-budget dense | `steady-over-budget-dense`, `sample_ratio_cap=0.35` |
| steady over-budget very dense | `steady-over-budget-very-dense`, `sample_ratio_cap=0.22` |
| global large canvas dense under budget | `global-large-canvas`, `sample_ratio_cap=0.55` |
| regional large canvas dense under budget | remains `full-quality` |
| interaction large canvas under budget | `drag-large-canvas`, sparse cap `0.65`, dense cap `0.40` |
| boundary/equality at `target_ms * 1.08` | not over budget because implementation uses `>` |
| `render_ms=None` and negative point count | coerces current ms to `0.0`, point count to `0`, keeps full quality |
| deterministic repeat call | same input returns the same output dict |
| decision output keys | exact key set is pinned |
| text output | exact split-line order is pinned, including heading, blank lines, rule line, layer section order, point formatting, pressure formatting, sample cap formatting, and interaction flag |

## Current fixture evidence

Focused tests exist in `tests/test_point_overlay_budget_policy.py`.

They prove only that the current policy object behavior is observable through import-level fixtures. They do not prove renderer behavior, output image behavior, metadata behavior, UI behavior, or performance improvement.

## False-leaf warnings

- `PointOverlayBudgetPolicy` looks like a low-risk policy object, but fixture parity does not approve extraction.
- Future movement still needs an import-boundary checker for the target helper module.
- Future movement must preserve exact branch ordering, equality behavior, output keys, and text wording unless o_1 approves a behavior change.
- Do not combine this with `LayerRenderBudgetPolicy`, compose execution, metadata schema, or renderer timing work in the same slice.

## Recommended next step

If this gate is accepted, the next low-risk step is one of:

1. Add a policy import-boundary checker for a future policy helper module.
2. Add a docs-only preimplementation gate for `PointOverlayBudgetPolicy` helper movement.

Current follow-up evidence:

- `scripts\validate_policy_import_boundary.py` defines the standalone AST import-boundary checker.
- `docs\POINT_OVERLAY_BUDGET_POLICY_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md` records the movement preimplementation gate.

Do not extract the policy in the same checkpoint as this fixture gate.

## Boundary statement

Test/docs-only PointOverlayBudgetPolicy fixture parity gate. No policy extraction, no packet builder extraction, no renderer/Qt/Taichi runtime execution, no metadata/output behavior change, no performance claim, no visual parity readiness claim.
