# Generated Artifact Audit Helper Integration Map

## TL;DR

This is a docs/evidence-only integration map for `GeneratedArtifactAuditPacket`.

Recommended next c_3 action:

Keep the helper isolated for one more slice and design a leaf evidence provider that supplies staged/untracked path lists to `build_generated_artifact_audit_packet`. Do not connect the helper to `compose_parity_contract_checkpoint.ps1` yet.

This map does not wire any script, checkpoint, renderer path, Qt path, runtime artifact path, CanvasStrategy, ViewCard, or Odoriba flow.

## Current helper surface

Source:

- `render_core/generated_artifact_audit.py`

Entry point:

- `build_generated_artifact_audit_packet(staged_paths, untracked_paths)`

Current validator:

- `scripts/validate_generated_artifact_audit_packet.py`
- `tests/test_generated_artifact_audit_validator.py`

Current helper test:

- `tests/test_generated_artifact_audit.py`

The helper is pure packet packaging from caller-provided path lists. It does not shell out, call Git, run renderer, launch Qt, read files, write files, inspect runtime artifacts, or infer image/runtime equivalence.

## Integration branch scan

| Branch | Candidate connection point | Evidence observed | Risk | Recommendation | Stop condition |
| ------ | -------------------------- | ----------------- | ---- | -------------- | -------------- |
| A | `scripts/compose_parity_contract_checkpoint.ps1` | The checkpoint currently aggregates compose gap packet and compose gap validator results. It also calls the negative validator path. | Medium. Connecting helper here too early can blur checkpoint-vs-validator-vs-meta-test boundaries. A checkpoint must aggregate leaf evidence only and must not call meta-tests. | Do not connect yet. First create a leaf provider that returns staged/untracked path lists without invoking tests. | Stop if the checkpoint would call `tests/*`, `--self-test-negative`, or the generated artifact validator. |
| B | `scripts/validate_generated_artifact_audit_packet.py` | Validator already checks conservative flags and in-memory negative mutations. | Low for validator-only work; medium if it starts gathering Git state or artifact state itself. Validators should validate packets, not collect external evidence. | Keep validator as in-memory packet validator. Do not make it collect runtime artifact state. | Stop if validator needs to read filesystem artifacts, execute renderer, or call checkpoint scripts. |
| C | Keep helper isolated; next slice designs a leaf evidence provider | Current helper and tests are isolated and caller-driven. This keeps evidence collection separate from packet validation. | Lowest risk. Slower, but preserves checkpoint/validator/meta-test separation. | Recommended. Next c_3 slice should design or add a small leaf provider that collects staged/untracked path lists and feeds the helper, without calling tests or renderer. | Stop if provider needs runtime artifact reads, PNG/JSON creation, or any renderer/Qt path. |
| D | Near `taichi_global_bathymetry.py`, renderer hot path, Taichi, Qt, preview output, compose output | These surfaces can affect pixels, layer ordering, runtime behavior, or user-facing operation. | High. Not appropriate for generated artifact audit helper wiring. | Do not touch. | Stop immediately if a connection requires renderer hot path, Taichi kernels, Qt behavior, metadata schema, output behavior, runtime merge, or runtime artifact generation. |

## Safe next connection shape

Recommended next slice:

`generated artifact audit leaf evidence provider`

Implementation status:

- Leaf provider: `scripts/generated_artifact_audit_leaf_provider.py`.
- Focused test: `tests/test_generated_artifact_audit_leaf_provider.py`.
- The provider queries only staged and untracked path lists, then passes them to `build_generated_artifact_audit_packet`.
- The provider does not call checkpoint scripts, validator scripts, tests, renderer, Qt, or runtime artifact generators.
- It prints one packet to stdout and does not write runtime artifact files.

Proposed shape:

- Script or helper returns path lists only:
  - staged paths
  - untracked paths
- It may call Git status commands with explicit timeout if implemented as a script.
- It must not call tests, checkpoint scripts, validator scripts, renderer scripts, Qt paths, or runtime artifact generators.
- It then passes those lists into `build_generated_artifact_audit_packet`.
- It emits one machine-readable packet for o_1/n_1 summary use.

Recommended packet flow:

```text
leaf evidence provider -> build_generated_artifact_audit_packet -> validator checks packet
```

Not recommended:

```text
checkpoint -> validator -> tests -> checkpoint
checkpoint -> negative self-test
validator -> checkpoint
renderer -> generated artifact audit helper
```

## Not-yet-authorized connection points

- `compose_parity_contract_checkpoint.ps1`
- `taichi_global_bathymetry.py`
- Qt panel/runtime code
- render output generation
- metadata sidecar schema builders
- compose output or preview output paths
- CanvasStrategy / ViewCard / Odoriba flows

## Validation expectations before any future wiring

Before any future wiring, require:

- `tests.test_generated_artifact_audit` passes.
- `tests.test_generated_artifact_audit_validator` passes.
- `scripts/validate_generated_artifact_audit_packet.py` passes.
- `scripts/validate_generated_artifact_audit_packet.py --self-test-negative` passes.
- Compose parity checkpoint and checkpoint validator still pass.
- Generated artifact audit confirms no task-created `state/`, PNG, or JSON runtime artifacts are staged/untracked.
- Docs readability guard passes if docs are touched.

## Final classification

`c3_generated_artifact_audit_helper_integration_mapping_complete_l2_no_push`

Boundary statement:

This is a docs/evidence-only integration map. It identifies the next safe connection shape for `GeneratedArtifactAuditPacket` and keeps the helper isolated for now. It does not wire checkpoint scripts, validators, renderers, Qt, runtime artifact producers, metadata schema builders, CanvasStrategy, ViewCard, or Odoriba flows.
