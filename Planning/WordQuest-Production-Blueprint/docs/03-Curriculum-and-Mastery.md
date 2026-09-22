# Curriculum, editorial standards, and mastery

## Select advanced usefulness

Score each candidate sense from 0–3 on communicative usefulness, target-audience challenge, context richness, and teachable contrast. Initial selection threshold: at least 9/12, with usefulness at least 2. This is our editorial rubric, not a validated proficiency scale. An editor can admit a literary word with a written reason. Exclude elementary senses, gratuitous jargon, archaic trivia, and words included solely because they are long.

Proposed launch mix across 600 senses: 210 reasoning/academic, 150 professional/precision, 120 character/emotion/social judgment, 90 literary/descriptive, 30 morphology-focused senses. Tags can overlap; primary category counts must sum to 600. All words still need everyday intelligible explanations.

Illustrative candidates: equivocal, cogent, perfunctory, intransigent, assiduous, circumspect, ostensibly, incongruous, parsimonious, pragmatic, tenacious, scrupulous, ambivalent, nuanced, exacerbate, mitigate, substantiate, corroborate, refute, obviate, propensity, reticence, prescience, ephemeral, ubiquitous, esoteric, ineffable, trenchant, laconic, magnanimous. These are candidate targets, not a vetted launch corpus.

## Model meanings, not spelling alone

Each stable sense ID has lemma, part of speech, definition, register, pronunciation reference, at least two collocations, three original examples, a non-example with explanation, relevant word family, confusable senses, editorial provenance, and license status. Polysemous words receive separate sense IDs. Inflections point to the intended lemma/sense with an explicit accepted-answer rule.

Reviewers must verify definitions, examples, distractors, pronunciations, and word-family claims. Do not infer etymology from a plausible-looking prefix. Record a reputable reference and the rights to any copied material. Prefer original teaching explanations reviewed against references; dictionary access does not automatically permit redistribution of its content or audio.

## Six learning encounters per released sense

Minimum inventory per sense: two context items in genuinely different situations, one meaning-to-word recall item, one precision/contrast item, one usage/repair item, and one delayed-transfer item reserved from initial teaching. That produces a minimum of 3,600 reviewed items for 600 senses. Some items refer to multiple senses, but count coverage per sense transparently; do not double-count an untested sense.

Thirty prototype senses require at least 180 reviewed items; 120 slice senses require at least 720. Production may draft in batches, but every released record passes human review. Draft examples in this package do not satisfy those quotas.

## Learning evidence

Track recognition, free/cued recall, spelling where relevant, contextual precision, and usage separately. Every attempt records mode, item, content version, skill, response result, hint level, attempt number, and elapsed time. Elapsed time describes fluency; it should not automatically penalize slow readers or accessibility users.

Player-facing stages:

| Stage | Proposed evidence rule |
|---|---|
| Encountered | Teaching exposure recorded |
| Recognized | Correct recognition on two distinct items, at least one unaided |
| Recalled | Unaided recall on two distinct items, including a later session |
| Applied | Correct use/precision on two contexts, at least one held-out context |
| Retained | Successful unaided recall and contextual check after at least 7 days, on different days |

These are honest labels for measured performance, not a guarantee of permanent memory. Preserve strengths after a lapse; show 'ready for review' instead of humiliating demotion. The underlying scheduler can lower confidence without deleting earned campaign rewards.

## Scheduler baseline

Use a deterministic, testable scheduling interface and an initial simple interval policy. It is not branded as a scientifically calibrated memory model. Start an unfamiliar sense with teaching then same-session retrieval; successful unaided retrieval schedules checks at approximately 1, 3, 7, 14, and 30 days. Later spacing increases after consistent success; failure returns the relevant skill to a shorter interval. Tune from observed retention and load.

Store intervals per sense/skill, last successful attempt, due timestamp, scheduler version, lapse count, and assistance history. Correctness after a revealing hint is assisted; it cannot promote an unaided stage. Recognition cannot substitute for recall. Repeating an identical item within minutes cannot establish retention.

Queue construction: due skills first, capped to a manageable workload; then weak skills; then new senses within daily quota; finally optional transfer. Prevent repeated near-identical items in a session. Clock anomalies: use server time when connected, record device offset and monotonic elapsed time for local sessions, and never award repeated daily rewards from clock changes. Offline attempts remain useful, but suspicious timing cannot certify delayed retention until reconciled.

Future algorithm replacement needs an ADR, data migration, deterministic replay comparison, and learning evaluation. Keep curriculum rules separate from scheduling math.

## Editorial workflow

Candidate → drafted → schema-valid → linguist-reviewed → independent ambiguity check → audio checked → playtest → approved → published. At least one qualified human editor reviews every production item. A second reader checks high-confusion items and all capstones. AI can perform consistency sweeps but cannot serve as the sole independent authority.

Review checklist: target sense correct; examples natural; exactly one intended answer or explicit accepted alternatives; distractors plausible; no answer leakage; register accurate; no unnecessary cultural knowledge; no unsafe stereotypes; readable length; pronunciation rights recorded; item difficulty sensible. Track editor identity/date, revision, source notes, and status.

## Placement and personalization

Offer a short optional diagnostic of 12–20 items drawn from reviewed bands. Explain that it estimates a starting point, not an official vocabulary size or exam score. Use it to reduce unnecessary teaching and tune hints. Users choose professional, academic, expressive, or balanced emphasis. Preserve variety across skill types; do not create a narrow bubble of only comfortable words.

## Measure real improvement

Reserve unfamiliar contexts and alternate forms for evaluation. Conduct baseline, immediate, and delayed checks, including a 7-day follow-up and a longer follow-up when feasible. Report sample, attrition, and uncertainty. Compare a game experience with a content/time-matched plain practice condition where possible. Do not claim clinical or exam-score benefits from uncontrolled anecdotes.

Learning research supports retrieval and spacing generally; our exact stage thresholds, intervals, and game loop remain product hypotheses. See [retrieval practice](https://www.retrievalpractice.org/why-it-works) and [spacing guidance](https://www.retrievalpractice.org/spacing). Those sources do not validate this particular game.
