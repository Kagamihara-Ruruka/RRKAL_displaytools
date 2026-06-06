# DataFrame Parser Fixture Parity Gate

## TL;DR

This gate covers the DataFrame parsing helpers around `taichi_global_bathymetry.py` lines `1178-1283`.

The target is to prove that this parser zone is fixture-testable and separable at the input/output contract level before any future extraction is discussed. Passing this gate would not authorize helper extraction, renderer movement, visual parity claims, or UI operation claims.

## Scope boundary

In scope:

- `dataframe_from_geojson`
- `dataframe_from_json`
- `dataframe_from_jsonl`
- `dataframe_from_nmea`
- `dataframe_from_text`

Out of scope:

- `read_file_text`: file decoding and gzip handling, not parser contract only.
- `normalize_ais_frame`: downstream AIS schema normalization.
- `normalize_aircraft_frame`: downstream aircraft schema normalization.
- renderer execution, Qt, Taichi, VisPy, overlay composition, alpha/layer ordering, metadata schema, output artifacts.

## Candidate parser symbols

| symbol | anchor | classification | reason |
| --- | --- | --- | --- |
| `dataframe_from_geojson` | `taichi_global_bathymetry.py:1178` | `parser_fixture_candidate` | Converts GeoJSON FeatureCollection-like objects to a DataFrame without file/cache access. |
| `dataframe_from_json` | `taichi_global_bathymetry.py:1191` | `parser_fixture_candidate` | Dispatches JSON object/list shapes into DataFrame output; fixture matrix can cover branches. |
| `dataframe_from_jsonl` | `taichi_global_bathymetry.py:1227` | `parser_fixture_candidate` | Converts non-empty JSONL lines to normalized rows; empty input behavior is explicit. |
| `dataframe_from_nmea` | `taichi_global_bathymetry.py:1236` | `parser_needs_runtime_context` | Optional `pyais` dependency and decoder error handling require environment-aware fixtures. |
| `dataframe_from_text` | `taichi_global_bathymetry.py:1256` | `parser_false_leaf_risk` | It is a dispatch wrapper that may call CSV parsing or NMEA fallback; it should be fixture-gated before extraction. |
| `read_file_text` | `taichi_global_bathymetry.py:1171` | `not_parser_scope` | Reads bytes and handles gzip before parsing; it touches files and should not be bundled into parser fixture parity. |
| `normalize_ais_frame` | `taichi_global_bathymetry.py:1286` | `not_parser_scope` | Normalizes parser output into renderer/provider schema; it is a downstream normalization gate. |
| `normalize_aircraft_frame` | `taichi_global_bathymetry.py:1331` | `not_parser_scope` | Normalizes aircraft schema after parsing; it is not part of the parser input matrix. |

## Fixture matrix

