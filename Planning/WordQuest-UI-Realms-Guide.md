# WordQuest — Complete G/H/I UI Realms Guide

21 September 2026. Companion to WordQuest-UI-Realms-Addendum.zip. Images and machine-readable specifications are in the ZIP.


---

Source: README.md

# WordQuest — G/H/I UI, Realms & Motion Addendum

Prepared for Robert Loterh • 21 September 2026 • v1.1 visual-direction addendum

This package extends the original WordQuest Production Blueprint. It captures Robert's preference for the exact G/H/I concepts, theme variety on app opening, animated environments, and possible Wordmaster characters/teams. It provides original reference images, three new home-screen concepts, production requirements, and bounded execution prompts. No Unreal UI, rigged character, decomposed art asset, animation or packaged game has been implemented here.

## Immediate decisions

- Launch with **G Celestial Reverie**, **H Moonlit Wisteria**, and **I Starlight Library** as the three visual realms.
- Proposed default: **Surprise me** selects a realm at a fresh visit; keep that realm across screens for the session. Provide fixed and companion-linked modes.
- Preserve the original gameplay images as authoritative visual targets. Do not ask a coding agent to freely reinterpret them.
- Create layered art and real UI controls, then add restrained ambient motion. A flattened screenshot is not a responsive animated interface.
- Recommend three optional launch companions using the three existing spirits. Plan stable data IDs for expansion now; defer twelve fully produced Houses/characters and multiplayer teams.
- Next implementation proof: one faithful G gameplay screen with live text/controls and one moving cloud layer, running on a real phone. Then H/I and the rest of the screen family.

## Read in order

1. Decisions and blueprint integration (docs/01-Decisions-and-Integration.md)
2. Realm behavior and character settings (docs/02-Realm-Behavior.md)
3. Reference fidelity contract (docs/03-Reference-Fidelity.md)
4. Screen and component system (docs/04-Screens-and-Components.md)
5. Living environments and motion (docs/05-Motion-and-Living-Environments.md)
6. Asset preparation and Unreal handoff (docs/06-Asset-and-Unreal-Pipeline.md)
7. Companions and future Houses (docs/07-Companions-and-Houses.md)
8. QA, performance and acceptance (docs/08-QA-and-Acceptance.md)
9. Production sequence and capacity (docs/09-Production-Sequence.md)
10. Sources and limitations (docs/10-Sources-and-Limitations.md)
11. Execution prompt index (prompts/00-Execution-Index.md)

## Visual references

| Realm | Original gameplay target | New home concept |
|---|---|---|
| G — Celestial Reverie | G gameplay (references/G-Celestial-Reverie-Gameplay.png) | G home draft (references/G-Celestial-Reverie-Home-Draft.png) |
| H — Moonlit Wisteria | H gameplay (references/H-Moonlit-Wisteria-Gameplay.png) | H home draft (references/H-Moonlit-Wisteria-Home-Draft.png) |
| I — Starlight Library | I gameplay (references/I-Starlight-Library-Gameplay.png) | I home draft (references/I-Starlight-Library-Home-Draft.png) |

Original gameplay targets express the user-selected visual direction. Home screens are newly generated proposals, not owner-approved final layouts. Their example progress values are mock data. Keep the original image files unchanged; the included manifest records their actual dimensions and hashes.

## Use with the earlier package

Extract beside the original planning directory. Attach this README, document 01, the selected realm reference, and the relevant UI prompt in the coding workspace. Follow the integration map: these tasks extend P01/P06/P07/P09 and do not bypass environment checks, learning tests or platform qualification. Read the original P00 first if it has not run.

A separate combined Markdown guide accompanies the ZIP for convenient reading. The ZIP is the complete handoff because it also includes images and structured specifications.


---

Source: START-HERE.md

# Start here

The recommendation is three launch realms, three optional companions and future expansion to Houses. First prove G as a faithful live interface with gentle animation. The ZIP includes all six references; the separate combined guide is for reading.

## First coding-agent instruction

Read the original WordQuest Production Blueprint and this UI Realms Addendum. Start with prompts/UI00-Reconcile-and-Inventory.md. Preserve the original G/H/I gameplay images as visual targets. Report the actual engine/tool environment, assets and dependencies before implementation. Then execute UI01 and UI02 to produce a faithful G Context Detective screen with live text/buttons, layered cloud movement and lantern glow, plus static comparison and physical-phone evidence. Do not expand the remaining UI until this proof is credible. Continue routine reversible work without repeated confirmation, but never claim unavailable device tests or generated concepts are implemented.

## What to review first

Look at G's still comparison, then its motion recording, then read the real vocabulary question on a phone. Confirm the art's identity survives and the effects do not compete with reading. Review H and I by the same method after the shared approach is established.


---

Source: docs/01-Decisions-and-Integration.md

# Decisions and integration with the production blueprint

## Authority and status

Robert explicitly favours the final G/H/I images and asks to preserve their look in production, rotate themes on opening, add living backgrounds, and explore characters and about twelve teams. Those are the governing new directions. The detailed rules below are recommended defaults for implementation, not claims that the owner already chose every character name or future feature.

Where visual instructions conflict, use this addendum over the earlier September 20 blueprint. Earlier learning, content, commerce, security, accessibility and release requirements remain in force unless explicitly changed here. Do not use a newer illustrative home image to overwrite the approved gameplay art.

## Decision table

| ID | Decision | Status |
|---|---|---|
| UI-D01 | G/H/I are the initial visual realm set | Based on explicit user direction |
| UI-D02 | Preserve their composition/material identity in the running product | Explicit user requirement |
| UI-D03 | Add clouds, water, glow and restrained glints where appropriate | Explicit user direction; parameters proposed |
| UI-D04 | Surprise me by default, one stable theme per visit | Recommended interpretation of app-opening variety |
| UI-D05 | Fixed realm and Match my companion alternatives | Recommended control for user preference |
| UI-D06 | Three optional companions; theme can follow selection | Recommended launch scope |
| UI-D07 | Twelve future Wordmaster Houses, not twelve launch teams | Recommended scope decision; not yet a commitment |
| UI-D08 | Shared semantic components with per-theme visual skins | Engineering direction |
| UI-D09 | Reference-guided layered 2.5D production | Recommended fidelity/performance approach |

## Exact changes to previous documents and prompts

