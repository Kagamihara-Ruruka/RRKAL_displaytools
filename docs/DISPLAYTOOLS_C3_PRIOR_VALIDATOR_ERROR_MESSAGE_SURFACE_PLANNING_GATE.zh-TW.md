# C3 prior validator error message surface planning gate

## Purpose

This docs and test planning gate defines future validator error-message surfaces.

It plans error code families, diagnostic wording style, fixture filename alignment, and PASS/FAIL/not-applicable wording. It does not modify the validator script.

## Evidence read

- `tests/test_displaytools_c3_prior_yaml_fixture_error_surface_material_settlement.py`
- `docs/DISPLAYTOOLS_C3_PRIOR_YAML_FIXTURE_ERROR_SURFACE_MATERIAL_SETTLEMENT_GATE.zh-TW.md`
- `tests/test_displaytools_c3_prior_semantic_dictionary_minimal_yaml_fixture.py`
- `scripts/validate_displaytools_c3_prior_semantic_dictionary.py`
- `L:/RRKAL_lab/external_research/analysis/a1_c3_yaml_fixture_error_message_readability_scout.zh-TW.md`
- `L:/RRKAL_lab/external_research/analysis/c1_c3_reference_envelope_fixture_error_surface_scout.zh-TW.md`
- `L:/RRKAL_lab/external_research/analysis/c2_c3_display_hint_fixture_error_surface_scout.zh-TW.md`
- `L:/RRKAL_lab/external_research/analysis/c4_c3_yaml_fixture_error_card_surface_scout.zh-TW.md`

Some lab reports contain mojibake-heavy prose. This planning gate uses stable labels and code tokens only.

## Planned error code families

- `parse_error`
- `schema_error`
- `business_rule_error`
- `reference_envelope_error`
- `display_hint_error`

Planned examples:

- `yaml_syntax_error`
- `missing_required_section`
- `bare_high_risk_term_id`
- `legacy_fossil_direct_adoption`
- `c4_mediation_bypassed`
- `asset_id_pathlike_rejected`
- `source_ref_fetchable_rejected`
- `sample_query_ref_callable_rejected`
- `display_hint_bbox_invalid_geometry`
- `display_hint_planning_only_false`

## Planned diagnostic wording style

Planned stderr shape:

```text
[ERROR] <error_code>: File "<file_path>", at <position> | <reason>
```

Planned JSON-like surface for future work:

- `error_code`
- `file_path`
- `position`
- `reason`
- `severity`
- `boundary`

Style rules:

- Error codes use `snake_case`.
- Stderr should be one line.
- Do not dump full YAML.
- Do not echo raw payloads.
- PASS wording stays neutral: `Validation passed successfully.`
- Missing dictionary wording stays neutral: `not_applicable_dictionary_missing`
- PASS and not-applicable wording must not imply readiness or usability.

## Planned fixture filename alignment

- `invalid_missing_required_section.yaml` maps to `missing_required_section`
- `invalid_bare_high_risk_term_id.yaml` maps to `bare_high_risk_term_id`
- `invalid_forbidden_runtime_field.yaml` maps to `forbidden_field_detected`
- `invalid_legacy_fossil_direct_adoption.yaml` maps to `legacy_fossil_direct_adoption`
- `invalid_c4_mediation_bypass.yaml` maps to `c4_mediation_bypassed`
- `invalid_readiness_claim.yaml` maps to `readiness_claim_rejected`

## Unknown stop-lines

- `structured_json_error_output` remains future work because the current validator emits stdout and stderr text only.
- `display_hint_warning_vs_fail_runtime_policy` remains future work because display-hint warning policy must not imply runtime SLA.

## Stop-lines preserved

- No validator script modification.
- No schema JSON modification.
- No YAML fixture creation.
- No formal dictionary creation.
- No runtime behavior.
- No renderer behavior.
- No formula behavior.
- No SQL, storage, crawler, or cross-agent integration behavior.
- No readiness claim.
- No usable dictionary claim.
- No correctness claim.
- No visual parity claim.
- No performance claim.
- No runtime replacement claim.

## Recommended next gate

`c3_prior_validator_error_message_surface_contract_gate`

## Boundary statement

Docs/test-only c_3 prior validator error message surface planning gate. No validator script modification, no schema JSON modification, no YAML fixture creation, no formal dictionary creation, no runtime behavior, no integration, no readiness claim, and no push.

## Final classification

`c3_prior_validator_error_message_surface_planning_gate_committed_for_o1_review_no_push`
