# WordQuest — Complete Production Blueprint

Prepared for Robert Loterh · 20 September 2026

A self-contained edition of the complete planning package. The companion ZIP preserves individual documents and prompts for focused use in a coding workspace. No game implementation or release validation is claimed.

## Contents
- [README.md](#file-readme-md)
- [docs/00-Executive-Direction.md](#file-docs-00-executive-direction-md)
- [docs/01-Product-Requirements.md](#file-docs-01-product-requirements-md)
- [docs/02-Game-Design.md](#file-docs-02-game-design-md)
- [docs/03-Curriculum-and-Mastery.md](#file-docs-03-curriculum-and-mastery-md)
- [docs/04-Narrative-and-Level-Design.md](#file-docs-04-narrative-and-level-design-md)
- [docs/05-UX-and-Accessibility.md](#file-docs-05-ux-and-accessibility-md)
- [docs/06-Art-Motion-and-Sound.md](#file-docs-06-art-motion-and-sound-md)
- [docs/07-Engine-and-Tools.md](#file-docs-07-engine-and-tools-md)
- [docs/08-Technical-Architecture.md](#file-docs-08-technical-architecture-md)
- [docs/09-Data-and-Content-Pipeline.md](#file-docs-09-data-and-content-pipeline-md)
- [docs/10-AI-Production-Workflow.md](#file-docs-10-ai-production-workflow-md)
- [docs/11-QA-Performance-and-Research.md](#file-docs-11-qa-performance-and-research-md)
- [docs/12-Production-Roadmap.md](#file-docs-12-production-roadmap-md)
- [docs/13-Business-and-LiveOps.md](#file-docs-13-business-and-liveops-md)
- [docs/14-Release-and-Operations.md](#file-docs-14-release-and-operations-md)
- [docs/15-Decisions-and-Risks.md](#file-docs-15-decisions-and-risks-md)
- [docs/16-Source-Register.md](#file-docs-16-source-register-md)
- [docs/17-Requirements-Traceability.md](#file-docs-17-requirements-traceability-md)
- [docs/18-First-Ten-Working-Days.md](#file-docs-18-first-ten-working-days-md)
- [prompts/00-Execution-Index.md](#file-prompts-00-execution-index-md)
- [prompts/Creative-Asset-Prompts.md](#file-prompts-creative-asset-prompts-md)
- [prompts/P00-Environment-and-Evidence.md](#file-prompts-p00-environment-and-evidence-md)
- [prompts/P01-Mobile-Feasibility.md](#file-prompts-p01-mobile-feasibility-md)
- [prompts/P02-Project-Foundation.md](#file-prompts-p02-project-foundation-md)
- [prompts/P03-Content-Schemas-and-Validation.md](#file-prompts-p03-content-schemas-and-validation-md)
- [prompts/P04-Core-Challenge-Modes.md](#file-prompts-p04-core-challenge-modes-md)
- [prompts/P05-Learning-and-Durable-Saves.md](#file-prompts-p05-learning-and-durable-saves-md)
- [prompts/P06-UX-and-Design-System.md](#file-prompts-p06-ux-and-design-system-md)
- [prompts/P07-Hero-Art-and-Motion-Pipeline.md](#file-prompts-p07-hero-art-and-motion-pipeline-md)
- [prompts/P08-Narrative-and-Slice-Campaign.md](#file-prompts-p08-narrative-and-slice-campaign-md)
- [prompts/P09-Accessibility-and-Device-Polish.md](#file-prompts-p09-accessibility-and-device-polish-md)
- [prompts/P10-Slice-Research-and-Go-No-Go.md](#file-prompts-p10-slice-research-and-go-no-go-md)
- [prompts/P11-Backend-and-Cloud-Sync.md](#file-prompts-p11-backend-and-cloud-sync-md)
- [prompts/P12-Purchases-and-Entitlements.md](#file-prompts-p12-purchases-and-entitlements-md)
- [prompts/P13-Editorial-Publishing-Toolchain.md](#file-prompts-p13-editorial-publishing-toolchain-md)
- [prompts/P14-Analytics-and-Operational-Controls.md](#file-prompts-p14-analytics-and-operational-controls-md)
- [prompts/P15-Full-Campaign-and-Content-Production.md](#file-prompts-p15-full-campaign-and-content-production-md)
- [prompts/P16-Optional-AI-Lab.md](#file-prompts-p16-optional-ai-lab-md)
- [prompts/P17-Beta-Qualification.md](#file-prompts-p17-beta-qualification-md)
- [prompts/P18-Store-and-Policy-Preparation.md](#file-prompts-p18-store-and-policy-preparation-md)
- [prompts/P19-Release-Rehearsal.md](#file-prompts-p19-release-rehearsal-md)
- [prompts/P20-Independent-Release-Review.md](#file-prompts-p20-independent-release-review-md)
- [prompts/P21-Authorized-Launch-and-First-Month.md](#file-prompts-p21-authorized-launch-and-first-month-md)
- [prompts/Review-and-Recovery-Prompts.md](#file-prompts-review-and-recovery-prompts-md)
- [templates/AGENTS.template.md](#file-templates-agents-template-md)
- [templates/ASSET-MANIFEST.md](#file-templates-asset-manifest-md)
- [templates/DECISION-RECORD.md](#file-templates-decision-record-md)
- [templates/EDITORIAL-REVIEW.md](#file-templates-editorial-review-md)
- [templates/EVIDENCE-REPORT.md](#file-templates-evidence-report-md)
- [templates/PROJECT-STATUS.md](#file-templates-project-status-md)
- [templates/RELEASE-CHECKLIST.md](#file-templates-release-checklist-md)
- [examples/README.md](#file-examples-readme-md)
- [PACKAGE-VALIDATION.md](#file-package-validation-md)
- [examples/draft-content.json](#file-examples-draft-content-json)
- [examples/planning-example.schema.json](#file-examples-planning-example-schema-json)


---

<a id="file-readme-md"></a>

## README.md

# WordQuest: The Living Lexicon — Production Blueprint

Prepared for Robert Loterh • 20 September 2026 • Planning baseline v1.0

**An advanced vocabulary adventure with the tactile pleasure, charm, and production discipline of a premium casual game.** WordQuest is a working title, not a cleared commercial name.

This package is the preproduction specification and execution system. No game, asset library, production backend, or store build has been implemented by producing these documents. Examples are design fixtures, not approved release content. The prompts cover the route to a shippable product; executing them successfully means meeting their evidence gates, including human editorial review, device tests, and store requirements. Prompt completion alone is not proof of readiness or a promise of chart success.

## Start here

1. Read [the executive direction](#file-docs-00-executive-direction-md).
2. Read [scope and requirements](#file-docs-01-product-requirements-md), then [the game design](#file-docs-02-game-design-md).
3. Review [engine and tools](#file-docs-07-engine-and-tools-md) and [production roadmap](#file-docs-12-production-roadmap-md).
4. Extract this entire package into a new project workspace, preserving relative paths. Keep planning files together under `planning/` if placing them in a game repository.
5. Open that workspace in your coding environment. Attach this README and [the execution index](#file-prompts-00-execution-index-md). Run [P00: environment and evidence](#file-prompts-p00-environment-and-evidence-md). It inspects and records; it does not start game implementation.
6. Continue with P01 and subsequent eligible prompts in dependency order after implementation is authorized. Each prompt defines artifacts, checks, and stop conditions. Technical gates can pass on evidence without repeatedly asking the owner for routine permission.

## Documentation map

| Document | Purpose |
|---|---|
| [00 Executive direction](#file-docs-00-executive-direction-md) | Product promise, audience, ambition, assumptions |
| [01 Product requirements](#file-docs-01-product-requirements-md) | Requirements, scope, launch definition |
| [02 Game design](#file-docs-02-game-design-md) | Core loop, modes, progression, difficulty, rewards |
| [03 Curriculum](#file-docs-03-curriculum-and-mastery-md) | Advanced-word selection, learning model, editorial quality |
| [04 Narrative and levels](#file-docs-04-narrative-and-level-design-md) | World, characters, first chapter, level recipes |
| [05 UX and accessibility](#file-docs-05-ux-and-accessibility-md) | Screens, flows, text entry, edge states |
| [06 Art, motion, and sound](#file-docs-06-art-motion-and-sound-md) | Visual identity, asset budgets, animation contracts |
| [07 Engine and tools](#file-docs-07-engine-and-tools-md) | Unreal/Blender strategy, tool verification, setup |
| [08 Architecture](#file-docs-08-technical-architecture-md) | Modules, persistence, content delivery, backend |
| [09 Data and authoring](#file-docs-09-data-and-content-pipeline-md) | Schemas, content workflow, sample records |
| [10 AI production](#file-docs-10-ai-production-workflow-md) | GPT-6/Fable workflow, editor automation, runtime AI |
| [11 Quality and metrics](#file-docs-11-qa-performance-and-research-md) | Tests, performance, playtests, retention and learning |
| [12 Roadmap](#file-docs-12-production-roadmap-md) | Milestones, capacity, costs, ownership, critical path |
| [13 Business and live operations](#file-docs-13-business-and-liveops-md) | Monetization, acquisition, ongoing content |
| [14 Release and operations](#file-docs-14-release-and-operations-md) | Stores, support, monitoring, rollback |
| [15 Decisions and risks](#file-docs-15-decisions-and-risks-md) | Defaults, unresolved matters, escalation triggers |
| [16 Sources](#file-docs-16-source-register-md) | Verified references and verification limits |
| [17 Traceability](#file-docs-17-requirements-traceability-md) | Requirement → prompt → evidence |
| [18 First ten working days](#file-docs-18-first-ten-working-days-md) | Practical local starting sequence |
| [Execution index](#file-prompts-00-execution-index-md) | Ordered implementation prompts and handoff rules |
| [Creative prompt library](#file-prompts-creative-asset-prompts-md) | Concept, UI, Blender, motion, VFX, and audio briefs |
| [Recovery and review prompts](#file-prompts-review-and-recovery-prompts-md) | Resume, review, bug, performance, and content repair |

Templates include an agent-instructions template, project status, decision record, evidence report, asset manifest, editorial record, and release checklist. `examples/` contains illustrative structured content. `MANIFEST.json` contains file sizes and checksums. `PACKAGE-VALIDATION.md` describes the checks actually run on this package.

## Baseline in one table

| Area | Planning decision |
|---|---|
| Audience | Adults 18+ who already read English comfortably and want advanced vocabulary |
| Platforms | Android first for validation; Android and iOS for v1.0; Windows after mobile qualification |
| Presentation | Portrait-first 2.5D adventure; readable 2D interaction over stylized dimensional scenes |
| Engine | Unreal 5.8.2 as user-reported candidate; pin only after installed-build and mobile checks |
| Art | Blender 5.x pipeline, exact installed version recorded at P00 |
| Launch | 600 reviewed word senses; 3 districts; 60 authored missions; 4 core challenge modes plus story capstones |
| Slice | 120 reviewed senses; 12 missions; one district; all core systems demonstrated |
| Learning | Sense-specific recall, context, precision, usage, spaced review; no trivial target words |
| Offline | Core purchased/downloaded campaign and review playable offline |
| Revenue | Free opening chapter plus one-time full-campaign unlock; optional cosmetics later |
| AI | Strong during production; optional bounded tutor, not required for launch or core scoring |
| Release claim | Complete premium first release, followed by measured expansion—not a guaranteed ranking |

Owner decisions can amend these defaults through a decision record. Preserve requirement IDs and update traceability when changing scope. Do not silently replace Unreal, introduce subscriptions, reduce the vocabulary standard, or declare a gate passed without evidence.


---

<a id="file-docs-00-executive-direction-md"></a>

## docs/00-Executive-Direction.md

# Executive direction

## Product thesis

Build a game people choose because its world feels enchanting, its interactions feel wonderful, and its language challenges make them more articulate. The central fantasy is becoming a skilled Keeper who restores a city whose records, agreements, and stories are losing their meaning. Precision brings the world back to life.

**Promise:** Discover powerful words. Understand the difference. Use them with confidence.

Our competitive aspiration is Candy Crush-level clarity, polish, responsiveness, longevity, and affection. Our initial audience is narrower: serious vocabulary learners. Chart position depends on product-market fit, acquisition, distribution, content, and sustained operations. It is not a deliverable an engine or model can guarantee.

## Four pillars

1. **Meaning changes play.** A player's interpretation reveals evidence, changes a character's response, or restores a mechanism. Words are functional in the adventure.
2. **Mastery is visible.** Progress shows recall and use over time, with transparent evidence. Correct guesses do not become mastery badges.
3. **Delight has restraint.** Crafted light, materials, sound, and expressive movement support a readable challenge. Long celebrations never obstruct repeated play.
4. **Adult challenge, inviting tone.** Useful advanced vocabulary and sophisticated distinctions, explained clearly. No embarrassment for mistakes, no assumption that obscure language is always superior.

## Audience and boundaries

Primary: adults with fluent or upper-intermediate English seeking precise academic, professional, and expressive vocabulary. The curriculum can broadly target advanced learners, but do not label each word B2/C1/C2 without an appropriate source. CEFR describes language proficiency; a guessed word-level label is not certification.

Secondary expansion: GRE-focused adults, literature enthusiasts, and professional writers. Teen/SAT targeting, school accounts, family products, and multilingual foundations require separate design and release decisions; they are not secretly included in this adult-first launch.

Do not target early readers, teach foundational spelling, or fill the collection with elementary nouns and verbs. Ordinary words remain necessary in explanations and distractors. Advanced senses of common words may qualify when the challenge teaches a genuinely advanced distinction.

## Original creative direction

Working title: WordQuest: The Living Lexicon. A luminous, scholarly city of glass conservatories, amber libraries, ink canals, and brass astronomical instruments. Its inhabitants are charming but capable. The player restores meaning through investigations and linguistic craftsmanship.

The product should have its own silhouettes, symbols, writing, music, and interaction language. Candy Crush is a benchmark for craft and repeatable delight, not a source of copied assets or an instruction to add candy everywhere.

## Experience promises

- First meaningful interaction within a target 30 seconds after required initial screens.
- A satisfying mission fits approximately 3–6 minutes; a daily session fits 8–12 minutes. These are tuning targets, not timers imposed on every player.
- The main route is untimed. Optional speed challenges never reduce learning access.
- Advanced words appear early. A diagnostic adapts support, not the product into a beginner app.
- Returning after an absence begins with a manageable review and a warm welcome.
- Downloaded content works offline; a network error does not erase work.
- Writing and speech labs do not decide campaign success with uncertain AI judgments.

## What 'premium' means operationally

Premium means responsive inputs, coherent art, outstanding typography, stable frame pacing, trustworthy teaching, complete save/resume, useful settings, polished errors, and reliable release operations. It does not require photorealism, a heavy renderer, an open world, or every plugin available.

Each new effect must have a purpose, a device budget, a reduced-motion alternative, and a measurable benefit. Each new system must improve learning, player enjoyment, retention, or reliable operations enough to justify its cost.

## Planning assumptions

Robert is the owner and engineering lead. Staffing, weekly availability, budget, target phones, commercial identity, and access to Mac/iPhone hardware are not yet known. Use the defaults in this package to proceed with planning and reversible prototypes. Record facts during P00. Do not infer a large team or unlimited budget from the quality ambition.

The user reports Unreal Engine 5.8.2 and Blender 5 installed. Public documentation confirms relevant Unreal 5.8 documentation exists, but this session did not inspect those local installations. GPT-6 and Fable 5.1 are the user's preferred development assistants. Assign work by task and verified capability; do not invent Fable's provider, API, context size, or editor access.

## Decision standard

Choose a smaller complete work of exceptional quality over a sprawling incomplete feature list. The first complete release delivers the whole learning-adventure loop, three districts, a resolved story arc, offline reliability, and a sustainable content pipeline. Expansion follows evidence.


---

<a id="file-docs-01-product-requirements-md"></a>

## docs/01-Product-Requirements.md

# Product requirements and release scope

## Success definition

A user can enter without an account, experience an advanced vocabulary mission, receive an explanation, preserve progress, return for appropriately scheduled review, unlock a complete campaign, and finish a satisfying story. Learning improvement must be assessed on delayed and unfamiliar items, not just repeated screens.

All counts below are planning targets. A word sense is a distinct meaning with a stable ID; it is not automatically a unique spelling. Report unique lemmas and senses separately. At launch, aim for at least 550 unique lemmas across 600 senses; do not inflate totals with near-duplicate senses.

## Scope by stage

| Capability | Proof prototype | Vertical slice | v1.0 release | Expansion |
|---|---|---|---|---|
| Reviewed target senses | 30 | 120 | 600 | 2,000+ when justified |
| Missions | 3 | 12 | 60 across 3 districts | New districts |
| Core challenge modes | Context + Forge | All 4 | All 4 | New modes only after tests |
| Narrative | One short scene | One complete district episode | Complete three-district arc | Seasonal stories |
| Art | One benchmark scene | One polished district | Three coherent districts | New environments |
| Review | Simple local scheduler | Durable, sense-specific | Adaptive and validated | Improved model fitting |
| Commerce | None | Sandbox proof | Free chapter + campaign unlock | Optional cosmetics |
| Cloud save | None | Conflict simulation | Optional account + sync | Multi-device expansion |
| AI lab | None | Evaluation prototype only | Optional, default off until qualified | Bounded writing/voice |
| Social | None | None | Shareable personal progress card | Cooperative events, moderated |

The 60 missions include 6 capstones (2 per district). Suggested organization: 3 districts × 4 chapters × 5 missions. Every chapter ends with a scene or reveal. A mission is authored structure and narrative with adaptive practice slots; it does not introduce ten new words in one sitting. The 600-sense curriculum also lives in optional study trails and daily review, so story completion is not synonymous with learning all 600.

## Functional requirements

| ID | Requirement | Acceptance |
|---|---|---|
| PR-001 | Guest-first onboarding | Mission playable without account; progress persists after relaunch |
| PR-002 | Advanced curriculum | Every shipped sense passes selection and editorial rubric |
| PR-003 | Context Detective | Reviewed scene, unambiguous answer set, rationale, hint and retry |
| PR-004 | Word Forge | Meaning-cued target with correct tile multiset and fair input |
| PR-005 | Precision Duel | Distinguishes plausible nearby terms using explicit context |
| PR-006 | Sentence Rescue | Identifies and repairs usage with deterministic accepted variants |
| PR-007 | Story capstones | Vocabulary decisions affect reveal/order/reactions; no permanent lockout |
| PR-008 | Review scheduler | Separate evidence by skill; due queue survives offline and clock changes |
| PR-009 | Word collection | Search, definitions, audio, examples, usage, evidence and review status |
| PR-010 | Save/resume | Crash-safe journal, session resume, migration and backup recovery |
| PR-011 | Optional cloud | Guest migration, conflict handling, account deletion and explicit sync state |
| PR-012 | Offline campaign | Installed entitled content functions with no network |
| PR-013 | Accessible controls | Tap alternative, scalable text, non-colour cues, reduced motion, mute |
| PR-014 | Premium presentation | Art/motion rubric passes on nominated devices |
| PR-015 | Content updates | Versioned validated bundles, atomic activation, rollback |
| PR-016 | Commerce | Sandbox purchase/restore/refund/reinstall and no duplicate grants |
| PR-017 | Measurement | Consent-aware analytics plus honest learning and retention reporting |
| PR-018 | Operational release | Support, monitoring, recovery, store package and owner release decision |
| PR-019 | Optional AI lab | Feature flag; evidence-grounded feedback; deterministic fallback |
| PR-020 | Authoring system | Draft/review/publish separation and traceable rights for assets/content |

## Nonfunctional requirements

NF-001: 60 FPS target on the nominated mid-tier class and optional 30 FPS low tier, measured under sustained play. NF-002: no corruption or duplicate purchase entitlement in interruption testing. NF-003: readable UI on small/tall phones and tablets. NF-004: build reproducibility with pinned toolchain. NF-005: no private keys or service credentials in clients. NF-006: interruption-safe audio/input and resume. NF-007: no unresolved critical/high shipping defects. NF-008: release content has human editorial signoff and provenance. NF-009: network and AI outages never block ordinary practice. Detailed budgets and test recipes live in document 11.

## Essential user journeys

1. New guest → optional goal/diagnostic → first mystery → explanation → reward → save → next mission.
2. Returning player → capped review queue → mission → collection → exit and restore.
3. Offline returning player → cached entitled mission → saved attempts → later sync without duplication.
4. Free player → clear campaign purchase → store confirmation → persistent entitlement → restore on supported device.
5. Accessibility user → text/motion/input settings → full completion without timed or drag-only tasks.
6. User reports a flawed question → issue recorded with content ID/version → corrected item or withdrawn question → progress preserved.

## Release exclusions

No real-time PvP, public chat, guild economy, user-published questions, advertising SDK, procedurally generated production curriculum, open-world locomotion, live-service battle pass, paid hints, or required voice analysis. These are product decisions to protect a complete first release. Optional AI development work cannot delay the required launch path.

## Definition of done

A feature is done when its requirement maps to implementation, content, relevant automated checks, a real-device or user-facing demonstration, accessibility behavior, persistence/error handling, and a short evidence record. 'Code exists', a screenshot, a generated asset, or an agent's self-assessment is insufficient.

## Changes and ownership

Robert owns audience, commercial model, release geography, brand, spending, and publication. Engineering can resolve implementation details within this charter. Changes to launch count, mandatory platforms, learning standard, or business model require a documented owner decision. A missed technical gate triggers correction or a concrete scope tradeoff; it is not silently waived.


---

<a id="file-docs-02-game-design-md"></a>

## docs/02-Game-Design.md

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


---

<a id="file-docs-03-curriculum-and-mastery-md"></a>

## docs/03-Curriculum-and-Mastery.md

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


---

<a id="file-docs-04-narrative-and-level-design-md"></a>

## docs/04-Narrative-and-Level-Design.md

# Narrative and level design

## Premise

The city of Aurelian once stored its promises and knowledge in a living archive. A disturbance called the Blur has made its records imprecise: accusations become ambiguous, agreements lose conditions, and descriptions no longer match reality. The player is a newly appointed Keeper restoring the city's ability to understand itself.

The theme is precision with empathy. The antagonist is not ignorance or people with smaller vocabularies. Characters make understandable mistakes, disagree constructively, and improve alongside the player.

## Cast

- **Mira, the archivist:** capable, curious, dryly funny; concise explanations, never lectures before every move.
- **Pip, a brass-and-ink lantern companion:** expressive through silhouette, light and small gestures; no baby talk. Carries fragments between mechanisms.
- **Orin, the conservatory curator:** observant and deliberate; introduces distinctions in character and description.
- **Sera, the diplomat:** warm and incisive; makes word choice matter in disagreement.
- **The Redactor:** believes ambiguity can prevent conflict; the story explores when precision helps and when excessive certainty harms.

Character designs are original briefs. Names and final title require ordinary brand clearance before commerce.

## Three launch districts

| District | Visual identity | Semantic emphasis | Resolution |
|---|---|---|---|
| The Amber Archive | Walnut, amber glass, brass rails, luminous ink | Evidence, reasoning, uncertainty | Recover the missing testimony |
| The Verdant Conservatory | Jade glass, moss, ivory stone, warm sunlight | Character, observation, description | Restore the catalogue of living things |
| The Astral Court | Indigo, porcelain, silver, restrained starlight | Persuasion, judgment, precision | Rewrite a clear and fair civic accord |

Each has 20 missions, four landmarks, and two capstones. Reuse a modular environment kit while changing composition, atmosphere, materials, and story objects. One district is not merely another hue applied to the same room.

## First session script

0:00–0:15: A dim archive, Pip trying to illuminate an unreadable page. One line from Mira: 'The words are here. Their meaning is slipping.' Play button; account creation absent.

0:15–0:45: The player inspects a short equivocal testimony. Tap-based choice; a small clue appears if requested. The chosen interpretation reconnects a line of luminous ink.

0:45–1:30: Forge 'laconic' from seven tiles after a clear meaning clue. Pip mirrors the player's successful placement with a restrained anticipation and release.

1:30–2:30: Distinguish corroborate from refute using a second witness. The player sees how the correct relationship changes the evidence board.

2:30–4:00: One repair task and one recall of an earlier target, followed by a restored lamp and a new passage opening. A short result shows 'Encountered 3 words' and specific evidence, not 'Mastered 3 words'.

The first session teaches interaction and language without requiring a long explanation of the world's mythology. Timing is a target and must stretch for accessibility.

## Slice mission outline

| Mission | Story objective | Dominant mechanic | New senses target |
|---|---|---|---|
| 1 The Unclear Witness | Interpret testimony | Context + Forge | 3 |
| 2 The Broken Ledger | Establish support | Context + Repair | 3 |
| 3 Between the Lines | Notice implication | Precision | 3 |
| 4 The Careful Clerk | Distinguish care from fussiness | Precision + Forge | 3 |
| 5 A Lamp Restored | Assemble first evidence chain | Mixed | 2 |
| 6 The Missing Qualifier | Repair misleading account | Repair | 3 |
| 7 The Quiet Messenger | Interpret concise speech | Context | 3 |
| 8 Conflicting Records | Weigh plausible claims | Precision | 3 |
| 9 A Better Explanation | Replace vague phrasing | Repair + Recall | 3 |
| 10 The Archive Opens | Complete chapter landmark | Mixed | 2 |
| 11 The Redacted Page | Apply prior distinctions | Mixed review | 1 |
| 12 The Witness Chamber | First capstone | All four | 0 |

This story introduces roughly 29 target senses, with additional senses from the 120-sense slice supplied through curriculum trails and review. Do not overload the 12 missions to force all 120 into immediate exposure.

## Mission record contract

Mission ID, district/chapter/index, prerequisites, narrative objective, opening/closing lines, encounter slots, required sense pool, allowed modes, adaptation constraints, reward ID, restoration state, estimated reading load, audio refs, accessibility variants, and content revision. Prerequisites must form an acyclic graph with a reachable ending.

An adaptive slot can select among approved items meeting constraints. Story-critical wording is fixed; do not insert a randomly selected word that breaks the scene. Dynamic practice is framed as an archive exercise within the mission.

## Level variety and constraints

Alternate interpretation, reconstruction, and application. Never place more than three identical modes consecutively by default. Keep lore text separate from necessary evidence. No branching explosion: use reconverging choices and reusable reaction beats. At chapter end, show a visual transformation, a meaningful revelation, and a preview of the next objective.

## Content review and production

Write an episode synopsis before dialogue; create a low-cost storyboard; play it with placeholder art; review word mechanics; only then produce final shots. Every cinematic needs start/end states, skip behavior, subtitles, audio ducking, and resume behavior. Replaying a movie never reissues rewards. The ending is included in the campaign entitlement and must remain available offline after download.


---

<a id="file-docs-05-ux-and-accessibility-md"></a>

## docs/05-UX-and-Accessibility.md

# UX, interaction, and accessibility specification

## Information architecture

Primary destinations: Journey, Practice, Lexicon, Profile. Journey is the default home. Settings and support remain accessible from every safe pause point. Purchase is offered at a clear chapter boundary and from a dedicated campaign page. Do not occupy the primary navigation with a store.

Portrait phones are the primary layout. Tablets use a wider scene with a bounded reading panel. Windows uses a landscape composition with keyboard support after mobile qualification. Never stretch a phone layout across a desktop without reconsidering spacing and reading width.

## Screen contracts

| Screen | Primary action | Required secondary states |
|---|---|---|
| Welcome | Start adventure | Continue existing save, accessibility shortcut, legal links |
| Goal/diagnostic | Choose path or skip | Honest estimate, progress, pause/resume |
| Journey | Continue mission | Completed, locked with reason, downloaded, downloading |
| Mission intro | Enter | Back, optional recap, loading failure |
| Challenge | Submit answer | Hint, undo, audio, pause, disabled/selected/feedback |
| Explanation | Continue | Why alternatives fail, review word, report issue |
| Mission result | Continue journey | Replay, strengthened words, restoration progress |
| Practice | Begin capped session | No due words, weak skills, optional new trail |
| Lexicon | Open word | Search, filters, empty result, offline audio |
| Word detail | Practice this sense | Meaning, audio, examples, collocations, evidence |
| Campaign purchase | Unlock campaign | Localized price, pending, cancelled, failed, restore |
| Profile/sync | Manage progress | Guest warning, merge preview, conflict, deletion |
| Settings | Adjust experience | Text, motion, sound, input, reminders, downloads |
| Support | Report problem | Content ID included, offline queued report, contact |

## Challenge layout

At a 390×844 logical design reference: top region holds a compact progress indicator and pause; central region holds the scene and essential text; lower region holds the interaction; bottom holds submit/hint controls above the safe area. Treat proportions as a starting composition, not fixed coordinates. The native keyboard must not cover the clue or submit control.

Body target 18–20 logical units with comfortable leading. Support approximately 150–200% text enlargement through reflow and scrolling; exact platform mapping is verified in implementation. Minimum touch area target 48 logical units on Android and at least platform-equivalent comfortable size on iOS. Test long words, repeated letters, large fonts, notches, and narrow devices.

## Input rules

Touch-down gives immediate visual response; touch-up inside commits selection. Selection is distinct from submission for multiple choice. Ignore duplicate submit events using attempt IDs, not only a button disable. Drag interactions always have a tap alternative. Keyboard focus is visible, traversal is logical, and Escape/back opens pause or navigates safely rather than losing progress.

Audio replay does not advance the question or count as a wrong answer. A spoken clue cannot be the only route to a correct answer. Pronunciation playback has text/transcription equivalent as appropriate.

## Feedback language

Correct: 'Exactly—equivocal leaves more than one interpretation open.'
Near miss: 'Plausible, but this sentence emphasizes uncertainty rather than disagreement.'
After help: 'You found it with a clue. We will revisit it later.'
No connection: 'Your progress is saved on this device. Sync will resume when you reconnect.'
No due review: 'Your review is up to date. Explore a new trail or continue the story.'

Avoid 'Wrong!', faux praise for every tap, vocabulary-size claims from tiny diagnostics, and punitive streak copy.

## Accessibility requirements

- Full untimed core campaign; optional timers clearly isolated.
- No colour-only correctness or completion cues; pair with icon and text.
- Reduced motion removes camera travel, repeated particles, screen shake and large spatial transitions while preserving outcome feedback.
- Independent music, effects, voice, and haptics controls; subtitles for narrative speech.
- Screen-reader labels and focus order must be tested on actual target platforms. Unreal's platform accessibility limitations are an early feasibility risk, not something a designer can mark complete from a mockup.
- Reflowed large text; meaning and controls remain visible without shrinking type to fit.
- High-contrast reading surface, restrained glow behind text, no rapid flashing.
- Allow guided alternatives for letter rearrangement and for motor-intensive gestures.
- Meaning/usage scoring is independent of accent and reading speed.

Use current platform accessibility guidance during implementation. Contrast targets are design checks; do not claim complete legal or WCAG conformance from a visual audit alone.

## Save and interruption behavior

Commit an attempt before issuing a reward animation. Pause on backgrounding; stop timers and audio where appropriate. Resume at the last safe interaction boundary without resubmitting. A interrupted restoration cinematic resumes or skips to the persisted final state. A lost network does not reset a challenge.

## First-time experience

One interaction concept per step. Explain hints only when relevant. Offer the diagnostic after the first success or as an optional initial choice; never require a 20-question test before seeing the game. Introduce advanced words with supportive context immediately.

## Prototype validation

Observe at least five intended users with minimal guidance. Tasks: start as guest, solve an unfamiliar target, find explanation, use hint, replay audio, resume after interruption, change text size, find a word, distinguish mission score from retained knowledge. Record confusion and unintended taps. Revise repeated failure points before high-cost polish.


---

<a id="file-docs-06-art-motion-and-sound-md"></a>

## docs/06-Art-Motion-and-Sound.md

# Art direction, animation, VFX, and audio bible

## Art direction: luminous scholarly adventure

Stylized dimensional art with polished material response, soft sculpted shapes, and deliberate composition. Visual anchors: amber glass, aged brass, deep ink, jade enamel, ivory paper. One focal object per screen; interface surfaces remain readable and tactically quiet. The emotional tone is curiosity, competence, discovery, and warmth.

Palette starting tokens: ink #14233B, parchment #F6EFDF, amber #E9B85C, jade #347F73, coral #CB7464, sky #94C9D6. These are art tokens, not prevalidated contrast pairs. Test every text/background combination separately. Avoid relying on red/green for correctness.

Use an expressive display face for brief headings and an exceptionally readable text face for definitions. Select commercially usable fonts with complete English punctuation and phonetic support or a deliberate fallback. Record font licenses. Do not rasterize body text into generated imagery.

## Asset inventory at v1.0

3 district environment kits; 12 landmark states before/after; 4 principal character designs plus Pip; approximately 30 modular props; 4 core challenge component families; 30–40 functional icons; 12 journal/collection decorations; 3 district music loops; approximately 25 interaction cues; reviewed pronunciation audio per released lemma/sense need. Exact counts are production estimates and can be reduced through reuse without reducing the learning scope.

Environments are fixed-camera or gently parallaxed compositions. Use Blender to sculpt, model, rig and render; choose live 3D for a small number of interactive hero objects and characters where it adds value. Bake lighting/detail into textures or rendered layers when that gives the better mobile tradeoff. Keep editable source files and deterministic exports.

## Asset contract

For each asset: ID, purpose, owner, source file, export recipe, target engine import settings, pivot/orientation, scale, material slots, texture dimensions, alpha rules, LODs where needed, collision requirement, animation set, license/provenance, performance estimate, and review status. Use a test scene to verify centimetre/metre conversion, axis, normals, skinning, colour management, alpha edges and texture compression. Do not rely on an assumed universal Blender-to-Unreal transform.

Initial scene budgets: 1–2 live hero characters, mostly baked environments, ordinary props using texture atlases, mostly 1K textures with 2K reserved for justified hero surfaces. These are provisional production constraints; measured memory and GPU time determine actual limits. Exclude 4K texture proliferation and physically simulated decoration with no interaction value.

## Character animation

Pip animation set: idle subtle glow; inspect; anticipate answer; delighted response; curious near-miss; point to clue; carry fragment; celebrate landmark; settle; sleep/pause. Characters use idle, listen, think, agree, disagree gently, explain, reveal, and farewell. Facial poses must remain legible at phone size. Start with a simple rig and authored poses rather than expensive cinematic facial technology.

Animation state changes follow game events. Interruptibility is part of the contract: an idle cannot prevent a tap; a celebration can shorten; a hint reaction cannot obscure the clue. No per-character bespoke state graph when a shared state interface fits.

## Motion language

| Event | Starting duration | Motion intent | Reduced-motion variant |
|---|---|---|---|
| Button press | 70–100 ms | Small tactile compression | Colour/outline change |
| Tile placement | 140–180 ms | Fast settle with tiny overshoot | Direct placement + highlight |
| Correct answer | 300–450 ms | Ink alignment and warm accent | Check icon and brief tint |
| Near miss | 180–250 ms | Gentle return, no punitive shake | Outline + explanation |
| Explanation open | 180–240 ms | Clear layer transition | Immediate panel |
| Mission finish | 800–1,200 ms, skippable | Landmark response and short flourish | Static completed landmark |
| District restoration | 2–4 seconds, skippable | Directed reveal and emotional payoff | Before/after dissolve |
| Background ambient | Slow loops | Subtle life away from reading | Static scene |

Use consistent easing families and finite animation lifetimes. Animations never determine reward authority. Input can continue after a short feedback beat; a repeated player should not spend more time watching celebration than solving.

## Niagara and effects

Use Niagara for localized world-space ink motes, fragment trails, and landmark reveals after compatibility/performance checks. Use UMG/material-based feedback for common UI actions when simpler and cheaper. Do not assume a third-party Niagara-in-UMG bridge is necessary. Avoid stacking multiple full-screen translucent layers and blur passes.

An effect record specifies emitter count, particle limit, lifespan, screen coverage, material complexity, culling distance, low-tier version, reduced-motion version, trigger, cancellation, pooling and measured GPU cost. Initial common-feedback budget: at most two short-lived effects simultaneously and no effect over the clue text. Numbers are hypotheses to profile, not guarantees.

Mobile baseline does not depend on Lumen, hardware ray tracing, Nanite, volumetric fog, or desktop render paths. Those may be useful for offline cinematics or future high-end variants, but the game must look intentionally finished without them.

## Audio

Create a distinctive restrained musical motif. Amber Archive: felt piano, plucked strings, soft mechanical textures. Conservatory: airy woodwinds and gentle organic percussion. Astral Court: warm sustained harmony and subtle bell accents. Correct-answer sounds should vary slightly without becoming a slot-machine barrage.

Separate gameplay cues, pronunciation and narrative buses. Duck music during pronunciation; never overlap two pronunciation clips. Audio reacts to foreground/background, headphones and mute. All meaning-bearing speech has text. Avoid continual full voice acting for every challenge; it multiplies cost and patch size. License or commission audio, keeping proof of permitted commercial use.

## AI-assisted asset pipeline

Generate multiple concepts from the same brief, then choose a coherent direction. Produce orthographic turnaround, expression sheet, material sheet, colour key, and UI reference. AI concepts are references unless explicitly prepared and reviewed as final assets. Generated images do not supply reliable geometry, UVs, rigging, alpha, or usable UI text automatically.

Reconstruct hero assets in Blender; batch export via reviewed scripts; import into a benchmark scene; inspect on phone; iterate. Maintain source provenance and prompt/reference history. Do not ask a model to imitate a named living artist; describe visual attributes and original references.

## Acceptance rubric

Score 1–5 on hierarchy, readability, material consistency, silhouette, motion timing, emotional appeal, and mobile performance. Require no dimension below 4 for the hero slice, plus no blocking usability or accessibility failure. This rubric is an internal review tool. It cannot establish market appeal without player observation.

Capture identical gameplay at native phone resolution, slow motion, muted, and reduced motion. Review clipping, safe areas, particle obstruction, repeated animation fatigue, and hitches. Polish the common interaction before expanding to the full art inventory.


---

<a id="file-docs-07-engine-and-tools-md"></a>

## docs/07-Engine-and-Tools.md

# Engine, tools, and environment plan

## Provisional engine decision

Use Unreal as the first candidate because the owner already has it installed and the art direction benefits from dimensional scenes, native effects, and a unified content editor. The game remains primarily a text-heavy mobile interaction product, so Unreal's packaging, startup, UI accessibility and memory costs must be proven early.

Run one bounded Unreal benchmark before committing to full production: a packaged Android build containing a representative background, one rigged character, 12 letter tiles, large text, audio, a small effect, save/resume, and native keyboard input. Capture sustained frame time, memory, startup and download size. Probe iOS build feasibility at the same stage. An editor viewport on a powerful PC does not pass this gate.

If it fails after one focused optimization pass, document the cause. Compare a lean prototype in a suitable current stable Unity or Godot release using the same art and interactions. This comparison is a contingency, not permission to build two full games. Select the engine based on demonstrated performance, accessibility, development throughput and deployment reliability. Engine changes require a recorded owner decision because they affect cost and the prompt sequence.

## Recommended tool stack

| Tool/system | Role | Decision |
|---|---|---|
| Unreal 5.8.2, user-reported | Game runtime/editor | Verify installed build, pin after P00/P01 |
| C++ | Domain logic, validation boundaries, persistence | Core logic reviewable and testable |
| Blueprints + UMG | Scene assembly and UI presentation | Small graphs; event-driven updates |
| CommonUI | Shared input/navigation where useful | Enable only after packaged compatibility test |
| Niagara | Localized world effects | Built-in candidate; profile mobile behavior |
| Sequencer | Short restoration scenes | Skip/resume support; not every button tween |
| Control Rig / animation tools | Author expressive poses | Use only where they simplify production |
| MetaSounds / engine audio | Interactive sound and mixing | Default audio route; no mandatory middleware |
| Unreal Insights / platform profilers | CPU/GPU/memory diagnostics | Required for performance evidence |
| Blender 5.x | Models, rigs, renders, textures and export scripts | Exact version pinned, exports verified |
| Git + Git LFS | Code and binary asset history | Lock binary assets; exclude generated build data |
| VS Code + supported C++ toolchain | AI-assisted engineering | Discover exact engine compiler requirements |
| Android Studio / SDK / NDK / JDK | Android packaging and device tools | Install versions required by chosen engine |
| Mac + compatible Xcode + iPhone | iOS packaging and signing | Provision before claiming iOS-ready |
| Python | Content validation and asset automation | Pin project environment and dependencies |
| TypeScript + PostgreSQL | Small managed backend, if selected | Resolve provider/SDK at implementation gate |

Optional additions: Figma for collaborative UI source files; a commercial texturing tool if Blender's workflow becomes a bottleneck; a DAW for bespoke audio; a crash-reporting service; an asset inspection plugin proven against the pinned engine. These are candidate purchases, not required installations. Current compatibility, licensing, telemetry behavior, and cost must be checked before use.

Do not install web animation packages such as GSAP, Framer Motion, or Lottie merely because they are popular. They are not automatically native Unreal UI solutions. Rive/Spine-style runtimes or audio middleware merit adoption only after an actual integration need and shipping-build test. Engine-native tools are the initial baseline.

## Version and capability verification

P00 records: engine installation path, exact build/changelist, project association, compiler, SDK/NDK/JDK, Blender build, GPU driver, available disks, device models/OS, Mac/Xcode access, signing account status, AI tool/model labels and editor access. Keep credentials out of reports.

The official Epic mobile pages accessed for this plan are labelled Unreal 5.8. They do not verify the exact installed patch 5.8.2. Blender 5 is user-reported; the exact local patch was not inspected. Some official Blender and Apple-platform requirement pages did not return usable content during research; verify from the local tools and official version-specific requirements during P00.

## Build setup sequence

1. Record environment; create a separate prototype workspace and Git repository when implementation is authorized.
2. Pin engine association and compiler requirements. Build an empty C++ project locally.
3. Configure Android through the supported engine toolchain workflow. Package and install on a physical phone.
4. Establish iOS compilation/signing path with compatible Mac/Xcode and a real iPhone. Record any missing resource explicitly.
5. Add only baseline modules, UMG and required platform components. Disable unused plugins with care.
6. Import one Blender export and verify transform, materials and animation.
7. Establish source/LFS rules and a clean-clone build recipe before large assets accumulate.

## Rendering strategy

Start with a baked-lighting composition and mobile forward rendering; profile against the actual representative scene. Epic recommends forward for precomputed-lighting projects, while deferred has different advantages for dynamic-lighting workloads. Do not assume one path wins universally. [Epic mobile rendering guidance](https://dev.epicgames.com/documentation/en-us/unreal-engine/mobile-rendering-and-shading-modes-for-unreal-engine)

Use event-driven UI changes and avoid unnecessary per-frame bindings or nested layout complexity. [Epic UMG optimization](https://dev.epicgames.com/documentation/en-us/unreal-engine/optimization-guidelines-for-umg-in-unreal-engine)

## Plugin adoption checklist

Need; alternatives; exact version; engine/platform support; source availability; commercial rights; maintenance history; binary packaging; size/memory impact; failure behavior; uninstall path; owner-approved spend if any. Verify in a shipping configuration, not just editor play. Never auto-upgrade all dependencies mid-milestone.


---

<a id="file-docs-08-technical-architecture-md"></a>

## docs/08-Technical-Architecture.md

# Technical architecture

## Principles

Offline-first core learning, deterministic scoring, data-driven curriculum, presentation separated from learning state, and a small backend with clear authority. No runtime AI dependency in the campaign. Use a modular monolith rather than distributed services until scale or ownership makes a split necessary.

## Client modules

| Module | Responsibility | Must not own |
|---|---|---|
| LexiconDomain | Senses, accepted answers, progression and scoring | Widgets/network |
| LearningScheduler | Due skills, evidence rules, queue composition | Rewards and rendering |
| SessionRuntime | Mission state machine and attempt lifecycle | Store verification |
| Presentation | UMG screens, input, animation events | Canonical mastery writes |
| WorldPresentation | Scenes, characters, Niagara, cinematics | Entitlement decisions |
| ContentRuntime | Bundle resolution, schema/version compatibility | Editorial approval |
| Persistence | Journal, snapshots, migration and recovery | UI-derived truth |
| PlatformServices | Audio/input lifecycle, purchases, secure tokens | Hard-coded business logic |
| SyncClient | Outbox, retries, account migration and reconciliation | Trusting client purchase claims |
| Telemetry | Consent-aware event queue and crash breadcrumbs | Raw sentence/audio capture by default |

Prefer pure C++ data/logic where practical, wrapped by Unreal-facing classes. Use GameInstance subsystems for long-lived services only when appropriate; keep screen widgets short-lived and disposable. A single composition root wires dependencies. Avoid a giant all-purpose GameInstance or Blueprint event graph.

Suggested repository areas: `Source/WordQuest/Domain`, `Learning`, `Sessions`, `Persistence`, `UI`, `Platform`; `Content/WordQuest` for assets; `ContentSource` for reviewed data; `Tools` for validators/importers; `Tests`; `docs`; `evidence`. Exact layout follows project conventions established at P02.

## Session state machine

States: Loading → Intro → Presenting → AwaitingInput → Evaluating → Feedback → NextEncounter → Result → Complete. Pause/background can suspend any safe state. Network state is orthogonal. Failed content loading transitions to a recoverable error with retry or return.

Every submission gets an attempt UUID before evaluation. The evaluator returns a structured outcome: correct/incorrect/accepted_variant, assistance, rationale ID, skill evidence and presentation event. Persistence records the outcome atomically before rewards or animation. Duplicate submissions with the same ID return the same outcome. Presentation completion must not be the only trigger that saves progress.

## Local persistence

Use a versioned event journal plus compact snapshots through a replaceable persistence adapter. Implementation may use supported local storage mechanisms, but atomic write/rename and backup recovery must be demonstrated on both platforms. Do not select an unmaintained SQLite plugin without a compatibility check.

Stored entities: profile, preferences, content versions, session checkpoints, attempts, skill evidence, mission completion, restoration grants, entitlements cache, sync outbox. Each record includes schema version. Checksums detect corruption, not malicious tampering. Keep a last-known-good snapshot; quarantine corrupt files and offer recovery. Migration fixtures cover at least N-1 → N and interrupted migration. Never overwrite an unknown newer save format.

## Backend baseline

Proposed managed PostgreSQL with a small TypeScript API, object storage/CDN for signed content bundles, and platform purchase verification. Choose the actual provider after region, cost, maintenance, and SDK checks; Supabase is a candidate, not a dependency mandated by the user's unrelated projects. No need for Redis, Kubernetes, microservices, or real-time multiplayer infrastructure at launch.

Services: identity, profile sync, entitlement verification, content manifest, consent-aware analytics intake, support intake, optional AI gateway. Admin authoring/publishing is separate from player access. Client-facing credentials cannot publish content or grant campaign access.

## API contracts, proposed

- `GET /v1/content/manifest?client_version=...&platform=...`: compatible signed bundle metadata; no secrets.
- `POST /v1/sync`: authenticated device ID, cursor, batch of uniquely identified events; returns acknowledgements, authoritative grants and new cursor. Limit batch sizes and body sizes.
- `POST /v1/purchases/verify`: platform transaction token/ID with idempotency key; server verifies through current platform mechanism and returns entitlement version.
- `GET /v1/entitlements`: authenticated current grants and revocation state.
- `POST /v1/support/content`: content ID/version, problem category and optional user explanation; rate limited.
- `DELETE /v1/account`: authenticated deletion request with status/recovery behavior documented.
- Optional `POST /v1/tutor/feedback`: approved sense ID/version plus bounded response; structured feedback, refusal/uncertainty states, strict quota.

Standard error envelope: code, retryable, safe message key, request ID. Never leak stack traces or store receipt contents to logs. Retry only idempotent operations with bounded exponential backoff and jitter. A versioned OpenAPI contract is produced during implementation, not guessed from current vendor SDKs in this plan.

## Merge and trust

Attempts deduplicate by UUID; preserve distinct offline attempts. Mission completion is monotonic per content-defined mission ID; restoration rewards grant exactly once per first completion. Cosmetic inventory merges through grant IDs. Preferences use last explicit change with a sensible conflict policy. Scheduler projections rebuild from merged attempts using a pinned algorithm version; do not simply take whichever device reports higher mastery.

Guest-to-account merge presents a concise explanation and preserves both attempt histories. Account deletion creates a tombstone so a stale device cannot silently recreate deleted server data. Document which local data remains and provide local reset. Store transactions, refunds, and campaign entitlements are server/platform-authoritative. Offline learning is permitted, but competitive rankings must not trust arbitrary client mastery reports.

## Content delivery

Each bundle carries content version, schema version, minimum client, IDs, hashes, locale and editorial release ID. Verify integrity and a trusted manifest signature using an approved cryptographic library. Download to temporary storage, validate fully, then activate atomically. Keep the last compatible bundle. An in-progress session stays pinned to its content version; never change an answer key mid-question.

Revoked/incorrect items can be disabled by manifest; offline clients may retain old versions until reconnection. Reports preserve the original content version. Correcting a flawed item does not punish the player or delete unrelated progress.

## Security and data handling

Tokens use platform-secure storage. Never ship service-role secrets, AI keys or signing private keys. Enforce ownership on every data access; test cross-user attempts. Restrict admin publishing, separate staging/production, rotate secrets, maintain dependency inventory. Keep raw writing/audio out of default telemetry. Runtime tutor text is ephemeral unless the user explicitly saves it; policy and implementation must agree.

## Delivery and environments

Local, staging and production have distinct configuration and credentials. Build artifacts record commit, engine/toolchain, content hash and config version. CI validates code/content and packages supported targets on appropriate hosts. CI without Mac access cannot certify iOS. A content rollback and a binary rollback are separate operations; mobile store rollback may require a new release, so remote flags and compatible bundles are essential.


---

<a id="file-docs-09-data-and-content-pipeline-md"></a>

## docs/09-Data-and-Content-Pipeline.md

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


---

<a id="file-docs-10-ai-production-workflow-md"></a>

## docs/10-AI-Production-Workflow.md

# AI-assisted production workflow

## Roles for GPT-6 and Fable 5.1

Use the strongest available reasoning/coding capability for architecture, difficult defects, test design and integration. Use a separate review pass for semantic errors, edge cases, and compliance with the game's contracts. Either named assistant can implement or review depending on actual tool access and observed performance. The plan does not assume an unverified benchmark advantage or invent Fable's provider/API.

Record model label, tool version, task, output, evidence and cost/time where available. Compare assistants on the same small representative tasks: one C++ domain change, one content validator, one Unreal editor asset task, one visual correction, one bug diagnosis. Choose by successful verified output, not marketing adjectives.

## Task packet

Every prompt gets: objective, relevant documents only, current status, baseline commit, owned files, dependency state, constraints, acceptance evidence, and exact stop condition. Do not paste the entire planning bundle into every task. For visual work attach the approved reference plus the interaction and motion spec. A screenshot alone cannot specify behavior.

Official Codex guidance emphasizes concrete context, reproducible steps and verification. Our task packets apply that approach; the particular production roles here are design choices. [Official prompting guidance](https://learn.chatgpt.com/docs/prompting)

## Working loop

Inspect existing state → identify the smallest complete task → implement → build/run → inspect the result → correct defects → record evidence → review → integrate. Never treat a generated diff as tested software. Do not repeatedly ask the owner to approve ordinary refactors within the accepted scope. Escalate product changes, purchases, credentials, destructive actions and public release when needed.

If multiple agents are explicitly authorized in the implementation environment, separate by disjoint source files or worktrees. One writer owns each binary Unreal/Blender asset at a time. Never concurrently edit the same `.uasset`, `.umap`, or `.blend`. Cross-review can be sequential. Multi-agent execution is optional; the plan works with one assistant.

## Unreal and Blender automation

Text is the preferred source for C++, configuration, content JSON and deterministic scripts. Blueprints and binary assets require editor-supported operations. Agents must not fabricate binary asset bytes or claim an asset exists because a script was written. Where editor scripting is supported by the pinned build, use it to import assets, create documented structures, validate names and perform repeatable batch actions.

Unreal Python is an editor automation route, not the shipped mobile gameplay language. Confirm exact APIs in the installed engine before generating automation. Blender Python scripts should create reproducible collections/materials/export settings and operate in a disposable copy before modifying valuable art sources.

If the agent cannot control the editor, it must supply a numbered manual recipe with exact objects/properties, expected screenshot and verification steps. Mark the result blocked on editor execution. A C++ compile does not prove a UMG screen or Niagara effect behaves correctly.

## Evidence contract

Each milestone report records commit, files/artifacts, actual commands, exit results, device/build, content version, screenshots/video where relevant, remaining defects and gate disposition. Evidence paths must exist. A simulated result is labelled simulated. Failed tests remain visible after fixes with the final passing result linked. An unavailable device is a blocker, never an implied pass.

## Prompt execution discipline

Run one numbered task at a time unless dependency-independent work has explicit ownership. Continue routine corrective work inside a task until its criteria pass. If an environmental blocker prevents completion, deliver the concrete partial artifacts and exact recovery action. Do not rewrite the roadmap to label incomplete work complete.

At a context reset, read project status and the latest evidence report, inspect the repo, then resume the first incomplete dependency. Do not restart finished architecture or regenerate all assets. Update status after a meaningful completed unit.

## Runtime AI boundary

The campaign, answer keys, learning evidence and offline review use deterministic approved content. Optional AI lab feedback is advisory. It can explain a sense, suggest a corrected sentence, or role-play a bounded scenario. It cannot silently grant mastery, change published definitions, set prices, or publish new curriculum.

Gateway input: approved sense ID/version, bounded user text, task type. Output: structured judgment (appropriate/needs_revision/uncertain), short explanation, revised example and evidence reference. Keep secrets server-side; set quotas, timeouts and spending alerts. Treat user text as data, not instructions. Reject tool-use instructions embedded in responses; no arbitrary network/tool access.

On outage or uncertain judgment: show a reviewed explanation and allow practice to continue. Do not fail the learner. Voice input is optional, consent-based and separate from pronunciation claims; speech recognition errors and accents must not reduce knowledge scores.

## AI evaluation gate

Create at least 200 representative reviewed examples spanning valid usage, subtle misuse, multiple senses, nonsense, prompt injection, sensitive personal text and dialect variation. Human raters judge correctness, helpfulness and unjustified certainty. Initial target: no critical factual/privacy failure, at least 95% acceptable feedback on the evaluated set, and clearly reported uncertainty for ambiguous cases. This is an internal release target, not a claim that the model meets it now. Track latency/cost on actual requests and compare against a deterministic fallback.

If the optional lab fails, keep it off and ship the complete core game. No subscription or expensive API dependency is required for the launch experience.


---

<a id="file-docs-11-qa-performance-and-research-md"></a>

## docs/11-QA-Performance-and-Research.md

# Quality assurance, performance, and product research

## Evidence levels

L0: authored specification. L1: automated local checks. L2: running editor/staging demonstration. L3: packaged physical-device evidence. L4: target-user observation. L5: operational/store evidence. Each feature requires the relevant levels; a screenshot cannot substitute for L3 performance or L4 comprehension.

## Provisional device budgets

These are project targets, not measured results or store limits. P01 names actual devices and revises budgets from evidence.

| Metric | Initial target | Measurement |
|---|---|---|
| Mid-tier active play | 60 FPS target; p95 frame time ≤20 ms | 20-minute physical-device run |
| Supported low tier | Stable 30 FPS; p95 ≤35 ms | Same sequence with low profile |
| Touch response | visible response within 100 ms target | High-frame-rate recording |
| Peak working memory | ≤700 MB on 4 GB Android target | Platform profiler; include scene transitions |
| Cold start to playable | ≤5 seconds after initial setup | Ten cold launches; median and p95 |
| Base delivery | ≤250 MB compressed aspiration | Actual store-style package report |
| Full campaign download | ≤750 MB aspiration | Bundle sizes incl. audio |
| Core offline | All installed entitled missions and review | Airplane-mode matrix |
| Reliability | ≥99.5% crash-free sessions in meaningful beta sample | Report numerator, denominator, build |

Measure frame hitches, shader compilation, thermal throttling and battery behavior. Do not reduce reading clarity to pass a GPU budget. A device excluded from support is explicitly documented; an emulator does not qualify it.

## Test pyramid

Domain tests: answer normalization, repeated tiles, option shuffle, assistance rules, distinct-context evidence, delayed retention, queue caps, mission prerequisites, duplicate submissions, grant idempotency. Property/invariant tests where valuable: no negative interval, no hint-treated-as-unaided, no reward duplication, no impossible tile solutions, no missing-reference release.

Integration: save interrupted mid-write, backup restore, old-schema migration, two-device divergent attempts, guest merge, deleted-account stale sync, revoked item, interrupted bundle activation, corrupt bundle, purchase pending/cancelled/refunded, entitlement restore.

UI/device: small screen, largest text, keyboard, tap alternative, screen reader, reduced motion, all audio off, background/resume, incoming call, low storage, loss of connection, slow download, device rotation policy, cold start.

Content: every release record validated, editor signoff, answer rationale, audio match, rights, coverage, capstone ambiguity. Semantic review is not replaceable by unit tests.

## Required scenario matrix

Q01 duplicate submit emits one attempt and one grant. Q02 kill app after answer before celebration preserves outcome. Q03 wrong answer plus revealing hint cannot grant unaided recall. Q04 same question repeated instantly cannot count as retained. Q05 clock moved forward/backward cannot repeatedly farm rewards. Q06 offline purchase cannot fabricate entitlement. Q07 refund updates connected clients while offline policy is documented. Q08 corrupted content falls back safely. Q09 large text preserves complete clue and controls. Q10 no-audio/no-motion campaign remains completable. Q11 free campaign boundary permits review of previously learned free senses. Q12 two-device merge preserves attempts and avoids duplicate restoration. Q13 withdrawn question does not punish prior progress. Q14 account deletion does not resurrect on stale sync. Q15 resumed cinematic never grants twice.

## Playtest progression

Discovery: 8–12 intended adult learners; interview motivations and word-study frustrations. Prototype: 5–8 observed users; test comprehension, interaction and desire to continue. Slice: 20–30 users across ability/device range; examine repeated use and delayed learning. Beta: recruit a larger cohort appropriate to confidence needs; do not pretend a handful of users establishes business viability.

Ask players to explain a word in their own terms and apply it in a new context. Observe whether they understand why a distractor fails. Measure whether they return without compensation or researcher reminders separately from scheduled research sessions.

## Metrics dictionary

Activation: first mission completed / eligible new installs. D1/D7/D30 retention: proportion of an install cohort returning in a specified day window; publish the exact timezone/window and exclude only predeclared invalid installs. Mission completion: completion / mission starts. Hint rate: assisted attempts / attempts. Delayed retention: correct unaided held-out responses / eligible delayed responses, with attrition reported. Weekly retained senses: unique senses newly meeting the stated delayed evidence rule per active learner. Do not count all exposures as words learned.

Initial product discussion targets: activation ≥70%, D1 ≥35%, D7 ≥15%, D30 ≥8%. These are provisional internal hypotheses, not published industry benchmarks or forecasts. Reassess with audience, channel, sample size and confidence intervals. Good retention without meaningful learning is a product failure; learning gains with no voluntary return mean the game loop needs work.

## Telemetry events

session_start/end; mission_start/complete; challenge_presented; attempt_submitted; hint_used; explanation_opened; sense_stage_changed; review_due/completed; restoration_granted; bundle_download/activated/failed; purchase_started/result/restored; sync_failed/recovered; content_reported. Shared fields: anonymous/consented profile ID, build, content/config version, session ID, device class, locale and event ID. No raw writing, audio, email or receipt in standard analytics.

## Art and motion QA

Capture a standard scene set before/after each visual milestone. Review safe areas, baseline alignment, line breaks, word lengths, animation overlap, translucent overdraw, texture blur, letter contrast and aliasing. Pair visual comparison with hands-on play; a screenshot cannot reveal input lag or animation fatigue.

## Exit policy

No unresolved severity-1/2 defect affecting crash, data loss, purchase, content correctness, security or campaign completion. Lower issues have owner, impact and disposition. A flaky required test is a defect to investigate, not a reason to ignore the gate. Record actual results in the evidence template.


---

<a id="file-docs-12-production-roadmap-md"></a>

## docs/12-Production-Roadmap.md

# Production roadmap, staffing, and cost control

## Schedule stance

There is no reliable single completion date without staffing, weekly availability, device access and observed content throughput. Use milestones with exit evidence. For a solo engineer with targeted contract art/editorial help, a polished 600-sense release could plausibly take 12–24+ months; a small experienced team might target 6–12+ months. These are rough planning scenarios, not commitments. Unreal learning, asset revisions, editorial work and store operations can dominate the schedule despite fast AI coding.

## Milestones

| Gate | Deliverable | Planning effort window | Exit evidence |
|---|---|---|---|
| G0 Environment | Local facts, supported versions, device/build access | 2–5 working days | P00 inventory and risks |
| G1 Feasibility | Representative packaged mobile benchmark | 1–2 weeks | P01 physical-device report |
| G2 Fun prototype | 30 senses, 3 missions, basic review/save | 3–5 weeks | P02–P05 + observed test |
| G3 Production slice | 120 senses, 12 missions, one polished district | 6–10 additional weeks | P06–P10 and slice report |
| G4 Feature alpha | Complete systems and authoring workflow | 4–8 additional weeks | P11–P14 integration evidence |
| G5 Content beta | 600 senses, 60 missions, all art/audio | 8–16+ additional weeks | P15–P17 content/device reports |
| G6 Release candidate | Store builds, purchases, operations and fixes | 4–8 additional weeks | P18–P20 evidence |
| G7 Launch/operate | Staged launch and first content cycle | Ongoing | P21 operational review |

Windows overlap only when responsible people and resources exist; do not add columns and present the sum as a promise. Solo work and specialist availability may stretch these windows. Content production begins after the schema is stable and continues through alpha; it is a critical path, not final polish.

## Ownership

Robert: product owner, engineering lead and release decision. AI assistants: implementation, documentation, draft assets/content and review assistance, subject to evidence. Needed human functions: vocabulary editor/lexicographer, art/animation judgment, target-user research, platform/device QA, and business/legal/account ownership. One person can cover several functions, but their hours still count. Plan targeted contractor help for editorial and hero art if budget allows.

## Content capacity model

Launch minimum = 600 senses × 6 reviewed items = 3,600 items, plus definitions, examples and audio. If complete review averages 4–8 items per reviewer-hour, item review alone is approximately 450–900 hours. Measure actual throughput on the first 30 senses; difficult precision items may take longer. Add drafting, rework, audio, testing and metadata. AI reduces drafting effort but does not remove semantic verification.

## Cost worksheet

Track actual local currency and quotes rather than inventing software prices. Lines: engineering time; editorial hours; concept/3D/animation; music/audio rights; test phones; Mac/iPhone access; engine/marketplace obligations; developer accounts; AI subscriptions and usage; backend/CDN; crash monitoring; localization; acquisition tests; support. Separate one-time investment, monthly operating costs and per-user variable costs.

Formula: total production = labour + art/audio + hardware + tools/accounts + contingency. Operating monthly = fixed services + active users × storage/egress/support + optional AI calls × measured cost. Begin with a 20–30% contingency as an owner-adjustable planning allowance, not a statistical guarantee. Verify current engine licensing and all commercial terms before revenue.

## Critical path

Toolchain/device proof → input/readability proof → core loop → content schema → learning/save correctness → hero art slice → editorial throughput → complete curriculum/campaign → purchase/platform qualification → beta evidence → release. Delay expensive full-world art until the loop survives observed playtesting.

## Backlog organization

Epics: platform foundation; curriculum tooling; challenge system; learning; narrative; art/audio; accessibility; persistence/sync; commerce; content production; research/analytics; release/operations. Each ticket contains requirement ID, concrete user outcome, dependencies, files/assets, acceptance evidence and owner. Keep stories small enough to build and verify without a month-long opaque branch.

Weekly cadence: select outcomes from blockers and gate dependencies; integrate working changes; review a device build; examine content throughput and player evidence; update risk/cost forecast. The demo should show the actual game, not slides alone.

## Scope adjustment rules

Preserve advanced learning, input quality, core offline play, save integrity and a complete story arc. First defer runtime AI lab, social play, extra cosmetics, extensive voice acting, Windows, and optional cinematics. Reducing the 600-sense/60-mission promise is an explicit release scope decision with marketing updates. Do not quietly ship a prototype as the planned full release.

## Procurement sequence

Immediately: inventory existing tools/hardware; no purchase required for the planning package. Before G1: required compatible compiler/Android tooling and access to representative devices. Before iOS qualification: Mac/Xcode/iPhone and relevant account access. Before G3: editorial and art capacity. Before commerce: verified store accounts, business identity, rights and tax/payment setup. Before launch: support contact, monitoring and current submission requirements.


---

<a id="file-docs-13-business-and-liveops-md"></a>

## docs/13-Business-and-LiveOps.md

# Business model, engagement, and live operations

## Positioning

A premium advanced-English adventure for people who enjoy difficult words and want to use them accurately. The first market experiment should test this promise with adult professionals, university-level readers, vocabulary enthusiasts and adult exam candidates. Do not claim affiliation with exam owners or guaranteed scores.

Benchmark dimensions: Candy Crush for interaction clarity and emotional reward; vocabulary products for teaching trust and practice depth; narrative puzzle games for atmosphere and meaningful progression. Conduct direct product teardowns during discovery rather than assuming this plan proves competitor gaps. Vocabulary.com's public product describes vocabulary learning and practice; that establishes an existing category, not evidence that our concept will outperform it. [Vocabulary.com](https://www.vocabulary.com/)

## Launch monetization

Default: free first chapter (5 missions and a corresponding starter curriculum of about 50 senses), followed by a one-time full-campaign unlock. The purchased campaign contains all 60 missions and 600 senses, including the free content. Previously available free senses remain reviewable. Downloaded purchased content remains playable offline under a documented entitlement-cache policy.

No ads, paid hints, energy or learning penalties at launch. Cosmetics can follow once production and demand justify them. A recurring subscription is not the baseline because the first product is a complete campaign, not an unbounded promise of continuous tutoring. Paid future expansions need explicit scope and pricing.

Price is an owner decision after market interviews and regional willingness-to-pay tests. Show current store-localized prices; never hard-code a guessed currency conversion or write placeholder prices into release assets. Verify current platform payment rules for target storefronts at submission.

## Retention strategy

Story curiosity; visible restoration; challenging but fair practice; retained-word evidence; manageable review; a personal collection worth revisiting. Gentle reminders require opt-in. Players choose goals and quiet hours. Missing days never destroys progress. Support re-entry with a short recap and a capped workload.

Daily content is pre-reviewed and scheduled. Four-week operational rhythm: week 1 publish one small content pack; week 2 inspect item quality and feedback; week 3 tune/fix; week 4 prepare the next verified pack. Adapt cadence to editorial capacity. Never promise weekly stories without funded production throughput.

## Acquisition experiments

Test three messages with genuine gameplay clips: become more articulate; master subtle distinctions; explore a beautiful word adventure. Measure qualified interest and activation, not only views. Recruit beta readers through appropriate communities and voluntary signups; avoid spam. Use real screenshots of running builds for store claims.

Small-budget tests begin only with owner-defined spending caps. Track channel, cohort, acquisition cost, conversion, refund rate, retention and contribution margin. Do not scale paid acquisition solely because a video gets clicks. Assess whether lifetime contribution can cover acquisition with uncertainty, especially for a one-time purchase product.

## Metrics and reporting

North star: weekly learners who demonstrate at least one retained sense and voluntarily return. Supporting metrics: activation, D7 retention, delayed recall, campaign completion, purchase conversion, crash-free sessions, content reports, refunds and support burden. Revenue cannot compensate for misleading mastery claims.

A weekly report includes denominators, cohort maturity and device/channel mix. Separate development testers, incentivized research participants and genuine customers. Do not compare immature D30 cohorts with mature ones.

## Operations controls

Versioned content calendar; reviewer coverage; remote disable of flawed items; feature flags for risky optional features; incident owner; refund/support process; safe maintenance notice. A live event cannot require undocumented client capabilities. New content must load on the supported client matrix or be filtered by minimum version.

## Expansion path

After evidence: additional advanced curriculum trails, new districts, bounded writing lab, Windows release, cooperative goals without public chat. Teen/SAT product and multilingual entry paths need new audience research, content treatment, privacy and platform review. Real-time competition is a separate investment in fairness, networking and moderation.


---

<a id="file-docs-14-release-and-operations-md"></a>

## docs/14-Release-and-Operations.md

# Release, support, and operations runbook

## Release definition

A release candidate is a reproducible signed build containing the promised approved content, with entitlement handling, save migration, accessibility, performance and operational evidence. This plan does not authorize public publication or purchases today. The execution sequence prepares a reviewable candidate; the owner decides release when the gates pass.

## Platform prerequisites

Android: pinned engine-compatible SDK/NDK/JDK, required architectures, package name, signing-key custody, current target API and store packaging requirements, real-device qualification and current testing obligations for the actual developer account.

iOS: supported engine/Xcode/macOS combination, Mac build path, physical iPhone testing, bundle ID, certificates/profiles, required privacy disclosures and store account. Windows-only editor work cannot certify iOS. Record exact values from official requirements during P00/P18 rather than freezing guessed versions in this dated plan.

Windows expansion: chosen distribution channel, supported architecture, installer/package signing, DPI/input/accessibility, persistence paths, updates and commerce differences. Do not assume the Android purchase SDK works on Windows.

## Store-readiness checklist

- Brand/title cleared sufficiently for commercial use; business and support identity supplied by owner.
- Accurate description, original icon, real gameplay screenshots, preview footage, age/content questionnaire and category.
- Purchase products configured, price approved, sandbox purchase/restore/refund behavior demonstrated.
- Privacy policy, data disclosures, account deletion behavior and permissions match actual implementation.
- Relevant font, image, audio, dictionary, engine and plugin rights recorded.
- Review access or demonstration instructions provided where necessary; staging credentials never shipped in the client.
- All content in screenshots is present; no unsupported learning, score or ranking claims.
- Current rules checked for each intended geography/storefront, including region-specific commerce differences.

Apple's current guidelines cover complete metadata, tested builds, review access and purchase information. Google provides its app-creation and setup workflow. They change; recheck at submission. [Apple review guidelines](https://developer.apple.com/app-store/review/guidelines/) · [Google Play setup](https://support.google.com/googleplay/android-developer/answer/9859152)

## Release candidate sequence

1. Freeze candidate code/content/config identifiers; produce changelog and known-issues list.
2. Build from clean checkout using pinned tools; archive logs and hashes.
3. Run required domain/content/integration gates; execute physical-device matrix.
4. Validate production-like backend, least-privilege access, purchase sandbox and content signatures.
5. Exercise backup restore, bundle rollback, disable flag and support intake.
6. Produce store metadata, disclosures, screenshots, and review notes.
7. Present candidate evidence and unresolved owner decisions.
8. After explicit owner publication decision, submit/distribute through the intended platform workflow.
9. Use available staged distribution controls and monitor before widening exposure.

## Monitoring

Dashboards: crash-free sessions by build/device, startup and frame regressions, content activation errors, sync backlog, purchase verification failures, item reports, support response time and backend cost. Alert thresholds begin conservative and are tuned to traffic. A sudden transaction or save failure is urgent even at low volume.

## Incident classes

Critical: save loss, incorrect entitlements, privacy exposure, widespread crash, blocked campaign, systematically wrong teaching. Disable affected optional features/content where safe, preserve evidence, communicate concretely, and begin repair. Do not clear users' saves to hide a migration problem.

High: repeated device-specific crash, broken audio bundle, unfair capstone, stuck download. Contain by config/content rollback or platform hotfix; publish a known-issue note where appropriate.

Low: cosmetic clipping or minor copy error without semantic impact. Schedule a patch with a regression check.

## Rollback

Content: revert manifest to a compatible prior bundle, preserve IDs and account for withdrawn items; keep session pinning. Backend: revert deploy where compatible; use backward-compatible migrations and tested restore procedures. Client: disable risky features remotely and prepare corrected store build; a store binary cannot be assumed instantly reversible.

## Support and data requests

Support report contains build/device, content ID/version, safe error code and optional user explanation. Avoid raw receipt, private message or audio attachments by default. Document response ownership, refund routing, account deletion, local reset and lost-device recovery. Deletion requests must propagate to active storage and respect a documented backup retention policy; verify current requirements with appropriate advice for the actual business.

## Post-launch first month

Daily early review of crashes/purchases/content failures; weekly cohort and learning review; one controlled content update after rollback proof; support taxonomy; first cost report; decision on acquisition expansion. Freeze discretionary new features during an unresolved reliability or content-quality incident.


---

<a id="file-docs-15-decisions-and-risks-md"></a>

## docs/15-Decisions-and-Risks.md

# Decisions, assumptions, and risk register

## Defaults adopted for planning

| ID | Decision | Reason | Revisit trigger |
|---|---|---|---|
| D01 | Adults 18+ first | Serious advanced vocabulary; focused audience | Owner selects teen/school market |
| D02 | Portrait 2.5D | Readable touch play with premium scene depth | Device/user test contradicts |
| D03 | Unreal candidate, early gate | Existing installation and art tooling | Packaging, accessibility or performance fails |
| D04 | 600 senses / 60 missions | Complete bounded first campaign | Capacity/budget evidence requires owner change |
| D05 | Four modes + capstones | Variety with manageable engineering | Repeated boredom or weak transfer |
| D06 | Deterministic campaign | Fair scoring, offline reliability, cost control | New mode requires bounded evaluated AI |
| D07 | Guest/offline-first | Low friction and reliable access | Specific business necessity |
| D08 | One-time campaign unlock | Clear value and finite content promise | Owner chooses funded live-service model |
| D09 | Android validation; Android+iOS v1 | Fast local proof plus broad mobile release | iOS resources remain unavailable |
| D10 | Human editorial signoff | Semantic quality and trustworthy teaching | Never removed solely to accelerate output |

## Owner inputs to collect without blocking this planning package

Weekly hours; available budget range; solo/contractor/team preference; target device models; Mac/iPhone access; launch countries; business/store-account status; preferred visual references; desired paid/free model; desired name; accessibility commitments; whether Windows must join first release. P00 records known answers and default assumptions. Do not ask the owner to restate facts already supplied.

## Risk register

| ID | Risk | Probability/impact estimate | Mitigation | Trigger/owner |
|---|---|---|---|---|
| R01 | Unreal overhead on target phones | Medium/high | Packaged benchmark, baked scenes, bounded fallback comparison | G1 engineering |
| R02 | Beautiful but repetitive quiz loop | High/high | Observe voluntary replay before mass art/content | G2/G3 product |
| R03 | Ambiguous or unnatural advanced content | High/high | Human review, alternatives rationale, item reports | Every batch editor |
| R04 | Content workload exceeds capacity | High/high | Measure 30-sense throughput, budget editorial help | G2 owner |
| R05 | iOS build/signing resources absent | Medium/high | Identify Mac/iPhone route early | G0 owner |
| R06 | Generated assets lack consistency/rights | Medium/high | Style bible, reconstruction, rights manifest | Art review |
| R07 | Binary asset conflicts | Medium/medium | Asset locks, one writer, small ownership units | Engineering lead |
| R08 | Save/sync/purchase duplication | Medium/high | IDs, journals, authority and interruption tests | G4 engineering |
| R09 | AI tutor confident errors/cost | Medium/high | Optional flag, human-rated evals, quota, fallback | AI lab owner |
| R10 | Scope inflation | High/high | Fixed launch contract, change records | Weekly product |
| R11 | Weak market acquisition | Medium/high | Positioning tests, cohort economics, capped spend | Beta/owner |
| R12 | Inaccessible text/input despite polish | Medium/high | Early real-device screen reader and large-text proof | G1/G3 UX |
| R13 | Tool/model/version assumptions false | Medium/medium | Local inventory and official compatibility checks | P00 engineering |
| R14 | Store/legal/commercial blockers | Medium/high | Current requirement checks before candidate | Release owner |

Probability labels are planning judgments, not calculated forecasts. Update with observed evidence and mitigation status.

## Escalation rules

Engineering chooses routine module structure, tests, bugs and optimization within the accepted charter. Ask for a concrete owner decision when changing audience, engine, paid model, launch-platform commitment, content promise, budget, account identity, or public release. Present options with consequences and a recommendation. Missing test evidence is a blocker to the claim, not a reason to invent success.

## Decision log format

Date; ID; question; facts; assumptions; options; chosen action; owner; cost/schedule impact; affected requirements/docs/prompts; revisit trigger. A later explicit owner decision supersedes this planning baseline. Keep change history and update all affected counts.


---

<a id="file-docs-16-source-register-md"></a>

## docs/16-Source-Register.md

# Source register and verification limits

Research date: 20 September 2026. Links below were opened during preparation unless marked otherwise. Tool availability, product versions, commercial terms and submission rules must be rechecked when implementation or release occurs.

| Source | What it supports | Limits |
|---|---|---|
| [Epic mobile rendering modes](https://dev.epicgames.com/documentation/en-us/unreal-engine/mobile-rendering-and-shading-modes-for-unreal-engine) | Mobile forward/deferred tradeoffs; baked-lighting direction | Documentation labelled 5.8; does not inspect local 5.8.2 or prove our performance |
| [Epic UMG optimization](https://dev.epicgames.com/documentation/en-us/unreal-engine/optimization-guidelines-for-umg-in-unreal-engine) | Event-driven UI, layout/animation cost awareness | Requires measurement for this particular interface |
| [Epic Niagara overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine) | Niagara is an engine VFX system | Not a test of our effects or plugins |
| [Epic Android support](https://dev.epicgames.com/documentation/en-us/unreal-engine/android-support-for-unreal-engine) | Toolchain, packaging, profiling and platform workflows | Resolve exact requirements for pinned build at P00 |
| [OpenAI prompting guidance](https://learn.chatgpt.com/docs/prompting) | Concrete context, reproduction, focused tasks and verification | No guarantee a prompt produces correct Unreal assets |
| [OpenAI developer documentation](https://developers.openai.com/) | Current GPT-6 Astra-related documentation surfaced | No model-price, context-limit or performance claims needed in this plan |
| [Retrieval practice overview](https://www.retrievalpractice.org/why-it-works) | General value of active retrieval | Does not validate our game, thresholds or schedule |
| [Spacing overview](https://www.retrievalpractice.org/spacing) | General spaced-practice rationale | Our interval policy is a testable starting design |
| [Vocabulary.com](https://www.vocabulary.com/) | Existing vocabulary-learning category/product | No direct hands-on competitor evaluation performed |
| [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) | Submission completeness and current review considerations | Recheck storefront-specific rules; not legal advice |
| [Google Play app setup](https://support.google.com/googleplay/android-developer/answer/9859152) | App-creation/setup process | Recheck actual account, region and testing rules |

## Explicitly unverified

The local Unreal 5.8.2 and Blender 5 installations were reported by Robert and not accessed here. Official Blender release/manual pages attempted in research did not provide usable content in this session; do not construe the plan as validation of an exact Blender patch. Some Epic Apple-platform requirement pages were similarly unavailable or empty. Exact Xcode/macOS/SDK compatibility remains P00 work.

Fable 5.1 is retained as the user's chosen assistant label. Its provider, APIs, pricing, editor control and model limits were not independently established. The execution method is capability-based and does not depend on invented Fable-specific commands. OpenAI documentation was used for general verified workflow guidance; no assumption that subscription access equals API access is made.

Specific third-party plugins and paid tools are not approved purchases or verified integrations. The candidate engine tools must be proven against the installed build and packaged targets. No engine licensing rates, store fees, software prices or acquisition benchmarks are asserted.

## Original design judgments

The story, title, mechanics, scope counts, palette, motion timings, performance budgets, retention targets, learning-stage rules, schedule scenarios and staffing estimates are original planning proposals. They are not facts sourced from the reference pages. They should be validated through prototyping, editorial work, device tests and user research.


---

<a id="file-docs-17-requirements-traceability-md"></a>

## docs/17-Requirements-Traceability.md

# Requirements traceability

All evidence is pending implementation. This table describes required proof; it is not a completion claim. Store exact artifact links and build IDs in the implementation evidence reports.

| Requirement | Implement/verify tasks | Required evidence |
|---|---|---|
| PR-001 | [P02](#file-prompts-p02-project-foundation-md), [P06](#file-prompts-p06-ux-and-design-system-md) | Guest start and relaunch |
| PR-002 | [P03](#file-prompts-p03-content-schemas-and-validation-md), [P13](#file-prompts-p13-editorial-publishing-toolchain-md), [P15](#file-prompts-p15-full-campaign-and-content-production-md) | Editorial rubric and approved coverage |
| PR-003 | [P04](#file-prompts-p04-core-challenge-modes-md) | Context answer/rationale checks |
| PR-004 | [P04](#file-prompts-p04-core-challenge-modes-md) | Tile multiset/input tests |
| PR-005 | [P04](#file-prompts-p04-core-challenge-modes-md), [P13](#file-prompts-p13-editorial-publishing-toolchain-md) | Semantic contrast review |
| PR-006 | [P04](#file-prompts-p04-core-challenge-modes-md), [P13](#file-prompts-p13-editorial-publishing-toolchain-md) | Repair variants and rationale |
| PR-007 | [P08](#file-prompts-p08-narrative-and-slice-campaign-md), [P15](#file-prompts-p15-full-campaign-and-content-production-md) | Capstone walkthrough and reachable ending |
| PR-008 | [P05](#file-prompts-p05-learning-and-durable-saves-md) | Scheduler replay and evidence rules |
| PR-009 | [P06](#file-prompts-p06-ux-and-design-system-md), [P15](#file-prompts-p15-full-campaign-and-content-production-md) | Word-detail audio/search/device checks |
| PR-010 | [P05](#file-prompts-p05-learning-and-durable-saves-md), [P17](#file-prompts-p17-beta-qualification-md) | Interrupted-write/migration/recovery |
| PR-011 | [P11](#file-prompts-p11-backend-and-cloud-sync-md), [P17](#file-prompts-p17-beta-qualification-md) | Two-device merge and deletion |
| PR-012 | [P05](#file-prompts-p05-learning-and-durable-saves-md), [P12](#file-prompts-p12-purchases-and-entitlements-md), [P17](#file-prompts-p17-beta-qualification-md) | Airplane-mode entitled campaign |
| PR-013 | [P01](#file-prompts-p01-mobile-feasibility-md), [P09](#file-prompts-p09-accessibility-and-device-polish-md), [P17](#file-prompts-p17-beta-qualification-md) | Actual accessibility/device matrix |
| PR-014 | [P07](#file-prompts-p07-hero-art-and-motion-pipeline-md), [P09](#file-prompts-p09-accessibility-and-device-polish-md), [P17](#file-prompts-p17-beta-qualification-md) | Art rubric, motion and frame capture |
| PR-015 | [P11](#file-prompts-p11-backend-and-cloud-sync-md), [P13](#file-prompts-p13-editorial-publishing-toolchain-md), [P19](#file-prompts-p19-release-rehearsal-md) | Signed bundle activation/rollback |
| PR-016 | [P12](#file-prompts-p12-purchases-and-entitlements-md), [P17](#file-prompts-p17-beta-qualification-md) | Store sandbox transaction matrix |
| PR-017 | [P10](#file-prompts-p10-slice-research-and-go-no-go-md), [P14](#file-prompts-p14-analytics-and-operational-controls-md), [P17](#file-prompts-p17-beta-qualification-md) | Metrics schema and honest cohort study |
| PR-018 | [P18](#file-prompts-p18-store-and-policy-preparation-md), [P19](#file-prompts-p19-release-rehearsal-md), [P20](#file-prompts-p20-independent-release-review-md), [P21](#file-prompts-p21-authorized-launch-and-first-month-md) | Release dossier and authorized status |
| PR-019 | [P16](#file-prompts-p16-optional-ai-lab-md) | 200-case evaluation or explicit disabled status |
| PR-020 | [P03](#file-prompts-p03-content-schemas-and-validation-md), [P13](#file-prompts-p13-editorial-publishing-toolchain-md), [P15](#file-prompts-p15-full-campaign-and-content-production-md) | Author-review-publish workflow and rights |
| NF-001 | [P01](#file-prompts-p01-mobile-feasibility-md), [P09](#file-prompts-p09-accessibility-and-device-polish-md), [P17](#file-prompts-p17-beta-qualification-md) | Sustained named-device profiler evidence |
| NF-002 | [P05](#file-prompts-p05-learning-and-durable-saves-md), [P12](#file-prompts-p12-purchases-and-entitlements-md), [P17](#file-prompts-p17-beta-qualification-md) | Save/transaction interruption tests |
| NF-003 | [P06](#file-prompts-p06-ux-and-design-system-md), [P09](#file-prompts-p09-accessibility-and-device-polish-md) | Small/large layouts and text reflow |
| NF-004 | [P02](#file-prompts-p02-project-foundation-md), [P19](#file-prompts-p19-release-rehearsal-md) | Clean-clone reproducible build |
| NF-005 | [P11](#file-prompts-p11-backend-and-cloud-sync-md), [P16](#file-prompts-p16-optional-ai-lab-md), [P20](#file-prompts-p20-independent-release-review-md) | Secret/authorization audit |
| NF-006 | [P05](#file-prompts-p05-learning-and-durable-saves-md), [P09](#file-prompts-p09-accessibility-and-device-polish-md) | Lifecycle/keyboard/audio resume |
| NF-007 | [P17](#file-prompts-p17-beta-qualification-md), [P20](#file-prompts-p20-independent-release-review-md) | Severity ledger with no blocking defects |
| NF-008 | [P13](#file-prompts-p13-editorial-publishing-toolchain-md), [P15](#file-prompts-p15-full-campaign-and-content-production-md) | Human signoff and provenance |
| NF-009 | [P05](#file-prompts-p05-learning-and-durable-saves-md), [P16](#file-prompts-p16-optional-ai-lab-md), [P17](#file-prompts-p17-beta-qualification-md) | Network/AI outage fallback |

All mandatory PR requirements except optional PR-019 must pass for the proposed launch. PR-019 may be explicitly disabled without reducing core campaign completeness. Windows and expansion features are outside v1.0 scope unless an owner decision changes that baseline.


---

<a id="file-docs-18-first-ten-working-days-md"></a>

## docs/18-First-Ten-Working-Days.md

# First ten working days

This is a practical starting sequence after implementation is authorized. It is not a promise that unresolved hardware or toolchain problems will fit ten days.

| Day | Main outcome | Evidence |
|---|---|---|
| 1 | Run P00; inventory Unreal, Blender, compiler, AI tools and devices | Environment report; exact blockers |
| 2 | Pin candidate toolchain; create isolated benchmark project | Empty C++ build and Android install |
| 3 | Import one Blender prop and simple rig; verify scale/materials | Export recipe and on-device screenshot |
| 4 | Add 12 tiles, long text, keyboard and large-text variant | Input/accessibility capture |
| 5 | Add one representative effect/audio scene and save/resume | Benchmark build and interruption check |
| 6 | Profile 20-minute phone run; identify largest costs | CPU/GPU/memory/frame-time report |
| 7 | Optimize once; resolve engine feasibility and iOS route | G1 decision record |
| 8 | Bootstrap production project and content schema | P02/P03 outputs and validator |
| 9 | Prepare 30 candidate senses with an editor; build first mode | Draft/review queue and playable encounter |
| 10 | Observe a few target users with the prototype | Findings and next weekly backlog |

Do not buy a large asset pack before confirming its style, license and mobile cost. Do not generate hundreds of polished screens before validating the common challenge screen. Do not write thousands of questions before validating the sense schema and editorial throughput.

The first expensive milestone is the polished vertical slice. Its purpose is to answer: Is this enjoyable? Does it teach useful advanced language? Can it run beautifully on the intended phones? Can we produce approved content at a sustainable rate?


---

<a id="file-prompts-00-execution-index-md"></a>

## prompts/00-Execution-Index.md

# Execution index

These are bounded work orders, not one enormous 'build the whole game' prompt. They cover implementation through release, but their gates require actual execution, human review and external platform/account access. All code remains unimplemented at package delivery.

## Operating procedure

1. Place the planning package in the intended project workspace.
2. Run P00 with this index and relevant documents attached. It inspects only.
3. When implementation is authorized, run P01 and proceed in dependency order.
4. At each task, load project status plus the named references. The assistant must inspect actual work before editing.
5. Review tangible artifacts and evidence. Technical routine work can continue autonomously; material product changes and public publication use owner decisions.
6. If a task is blocked, do not mark it passed. Continue only independent eligible tasks.
7. P16 is optional; explicitly disabling it satisfies the release dependency for that optional feature.
8. A complete sequence means all required gates passed. It does not guarantee store approval, user demand or commercial ranking.

## Task order and dependencies

| Task | Prompt | Prerequisite |
|---|---|---|
| P00 | [Environment and Evidence](#file-prompts-p00-environment-and-evidence-md) | None; planning/inspection only |
| P01 | [Mobile Feasibility](#file-prompts-p01-mobile-feasibility-md) | P00; implementation authorized |
| P02 | [Project Foundation](#file-prompts-p02-project-foundation-md) | P01 engine decision passed |
| P03 | [Content Schemas and Validation](#file-prompts-p03-content-schemas-and-validation-md) | P02 |
| P04 | [Core Challenge Modes](#file-prompts-p04-core-challenge-modes-md) | P03; approved prototype items available |
| P05 | [Learning and Durable Saves](#file-prompts-p05-learning-and-durable-saves-md) | P04 |
| P06 | [UX and Design System](#file-prompts-p06-ux-and-design-system-md) | P04 and P05 |
| P07 | [Hero Art and Motion Pipeline](#file-prompts-p07-hero-art-and-motion-pipeline-md) | P06; approved style direction |
| P08 | [Narrative and Slice Campaign](#file-prompts-p08-narrative-and-slice-campaign-md) | P05 through P07 |
| P09 | [Accessibility and Device Polish](#file-prompts-p09-accessibility-and-device-polish-md) | P08 |
| P10 | [Slice Research and Go No Go](#file-prompts-p10-slice-research-and-go-no-go-md) | P03 through P09; slice content reviewed |
| P11 | [Backend and Cloud Sync](#file-prompts-p11-backend-and-cloud-sync-md) | P05 and G3 proceed decision |
| P12 | [Purchases and Entitlements](#file-prompts-p12-purchases-and-entitlements-md) | P11; owner commercial/account inputs available |
| P13 | [Editorial Publishing Toolchain](#file-prompts-p13-editorial-publishing-toolchain-md) | P03; G3 proceed decision |
| P14 | [Analytics and Operational Controls](#file-prompts-p14-analytics-and-operational-controls-md) | P11; stable event contracts |
| P15 | [Full Campaign and Content Production](#file-prompts-p15-full-campaign-and-content-production-md) | P10 proceed; P13; established art pipeline |
| P16 | [Optional AI Lab](#file-prompts-p16-optional-ai-lab-md) | P11 and P14; optional feature only |
| P17 | [Beta Qualification](#file-prompts-p17-beta-qualification-md) | P09 and P11–P15; P16 passed or disabled |
| P18 | [Store and Policy Preparation](#file-prompts-p18-store-and-policy-preparation-md) | P17 technical candidate; owner account/legal inputs |
| P19 | [Release Rehearsal](#file-prompts-p19-release-rehearsal-md) | P18; candidate identifiers frozen |
| P20 | [Independent Release Review](#file-prompts-p20-independent-release-review-md) | P19 |
| P21 | [Authorized Launch and First Month](#file-prompts-p21-authorized-launch-and-first-month-md) | P20 GO; explicit owner publication authorization |

## Suggested assistant use

Choose GPT-6 or Fable 5.1 based on verified task performance and tool access. Use a second fresh review pass for high-risk changes; either model can fill it. Do not assume these named tools have identical commands or context capacities. If multiple workers are authorized, keep binary asset ownership exclusive and branch/worktree boundaries explicit.

## Resume message

Read PROJECT-STATUS.md, the latest evidence report, and the selected task. Inspect the current repository and baseline commit. Identify the first unmet acceptance criterion, complete it, run the relevant checks, and update evidence. Do not restart completed work or reinterpret a blocked task as complete.

## Reference companions

[Creative asset prompts](#file-prompts-creative-asset-prompts-md) · [Review and recovery prompts](#file-prompts-review-and-recovery-prompts-md) · [AI production workflow](#file-docs-10-ai-production-workflow-md)


---

<a id="file-prompts-creative-asset-prompts-md"></a>

## prompts/Creative-Asset-Prompts.md

# Creative asset and motion prompt library

Use these during authorized production after reading the art bible. Keep the chosen art direction and reference assets attached. Produce drafts, select, inspect, revise and record provenance. Generated images are visual proposals, not functioning UI or automatically production-ready 3D assets. Exact word content and UI text must be rebuilt as live text in the engine.

## C01 — World key art

Create original premium mobile-game concept art for WordQuest: The Living Lexicon, an advanced vocabulary adventure for adults. Show the Amber Archive: a warm architectural library of walnut, amber glass and aged brass, with a broken luminous-ink mechanism at the focal point. A small expressive brass-and-ink lantern companion hovers nearby. Stylized dimensional forms, meticulous material design, restrained atmospheric depth, inviting cinematic lighting, strong silhouette and rich but controlled colour. The image should feel enchanting and intelligent. Reserve a quiet central/lower region for a readable mobile challenge panel. No text, logos, watermarks, copied franchise characters, candy motifs or excessive visual clutter. Generate a portrait composition and a separate landscape environment keyframe with consistent design language. Deliver each as a concept reference with palette and focal hierarchy notes; do not claim mobile performance from a rendered image.

## C02 — Actual gameplay screen reference

Design one polished portrait vocabulary challenge screen at a 390×844 logical reference ratio, using the attached approved Amber Archive direction. Show a small progress header, a restrained dimensional archive scene, a warm ivory reading panel, four generously spaced answer controls and a bottom submit/hint area above the safe margin. Prioritize adult readability, clear hierarchy, tactile materials and thumb reach. Target word: equivocal. Example sentence: 'The witness neither confirmed the meeting nor denied attending.' The intended meaning is ambiguous or noncommittal. Treat all text as layout reference to be typeset accurately in-engine; preserve ample space rather than cramming. Supply default, selected, explanation and large-text composition references separately. Include spacing/type/colour annotations in a companion spec rather than cluttering the visual. Avoid decorative borders around every element and avoid particles over text.

## C03 — Pip turnaround and expressions

Using the approved character reference, develop Pip as an original small floating lantern made from warm aged brass and a contained ink-like light. Its personality is curious, helpful and quietly humorous; readable at phone scale. Produce consistent front/side/back/three-quarter views, scale comparison, material breakdown and eight expression/action poses: idle, inspect, anticipate, delight, thoughtful near-miss, point to clue, carry fragment and settle. Maintain identical proportions and construction across views. Limit tiny surface details that disappear on phones. Design a riggable silhouette with clear movement pivots; avoid unbuildable changing topology. Separate the concept sheet from any claim of a final rig or animation.

## C04 — Blender production asset

Inspect the pinned Blender installation and approved character/prop sheets. Create an editable, sensibly organized source scene with named collections, objects, materials, units and origins. Build a mobile-conscious mesh and simple rig matching the reference. Start with a greybox for silhouette review before detailing. Provide UVs, texture strategy, material slots, LOD proposal, animation actions and deterministic export script where supported. Verify the export in the pinned Unreal build using the established scale/axis/material recipe. Record triangle/texture counts and actual in-engine appearance. Do not add dense geometry where a baked normal or texture suffices. Deliver the .blend, source textures, exports, importer settings and capture of the real imported object; a generated picture is not the deliverable for this task.

## C05 — Motion and interaction implementation

Implement the attached interaction storyboard in the current Unreal project using its existing design tokens and event contracts. Create button compression, tile placement, correct-answer alignment, gentle near-miss return, explanation transition and landmark reveal with the timing ranges in the art bible. Prioritize anticipation, clear causality, restrained overshoot and responsive cancellation. Gameplay/persistence owns the outcome; animation observes it. Handle rapid repeated taps, pause, screen changes and reduced motion. Use the cheapest appropriate engine-native method for each effect, and profile actual CPU/GPU cost. Deliver normal-speed and slow-motion device captures, interruption cases and a concise explanation of any timing deviation. Do not substitute a web animation library for Unreal implementation.

## C06 — Niagara effect

Create a localized luminous-ink fragment trail and a short landmark-restoration burst for the approved Amber Archive scene. Use Niagara only where it adds value over a simple material/UI effect. Provide a restrained colour range, readable direction, short lifetime, bounded particle count, pooling/culling policy, low-tier variant and reduced-motion substitute. Prevent overlap with clue text and avoid large translucent full-screen layers. Verify materials and simulation behavior on the actual mobile renderer. Deliver editable system/material sources, parameter documentation, screen-coverage measurements, peak/average cost captures and cancellation behavior. Do not claim desktop-preview performance as phone performance.

## C07 — Sound identity

Compose or source original commercially usable audio for the approved world: a warm scholarly-adventure motif, quiet archive ambience, tactile tile placement, distinct but subtle correct/near-miss cues, and a brief restoration flourish. Use felt piano, delicate plucked textures, soft mechanical detail and restrained bells as direction, not a requirement to copy any existing soundtrack. Avoid harsh repetitive treble and casino-like celebration. Provide clean loop points, consistent perceived loudness, separate stems where useful, naming/bus metadata and documented rights. In-engine, duck music during pronunciation, prevent overlapping spoken words and support all mute settings. Deliver actual audio files and an implementation audition, not only prose describing sounds.

## C08 — District expansion kit

Extend the approved art system into the Verdant Conservatory and Astral Court. Preserve shared character proportions, UI material vocabulary and icon language while changing architecture, lighting, composition and story objects. Conservatory: jade glass, moss, ivory stone and warm sunlight. Court: indigo, porcelain, silver and restrained starlight. Produce modular kit plans, hero landmarks in unrestored/restored states, layer breakdown, reusable material inventory and mobile budgets. Design transitions and restoration reveals with skip/reduced-motion behavior. Review a phone-scale composite before producing every asset. Avoid merely recolouring the Archive kit or introducing a conflicting art style.

## C09 — Curriculum batch generation

Act as a vocabulary-content drafter working under a human editor. Use the approved 20–30-sense selection and source notes. For each intended sense, create an original plain-English definition, natural collocations, three distinct examples, a non-example, plausible confusables, and six challenge items covering the required skills. Reserve one new-context item for delayed transfer. Use the current schema exactly. Do not copy dictionary prose, invent etymology, label unverified CEFR levels, or claim editorial approval. Explain each distractor's flaw; flag any defensible alternative. Keep all output in DRAFT. Run structural checks, then produce a reviewer queue highlighting semantic uncertainty. Never bulk-publish the output.

## C10 — Store visuals from the real build

Use only the approved release candidate and its actual captures. Create a coherent icon proposal, screenshot sequence and short gameplay trailer showing the central interaction, visual restoration and advanced learning. Keep descriptions truthful: do not label first exposure as mastery or promise examination results. Rebuild promotional typography cleanly rather than trusting generated text. Match current target-store size/format requirements after verifying them. Include rights/provenance, editable source, exports and comparison against the running build. No fabricated reviews, award badges, user counts or chart positions.


---

<a id="file-prompts-p00-environment-and-evidence-md"></a>

## prompts/P00-Environment-and-Evidence.md

# P00 — Environment and Evidence

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** None; planning/inspection only

**Read:** 00-Executive-Direction.md; 07-Engine-and-Tools.md; 15-Decisions-and-Risks.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Inspect the actual local Windows workspace and available tools. Verify the user-reported Unreal 5.8.2 and Blender 5 installations from their real version output and installation metadata; do not silently substitute a different engine or upgrade. Record compiler, SDK/NDK/JDK compatibility, GPU/RAM/free disk, Android devices, Mac/Xcode/iPhone access, and developer-account readiness without exposing credentials. Determine what the selected GPT-6/Fable environment can actually do: filesystem, shell, builds, screenshots and editor operations. Preserve the Fable label without inventing its API.

Inventory any existing project before proposing a new one. If none exists, recommend a concrete project path and repository structure. Compare installed tools with official requirements for the pinned engine. Produce a capability matrix and a short missing-resource list. Separate facts, defaults and unresolved owner choices. This task must not start gameplay implementation, buy tools, change system installations or publish anything.

## Required deliverables and pass conditions

Create docs/ENVIRONMENT.md, docs/TOOLCHAIN-LOCK.md (provisional where necessary), docs/DECISIONS.md and PROJECT-STATUS.md. Record exact commands and version outputs, redacting secrets. List required manual checks for devices or editor access that cannot be inspected. Identify the next eligible task and whether implementation authorization exists.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P00/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p01-mobile-feasibility-md"></a>

## prompts/P01-Mobile-Feasibility.md

# P01 — Mobile Feasibility

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P00; implementation authorized

**Read:** 07-Engine-and-Tools.md; 05-UX-and-Accessibility.md; 11-QA-Performance-and-Research.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Create an isolated throwaway feasibility project using the pinned Unreal candidate. Build a representative portrait scene with one dimensional background, one simple animated character, 12 readable letter tiles including duplicates, an 18-character label, body text, native text entry, pronunciation playback, one short effect and a persisted answer. Implement large-text and reduced-motion variants. Use a small Blender source/export fixture and record transform/import settings.

Package a real Android build and run it on the nominated physical phone. Capture a 20-minute sequence, startup, memory, frame-time distribution, keyboard behavior, background/resume and accessibility feasibility. Establish the iOS compilation/signing route and run a package/device proof if resources exist. Make one focused optimization pass for the largest measured bottleneck. If the candidate still fails, produce a bounded alternative-engine comparison proposal using the same scene; do not migrate the production plan automatically.

## Required deliverables and pass conditions

Deliver benchmark project/source, actual package, export fixture, profiler logs and feasibility ADR. Pass only with real Android evidence and a credible evidenced iOS route; mark missing platform/device checks blocked. Report budgets met/missed, engine-specific accessibility limitations and final recommended configuration. G1 cannot pass on editor FPS alone.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P01/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p02-project-foundation-md"></a>

## prompts/P02-Project-Foundation.md

# P02 — Project Foundation

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P01 engine decision passed

**Read:** 08-Technical-Architecture.md; 07-Engine-and-Tools.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Initialize the production repository without overwriting unrelated work. Establish pinned engine association, C++ module boundaries, configuration separation, Git LFS rules for binary assets, generated-file ignores, ownership/locking practice and a clean-clone build recipe. Reconcile existing AGENTS.md before using the provided template.

Implement the smallest shell with Journey, challenge placeholder, settings and navigation; no fake mastery or production transactions. Create interfaces for content, session, learning, persistence, platform services and telemetry. Keep domain logic independent of widgets. Establish local automated checks and appropriate CI hosts. Provide exact setup/run commands resolved from the actual engine installation, not guessed generic commands.

## Required deliverables and pass conditions

Clean checkout builds and packages the smoke scene; source/assets are tracked appropriately; no secrets or generated caches committed. Deliver architecture map, build scripts, basic domain smoke test, dependency lock and first evidence report. Verify binary asset ownership rules and one repeatable editor import path.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P02/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p03-content-schemas-and-validation-md"></a>

## prompts/P03-Content-Schemas-and-Validation.md

# P03 — Content Schemas and Validation

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P02

**Read:** 03-Curriculum-and-Mastery.md; 09-Data-and-Content-Pipeline.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Implement versioned JSON schemas and cross-record validation for senses, challenges, missions and manifests. Use example fixtures only as drafts. Enforce stable IDs, skill/mode enums, answer references, accepted variants, tile multiset correctness, prerequisite DAG, coverage and release-only editorial/rights/audio requirements. Build a deterministic importer into engine-consumable assets without hand-editing production data in multiple places.

Create a 30-sense prototype batch with the curriculum lead. AI drafts are clearly marked; route them to human review. Keep a held-out transfer item per sense and detect obvious duplicate contexts. The tool must reject unapproved release exports while allowing draft previews. Produce actionable errors with record ID and field path.

## Required deliverables and pass conditions

Run valid and intentionally invalid fixtures including repeated letters, duplicate IDs, multiple answer ambiguity flags, dangling references and missing release approval. Demonstrate draft preview, approved export and deterministic reimport. Deliver schema, validator, importer, editorial queue, coverage report and human-review status. Do not claim all prototype content reviewed unless evidence exists.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P03/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p04-core-challenge-modes-md"></a>

## prompts/P04-Core-Challenge-Modes.md

# P04 — Core Challenge Modes

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P03; approved prototype items available

**Read:** 02-Game-Design.md; 05-UX-and-Accessibility.md; 08-Technical-Architecture.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Implement Context Detective and Word Forge first, then Precision Duel and Sentence Rescue on a shared challenge lifecycle. Use deterministic answer rules, stable option IDs and structured feedback. Forge must support repeated letters, tap placement/return, shuffle, keyboard path and explicit alternate handling. Preserve the clue when the keyboard appears. Add curated hint steps and explain why distractors fail.

Keep scoring separate from animation. Submission creates a unique attempt ID and duplicate actions cannot create multiple outcomes. No network call or runtime LLM determines correctness. Include correct, wrong, assisted, retry, paused and interrupted states. Use temporary art until the interaction is solid. Assemble three short prototype missions from the approved 30-sense batch so the initial loop can be played end to end before the full slice.

## Required deliverables and pass conditions

Demonstrate all four modes in a packaged build with approved items. Test option shuffle, repeated tiles, alternate answers, double submission, hint classification, native keyboard and back/pause. Deliver mode contracts and actual evidence. Pass only when every mode has fair completion and explanations, not only a happy-path screenshot.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P04/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p05-learning-and-durable-saves-md"></a>

## prompts/P05-Learning-and-Durable-Saves.md

# P05 — Learning and Durable Saves

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P04

**Read:** 03-Curriculum-and-Mastery.md; 08-Technical-Architecture.md; 11-QA-Performance-and-Research.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Implement per-sense/per-skill evidence and the initial deterministic scheduler. Keep encounter/recognition/recall/application/retention rules distinct. Store assistance, contexts and timestamps so hints and instant repetition cannot inflate mastery. Build a capped daily queue and introduce new senses conservatively.

Implement attempt journal, snapshots, backups, schema versions and safe session checkpoints. Persist before celebration/reward and support kill/relaunch at each transaction boundary. Handle device clock changes without repeated daily grants. Define migration and unknown-newer-save behavior. Connect mission progression and restoration grants with exactly-once IDs; knowledge evidence must remain separate from game score.

## Required deliverables and pass conditions

Test guided-correct versus unaided, recognition versus recall, distinct contexts, 7-day rule using controlled clocks, queue limits, duplicate grant prevention, corrupted snapshot fallback and interrupted writes. Demonstrate airplane-mode play and relaunch continuity on device. Deliver migration fixtures and a scheduler replay report.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P05/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p06-ux-and-design-system-md"></a>

## prompts/P06-UX-and-Design-System.md

# P06 — UX and Design System

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P04 and P05

**Read:** 05-UX-and-Accessibility.md; 06-Art-Motion-and-Sound.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Implement reusable UI components and all required screen states for the current slice: onboarding, journey, four modes, explanation, results, practice, lexicon, word detail, settings and support placeholder. Use semantic typography, spacing, colour and motion tokens. Keep meaningful text live and reflowable; never bake definitions into backgrounds. Design portrait, tablet and keyboard-safe layouts.

Create every control state: normal, selected, pressed, focused, disabled, loading, success and error. Show honest learning evidence and warm recovery copy. The first interaction should arrive quickly without forced registration or a lengthy diagnostic. Avoid per-frame text polling and unnecessary layout nesting.

## Required deliverables and pass conditions

Capture small/tall phone and tablet layouts, long words, largest text, no audio, loading/error/empty states and native keyboard. Observe five target users on core navigation with minimal guidance and fix repeated confusion. Deliver component catalogue, screenshots and usability findings; state which accessibility checks remain platform-dependent.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P06/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p07-hero-art-and-motion-pipeline-md"></a>

## prompts/P07-Hero-Art-and-Motion-Pipeline.md

# P07 — Hero Art and Motion Pipeline

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P06; approved style direction

**Read:** 06-Art-Motion-and-Sound.md; 07-Engine-and-Tools.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Produce a coherent Amber Archive hero scene and Pip prototype from original approved concepts. Use the creative prompt library for exploration, then retain one art direction. Build editable Blender sources, rigs, materials and deterministic export scripts. Import through the proven pipeline with correct scale, pivots, alpha, textures and animation clips.

Implement tactile tile/button motion, correct/near-miss feedback, one landmark restoration, ambient life and audio ducking. Use engine-native tools where sufficient. Provide low-tier and reduced-motion variants. Never add a plugin solely for visual novelty or assume generated images are rigged game assets. Record rights and performance for every selected asset.

## Required deliverables and pass conditions

Deliver source/export assets, import recipes, manifest, actual engine captures and phone footage. Verify interruption/skip behavior, no reward coupling to animation, legibility during effects, repeated-play comfort and budget impact. The hero scene must meet the art rubric and physical-device performance evidence before full-world production.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P07/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p08-narrative-and-slice-campaign-md"></a>

## prompts/P08-Narrative-and-Slice-Campaign.md

# P08 — Narrative and Slice Campaign

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P05 through P07

**Read:** 04-Narrative-and-Level-Design.md; 02-Game-Design.md; 09-Data-and-Content-Pipeline.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Expand the reviewed slice inventory to 120 senses and at least 720 items through the established editorial workflow. Implement 12 slice missions with one complete district episode and the first capstone. Create authored story-critical encounters plus approved adaptive practice slots. Do not force all 120 slice senses into 12 missions; use trails and review to provide coverage. Keep choices reconvergent and prevent permanent lockout.

Build chapter landmarks, mission prerequisites, bounded reactions, subtitles, skippable cinematics and reliable resume. Validate mission graph reachability. Write original dialogue with an adult, warm tone and a concise first session. Show mission completion separately from retained vocabulary.

## Required deliverables and pass conditions

Complete the episode from a fresh save, resume from interruptions and replay the capstone without duplicate rewards. Provide narrative/mission records, coverage report, screenshots and end-to-end device capture. Human editorial signoff is required for released slice encounters; unfinished draft content stays clearly labelled.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P08/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p09-accessibility-and-device-polish-md"></a>

## prompts/P09-Accessibility-and-Device-Polish.md

# P09 — Accessibility and Device Polish

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P08

**Read:** 05-UX-and-Accessibility.md; 11-QA-Performance-and-Research.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Perform a focused accessibility and device pass on the actual slice. Test large text/reflow, screen-reader labels and focus on the target platforms, touch targets, visible keyboard focus, tap alternatives, no-colour/no-audio completion, reduced motion, subtitles and interruption handling. Identify engine limitations with actual reproduction evidence.

Profile sustained gameplay and scene transitions. Fix measured CPU/GPU/layout/overdraw/texture costs before adding more effects. Exercise low storage, slow/absent connection, backgrounding and native keyboard variants. Preserve teaching clarity while optimizing.

## Required deliverables and pass conditions

Deliver completed accessibility matrix and performance captures by named device/build, plus remaining defects with severity and fixes. Demonstrate all core modes without timing or drag dependence. Required failures block G3; do not substitute a desktop mockup for physical-device behavior.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P09/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p10-slice-research-and-go-no-go-md"></a>

## prompts/P10-Slice-Research-and-Go-No-Go.md

# P10 — Slice Research and Go No Go

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P03 through P09; slice content reviewed

**Read:** 11-QA-Performance-and-Research.md; 12-Production-Roadmap.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Prepare and run the vertical-slice evaluation with real adult target learners. Recruit/coordinate only through owner-authorized channels. Test first-use comprehension, voluntary replay, pacing, advanced-word appropriateness and delayed unfamiliar-context recall. Separate observed sessions from unsupported assumptions and report attrition.

Evaluate editorial throughput on 120 senses/720 items, art throughput, crash/performance evidence and player response. Identify the three most consequential issues and implement focused corrections where authorized. Recommend proceed, iterate, reduce scope explicitly, or reconsider the loop. Do not declare research complete from synthetic personas.

## Required deliverables and pass conditions

Deliver anonymized study protocol/results, sample/limitations, slice quality rubric, actual content counts, revised capacity forecast and G3 decision recommendation. Full content production may proceed only after required technical/editorial gates and the owner's material product decision. Missing users or follow-up data remain explicit blockers to research claims.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P10/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p11-backend-and-cloud-sync-md"></a>

## prompts/P11-Backend-and-Cloud-Sync.md

# P11 — Backend and Cloud Sync

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P05 and G3 proceed decision

**Read:** 08-Technical-Architecture.md; 14-Release-and-Operations.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Select the smallest supported managed backend meeting cost, region and operational needs; record an ADR. Implement optional identity, guest-to-account merge, sync outbox, idempotent batch API, per-user authorization, signed content manifest/bundle delivery and account deletion. Keep local play functional without an account.

Merge attempts by ID, grant rewards once, rebuild learning projections deterministically and preserve content versions. Do not trust client entitlement claims or higher self-reported mastery. Implement retry/backoff, schema compatibility and deletion tombstones. Provide a versioned API contract and staging configuration.

## Required deliverables and pass conditions

Test cross-user denial, offline divergent devices, interrupted sync, guest merge, duplicated events, corrupted/unsigned bundle rejection, bundle rollback and stale sync after deletion. Deliver migration scripts, API spec, least-privilege config and staging evidence. No production secrets in repository/client and no public deployment claim without actual deployment.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P11/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p12-purchases-and-entitlements-md"></a>

## prompts/P12-Purchases-and-Entitlements.md

# P12 — Purchases and Entitlements

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P11; owner commercial/account inputs available

**Read:** 13-Business-and-LiveOps.md; 14-Release-and-Operations.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Implement the free first chapter and one-time full-campaign unlock using currently supported native platform purchase flows. Resolve exact APIs for the pinned engine/platform; do not invent SDK methods. Display localized store price and clear product scope. Preserve free review access and offline entitled content under a documented cache/revalidation policy.

Verify transactions on the trusted platform/server path; implement idempotent grants, pending/cancelled/error states, restore, reinstall/account scenarios and refund/revocation handling. Keep payment credentials and receipt data out of ordinary logs. Prices and commercial identity come from the owner.

## Required deliverables and pass conditions

Provide sandbox evidence on Android and iOS for purchase, cancel, pending, duplicate callback, restore, refund and offline return. Test the free/purchased content boundary and no fake client grants. Produce entitlement threat model and operations recipe. Block commerce qualification if required store access or devices are absent.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P12/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p13-editorial-publishing-toolchain-md"></a>

## prompts/P13-Editorial-Publishing-Toolchain.md

# P13 — Editorial Publishing Toolchain

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P03; G3 proceed decision

**Read:** 09-Data-and-Content-Pipeline.md; 03-Curriculum-and-Mastery.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Build the sustainable authoring/review/publishing workflow for 600 senses and at least 3,600 items. Provide draft/edit/preview/review/history/coverage/audio/rights views, ambiguity flags and deterministic export. Reuse existing simple tools if they meet the need; avoid a sprawling CMS.

Separate author, reviewer and publisher responsibilities. Prevent draft/unlicensed/invalid content entering release bundles. Preview actual phone layout, option shuffles and audio. Implement withdrawal, version changelog, compatibility checks, signing and staging promotion. Add reports for unique lemmas, senses, skill coverage and held-out transfer.

## Required deliverables and pass conditions

Demonstrate a complete batch from AI draft through human review and staging bundle, including rejected content and a correction rollback. Report measured reviewer-hours/item and bottlenecks. Export must fail on missing approval or rights and must preserve stable IDs. Deliver workflow guide and reproducible build report.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P13/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p14-analytics-and-operational-controls-md"></a>

## prompts/P14-Analytics-and-Operational-Controls.md

# P14 — Analytics and Operational Controls

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P11; stable event contracts

**Read:** 11-QA-Performance-and-Research.md; 13-Business-and-LiveOps.md; 14-Release-and-Operations.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Implement consent-aware telemetry, event deduplication, build/content/config identifiers, crash breadcrumbs and dashboards. Track activation, mature retention cohorts, delayed learning, hint use, content reports, purchase/sync failures and operating costs. Keep raw writing/audio/receipts out of analytics.

Add safe remote flags, config compatibility and optional-feature disable controls. Document exact metric denominators and date windows. Build support intake and privacy/deletion handling consistent with actual data flow. Ensure analytics outages do not block gameplay or grow local queues without bounds.

## Required deliverables and pass conditions

Validate event schemas, duplicate/offline replay, opt-out behavior, bounded queue, deletion behavior, bad config rejection and emergency disable. Demonstrate dashboards with labelled synthetic data first, then actual beta data when available. Never present synthetic retention as real performance. Deliver metrics dictionary and operations guide.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P14/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p15-full-campaign-and-content-production-md"></a>

## prompts/P15-Full-Campaign-and-Content-Production.md

# P15 — Full Campaign and Content Production

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P10 proceed; P13; established art pipeline

**Read:** 01-Product-Requirements.md; 03-Curriculum-and-Mastery.md; 04-Narrative-and-Level-Design.md; 06-Art-Motion-and-Sound.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Expand through small reviewed batches to 600 approved senses, at least 550 unique lemmas, at least 3,600 reviewed items and 60 missions across three districts. Complete all six capstones, 12 landmarks, the final story resolution, pronunciation coverage and required UI/art/audio. Reuse approved kits without making districts indistinguishable.

Use the same per-sense coverage and quality rules as the slice. Measure editor/art throughput and revise forecasts honestly. Keep draft production separate from approved bundles. Play every mission and inspect every published item in the client. Track rights, audio, localization readiness and download budgets.

## Required deliverables and pass conditions

Deliver release-candidate content bundles with count/coverage/rights/review reports, complete campaign traversal and actual device captures for each district. No placeholder ending, missing pronunciation or unreviewed AI batch may count toward completion. If resources are insufficient, report the exact remaining inventory and a concrete owner scope decision.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P15/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p16-optional-ai-lab-md"></a>

## prompts/P16-Optional-AI-Lab.md

# P16 — Optional AI Lab

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P11 and P14; optional feature only

**Read:** 10-AI-Production-Workflow.md; 08-Technical-Architecture.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Prototype a bounded writing-feedback lab behind an off-by-default flag. Use approved sense/version records, server-side credentials, strict quotas, timeout and structured feedback. Treat learner text as data and never let it instruct tools or publishing. AI judgment is advisory and cannot grant campaign mastery.

Create the 200-case human-rated evaluation set covering valid/invalid/ambiguous use, multiple senses, dialect, injection and private text. Measure helpfulness, factuality, uncertainty, latency and cost. Provide deterministic explanation fallback. Voice is a separate opt-in experiment and cannot be required for launch.

## Required deliverables and pass conditions

Deliver gateway, fallback, data-retention behavior, test cases and actual evaluation/cost report. Enable only if the stated gate passes and the owner accepts the feature/cost; otherwise record DISABLED and continue the core release sequence. This optional task must not block a complete launch without AI.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P16/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p17-beta-qualification-md"></a>

## prompts/P17-Beta-Qualification.md

# P17 — Beta Qualification

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P09 and P11–P15; P16 passed or disabled

**Read:** 11-QA-Performance-and-Research.md; 14-Release-and-Operations.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Run the full feature/content beta matrix on supported physical devices and target users. Include cold starts, 20-minute thermal runs, large text, all modes, full story, offline play, sync conflicts, interrupted updates, corrupt saves, purchases, restores, refunds and deletion. Audit teaching correctness and content reports.

Fix critical/high defects with reproduction-based regressions. Report actual cohort retention and delayed learning with sample sizes and uncertainty. Treat soft business targets as decision evidence, not numbers to manufacture. Conduct a fresh build from clean checkout and compare it with the tested candidate.

## Required deliverables and pass conditions

Deliver beta report, device matrix, defect ledger, clean-build evidence, learning/retention report and G5 recommendation. Zero unresolved critical/high shipping defects; missing platform evidence remains blocked. Document whether the current product merits release, another test cycle or a scoped product change.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P17/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p18-store-and-policy-preparation-md"></a>

## prompts/P18-Store-and-Policy-Preparation.md

# P18 — Store and Policy Preparation

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P17 technical candidate; owner account/legal inputs

**Read:** 14-Release-and-Operations.md; 13-Business-and-LiveOps.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Recheck current Apple/Google requirements for actual target accounts, regions, engine toolchain and product behavior. Prepare signed internal candidate builds, store metadata, original icon, actual gameplay screenshots/video, age/content answers, privacy/data declarations, support links and reviewer instructions. Do not assert unsupported learning or ranking outcomes.

Verify rights inventory, account deletion, purchase disclosures, permissions and SDK behavior against implemented data flows. Identify any missing commercial identity, licensing, tax/account or policy decision for the owner. Do not invent approvals or submit publicly as part of preparation.

## Required deliverables and pass conditions

Deliver platform-specific submission checklist with verified current requirements, candidate packages/hashes, metadata assets and exact owner blockers. All screenshots must reflect the tested build. Required credentials/accounts/legal decisions remain explicit rather than filled with fabricated data.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P18/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p19-release-rehearsal-md"></a>

## prompts/P19-Release-Rehearsal.md

# P19 — Release Rehearsal

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P18; candidate identifiers frozen

**Read:** 14-Release-and-Operations.md; ../templates/RELEASE-CHECKLIST.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Rehearse production operations in the appropriate nonpublic environment: compatible content rollback, optional-feature disable, failed sync recovery, purchase incident triage, backup restore, monitoring alerts and support intake. Verify clean build reproducibility and archive commit/content/config/toolchain identifiers.

Run the release checklist against concrete evidence. Distinguish content rollback, backend rollback and store binary replacement. Ensure no migration makes a rollback unsafe without a documented recovery plan. Recheck final free/purchased/offline experience.

## Required deliverables and pass conditions

Deliver rehearsal log, rollback/recovery commands appropriate to actual infrastructure, monitoring ownership, support runbook and candidate release dossier. No real user data destruction or unapproved public rollout. Every unchecked checklist item has a disposition and owner.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P19/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p20-independent-release-review-md"></a>

## prompts/P20-Independent-Release-Review.md

# P20 — Independent Release Review

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P19

**Read:** 01-Product-Requirements.md; 17-Requirements-Traceability.md; 14-Release-and-Operations.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Review the candidate as a skeptical release lead. Trace every required PR/NF ID to actual code/content and current evidence. Inspect the running build, not only prior reports. Reproduce high-risk save, entitlement, offline and learning-evidence cases. Verify content counts and review records. Check that optional AI is genuinely disabled if unqualified.

Produce a concise owner decision packet with release recommendation, known limitations, business targets versus observed results, publication scope, costs and rollback readiness. Fix routine defects and rerun affected checks; do not waive missing required evidence or silently shrink the promise.

## Required deliverables and pass conditions

Deliver signed-off technical review and explicit go/no-go recommendation with exact candidate IDs. A GO means technically ready for owner publication decision, not already approved by stores or released. Ask only for material remaining owner decisions after completing all reviewable preparation.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P20/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-p21-authorized-launch-and-first-month-md"></a>

## prompts/P21-Authorized-Launch-and-First-Month.md

# P21 — Authorized Launch and First Month

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P20 GO; explicit owner publication authorization

**Read:** 14-Release-and-Operations.md; 13-Business-and-LiveOps.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Confirm the owner's actual publication scope and target candidate, then execute the authorized submission/distribution workflow using platform-supported controls. Track review status and address rejection reasons factually. Do not bypass platform review or broaden rollout beyond the authorized scope.

Monitor crashes, purchases, saves, content failures and cost as availability expands. Perform the first-month cadence, prioritize incidents and support, and publish only reviewed compatible content updates. Keep a rollback/disable path ready. Record real acquisition and learning evidence before recommending larger marketing spend.

## Required deliverables and pass conditions

Deliver actual submission/release status, URLs only when real, build/content IDs, monitoring reports, incident/support ledger and first-month product review. If publication or account access is absent, retain the ready dossier and state the exact remaining action. Store acceptance and commercial success cannot be fabricated by completing this prompt.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P21/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.


---

<a id="file-prompts-review-and-recovery-prompts-md"></a>

## prompts/Review-and-Recovery-Prompts.md

# Review, recovery, and production support prompts

## R01 — Fresh engineering review

Inspect the actual diff, affected modules and current requirements. Find concrete correctness, data integrity, learning-evidence, entitlement, performance and accessibility defects. Prioritize by severity and give reproducible examples with file locations. Check whether tests cover behavior rather than mirror implementation. Do not invent findings to appear thorough. Fix routine confirmed defects if authorized, rerun affected checks and record residual risks. Distinguish reviewed code from unexecuted editor/device behavior.

## R02 — Visual polish review

Review the running build plus attached native-resolution captures against the approved art and motion bible. Identify the five changes with greatest impact on readability, hierarchy, material coherence, tactile response and emotional appeal. Consider normal play, large text and reduced motion. Implement a focused pass without changing game rules, then capture comparable before/after evidence and profile cost. Do not add decoration merely to make the screen busier.

## R03 — Curriculum ambiguity review

Inspect the identified sense/items independently. Verify meaning, register, natural usage, collocations, accepted variants and each distractor. State every alternative that a knowledgeable learner could reasonably defend. Propose the smallest wording change that makes the intended distinction fair. Keep changes in review state, preserve IDs/revisions correctly and record sources/rights. A model's confidence is not human editorial signoff.

## R04 — Resume after interruption or model limit

Read PROJECT-STATUS.md and the most recent task evidence, inspect git status/diff and the actual files. Summarize the last verified state and first incomplete criterion. Continue from that point; do not overwrite unfinished owner work or rebuild completed architecture. If tools/devices are unavailable, perform safe independent work and record the exact recovery steps. Update status with actual results before ending.

## R05 — Performance regression

Reproduce the slow sequence on the same named device/build configuration. Capture CPU/GPU/frame/memory evidence and compare with the accepted baseline. Identify the dominant bottleneck before editing. Fix one cause at a time, preserving appearance and learning clarity where possible. Verify over a sustained run and include low-tier/reduced-motion variants. Do not claim a win from editor FPS, disabling all effects, or a different device without disclosure.

## R06 — Save or sync incident

Preserve the affected save and logs before reproduction. Identify schema/content/build versions and transaction boundary. Reproduce using a copy, check journal/snapshot/backup integrity, duplicate IDs, migration and reconciliation. Repair without deleting legitimate progress or issuing duplicate rewards. Add a regression for the actual failure and document a safe user-recovery path. Avoid printing personal data or tokens.

## R07 — Scope and completion audit

Compare the current repository, assets, content bundle, tests and release evidence with every PR/NF ID. Report confirmed complete, partial, missing and blocked separately. Count only approved content. Detect placeholder screens, unexecuted scripts, disabled essential paths and unsupported success claims. Produce the dependency-ordered remaining work with concrete acceptance criteria; do not silently redefine v1.0.

## R08 — Editor automation failure

Inspect the actual pinned engine/Blender API and failing script/log. Work in a disposable copy. Repair the smallest reproducible editor operation; validate asset creation/import/opening and produce a real screenshot. If no supported automation route exists, provide a precise manual recipe with object names/properties and expected verification. Mark the task incomplete until executed; never fabricate a binary asset or pretend a recipe ran.

## R09 — Budget and capacity checkpoint

Use actual hours, quotes, usage and throughput from the project. Reforecast remaining engineering, editorial, art, QA and platform work. Separate incurred cost, committed cost and optional scope. Identify the bottleneck and propose realistic tradeoffs that preserve learning, offline reliability and a complete story. Ask the owner only about material spending or scope decisions, with a recommended option and consequences.

## R10 — Release rejection or blocked store task

Read the actual platform response and the exact candidate metadata/build. Map each cited issue to current official requirements. Reproduce behavior, fix what is actionable, prepare updated evidence and reviewer notes, and distinguish required changes from assumptions. Do not bypass review, fabricate compliance, or repeatedly resubmit the same unexplained build. Respect the owner's authorized publication scope.


---

<a id="file-templates-agents-template-md"></a>

## templates/AGENTS.template.md

# Proposed repository agent instructions

Copy into the game repository as AGENTS.md only when initializing that project and after reconciling any existing instructions. This is a template, not an installed skill or a change to the current workspace's authority.

Read project status, relevant requirements and the selected task before editing. Preserve advanced vocabulary, deterministic campaign scoring, offline core play and documented launch scope. Inspect existing work and baseline commit; do not overwrite user changes.

Use C++ for reviewable core logic and supported editor workflows for binary assets. Never fabricate .uasset/.umap/.blend outputs. Verify editor APIs against the pinned installation. Use one writer per binary asset; use locks/worktrees when multiple workers are explicitly authorized.

Keep tasks bounded. Run relevant tests and actual packaged-device checks when required. Report actual commands, results, artifacts and limitations. Never mark a gate passed on generated code alone. Preserve failed evidence until resolved. Do not disable meaningful tests to create a pass.

AI may draft curriculum, but only reviewed content may enter release bundles. Hints and recognition cannot masquerade as unaided recall. No service secrets in clients. Do not change the engine, business model, audience, launch promise or public release state without the appropriate owner decision.

Continue routine implementation and fixes within authorized scope. Ask only for material missing decisions or unavailable access. Update project status and evidence after each completed task. Load focused context, not all design documents indiscriminately.


---

<a id="file-templates-asset-manifest-md"></a>

## templates/ASSET-MANIFEST.md

# Asset manifest template

| ID | Purpose | Source file | Export | License/provenance | Import recipe | Budget | Reviewer/status |
|---|---|---|---|---|---|---|---|
| asset ID | Player-facing use | Editable source | Engine output | Evidence path | Scale/axis/material/LOD | Memory/triangles/effect | Named review |

For generated concepts record prompt, model/tool, reference rights and selected revision. For rigged assets record skeleton, clips and interruptible states. For UI record all interaction states, scalable text behavior and reduced-motion equivalent. For audio record usage rights, language/voice, bus and subtitle/transcript reference.


---

<a id="file-templates-decision-record-md"></a>

## templates/DECISION-RECORD.md

# ADR: decision title

ID / date / owner / status:
Question:
Verified facts:
Assumptions:
Options and tradeoffs:
Decision and rationale:
Cost / schedule / platform impact:
Affected requirements / documents / prompts:
Verification or rollback plan:
Revisit trigger:


---

<a id="file-templates-editorial-review-md"></a>

## templates/EDITORIAL-REVIEW.md

# Editorial review

Sense/item IDs and revisions:
Editor / date:
Original content and reference notes:
Rights/provenance:

- [ ] Advanced usefulness rubric passes.
- [ ] Definition and intended sense are correct.
- [ ] Examples and collocations are natural.
- [ ] Alternatives are unambiguous or explicitly accepted.
- [ ] Distractors are plausible without being defensible answers.
- [ ] Rationale explains the distinction.
- [ ] Pronunciation/audio is correct and licensed.
- [ ] No unnecessary cultural knowledge or harmful stereotype.
- [ ] Reading load and accessibility variant reviewed.
- [ ] Coverage includes context, recall, precision, usage and held-out transfer.
- [ ] Second reader completed high-ambiguity/capstone review where needed.

Decision: draft / revise / approved / withdrawn.
Open issues and changes:


---

<a id="file-templates-evidence-report-md"></a>

## templates/EVIDENCE-REPORT.md

# Milestone evidence report

Task/gate:
Date and responsible person:
Repository / branch / commit:
Engine / toolchain / build configuration:
Content / schema / config version:
Physical devices and OS:

## Outcome

Pass / fail / blocked, with concrete reason.

## Artifacts

Paths to actual code, builds, validated content, screenshots/video and logs.

## Verification

| Check | Command or manual steps | Actual result | Evidence path |
|---|---|---|---|
| Required check | Fill with real action | Pass/fail/blocked | Existing artifact |

## Defects and limitations

Severity, reproduction, impact, owner, next action. Distinguish simulated/local/editor/device/user evidence.

## Decisions

Routine decisions made; material owner decisions required; affected requirements.

## Next task

First dependency-eligible task and precise handoff.


---

<a id="file-templates-project-status-md"></a>

## templates/PROJECT-STATUS.md

# Project status

Baseline date: 2026-09-20
Current state: planning package delivered; no game implementation claimed.
Current gate: G0 pending local environment inspection.
Current task: P00.
Repository/branch/commit: not yet established for this project.

## Completed

- Production planning package and execution sequence authored.

## In progress

- None in the game repository.

## Blockers and owner inputs

- Actual local toolchain/device evidence needed.
- Budget, hours and specialist capacity not supplied.
- Mac/iPhone/store-account access not supplied.

## Next eligible action

Run P00 in the user's local workspace. It is inspection and planning only.

## Handoff

Record latest evidence report, changed files, actual tests, current content version, accepted decisions, outstanding defects and next task. Never replace missing evidence with a success label.


---

<a id="file-templates-release-checklist-md"></a>

## templates/RELEASE-CHECKLIST.md

# Release checklist

Candidate commit / content hash / engine/toolchain / platform builds:
Owner release decision and date:

- [ ] G0–G6 required evidence exists; optional AI is off if unqualified.
- [ ] 600 approved senses, at least 550 unique lemmas, 3,600 approved items and 60 missions verified.
- [ ] Complete story, free boundary and purchased content function.
- [ ] Offline, save/resume, migration and recovery pass.
- [ ] Purchases, restore, duplicate prevention and refund path pass.
- [ ] Supported devices meet declared performance and accessibility requirements.
- [ ] No unresolved critical/high shipping defect.
- [ ] Content/asset/audio/font/plugin rights recorded.
- [ ] Privacy, permissions and store disclosures match actual behavior.
- [ ] Support, account deletion and incident owner ready.
- [ ] Staging/production secrets separated; no client secrets.
- [ ] Content rollback and remote disable tested.
- [ ] Store metadata uses actual build images and accurate claims.
- [ ] Current platform requirements checked for target accounts/regions.
- [ ] Signed build hashes, logs and changelog archived.
- [ ] Explicit publication decision recorded before public release.


---

<a id="file-examples-readme-md"></a>

## examples/README.md

# Illustrative content fixtures

`draft-content.json` contains three original draft senses and four challenge examples, one per core mode. `planning-example.schema.json` validates only this planning example's structure. P03 must implement complete production schemas, semantic/cross-record checks and release gates.

These examples have not received human editorial, pronunciation or rights signoff. They intentionally set `release_ready` to false and use draft status. They do not satisfy the six-item-per-sense release inventory or provide the production curriculum. Do not import them as approved shipped content.


---

<a id="file-package-validation-md"></a>

## PACKAGE-VALIDATION.md

# Package validation report

Date: 20 September 2026. This report checks the planning deliverables, not a game implementation.

| Check | Result |
|---|---|
| Local Markdown references | PASS — 121 relative links resolved |
| Markdown fenced blocks | PASS — balanced |
| Numbered execution prompts | PASS — P00 through P21, 22 tasks |
| Task structure | PASS — task, acceptance and handoff in every numbered prompt |
| Requirement traceability | PASS — PR-001–PR-020 and NF-001–NF-009 present |
| Structured examples | PASS — JSON parsed and checked against the used structural schema keywords |
| Invalid example rejection | PASS — missing field, false release status and invalid mode fixtures rejected |
| Example IDs/references | PASS — unique IDs, valid sense/answer references |
| Forge repeated-letter counts | PASS — exact tile multiset for laconic |
| Mode examples | PASS — all four core modes represented |
| Release labelling | PASS — examples explicitly draft and not release-ready |
| Scope consistency review | Reviewed — 600 senses, minimum 550 lemmas, 3,600 items, 60 missions, 3 districts |
| Optional AI boundary | Reviewed — P16 may remain disabled; core launch remains complete |

The structural checker was purpose-built for the keywords in the illustrative schema; no claim of a general production JSON Schema validation implementation is made. Production validators are P03 work. Semantic editorial approval, device performance, learning effectiveness, store acceptance and commercial outcomes have not been tested by this package.

The ZIP is checked for integrity and its file hashes are checked against MANIFEST.json during packaging. The manifest excludes itself to avoid a recursive hash. Local reference checks do not imply every external web page will remain available.


---

<a id="file-examples-draft-content-json"></a>

## examples/draft-content.json

```json
{
  "schema_version": 1,
  "release_ready": false,
  "senses": [
    {
      "id": "sense.equivocal.adj.ambiguous.v1",
      "lemma": "equivocal",
      "part_of_speech": "adjective",
      "definition": "Open to more than one interpretation; not giving a clear or definite position.",
      "register": "neutral/formal",
      "examples": [
        "The witness gave an equivocal reply, neither confirming nor denying the meeting.",
        "The study produced equivocal results that supported no clear conclusion.",
        "Her equivocal response left the committee unsure of her position."
      ],
      "collocations": [
        "equivocal response",
        "equivocal evidence"
      ],
      "confusables": [
        "ambivalent",
        "unequivocal"
      ],
      "category": "reasoning",
      "difficulty_band": "advanced-candidate",
      "pronunciation_refs": [],
      "provenance": {
        "origin": "Original illustrative draft for this planning package",
        "reviewer": null,
        "rights_status": "pending-review"
      },
      "status": "draft",
      "revision": 1
    },
    {
      "id": "sense.laconic.adj.concise.v1",
      "lemma": "laconic",
      "part_of_speech": "adjective",
      "definition": "Using very few words.",
      "register": "formal/literary",
      "examples": [
        "His laconic reply was a single word: no.",
        "The usually talkative guide became laconic when the subject arose.",
        "Her laconic note conveyed the decision in one short sentence."
      ],
      "collocations": [
        "laconic reply",
        "laconic style"
      ],
      "confusables": [
        "reticent",
        "terse"
      ],
      "category": "expression",
      "difficulty_band": "advanced-candidate",
      "pronunciation_refs": [],
      "provenance": {
        "origin": "Original illustrative draft for this planning package",
        "reviewer": null,
        "rights_status": "pending-review"
      },
      "status": "draft",
      "revision": 1
    },
    {
      "id": "sense.corroborate.verb.support.v1",
      "lemma": "corroborate",
      "part_of_speech": "verb",
      "definition": "To support a statement or account by providing additional evidence.",
      "register": "formal",
      "examples": [
        "The receipt corroborated her account of the purchase.",
        "A second witness corroborated the description given by the driver.",
        "The records corroborate the claim that the office was closed."
      ],
      "collocations": [
        "corroborate an account",
        "corroborate a claim"
      ],
      "confusables": [
        "refute",
        "substantiate"
      ],
      "category": "reasoning",
      "difficulty_band": "advanced-candidate",
      "pronunciation_refs": [],
      "provenance": {
        "origin": "Original illustrative draft for this planning package",
        "reviewer": null,
        "rights_status": "pending-review"
      },
      "status": "draft",
      "revision": 1
    }
  ],
  "challenges": [
    {
      "id": "item.equivocal.context.001",
      "sense_ids": [
        "sense.equivocal.adj.ambiguous.v1"
      ],
      "mode": "context",
      "skill": "recognition",
      "prompt": "The witness neither confirmed the meeting nor denied attending. Her reply was equivocal. What does equivocal mean here?",
      "options": [
        {
          "id": "a",
          "text": "Ambiguous or noncommittal"
        },
        {
          "id": "b",
          "text": "Openly hostile"
        },
        {
          "id": "c",
          "text": "Extremely detailed"
        },
        {
          "id": "d",
          "text": "Expressing certainty"
        }
      ],
      "answer_rule": {
        "kind": "option_ids",
        "accepted": [
          "a"
        ]
      },
      "rationale": "The reply does not give a clear yes or no.",
      "hint_steps": [
        "Look at what the witness does not confirm or deny."
      ],
      "difficulty": "supported",
      "held_out_transfer": false,
      "status": "draft",
      "reviewer": null,
      "revision": 1
    },
    {
      "id": "item.laconic.forge.001",
      "sense_ids": [
        "sense.laconic.adj.concise.v1"
      ],
      "mode": "forge",
      "skill": "recall",
      "prompt": "Build the adjective meaning using very few words.",
      "tiles": [
        "l",
        "a",
        "c",
        "o",
        "n",
        "i",
        "c"
      ],
      "answer_rule": {
        "kind": "exact_words",
        "accepted": [
          "laconic"
        ]
      },
      "rationale": "A laconic response uses very few words.",
      "hint_steps": [
        "It begins with l."
      ],
      "difficulty": "supported",
      "held_out_transfer": false,
      "status": "draft",
      "reviewer": null,
      "revision": 1
    },
    {
      "id": "item.corroborate.precision.001",
      "sense_ids": [
        "sense.corroborate.verb.support.v1"
      ],
      "mode": "precision",
      "skill": "precision",
      "prompt": "A second independent witness gives an account consistent with the first. Which verb describes what the new account does to the first?",
      "options": [
        {
          "id": "a",
          "text": "Corroborates"
        },
        {
          "id": "b",
          "text": "Refutes"
        },
        {
          "id": "c",
          "text": "Obscures"
        }
      ],
      "answer_rule": {
        "kind": "option_ids",
        "accepted": [
          "a"
        ]
      },
      "rationale": "Consistent additional evidence supports the first account.",
      "hint_steps": [
        "Decide whether the second account supports or contradicts the first."
      ],
      "difficulty": "supported",
      "held_out_transfer": false,
      "status": "draft",
      "reviewer": null,
      "revision": 1
    },
    {
      "id": "item.corroborate.repair.001",
      "sense_ids": [
        "sense.corroborate.verb.support.v1"
      ],
      "mode": "repair",
      "skill": "usage",
      "prompt": "Both witnesses described the same events. Repair this sentence: The second account refuted the first.",
      "options": [
        {
          "id": "a",
          "text": "Replace refuted with corroborated"
        },
        {
          "id": "b",
          "text": "Replace refuted with contradicted"
        },
        {
          "id": "c",
          "text": "Keep the sentence unchanged"
        }
      ],
      "answer_rule": {
        "kind": "option_ids",
        "accepted": [
          "a"
        ]
      },
      "rationale": "The accounts agree, so the second supports rather than disproves the first.",
      "hint_steps": [
        "The opening sentence says the accounts agree."
      ],
      "difficulty": "supported",
      "held_out_transfer": false,
      "status": "draft",
      "reviewer": null,
      "revision": 1
    }
  ]
}
```


---

<a id="file-examples-planning-example-schema-json"></a>

## examples/planning-example.schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Planning example structural schema; production validation is P03",
  "type": "object",
  "required": [
    "schema_version",
    "release_ready",
    "senses",
    "challenges"
  ],
  "additionalProperties": false,
  "properties": {
    "schema_version": {
      "const": 1
    },
    "release_ready": {
      "const": false
    },
    "senses": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": [
          "id",
          "lemma",
          "part_of_speech",
          "definition",
          "examples",
          "collocations",
          "status",
          "revision",
          "provenance"
        ],
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^sense\\."
          },
          "lemma": {
            "type": "string",
            "minLength": 1
          },
          "definition": {
            "type": "string",
            "minLength": 1
          },
          "examples": {
            "type": "array",
            "minItems": 3,
            "items": {
              "type": "string"
            }
          },
          "collocations": {
            "type": "array",
            "minItems": 2,
            "items": {
              "type": "string"
            }
          },
          "status": {
            "const": "draft"
          },
          "revision": {
            "type": "integer",
            "minimum": 1
          }
        }
      }
    },
    "challenges": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": [
          "id",
          "sense_ids",
          "mode",
          "skill",
          "prompt",
          "answer_rule",
          "rationale",
          "status",
          "revision"
        ],
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^item\\."
          },
          "sense_ids": {
            "type": "array",
            "minItems": 1,
            "items": {
              "type": "string"
            }
          },
          "mode": {
            "enum": [
              "context",
              "forge",
              "precision",
              "repair"
            ]
          },
          "skill": {
            "enum": [
              "recognition",
              "recall",
              "precision",
              "usage"
            ]
          },
          "status": {
            "const": "draft"
          },
          "revision": {
            "type": "integer",
            "minimum": 1
          },
          "answer_rule": {
            "type": "object",
            "required": [
              "kind",
              "accepted"
            ],
            "properties": {
              "kind": {
                "enum": [
                  "option_ids",
                  "exact_words"
                ]
              },
              "accepted": {
                "type": "array",
                "minItems": 1,
                "items": {
                  "type": "string"
                }
              }
            }
          }
        }
      }
    }
  }
}
```
