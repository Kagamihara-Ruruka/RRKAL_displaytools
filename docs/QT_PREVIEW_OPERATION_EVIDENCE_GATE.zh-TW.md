# Qt Preview Operation Evidence Gate

Date: 2026-06-03
Scope: RRKAL_displaytools Qt preview operation evidence design
Status: docs/evidence-gate-design only

## TL;DR

The current renderer evidence proves preview artifact generation and renderer timing. It does not prove Qt preview operation readiness.

Before making any UI readiness claim, RRKAL_displaytools needs a separate opt-in Qt Preview Operation Evidence Gate that measures the running UI path:

- UI event loop non-blocking behavior.
- preview refresh request to UI update timing.
- frame-to-frame interaction timing.
- user operation latency for layer and camera operations.
- artifact and metadata invariants.
- conservative failure when the UI path is unavailable.

This document is a gate draft only. It does not implement Qt event-loop code and does not authorize interactive FPS readiness claims.

## Why renderer artifact evidence is not UI operation evidence

Renderer scripts such as `render_quick_smoke.ps1`, `render_repeated_quick_smoke.ps1`, and `render_warm_frame_smoke.ps1` run renderer paths and inspect output artifacts. They do not observe a live Qt event loop.

That distinction matters because a renderer can emit correct preview artifacts while the UI still has problems:

- the Qt event loop may block during renderer work.
- preview refresh may lag behind user actions.
- layer selection or visibility toggles may feel delayed.
- camera pan/zoom may trigger preview updates too slowly.
- output artifacts may update, but the visible UI may not refresh predictably.

Therefore renderer evidence is necessary but not sufficient for Qt preview operation readiness.

## Required future evidence

A future Qt preview operation gate should collect machine-readable evidence for:

- event-loop heartbeat during preview requests.
- preview refresh request timestamp.
- renderer or preview artifact ready timestamp.
- UI preview update/display timestamp.
- user operation start/end timestamps.
- bounded operation set and operation ids.
- whether UI controls stayed responsive during renderer work.
- output artifact path and metadata schema invariants.
- generated evidence path under ignored `state/`.
- explicit `interactive_fps_claimed=false`.

## Proposed measurement points

Minimum measurement points:

1. `ui_event_loop_heartbeat_ms`: a lightweight periodic heartbeat that records event-loop progress while preview work is requested.
2. `preview_request_to_dispatch_ms`: time from UI preview request to renderer/preview dispatch.
3. `preview_dispatch_to_artifact_ready_ms`: time from dispatch to preview artifact availability.
4. `artifact_ready_to_ui_update_ms`: time from preview artifact availability to UI-visible preview update.
5. `user_action_to_preview_request_ms`: time from a UI operation to preview request.
6. `user_action_to_ui_ack_ms`: time from a UI operation to visible UI acknowledgement.
7. `frame_to_frame_preview_interval_ms`: interval between bounded preview updates.

These are proposed evidence fields only. Adding them would require a separate reviewed implementation slice.

## Non-blocking event loop criteria

The future gate should treat UI readiness as unproven unless it can show:

- event-loop heartbeat continues during preview operation.
- no single preview operation blocks the heartbeat beyond a configured conservative threshold.
- user-facing controls can acknowledge bounded operations while preview work is pending.
- the evidence records any missed heartbeat or blocked interval.

The gate should fail conservatively if no event-loop heartbeat is available.

## Preview refresh timing criteria

The future gate should record:

- preview request time.
- dispatch time.
- artifact-ready time.
- UI update time.
- final visible preview state or acknowledgement.

It should separate renderer artifact generation from UI display update. A preview PNG being written is not the same as a preview becoming visible inside Qt.

## User operation latency criteria

Minimum operation set for future evidence:

- layer selection.
- layer visibility toggle.
- camera pan.
- camera zoom.
- preview refresh request.

For each operation, collect:

- operation id.
- start timestamp.
- UI acknowledgement timestamp.
- preview request timestamp if applicable.
- preview update timestamp if applicable.
- latency classification.

This still must not be presented as interactive FPS. It is bounded operation latency evidence.

## Artifact / metadata invariants

The future gate must preserve:

- renderer output metadata schema remains `rrkal_displaytools.renderer_output_metadata.v1`.
- output artifact path behavior remains unchanged unless separately reviewed.
- generated evidence artifacts remain under ignored `state/`.
- no generated PNG, JSON, or Markdown evidence artifact is committed.
- runtime merge remains disabled unless separately approved.
- default non-gate behavior remains unchanged.

## Required gate table

