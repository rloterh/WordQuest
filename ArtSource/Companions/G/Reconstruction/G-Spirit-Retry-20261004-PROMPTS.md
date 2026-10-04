# Close-up G spirit retry, discarded

Built-in `image_gen.imagegen`, edit / background-extraction, transparency requested.
Input: inspected exact-pixel diagnostic crop of the immutable original gameplay
image, box [72,266,300,471), 228x205; no resampling or reference replacement.
Input SHA-256 `881c06f6b4dc6e885fca63827474f567d3e08a17a7e8af3be04e7ed87da6358f`.

## Exact prompt

Use case: background-extraction.
Input image: an exact-pixel diagnostic close-up of the ORIGINAL WordQuest G spirit, cropped from the owner's gameplay reference; it is the edit target and sole identity authority. This is a background-removal edit, NOT a new character illustration.
Remove only the surrounding blue/purple sky, castle fragments and flowers, making them genuinely transparent. Keep the existing white/lilac spirit and its gold lantern exactly as pictured: same face shape and angle, eyes and tiny smile, thin curved gold circlet, tiny pointed gold crest beneath the top wisp, translucent trailing wisps, tiny right-hand wisp, and hanging lantern's frame/panes/roof/finial. Do not enhance, redesign or add details. Preserve the slender circlet: never broaden it into a helmet or headpiece. No extra jewels, stars, glitter, eyelashes, tongues or limbs. Preserve all relative sizes and positions; don't enlarge the lantern or change its angle. Keep the full fine curling tips and lower lantern finial. Maintain the original soft painterly edge/lighting and lavender translucency, removing background contamination at the edges.
Output the complete same spirit-plus-lantern on a genuine transparent RGBA background with a small clear margin, clean antialiased alpha and no stray fragments or opaque rectangular background. No scene, text or new objects. Keep the supplied source unchanged; save a separate extraction candidate.

## Result

Generated path:
`C:/Users/HP/.codex/generated_images/01a0c93a-4fed-71e2-8bb4-3faa449a0984/exec-f53dfcf7-942f-4cf1-9b8e-bb74f037ee3c.png`.
Ignored copy: `Artifacts/QA/UI01/SpiritRetry20261004/attempt-1-rejected.png`.
SHA-256 `1dc9e0b09dccc9677c5d961a4aa9dd2e8fb47dcef92829c3109279098047d183`.
1323x1189 RGBA, alpha 0..255, nonzero bounds [0,9,1287,1157).
Character details/proportions are redrawn, and scattered edge pixels remain.
It is discarded, not imported, committed as art or adopted as a visual target.

The original itself has substantial gold banding and a tiny pink mouth detail;
the prompt's prohibition on a tongue/slenderness was too restrictive. Those are
not standalone rejection reasons. The selected alternative uses the original RGB
pixels with an editable static mask, not a revised generative character.
See `Docs/QA/UI01/G-SPIRIT-SOURCE-MASK.md` for source integrity and remaining gates.
No CLI/API imagegen fallback, paid tool or permission unlock was needed.
