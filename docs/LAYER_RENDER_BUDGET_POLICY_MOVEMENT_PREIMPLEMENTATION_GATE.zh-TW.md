# LayerRenderBudgetPolicy Movement Preimplementation Gate

## TL;DR

This gate defines the import-boundary and parity requirements before any future movement of `LayerRenderBudgetPolicy`.

Cut-out note: No monolith source extracted in this slice.

This checkpoint does not create a helper module, does not move `LAYER_RENDER_COSTS`, and does not extract policy code.

## Candidate future path

Future candidate path:

```text
render_core/layer_render_budget_policy.py
```

The candidate file is intentionally absent in this checkpoint. The standalone checker must return `not_applicable_candidate_missing` with `boundary_passed=true` while it is absent.

## LAYER_RENDER_COSTS movement decision

Preferred future movement strategy:

- Move `LAYER_RENDER_COSTS` into the same future helper module as `LayerRenderBudgetPolicy`.

Acceptable alternative:

- Move `LAYER_RENDER_COSTS` into a pure constants module such as `render_core/layer_render_costs.py`, but only if that constants module has its own no-renderer import-boundary check.

Forbidden strategy:

- A future helper must not import `taichi_global_bathymetry` only to read `LAYER_RENDER_COSTS`.

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

A future layer render budget policy helper must not import or depend on:

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

Before any future movement, run:

```powershell
py -3 -m unittest tests.test_layer_render_budget_policy
py -3 -m unittest tests.test_layer_render_budget_policy_import_boundary
py -3 -m unittest tests.test_generated_artifact_audit
py -3 -B scripts\validate_layer_render_budget_policy_import_boundary.py render_core\layer_render_budget_policy.py
py -3 -B scripts\validate_layer_render_budget_policy_import_boundary.py --self-test-negative
py -3 -B scripts\generated_artifact_audit_leaf_provider.py
git diff --check
```

If movement happens later, `taichi_global_bathymetry.py` must be limited to import/delegation or re-export wiring for this policy plus reviewed `LAYER_RENDER_COSTS` handling. Any broader source change requires a separate review.

## Artifact audit requirements

Future movement must preserve:

- no `state/` artifacts staged or untracked from the task
- no PNG artifacts staged or untracked from the task
- no generated runtime JSON artifacts staged or untracked from the task
- checker stdout JSON only, with no artifact file writes

## Not authorized

- Policy extraction.
- Helper module creation.
- Movement of `LAYER_RENDER_COSTS`.
- Renderer runtime behavior change.
- Metadata or output behavior change.
- Performance claim.
- Readiness claim.
- Visual parity claim.
- Runtime merge.

## Boundary statement

Tooling/docs-only LayerRenderBudgetPolicy movement preimplementation gate. No policy extraction, no helper module creation, no renderer/Qt/Taichi runtime execution, no metadata/output behavior change, no performance claim, no visual parity readiness claim.