| Earlier item | New instruction |
|---|---|
| docs/00 visual anchors and mood | G/H/I purple-blue magical references now govern overall look |
| docs/06 amber/jade/ivory palette | Replace global palette with per-realm tokens; keep quality/performance principles |
| docs/06 one Pip design | Three existing concept spirits become proposed companion identities; preserve each silhouette |
| docs/04 story districts | Keep mission/story IDs and semantic content; visual realm is a separate presentation setting |
| P01 benchmark | Use a G-derived panel/background and one cloud/glow effect; test H contrast as well |
| P06 UI | Implement common components and the realm resolver; preserve theme-specific geometry/type |
| P07 Amber Archive hero art | Replace initial hero target with G Celestial Reverie; H and I follow the shared pipeline |
| P08 narrative | Use realm-independent story labels and reviewed illustrations; never randomize story progress |
| P09 QA | Add three-realm, visit rotation, companion override and motion matrix |
| P15 art expansion | Prioritize these three realm packs, not three abandoned A/B/C style kits |
| P17/P20 release | Require the new visual fidelity and motion evidence |

The original campaign remains 600 reviewed senses, at least 550 unique lemmas, 60 missions, three narrative districts and four challenge modes. Visual realm is not a fourth learning mode or extra campaign. Avoid building nine complete worlds from three themes multiplied by three districts: global backgrounds/UI are three realm packs; story-specific content uses compact authored illustrations, props and dialogue. If a cinematic needs a literal narrative location, it may show that location while retaining the selected interface skin. This exception must be legible and not look like a random theme switch.

## Practical meaning of 'the same design'

The supplied pictures determine palette relationships, composition, hero architecture, character identity, panel silhouette, ornament, typography character and finish. Developers cannot replace them with a generic purple interface or a different fantasy scene and call it matching.

A static generated image does not contain exact font files, layer masks, hidden pixels, animation rigs or responsive rules. Exact identical pixels across different devices, text lengths and moving frames cannot be promised. At a matched reference size and frozen animation state, require a documented visual comparison and close reconstruction. Functional typography and responsive changes are controlled, reviewed adjustments, not permission for arbitrary restyling.

## Decisions not made by this package

Final companion names, competitive/social rules, a twelve-character release, new paid products, a revised launch date and public release remain unresolved. Routine implementation choices inside these specifications should proceed without repeated owner approval. Present material departures with a concrete visual comparison and impact.


---

Source: docs/02-Realm-Behavior.md

# Realm selection, visits, persistence and companion behavior

## Player-facing controls

Appearance offers three mutually exclusive modes:

1. **Surprise me** — choose among G/H/I at a fresh visit, avoid immediate repeats when alternatives are available.
2. **Keep this realm** — use the selected fixed realm until changed.
3. **Match my companion** — use the preferred realm of the selected companion until changed.

Default for a new installation: Surprise me. All three launch themes are included; no subscription or currency is introduced. The first visible realm can be selected locally; no login or network is required. The opening experience still prioritizes playing, not a compulsory character-selection menu.

## Define a visit precisely

Start a new visit on an ordinary cold launch when no unfinished mission is being recovered, or when returning to the home screen after at least 30 minutes in the background. A brief background/foreground cycle retains the same visit. Navigation, settings, opening the lexicon and starting another mission do not roll another theme.

An interrupted mission is pinned to its stored theme and content version through completion, even after a crash/cold launch. After the result and return home, apply a pending new-visit selection. This prevents changing scene or contrast in the middle of a question. A system process kill is not treated as permission to lose the pinned state.

Use a persisted visit UUID and monotonic session timing where possible. Time is used only for cosmetic visit detection here; clock anomalies cannot create rewards or affect learning intervals. If elapsed time is uncertain after restart, use the cold-launch rule and preserve any unfinished mission.

## Surprise selection

Use a shuffled bag of available realm IDs. Consume once per new visit. When rebuilding the bag, avoid the previous realm as the first entry if at least two realms are available. Persist the selected realm before rendering and record a selection event once. This provides variety and reasonably balanced exposure without alternating every screen.

Only verified installed realm bundles are eligible. One available realm simply repeats; do not wait on a download. Ship at least lightweight usable versions of all three for the promised launch behavior. If a realm is unavailable, choose a valid fallback and quietly expose download/repair status in settings. Never loop on retry during app entry.

## Resolver order

1. A recovered/active mission's pinned realm wins until a safe boundary.
2. An explicit pending theme change applies at a safe boundary after its assets are ready.
3. For a fresh visit, resolve selected mode: fixed ID, selected companion preferred realm, or surprise bag.
4. Validate bundle and select a compatible installed fallback if needed.
5. Publish one complete immutable presentation snapshot to the screen.

Accessibility and quality settings modify presentation intensity/text independently. They do not silently change the selected realm ID. An optional high-contrast reading surface is a disclosed accessibility override.

## Companion selection and theme choice

The default companion on a fresh profile may match the first randomly chosen realm. After the player explicitly chooses a companion, that identity persists independently of subsequent Surprise me themes.

Selecting a companion presents an optional action: 'Use this companion’s realm'. This explicitly switches to Match my companion. If the user leaves it off, retain the current appearance mode. Changing companion does not erase learning progress, alter challenge difficulty or grant a scoring advantage.

No companion chosen in Match mode: fall back to the last valid realm or G and explain the setting when opened. Deleting a future companion definition must map to a supported fallback without breaking saves. Existing snapshots show each theme's associated spirit; a pinned companion in another realm is an intentional supported variation.

## Safe switching

Home: preload required resources, then apply a restrained 350–500 ms transition with no bright flash; immediate swap or short opacity fade for reduced motion. Preserve navigation focus. Inside a challenge: queue the requested change for result/home, or offer to apply after the current question at a persisted safe point. Never reset an attempt or alter answer layout during a tap.

Do not keep every full-resolution realm resident just to switch instantly. Use a neutral coherent transition surface or last realm while preparing the target. An asset failure leaves the current working theme intact.

## Stored state contract

schema_version; appearance_mode; fixed_realm_id; selected_companion_id; companion_user_selected; current_visit_id; current_realm_id; last_realm_id; remaining_shuffle_bag; backgrounded_at; pinned_mission_realm_id; pending_realm_id; motion_preference; sparkle_preference; quality_tier; realm_bundle_versions. Store user preference separately from current resolved presentation. Sync preferences as ordinary explicit changes; random bag order can remain device-local.

## Essential tests

Fixed mode stays fixed across ten opens. Surprise uses all eligible themes without immediate repeats at bag boundaries. Brief resume retains theme. Recovery pins a mission. Invalid fixed/companion IDs fall back safely. Changing character without matching preserves theme mode. Missing assets never block practice. No theme action changes attempts, mastery, purchases or reward grants. Double resolver calls for one visit return the same theme.


---

Source: docs/03-Reference-Fidelity.md

# Visual reference fidelity contract

## Reference authority

The original G/H/I gameplay PNGs are immutable visual targets. Their exact filenames, pixel dimensions and SHA-256 hashes are in `specs/reference-manifest.json`. Do not overwrite them, crop them into new references silently, or replace them with fresh unconstrained image generations. Working exports are separate assets with revision IDs.

