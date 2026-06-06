# PointOverlayBudgetPolicy Movement Preimplementation Gate

## TL;DR

This gate defines the import-boundary and parity requirements before any future movement of `PointOverlayBudgetPolicy`.

This checkpoint does not create a helper module and does not extract policy code.

## Candidate future path

Future candidate path:

```text
render_core/point_overlay_budget_policy.py
```

The candidate file is intentionally absent in this checkpoint. The standalone checker must return `not_applicable_candidate_missing` with `boundary_passed=true` while it is absent.

## Preserved behavior from fixture tests

Future movement must preserve current fixture coverage:

- low / sparse / medium / high record-count branches
- drag-over-budget branches
- steady over-budget dense and very-dense branches
- global large-canvas dense branch
- equality boundary at `target_ms * 1.08`
- `render_ms=None` and negative point count coercion
- exact `decision()` key set
- exact `text().splitlines()` sequence

## Forbidden dependencies

A future policy helper must not import or depend on:

- renderer/controller modules or state
- Qt, VisPy, or Taichi runtime modules
- preview or artifact writers
- metadata sidecar writers
- provider/source loaders
- parser functions
- DataFrame normalizer modules
- `pyais`
- runtime merge behavior

## Import-boundary checker

Standalone checker:

```powershell
py -3 -B scripts\validate_policy_import_boundary.py render_core\point_overlay_budget_policy.py
```

Negative self-test:

```powershell
py -3 -B scripts\validate_policy_import_boundary.py --self-test-negative
```

The checker uses stdlib AST only. It must not import or execute the target module.

## Before/after parity requirements

Before any future movement, run:

```powershell
py -3 -m unittest tests.test_point_overlay_budget_policy
py -3 -m unittest tests.test_policy_import_boundary
py -3 -m unittest tests.test_generated_artifact_audit
py -3 -B scripts\validate_policy_import_boundary.py render_core\point_overlay_budget_policy.py
py -3 -B scripts\generated_artifact_audit_leaf_provider.py
git diff --check
```

If movement happens later, `taichi_global_bathymetry.py` must be limited to import/delegation or re-export wiring for this policy. Any broader source change requires a separate review.

## Artifact audit requirements

Future movement must preserve:

- no `state/` artifacts staged or untracked from the task
- no PNG artifacts staged or untracked from the task
- no generated runtime JSON artifacts staged or untracked from the task
- checker stdout JSON only, with no artifact file writes

## Not authorized

- Policy extraction.
- Helper module creation.
- Renderer runtime behavior change.
- Metadata or output behavior change.
- Performance claim.
- Visual parity readiness claim.
- UI readiness claim.
- Runtime merge.

## Boundary statement

Tooling/docs-only policy movement preimplementation gate. No policy extraction, no helper module creation, no renderer/Qt/Taichi runtime execution, no metadata/output behavior change, no performance claim, no visual parity readiness claim.
