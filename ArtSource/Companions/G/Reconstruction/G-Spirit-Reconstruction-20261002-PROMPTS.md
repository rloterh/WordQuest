# G spirit reconstruction prompts — candidates only

Built-in `image_gen.imagegen`, 2026-10-02; transparent background requested.
The original G gameplay PNG was inspected before use and remains unchanged.
No CLI fallback, raster script editing or layered art source is claimed.

## Attempt 1

Use case: background-extraction. Asset type: separate static WordQuest G Celestial Reverie companion texture, reconstruction candidate. Input image 1 is the immutable ORIGINAL gameplay reference; extract its existing small white/lilac lantern-carrying spirit from the upper-left scene around x82–289/y276–461. Only remove the surrounding scene/UI; keep the character's original identity, pose and relative proportions. Tight cutout with a small transparent margin, all wisps and lantern fully included, original leftward flowing silhouette and tilt. Preserve the modest dark-violet eyes and their spacing, tiny simple smiling mouth, softly rounded face, thin gold circlet, fine white/lilac trailing wisps, and small gold lantern hanging below-left of the face. The lantern must remain small relative to the head as in the reference. Preserve original painterly soft lighting and subtle lavender/gold, with no added glitter, star-shaped eye highlights, limbs or new ornament. Genuine transparent RGBA background with clean antialiased edges, not painted checkerboard, black or white. No palace, clouds, flowers, text, panel, frame or other subject. Do not make a new mascot or use an enlarged-eye/lantern interpretation. The supplied original file must remain unchanged; output a separate candidate.

Attempt 1 produced genuine RGBA but retained an oversized lantern and invented
spherical head ornament. It is not selected for runtime import.

## Attempt 2 — gold elements only

Use case: precise-object-edit. Input 1 is the transparent G spirit reconstruction edit target. Input 2 is the original gameplay image and is the authority for its small upper-left spirit's GOLD CIRCLET AND LANTERN. Change only these two gold elements in input 1 to match their shapes and relative scale in input 2: remove the invented spherical ornament atop the headband; use the original thin simple gold circlet with its small pointed crest. Reduce the lantern width/height about 18% while retaining its hanging-below-left location; match the original small pointed roof, straight slim gold frame and warm-white panes, without fancy arched panes or extra ornament. Keep the face, eyes, tiny smile, head tilt, white/lilac wisps and their exact placement/lighting unchanged. Preserve all transparency and clean fine edges. No extra glitter, limbs, background, text or other objects. Output the complete spirit plus corrected lantern as one genuine transparent RGBA image with a small clear margin, all wisps included, not checkerboard painted into RGB. This remains a static art candidate; do not produce animation or a full screen.

Attempt 2 has genuine RGBA and a smaller lantern, but introduced a prominent
four-point star on the circlet, changed its silhouette and retained different
face/lantern proportions. It is also rejected for runtime import. Neither attempt
changes the original v001 master/Unreal asset or becomes the new visual target.
Local copies remain under `Artifacts/QA/UI01/g-spirit-rejected-20261002`.

Output inspection, source provenance and native evidence are recorded in
`Docs/QA/UI01/G-SPIRIT-FRAMING.md`. Generation alone cannot pass identity,
static fidelity, motion or phone gates.
