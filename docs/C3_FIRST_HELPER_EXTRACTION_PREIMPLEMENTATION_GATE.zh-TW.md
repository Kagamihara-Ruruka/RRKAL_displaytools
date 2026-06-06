# C3 First Helper Extraction Preimplementation Gate

## TL;DR

This is a docs/evidence-only gate for the first safe future renderer helper extraction.

The recommended future implementation candidate is exactly one helper type:

`generated artifact audit / report packaging helper`

This candidate is safer than metadata schema movement, timing runtime movement, preview PNG writing, compose execution movement, pixels, alpha blending, layer ordering, Taichi kernels, or Qt behavior because it only packages external evidence about generated artifacts and staged files.

This document does not authorize implementation. It only defines the preimplementation decision boundary.

## Current repo evidence

Observed surfaces:

- `taichi_global_bathymetry.py` imports `render_core.metadata.build_renderer_output_metadata_payload`, `render_core.preview.write_preview_frame_png`, `render_core.batch_prepare.build_prepare_batch_cache_evidence`, and many render-plan metadata/timing helpers.
- `render_core/metadata.py` already owns `build_renderer_output_metadata_payload` and emits `rrkal_displaytools.renderer_output_metadata.v1`.
- `render_core/preview.py` writes preview PNG files through `write_preview_frame_png`; this is an artifact/output touch point.
- `render_core/batch_prepare.py` emits `prepare_batch_cache_evidence.v1` and explicitly does not mutate overlay arrays or enable runtime merge.
- `render_core/render_plan.py` already contains metadata summary, phase timing, adapter payload, execution summary, and parity contract packet builders.
- `render_core/render_plan_performance.py` records compose parity artifact workflow metadata and repeatedly states runtime merge remains disabled until parity evidence exists.
- `display_core/render_matrix.py` and `display_runtime/*` are contract/runtime-adapter surfaces and do not invoke renderer backends in their contract-only paths.

Conclusion: metadata and timing helper surfaces are already partially extracted, but any movement that changes renderer metadata payloads, timing placement, PNG output, compose paths, or preview paths still needs parity gates. Generated artifact audit/report packaging is the safest first future candidate because it can stay outside renderer execution.

## Branch scan

| Branch | Evidence observed | Risk | Validation available | Recommended next action | Stop condition |
| ------ | ----------------- | ---- | -------------------- | ----------------------- | -------------- |
| A. Candidate touches only metadata/evidence/report packaging | Existing `render_core.metadata`, `render_core.batch_prepare`, and render-plan summary helpers already package dictionaries without pixels. | Medium if metadata schema or sidecar fields move; low only when the helper packages already-produced evidence without changing keys. | `compose_parity_contract_checkpoint.ps1`, `validate_compose_parity_contract_checkpoint.ps1`, docs readability guard, and no generated artifact audit. | Do not move renderer metadata yet. Use this branch only after a contract-only helper proves no schema drift. | Stop if field names, schema values, sidecar paths, or output metadata semantics would change. |
| B. Candidate touches timing summary but not renderer output | `build_layer_render_plan_phase_timing_runtime_packet` and related summary packets already exist. Warm-frame evidence shifted bottleneck interpretation toward compose phases. | Medium. Even if output pixels do not change, timing placement can change measured phase semantics. | Existing warm/repeated evidence scripts plus contract validators, but no UI operation readiness proof. | Defer timing extraction until a timing-only parity packet can compare before/after phase semantics. | Stop if timing boundaries, slowest phase selection, or bottleneck recommendation semantics would change. |
| C. Candidate touches generated artifact audit only | Current tasks repeatedly require checking that `state/`, PNG, and generated JSON are not staged/untracked. This audit is outside renderer execution and can be packaged as a helper/report. | Low. It reads Git/file status only and does not create artifacts or mutate renderer data. | `git status --short --branch`, staged name audit, untracked generated artifact scan, `git diff --check`, and checkpoint validators. | Recommended first future implementation candidate: add a generated artifact audit/report packaging helper that returns a machine-readable packet for no-state/no-PNG/no-JSON staged/untracked evidence. | Stop if the helper needs to read baseline/candidate render artifacts, run renderer, write `state/`, or infer visual parity. |
| D. Candidate touches pixels/alpha/layer ordering/Taichi/Qt | Preview PNG writer, compose execution, Taichi kernels, alpha blending, layer ordering, and Qt event-loop behavior are runtime/output surfaces. | High. These paths can change output pixels, ordering, user-visible behavior, or runtime readiness claims. | Existing contract-only evidence is insufficient for behavioral changes; visual parity and UI operation gates remain separate. | Do not touch in this phase. Require explicit o_1 approval plus parity evidence before any movement. | Stop immediately if a future slice touches pixels, alpha, layer ordering, Taichi kernels, Qt behavior, runtime merge, or output behavior. |

