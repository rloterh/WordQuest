# G blank answer-skin attempts

Built-in imagegen, 2026-10-01. Original G gameplay PNG remains unchanged.
These are reconstruction candidates, with no fidelity or release acceptance.

## v001 — rejected edge/shadow treatment

Use case: background-extraction / precise-object-edit. Asset type: a single blank Unreal UMG answer-button skin. Input image 1 is the original immutable G Celestial Reverie gameplay reference; extract a working asset without modifying the source. Isolate ONLY the first pearl/lavender answer button at approximately x109–775, y990–1085 on the 884x1780 reference. Preserve the original wide low rounded-rectangle silhouette (about 7:1), warm white upper bevel, thin pearl outline, restrained pale lavender gradient, subtle cloudy pearl texture and soft purple drop shadow directly below. Remove the A badge circle and all lettering completely, reconstructing only the small covered areas to match the surrounding blank surface. Output ONE straight-on blank wide button, tightly framed with just a small transparent margin for its shadow, genuine RGBA transparency outside its outline. No surrounding panel or scenery, no decorative icons, no text or letters, no badge, no extra buttons, no stars, no gold border, no redesign or thick glossy bubble. Keep its original delicate material and geometry; the letters/badges will be live native widgets. Do not draw a checkerboard or white/black background.

## v002 — candidate perimeter cleanup

Input 1: the v001 generated export. Input 2: immutable original G gameplay reference.

Use case: precise-object-edit. Image 1 is the working blank pearl button to correct; image 2 is its original G gameplay reference. Change only the perimeter and drop-shadow cleanup on image 1. Keep its blank lavender pearl interior, thin white bevel, horizontal capsule geometry and lack of lettering/badges. The current outer edge has white crust/noise across the top and electric blue/magenta fringe around the lower shadow. Remove that crust and all blue/magenta stray pixels; use clean, smooth antialiased RGBA edges matching the reference. Make the lower shadow as restrained as the reference: soft desaturated lavender, just a narrow diffuse shadow below the lower edge, not a thick dark purple pedestal. Preserve genuine transparency everywhere outside this one button/shadow. Output a tightly framed wide button on alpha, small margin only, no scenery or panel, no new symbols, no text, no checkerboard or opaque backdrop. Do not redesign the material or add shine.

Selected output is copied unchanged into `G-Answer-Skin-v002-Candidate.png`.
Generated originals remain in the tool's output folder. Runtime UV framing is
documented separately; no pixels, alpha, dimensions or references were manually edited.
