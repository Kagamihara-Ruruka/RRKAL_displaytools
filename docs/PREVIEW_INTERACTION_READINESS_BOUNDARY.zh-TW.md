# Preview Interaction Readiness Boundary Audit

Date: 2026-06-03
Scope: RRKAL_displaytools preview evidence boundary
Status: docs/evidence-design only

## TL;DR

Current evidence proves that renderer preview artifacts can be produced through quick, repeated, warm-frame, high-density, and runtime_blend timing paths. It does not prove Qt/UI interactive readiness, event-loop responsiveness, or interactive FPS.

The safe claim is:

- Renderer preview artifact path is smoke-covered.
- Repeated preview artifact generation is stable enough for renderer evidence review.
- Warm-frame evidence identifies in-process renderer timing pressure.
- runtime_blend timing is evidence-only and remains behind a data-ready timing gate.

The unsafe claim is:

- Do not claim interactive FPS readiness.
- Do not claim the Qt preview operation path is non-blocking.
- Do not claim user interaction latency has been measured.

## What current evidence proves

- `render_quick_smoke.ps1` proves a single renderer preview artifact, preview frame, and metadata sidecar can be emitted.
- `render_repeated_quick_smoke.ps1 -Frames 3` proves the actual renderer preview path can repeat across multiple process-per-frame runs.
- `render_repeated_quick_smoke.ps1 -Frames 5` adds a small stability sample for process-per-frame preview output.
- `render_warm_frame_smoke.ps1` proves in-process warm-frame renderer timing can be collected without changing output behavior.
- high-density warm-frame evidence increases overlay pressure and keeps the timing path measurable.
- runtime_blend timing proves per-step timing can be collected in opt-in evidence mode.
- the data-ready timing gate defines the next review boundary before deeper renderer-core instrumentation.
- demo-readiness baseline documents renderer artifact evidence for near-term presentation judgment.

## What current evidence does not prove

- It does not prove Qt event loop responsiveness.
- It does not prove frame-to-frame UI refresh timing.
- It does not prove mouse/keyboard interaction latency.
- It does not prove that long renderer work does not block UI controls.
- It does not prove interactive FPS.
- It does not prove production deployment readiness.
- It does not authorize runtime_blend optimization, alpha blending changes, layer ordering changes, runtime merge, metadata schema changes, or output pixel behavior changes.

## Evidence type differences

`render_quick_smoke.ps1`:

- Single renderer artifact run.
- Good for output existence, metadata schema, and preview path sanity.
- Not an interaction or FPS measurement.

`render_repeated_quick_smoke.ps1`:

- Repeats the actual quick render path across separate process runs.
- Good for preview artifact stability and process-per-frame bottleneck evidence.
- Not an in-process UI loop measurement.

`render_warm_frame_smoke.ps1`:

- Runs repeated frames inside one renderer process.
- Good for separating cold first-frame and warm-frame renderer timing.
- Not a Qt event-loop measurement.

`render_warm_frame_smoke.ps1 -RuntimeBlendTiming`:

- Adds opt-in runtime_blend step timing.
- Good for runtime_blend pressure and data-ready attribution review.
- Not an optimization result and not a UI readiness claim.

Demo-readiness baseline:

- A curated summary of renderer artifact evidence and timing interpretation.
- Good for deciding what can be shown in a student/project demo.
- Not proof of full UI readiness.

Actual Qt/UI interactive loop:

- Requires evidence from the running Qt event loop, preview refresh path, user operations, and latency capture.
- Not measured by the current renderer smoke artifacts.

## Why interactive FPS readiness cannot be claimed yet

Interactive FPS readiness is a UI-system property, not a renderer-artifact property. The current evidence runs renderer scripts and collects output artifacts, but it does not observe the Qt event loop while the user interacts with layers, preview refresh, selection, panels, or camera controls.

Current warm-frame evidence is useful because it shows in-process renderer timing. It still lacks:

- UI event-loop timing.
- preview refresh dispatch timing.
- user action to preview update latency.
- evidence that controls remain responsive during renderer work.
- sustained frame cadence under real UI operation.

## Evidence required before claiming UI readiness

Before claiming Qt preview/UI interactive readiness, collect evidence for:

- UI event loop non-blocking behavior during preview refresh.
- preview refresh timing from request to visible frame update.
- frame-to-frame interaction timing during repeated UI operations.
- user interaction latency for layer selection, visibility toggles, camera/pan/zoom, and preview update.
- renderer artifact output unchanged under the UI path.
- metadata schema unchanged.
- generated artifacts ignored and not committed.
- no interactive FPS overclaim.

