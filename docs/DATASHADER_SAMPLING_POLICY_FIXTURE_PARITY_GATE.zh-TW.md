# DatashaderSamplingPolicy Fixture Parity Gate

## TL;DR

This gate locks the current `DatashaderSamplingPolicy.decision()` and `DatashaderSamplingPolicy.text()` behavior with focused fixtures before any future policy movement is discussed.

This is a test/docs gate only. It does not authorize policy extraction, helper creation, renderer movement, performance claims, output behavior changes, visual parity claims, UI readiness claims, or runtime merge.

## Static evidence

Target:

- `taichi_global_bathymetry.py:5064` in the current file.
- Class: `DatashaderSamplingPolicy`.
- Methods: `decision()`, `text()`.

Observed dependencies:

- Inputs are scalar counts, lod, scale, realtime/mode values.
- Local class registry: `LOD_BUDGETS`.
- No renderer/controller object is accepted.
- No Qt, VisPy, or Taichi runtime reference is observed in the class body.
- No file/cache/artifact read or write is observed.
- No metadata schema or output image behavior is touched.

## Fixture matrix

| fixture | expected branch / behavior |
| --- | --- |
| records `< 200_000` | regional budget allows `aggregate-all` |
| records `>= 200_000` | still under regional budget at `200_000` |
| records `>= 800_000` | regional half-scale pre-samples at `0.5625` |
| records `>= 2_000_000` | global realtime pre-samples at `0.125` |
| unknown lod | falls back to global base budget |
| continental/local lod budgets | `continental=500_000`, `local=1_250_000` |
| offline mode | effective budget is raised to records and aggregates all |
| user scale floor | scale below `0.05` is clamped to `0.05` |
| sample fraction lower clamp | very large realtime records clamp `sample_fraction` to `0.001` |
| negative records | coerces to `0` and aggregates all |
| decision output keys | exact key set is pinned |
| deterministic repeat call | same input returns same output |
| text output | split-line order, mode/lod wording, budget fields, sample fraction formatting, and rule line are pinned |
| offline text output | split-line order, section order, `1.0000` sample fractions, and `aggregate-all` strategies are pinned |

## Current fixture evidence

Focused tests exist in `tests/test_datashader_sampling_policy.py`.

They prove only that the current policy object behavior is observable through import-level fixtures. They do not prove renderer behavior, output image behavior, metadata behavior, UI behavior, or performance improvement.

## False-leaf warnings

- `DatashaderSamplingPolicy` looks like a deterministic policy object, but fixture parity does not approve extraction.
- The text output contains "realtime FPS valve" wording from the current implementation; tests pin existing text but do not make a performance claim.
- Future movement still needs an import-boundary checker for the target helper module.
- Do not combine this with renderer timing, compose execution, metadata schema, or output behavior work in the same slice.

## Recommended next step

If this gate is accepted, use `DATASHADER_SAMPLING_POLICY_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md` and `scripts\validate_datashader_policy_import_boundary.py` before any future movement of this policy.

Do not extract the policy in the same checkpoint as this fixture gate.

## Boundary statement

Test/docs-only DatashaderSamplingPolicy fixture parity gate. No policy extraction, no helper module creation, no renderer/Qt/Taichi runtime execution, no metadata/output behavior change, no performance claim, no visual parity readiness claim.
