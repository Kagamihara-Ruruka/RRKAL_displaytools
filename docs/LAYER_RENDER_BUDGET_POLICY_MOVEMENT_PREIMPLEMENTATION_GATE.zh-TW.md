# LayerRenderBudgetPolicy Movement Preimplementation Gate

## TL;DR

This gate defines the import-boundary and parity requirements for the reviewed movement of `LayerRenderBudgetPolicy`.

Cut-out note: This gate has been consumed by the minimal movement slice for `LAYER_RENDER_COSTS` and `LayerRenderBudgetPolicy`.

`LAYER_RENDER_COSTS` and `LayerRenderBudgetPolicy` now live together in `render_core/layer_render_budget_policy.py`. This note records the boundary only and does not authorize broader movement.

## Current helper path

Current helper path:

```text
render_core/layer_render_budget_policy.py
```

The candidate file now exists after the reviewed minimal movement. The standalone checker must return `status=pass` with `boundary_passed=true` for this file. The synthetic missing-candidate behavior remains covered by tests using a deliberately absent path.

## LAYER_RENDER_COSTS movement decision

Movement strategy used in this slice:

- `LAYER_RENDER_COSTS` moved into the same helper module as `LayerRenderBudgetPolicy`.

Acceptable alternative for future refactors:

- Move `LAYER_RENDER_COSTS` into a pure constants module such as `render_core/layer_render_costs.py`, but only if that constants module has its own no-renderer import-boundary check.

Forbidden strategy:

- A helper must not import `taichi_global_bathymetry` only to read `LAYER_RENDER_COSTS`.

## Preserved behavior from fixture tests

Future movement must preserve current fixture coverage:

- warming-up branch for missing render timing
- under-budget static layer branch
- over-budget vector static-cache branch
- regional/local static-cache stride branch
- dragging vector deferral branch
- heavy-canvas interaction branch without vector cost
- global heavy-canvas within-budget branch
- unknown layer default cost fallback
- exact `decision()` key set
- deterministic repeat calls
- exact `text().splitlines()` sequence

## Forbidden dependencies

The layer render budget policy helper must not import or depend on:

- renderer/controller modules or state
- Qt, VisPy, or Taichi runtime modules
- preview or artifact writers
- metadata sidecar writers
- provider/source/load/fetch/download/cache modules
- parser functions
- DataFrame normalizer modules
- `pandas`
- `numpy`
- `datashader`
- `pyais`
- `PointOverlayBudgetPolicy`
- `DatashaderSamplingPolicy`
- runtime merge behavior

## Import-boundary checker

Standalone checker:

```powershell
py -3 -B scripts\validate_layer_render_budget_policy_import_boundary.py render_core\layer_render_budget_policy.py
```

Negative self-test:

```powershell
py -3 -B scripts\validate_layer_render_budget_policy_import_boundary.py --self-test-negative
```

The checker uses stdlib AST only. It must not import or execute the target module.

## Before/after parity requirements

For this reviewed movement and any future edits, run:

```powershell
py -3 -m unittest tests.test_layer_render_budget_policy
py -3 -m unittest tests.test_layer_render_budget_policy_import_boundary
py -3 -m unittest tests.test_generated_artifact_audit
py -3 -B scripts\validate_layer_render_budget_policy_import_boundary.py render_core\layer_render_budget_policy.py
py -3 -B scripts\validate_layer_render_budget_policy_import_boundary.py --self-test-negative
py -3 -B scripts\generated_artifact_audit_leaf_provider.py
git diff --check
```

`taichi_global_bathymetry.py` must remain limited to import/delegation or re-export wiring for this policy plus reviewed `LAYER_RENDER_COSTS` handling. Any broader source change requires a separate review.

## Artifact audit requirements

This movement and any future edits must preserve:

- no `state/` artifacts staged or untracked from the task
- no PNG artifacts staged or untracked from the task
- no generated runtime JSON artifacts staged or untracked from the task
- checker stdout JSON only, with no artifact file writes

## Not authorized

- Additional policy extraction beyond `LayerRenderBudgetPolicy`.
- Additional helper module creation beyond `render_core/layer_render_budget_policy.py`.
- Further movement or splitting of `LAYER_RENDER_COSTS` without a new review.
- Renderer runtime behavior change.
- Metadata or output behavior change.
- Performance claim.
- Readiness claim.
- Visual parity claim.
- Runtime merge.

## Boundary statement

Minimal LayerRenderBudgetPolicy movement gate consumed by this slice. No broader policy extraction, no renderer/Qt/Taichi runtime execution, no metadata/output behavior change, no performance claim, no visual parity readiness claim.
