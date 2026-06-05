# Display ViewCard Consumer Mapping

Date: 2026-06-05
Agent: c_3
Scope: display-consumer mapping only

## TL;DR

c_3 should consume validated ViewCards, not upstream database rows, raw manifests, or raw datasets.

For future Odoriba handoff, displaytools only needs the minimum fields required to choose a canvas, render a layer, show preview state, and attach evidence. The ViewCard contract should stay small, inspectable, and display-oriented.

This is not renderer integration. This is not CanvasStrategy implementation. This does not change metadata schema, output behavior, Qt UI, or renderer hot path.

## Display consumer current-state summary

Current displaytools evidence already separates renderer artifacts from UI readiness:

- `docs/PREVIEW_INTERACTION_READINESS_BOUNDARY.zh-TW.md` distinguishes renderer preview evidence from Qt/UI interactive evidence.
- `docs/QT_PREVIEW_OPERATION_EVIDENCE_GATE.zh-TW.md` defines future evidence needed for UI event-loop and preview operation measurement.
- `docs/RUNTIME_BLEND_SUBPHASE_TIMING_DESIGN.zh-TW.md` keeps runtime_blend timing evidence behind data-ready and parity gates.
- `docs/DEMO_READINESS_BASELINE.zh-TW.md` records renderer preview, repeated quick, warm-frame, and runtime_blend evidence as renderer evidence only.
- `scripts/render_quick_smoke.ps1` verifies renderer output metadata sidecar schema `rrkal_displaytools.renderer_output_metadata.v1`.
- Existing metadata evidence aligns with runtime pressure, LayerRenderState, LOD counters, heavy overlay defer/cache, and render-plan timing summaries.

c_3's downstream role:

- consume view-ready display descriptors.
- choose display/canvas behavior from bounded fields.
- render layers from validated references and style hints.
- report preview/evidence status.
- avoid upstream ownership of discovery, download, import, cache governance, or raw data interpretation.

## Minimal DisplayViewCard fields

DisplayViewCard describes the whole display/canvas request.

| Field | Type | Required | Purpose |
| --- | --- | --- | --- |
| `schema` | string | yes | Example: `rrkal.display_view_card.v1`. |
| `display_id` | string | yes | Stable id for this display request. |
| `title` | string | yes | Human-readable display title. |
| `canvas_kind` | string | yes | Example: `earth_globe`, `map_2d`, `timeline`, `plot`. |
| `projection` | string | conditional | Needed for geo displays; example: `globe`, `equirectangular`. |
| `style_profile` | string | yes | Display-level visual profile such as scientific, nautical, parchment, tactical. |
| `coordinate_reference` | object | conditional | Minimal CRS/projection note; should be normalized before c_3 receives it. |
| `viewport_hint` | object | no | Optional camera/extent/zoom hint. |
| `layer_cards` | array | yes | Ordered LayerViewCard list or references. |
| `preview_card` | object | no | PreviewViewCard for artifact and preview status. |
| `evidence_card` | object | no | EvidenceViewCard for smoke/provenance summary. |
| `source_summary` | object | yes | Human-readable upstream source summary, not raw source payload. |
| `governance_boundary` | object | yes | Explicit owner boundary and what c_3 must not do. |

Minimal DisplayViewCard example:

```json
{
  "schema": "rrkal.display_view_card.v1",
  "display_id": "earth-demo-001",
  "title": "Global bathymetry preview",
  "canvas_kind": "earth_globe",
  "projection": "globe",
  "style_profile": "scientific",
  "layer_cards": [],
  "source_summary": {
    "producer": "Odoriba",
    "validation_state": "validated"
  },
  "governance_boundary": {
    "displaytools_consumes_view_cards": true,
    "displaytools_reads_raw_data": false
  }
}
```

## Minimal LayerViewCard fields

LayerViewCard describes one displayable layer after upstream validation and interpretation.

