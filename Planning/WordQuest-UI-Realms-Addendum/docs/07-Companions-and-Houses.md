# Companions, Wordmasters and future Houses

## Interpret the proposed teams

This plan treats 'teams' as in-game factions/Houses or social player teams, not AI development teams. Three distinct concepts should remain separate: companion = the guide/avatar the player chooses; House = a fictional identity/theme family; team/guild = real players cooperating or competing. The last one needs networking, fairness, moderation and ongoing operations.

## Recommended launch

Three optional companions, based on the existing spirits so the selected screen designs remain faithful. Working names and personalities below are proposals, not approved final branding.

| Companion ID | Working name | Existing visual identity | Preferred realm | Personality |
|---|---|---|---|---|
| companion_g | Aster, Keeper of Wonder | Flowing white spirit carrying a lantern | G | Curious, encouraging, expansive |
| companion_h | Luma, Keeper of Insight | Round violet lantern spirit | H | Thoughtful, observant, gently playful |
| companion_i | Quill, Keeper of Words | Gold-capped winged lantern | I | Precise, witty, fond of discoveries |

Use these as optional guides/avatars rather than mandatory complex playable heroes initially. Selection can happen after the first successful mission or from home. Allow changing later without losing progress. The associated realm is a preference, never a restriction. Themes remain selectable independently.

Companion animations share a state contract: greet, idle, think, hint, correct, gentle near-miss, celebrate, settle. Reuse a common control interface while preserving each silhouette and movement. No character-exclusive correct answers, paid knowledge boosts or competitive score advantages. Personality can vary presentation copy only after editorial review; it cannot invent definitions.

## Why not twelve at launch?

Twelve fully animated characters need concepts, turnarounds, rigs, poses, effects, audio, dialogue, accessibility, thumbnails and device QA. Twelve independent realm themes multiply art and maintenance work. The game first needs evidence that advanced vocabulary play remains enjoyable across repeated sessions. Three memorable companions support that goal while keeping the selected artwork intact.

If each of twelve characters has eight states, that is 96 state implementations/animations to author and verify before transitions, theme combinations and skins. This is a scope illustration, not a cost quote. Reusing rigs helps but does not eliminate review.

## Factor expansion into data now

Use stable companion_id, preferred_realm_id and optional house_id with migration-safe fallbacks. House and realm are many-to-one or independently mapped; do not assume twelve Houses require twelve themes. Reserve no giant unused framework or empty production roster. A registry interface and unknown-ID fallback are enough until features are justified.

Potential twelve House learning identities for future exploration: Context, Precision, Recall, Expression, Reasoning, Rhetoric, Morphology, Literature, Discovery, Insight, Clarity and Synthesis. These are creative placeholders, not twelve implemented curricula or bonuses. Better names and identities should emerge from narrative design and player testing.

## Expansion gates

Version 1.x: additional cosmetic companions or fictional Houses after retention, editorial throughput and art capacity are demonstrated. Design a small authored introduction and ensure all themes still function independently.

Later social release: cooperative weekly objectives before real-time PvP. Define contribution caps, fair metrics, anti-cheat, reporting/blocking, privacy, moderation and an operational owner. Avoid raw self-reported mastery or streak pressure as a leaderboard basis. Public chat is not implied by adding Houses.

## Character/theme edge cases

Surprise me plus explicitly chosen Aster: keep Aster, rotate background. Match companion plus Luma: use H. Fixed G plus Quill: keep G and Quill. Changing from Luma to Aster without enabling matching leaves appearance preference unchanged. Recovered mission uses pinned theme even if settings changed elsewhere; apply after the safe boundary. New unavailable companion falls back gracefully.

## Narrative relationship

Companions guide the player; the earlier story cast can still exist as NPCs. Do not replace all narrative roles with the three spirits automatically. Maintain consistent dialogue speaker IDs. Characters should celebrate thoughtfulness and progress rather than imply a learner's intelligence or worth depends on test performance.
