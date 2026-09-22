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
