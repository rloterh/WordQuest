# G working-art generation prompts

Tool: built-in `image_gen.imagegen`, 2026-09-22. No CLI fallback. Each source was
viewed before use. Original G gameplay reference was the input to calls 1–3;
the rejected panel from call 3 was the input to call 4. Files are saved within
`ArtSource`; generated originals are also retained in the tool's local output folder.
These are reconstruction attempts, not accepted game assets or runtime evidence.

## 1 — G-Clean-Plate-v001.png

Use case: precise-object-edit. Asset: WordQuest G Celestial Reverie clean environment plate, production reconstruction candidate. Edit the supplied image, preserving its original 884x1780 portrait composition, exact castle and waterfall silhouettes, crescent, lavender cloud ocean, side columns flowers and foreground steps, lighting and palette. Remove ALL interface: WordQuest title, pause button, progress plaque, the entire large reading panel and all buttons/text. Reconstruct the areas hidden by the panel as softly atmospheric lavender cloudscape leading to the existing foreground marble steps; no additional buildings or competing objects. Also remove the single white lantern-carrying companion entirely, including its lantern and glow, and reconstruct that small patch of distant cloud landscape. Preserve remaining visible art as closely as possible; no redesign. No text, letters, words, icons, panels, controls, characters, watermarks. This is only a background layer, not a finished interface. Save generated result so it can be copied into the project.

## 2 — G-Spirit-v001-Candidate.png

Use case: background-extraction. Extract ONLY the exact small white flowing lantern-carrying spirit from the left upper scene of the supplied G reference into a transparent PNG. Preserve exact original character identity: round white face, large navy eyes, tiny pink smiling mouth, flowing white/lilac hair and trailing leftward wisps, small gold headband, gold lantern below its face held at original angle. Same pose, proportions, silhouette and illustration lighting, not a redesign. Include lantern but no scene, clouds, text, stars, frame or other object. Actual alpha transparency, not checkerboard paint or black/white backdrop. Output tightly framed with small transparent margins, preserving original orientation and relative size of spirit versus lantern. High fidelity cutout for a separate Unreal sprite layer.

## 3 — G-Panel-v001-Rejected.png

Use case: background-extraction and precise-object-edit. Extract ONLY the large warm-white/lilac curved reading-panel surface from the original G WordQuest reference. It runs approximately x66 to820 y521 to1615 in the 884x1780 reference. Keep EXACT original silhouette: central pointed arch tip, lavender diamond near top, low curved shoulders, gold/pearl narrow bevel, near-vertical sides and gently curved bottom. Keep pastel pearlescent lavender-white material and original lighting. Remove every letter, word, clue, option, circular option badges, Hint and Check answer buttons, icons and horizontal text dividers from inside, replacing with uninterrupted blank pearlescent surface. No new ornament. Isolate on genuine transparent alpha background, tightly framed with small transparent margins. No environment, flowers, stairs, character or text. This is a standalone ornamental frame and blank reading surface for LIVE Unreal widgets; not a complete screenshot UI.

## 4 — G-Panel-v002-Candidate.png

Use case: background-extraction. Fix ONLY the alpha channel / background of this already-created blank ornamental reading panel. The gray checkerboard in the supplied file is incorrectly baked into opaque RGB pixels. Remove all checkerboard pixels outside the gold outer frame and output a genuine RGBA PNG with alpha=0 outside the frame, smooth partial alpha at antialiased edges, opaque panel interior. Keep the panel itself, dimensions, point at the top, diamond, gold trim, pastel material and proportions unchanged. Do not paint a checkerboard, white, black or any other replacement backdrop. Real transparency is essential.
