# Documentation Index

## Core docs

- `PRODUCT_POSITIONING.zh-TW.md`: RRKAL / displaytools responsibility boundary and renderer-layer positioning.
- `PROJECT_GTD.md`: active work lines, current status, backlog, and next development slices.
- `DEVELOPMENT_LOG.zh-TW.md`: chronological development log and commit handoff notes.
- `WORKFLOW.zh-TW.md`: standard local/cloud development loop, testing split, conversation backup policy, and push report template.
- `CODEX_CLOUD_HANDOFF.zh-TW.md`: first-read entrypoint for Codex Cloud, local Codex, and other agents taking over from GitHub.
- `DIALOGUE_SAVE_RESTORE.zh-TW.md`: private `dialogue-save` transcript chunk restore workflow for emergency full-context recovery.
- `DECOUPLING_RUNBOOK.zh-TW.md`: post-2026-05-31 07:00 decoupling gate, first extraction order, and module-boundary rules.
- `AGENT_HANDOFF.zh-TW.md`: current agent-facing working rules, scope, and known risks.
- `GIT_HANDOFF.md`: git start/end loop, commit/push rules, and do-not-commit list.
- `WORKSPACE_LAYOUT.zh-TW.md`: canonical workspace, root files, docs map, and local-only artifact policy.
- `PROFILE_SCHEMA.zh-TW.md`: Qt panel profile template schema and RRKAL/displaytools handoff rules.
- `SETUP_WINDOWS.zh-TW.md`: clone/setup/smoke/Qt panel steps for another Windows computer.
- `RRKAL_HANDOFF_CONTRACT.zh-TW.md`: no-GUI RRKAL/displaytools integration contract.
- `CAPABILITY_SUMMARY.zh-TW.md`: current program capability summary for push reports and GitHub review.
- `DISPLAY_SHELL_RENDER_MATRIX.zh-TW.md`: DisplayShell / Canvas / Render Matrix contracts, display runtime landing zones, and no-GUI review/check commands.
- `RENDERER_BACKEND_MAPPING_AUDIT.zh-TW.md`: renderer backend mapping, render flow, monolith responsibility audit, and staged decomposition candidates for demo-readiness review.
- `LAYER_STATE_SOURCE_MAP.zh-TW.md`: layer visibility/opacity/blend/selected-target/dirty-flag source map before layer-state helper extraction.
- `RENDER_PLAN_COMPILE_SOURCE_MAP.zh-TW.md`: compile-layer-render-plan source map before compile facade / payload helper extraction.
- `STATIC_BATCH_PREPARE_SOURCE_MAP.zh-TW.md`: `prepare_batches` / vector overlay cache source map before static batch cache work.
- `RUNTIME_BLEND_SUBPHASE_TIMING_DESIGN.zh-TW.md`: runtime-blend subphase timing feasibility, safe insertion points, and parity/safety gate before instrumentation.
- `DEMO_READINESS_BASELINE.zh-TW.md`: latest renderer preview, repeated quick render, warm-frame, and runtime-blend timing evidence for demo-readiness judgment.
- `PREVIEW_INTERACTION_READINESS_BOUNDARY.zh-TW.md`: boundary between renderer preview evidence and future Qt/UI interactive readiness evidence.
- `QT_PREVIEW_OPERATION_EVIDENCE_GATE.zh-TW.md`: proposed future Qt preview operation evidence gate for event-loop, preview-refresh, and user-latency measurement.
- `DISPLAY_VIEWCARD_CONSUMER_MAPPING.zh-TW.md`: c_3 downstream consumer mapping for minimal DisplayViewCard, LayerViewCard, PreviewViewCard, and optional EvidenceViewCard fields.

## Positioning

`RRKAL_displaytools` is the visualization/display layer for RRKAL-related renderer work. `APIkeys_collection` / RRKAL remains responsible for dataset discovery, download, import, install registry, manifest, cache governance, and renderer bridge asset ownership.

## Project rule

Every development round must end with:
- code/doc updates staged intentionally,
- development log updated,
- commit created before the next round begins.

## Reference

- Documentation governance reference: Kagamihara-Ruruka/APIkeys_collection.
- Product boundary reference: `APIkeys_collection/docs/PRODUCT_POSITIONING.zh-TW.md`, especially the renderer bridge and tile/cache asset sections.
