# G blank progress-plaque attempts

Built-in imagegen, 2026-10-01. Original G reference remains unchanged. These are
unapproved reconstruction candidates, not faithful or release-accepted art.

## v001 — rejected edge treatment

Input: immutable original G gameplay PNG.

Use case: background-extraction / precise-object-edit. Asset type: a single blank Unreal UMG progress plaque. Input image 1 is the immutable original G Celestial Reverie gameplay reference. Isolate ONLY the small purple-and-gold progress plaque surrounding '3 / 7' at approximately x352–530, y169–230 on the 884x1780 reference. Preserve its exact low wide silhouette (178:61, about 2.92:1): straight horizontal top and bottom, tiny stepped shoulders, symmetric inward-curving edges ending at pointed left/right centers. Preserve the delicate warm pale-gold double bevel outline, royal indigo-purple interior, faint soft lavender light along the top and restrained diffuse shadow. Remove ALL numerals and the slash, reconstructing the covered blank purple surface. Output ONE straight-on, horizontally centered blank plaque, tightly framed with only a very small transparent margin, genuine RGBA alpha outside the shape. No scenery, no title, no text/letters/numerals, no stars, no additional ornaments or flourish, no inflated button gloss, no thick ornate frame, no checkerboard or opaque background. This is a faithful extraction/reconstruction of that one reference detail, not a redesign; live text will be a separate native widget. Do not alter the original input.

Output: `exec-f42d8fd7-cc18-4b7e-9f33-b60da3137eb5.png` in the built-in output
folder. Rejected visible red/yellow fringe and overly wide core; not imported.

## v002 — working candidate

Input 1: v001 generated export. Input 2: immutable original G gameplay PNG.

Use case: precise-object-edit. Image 1 is the generated blank progress plaque to correct. Image 2 is the original immutable G gameplay reference. Correct only the generated perimeter and silhouette: remove every red/yellow stray pixel, colored fringe and edge noise outside the gold border. Use smooth clean antialiased genuine transparent alpha edges. Keep the indigo interior blank and the thin warm pale-gold double bevel, matching the reference plaque around '3 / 7'. Its target core width-to-height is 178:61 (2.92:1), not the overly wide/flat 3.8:1 current core; gently bring it to the reference proportion while retaining the exact symmetric pointed ends, stepped shoulders and straight top/bottom. The border must stay delicate, not thicker. Output one tight-framed blank straight-on plaque with only a tiny clear margin. No numerals/slash/text, no stars, no new ornament, no scenery, no opaque or checkerboard background. Preserve true RGBA outside; do not change the original reference.

Selected output is copied unchanged to `G-Progress-Plaque-v002-Candidate.png`.
The correction still leaves faint colored fringe and a wider core than requested;
native UV framing and reference-sized drawing are documented in provenance/QA.
No raster pixels, alpha or source dimensions were manually edited. No layered
paint document or exact extraction of original source pixels is claimed.
