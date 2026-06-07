# Layer Render Plan Cache Diagnostics Fixture Parity Gate

## TL;DR

This gate pins current pure dict/list/scalar behavior for render-plan cache diagnostics helpers before any future movement.

This slice is test/docs-only. It does not move helpers, change metadata sidecar writing, execute artifact writers, run renderer code, or change output behavior.

## Candidate discovery result

| Candidate | Current owner | Classification | Fixture gate status | Boundary |
| --- | --- | --- | --- | --- |
| `build_layer_render_plan_cache_key` | `render_core.layer_render_plan_cache_diagnostics`; re-exported by `render_core.render_plan` | pure dict/scalar helper | covered by fixture tests | Builds deterministic JSON cache key only. |
| `build_layer_render_plan_cache_invalidation_reasons` | `render_core.layer_render_plan_cache_diagnostics`; re-exported by `render_core.render_plan` | pure list helper | covered by fixture tests | Reads runtime snapshot dict only. |
| `build_layer_render_plan_cache_invalidation_scope` | `render_core.layer_render_plan_cache_diagnostics`; re-exported by `render_core.render_plan` | pure list-of-dict helper | covered by fixture tests | Reads dirty flags and batch target dicts only. |
| `build_layer_render_plan_metadata_summary` | `render_core.layer_render_plan_cache_diagnostics`; re-exported by `render_core.render_plan` | pure summary packet helper with metadata-sidecar proximity | covered by fixture tests | Summary only; does not write sidecar files. |
| `build_compiled_layer_render_plan_packet` | `render_core.render_plan` | broad packet builder | excluded | Too close to full compiled plan contract for this fixture gate. |
| `build_reused_compiled_layer_render_plan_packet` | `render_core.render_plan` | broad packet builder | excluded | Mutates copied plan packet and aggregates multiple contracts. |

## Fixture matrix

| Branch | Evidence pinned |
| --- | --- |
| Cache key deterministic ordering | Same logical inputs with reordered dictionaries produce the same JSON key. |
| Cache key payload shape | Exact payload key set, visible-layer ordering, sorted boundary layer ids, and visible-layer opacity/blend filtering are asserted. |
| Missing runtime snapshot fields | Missing `visible_layers` and related maps produce empty lists/maps while preserving current `None` composition id behavior. |
| Dirty invalidation reasons | Dirty flags are emitted before previous-plan/cache-key state reasons. |
| Previous plan missing | Non-dict cached plan adds `no_previous_compiled_plan`. |
| Cache key mismatch | Existing cached plan with different previous key adds `cache_key_changed`. |
| Cache key match | Clean matching cache emits `cache_key_match`. |
| Invalidation scope ordering | Batch scopes are emitted before global scopes, then plan scope. |
| Reuse scope | Clean cache match emits the reuse scope packet. |
| Metadata summary unavailable | Empty plan returns current unavailable schema/status/default values and exact key set. |
| Metadata summary populated | Count coercion, status fields, slowest phase, and slow-frame fields are pinned. |
| Deterministic repeat call | Repeated metadata summary calls return identical packets. |

## Cache diagnostics coverage assessment

The fixture gate covers current pure helper output shape and ordering for cache key, invalidation reason, invalidation scope, and metadata summary packets.

It does not cover:

- metadata sidecar writer execution
- artifact writer execution
- renderer/controller cache lifecycle behavior
- output image behavior
- runtime merge behavior
- visual comparison

## False-leaf warnings

- `build_layer_render_plan_metadata_summary` is pure today, but it is close to metadata sidecar content. Any future movement must preserve schema/source fields and must not add writer behavior.
- `build_compiled_layer_render_plan_packet` and reused packet builders aggregate multiple contracts. They are not part of this fixture gate.
- Cache key behavior depends on JSON serialization and current list ordering. Future movement must preserve exact current ordering before changing any behavior.
- Dirty flag ordering follows dictionary insertion order. Fixture tests pin representative ordering but do not approve broader cache policy changes.

## Future movement requirements

Before any future helper movement:

1. `tests.test_layer_render_plan_cache_diagnostics` must pass before and after.
2. Any new helper must remain pure dict/list/scalar logic.
3. The helper must not import renderer, controller, Qt, VisPy, Taichi, metadata writer, artifact writer, parser, provider, or ndarray/pixel code.
4. Metadata schema and output behavior must remain unchanged.
5. Runtime merge must remain disabled unless separately authorized.

## Import-boundary checker

`scripts/validate_layer_render_plan_cache_diagnostics_import_boundary.py` defines the future movement import boundary for `render_core/layer_render_plan_cache_diagnostics.py`.

The checker treats a missing candidate as not applicable and passing. It allows `cache` in helper and field names, but bans provider/source/download/cache lifecycle module imports.

## Boundary statement

Test/docs-only cache diagnostics fixture gate. No helper extraction, no metadata sidecar writer change, no artifact writer execution, no controller instantiation, no renderer/Qt/VisPy/Taichi runtime execution, no output schema change, no runtime merge enablement, and no pixel-equivalence/performance/readiness claim.
