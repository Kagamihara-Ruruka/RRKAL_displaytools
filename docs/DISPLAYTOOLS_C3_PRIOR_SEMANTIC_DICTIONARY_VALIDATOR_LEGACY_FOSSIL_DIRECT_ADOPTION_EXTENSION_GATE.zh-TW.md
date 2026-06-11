# C3 prior semantic dictionary validator legacy fossil direct adoption extension gate

## Purpose

This validator, test, and docs gate extends the existing c_3 prior semantic dictionary validator so it rejects direct legacy fossil adoption.

The extension is narrow: every `legacy_fossil_translation` entry must set `direct_adoption_forbidden: true`.

## Coverage labels

- `legacy fossil direct adoption validator rule`
- `direct_adoption_forbidden: false`
- `direct_adoption_forbidden missing`
- `direct_adoption_forbidden: true`
- `no schema JSON modification`
- `no formal dictionary creation`
- `no runtime behavior`

## Validator behavior

The validator now fails when:

- `legacy_fossil_translation[*].direct_adoption_forbidden` is `false`
- `legacy_fossil_translation[*].direct_adoption_forbidden` is missing
- `legacy_fossil_translation[*].direct_adoption_forbidden` is any value other than boolean `true`

The validator still allows entries with `direct_adoption_forbidden: true`, assuming no other rule fails.

## Files intentionally not changed

- `docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml` is not created.
- `docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json` is not modified.
- No remaining invalid product fixture is created in this gate.

## Stop-lines preserved

- No formal dictionary creation.
- No schema JSON modification.
- No product fixture expansion.
- No runtime behavior.
- No prototype behavior.
- No renderer behavior.
- No formula movement.
- No c_1, c_2, or c_4 real integration.
- No readiness claim.
- No usable claim.
- No correctness claim.
- No visual parity claim.
- No runtime replacement claim.

## Boundary statement

Validator, test, and docs only c_3 prior semantic dictionary validator extension gate. This gate only teaches the validator to reject direct legacy fossil adoption. It does not create the formal dictionary, does not create the remaining invalid fixtures, does not modify schema JSON, does not implement runtime, prototype, renderer, formula, or real cross-agent integration behavior, and does not claim readiness, usability, correctness, visual parity, or runtime replacement.

## Final classification

`c3_prior_semantic_dictionary_validator_legacy_fossil_direct_adoption_extension_gate_committed_for_o1_review_no_push`
