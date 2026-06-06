# Normalizer Fixture Parity Gate

## TL;DR

This gate covers `normalize_ais_frame` and `normalize_aircraft_frame` in `taichi_global_bathymetry.py`.

The purpose is to define fixture parity expectations for DataFrame normalization behavior before any future normalizer fixture tests are added. This document does not approve parser extraction, normalizer extraction, renderer movement, UI readiness, visual parity, runtime merge, or helper movement.

## Static normalizer inventory

| symbol | anchor | classification | direct dependencies | globals used | files/cache/artifacts | renderer/Qt/Taichi runtime |
| --- | --- | --- | --- | --- | --- | --- |
| `normalize_ais_frame` | `taichi_global_bathymetry.py:1286` | `normalizer_fixture_candidate` | `find_column`, `LAT_ALIASES`, `LON_ALIASES`, `COLUMN_ALIASES`, `pd.to_numeric` | alias tuples/maps only | none observed | none observed |
| `normalize_aircraft_frame` | `taichi_global_bathymetry.py:1331` | `normalizer_fixture_candidate` | `find_column`, `LAT_ALIASES`, `LON_ALIASES`, `AIRCRAFT_COLUMN_ALIASES`, `pd.to_numeric`, `np.nan` | alias tuples/maps only | none observed | none observed |

Direct alias dependencies observed:

- Latitude aliases: `lat`, `latitude`, `y`, `position.lat`, `position.latitude`, `navigation.lat`, `ais.lat`.
- Longitude aliases: `lon`, `lng`, `long`, `longitude`, `x`, `position.lon`, `position.lng`, `position.longitude`, `navigation.lon`, `ais.lon`.
- AIS target aliases: `mmsi`, `sog`, `cog`, `heading`, `timestamp`, `name`.
- Aircraft target aliases: `icao24`, `callsign`, `altitude_m`, `altitude_ft`, `speed_kt`, `speed_ms`, `heading`, `timestamp`.

No file IO, cache write, preview artifact, renderer controller, Qt widget, VisPy viewer, or Taichi kernel call is observed inside either normalizer.

## AIS fixture matrix

| fixture | input DataFrame shape | expected output columns | alias mapping | missing/null behavior | dtype/coercion | failure mode | globals/cache/files touched |
| --- | --- | --- | --- | --- | --- | --- | --- |
| canonical coordinates | columns `lat`, `lon` | at least `lat`, `lon` | direct canonical columns | rows with valid coordinates retained | coordinates coerced numeric | none expected | none |
| coordinate aliases | columns such as `latitude`, `longitude` or `position.lat`, `position.lon` | normalized `lat`, `lon` | first matching alias via `find_column` | rows with valid coordinates retained | coordinates coerced numeric | none expected | none |
| missing coordinate fields | no latitude or no longitude alias | no output; raises | not applicable | not applicable | not applicable | `ValueError` mentioning available columns | none |
| null coordinate rows | lat/lon values include null or nonnumeric text | valid rows only | canonical or alias | rows with null/coerced-null coordinates dropped | `pd.to_numeric(..., errors="coerce")` | none expected if at least one valid row remains | none |
| coordinate bounds | lat outside `[-90, 90]` or lon outside normalized range after wrap | valid bounded rows only | canonical or alias | out-of-range lat rows removed; lon is wrapped then bounded | lon normalized to `[-180, 180]` | none expected | none |
| AIS optional columns | aliases for `mmsi`, `sog`, `cog`, `heading`, `timestamp`, `name` | matching target columns copied when observed | `COLUMN_ALIASES` | absent optional columns are omitted | `sog`, `cog`, `heading` coerced numeric if present | none expected | none |
| empty input | empty DataFrame | `lon`, `lat`, `mmsi`, `sog`, `cog`, `heading`, `timestamp` | not applicable | returns empty schema frame | no coercion | none expected | none |

Observed AIS behavior:

- `name` can be copied when present through `COLUMN_ALIASES`, but it is not included in the empty-frame schema.
- MMSI is copied, not numerically coerced in the current implementation.
- Callsign-style AIS column normalization is not observed in current implementation.

## Aircraft fixture matrix

