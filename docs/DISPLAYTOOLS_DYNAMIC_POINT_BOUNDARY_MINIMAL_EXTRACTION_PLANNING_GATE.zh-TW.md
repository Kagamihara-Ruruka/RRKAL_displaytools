# Displaytools AIS / Aircraft Dynamic Point Boundary Minimal Extraction Planning Gate

## Scope

本文件是 docs/test-only AIS / aircraft dynamic point boundary minimal extraction planning gate。它只規劃未來 `render_core\dynamic_point_boundary.py` 的 descriptor / policy / ledger-only 候選範圍，不建立 helper module，不移動 source，不修改 production source。

本 gate 不 import monolith，不執行 SQL / WebSocket / live source，不讀 real AIS / ADS-B / cache / database，不 import pandas / datashader / numpy runtime，不修改 projection / flip / mask formula，不碰 controller selection runtime，不啟動 renderer / Qt / VisPy / Taichi，不碰 metadata/output writer，也不宣稱 live-data、readiness 或 bug fix。

## Candidate target summary

| field | value |
| --- | --- |
| `target_candidate` | `render_core\dynamic_point_boundary.py` |
| `helper_module_creation_authorized` | `false` |
| `source_movement_authorized` | `false` |
| `dynamic_point_planning_candidate` | `true` |
| `dynamic_point_extraction_candidate` | `false` |
| `a1_macro_observer_required_before_source_movement` | `true` |
| `import_boundary_checker_required_before_extraction` | `true` |

The target path is hypothetical only and must not be created in this slice.

## Candidate descriptor families

Every candidate is limited to dict/list/scalar descriptor builders or policy/ledger tables.

| candidate | required fixture | forbidden next action |
| --- | --- | --- |
| `build_dynamic_point_source_descriptor` | source descriptor exact key-set and repeat-call parity | do not execute SQL, WebSocket, live source, or cache source |
| `build_dynamic_point_payload_shape_descriptor` | payload shape descriptor exact key-set parity | do not parse real payload or import dataframe runtime |
| `build_dynamic_point_replay_live_lineage_descriptor` | replay/live lineage unresolved branch parity | do not execute replay query, WebSocket, or real clock |
| `build_dynamic_point_selection_label_descriptor` | selection label-only parity | do not mutate controller selection runtime |
| `build_dynamic_point_render_policy_label_descriptor` | render policy label-only parity | do not execute datashader or renderer runtime |
| `build_dynamic_point_safety_ledger_descriptor` | blocked-source safety ledger parity | do not execute SQL, WebSocket, live source, datashader, or runtime source |
| `build_dynamic_point_known_fault_ledger_descriptor` | known fault unresolved ledger parity | do not claim live data, bug fix, or visual parity |
| `dynamic_point_boundary_descriptor` | aggregate descriptor exact key-set parity | do not include SQL/live/dataframe/projection/controller/runtime behavior |
| `dynamic_point_planning_bundle` | bundle key-set and blocked-surface declaration parity | do not authorize source movement inside bundle |

Each candidate must keep:

- `runtime_dependency_allowed = false`
- `sql_live_source_execution_allowed = false`
- `dataframe_runtime_allowed = false`
- `projection_formula_allowed = false`
- `controller_selection_runtime_allowed = false`
- `renderer_runtime_allowed = false`
- `candidate_for_minimal_extraction = true`

## Blocked surfaces

Blocked from first cut:

- SQL / MySQL / pymysql / sqlalchemy / replay query
- WebSocket / live AIS / live ADS-B
- real AIS / ADS-B / cache / DB reads
- pandas / datashader / numpy runtime
- projection / flip / mask formula
- controller selection / picker / hit-test mutation
- renderer / Qt / VisPy / Taichi runtime
- metadata/artifact writers
- alpha/apply/composition hot path

These surfaces remain blocked because they execute IO, read real data, process runtime dataframe/array payloads, change coordinate behavior, mutate controller selection state, require renderer/UI/GPU runtime, or affect output/artifact/hot-path behavior.

## Fixture parity plan

Future extraction planning must require:

- exact key-set parity for descriptor builders
- deterministic repeat-call parity
- source descriptor branch
- point payload shape descriptor branch
- replay/live lineage descriptor branch
- selection label descriptor branch
- render policy label descriptor branch
- safety ledger blocked-source branch
- known fault unresolved ledger branch
- future import-boundary checker missing target pass
- future forbidden SQL/live/dataframe/projection/controller/runtime dependency fail

## Import-boundary checker need assessment

Future checker is required before extraction.

Current planning state:

- `required_before_extraction = true`
- `required_now = false`
- `future_checker_target = render_core\dynamic_point_boundary.py`
- `target_missing_now = true`

Reason:

- This slice is planning-only.
- No helper module is created.
- A checker should be introduced after the target is planned and before any source movement.

## a_1 macro observer requirement

`a_1` macro observer review is required before source movement.

Questions for that observer:

- Are the candidate descriptor families still one descriptor/policy/ledger craton.
- Did any SQL replay, live stream, dataframe runtime, projection formula, controller selection mutation, or renderer host behavior leak into the candidate set.
- Are live-vs-replay ambiguity, timestamp staleness, and point/vector sync dependency still unresolved ledger items.
- Is there a smaller first-cut candidate than the listed aggregate target.
- Is additional historical or horizontal graph evidence needed before movement.

## Recommended next gate

Recommended next gate:

- `dynamic_point_import_boundary_checker_gate`

That next gate should still be tooling/docs-only. It should validate a missing candidate target, allow safe string labels, and block SQL/live/dataframe/projection/controller/runtime dependencies before any helper module is created.

## Boundary Statement

Docs/test-only AIS/aircraft dynamic point boundary minimal extraction planning gate. No helper module creation, no source movement, no production source change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection runtime change, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_dynamic_point_boundary_minimal_extraction_planning_gate_ready_for_o1_review`