The home drafts extend the same identity but are not automatically approved pixel specifications. The common interaction layout is shared while surface geometry, type character and decoration can vary by realm. Original G uses a cleaner sans reading style; H and I use more serif character. Do not homogenize those away without showing the difference to the owner.

## What must remain recognizable

| Realm | Locked visual anchors |
|---|---|
| G | Lavender cloud ocean; floating palace and waterfalls; crescent; warm-white/lilac curved panel; navy reading text; pearl/lavender controls; thin pale gold; flowing white lantern-carrying spirit |
| H | Wisteria arch framing; bridge and glowing stream; moonlit castle; cyan flowers; deep blue-violet panel; ivory text; cool illuminated borders; round violet spirit |
| I | Celestial bookshelves; floating books and crystals; staircase; full moon; ivory-lavender panel; plum serif character; sculpted gold/star trims; lilac tiles; capped winged lantern spirit |

Keep the WordQuest mark's silhouette and placement as a reconstruction target; rebuild a clean brand asset after checking name/font rights. Generated lettering can be imperfect at small size. Do not use a low-resolution logo cutout as a substitute for final typography.

## Static-match pass before motion

1. Capture the target image at its actual dimensions and preserve it.
2. Record normalized anchors for title, progress, hero scene, panel, target word, clue, options, hint and submit using the actual source pixels. Do not assume identical geometry across G/H/I.
3. Reconstruct the reference state with the exact example text, no animation, matched camera, fixed texture import/colour settings and pinned fonts.
4. Compare side by side and using a half-opacity overlay in an image/editor tool. Review layout and material regions separately from text and dynamic masks.
5. Fix composition, scale and material mismatches before adding effects.
6. Capture at realistic phone display size and inspect touch/readability. Record any approved adaptation.

Suggested initial tolerances: key anchor centres within about 1% of viewport dimensions at the matched size, control bounds within about 2%, no unwanted wrapping/truncation, and no material/palette mismatch visible at ordinary phone size. These are project acceptance targets to refine from measured feasibility, not claims of already achieved matching. A global pixel similarity score is insufficient: a flattened screenshot can score perfectly and still be nonfunctional.

## Responsive adaptation

Use a normalized composition with semantic layout regions, not one stretched bitmap. Maintain art focal points with controlled crop and overscan; never stretch a moon or companion. Artwork can extend off-screen while reading surfaces and controls stay within safe areas. Large text can expand/scroll the content region and reduce decorative scene height. Preserve identity, not unreadable fixed line breaks at every font size.

For the reference-size comparison, use reference-like type metrics; for accessible sizes, document the adaptation. A functional accessibility override is not counted as an unexplained visual regression.

## Prohibited shortcuts

No entire screenshot as the clickable UI. No baked definitions or answers. No random substitute castle or mascot. No unrelated asset-pack buttons. No clipping the original companion while animating a second duplicate above it. No adding aggressive bloom to compensate for weak materials. No AI-generated animation of the entire screen that warps letters or hit targets.

## Reference versus production artefacts

Source PNG: visual reference. Decomposed/background-cleaned layers: working art requiring inspection. Engine textures/materials: production candidates after import/device QA. Widget implementation: live text/input/accessibility. Character rig/sprite animation: movement assets. Packaged capture: evidence. Each has a separate ID and status.

## Review states

Concept → reconstruction in progress → static fidelity accepted → motion accepted → device accepted → release qualified. Keep an exception log containing reference, capture, reason, decision and owner when departing materially from the appearance. These gates should reuse existing project reviews, not create a permission request for every routine pixel adjustment.


---

Source: docs/04-Screens-and-Components.md

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


---

Source: docs/05-Motion-and-Living-Environments.md

# Living backgrounds, magical effects and motion contracts

## Motion goal

Make the world breathe while the learner can comfortably read. Animation reveals depth and personality: cloud drift, slow water shimmer, soft lantern breathing, rare gem glints and a lightly floating companion. The original composition must remain recognizable at every phase. The effects are planned here; the PNGs in this package are static.

## Motion profiles

Full: approved low-amplitude loops plus event effects. Subtle: slower/less movement and fewer particles. Reduced motion: static environmental composition and immediate or short-opacity UI state changes; preserve information. Battery saver: static or minimal ambient layers, reduced rendering workload, no quality change to text. Player settings and OS accessibility signals take precedence over decorative motion defaults where supported.

## Initial effect specifications

All values are tuneable proposals to test on phones. Logical-unit amplitudes refer to a 390-wide reference viewport, not raw source pixels.

| Element | Suggested implementation | Starting motion | Constraint |
|---|---|---|---|
| G cloud layers | Two masked planes with gentle material drift | 45–90 s cycle; 4–12 units excursion | Seamless overscan, no movement of castle silhouette |
| G distant haze | Low-opacity masked material | 30–60 s variation | No contrast loss behind text |
| H water/reflections | Local UV/distortion mask | Slow continuous flow; 1–3 units apparent shimmer | Bridge/shore stay rigid |
| H wisteria | Sparse isolated branch cards or mesh | 8–14 s cycle; 0.5–1.5 degree sway | No full-frame rubber warping |
| H lanterns | Local emissive modulation | 5–9 s smooth pulse; roughly 8–12% intensity variation | No abrupt blinking or global brightness pulse |
| I crystals/gems | Local reflection sweep or brief glint | 0.8–1.4 s glint, 8–16 s idle between | Staggered; never simultaneous strobe |
| I floating book | Isolated sprite/mesh | 6–10 s bob; 3–6 units; small tilt | No letter/text warping |
| Star field | Tiny low-opacity accents | Slow individual fade, mostly static | No giant exploding stars during reading |
| Companion idle | Rig/sprite animation | 4–7 s bob; 2–4 units, occasional blink | Outside reading/hit-target region |
| CTA finish | Very subtle material sheen | Infrequent at idle, suspended while reading | Never disguise disabled/selected state |
| Correct answer | Local accent and optional tiny trail | 300–450 ms | One clear outcome cue |
| Landmark completion | Authored reveal | 2–4 s, skippable | Persist first; stop/skip yields same final scene |

## Composition masks

Every screen defines reading_area, interaction_area, scene_area and ornamental_edge_area masks. Ambient particles and high-contrast glints are excluded from reading and interaction regions. Backgrounds should remain sufficiently opaque under text so movement does not affect contrast. During a clue or explanation, damp secondary effects and remove attention-seeking companion behavior.

Define separate idle/event effect budgets: at most one salient ambient glint at a time initially, plus one short gameplay feedback effect. The numbers are project tuning limits, not universal hardware guarantees. Particle pools have maximum size, finite lifetimes, culling and explicit cleanup on screen changes.

## Sparkle instead of strobe

