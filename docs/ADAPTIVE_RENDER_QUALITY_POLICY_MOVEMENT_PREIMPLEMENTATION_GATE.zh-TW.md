# AdaptiveRenderQualityPolicy Movement Preimplementation Gate

## TL;DR

This gate defines the import-boundary and parity requirements for the reviewed movement of `AdaptiveRenderQualityPolicy`.

Cut-out note: This gate has been consumed by the minimal movement slice for `AdaptiveRenderQualityPolicy`.

This gate has been used for a minimal movement slice: `AdaptiveRenderQualityPolicy` now lives in `render_core/adaptive_render_quality_policy.py`. This note records the boundary only and does not authorize broader movement.

## Current helper path

Current helper path:

```text
render_core/adaptive_render_quality_policy.py
```

The candidate file now exists after the reviewed minimal movement. The standalone checker must return `status=pass` with `boundary_passed=true` for this file. The synthetic missing-candidate behavior remains covered by tests using a deliberately absent path.

## Movement boundary

The helper must remain scalar-only recommendation logic.

It must not imply runtime degradation is active. The current policy reports recommendation fields only; it does not change render output or renderer state by itself.

It must not claim performance, readiness, or visual parity.

The monolith wiring must remain import plus re-export wiring only in `taichi_global_bathymetry.py`.

## Preserved behavior from fixture tests

This movement and any future edits must preserve current fixture coverage:

- unknown render timing branch
- pressure bucket boundaries
- large canvas guardrail
- width and height coercion
- target fps floor behavior
- negative render timing coercion
- exact `decision()` key set
- deterministic repeat calls
- exact `text().splitlines()` sequence

## Forbidden dependencies

The adaptive render quality policy helper must not import or depend on:

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
- `LayerRenderBudgetPolicy`
- `LAYER_RENDER_COSTS`
- runtime merge behavior

## Import-boundary checker

Standalone checker:

```powershell
py -3 -B scripts\validate_adaptive_render_quality_policy_import_boundary.py render_core\adaptive_render_quality_policy.py
```

Negative self-test:

```powershell
py -3 -B scripts\validate_adaptive_render_quality_policy_import_boundary.py --self-test-negative
```

The checker uses stdlib AST only. It must not import or execute the target module.

## Before/after parity requirements

For this reviewed movement and any future edits, run:

```powershell
py -3 -m unittest tests.test_adaptive_render_quality_policy
py -3 -m unittest tests.test_adaptive_render_quality_policy_import_boundary
py -3 -m unittest tests.test_generated_artifact_audit
py -3 -B scripts\validate_adaptive_render_quality_policy_import_boundary.py render_core\adaptive_render_quality_policy.py
py -3 -B scripts\validate_adaptive_render_quality_policy_import_boundary.py --self-test-negative
py -3 -B scripts\generated_artifact_audit_leaf_provider.py
git diff --check
```

`taichi_global_bathymetry.py` must remain limited to import/delegation or re-export wiring for this policy. Any broader source change requires a separate review.

## Artifact audit requirements

This movement and any future edits must preserve:

- no `state/` artifacts staged or untracked from the task
- no PNG artifacts staged or untracked from the task
- no generated runtime JSON artifacts staged or untracked from the task
- checker stdout JSON only, with no artifact file writes

## Not authorized

- Additional policy extraction beyond `AdaptiveRenderQualityPolicy`.
- Additional helper module creation beyond `render_core/adaptive_render_quality_policy.py`.
- Renderer runtime behavior change.
- Metadata or output behavior change.
- Performance claim.
- Readiness claim.
- Visual parity claim.
- Runtime merge.

## Boundary statement

Minimal AdaptiveRenderQualityPolicy movement gate consumed by this slice. No broader policy extraction, no renderer/Qt/Taichi runtime execution, no metadata/output behavior change, no performance claim, no visual parity readiness claim.
