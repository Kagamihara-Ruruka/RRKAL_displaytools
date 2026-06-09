# Dynamic Point Payload / Coordinate Quality Boundary Fixture Gate

## Gate scope

本 gate 只釘住 dynamic point payload 與 coordinate quality 的 descriptor / ledger 外圍。它不建立 helper module，不移動 source，不修改 `render_core`、checker 或 `taichi_global_bathymetry.py`，也不讀 real AIS / ADS-B / cache / database。

## Evidence read

- Required startup HEAD: `a62442f test: add dynamic point cutout cartography gate`
- Required evidence scan: `rg -n "lat|lon|timestamp|source_id|speed|heading|stale|invalid|missing|dynamic_point" taichi_global_bathymetry.py render_core tests docs scripts`
- Static references to existing dynamic point helper shells, checker scripts, tests, and docs

The evidence scan shows payload fields and timestamp handling in the monolith and existing descriptor shells. This gate records those as static evidence only and does not import or execute them.

## Payload / coordinate quality fixture matrix summary

| Family | Cases | Status |
| --- | --- | --- |
| Payload fields | `lat`, `lon`, `timestamp`, `source_id`, `speed`, `heading` | `pinned` |
| Quality labels | `valid`, `missing`, `invalid`, `stale`, `unknown` | `pinned` |
| Coordinate cases | missing lat/lon, invalid lat/lon, out-of-range lat/lon, zero coordinate candidate, anti-meridian candidate | `unresolved_static_only` |
| Timestamp cases | missing timestamp, stale timestamp, future timestamp candidate, timezone ambiguity label | `unresolved_static_only` |
| Source id cases | missing id, synthetic id, AIS id, ADS-B id | mixed `unresolved_static_only` and `pinned` |
| Runtime blockers | SQL/WebSocket/live, real cache/database read, pandas/Datashader/NumPy, projection/flip/mask, controller/picker/hit-test, renderer/Qt/VisPy/Taichi | `blocked_runtime_only` |

## Fixture cases added

- payload field descriptors for `lat`, `lon`, `timestamp`, `source_id`, `speed`, and `heading`
- quality label descriptors for `valid`, `missing`, `invalid`, `stale`, and `unknown`
- coordinate quality descriptors for missing lat/lon, invalid lat/lon, out-of-range lat/lon, zero coordinate candidate, and anti-meridian candidate
- timestamp quality descriptors for missing timestamp, stale timestamp, future timestamp candidate, and timezone ambiguity label
- source id descriptors for missing id, synthetic id, AIS id, and ADS-B id
- known fault ledger for timestamp staleness, coordinate payload ambiguity, and point/vector sync dependency
- runtime blocker descriptors for SQL/WebSocket/live source, real cache/database reads, dataframe runtime, projection formula, controller selection, picker/hit-test, and renderer host runtime

## Known unresolved faults

- timestamp staleness
- coordinate payload ambiguity
- point/vector sync dependency

These faults remain static ledger entries only. The gate does not claim that coordinate projection, renderer display, live source lineage, or timestamp handling has been corrected.

## Explicit exclusions

This gate does not:

- create helper modules
- move source
- modify `render_core/*.py`
- modify `taichi_global_bathymetry.py`
- modify checker scripts
- import or execute the monolith
- read real AIS, ADS-B, cache, or database data
- execute SQL, WebSocket, or live-source paths
- import pandas, Datashader, or NumPy runtime
- change projection, flip, mask, controller, picker, hit-test, renderer, Qt, VisPy, or Taichi behavior
- claim readiness, safe-to-extract, bug fix, visual parity, performance, or live-data readiness

## Recommended next gate

`dynamic_point_payload_coordinate_quality_craton_ablation_matrix_gate`

Reason: the payload and quality descriptors are now pinned as data-only fixture surfaces. The next gate should use a craton ablation matrix to test which consumers would degrade when payload, coordinate, timestamp, or source-id labels are temporarily removed, substituted, traced, or tripped.

## Boundary statement

Docs/test-only dynamic point payload/coordinate quality boundary fixture gate. No helper module creation, no source movement, no production source change, no checker change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix/safe-to-extract claim.