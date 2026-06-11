# C3 Prior Dictionary International Law Registry Gate

## 目的

本 gate 是 future new c_3 semantic dictionary 的 external authority-source registry。它先列出可作為國際法的外部標準、成熟工具模型、RRKAL native governance 與 legacy fossil evidence，讓下一階段規劃 YAML prior dictionary 時不會用 RRKAL 自己亂定的詞直接覆蓋圖形學、GIS、UIUX 與 runtime budget 的成熟語言。

本 gate 不建立 YAML dictionary、不建立 prior card schema、不建立 helper、不建立 prototype，也不執行 renderer 或 runtime。

## Evidence read

- `docs/DISPLAYTOOLS_DYNAMIC_POINT_ANDESITE_REGISTRY_MILESTONE_SETTLEMENT_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_andesite_registry_milestone_settlement.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_MASK_OCCLUSION_LEGACY_ANATOMY_CLASSIFICATION_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_mask_occlusion_legacy_anatomy_classification.py`
- Extracted boundary helper tests for sampling visibility, presentation count, computed-but-hidden, source-lineage guard, and presentation reduction.
- Post source-lineage and presentation-reduction planning context.
- Static scan terms: `mask`, `occlusion`, `projection`, `LOD`, `bake`, `layer`, `frame`, `alpha`, `tile`, `grid`, `trajectory`, `time`, `schema`, `source_lineage`.

## Authority kind taxonomy

- `external_standard`
- `external_reference_implementation`
- `external_mature_tool_model`
- `rrkal_native_governance`
- `legacy_fossil_evidence`
- `candidate_pending_review`

## Registry matrix

| source_id | prior_layer | authority_kind | source_name | source_url_or_local_ref | why_relevant_to_c3 | terms_expected_to_govern | adoption_status | rrkal_translation_needed | forbidden_overread | future_dictionary_candidate | stop_condition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `stac_spec_candidate` | `data_spacetime_prior` | `external_mature_tool_model` | SpatioTemporal Asset Catalog specification | `https://stacspec.org/` | Spatial and temporal asset metadata model. | time slice, event, trajectory, raster, vector, geometry | `candidate_pending_review` | true | Not already adopted as RRKAL asset schema. | true | Stop if source metadata is treated as c_1 implementation. |
| `cf_conventions_candidate` | `data_spacetime_prior` | `candidate_pending_review` | CF Metadata Conventions | `https://cfconventions.org/` | Candidate vocabulary for gridded raster and time-indexed scientific data. | grid, raster, time, feature, point cloud | `candidate_pending_review` | true | Not a renderer or UI schema. | true | Keep pending if c_3 data terms cannot be mapped cleanly. |
| `khronos_rendering_pipeline` | `graphics_prior` | `external_reference_implementation` | Khronos OpenGL rendering pipeline overview | `https://wikis.khronos.org/opengl/Rendering_Pipeline_Overview` | Reference vocabulary for graphics pipeline and framebuffer-adjacent concepts. | camera, view frame, projection, depth, occlusion, clipping, framebuffer | `candidate_pending_review` | true | Does not authorize renderer execution or formula movement. | true | Stop if graphics terms become runtime behavior changes. |
| `khronos_gltf_candidate` | `graphics_prior` | `external_standard` | Khronos glTF specification | `https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html` | Candidate vocabulary for mesh, texture, material and scene graph terms. | texture, mesh, LOD, alpha, compositing | `candidate_pending_review` | true | Not a claim that c_3 outputs glTF. | true | Stop if asset format adoption is implied. |
| `epsg_registry` | `geospatial_prior` | `external_standard` | EPSG Geodetic Parameter Dataset | `https://epsg.org/home.html` | Authority source for CRS identifiers and coordinate reference vocabulary. | CRS, EPSG, WGS84, projection | `candidate_pending_review` | true | Not coordinate correctness proof. | true | Stop if CRS label becomes projection formula movement. |
| `rfc7946_geojson` | `geospatial_prior` | `external_standard` | RFC 7946 GeoJSON | `https://www.rfc-editor.org/rfc/rfc7946` | Standardized feature and geometry vocabulary for geospatial JSON-like terms. | GeoJSON-like feature, geometry, bbox, vector | `candidate_pending_review` | true | Not metadata schema adoption claim. | true | Stop if JSON shape becomes product schema. |
| `ogc_tiles_candidate` | `geospatial_prior` | `external_standard` | OGC tiles and geospatial standards family | `https://www.ogc.org/standards/` | Standards family for tile, bbox, geometry and geospatial interoperability terms. | tile, bbox, geometry, projection | `candidate_pending_review` | true | Not tile runtime implementation authorization. | true | Stop if tile vocabulary implies cache or renderer behavior. |
| `w3c_wai_aria` | `uiux_prior` | `external_standard` | W3C WAI-ARIA | `https://www.w3.org/TR/wai-aria-1.2/` | Reference vocabulary for UI state and interaction roles. | inspector, selection, visibility toggle, tool mode | `candidate_pending_review` | true | Not UI implementation authorization. | true | Stop if semantic labels become UI widgets. |
| `material_design_layering_candidate` | `uiux_prior` | `external_mature_tool_model` | Material Design interaction and layout vocabulary | `https://m3.material.io/` | Mature UI vocabulary for panels, layers, navigation and interaction states. | layer stack, viewport, timeline, style panel | `candidate_pending_review` | true | Not visual design system adoption claim. | true | Keep pending if terms collide with RRKAL renderer layers. |
| `web_performance_budget_candidate` | `runtime_budget_prior` | `external_mature_tool_model` | Web performance budget model | `https://web.dev/articles/performance-budgets-101` | Mature model for bounded frontend render and resource budget vocabulary. | bounded query, streaming, batching, cache, tile, bake, memory budget, frontend render budget | `candidate_pending_review` | true | Not performance readiness or benchmark claim. | true | Stop if budget label becomes performance claim. |
| `rrkal_asset_card_governance` | `rrkal_governance_prior` | `rrkal_native_governance` | RRKAL c_1 asset card governance | `local_ref: APIkeys_collection governance and RRKAL_displaytools docs index` | Separates c_3 display semantics from mature c_1 asset ownership. | c_1 asset card, interface sovereignty, temporary backdoor | `local_governance_reference_only` | false | No direct c_3-to-c_1 maturity claim. | true | Stop if c_3 directly integrates c_1 without c_4 mediation. |
| `rrkal_c4_render_consumption_card` | `rrkal_governance_prior` | `rrkal_native_governance` | RRKAL c_4 render-consumption and Odoriba mediation governance | `local_ref: c_4/Odoriba governance docs and current c_3 source-lineage gates` | Requires cross-organ language mediation before mature integration claims. | c_4 render-consumption card, source lineage, no direct c_3-to-c_1 maturity claim | `local_governance_reference_only` | false | No c_4/Odoriba implementation in this gate. | true | Stop if Odoriba mediation is bypassed. |
| `legacy_mask_fossil_registry` | `legacy_fossil_translation` | `legacy_fossil_evidence` | 21k mask and occlusion legacy anatomy classification | `local_ref: docs/DISPLAYTOOLS_DYNAMIC_POINT_MASK_OCCLUSION_LEGACY_ANATOMY_CLASSIFICATION_GATE.zh-TW.md` | Preserves fossil evidence while blocking direct legacy adoption. | mask, transparent-globe leak, render_if_needed, occlusion | `legacy_evidence_only` | true | Legacy fossil is not ideal form or final interface. | true | Stop if legacy mask becomes prototype API. |
| `extracted_andesite_boundaries` | `legacy_fossil_translation` | `rrkal_native_governance` | Extracted c_3 dynamic point semantic boundaries | `local_ref: render_core dynamic_point boundary helpers` | Local cooled semantics for computed-hidden, presentation reduction and source-lineage guard. | computed-but-hidden, presentation reduction, source-lineage guard | `local_semantic_evidence_not_final_api` | true | Not readiness or prototype final API. | true | Stop if extracted helpers are treated as final prototype API. |

