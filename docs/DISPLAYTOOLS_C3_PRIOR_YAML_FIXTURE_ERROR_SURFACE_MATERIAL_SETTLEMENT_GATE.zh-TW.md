# C3 prior YAML fixture error-surface material settlement gate

## Purpose

This docs and test gate settles lab-only YAML fixture error-surface materials into product-repo planning evidence.

It does not create YAML fixtures, does not create the formal dictionary, does not modify schema JSON, and does not modify validator behavior.

## Evidence read

- `L:/RRKAL_lab/external_research/analysis/a1_c3_yaml_fixture_error_message_readability_scout.zh-TW.md`
- `L:/RRKAL_lab/external_research/analysis/c1_c3_reference_envelope_fixture_error_surface_scout.zh-TW.md`
- `L:/RRKAL_lab/external_research/analysis/c2_c3_display_hint_fixture_error_surface_scout.zh-TW.md`
- `L:/RRKAL_lab/external_research/analysis/c4_c3_yaml_fixture_error_card_surface_scout.zh-TW.md`
- `tests/test_displaytools_c3_prior_semantic_dictionary_minimal_yaml_fixture.py`
- `tests/test_displaytools_c3_prior_yaml_fixture_expectation_material_settlement.py`
- `scripts/validate_displaytools_c3_prior_semantic_dictionary.py`
- `docs/DOCS_INDEX.zh-TW.md`

Some lab reports contain mojibake-heavy prose. This gate settles stable labels, error surfaces, diagnostic candidates, and stop-lines only.

## Settlement categories

- `error_message_style_candidate`
- `validator_error_code_candidate`
- `diagnostic_phrase_candidate`
- `fixture_error_surface_candidate`
- `card_edge_error_surface_candidate`
- `reference_only_guard`
- `planning_only_guard`
- `future_validator_rule_candidate`
- `not_yet_allowed`
- `stop_line`

## Error surface coverage

Settled common surfaces:

- `parse_error`
- `schema_error`
- `business_rule_error`
- `missing_fixture_not_applicable`
- `valid_fixture_pass`

Settled c_1 reference envelope surfaces:

- `path_like_asset_id`
- `geometry_bearing_subject_ref`
- `fetchable_source_ref`
- `private_schema_ref`
- `callable_sample_query_ref`
- `raw_spatial_extent`
- `row_level_temporal_extent`
- `fake_or_free_text_evidence_refs`
- `ambiguous_redaction`
- `approval_like_review`

Settled c_2 display hint surfaces:

- `unknown_lod_hint`
- `invalid_bbox`
- `missing_or_unknown_coord_ref`
- `invalid_time_window`
- `credential_bearing_tile_ref`
- `unitless_density_hint`
- `unitless_sample_budget`
- `planning_only_false`

## Conservative future use

Each settled surface is only future planning material:

- `future_fixture_candidate`
- `future_error_code_candidate`
- `future_diagnostic_candidate`
- `future_card_edge_expectation`
- `not_current_validator_change`

## Guards preserved

- c_1 reference-only boundary
- c_2 planning-only and no runtime SLA boundary
- c_4 card-edge only and no parser-validator-renderer boundary
- a_1 readability guidance only and no product integration boundary

## Stop-lines preserved

- No YAML fixture creation.
- No formal dictionary creation.
- No schema JSON modification.
- No validator script modification.
- No runtime behavior.
- No renderer behavior.
- No formula behavior.
- No storage, SQL, crawler, or cross-agent integration behavior.
- No readiness claim.
- No usable dictionary claim.
- No correctness claim.
- No visual parity claim.
- No performance claim.
- No runtime replacement claim.

## Recommended next gate

`c3_prior_yaml_fixture_error_message_planning_gate`

## Boundary statement

Docs/test-only c_3 prior YAML fixture error-surface material settlement gate. This gate classifies lab-only error-surface materials as future fixture, validator, diagnostic, and card-edge planning evidence. It does not create YAML fixtures, does not create the formal dictionary, does not modify schema JSON, does not modify validator scripts, does not add runtime, renderer, formula, SQL, storage, crawler, or cross-agent integration behavior, and does not claim readiness, usability, correctness, visual parity, performance, or runtime replacement.

## Final classification

`c3_prior_yaml_fixture_error_surface_material_settlement_gate_committed_for_o1_review_no_push`
