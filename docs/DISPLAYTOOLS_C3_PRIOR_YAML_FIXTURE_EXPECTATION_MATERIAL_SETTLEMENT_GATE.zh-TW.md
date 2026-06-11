# C3 prior YAML fixture expectation material settlement gate

## Purpose

This docs and test settlement gate records the next fixture expansion expectations after the minimal YAML fixture gate.

This gate does not create more YAML fixtures. It only decides which lab materials can guide the next fixture expansion.

## Evidence read

- `tests/test_displaytools_c3_prior_semantic_dictionary_minimal_yaml_fixture.py`
- `tests/test_displaytools_c3_prior_semantic_dictionary_minimal_yaml_fixture_planning.py`
- `L:/RRKAL_lab/external_research/analysis/a1_c3_yaml_fixture_readability_and_fixture_style_audit.zh-TW.md`
- `L:/RRKAL_lab/external_research/analysis/c1_c3_reference_envelope_fixture_validator_expectation_scout.zh-TW.md`
- `L:/RRKAL_lab/external_research/analysis/c2_c3_display_hint_fixture_validator_expectation_scout.zh-TW.md`
- `L:/RRKAL_lab/external_research/analysis/c4_c3_yaml_fixture_validation_card_expectation_scout.zh-TW.md`

Some lab notes contain mojibake-heavy prose. This gate settles stable labels, fixture expectations, and stop-lines only.

## Settlement categories

- `fixture_style_rule`
- `validator_expectation_candidate`
- `schema_pressure_candidate`
- `card_edge_expectation_candidate`
- `reference_only_guard`
- `planning_only_guard`
- `negative_fixture_candidate`
- `stop_line`
- `not_yet_allowed`

## Material decisions

| material | decision | settled use |
| --- | --- | --- |
| `a1_c3_yaml_fixture_readability_and_fixture_style_audit` | accepted | Future fixture style rule. Use stable rules such as fixture naming, valid and invalid filename separation, field order recommendation, single error per negative fixture, and formal dictionary confusion prevention. |
| `c1_c3_reference_envelope_fixture_validator_expectation_scout` | accepted | Future reference-envelope fixture material. It stays reference-only and blocks payload, DB query, raw row, fetchable source, callable sample query, and c_3 consumes c_1 claims. |
| `c2_c3_display_hint_fixture_validator_expectation_scout` | accepted | Future display-hint fixture material. It may guide `lod_hint`, `bbox`, `coord_ref`, `time_window`, `tile_ref`, `density_hint`, `sample_budget`, and `planning_only` expectations while blocking runtime SLA and c_2 algorithm transfer. |
| `c4_c3_yaml_fixture_validation_card_expectation_scout` | accepted | Future card-edge fixture material. It may guide validation result references, dictionary and schema refs, diagnostics refs, failed rule id, error code, status, producer, schema version, evidence refs, and output card refs. |
| `current_minimal_yaml_fixture_gate` | accepted | Current fixture baseline. It proves the first valid and invalid fixtures exist while the formal dictionary remains absent. |

## Next invalid fixture recommendation

Recommended next expansion order:

```text
invalid_legacy_fossil_direct_adoption.yaml
invalid_c4_mediation_bypass.yaml
invalid_readiness_claim.yaml
```

This is an order recommendation only. This gate does not create those fixtures.

## Formal dictionary boundary

The formal dictionary remains unauthorized:

```text
docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml
```

No fixture material in this gate may be read as a dictionary usable claim.

## Stop-lines preserved

- No additional YAML fixture creation.
- No formal dictionary creation.
- No schema JSON modification.
- No validator script modification.
- No runtime behavior.
- No renderer behavior.
- No formula behavior.
- No c_1, c_2, or c_4 real integration.
- No readiness claim.
- No usable claim.
- No correctness claim.
- No visual parity claim.
- No runtime replacement claim.

## Recommended next gate

`c3_prior_semantic_dictionary_yaml_invalid_fixture_expansion_gate`

## Boundary statement

Docs and test only c_3 prior YAML fixture expectation material settlement gate. This gate classifies a_1, c_1, c_2, c_4, and current fixture evidence into fixture style rules, validator expectation candidates, schema pressure candidates, card-edge expectation candidates, guards, stop-lines, and next invalid fixture recommendations. It does not create YAML fixtures, does not create the formal dictionary, does not modify schema JSON, does not modify the validator script, does not implement runtime, prototype, renderer, formula, or real cross-agent integration behavior, and does not claim dictionary usability, readiness, correctness, visual parity, or runtime replacement.

## Final classification

`c3_prior_yaml_fixture_expectation_material_settlement_gate_committed_for_o1_review_no_push`
