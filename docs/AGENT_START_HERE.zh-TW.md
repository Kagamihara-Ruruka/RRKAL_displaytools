# Agent Start Here

## TL;DR

This is the first-read startup index for `RRKAL_displaytools` agents.

Use it to align the current workspace, evidence boundary, and no-overclaim rules before choosing any c_3 task. It is not a readiness certificate and does not authorize renderer behavior changes.

## Startup sequence

Run these checks first:

```powershell
git status --short --branch
git log -1 --oneline --decorate
```

Then read:

- `docs\AGENT_HANDOFF.zh-TW.md`
- `docs\PROJECT_GTD.md`
- `docs\DOCS_INDEX.zh-TW.md`

Use `README.md` for clone/setup commands and user-facing project overview.

## Coordination boundary

- GitHub commits, tests, smoke, and local evidence are product evidence.
- Notion Agents coordination is a dashboard for status, handoff, review requests, accepted decisions, and operations notes.
- Notion is not product evidence and is not renderer behavior authority.
- Cloud-drive `L:\AGENT_EXCHANGE` is historical/archive reference only. Do not write new primary coordination mail there.

## c_3 displaytools boundary

c_3 owns display/runtime evidence clarity for:

- renderer preview evidence
- compose parity contracts
- runtime/FPS/profiler evidence boundaries
- preview path and Qt preview operation gate design
- LOD counters and LayerRenderState evidence
- display consumer ViewCard boundary documents

c_3 must not directly read c_1 databases, c_2 manifests, c_4 assets, or raw data as part of display runtime work.

## Compose parity boundary

Current compose parity docs:

- `docs\COMPOSE_EXECUTION_SOURCE_MAP.zh-TW.md`
- `docs\COMPOSE_EXECUTION_PARITY_GATE.zh-TW.md`
- `docs\COMPOSE_PARITY_CONTRACT_ONLY_EVIDENCE_PACKET.zh-TW.md`
- `docs\COMPOSE_PARITY_PAIRWISE_COMPARISON_PLAN.zh-TW.md`

Current contract-only semantics:

- contract-only evidence means the contract exists and can be inspected.
- contract-only evidence is not visual parity.
- contract-only evidence is not precommit readiness.
- artifact diff mode is required before visual parity can be claimed.
- `precommit_gate_passed=null` and `precommit_gate_evaluated=false` are expected for compose parity `-ContractOnly` output.

## Stop conditions

Stop and report before editing if a task requires:

- `taichi_global_bathymetry.py` changes
- Qt code changes
- renderer hot path changes
- metadata schema changes
- output behavior changes
- runtime merge enablement
- artifact-generating render/smoke execution without explicit authorization
- CanvasStrategy implementation
- ViewCard consumption implementation
- Odoriba handoff implementation
- visual parity or interactive FPS readiness claims

## Boundary statement

This startup index is for c_3 startup alignment and evidence boundary clarity. It does not authorize renderer behavior changes, Qt behavior changes, metadata schema changes, output behavior changes, runtime merge, visual parity readiness, interactive FPS readiness, CanvasStrategy, ViewCard consumption, or Odoriba handoff.
