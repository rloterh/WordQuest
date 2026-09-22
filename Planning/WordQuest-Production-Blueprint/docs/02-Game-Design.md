# Game design bible

## Core interaction: restore meaning

The player receives a short scene, identifies or recalls the precise word, and uses that answer to restore a meaningful object: a testimony, an agreement, an inscription, or a mechanism. A mission has a clear objective and 5–8 compact encounters. The spectacle follows the successful action: ink reconnects a broken sentence, a brass mechanism aligns, a conservatory regains colour.

Core loop: enter mission → inspect evidence → solve a linguistic challenge → see consequence and explanation → earn restoration progress → choose next encounter. Session loop: review due words → continue story → inspect newly strengthened words → choose a next goal. Long loop: complete chapters → restore districts → build a personal lexicon → demonstrate retained skill.

## Four core modes

### Context Detective

Input: a 30–70-word scene with one target sense and four plausible interpretations. The player selects the interpretation and, on later difficulty, highlights the phrase supporting it. Explicit submission prevents accidental taps. Wrong answers receive a specific contrast; hint removes one distraction or highlights a clue. A corrected attempt continues play but is marked assisted for learning evidence.

Win: identify the intended meaning; higher performance requires the evidence phrase. Avoid distractors that are silly, grammatically incompatible, or obviously shorter. Do not rely on world knowledge unrelated to vocabulary.

Example: 'The witness gave an equivocal reply: she neither confirmed the meeting nor denied attending.' Correct interpretation: ambiguous or noncommittal. Distinguish it from 'hostile' and 'detailed'. This example requires editorial review before use.

### Word Forge

Input: a clear meaning or sentence clue plus target tiles. First implementation uses 6–12-letter targets; longer words use two rows or morphology segments. There is no six-letter cap inherited from Text Twist. Repeated letters have separate tile IDs. Tap tiles to place them; tap placed tile to return; keyboard input is supported where available. Shuffle changes presentation only.

Win: reconstruct the intended target or an explicitly reviewed alternate that satisfies both clue and tile rules. Reject a valid unrelated anagram with 'That is a word; the clue asks for…', not a generic error. Show definition and usage after solving. Hints reveal a letter or meaningful segment; they do not cost real money.

Example target: 'laconic', seven letters; clue 'Using very few words.' Other found words are optional decorative discoveries, not curriculum credit. Avoid letter scrambling for learners whose chosen accessibility mode makes it inappropriate; provide equivalent typed recall or context challenge.

### Precision Duel

A dialogue or passage makes register, connotation, or degree decisive. Pick the best word from 3–4 semantically related candidates. Advanced rounds ask the learner to select the reason. The opponent is a friendly character, not an artificial countdown.

Example set: meticulous / pedantic / scrupulous / fastidious. Do not pretend they are interchangeable. A record can be meticulous without a person being pedantic. The passage must make the intended distinction clear enough for independent editors to agree.

### Sentence Rescue

A sentence contains a target-word misuse, wrong collocation, or inappropriate tone. The player chooses the problematic phrase, then repairs it using curated alternatives. Initially use deterministic reconstruction, not unrestricted AI grading. More advanced items require selecting both replacement and rationale.

Example: 'The report exacerbated the uncertainty' describes worsening it; replace with 'alleviated' if context establishes that the report reduced uncertainty. The exact sentence and alternatives must support a unique outcome.

## Capstones

Two per district combine 6–10 encounters across the four modes, with a final interpretation changing the scene. The player may ask for help or retry without losing campaign access. A perfect run earns a cosmetic distinction, not exclusive learning. Narrative consequences are bounded: dialogue and reveal order differ, but no player is permanently trapped by an early vocabulary mistake.

## Difficulty model

Difficulty has separate axes: target familiarity, semantic closeness of distractors, contextual support, recall demand, response length, and number of concepts combined. Change one or two at a time. Do not manufacture difficulty with tiny text, frantic timers, inconsistent touch targets, or rare words chosen only for obscurity.

Mission 1 supports unfamiliar advanced words explicitly. Later missions reduce cues. The scheduler chooses reviewed difficulty bands; it never mutates a production answer key on the fly. Track repeated failure and offer a teaching detour. A recommended initial tuning policy: after two failed submissions on the same item, show a contrasting example and offer retry or guided completion.

## Scoring and rewards

Initial tuneable mission score: 100 points per unaided first-correct encounter; 70 after a non-revealing hint; 40 after revealing help or correction. A second explanatory step adds 20. No negative points. These numbers are balancing proposals, not research findings.

Three mission emblems: completed; completed with mostly unaided answers (initial threshold 80%); completed the optional explanation/transfer challenge. Never label those emblems 'mastery'. Mastery is longitudinal and separate.

Award one fixed restoration token per first mission completion. Every five tokens restores the next chapter landmark; the 60 missions map to 12 landmarks. Retries give practice and modest decorative XP, but cannot farm restoration tokens. Recovery paths ensure guided completion can advance the story. There is no energy, paid failure recovery, or consumable that raises knowledge scores.

Cosmetic collection: 12 landmark restorations, 6 character keepsakes, and a modest set of journal covers. No randomized paid loot. The first paid product is the campaign, not an artificial frustration bypass.

## Daily play

Recommended daily mix: approximately 60% due review, 25% new learning, 15% transfer/challenge, adapted to available content. This is a design starting point, not a scientific optimum. Cap visible review workload at 20 short encounters; offer more by choice. Introduce 3–5 new senses per ordinary session until observations justify adjustment. An advanced diagnostic can skip already-known targets into delayed checks.

Daily discovery is a reviewed rotating item cached ahead of time. Failure to log in does not remove earned progress. Optional weekly goals count practice days, retained words, or missions, with forgiving resumption.

## Anti-repetition design

Every released sense needs multiple contexts and at least one recall task plus one usage/precision task. Mix modes, context, character, and setting while keeping the sense stable. Do not reskin the same sentence six times and call it variety. Do not ask a newly taught word to prove long-term retention seconds later.

## Completion and endgame

The third district resolves the stolen-meaning story. Players can replay capstones, finish remaining curriculum trails, and maintain their lexicon through review. Offline users retain a complete game. A future content season is an addition, not a missing ending.

## Tuning controls

Versioned configuration: new-word quota, review cap, mode distribution, hint cadence, animation duration profile, retry thresholds, reward values, and challenge bands. Difficulty and reward experiments cannot alter definitions or correct answers. Every experiment records cohort and config version; retain a stable control.
