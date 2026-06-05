# Compose Parity Contract-Only Evidence Packet

## TL;DR

This packet records contract-only compose parity evidence collected without launching Qt, Taichi rendering, artifact-generating smoke, or renderer state mutation.

Contract-only evidence proves:

- the current compose parity smoke contract exists
- the artifact runner contract exists
- the review packet exposes zero-diff parity requirements
- runtime merge remains disabled
- no artifact parity is available yet

Contract-only evidence does not prove:

- visual parity
- pixel equality
- alpha blending correctness after movement
- layer ordering correctness after movement
- metadata baseline-vs-candidate compatibility
- interactive FPS readiness

## Commands run

All commands were run from `L:\RRKAL_displaytools`.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\render_compose_parity_smoke.ps1 -ContractOnly
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\render_compose_parity_artifacts.ps1 -ContractOnly
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\inspect_render_plan_review_packet.ps1 -ContractOnly
```

No artifact-generating mode was run.

## Evidence summary

### `render_compose_parity_smoke.ps1 -ContractOnly`

Observed packet summary:

| Field | Value |
| ----- | ----- |
| `schema` | `rrkal_displaytools.render_compose_parity_smoke.v1` |
| `status` | `contract_only_forced` |
| `mode` | `contract_only_no_render_side_effect` |
| `runtime_merge_enabled` | `false` |
| `contract_only` | `true` |
| `artifacts_present` | `false` |
| `artifact_parity_ready` | `false` |
| `visual_parity_passed` | `null` |
| `max_abs_diff` | `null` |
| `changed_pixel_count` | `null` |
| `notification_reason` | `contract_only_no_render_side_effect` |

What this proves:

- The parity smoke contract is callable without rendering.
- The contract-only path does not claim artifact parity.
- Runtime merge remains disabled.

What this does not prove:

- No baseline/candidate PNG diff was executed.
- No visual parity was measured.
- No pixel or metadata output equivalence was established.

### `render_compose_parity_artifacts.ps1 -ContractOnly`

Observed packet summary:

| Field | Value |
| ----- | ----- |
| `schema` | `rrkal_displaytools.compose_run_parity_artifact_runner.v1` |
| `status` | `contract_only_no_render_side_effect` |
| `contract_only` | `true` |
| `runtime_merge_enabled` | `false` |
| `artifact_dir` | `state/compose_parity` |
| `boundary` | Contract-only mode does not create artifact directories, launch Taichi, render frames, diff images, write manifests, or enable runtime merge. |

What this proves:

- The artifact runner contract is available.
- Required artifact location is declared.
- Contract-only mode does not generate parity artifacts.
- Runtime merge remains disabled.

What this does not prove:

- Baseline and candidate artifacts were not generated.
- Artifact diff was not run.
- Precommit visual parity did not pass because it was not measured.

### `inspect_render_plan_review_packet.ps1 -ContractOnly`

Observed packet summary:

| Field | Value |
| ----- | ----- |
| `schema` | `rrkal_displaytools.render_plan_review_packet.v1` |
| `status` | `contract_only_no_runtime` |
| `zero_diff_parity_source_script` | `scripts\render_compose_parity_smoke.ps1` |
| `zero_diff_parity_manifest_path` | `state/render_compose_parity_smoke_manifest.json` |
| `zero_diff_parity_artifact_producer_script` | `scripts\render_compose_parity_artifacts.ps1` |
| `zero_diff_parity_artifact_runner_schema` | `rrkal_displaytools.compose_run_parity_artifact_runner.v1` |
| `zero_diff_parity_precommit_gate_field` | `render_compose_parity_smoke.precommit_gate_passed` |
| `boundary` | Reviewer packet only; it does not launch Qt, Taichi, render frames, write metadata, or enable runtime single-pass composition. |

What this proves:

- The review packet links compose parity smoke, artifact runner, manifest path, and precommit gate field.
- The review packet is contract-only and does not invoke runtime rendering.

What this does not prove:

- The linked manifest exists.
- The linked precommit gate has passed.
- Runtime single-pass or compose movement is safe.

## Current contract-only capability matrix

| Branch | Current contract-only evidence | Status |
| ------ | ------------------------------ | ------ |
| Queue building parity | Parity design requires this, but no pairwise queue packet comparator exists yet. | `missing_evidence` |
| Skip reason parity | Parity design requires this, but no pairwise skip reason comparator exists yet. | `missing_evidence` |
| Dispatch path parity | Dispatch packet contract exists, but no baseline/candidate pair comparison exists yet. | `contract_exists_missing_pair_evidence` |
| Timing packet parity | Timing packet schema exists, but no baseline/candidate timing compatibility comparison exists yet. | `contract_exists_missing_pair_evidence` |
| Metadata summary parity | Summary fields exist, but no baseline/candidate metadata sidecar comparison exists yet. | `contract_exists_missing_pair_evidence` |
| Alpha/layer ordering parity | Artifact diff contract exists. | `contract_exists_missing_artifacts` |
| Generated artifact audit | Contract-only commands left the working tree clean. | `pass_for_this_packet` |
| Runtime merge state | Contract-only packets report `runtime_merge_enabled=false`. | `pass_contract_only` |

## Missing evidence before compose execution movement

Required before any renderer hot path change:

1. Pairwise queue packet comparison.
2. Pairwise skip reason comparison.
3. Pairwise dispatch path comparison.
4. Baseline vs candidate metadata sidecar comparison.
5. Baseline sequential RGBA artifact.
6. Candidate moved/refactored RGBA artifact.
7. Pixel diff with `max_abs_diff=0`.
8. Pixel diff with `changed_pixel_count=0`.
9. Generated artifact audit proving no `state/` PNG/JSON is staged.
10. o_1/u_o review before any runtime behavior move.

## Generated artifact audit

Observed after running the three contract-only commands:

- `git status --short --branch` remained clean before creating this docs packet.
- No `state/` PNG/JSON was created by the contract-only commands.
- No generated artifact was staged by this task.

Required before any future commit touching parity evidence:

```powershell
git status --short --branch
git diff --cached --name-only -- state
```

Pass condition:

- no `state/` PNG/JSON appears in the staged file list.

## Not authorized by this packet

This packet does not authorize:

- editing `taichi_global_bathymetry.py`
- editing Qt code
- changing renderer behavior
- changing metadata schema
- changing output behavior
- enabling runtime merge
- running artifact-generating parity mode
- staging `state/` PNG/JSON artifacts
- claiming interactive FPS readiness
- implementing CanvasStrategy
- implementing ViewCard consumption
- implementing Odoriba handoff

## Final classification

`c3_compose_parity_contract_only_evidence_packet_complete_l2_no_push`

Boundary statement:

This is a contract-only compose parity evidence packet. It records what existing contract-only scripts can prove and what evidence remains missing before compose execution movement. It does not modify renderer hot path code, Qt code, metadata schema, output behavior, runtime merge, artifact-generating smoke, CanvasStrategy, ViewCard consumption, Odoriba handoff, or interactive FPS readiness.
