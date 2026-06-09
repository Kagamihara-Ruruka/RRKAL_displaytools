# Displaytools AIS / Aircraft Dynamic Point Boundary Fixture Gate

## Scope

本文件是 test/docs-only AIS / aircraft dynamic point boundary fixture gate。它只用 synthetic descriptor 測繪動態點圖層的資料來源、點 payload、投影 label、時間/replay label、selection label、render policy label、安全 ledger 與 known fault ledger。

本 gate 不修改 production source，不建立 helper module，不 import `taichi_global_bathymetry.py`，不執行 SQL / MySQL / WebSocket / live AIS / ADS-B，不讀 real AIS cache / network / database，不 import pandas / datashader / numpy runtime，不修改 projection / flip / mask formula，不啟動 renderer / Qt / VisPy / Taichi，不碰 controller selection runtime，也不宣稱 live data restored、bug fixed、readiness、visual parity 或 performance。

## Descriptor contract

Every descriptor has exactly these fields:

- `surface_name`
- `source_evidence`
- `input_frame`
- `consumer_layers`
- `policy_labels`
- `known_faults`
- `fixture_status`
- `forbidden_next_action`

Allowed `fixture_status` values:

- `pinned`
- `unresolved_static_only`
- `blocked_hot_path`

## Dynamic point boundary matrix

| descriptor_id | surface | input frame | fixture status | blocked next action |
| --- | --- | --- | --- | --- |
| `source_descriptor` | AIS / aircraft source descriptor | source lineage label | `unresolved_static_only` | do not execute SQL, WebSocket, live source, or cache source |
| `point_payload_descriptor` | dynamic point payload descriptor | raw lon/lat payload label | `pinned` | do not import pandas/datashader/numpy or parse real payload |
| `projection_label_descriptor` | dynamic point projection label descriptor | screen projection peer label | `unresolved_static_only` | do not change projection, flip, or mask formula |
| `time_replay_label_descriptor` | time / replay label descriptor | timestamp lineage label | `unresolved_static_only` | do not execute real clock, SQL, WebSocket, or live replay |
| `selection_descriptor` | dynamic point selection descriptor | selection label only | `unresolved_static_only` | do not mutate controller selection runtime |
| `render_policy_label_descriptor` | dynamic point render policy label descriptor | render policy label only | `pinned` | do not execute datashader or renderer runtime |
| `safety_ledger_descriptor` | dynamic point safety ledger descriptor | safety ledger label | `blocked_hot_path` | do not execute SQL, WebSocket, live source, datashader, or runtime source |
| `known_fault_ledger_descriptor` | dynamic point known fault ledger descriptor | known fault ledger label | `unresolved_static_only` | do not claim live data, bug fix, or visual parity |

## Fixture cases added

Focused tests live in:

- `tests/test_displaytools_dynamic_point_boundary.py`

The test module covers:

- AIS source descriptor
- ADS-B source descriptor
- replay source descriptor
- synthetic source descriptor
- unavailable source descriptor
- point payload lat/lon/speed/heading/timestamp/id labels
- projection label with no formula
- static replay label
- live lineage unresolved label
- selected vehicle descriptor
- selected layer descriptor
- hit false descriptor
- visible count, rendered count, cap, and adaptive sampling labels
- SQL/WebSocket/live-source blocked ledger
- live-vs-replay ambiguity fault
- timestamp staleness fault
- point/vector sync dependency fault

## Known unresolved faults

| fault | fixture treatment | blocked implementation action |
| --- | --- | --- |
| live-vs-replay ambiguity | known fault ledger only | do not claim live data restored |
| timestamp staleness | time/replay label and known fault ledger | do not execute real clock or live replay |
| point/vector sync dependency | projection label and known fault ledger | do not change projection, flip, or mask formula |
| controller selection runtime dependency | selection descriptor only | do not mutate controller selection runtime |
| datashader/runtime sampling dependency | render policy label only | do not import or execute datashader runtime |

## Explicit exclusions

Excluded from this gate:

- production `.py` source changes
- helper module creation
- monolith import
- SQL / MySQL / pymysql / sqlalchemy execution
- WebSocket / live AIS / ADS-B execution
- real AIS cache, network, or database reads
- pandas / datashader / numpy runtime imports
- projection / flip / mask formula changes
- renderer / Qt / VisPy / Taichi runtime execution
- controller selection runtime changes
- metadata/output schema changes
- runtime merge enablement
- live-data/readiness/bug-fix/visual parity/performance claims

## Recommended next gate

Recommended next gate:

- `dynamic_point_source_surface_movement_preimplementation_gate`

Reason:

- This fixture identifies source/payload/projection/time/selection/render-policy boundaries.
- SQL/WebSocket/live-source, datashader, projection formula, and controller selection runtime remain blocked.
- A source-surface movement gate should classify descriptor/policy/ledger candidates versus provider/runtime hot paths before any checker or source movement.

## Boundary Statement

Test/docs-only AIS/aircraft dynamic point boundary fixture gate. No production source change, no helper module creation, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache read, no pandas/datashader runtime, no projection/flip/mask formula change, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_dynamic_point_boundary_fixture_gate_ready_for_o1_review`