| fixture | input DataFrame shape | expected output columns | alias mapping | missing/null behavior | dtype/coercion | failure mode | globals/cache/files touched |
| --- | --- | --- | --- | --- | --- | --- | --- |
| canonical coordinates | columns `lat`, `lon` | at least `lat`, `lon` | direct canonical columns | rows with valid coordinates retained | coordinates coerced numeric | none expected | none |
| coordinate aliases | columns such as `latitude`, `longitude` or `position.lat`, `position.lon` | normalized `lat`, `lon` | first matching alias via `find_column` | rows with valid coordinates retained | coordinates coerced numeric | none expected | none |
| missing coordinate fields | no latitude or no longitude alias | no output; raises | not applicable | not applicable | not applicable | `ValueError` mentioning available columns | none |
| null coordinate rows | lat/lon values include null or nonnumeric text | valid rows only | canonical or alias | rows with null/coerced-null coordinates dropped | `pd.to_numeric(..., errors="coerce")` | none expected if at least one valid row remains | none |
| aircraft identity columns | aliases for `icao24`, `callsign` | matching target columns copied when observed | `AIRCRAFT_COLUMN_ALIASES` | absent identity columns are omitted | copied as-is | none expected | none |
| altitude in meters | `altitude_m` or meter aliases | `altitude_m` | meter aliases | absent meter altitude may be derived or defaulted | coerced numeric | none expected | none |
| altitude in feet only | `altitude_ft` or feet aliases | `altitude_ft`, derived `altitude_m` | feet aliases | `altitude_m` created from feet when meter source absent | feet coerced numeric; meters = feet * 0.3048 | none expected | none |
| speed in knots | `speed_kt` or knot aliases | `speed_kt` | knot aliases | absent speed may be derived or defaulted | coerced numeric | none expected | none |
| speed in m/s only | `speed_ms` or m/s aliases | `speed_ms`, derived `speed_kt` | m/s aliases | `speed_kt` created from m/s when knot source absent | m/s coerced numeric; kt = m/s * 1.943844 | none expected | none |
| missing altitude/speed | valid coordinates but no altitude/speed source | includes default `altitude_m`, `speed_kt` | not applicable | altitude defaults to `0.0`; speed defaults to `np.nan` | default values inserted | none expected | none |
| empty input | empty DataFrame | `lon`, `lat`, `icao24`, `callsign`, `altitude_m`, `speed_kt`, `heading`, `timestamp` | not applicable | returns empty schema frame | no coercion | none expected | none |

Observed aircraft behavior:

- `icao24`, `callsign`, `heading`, and `timestamp` are copied when matching aliases are present.
- `altitude_ft` and `speed_ms` may remain in output if present because the implementation copies aliases before deriving canonical meter/knot targets.
- Airline/operator fields are not observed in current implementation.

## False-leaf warnings

- These functions look fixture-testable, but they still depend on shared alias maps and `find_column`.
- Fixture evidence would prove normalization behavior for covered DataFrame shapes only.
- Fixture evidence would not prove parser behavior, provider behavior, renderer behavior, output image parity, metadata behavior, or UI operation behavior.
- Empty-frame schema differs from optional copied columns, for example AIS `name` and aircraft `altitude_ft` / `speed_ms`; tests should pin current behavior rather than infer a broader schema.

## Why fixture-only evidence is enough for this stage

The current stage is preimplementation gate design. The observed code is deterministic DataFrame transformation with no file IO, cache IO, renderer controller use, Qt widget use, VisPy viewer use, or Taichi runtime call inside the normalizer bodies.

Fixture-only evidence is enough to define the next test slice because the immediate question is whether DataFrame input/output behavior can be observed without running display runtime. It is not enough to approve any extraction or movement.

## Next-step branch recommendation

| branch | recommendation | reason |
| --- | --- | --- |
| A:補 normalizer gate 缺口 | not next | This gate now captures the observed AIS and aircraft normalizer matrix. |
| B:新增 normalizer fixture tests | recommended | The code evidence supports import-level DataFrame fixture tests without touching renderer behavior. |
| C:回 parser 區域補更多 edge cases | backlog | Parser fixtures already have first parity and gap-closure coverage; more edge cases can wait unless failures appear. |
| D:停下來回 graph/risk map | not needed now | No renderer/Qt/Taichi/file/cache touch was observed inside the normalizer bodies. |

Recommended next c_3 slice: add focused `normalize_ais_frame` and `normalize_aircraft_frame` fixture tests. The tests should not authorize extraction or helper movement.

## Stop conditions for future tests

Stop if future normalizer tests require source changes, renderer/controller setup, Qt/VisPy/Taichi execution, file/cache writes, runtime artifacts, metadata schema changes, output behavior changes, or wording that implies extraction approval.