| parser | input shape | expected output shape | nullable / missing-column behavior | dtype assumptions | failure mode | globals/cache/files touched |
| --- | --- | --- | --- | --- | --- | --- |
| `dataframe_from_geojson` | `dict` with `features`, each feature has `properties` and optional Point geometry | DataFrame with properties plus `lon`/`lat` when Point coordinates exist | Missing geometry keeps properties only; missing properties becomes empty dict row | No strict dtype guarantee; pandas infers | Does not catch malformed non-dict feature shapes | No globals, cache, or files observed |
| `dataframe_from_json` | JSON text containing FeatureCollection | Delegates to `dataframe_from_geojson` | Same as GeoJSON branch | Same as GeoJSON branch | `json.loads` raises on invalid JSON | No globals, cache, or files observed |
| `dataframe_from_json` | JSON text containing OpenSky-style `states` list | DataFrame with OpenSky column names sliced to row width | Empty `states` returns DataFrame with full OpenSky columns | No strict dtype guarantee; pandas infers | Ragged rows follow pandas DataFrame behavior | No globals, cache, or files observed |
| `dataframe_from_json` | JSON text containing one list field among `data`, `ships`, `vessels`, `aircraft`, `planes`, `positions`, `rows`, `results` | `pd.json_normalize(value)` | Missing target list falls through to normalize whole object | No strict dtype guarantee | `json.loads` raises on invalid JSON | No globals, cache, or files observed |
| `dataframe_from_json` | JSON list | `pd.json_normalize(obj)` | Empty list returns empty DataFrame | No strict dtype guarantee | `json.loads` raises on invalid JSON | No globals, cache, or files observed |
| `dataframe_from_jsonl` | newline-delimited JSON text | DataFrame normalized from non-empty lines | Empty/blank-only input returns empty DataFrame | No strict dtype guarantee | first invalid non-empty line raises from `json.loads` | No globals, cache, or files observed |
| `dataframe_from_nmea` | AIS/NMEA text lines beginning `!AI` or `$AI` | DataFrame of decoded rows containing `lat` and `lon` | Lines without lat/lon are skipped | Depends on `pyais.decode().asdict()` output | Missing `pyais` returns empty DataFrame; decode errors are skipped | No globals, cache, or files observed |
| `dataframe_from_text` | source suffix `.json` / `.geojson` or JSON-looking text | Delegates to `dataframe_from_json`; fallback continues on parse exception | Parser exceptions are swallowed for JSON branch and may fall through | Branch-dependent | Final CSV failure may fall back to NMEA or re-raise | No globals/cache/files; uses `Path(source_name)` only |
| `dataframe_from_text` | source suffix `.jsonl` / `.ndjson` | Delegates to `dataframe_from_jsonl`; fallback continues on parse exception | Parser exceptions are swallowed for JSONL branch and may fall through | Branch-dependent | Final CSV failure may fall back to NMEA or re-raise | No globals/cache/files; uses `Path(source_name)` only |
| `dataframe_from_text` | NMEA-looking text | Calls `dataframe_from_nmea`, returns only if non-empty | Empty decoded NMEA continues to CSV path | Depends on NMEA decode output | CSV fallback can return a text-shaped DataFrame if pandas accepts it | No globals/cache/files; uses `Path(source_name)` only |
| `dataframe_from_text` | CSV text | `pd.read_csv(io.StringIO(text))` | Missing columns are not validated here | pandas infers dtypes | If CSV parse fails, NMEA fallback may return or original error is raised | No globals/cache/files; uses in-memory text |

## Required fixture groups before future extraction

Minimum focused fixtures:

1. GeoJSON Point feature adds `lon` and `lat`.
2. GeoJSON non-Point feature keeps properties without coordinates.
3. OpenSky `states` list maps to expected column prefix.
4. Known list-key object, such as `{"ships": [...]}`, normalizes nested rows.
5. JSON list normalizes directly.
6. JSONL ignores blank lines and normalizes valid lines.
7. Invalid JSONL raises rather than silently returning partial output.
8. NMEA missing `pyais` path returns empty DataFrame without requiring renderer runtime.
9. `dataframe_from_text` dispatches `.geojson`, `.jsonl`, NMEA-looking text, and CSV text through expected branches.
10. `dataframe_from_text` fallback behavior is explicitly asserted, especially swallowed JSON/JSONL parse failures.

## Risk notes

- `dataframe_from_text` is not a pure parser leaf until fixture evidence proves its branch and fallback behavior.
- `dataframe_from_nmea` depends on optional `pyais`; fixture design should use dependency-aware tests and avoid requiring live decoder availability.
- Parser fixture pass only proves parser input/output behavior for covered samples. It does not prove renderer parity, output image parity, metadata behavior, or UI operation behavior.
- Future extraction must keep parser-only scope separate from file reading, provider normalization, cache governance, and renderer setup.

## Preimplementation gate decision

Current classification: `preimplementation_gate_only`.

Recommended next c_3 action:

- Add focused unit fixtures for the parser symbols listed above.
- Keep tests import-level only.
- Do not instantiate renderer/controller/UI classes.
- Do not execute Taichi initialization.
- Do not write runtime artifacts.

Stop if future tests need renderer setup, Qt, Taichi, cache files, PNG/JSON runtime artifacts, metadata schema changes, or provider normalization changes.