## Prior layer coverage

- `data_spacetime_prior`: grid, raster, vector, feature, geometry, time slice, trajectory, event, point cloud.
- `graphics_prior`: camera, view frame, projection, depth, occlusion, clipping, alpha, compositing, LOD, texture, mesh, framebuffer.
- `geospatial_prior`: CRS, WGS84, EPSG, bbox, GeoJSON-like feature, tile, projection, geometry.
- `uiux_prior`: layer stack, viewport, inspector, timeline, style panel, visibility toggle, selection, tool mode.
- `runtime_budget_prior`: bounded query, streaming, batching, cache, tile, bake, memory budget, frontend render budget.
- `rrkal_governance_prior`: c_1 asset card, c_4 render-consumption card, source lineage, interface sovereignty, temporary backdoor, no direct c_3-to-c_1 maturity claim.
- `legacy_fossil_translation`: 21k `mask`, transparent-globe leak, `render_if_needed`, computed-but-hidden, presentation reduction, source-lineage guard.

## Decision output

```text
international_law_registry_gate_passed = true
external_authority_registry_created = true
yaml_dictionary_authorized = false
prior_card_schema_authorized = false
prototype_authorized = false
runtime_execution_authorized = false
legacy_fossil_direct_adoption_authorized = false
rrkal_native_terms_separated_from_external_authority = true
```

## Recommended next gate

```text
c3_prior_semantic_dictionary_yaml_skeleton_planning_gate
```

## Boundary statement

Docs/test-only external authority-source registry gate for the future new c_3 semantic dictionary. This gate identifies the international law sources that future c_3 YAML prior dictionaries may reference. It does not create the dictionary, does not create prior cards, does not implement prototype/runtime/rendering behavior, does not adopt legacy 21k terms directly, does not claim readiness, and does not push.

## Final classification

```text
c3_prior_dictionary_international_law_registry_gate_committed_for_o1_review_no_push
```
