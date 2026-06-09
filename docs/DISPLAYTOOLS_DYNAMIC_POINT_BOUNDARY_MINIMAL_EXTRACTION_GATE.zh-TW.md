# Displaytools AIS / Aircraft Dynamic Point Boundary Minimal Extraction Gate

## Scope

本文件記錄 AIS / aircraft dynamic point boundary 的 minimal descriptor/policy/ledger-only extraction。此 slice 建立 `render_core\dynamic_point_boundary.py`，但不修改 `taichi_global_bathymetry.py`，因為 static source search 未找到可安全搬移的同名 descriptor / policy / ledger definitions。

此 gate 只建立純 helper module、fixture parity tests、import-boundary checker candidate pass 與文件索引。不執行 SQL、WebSocket、live source、database、cache、pandas、datashader、numpy、projection、controller、renderer、Qt、VisPy 或 Taichi runtime。

## a_1 macro observer acceptance

`a_1` macro observer result is treated as `accept_with_conditions` for descriptor/policy/ledger-only movement. The readable stop lines require:

- descriptor / policy / ledger only
- no SQL replay database
- no WebSocket or live AIS / ADS-B
- no real cache or database read
- no pandas, datashader, or numpy runtime
- no projection, flip, or mask formula
- no controller selection, picker, or hit-test mutation
- no renderer, Qt, VisPy, or Taichi runtime
- checker must pass
- no live-data, readiness, visual parity, performance, bug-fix, or safe-to-extract claim

The lab document contains mojibake in some Chinese text, so this product doc records only the readable macro decision and stop-line summary.

## Helpers introduced

| helper | content kind | runtime dependency allowed |
| --- | --- | --- |
| `build_dynamic_point_source_descriptor` | source label descriptor | `false` |
| `build_dynamic_point_payload_shape_descriptor` | payload shape descriptor | `false` |
| `build_dynamic_point_replay_live_lineage_descriptor` | replay/live lineage unresolved descriptor | `false` |
| `build_dynamic_point_selection_label_descriptor` | selection label descriptor | `false` |
| `build_dynamic_point_render_policy_label_descriptor` | render policy label descriptor | `false` |
| `build_dynamic_point_safety_ledger_descriptor` | blocked runtime safety ledger | `false` |
| `build_dynamic_point_known_fault_ledger_descriptor` | unresolved known fault ledger | `false` |
| `dynamic_point_boundary_descriptor` | aggregate boundary descriptor | `false` |
| `dynamic_point_planning_bundle` | planning bundle descriptor | `false` |

All helpers return dict/list/scalar data only. They do not return runtime objects, callables, module references, database handles, dataframe objects, or render buffers.

## Explicit exclusions

This extraction excludes:

- SQL / MySQL / pymysql / sqlalchemy / replay query
- WebSocket / live AIS / live ADS-B
- real AIS / ADS-B / cache / database reads
- pandas / datashader / numpy runtime
- projection / flip / mask formula
- controller selection / picker / hit-test mutation
- renderer / Qt / VisPy / Taichi runtime
- metadata / artifact writers
- alpha / apply / composition hot path
- runtime merge enablement
- live-data, readiness, visual parity, performance, bug-fix, or safe-to-extract claims

## Import-boundary checker result expectation

`validate_displaytools_dynamic_point_import_boundary.py` must pass against `render_core\dynamic_point_boundary.py`.

Expected candidate result:

- `candidate_exists = true`
- `status = pass`
- `boundary_passed = true`
- `violations = []`

The negative self-test must still detect all forbidden snippets.

## Fixture parity coverage

The helper fixture parity test pins:

- safe helper module import
- exact key sets for every descriptor builder
- deterministic repeat-call parity
- dict/list/scalar-only output
- source descriptor branches
- replay/live lineage branches
- payload shape descriptor branch
- selection label descriptor branch
- render policy label descriptor branch
- safety ledger branch
- known fault ledger branch
- planning bundle guard flags
- no runtime, readiness, live-data, bug-fix, or safe-to-extract claims

## Monolith touch summary

`taichi_global_bathymetry.py` is not touched in this slice. No local same-name descriptor / policy / ledger definitions were found for safe source removal or re-export wiring.

## Cut-out note

This is a minimal descriptor/policy/ledger helper creation. It does not move runtime behavior out of the monolith. It does not prove live data, rendering correctness, visual parity, performance readiness, or safe extraction of runtime surfaces.

## Boundary statement

Minimal descriptor/policy/ledger-only dynamic point boundary extraction after a_1 macro observer. No SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula movement, no controller selection/picker/hit-test movement, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix/safe-to-extract claim.
