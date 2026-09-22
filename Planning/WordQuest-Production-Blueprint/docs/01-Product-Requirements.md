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