| Field | Type | Required | Purpose |
| --- | --- | --- | --- |
| `schema` | string | yes | Example: `rrkal.layer_view_card.v1`. |
| `layer_id` | string | yes | Stable layer id for display ordering and state. |
| `label` | string | yes | Human-readable layer name. |
| `layer_kind` | string | yes | Example: `geo_vector`, `geo_raster`, `point_marker`, `annotation`, `image_overlay`. |
| `display_role` | string | yes | Example: `hydrology`, `boundary`, `terrain`, `traffic`, `pin`, `preview`. |
| `renderer_target` | string | yes | Bounded target recognized by c_3 renderer path. |
| `visibility_default` | boolean | yes | Initial visible state. |
| `opacity_default` | number | yes | Initial opacity 0.0 to 1.0. |
| `blend_mode_default` | string | yes | Display blend mode; must be bounded to supported modes. |
| `z_order` | number | yes | Stable order after upstream policy resolution. |
| `asset_ref` | object | yes | Validated display-ready asset reference, not raw data. |
| `geometry_summary` | object | conditional | Required for geo/vector layers. |
| `style_hint` | object | no | Color, line width, fill, icon, or thematic hint. |
| `interaction_hint` | object | no | Pickable/selectable/hoverable flags. |
| `lod_hint` | object | no | Display LOD bucket or simplification hint. |
| `evidence_ref` | object | no | Link to validation/evidence summary. |
| `provenance_summary` | object | yes | Compact source/provenance statement. |

## Minimal LayerViewCard for Geo layer add

Geo layer add is the most important near-term case. c_3 needs enough information to place, style, order, and preview the layer without reading upstream raw data.

Required minimum:

| Field | Type | Purpose |
| --- | --- | --- |
| `layer_id` | string | Stable id for layer stack and runtime state. |
| `label` | string | UI label and evidence report label. |
| `layer_kind` | string | `geo_vector` or `geo_raster`. |
| `display_role` | string | Example: `boundary`, `hydrology`, `terrain`, `mask`, `annotation`. |
| `renderer_target` | string | Renderer-facing target such as `borders`, `lakes`, `rivers`, `territorial_sea`, `eez`, or a bounded extension id. |
| `geometry_type` | string | Example: `point`, `line`, `polygon`, `raster_grid`. |
| `coordinate_reference` | object | CRS/projection summary already normalized by upstream. |
| `bbox` | array | `[min_lon, min_lat, max_lon, max_lat]` when applicable. |
| `asset_ref` | object | Display-ready file/blob/tile reference with local/portable path or id. |
| `style_hint` | object | Minimal color/width/fill/opacity defaults. |
| `visibility_default` | boolean | Initial visibility. |
| `opacity_default` | number | Initial opacity. |
| `z_order` | number | Stable order. |
| `pick_policy` | object | Whether hover/click identity is available. |
| `identity_summary` | object | Feature identity keys available for display, not the full upstream record. |
| `evidence_ref` | object | Validation/evidence packet id or path. |

Geo layer add should not require:

- direct upstream DB access.
- raw manifest parsing.
- discovery/download/import logic.
- unbounded renderer target strings.
- full feature tables in the card.
- unreviewed alpha/blend semantics.

## Minimal PreviewViewCard fields

PreviewViewCard describes preview artifacts and preview evidence boundaries.

| Field | Type | Required | Purpose |
| --- | --- | --- | --- |
| `schema` | string | yes | Example: `rrkal.preview_view_card.v1`. |
| `preview_id` | string | yes | Stable preview id. |
| `preview_mode` | string | yes | Example: `static_artifact`, `file_live_preview`, `qt_state_preview`. |
| `artifact_ref` | object | conditional | Preview PNG/frame reference when available. |
| `metadata_ref` | object | conditional | Renderer metadata sidecar reference when available. |
| `metadata_schema` | string | conditional | Expected `rrkal_displaytools.renderer_output_metadata.v1` for renderer outputs. |
| `generated_artifact_policy` | object | yes | Confirms local artifacts are ignored and not committed. |
| `readiness_boundary` | string | yes | Example: `renderer_preview_artifact_only`. |
| `ui_readiness_claimed` | boolean | yes | Must remain false unless future UI gate proves otherwise. |
| `interactive_fps_claimed` | boolean | yes | Must remain false. |

