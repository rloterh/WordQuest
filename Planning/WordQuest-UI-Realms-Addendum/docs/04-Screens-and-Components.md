# Screen family, reusable components and next visual work

## Shared structure, distinct skins

One semantic screen hierarchy serves all three themes. Realm data supplies materials, fonts, frames, artwork and motion profile. G/H/I should feel like the same product while maintaining the visual distinctions the owner selected. Avoid maintaining three copies of gameplay logic or duplicating every widget Blueprint.

Components: brand header, icon button, realm pill, reading panel, mode label, target-word title, clue block, answer option, hint action, primary action, result panel, word-evidence chip, navigation item, practice tile, companion portrait, modal, error banner and loading placeholder. Each has focused/pressed/selected/disabled/error/large-text/reduced-motion states.

## Proposed home-screen contract

The three new drafts share: logo and settings; Change realm; a scene with companion; Your next discovery; chapter label; Continue journey; Daily practice and My lexicon cards; Your companion; bottom Journey/Practice/Lexicon/Profile navigation. The same action IDs and focus order apply in every theme.

'8 words ready' is mock data, not eight words already mastered. Production displays the actual due queue count; no due words becomes 'Review up to date'. Continue journey becomes Start journey for a new player and Review the journey for a completed campaign. Locked campaign content uses the earlier clear purchase boundary. Realm and companion controls are appearance preferences, not purchases in this addendum.

Inspect home drafts before freezing them. G's companion portrait and scene use the same flowing spirit; H uses its round violet form; I uses its winged lantern. Cross-theme character overrides need a deliberate composition pass, not accidental recolouring or mascot replacement.

## Screen production order

| Priority | Screen | Visual concept status | Required behavior |
|---|---|---|---|
| 1 | Context Detective G/H/I | Existing original targets | Real text, choice, submit, hint and pause |
| 2 | Home/Journey G/H/I | Three new drafts included | Resume/start, due review, navigation, settings |
| 3 | Appearance/companion chooser | Spec and prompt included; not generated here | Three modes, realm previews, independent identity |
| 4 | Correct/near-miss explanation | Spec and prompt included | Specific rationale, retry/continue, no premature mastery |
| 5 | Mission result | Spec and prompt included | Outcome, evidence, restoration, replay without duplicate rewards |
| 6 | Lexicon + word detail | Spec and prompt included | Search, sense distinction, audio, examples, recall evidence |
| 7 | Forge/Precision/Repair | Adapt the shared system | Word-length and mode-specific input needs |
| 8 | Chapter map + story | After central experience is stable | Story IDs distinct from appearance |
| 9 | Settings, support, download/purchase states | Required before release | Honest state and recovery; no dark patterns |

Do not generate dozens of disconnected final screens before the first functional reconstruction proves the design. Next concept work should include chooser and feedback, then state boards, not another unrelated visual style.

## Chooser specification

Title 'Your magical realm'. Three preview cards labelled Celestial Reverie, Moonlit Wisteria, Starlight Library. A mode group: Surprise me / Keep this realm / Match my companion. A companion group separately presents the three identities; explicitly labelled matching option. A Preview action does not commit or reset the current theme. Save/Apply commits at a safe point. Reduced motion and Sparkles settings are nearby or linked to accessibility. No twelve empty locked slots at launch.

## Feedback and results

Correct outcome can brighten the selected option and show a check plus explanation. Before submit, selection is an outline/radio, not a correctness check. Near miss keeps layout stable and explains the distinction. Do not flash the entire panel red. On a miss, the companion responds thoughtfully, never mocks.

Mission result uses the game's existing completion and evidence data. A newly encountered word is 'Encountered', not 'Mastered'. Background restoration is cosmetic playback driven by an already-persisted reward, not the source of truth. Skip animation leaves the same final state.

## Typography and icon handling

Use actual editable type with verified font licenses and glyph coverage. Identify fonts by measured similarity to references rather than guessing exact generated font names. Provide English punctuation and phonetic fallback. Preserve theme-specific title/body intent, but share semantic type roles and accessibility scaling. All icons have textual/assistive labels; theme ornament cannot replace navigation labels.

## Narrative consistency

The theme presents an atmosphere, not a random story reset. Chapter and character dialogue do not change simply because Surprise me selected H. In screens where a specific location is essential, insert a contained story illustration while retaining the realm's interface. Explain this separation in art briefs to avoid nine full environment production pipelines.
