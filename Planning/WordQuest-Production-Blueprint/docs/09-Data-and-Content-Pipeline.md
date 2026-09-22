# Data contracts and content production

## Core records

| Record | Required fields |
|---|---|
| Sense | id, lemma, part_of_speech, definition, register, pronunciation refs, examples, collocations, confusables, category, difficulty band, provenance, status, revision |
| Challenge | id, sense_ids, mode, skill, prompt, options/tiles/segments, answer rule, rationale, hint steps, difficulty, transfer flag, reviewer, status, revision |
| Mission | id, chapter, prerequisites, narrative refs, encounter slots, reward grant, restoration target, revision |
| Attempt | id, device/profile, session, challenge/version, sense/skill, outcome, assistance, timestamps, scheduler version |
| SkillState | sense/skill, evidence references, stage, interval, due time, lapse count, algorithm version |
| Entitlement | subject, product, platform, transaction reference, state, version, verified_at |
| Asset | id, source/export paths, rights, import recipe, budgets, review status |

Use opaque stable IDs such as `sense.equivocal.adj.ambiguous.v1`. Human-facing spelling may change without changing identity when correcting a typo; substantive meaning changes need explicit migration. IDs are never derived only from array positions.

## Schema rules

UTF-8; normalized strings; explicit locale; nonempty definitions; unique IDs; valid references; enumerated modes/skills/statuses; bounded text lengths; structured answer keys; revision and provenance. Draft records can omit final audio or reviewer identity, but the release validator rejects missing required release fields. Validation mode is explicit: draft vs release.

Keep accepted alternatives separate from distractors. For Forge, tile counts must exactly permit each claimed solution under the mode's rules, including repeated letters. Normalize whitespace and case where appropriate; do not erase meaning-bearing punctuation indiscriminately. For multiword expressions, explicitly define spacing/hyphen behavior.

## Minimum challenge representation

Options have stable IDs, text and rationale; answer keys refer to IDs. Shuffling options cannot change correctness. Sentence Rescue uses a specified span and accepted replacement IDs; typed variants require a reviewed normalization table. Context items cannot contain their own answer inadvertently. Word-count, duplicate and obvious leakage checks help but do not replace editorial review.

`examples/` contains three draft sense records and representative challenges, plus a structural JSON schema. They illustrate the contract. The complete release schema and cross-record validator are produced in P03. They are not a production seed corpus.

## Authoring workflow

1. Curriculum lead selects a batch of 20–30 senses with coverage targets.
2. AI drafts original definitions, contexts, distractors, hints and metadata using approved source notes.
3. Automated validator checks structure, references, tile math, duplicates, coverage and lengths.
4. Human editor reviews naturalness, meaning, nuance and rights; ambiguous items go back to draft.
5. Independent reader resolves high-risk distinctions and capstones.
6. Audio is produced/licensed and matched to the intended sense/region; pronunciation QA follows.
7. Playtest checks difficulty and clarity with target learners.
8. Publisher builds a signed versioned bundle and a content changelog.
9. Staging client verifies and previews every released item.
10. Content owner marks the batch releasable; deployment uses staged rollout and rollback.

## Editorial dashboard requirements

Batch view with status counts; sense editor; item preview at phone size; option shuffle preview; audio playback; review comments; history diff; rights fields; duplicate warnings; coverage heatmap; blocklist/withdrawal; validation report; export manifest. Begin with local files and a simple review UI if sufficient. A large CMS is not a prerequisite for the prototype, but a sustainable review/publish workflow is required before producing 3,600 items.

## Release validation failures

Block on duplicate IDs, dangling sense references, invalid tile counts, no correct option, multiple correct options unless explicitly allowed, missing rationale, unreviewed status, missing rights evidence, missing required audio, unreachable mission, prerequisite cycle, unsupported schema version, hash mismatch, or target-sense coverage below the promised release count.

Warn for long text, repeated phrases, weak distractor similarity, category imbalance, unusually high hint rate or a large content-size increase. Warnings require disposition, not blind suppression.

## Quality monitoring

Track per-item wrong-answer distribution, hint usage, report rate, abandonment and unusually fast correct answers. Interpret difficulty with learner level and prior exposure. A high error rate may indicate a flawed question rather than a difficult word. Quarantine confirmed flawed items, patch them, and preserve prior fair progress. Do not automatically change correct answers based on a popularity vote.

## Asset and content rights

A source URL is not a license. Record whether text is original, quoted with permission, licensed, or public-domain with verified basis. Track attribution obligations for fonts, music, effects, images, voice and dictionary audio. Production checklists must use current applicable terms; this plan is not a legal clearance opinion.