Interpret the requested shining/flashing as gentle glints and smooth luminance changes. Do not add rapid, high-contrast or full-screen flashing. The W3C flash guidance is a useful safety reference, but simply staying below a nominal frequency does not replace reviewing area, contrast, colour and combined effects. [W3C flash guidance](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html)

Offer Sparkles on/off independently of general motion. Review actual recordings including multiple effects together. Reduced motion should be beautiful, not a deliberately inferior empty screen.

## Timeline and state

Use a central motion policy resolved from settings, foreground state and quality tier. Inactive widgets/effects stop ticking. Backgrounding pauses audio and nonessential animation; resume starts from a stable phase rather than replaying all celebrations. Scrub or freeze ambient time for screenshot comparison. Effect seeds are deterministic in tests and varied normally for natural motion.

On theme swap, cancel old effects, preserve screen state, activate the new complete skin and restart a gentle ambient loop. Never animate a halfway-loaded scene. Motion completion cannot trigger learning-state writes or entitlement changes.

## Audio pairing

A very quiet airy bed for G, water/garden ambience for H, and soft crystalline/book ambience for I can share one melodic identity. Avoid different songs competing during navigation. Crossfade at safe transitions, duck under pronunciation and respect independent music/effects/voice settings. Ambient audio is optional and does not communicate required answers.

## Fidelity during animation

Show frozen t=0 versus the original target, then review representative t=5/15/30 frames and a 60-second loop. Detect exposed edges, duplicated clouds/characters, seams, shimmer aliasing, unnatural looping and drift away from the reference. Optical-flow animation of the entire flattened screen is disallowed because it can deform readable text and UI.


---

Source: docs/06-Asset-and-Unreal-Pipeline.md

# Asset decomposition and Unreal implementation handoff

## Prefer a hybrid 2.5D reconstruction

The strongest starting route for preserving these exact paintings is layered 2D art with real UI and selective 3D/sprite characters/props. Rebuilding every castle in full 3D would add cost and can move the look further from the reference. Use Blender where actual depth/rigging benefits the scene; keep the source art's lighting and composition as authority.

## Layer extraction inventory per realm

Background sky/moon; distant architecture; midground architecture/waterfalls; foreground foliage/columns; cloud/haze layers; water/reflection mask; companion cutout and clean plate; isolated books/crystals/lanterns; ornamental frame pieces; blank panel surfaces; control normal/pressed/selected variants; logo/icon source; glow/emission masks. Not every realm needs every layer. Record which pixels are painted reconstruction because they were hidden by the original UI.

Use image editing with the original as reference to create clean plates and isolated parts, then manually inspect. Inpainting can change architecture or character identity: compare visible retained regions, do not assume fidelity. Keep reference, masks, reconstructed source and export separately. Never animate a cutout over its original baked copy. These editable layers are future work; the supplied originals and home concepts remain flattened PNGs.

## Source preparation

Use a layered art file format supported by the chosen art tool; define canvas, colour profile, alpha convention and export naming. Store clean foreground masks without halos. Extend cloud/edge artwork beyond the viewport for drift. Give panel/control frames nine-slice or component geometry so corners do not stretch. Keep all educational text out of textures. Maintain source resolution adequate for target pixel density, but do not indiscriminately ship maximum-size layers.

A 2048×4096 uncompressed RGBA layer is roughly 32 MiB before mips; a stack of such layers can consume substantial memory. Actual GPU compression, mips, streaming and render targets determine measured cost. Budget layers deliberately and inspect package size, not merely PNG compression size.

## Runtime structure

ThemeDefinition supplies realm ID, palette/type roles, frame materials, scene bundle, effect profile, preferred companion mapping, fallback ID and compatibility version. ThemeResolver selects the active definition; it knows nothing about answer correctness. ThemePresenter applies an immutable presentation snapshot to common screens. MotionDirector applies motion/quality policy. CompanionPresenter renders selected companion independently. AssetProvider loads validated installed bundles.

