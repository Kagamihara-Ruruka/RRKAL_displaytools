# AdaptiveRenderQualityPolicy Fixture Parity Gate

## TL;DR

This gate locks the current `AdaptiveRenderQualityPolicy.decision()` and `AdaptiveRenderQualityPolicy.text()` behavior with focused fixtures before any future policy movement is discussed.

Cut-out note: No monolith source extracted in this slice.

This is a test/docs gate only. It does not authorize policy extraction, helper creation, renderer movement, performance claims, output behavior changes, visual parity claims, UI readiness claims, or runtime merge.

## Static evidence

Target:

- `taichi_global_bathymetry.py:5069` in the current file.
- Class: `AdaptiveRenderQualityPolicy`.
- Methods: `decision()`, `text()`.

Observed dependencies:

- Inputs are scalar canvas size, render timing, lod, and target fps.
- No global cost map is used.
- No renderer/controller object is accepted.
- No Qt, VisPy, or Taichi runtime reference is observed in the class body.
- No file/cache/artifact read or write is observed.
- No metadata schema or output image behavior is touched.

## Fixture matrix

| fixture | expected branch / behavior |
| --- | --- |
| unknown render timing | `render_ms=None` yields `pressure=1.0`, full quality, and text `unknown` |
| pressure `<= 1.15` | scale `1.0`, overlay budget `full` |
| pressure `> 1.15` and `<= 2.0` | scale `0.85`, overlay budget `reduced overlays` |
| pressure `> 2.0` and `<= 4.0` | scale `0.70`, overlay budget `sample realtime overlays` |
| pressure `> 4.0` | scale `0.55`, overlay budget `aggressive realtime sampling` |
| large canvas guardrail | pixels `>= 6_000_000` limits full quality to scale `0.85` |
| width/height coercion | non-positive width/height become at least `1` |
| target fps floor | target ms uses fps floor `1.0`, while reported target fps preserves input float |
| negative render timing | negative `render_ms` coerces to `0.0` |
| decision output keys | exact key set is pinned |
| deterministic repeat call | same input returns same output |
| text output | split-line order, numeric formatting, `unknown` wording, and rule line are pinned |

## Current fixture evidence

Focused tests exist in `tests/test_adaptive_render_quality_policy.py`.

They prove only that the current policy object behavior is observable through import-level fixtures. They do not prove renderer behavior, output image behavior, metadata behavior, UI behavior, or performance improvement.

## False-leaf warnings

- `AdaptiveRenderQualityPolicy` reports recommendation fields, but fixture parity does not approve extraction.
- The class uses render timing inputs, so future movement must avoid implying runtime readiness or speed improvement.
- Do not combine this with renderer timing, compose execution, metadata schema, or output behavior work in the same slice.

## Recommended next step

If this gate is accepted, use `ADAPTIVE_RENDER_QUALITY_POLICY_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md` and `scripts\validate_adaptive_render_quality_policy_import_boundary.py` before any future movement of this policy.

Do not extract the policy in the same checkpoint as this fixture gate.

## Boundary statement

Test/docs-only AdaptiveRenderQualityPolicy fixture parity gate. No policy extraction, no helper module creation, no renderer/Qt/Taichi runtime execution, no metadata/output behavior change, no performance claim, no visual parity readiness claim.
