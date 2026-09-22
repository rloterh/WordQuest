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
