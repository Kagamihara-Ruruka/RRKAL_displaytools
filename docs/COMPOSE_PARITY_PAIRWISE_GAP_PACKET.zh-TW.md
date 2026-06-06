# Compose Parity Pairwise Gap Packet

## TL;DR

This document describes `scripts\compare_compose_pairwise_packet.ps1 -ContractOnly`.

The script emits a machine-readable JSON packet that names the current compose parity gaps before any renderer movement:

- queue parity is not run because the candidate packet is missing.
- skip parity is not run because the candidate packet is missing.
- dispatch parity is not run because the candidate packet is missing.
- timing packet parity is not run because the candidate packet is missing.
- metadata sidecar parity is not run because the candidate sidecar is missing.
- artifact parity is not run because baseline/candidate artifacts are missing.
- visual parity is not evaluated.
- precommit gate is not evaluated in contract-only mode.

This is contract-only tooling. It does not run the renderer, launch Qt, create PNG/JSON artifacts, change metadata schema, change output behavior, enable runtime merge, or claim visual parity / interactive FPS readiness.

## Command

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\compare_compose_pairwise_packet.ps1 -ContractOnly
```

The script supports `-ContractOnly` only. Running it without `-ContractOnly` is intentionally rejected.

Validator:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\validate_compose_pairwise_gap_packet.ps1 -ContractOnly
```

The validator checks the contract-only JSON for false readiness signals. It fails if contract-only output claims visual parity, precommit readiness, runtime merge, generated artifacts, metadata schema change, output behavior change, or an evaluated parity branch.

Negative self-test:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\validate_compose_pairwise_gap_packet.ps1 -ContractOnly -SelfTestNegative
```

The negative self-test mutates an in-memory copy of the contract-only packet and verifies the validator detects these false readiness signals:

- `visual_parity_passed=true`
- `precommit_gate_passed=true`
- `precommit_gate_evaluated=true`
- `runtime_merge_enabled=true`

It does not read baseline/candidate artifacts and does not write `state/` outputs.

## Contract checkpoint bundle

Use:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\compose_parity_contract_checkpoint.ps1
```

This checkpoint bundle runs the contract-only gap packet, the normal validator, and the negative self-test validator together. Its checkpoint JSON must preserve `contract_only=true`, `runtime_merge_enabled=false`, `visual_parity_passed=null`, `precommit_gate_passed=null`, and `precommit_gate_evaluated=false`.

For o_1 / n_1 summary use, the checkpoint JSON also repeats `missing_evidence`, `artifact_parity_ready=false`, `visual_parity_ready=false`, and `negative_self_test_detected_all_false_readiness_mutations=true`.

The bundle is still contract-only. It does not run renderer, launch Qt, read baseline/candidate artifacts, write `state/` outputs, generate PNG/JSON artifacts, change metadata schema, change output behavior, enable runtime merge, or claim visual parity / precommit / interactive FPS readiness.

Checkpoint validator:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\validate_compose_parity_contract_checkpoint.ps1
```

The checkpoint validator confirms the checkpoint JSON keeps conservative contract-only fields, keeps `missing_evidence` non-empty, and keeps artifact / visual readiness flags false. Its optional `-SelfTestNegative` mode mutates an in-memory checkpoint copy and verifies false readiness flags are detected.

## Required output fields

The packet includes:

- `schema`
- `source`
- `status`
- `contract_only`
- `runtime_merge_enabled`
- `queue_parity`
- `skip_parity`
- `dispatch_parity`
- `timing_packet_parity`
- `metadata_sidecar_parity`
- `artifact_parity`
- `visual_parity_passed`
- `precommit_gate_passed`
- `precommit_gate_evaluated`
- `precommit_gate_status`
- `missing_evidence`
- `boundary`

## Expected contract-only semantics

| Field | Expected value |
| ----- | -------------- |
| `status` | `contract_only_no_runtime` |
| `contract_only` | `true` |
| `runtime_merge_enabled` | `false` |
| `queue_parity.status` | `not_run` |
| `queue_parity.reason` | `missing_candidate` |
| `skip_parity.status` | `not_run` |
| `skip_parity.reason` | `missing_candidate` |
| `dispatch_parity.status` | `not_run` |
| `dispatch_parity.reason` | `missing_candidate` |
| `timing_packet_parity.status` | `not_run` |
| `timing_packet_parity.reason` | `missing_candidate` |
| `metadata_sidecar_parity.status` | `not_run` |
| `metadata_sidecar_parity.reason` | `missing_candidate` |
| `artifact_parity.status` | `not_run` |
| `artifact_parity.reason` | `missing_artifacts` |
| `visual_parity_passed` | `null` |
| `precommit_gate_passed` | `null` |
| `precommit_gate_evaluated` | `false` |
| `precommit_gate_status` | `not_evaluated_contract_only` |

## Missing evidence surfaced by the packet

The packet names missing evidence that must exist before compose execution movement:

- baseline queue packet
- candidate queue packet
- baseline skip reason packet
- candidate skip reason packet
- baseline dispatch packet
- candidate dispatch packet
- baseline timing packet
- candidate timing packet
- baseline metadata sidecar
- candidate metadata sidecar
- baseline sequential RGBA artifact
- merged candidate RGBA artifact
- artifact diff manifest

## Relationship to existing compose parity docs

This script implements the contract-only gap packet proposed by:

- `docs\COMPOSE_PARITY_PAIRWISE_COMPARISON_PLAN.zh-TW.md`
- `docs\COMPOSE_EXECUTION_PARITY_GATE.zh-TW.md`
- `docs\COMPOSE_PARITY_CONTRACT_ONLY_EVIDENCE_PACKET.zh-TW.md`

It does not replace artifact diff parity. It only makes the missing branches machine-readable.

The validator keeps that machine-readable packet honest by checking:

- `contract_only=true`
- `runtime_merge_enabled=false`
- `visual_parity_passed=null`
- `precommit_gate_passed=null`
- `precommit_gate_evaluated=false`
- `precommit_gate_status=not_evaluated_contract_only`
- queue/skip/dispatch/timing/metadata branches are `not_run / missing_candidate`
- artifact parity is `not_run / missing_artifacts`

## Not authorized

This tooling does not authorize:

- editing `taichi_global_bathymetry.py`
- editing Qt code
- renderer hot path changes
- metadata schema changes
- output behavior changes
- artifact-generating render
- staging `state/`, PNG, or generated JSON artifacts
- runtime merge
- visual parity readiness claims
- interactive FPS readiness claims
- CanvasStrategy
- ViewCard consumption
- Odoriba handoff

## Final classification

`c3_compose_parity_pairwise_gap_packet_complete_l2_no_push`

Boundary statement:

This is contract-only compose parity tooling. It emits a machine-readable gap packet for queue, skip, dispatch, timing, metadata, and artifact parity without renderer execution, Qt execution, metadata schema changes, output behavior changes, artifact generation, runtime merge, visual parity readiness, or interactive FPS readiness.