## Readiness boundary table

| Evidence type | What it proves | What it does not prove | Current status | Next gate |
| --- | --- | --- | --- | --- |
| quick smoke | single renderer artifact, preview frame, metadata sidecar | repeated stability, warm-frame timing, UI readiness | PASS baseline exists | keep as smoke prerequisite |
| repeated 3-frame | process-per-frame preview artifact stability | in-process warm behavior, Qt responsiveness | PASS baseline exists | compare with repeated 5-frame and warm-frame evidence |
| repeated 5-frame | larger process-per-frame preview stability sample | UI event loop, interactive FPS | PASS baseline exists | use as preview artifact stability floor |
| warm-frame | in-process renderer warm-frame timing | Qt event loop responsiveness | PASS baseline exists | separate renderer timing from UI timing |
| high-density warm-frame | renderer timing under increased overlay pressure | UI readiness or optimization safety | PASS baseline exists | compare pressure class before any optimization review |
| runtime_blend timing | opt-in runtime_blend per-step evidence | blend math vs data-ready wait attribution, UI FPS | PASS baseline exists | data-ready timing gate |
| data-ready timing gate | design boundary before deeper renderer-core instrumentation | implementation approval or optimization permission | design complete | separate o_1/Owner review before renderer-core hook |
| Qt preview / UI operation path | would prove event-loop and preview interaction behavior if measured | not covered by current renderer scripts | not yet measured | Qt Preview Operation Evidence Gate |

## Future gate proposal: Qt Preview Operation Evidence Gate

Purpose:

- Collect UI-path evidence before any interactive readiness claim.
- Keep the gate evidence-only and output-neutral.

Candidate evidence:

- UI event loop heartbeat while preview refresh is requested.
- preview refresh request timestamp, renderer result timestamp, and UI display/update timestamp.
- frame-to-frame interaction timing for a bounded operation set.
- user interaction latency for layer selection, visibility toggle, and preview update.
- explicit note whether renderer work blocks UI controls.
- artifact path and metadata schema unchanged.
- generated evidence artifacts under ignored `state/`.

Required constraints:

- no UI implementation in this audit document.
- no runtime optimization.
- no runtime merge.
- no output pixel behavior change.
- no metadata schema drift.
- no interactive FPS claim until UI-path evidence exists.

Suggested future classification:

`need_qt_preview_operation_evidence_gate_before_ui_readiness_claim`

Gate draft:

- See `docs/QT_PREVIEW_OPERATION_EVIDENCE_GATE.zh-TW.md` for the detailed measurement plan, future smoke concept, invariants, and stop conditions.

## 2026-06-03 audit baseline rerun

The audit reran the safe renderer evidence subset after HEAD `5650f99`.

| command | result | elapsed |
| --- | --- | ---: |
| `scripts\render_quick_smoke.ps1` | PASS | 16.959 s |
| `scripts\render_repeated_quick_smoke.ps1 -Frames 3` | PASS | 45.715 s |
| `scripts\render_repeated_quick_smoke.ps1 -Frames 5` | PASS | 70.216 s |
| `scripts\render_warm_frame_smoke.ps1` | PASS | 34.730 s |
| `scripts\render_warm_frame_smoke.ps1 -RuntimeBlendTiming` | PASS | 38.591 s |
| `scripts\smoke.ps1` | PASS | 248.241 s |

Latest renderer evidence snapshot:

| evidence | value |
| --- | ---: |
| repeated 5-frame render avg | 1017.780 ms |
| repeated 5-frame prepare_batches avg | 977.670 ms |
| repeated 5-frame compose_overlays avg | 35.022 ms |
| warm-frame render avg | 71.500 ms |
| warm-frame prepare_batches avg | 32.136 ms |
| warm-frame compose_overlays avg | 34.265 ms |
| runtime_blend total avg | 25.880 ms |
| runtime_blend first-step avg | 8.709 ms |
| runtime_blend non-first avg | 8.585 ms |

Audit interpretation:

- Preview artifacts still emit through the renderer path.
- Metadata schema remains unchanged.
- Runtime merge remains disabled.
- Repeated quick evidence remains process-per-frame and `prepare_batches` dominated.
- Warm-frame evidence remains renderer timing evidence, not Qt/UI event-loop evidence.
- runtime_blend first-step timing remains roughly uniform with later steps in this run.
- The readiness boundary remains unchanged: no interactive FPS readiness claim.

## Current boundary statement

Preview interaction readiness boundary only. No UI implementation. No runtime optimization. No interactive FPS readiness claim.