## Safest future helper candidate

Recommended candidate:

`GeneratedArtifactAuditPacket` / generated artifact audit report helper.

Implementation status:

- First helper extraction candidate: `render_core/generated_artifact_audit.py`.
- Helper entry: `build_generated_artifact_audit_packet(staged_paths, untracked_paths)`.
- Scope: package generated artifact audit evidence from caller-provided path lists only.
- Validation: `tests/test_generated_artifact_audit.py`.
- Validator: `scripts/validate_generated_artifact_audit_packet.py`.
- Validator test: `tests/test_generated_artifact_audit_validator.py`.
- Integration map: `docs/GENERATED_ARTIFACT_AUDIT_HELPER_INTEGRATION_MAP.zh-TW.md`.
- Boundary: this helper does not call Git, run renderer, launch Qt, read baseline/candidate artifacts, write files, or infer visual parity.

Candidate boundaries:

- Input: repo root plus optional staged/untracked file lists.
- Output: a machine-readable dict/JSON packet.
- Required fields: `schema`, `source`, `status`, `state_artifacts_staged`, `png_artifacts_staged`, `json_artifacts_staged`, `state_artifacts_untracked`, `png_artifacts_untracked`, `json_artifacts_untracked`, `generated_artifact_audit_passed`, `boundary`.
- Expected conservative values before commit: no generated `state/`, PNG, or JSON artifacts staged by the task.
- Must not run renderer, launch Qt, read baseline/candidate render artifacts, write files, change metadata schema, change output behavior, enable runtime merge, or make visual/interactive readiness claims.

Why this is the first safe candidate:

- It is evidence/report packaging only.
- It is independent from renderer pixels and metadata sidecar schema.
- It supports o_1/n_1 summaries without changing renderer behavior.
- It can be validated with existing contract-only scripts and Git status.
- It creates a reusable gate before future runtime or parity work.

## Rejected candidates for first implementation

- Metadata summary helper movement: already partially extracted, but moving more metadata assembly risks schema drift in `rrkal_displaytools.renderer_output_metadata.v1`.
- Timing/evidence packet movement: existing helpers are useful, but moving runtime timing boundaries can change measured phase semantics.
- Preview report helper movement: preview reporting is close to PNG artifact output and can be confused with UI or visual readiness evidence.
- Compose execution helper movement: blocked until pairwise parity evidence exists.
- Pixels/alpha/layer ordering/Taichi/Qt movement: not authorized in this phase.

## Preimplementation validation gate

Before implementing the recommended helper later, require:

- Existing worktree clean or dirty files explicitly classified.
- `scripts\compose_parity_contract_checkpoint.ps1` passes.
- `scripts\validate_compose_parity_contract_checkpoint.ps1` passes.
- `scripts\validate_compose_parity_contract_checkpoint.ps1 -SelfTestNegative` passes.
- Generated artifact audit confirms no task-created `state/`, PNG, or JSON artifacts staged/untracked.
- `git diff --check` passes.
- Touched docs pass UTF-8, U+FFFD, mojibake/PUA, and changed-hunk spot checks.

## Not authorized

This gate does not authorize:

- edits to `taichi_global_bathymetry.py`
- renderer hot path changes
- Taichi kernel changes
- Qt behavior changes
- metadata schema changes
- output behavior changes
- runtime merge
- visual parity readiness claims
- interactive FPS readiness claims
- CanvasStrategy implementation
- ViewCard consumption
- Odoriba handoff implementation

## Final classification

`c3_first_helper_extraction_preimplementation_gate_complete_l2_no_push`

Boundary statement:

This is a docs/evidence-only preimplementation gate. It recommends generated artifact audit/report packaging as the first safe future helper candidate and rejects pixels, alpha, layer ordering, Taichi, Qt, metadata schema, output behavior, runtime merge, CanvasStrategy, ViewCard, and Odoriba work for this phase.