## Optional EvidenceViewCard fields

EvidenceViewCard should summarize evidence without pulling raw logs into display state.

| Field | Type | Required | Purpose |
| --- | --- | --- | --- |
| `schema` | string | yes | Example: `rrkal.evidence_view_card.v1`. |
| `evidence_id` | string | yes | Stable evidence packet id. |
| `evidence_kind` | string | yes | Example: `quick_smoke`, `repeated_quick`, `warm_frame`, `runtime_blend_timing`, `qt_preview_operation`. |
| `command` | string | no | Review command when relevant. |
| `result` | string | yes | Example: `PASS`, `FAIL`, `not_collected`. |
| `artifact_refs` | array | no | Local ignored artifact refs or portable summary refs. |
| `summary_metrics` | object | no | Render ms, prepare ms, compose ms, or latency metrics. |
| `limitations` | array | yes | What this evidence does not prove. |
| `next_gate` | string | no | Example: `qt_preview_operation_evidence_gate`. |

## Fields c_3 should not receive / should not own

c_3 should not receive or own:

- raw crawler records.
- upstream database rows.
- raw download manifests.
- raw source API payloads.
- credential, token, or private config fields.
- cache governance rules.
- dataset discovery rules.
- import/install registry state.
- compression pipeline internals.
- upstream validation algorithms.
- full feature tables when a bounded display-ready asset reference is enough.
- unbounded style code or executable callbacks.
- authoritative truth claims beyond the provided provenance summary.

c_3 can receive summaries of those concerns only when needed for display evidence, warnings, or provenance.

## Existing evidence fields that can align with ViewCard

| Existing evidence | ViewCard alignment |
| --- | --- |
| `rrkal_displaytools.renderer_output_metadata.v1` | PreviewViewCard `metadata_schema` and EvidenceViewCard metadata refs. |
| runtime pressure snapshot | EvidenceViewCard `summary_metrics` and DisplayViewCard performance note. |
| LayerRenderState packet | LayerViewCard visibility, opacity, blend, dirty flags, renderer target, LOD hint. |
| LOD counter packet | LayerViewCard `lod_hint` and EvidenceViewCard metrics. |
| heavy overlay defer/cache snapshot | LayerViewCard defer/cache hint and EvidenceViewCard limitations. |
| repeated quick smoke summary | PreviewViewCard artifact readiness and EvidenceViewCard `repeated_quick`. |
| warm-frame smoke summary | EvidenceViewCard `warm_frame` metrics. |
| runtime_blend timing review | EvidenceViewCard `runtime_blend_timing` and next gate. |
| Qt preview operation gate draft | Future PreviewViewCard UI-path evidence boundary. |

## Gaps for future Odoriba integration

Future Odoriba handoff should define:

- exact ViewCard schema names and versioning.
- bounded `canvas_kind` vocabulary.
- bounded `layer_kind` and `display_role` vocabulary.
- renderer target alias policy.
- portable `asset_ref` shape.
- normalized coordinate reference summary.
- evidence packet id/path convention.
- feature identity summary shape for geo layers.
- missing/partial data warning shape.
- how ViewCards are validated before c_3 receives them.

Do not solve these gaps inside c_3 by directly reading upstream data. c_3 should only validate that a ViewCard is complete enough for display consumption.

## Final classification

`display_consumer_minimal_viewcard_mapping_complete_docs_only`

Boundary statement: DisplayViewCard / LayerViewCard / PreviewViewCard / EvidenceViewCard minimal mapping only. No renderer integration. No CanvasStrategy implementation. No UI readiness claim.
