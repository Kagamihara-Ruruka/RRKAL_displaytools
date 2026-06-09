# Displaytools Dynamic Point Source / Lineage Minimal Extraction Gate

## Scope

本文件記錄 dynamic point source/lineage 的 minimal descriptor extraction gate。此 slice 建立 `render_core\dynamic_point_source_lineage_boundary.py`，只包含 AIS、ADS-B、replay、live lineage、source availability、timestamp quality、coordinate payload quality 與 known fault ledger 的 descriptor / policy / ledger helpers。

此 slice 不修改 `render_core\dynamic_point_boundary.py`，不修改 `taichi_global_bathymetry.py`，不修改 source-lineage import-boundary checker 行為，不執行 monolith 或 runtime。

## Evidence read

- `tests\test_displaytools_dynamic_point_source_lineage_minimal_extraction_planning.py`
- `tests\test_displaytools_dynamic_point_source_lineage_import_boundary.py`
- `scripts\validate_displaytools_dynamic_point_source_lineage_import_boundary.py`
- `tests\test_displaytools_dynamic_point_source_lineage_craton_ablation_matrix.py`
- `render_core\dynamic_point_boundary.py`
- current `taichi_global_bathymetry.py` remains read-only and is not imported or executed

## Exact helpers introduced

New helper module: `render_core\dynamic_point_source_lineage_boundary.py`

Introduced helpers:

- `build_dynamic_point_source_lineage_descriptor`
- `build_dynamic_point_replay_lineage_label_descriptor`
- `build_dynamic_point_live_lineage_label_descriptor`
- `build_dynamic_point_source_availability_descriptor`
- `build_dynamic_point_timestamp_quality_descriptor`
- `build_dynamic_point_coordinate_payload_quality_descriptor`
- `build_dynamic_point_source_lineage_known_fault_ledger`
- `dynamic_point_source_lineage_boundary_descriptor`
- `dynamic_point_source_lineage_planning_bundle`

All outputs are dict/list/scalar descriptor packets. The module imports only `from __future__ import annotations` and has no dependency on `render_core.dynamic_point_boundary` or `taichi_global_bathymetry.py`.

## Descriptor branches

Pinned descriptor branches:

| helper | branches |
| --- | --- |
| `build_dynamic_point_source_lineage_descriptor` | `ais_source`, `adsb_source`, `synthetic_source`, `unavailable_source`, fallback to unavailable |
| `build_dynamic_point_replay_lineage_label_descriptor` | `sql_replay_lineage` label only |
| `build_dynamic_point_live_lineage_label_descriptor` | `websocket_live_lineage` label only |
| `build_dynamic_point_source_availability_descriptor` | source availability labels and fallback to unavailable |
| `build_dynamic_point_timestamp_quality_descriptor` | `timestamp_quality`, `stale_timestamp`, `missing_timestamp` |
| `build_dynamic_point_coordinate_payload_quality_descriptor` | `coordinate_payload_quality`, `missing_lat_lon`, `invalid_lat_lon` |
| `build_dynamic_point_source_lineage_known_fault_ledger` | unresolved static-only known fault ledger |

## Fixture parity coverage

Helper tests cover:

- safe helper import
- exact key-set parity for every descriptor builder
- deterministic repeat-call parity
- dict/list/scalar-only output
- AIS source label branch
- ADS-B source label branch
- SQL replay lineage label branch
- WebSocket live lineage label branch
- synthetic source branch
- unavailable source branch
- timestamp quality branches
- coordinate payload quality branches
- source id / lineage status descriptor fields
- known fault ledger branch
- planning bundle guard flags
- no runtime, readiness, live-data, bug-fix, visual parity, performance, or safe-to-extract claims

## Import-boundary checker result

Checker: `scripts\validate_displaytools_dynamic_point_source_lineage_import_boundary.py`

Expected result for `render_core\dynamic_point_source_lineage_boundary.py`:

- `candidate_exists=true`
- `status=pass`
- `boundary_passed=true`
- `violations=[]`

The checker continues to allow string labels as data while blocking forbidden executable imports, names, attributes, call targets, function definitions, async function definitions, and class definitions.

## Explicit symbols and surfaces excluded

Excluded from this extraction:

- aggregate `render_core\dynamic_point_boundary.py` changes
- `taichi_global_bathymetry.py` changes
- SQL / MySQL / pymysql / sqlalchemy / DB URL / replay query execution
- WebSocket / live AIS / live ADS-B stream execution
- real AIS / ADS-B / cache / database read
- pandas / datashader / numpy runtime
- projection / flip / mask formula
- controller selection / picker / hit-test mutation
- renderer / Qt / VisPy / Taichi runtime
- metadata / artifact writer
- alpha / apply / composition hot path
- runtime merge enablement
- live-data, readiness, performance, visual parity, bug-fix, or safe-to-extract claims

## Cut-out note

This is a new second-layer helper module. No lines were removed from `render_core\dynamic_point_boundary.py` and no lines were removed from `taichi_global_bathymetry.py` because no same-name local descriptor definitions were moved from those files in this slice.

## Boundary statement

Minimal descriptor/policy/ledger-only dynamic point source/lineage boundary extraction. No aggregate dynamic point helper change, no monolith change, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula movement, no controller selection/picker/hit-test movement, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix/safe-to-extract claim.