| Evidence | Measurement idea | What it proves | What it does not prove | Risk |
| --- | --- | --- | --- | --- |
| UI event loop non-blocking behavior | heartbeat while preview work is pending | event loop continues to process events | sustained FPS or full UI readiness | instrumentation may perturb timing |
| preview refresh request to UI update timing | request, dispatch, artifact-ready, UI-update timestamps | preview path latency in the running UI | renderer math attribution | needs careful path labeling |
| frame-to-frame interaction timing | bounded repeated preview update intervals | cadence under a small operation loop | open-ended interactive FPS | can be overclaimed if summarized as FPS |
| layer toggle latency | visibility toggle to UI ack and preview request/update | layer-control operation responsiveness | output visual parity | may require controlled layer state |
| camera / pan / zoom latency | pan/zoom action to UI ack and preview request/update | camera operation responsiveness | scientific render correctness | camera path may need separate invariants |
| output artifact unchanged | compare path/schema/expected artifact presence | UI gate does not alter artifact behavior | pixel parity by itself | pixel comparison may be a later gate |
| metadata schema unchanged | inspect sidecar schema and UI evidence schema separately | renderer metadata compatibility | UI readiness | schema drift can hide in evidence-only fields |
| generated artifacts ignored | git status and staged diff audit | local evidence is not committed | correctness of evidence content | ignored files can still be manually staged if careless |
| no FPS overclaim | explicit `interactive_fps_claimed=false` plus wording audit | report language remains bounded | actual readiness | humans may still misread latency as FPS |

## Minimum future smoke proposal

Future concept: `qt_preview_operation_smoke`

Required behavior:

- opt-in only.
- no default behavior change.
- no generated artifacts committed.
- emits machine-readable evidence.
- writes evidence under ignored `state/showcase/qt_preview_operation_smoke/`.
- fails conservatively if the Qt/UI path is unavailable.
- reports `interactive_fps_claimed=false`.
- reports metadata schema and output artifact invariants.
- reports whether event-loop heartbeat evidence was collected.
- reports whether preview update timing evidence was collected.

Suggested future evidence schema:

`rrkal_displaytools.qt_preview_operation_evidence.v1`

Suggested future result fields:

- `schema`
- `source`
- `ui_path_available`
- `event_loop_heartbeat_collected`
- `preview_refresh_timing_collected`
- `operation_latency_collected`
- `interactive_fps_claimed=false`
- `metadata_schema_changed=false`
- `output_behavior_changed=false`
- `runtime_merge_enabled=false`
- `generated_artifacts_ignored=true`
- `stop_condition_triggered`

This is a proposal only and must not be implemented in this docs-only checkpoint.

## Current evidence boundary

Current evidence may support:

- preview artifact generation.
- repeated preview artifact stability.
- renderer timing.
- warm-frame timing.
- runtime_blend timing.
- data-ready timing gate design.

Current evidence does not support:

- UI readiness.
- Qt event-loop non-blocking behavior.
- user interaction latency.
- preview refresh latency inside the running UI.
- interactive FPS.

## 2026-06-03 baseline rerun

The gate draft reran the safe renderer evidence subset after HEAD `aca6c5a`.

| command | result | elapsed |
| --- | --- | ---: |
| `scripts\render_quick_smoke.ps1` | PASS | 14.747 s |
| `scripts\render_repeated_quick_smoke.ps1 -Frames 3` | PASS | 51.187 s |
| `scripts\render_repeated_quick_smoke.ps1 -Frames 5` | PASS | 69.856 s |
| `scripts\render_warm_frame_smoke.ps1` | PASS | 43.354 s |
| `scripts\render_warm_frame_smoke.ps1 -RuntimeBlendTiming` | PASS | 36.605 s |
| `scripts\smoke.ps1` | PASS | 211.470 s |

Latest renderer evidence snapshot:

| evidence | value |
| --- | ---: |
| repeated 5-frame render avg | 1054.000 ms |
| repeated 5-frame prepare_batches avg | 1015.278 ms |
| repeated 5-frame compose_overlays avg | 33.815 ms |
| warm-frame render avg | 82.630 ms |
| warm-frame prepare_batches avg | 40.473 ms |
| warm-frame compose_overlays avg | 34.980 ms |
| runtime_blend total avg | 26.122 ms |
| runtime_blend first-step avg | 8.733 ms |
| runtime_blend non-first avg | 8.694 ms |

Rerun interpretation:

- Existing renderer evidence commands remain available and passing.
- Preview artifacts still emit through repeated quick render.
- Metadata schema remains unchanged.
- Runtime merge remains disabled.
- runtime_blend first-step timing remains roughly uniform with later steps.
- The rerun does not add Qt event-loop or user-latency evidence.
- The gate classification remains `need_qt_preview_operation_evidence_gate_before_ui_readiness_claim`.

## Stop conditions

Stop before implementation if:

- measuring the UI path requires new Qt event-loop code in the current docs-only slice.
- output pixels may change.
- metadata schema would change.
- runtime merge would be enabled.
- runtime_blend optimization appears in scope.
- generated evidence artifacts are not ignored.
- wording starts implying interactive FPS readiness.

## Not-yet-authorized items

Not authorized by this gate draft:

- UI implementation.
- Qt event-loop instrumentation.
- preview refresh instrumentation.
- runtime optimization.
- runtime merge.
- metadata schema migration.
- output behavior change.
- interactive FPS readiness claim.

## Boundary statement

Qt preview operation evidence gate design only. No UI implementation. No interactive FPS readiness claim.
