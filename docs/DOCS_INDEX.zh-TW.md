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
- `COMPOSE_EXECUTION_SOURCE_MAP.zh-TW.md`: docs-only map of queue building, skip reasons, dispatch path, timing packet, metadata summary, and parity requirements around compose execution.
- `COMPOSE_EXECUTION_PARITY_GATE.zh-TW.md`: future parity gate design before any compose execution movement, including queue, skip, dispatch, timing, metadata, visual diff, and artifact audit branches.
- `COMPOSE_PARITY_CONTRACT_ONLY_EVIDENCE_PACKET.zh-TW.md`: contract-only evidence packet showing what current compose parity scripts prove and what remains missing before visual parity.
- `COMPOSE_PARITY_PAIRWISE_COMPARISON_PLAN.zh-TW.md`: baseline-vs-candidate pairwise comparison plan for future queue, skip, dispatch, timing, metadata, and artifact diff parity evidence.
- `COMPOSE_PARITY_PAIRWISE_GAP_PACKET.zh-TW.md`: contract-only tooling document for the machine-readable compose parity gap packet emitted by `scripts\compare_compose_pairwise_packet.ps1 -ContractOnly`, validated by `scripts\validate_compose_pairwise_gap_packet.ps1 -ContractOnly`, bundled by `scripts\compose_parity_contract_checkpoint.ps1`, and checkpoint-validated by `scripts\validate_compose_parity_contract_checkpoint.ps1`.
- `C3_FIRST_HELPER_EXTRACTION_PREIMPLEMENTATION_GATE.zh-TW.md`: docs/evidence-only gate that selects generated artifact audit/report packaging as the first safe future helper candidate and records its focused validator.
- `GENERATED_ARTIFACT_AUDIT_HELPER_INTEGRATION_MAP.zh-TW.md`: docs/evidence-only map for the next safe connection shape of `GeneratedArtifactAuditPacket`, keeping checkpoint/validator/meta-test boundaries separate.
- `DATAFRAME_PARSER_FIXTURE_PARITY_GATE.zh-TW.md`: docs/evidence-only preimplementation gate for `taichi_global_bathymetry.py` DataFrame parser fixture parity around parser input/output behavior.
- `NORMALIZER_FIXTURE_PARITY_GATE.zh-TW.md`: docs/evidence-only preimplementation gate for AIS and aircraft DataFrame normalizer fixture parity.
- `NORMALIZER_HELPER_EXTRACTION_PREIMPLEMENTATION_GATE.zh-TW.md`: docs/evidence-only gate defining future normalizer helper extraction boundaries, import restrictions, before/after parity requirements, risks, and the standalone import-boundary checker.
- `POLICY_STATIC_PACKET_BUILDER_CANDIDATE_MAP.zh-TW.md`: docs/evidence-only map of policy object and static packet builder candidates after the normalizer extraction slice.
- `POINT_OVERLAY_BUDGET_POLICY_FIXTURE_PARITY_GATE.zh-TW.md`: test/docs-only gate for current `PointOverlayBudgetPolicy` decision/text fixture parity before any future policy movement.
- `POINT_OVERLAY_BUDGET_POLICY_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md`: tooling/docs-only gate for future `PointOverlayBudgetPolicy` movement boundaries and import checks.
- `DATASHADER_SAMPLING_POLICY_FIXTURE_PARITY_GATE.zh-TW.md`: test/docs-only gate for current `DatashaderSamplingPolicy` decision/text fixture parity before any future policy movement.
- `DATASHADER_SAMPLING_POLICY_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md`: tooling/docs-only gate for future `DatashaderSamplingPolicy` movement boundaries and import checks.
- `LAYER_RENDER_BUDGET_POLICY_FIXTURE_PARITY_GATE.zh-TW.md`: test/docs-only gate for current `LayerRenderBudgetPolicy` decision/text fixture parity, including its `LAYER_RENDER_COSTS` dependency warning.
- `LAYER_RENDER_BUDGET_POLICY_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md`: tooling/docs-only gate for future `LayerRenderBudgetPolicy` movement boundaries, import checks, and reviewed `LAYER_RENDER_COSTS` handling.
- `ADAPTIVE_RENDER_QUALITY_POLICY_FIXTURE_PARITY_GATE.zh-TW.md`: test/docs-only gate for current `AdaptiveRenderQualityPolicy` decision/text fixture parity before any future policy movement.
- `ADAPTIVE_RENDER_QUALITY_POLICY_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md`: tooling/docs-only gate for future `AdaptiveRenderQualityPolicy` movement boundaries and import checks.
- `LAYER_RENDER_PLAN_OVERLAY_QUEUE_NEXT_SLICE_MAP.zh-TW.md`: docs/evidence-only source map for layer render plan, overlay queue, and composition-adjacent next fixture-gate candidates.
- `DISPLAYTOOLS_MONOLITH_SIX_SUBSYSTEM_GRAPH_CUT_MAP.zh-TW.md`: docs/evidence-only six-subsystem graph-cut map for monolith decomposition route selection.
- `LAYER_RENDER_PLAN_COMPOSE_QUEUE_FIXTURE_PARITY_GATE.zh-TW.md`: test/docs-only gate for `render_core.render_plan` compose queue pure helper fixture parity.
- `LAYER_RENDER_PLAN_COMPOSE_QUEUE_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md`: tooling/docs-only gate and AST import-boundary checker for possible future compose queue helper movement.
- `RENDER_PLAN_COMPOSE_QUEUE_EXTRACTION_CLOSEOUT_NEXT_SLICE_MAP.zh-TW.md`: docs/evidence-only close-out map for compose queue extraction and next safe render-plan slice selection.
- `LAYER_RENDER_PLAN_COMPOSITION_DISPATCH_FIXTURE_PARITY_GATE.zh-TW.md`: test/docs-only gate for composition action and dispatch packet helper fixture parity.
- `LAYER_RENDER_PLAN_COMPOSITION_DISPATCH_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md`: tooling/docs-only gate and AST import-boundary checker for possible future composition dispatch helper movement.
- `LAYER_RENDER_PLAN_CACHE_DIAGNOSTICS_FIXTURE_PARITY_GATE.zh-TW.md`: test/docs-only gate for render-plan cache key, invalidation reason/scope, and metadata summary helper fixture parity.
- `LAYER_RENDER_PLAN_CACHE_DIAGNOSTICS_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md`: tooling/docs-only gate and AST import-boundary checker for possible future cache diagnostics helper movement.
- `LAYER_RENDER_PLAN_EXECUTION_PHASE_TIMING_FIXTURE_PARITY_GATE.zh-TW.md`: test/docs-only gate for render-plan execution summary, execution phases, phase timing, and bottleneck packet helper fixture parity.
- `LAYER_RENDER_PLAN_EXECUTION_PHASE_TIMING_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md`: tooling/docs-only gate and AST import-boundary checker for possible future execution phase timing helper movement.
- `LAYER_RENDER_PLAN_ADAPTER_PREFLIGHT_FIXTURE_PARITY_GATE.zh-TW.md`: test/docs-only gate for render-plan adapter, compile input, payload contract, and single-pass preflight packet helper fixture parity.
- `LAYER_RENDER_PLAN_ADAPTER_PREFLIGHT_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md`: tooling/docs-only gate and AST import-boundary checker for possible future adapter/preflight helper movement.
- `LAYER_RENDER_PLAN_COMPILED_REUSED_PACKETS_FIXTURE_PARITY_GATE.zh-TW.md`: test/docs-only gate for compiled/reused layer render plan packet builder fixture parity.
- `LAYER_RENDER_PLAN_COMPILED_REUSED_PACKETS_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md`: tooling/docs-only gate and AST import-boundary checker for possible future compiled/reused packet helper movement.
- `LAYER_RENDER_PLAN_RESIDUAL_PACKET_SURFACES_FIXTURE_PARITY_GATE.zh-TW.md`: fixture gate for residual non-alpha, non-apply-path render-plan packet surfaces now physically owned by `render_core/layer_render_plan_residual_packet_surfaces.py`.
- `LAYER_RENDER_PLAN_RESIDUAL_PACKET_SURFACES_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md`: consumed movement gate and AST import-boundary checker for residual packet-surface helper movement.
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