In Unreal, use supported data assets/configuration and event-driven UMG changes. Prefer shared widgets with skinnable materials/brushes over cloned screens. Confirm APIs in the actual pinned engine before coding. Localized world effects may use Niagara; modest UI glow may be cheaper as a material animation. Built-in Unreal VFX and UI guidance support these tool categories, but exact performance must be measured. [UMG guidance](https://dev.epicgames.com/documentation/en-us/unreal-engine/optimization-guidelines-for-umg-in-unreal-engine) · [Niagara](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine)

## Rendering boundaries

Choose either a screen-space layered scene or camera-fixed world planes based on the P01 benchmark. Keep scene and UI z-order explicit. Use no per-frame logic for static labels. Avoid full-screen translucent blur stacks and oversized render targets. Hard-code neither GPU assumptions nor experimental renderer features into the required launch path. Bake complex atmosphere if it preserves the look more efficiently.

## Asset naming and versioning

Examples: Realm_G_Backdrop_v001, Realm_H_WaterMask_v001, Realm_I_CrystalGlint_v001, UI_ReadingPanel_G, UI_AnswerOption, Companion_G_Idle. All exports carry source ID, exporter settings, rights/provenance, import settings and review status. Binary assets have a single writer and version history. Original reference names/hashes remain stable.

## Runtime loading

Ship a complete low-cost base for G/H/I. Optional high-resolution content cannot make the first home screen blank offline. Load the active realm only, preload a requested next realm at a safe point, and release old scene resources after transition. Measure peak memory during swaps, not just steady state. Failed loading retains a valid realm and records a recoverable diagnostic.

## Agent capability boundary

A coding agent can create code, validators and supported editor scripts. It must run those scripts in the installed engine and inspect the resulting assets to claim completion. Writing Python does not mean a UMG widget or Niagara system exists. When editor execution is unavailable, supply exact manual steps and mark the implementation incomplete. Do not fabricate .uasset/.blend binaries.


---

Source: docs/07-Companions-and-Houses.md

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


---

Source: docs/08-QA-and-Acceptance.md

# 08 — QA and acceptance

## Evidence required

A screenshot proves composition; a recording proves motion; a packaged build on a named physical device proves runtime behavior. Collect all three. Record build commit, operating system, device, resolution, UI scale, quality tier, theme, companion, motion setting and deterministic capture time. Never describe generated concepts as implemented screens.

| ID | Requirement | Acceptance evidence |
|---|---|---|
| V01 | Original G/H/I identities preserved | Reference-sized frozen captures and overlays; art lead checks composition, panel, type, lighting, companion and contrast |
| V02 | Live responsive UI | Long real sentences, dynamic text scaling and safe-area captures; all text selectable by assistive navigation where supported |
| V03 | Realm modes | Cold launch, short resume, long resume, mission recovery, fixed mode and companion mode test matrix |
| V04 | Stable session | Screen navigation and duplicate foreground events never reroll the active realm |
| V05 | Fair surprise rotation | Each available realm used once per persisted shuffle bag; no boundary repeat where alternatives exist; corrupt state recovers |
| V06 | Living backgrounds | 60-second recordings for each realm, with visible subtle motion and no seam, ghost companion or effects over reading masks |
| V07 | User controls | Reduced motion, battery saver and sparkles-off persist and take effect without restart |
| V08 | Independent companion | Each of three companions works in each realm; explicit link option determines realm only when chosen |
| V09 | Educational integrity | Changing theme, companion or motion never changes an answer, score, review schedule, purchase or saved mission |
| V10 | Reliable packaging | All three base realms function offline in packaged Android and iOS builds; missing assets recover without blank controls |
| V11 | Input and accessibility | Large targets, readable contrast, focus order, non-color feedback, platform back navigation and screen-reader proof on supported platforms |
| V12 | Performance | Named-device frame-time, memory, loading and thermal measurements; quality degradation preserves text and input |

## Performance qualification

Use the baseline blueprint's device/support requirements. Before final asset production, name actual minimum and representative phones and record their OS versions. Proposed initial targets, subject to this benchmark: stable 60 fps on representative devices, stable 30 fps on minimum devices using the battery/low tier. That means nominal frame budgets of 16.7 ms and 33.3 ms, not permission to ignore long frames. Record median, 95th and 99th percentile frame times and count frames above twice the target budget during five minutes of navigation/practice and a 20-minute sustained session. Test a realm swap's peak memory as well as steady state.

Measure cold launch to usable home and input response in release-like builds. Establish loading and memory budgets from the P01 feasibility benchmark; do not invent a universal memory ceiling. Save results in a device table, including ambient conditions, thermal state and whether plugged in. Reduce particles, parallax and texture cost before reducing text quality. Do not repeatedly reload full environments while answering questions.

## Accessibility acceptance

Use at least 44 pt / 48 dp platform-appropriate touch targets and verify actual physical UI scale. Target WCAG-style contrast of 4.5:1 for normal text and 3:1 for large text and essential control boundaries; measure final composites over their brightest and darkest motion states. These are engineering targets, not an automatic certification claim. Test text enlargement to 200% with reflow, scrolling and no clipped answer or action. Adopt the OS reduced-motion preference at first run, while allowing an explicit in-app override. Never rely solely on glow, color, sound or motion to convey correctness.

Avoid high-contrast repeated flashing by design. A frequency-only check does not establish safety: area, luminance and saturated red matter too. Test combined effects, transitions and rewards, including overlapping events. The reduced-motion mode removes parallax, bobbing, drifting, shimmer and decorative particles while retaining static depth and all learning feedback.

## Stateful cases

- App terminated during a question: restore its realm, answer state and content without rerolling or granting extra rewards.
- Explicit realm selection during a mission: queue until a safe home boundary, explain briefly and allow cancellation.
- Companion changed while linked: apply its preferred realm at the next safe boundary; fixed mode stays fixed.
- Corrupt settings, removed theme or interrupted asset load: use a verified fallback; keep learning data intact.
- Foreground event received twice: one visit resolution, one asset transition.
- Background for 29 minutes versus 31 minutes: no fresh visit versus fresh visit, except pinned mission recovery. Use elapsed-time handling resilient to wall-clock changes.
- Several changes made during loading: newest requested selection wins; cancel obsolete loads without dangling callbacks.
- Modal or screen exits while an animation runs: no input lock, retained hidden emitter or late UI callback.

## Release stop conditions

Stop release for unreadable content, inaccessible required controls, crashes, lost learning progress, incorrect scoring, duplicated rewards, uncontrolled flashes, missing offline themes or material departure from accepted references. A failed visual check creates a specific defect with side-by-side evidence, not a request to regenerate every screen. Fix and retest the affected path.

Owner review is reserved for accepting new compositions or material visual departures. Routine implementation, corrections and verification proceed within the selected direction. Maintain a brief decision log: requirement, evidence, owner if needed, disposition and remaining risk.


---

Source: docs/09-Production-Sequence.md

# 09 — Production sequence and capacity

## Recommended next action

Build one faithful, layered **G Context Detective** screen with live text and controls, then animate a cloud and lantern and run it on a phone. It tests the largest uncertainty: whether the selected image can retain its charm, readability and responsiveness in the real engine. More concept screens cannot answer that question.

The three home concepts included here are useful exploration. They do not authorize replacing the accepted gameplay panels with a common generic card. H retains its dark panel; G and I retain their different light panels and ornament.

| Stage | Work | Exit evidence | Baseline connection |
|---|---|---|---|
| 0 | Inventory originals, installed engine/tool versions, fonts and platform environment | Reconciled scope, hashes, actual environment report | P00 and P01 |
| 1 | Static G composition using extracted layers and live controls | Reference-sized comparison, responsive test and asset provenance | P01 feasibility, P06/P07 prototype |
| 2 | Small G motion proof | Phone recording, motion-off capture and first performance measurements | P01/P09 |
| 3 | Shared UI foundation and faithful H/I styling | All three context screens, separate styling assets, no learning fork | P02–P06 dependencies, P07 |
| 4 | Realm resolver, settings and companion selection | Persisted settings, session/mode/recovery tests | P05/P06 |
| 5 | Home, chooser, feedback, results and lexicon | Coherent screen journey in all three themes with real data | P06/P08 |
| 6 | Other learning modes and operational screens | Full functional UI coverage and empty/error/loading states | P04/P06/P15 |
| 7 | Device, accessibility and content qualification | Physical-device matrix, visual review, regression and offline evidence | P09/P10/P17 |
| 8 | Full product release gates | Original blueprint gates plus this addendum's UI criteria | P18–P21 |

Stages 1–2 may be isolated feasibility prototypes; do not prematurely wire purchases, online tutoring or production saves into them. Once the approach is proven, integrate against the actual schema and navigation architecture. Implementations must account for real variable-length vocabulary examples, not only the short EQUIVOCAL reference.

## Staffing by responsibility

If “teams” means development teams, twelve is excessive before a vertical slice proves the product. Start with clear responsibilities that a small team can combine: product/learning lead, UI and technical artist, Unreal engineer, vocabulary editor, and QA/device verification. Bring in character animation or audio specialists for bounded deliverables. One integration owner controls shared components, schemas and build health.

If “teams” means fictional player Houses, use the strategy in document 07: three companions first, scalable identifiers now, twelve Houses after evidence of demand. If it means real multiplayer teams, treat that as a separately estimated social product.

## Estimate from demonstrated throughput

Do not promise a release date from prompt count. After G, record time spent on clean plates, type matching, widgets, animation, device fixes and review. Estimate H/I using those observed costs and explicitly allow for their distinct artwork. Track each asset as reference-only, prepared, integrated, reviewed or release-ready. Estimate remaining screen families by unique interaction work plus each theme's styling overhead, not by screenshot count alone.

Use a small work board with owner, dependency, definition of done, evidence link and blocker. Parallel asset preparation is possible after dimensions and layer contracts stabilize; shared component edits require coordination. This plan does not provision or instruct autonomous agent teams.

## Scope boundaries

Launch scope contains three visual realms, three optional companions, ambient animation, all required functional screens and accessibility settings. It does not require twelve rigs, twelve full environment packs, seasonal live operations, chat, guilds, ranked multiplayer, a cinematic 3D overworld or procedural AI-generated live interfaces. Add those only with separate evidence and resourcing.

The original serious-vocabulary curriculum remains the core. A visual milestone fails if players struggle to read, answer, remember or return for practice, even if a still image is attractive. At the slice research gate, ask learners about recall, meaning discrimination, clarity and willingness to continue, alongside perceived beauty and distraction.


---

Source: docs/10-Sources-and-Limitations.md

# 10 — Sources, assumptions and limitations

## Primary implementation references

- [Epic: Optimization Guidelines for UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/optimization-guidelines-for-umg-in-unreal-engine): supports event-driven UI updates, careful invalidation and animation choices. Consult documentation matching the installed engine before implementation.
- [Epic: Creating Visual Effects in Niagara](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine): Niagara is an available Unreal VFX workflow; its existence does not make every effect appropriate for mobile UI.
- [W3C: Understanding Three Flashes or Below Threshold](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html): flashing assessment involves more than frequency. Prefer eliminating problematic flashing rather than approaching a threshold.
- [W3C: Understanding Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) and [Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html): accessibility targets to inform native UI validation; no certification is asserted.

## What is proposed versus established

The user selected G/H/I's visual direction and requested theme changes, lively environments and planning for characters/teams. The 30-minute fresh-visit threshold, default Surprise mode, shuffle-bag policy, companion names, exact motion timings, preliminary performance targets and staged scope are product recommendations made in this addendum. They are explicit defaults for prototyping, subject to measured results and product decisions.

The generated references are raster concepts, not source-layer files. Exact fonts, clean plates, rigs, masks, nine-slice borders, native widgets, sound and animations do not yet exist in this handoff. Image editing can help reconstruct layers but must be checked for changed architecture, ornament, lighting and character identity. Some manual retouching or drawing may be necessary. Font licensing and asset rights require a production inventory.

The user reports Unreal Engine 5.8.2 and Blender 5 installed. This package has not inspected that machine or verified platform SDKs, engine plugins, build tools, Apple signing or target hardware. P00 must report what is actually installed; do not silently substitute a different version. No new paid plugin is a prerequisite for the proposed visual proof.

The three new home concepts are drafts. The original gameplay images remain the visual anchors. A faithful implementation is an acceptance goal, not a guarantee of identical pixels on every screen: different aspect ratios, safe areas, text sizes and animation times require controlled adaptation.

Executing every prompt does not automatically make a game shippable. Actual builds, reviewed vocabulary, real device evidence, licensing, store requirements and all original blueprint release gates still apply. This addendum replaces the old visual direction where stated; it does not replace the original complete production plan.


---

Source: prompts/00-Execution-Index.md

# Execution prompts

Use these with the original P00–P21 prompts, not as a separate shortcut to shipping. Start with UI00. Follow the dependency in each prompt. The first visible milestone is UI01 + UI02, a faithful moving G screen on a phone. Resolve that before multiplying assets.

Attach actual referenced PNGs as image inputs when the agent supports them. A filename alone does not ensure the agent has seen the art. Keep source images immutable. Supply this package and the original blueprint in the workspace; require the agent to inspect existing work before editing.

- UI00 — Reconcile and Inventory (UI00-Reconcile-and-Inventory.md)
- UI01 — Faithful Static G (UI01-Faithful-Static-G.md)
- UI02 — G Living Environment Proof (UI02-G-Living-Environment-Proof.md)
- UI03 — H I and Theme Components (UI03-H-I-and-Theme-Components.md)
- UI04 — Realm Resolver and Settings (UI04-Realm-Resolver-and-Settings.md)
- UI05 — Three Optional Companions (UI05-Three-Optional-Companions.md)
- UI06 — Complete Screen Family (UI06-Complete-Screen-Family.md)
- UI07 — Device Fidelity and Accessibility (UI07-Device-Fidelity-and-Accessibility.md)
- UI08 — Integrate and Release Review (UI08-Integrate-and-Release-Review.md)

Run one bounded milestone at a time and inspect its evidence. Routine fixes stay in scope. Escalate only material departures, conflicting requirements or unavailable required access. No prompt authorizes inventing test outcomes, credentials, asset licenses or release readiness.


---

Source: prompts/UI00-Reconcile-and-Inventory.md

# UI00 — Reconcile and Inventory

Dependency: Before art implementation; run original P00 if needed.

Read: docs/01, 03, 06, 09; specs/reference-manifest.json.

## Paste into your coding agent

You are implementing WordQuest against the original Production Blueprint and the G/H/I UI Realms Addendum. Read README and docs/01 first, then this task's relevant documents and actual image references. Preserve the original gameplay composition and realm-specific styling. Home images are proposals. Do not reinterpret the art direction, bake learning text into art, implement a flattened screenshot as the UI, or claim a generated concept is a tested engine screen. Keep learning logic independent of theme and companion. Respect existing repository instructions and user changes. Do not introduce purchases, remote AI calls, extra plugins or multiplayer merely to complete this task. Use available tools and report unavailable editor/device access honestly.

Proceed autonomously with reversible implementation and verification in the authorized scope. Ask only for a material unresolved product decision or unavailable required access; complete the reviewable work first. Record exact files changed, execution commands, evidence, remaining limitations and next dependency. Do not claim unrun tests passed. Preserve the original P00–P21 release gates.

## Task

Inventory the six supplied images and verify hashes. Identify G/H/I gameplay as authoritative visual targets and home screens as drafts. Inspect the project, actual engine version, platform toolchains, prior work, current navigation and learning interfaces. Produce a concise precedence map for superseded palette decisions, an asset/layer inventory, a font identification and licensing task list, and a dependency-aware work board. Inventory exact target phones or record the missing hardware as a blocker for physical-device claims. Do not start a wholesale UI rewrite. Acceptance: no conflicting palette mandates, no invented existing assets, and a concrete bounded G screen task with evidence requirements.


---

Source: prompts/UI01-Faithful-Static-G.md

# UI01 — Faithful Static G

Dependency: UI00; original P01 feasibility can use an isolated prototype.

Read: docs/03, 04, 06; references/G-Celestial-Reverie-Gameplay.png.

## Paste into your coding agent

You are implementing WordQuest against the original Production Blueprint and the G/H/I UI Realms Addendum. Read README and docs/01 first, then this task's relevant documents and actual image references. Preserve the original gameplay composition and realm-specific styling. Home images are proposals. Do not reinterpret the art direction, bake learning text into art, implement a flattened screenshot as the UI, or claim a generated concept is a tested engine screen. Keep learning logic independent of theme and companion. Respect existing repository instructions and user changes. Do not introduce purchases, remote AI calls, extra plugins or multiplayer merely to complete this task. Use available tools and report unavailable editor/device access honestly.

Proceed autonomously with reversible implementation and verification in the authorized scope. Ask only for a material unresolved product decision or unavailable required access; complete the reviewable work first. Record exact files changed, execution commands, evidence, remaining limitations and next dependency. Do not claim unrun tests passed. Preserve the original P00–P21 release gates.

## Task

Create a native G Context Detective prototype. Separate clean background, foreground, spirit and ornamental surfaces; remove baked text from reconstructed panels. Match the reference's lighting, composition, panel shape, typography hierarchy, control positions and spirit. Build actual text, answer buttons, hint and check controls using a reviewed fixture with the original EQUIVOCAL wording. Preserve semantics; no answer selection is shown in the target. Supply selected, disabled and focus states separately. Test variable text and safe areas. Capture a frozen native render at the reference dimensions and an overlay comparison, listing every visible deviation and its remedy. If exact font identification is unresolved, document the candidate difference instead of pretending it matches. Acceptance: real controls, faithful static composition and documented responsive behavior. Do not proceed to large-scale art production with an unresolved material fidelity gap.


---

Source: prompts/UI02-G-Living-Environment-Proof.md

# UI02 — G Living Environment Proof

Dependency: UI01 static screen and original P00 device environment.

Read: docs/05, 06, 08.

## Paste into your coding agent

You are implementing WordQuest against the original Production Blueprint and the G/H/I UI Realms Addendum. Read README and docs/01 first, then this task's relevant documents and actual image references. Preserve the original gameplay composition and realm-specific styling. Home images are proposals. Do not reinterpret the art direction, bake learning text into art, implement a flattened screenshot as the UI, or claim a generated concept is a tested engine screen. Keep learning logic independent of theme and companion. Respect existing repository instructions and user changes. Do not introduce purchases, remote AI calls, extra plugins or multiplayer merely to complete this task. Use available tools and report unavailable editor/device access honestly.

Proceed autonomously with reversible implementation and verification in the authorized scope. Ask only for a material unresolved product decision or unavailable required access; complete the reviewable work first. Record exact files changed, execution commands, evidence, remaining limitations and next dependency. Do not claim unrun tests passed. Preserve the original P00–P21 release gates.

## Task

Animate one separated cloud layer and lantern glow first, then add only justified low-cost ambient elements. Keep all effects outside the reading and interaction masks. Implement full, reduced and battery settings plus a deterministic freeze/capture mode. Prove that the original still composition can be reproduced with motion frozen. Run a packaged phone build when hardware is available, measure frame time and memory, and capture at least 60 seconds of motion. Check edges, seams, transparency, bloom, thermal behavior and inactive-screen cancellation. Acceptance: visible gentle motion without ghosting or reading distraction; motion-off behavior and actual device evidence. If device access is absent, deliver the build and exact run guide while clearly marking the gate unverified.


---

Source: prompts/UI03-H-I-and-Theme-Components.md

# UI03 — H I and Theme Components

Dependency: UI01/UI02; original P02/P06 foundation for integration.

Read: docs/03, 04, 06; all three gameplay references.

## Paste into your coding agent

You are implementing WordQuest against the original Production Blueprint and the G/H/I UI Realms Addendum. Read README and docs/01 first, then this task's relevant documents and actual image references. Preserve the original gameplay composition and realm-specific styling. Home images are proposals. Do not reinterpret the art direction, bake learning text into art, implement a flattened screenshot as the UI, or claim a generated concept is a tested engine screen. Keep learning logic independent of theme and companion. Respect existing repository instructions and user changes. Do not introduce purchases, remote AI calls, extra plugins or multiplayer merely to complete this task. Use available tools and report unavailable editor/device access honestly.

Proceed autonomously with reversible implementation and verification in the authorized scope. Ask only for a material unresolved product decision or unavailable required access; complete the reviewable work first. Record exact files changed, execution commands, evidence, remaining limitations and next dependency. Do not claim unrun tests passed. Preserve the original P00–P21 release gates.

## Task

Create shared semantic controls backed by distinct G/H/I theme definitions. H must retain its deep blue-violet reading panel and ivory type; do not force it into the light G/I panel. Preserve I's sculpted gold/star identity and G's lighter ivory-lilac treatment. Prepare H canopy/water and I moon/library/crystal layers, masks and quality variants. Share component behavior, not arbitrary identical ornament. Compare each static screen to its original and record a motion proof for each. Acceptance: three independently faithful skins, live controls, no forked scoring logic and no simultaneous loading of all full-quality environments in ordinary play.


---

Source: prompts/UI04-Realm-Resolver-and-Settings.md

# UI04 — Realm Resolver and Settings

Dependency: UI03; original P05 persistence and navigation contract.

Read: docs/02, 08; specs/theme-config.example.json.

## Paste into your coding agent

You are implementing WordQuest against the original Production Blueprint and the G/H/I UI Realms Addendum. Read README and docs/01 first, then this task's relevant documents and actual image references. Preserve the original gameplay composition and realm-specific styling. Home images are proposals. Do not reinterpret the art direction, bake learning text into art, implement a flattened screenshot as the UI, or claim a generated concept is a tested engine screen. Keep learning logic independent of theme and companion. Respect existing repository instructions and user changes. Do not introduce purchases, remote AI calls, extra plugins or multiplayer merely to complete this task. Use available tools and report unavailable editor/device access honestly.

Proceed autonomously with reversible implementation and verification in the authorized scope. Ask only for a material unresolved product decision or unavailable required access; complete the reviewable work first. Record exact files changed, execution commands, evidence, remaining limitations and next dependency. Do not claim unrun tests passed. Preserve the original P00–P21 release gates.

## Task

Implement Surprise me, Keep this realm and Match my companion with stable IDs and versioned persistence. Implement the persisted shuffle bag and fresh-visit definition exactly as doc02; pin an active mission and defer changes to a safe boundary. Make repeated lifecycle callbacks idempotent. Preload assets before switching and cancel obsolete requests. Provide accessible settings, previews, loading/failure recovery and fallback. Use meaningful automated state tests for session resolution, bag boundaries, missing themes, process death and corrupted preferences. Acceptance: changing screens does not reroll, resume never loses a mission, and theme changes cannot affect learning or purchases.


---

Source: prompts/UI05-Three-Optional-Companions.md

# UI05 — Three Optional Companions

Dependency: UI03/UI04; shared animation and save contracts.

Read: docs/07, 05, 08; all original gameplay images.

## Paste into your coding agent

You are implementing WordQuest against the original Production Blueprint and the G/H/I UI Realms Addendum. Read README and docs/01 first, then this task's relevant documents and actual image references. Preserve the original gameplay composition and realm-specific styling. Home images are proposals. Do not reinterpret the art direction, bake learning text into art, implement a flattened screenshot as the UI, or claim a generated concept is a tested engine screen. Keep learning logic independent of theme and companion. Respect existing repository instructions and user changes. Do not introduce purchases, remote AI calls, extra plugins or multiplayer merely to complete this task. Use available tools and report unavailable editor/device access honestly.

Proceed autonomously with reversible implementation and verification in the authorized scope. Ask only for a material unresolved product decision or unavailable required access; complete the reviewable work first. Record exact files changed, execution commands, evidence, remaining limitations and next dependency. Do not claim unrun tests passed. Preserve the original P00–P21 release gates.

## Task

Implement the three existing spirit identities as optional cosmetic companions with data-driven preferred realms. Treat Aster/Luma/Quill as working names. Preserve silhouettes and materials. Build the eight states specified in doc07, supporting reduced motion and cancellation. Offer selection after the first successful learning experience, with a clear skip option and explicit opt-in to link realm to companion. Keep fixed/surprise modes independent. Use a compatible placement zone across themes and test all nine combinations. Add stable optional House identity only if the current data design needs it; do not build twelve characters or social infrastructure. Acceptance: companion selection works, is reversible, gives no learning advantage and never imposes a theme silently.


---

Source: prompts/UI06-Complete-Screen-Family.md

# UI06 — Complete Screen Family

Dependency: UI03–UI05; original P04/P06/P08 functionality.

Read: docs/04, 08; all three home drafts and gameplay targets.

## Paste into your coding agent

You are implementing WordQuest against the original Production Blueprint and the G/H/I UI Realms Addendum. Read README and docs/01 first, then this task's relevant documents and actual image references. Preserve the original gameplay composition and realm-specific styling. Home images are proposals. Do not reinterpret the art direction, bake learning text into art, implement a flattened screenshot as the UI, or claim a generated concept is a tested engine screen. Keep learning logic independent of theme and companion. Respect existing repository instructions and user changes. Do not introduce purchases, remote AI calls, extra plugins or multiplayer merely to complete this task. Use available tools and report unavailable editor/device access honestly.

Proceed autonomously with reversible implementation and verification in the authorized scope. Ask only for a material unresolved product decision or unavailable required access; complete the reviewable work first. Record exact files changed, execution commands, evidence, remaining limitations and next dependency. Do not claim unrun tests passed. Preserve the original P00–P21 release gates.

## Task

Use the home drafts as proposed compositions and implement a coherent journey: home, realm chooser, optional companion chooser, question, submitted-answer explanation, mission results and lexicon detail. Complete mode-specific screens and settings/loading/empty/error states identified in doc04 before declaring UI coverage complete. Preserve substantial space for serious vocabulary definitions, nuance and examples. Use actual application state for progress and review counts. Feedback must explain meaning, not merely celebrate. Match visual anchors across themes while keeping the same navigation semantics. Deliver a screen coverage matrix with functional, visual and accessibility evidence. Record new compositions for product review; do not silently call them approved.


---

Source: prompts/UI07-Device-Fidelity-and-Accessibility.md

# UI07 — Device Fidelity and Accessibility

Dependency: UI06 and original P09 qualification environment.

Read: docs/03, 05, 08.

## Paste into your coding agent

You are implementing WordQuest against the original Production Blueprint and the G/H/I UI Realms Addendum. Read README and docs/01 first, then this task's relevant documents and actual image references. Preserve the original gameplay composition and realm-specific styling. Home images are proposals. Do not reinterpret the art direction, bake learning text into art, implement a flattened screenshot as the UI, or claim a generated concept is a tested engine screen. Keep learning logic independent of theme and companion. Respect existing repository instructions and user changes. Do not introduce purchases, remote AI calls, extra plugins or multiplayer merely to complete this task. Use available tools and report unavailable editor/device access honestly.

Proceed autonomously with reversible implementation and verification in the authorized scope. Ask only for a material unresolved product decision or unavailable required access; complete the reviewable work first. Record exact files changed, execution commands, evidence, remaining limitations and next dependency. Do not claim unrun tests passed. Preserve the original P00–P21 release gates.

## Task

Execute doc08's acceptance matrix using packaged builds. Capture deterministic stills for G/H/I and compare against original references. Test long text, 200% text scaling, bright/dark effects composites, screen reader/focus navigation, touch sizing, reduce motion, sparkles off, battery tier, offline launch, interrupted loads and mission recovery. Profile representative and minimum physical phones, including realm-swap peak memory and sustained thermal behavior. Fix defects within authorized scope, retest affected paths and publish a compact evidence report. Acceptance: all critical criteria pass on named devices; unsupported or unavailable checks remain explicitly unverified, never inferred from desktop success.


---

Source: prompts/UI08-Integrate-and-Release-Review.md

# UI08 — Integrate and Release Review

Dependency: UI07; original P15–P21 when full product is ready.

Read: docs/01, 08, 09, 10; original complete production blueprint.

## Paste into your coding agent

You are implementing WordQuest against the original Production Blueprint and the G/H/I UI Realms Addendum. Read README and docs/01 first, then this task's relevant documents and actual image references. Preserve the original gameplay composition and realm-specific styling. Home images are proposals. Do not reinterpret the art direction, bake learning text into art, implement a flattened screenshot as the UI, or claim a generated concept is a tested engine screen. Keep learning logic independent of theme and companion. Respect existing repository instructions and user changes. Do not introduce purchases, remote AI calls, extra plugins or multiplayer merely to complete this task. Use available tools and report unavailable editor/device access honestly.

Proceed autonomously with reversible implementation and verification in the authorized scope. Ask only for a material unresolved product decision or unavailable required access; complete the reviewable work first. Record exact files changed, execution commands, evidence, remaining limitations and next dependency. Do not claim unrun tests passed. Preserve the original P00–P21 release gates.

## Task

Audit UI completion against both plans. Check original content, save, accessibility, privacy, purchases, offline, platform and release requirements remain satisfied; beautiful screens do not replace them. Verify font/art/audio provenance, package contents, all three offline realms and production build settings. Produce a requirement-to-evidence table, unresolved issue list, actual device results and release recommendation. Do not mark a release ready if only images or a prototype exist. Prepare the concrete deliverables required by the original release process; honor existing authorization and any applicable publishing gate. Acceptance: complete truthful evidence and no hidden expansion to twelve Houses, guilds or extra worlds.
