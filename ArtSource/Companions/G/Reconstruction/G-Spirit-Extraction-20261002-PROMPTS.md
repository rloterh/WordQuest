# G companion extraction attempts after PR #19

Built-in imagegen, `background-extraction`, transparent background requested.
These are rejected experiments, not editable production masters or new visual
targets. Neither output is imported or referenced by the game. Supplied original
G reference and existing v001 source/Unreal asset remain unchanged.

## Attempt 1

```text
Use case: background-extraction
Asset type: transparent G companion sprite for the existing Unreal gameplay proof.
Input image 1 is the edit target and sole identity authority: the original 884x1780 G gameplay reference. Extract ONLY the existing little spirit and its lantern at approximately x82–289,y276–461 into a tightly framed transparent cutout. Remove the surrounding castle scene and all UI. Preserve the character as it is drawn in that region: same face shape and tilt, exact modest dark violet eyes and tiny smiling mouth, flowing white/lilac wisps sweeping to the left, thin gold circlet with the small pointed crest, and small gold lantern below-left. Preserve the relative geometry and proportions of all parts; treat this as careful background removal, not character redesign or a new illustration. Keep the lantern at the original size relative to the face, its tall narrow body and fine roof details. No spherical ornament, star crown, four-point star, limbs, glitter eyes, enlarged lantern, background clouds or scene fragments. Keep the existing soft pearl/lilac shading and gold light. Genuine RGBA transparency with clean softly antialiased edges and a small transparent margin around every wisp and the lantern. No checkerboard baked into pixels. No text. Output only this isolated existing companion. The original supplied image must remain unchanged.
```

## Attempt 2: targeted correction

```text
Use case: background-extraction
Input 1 is the immutable original G gameplay reference and sole identity authority; input 2 is a rejected transparent extraction to correct. Change only the identity drift in input 2 to match the small existing spirit at original x82–289,y276–461: replace the new turret-like circlet crest with the original fine small pointed crest and thin circlet, close and shrink the mouth to the original tiny smile, and restore the original small narrow lantern and its relative size/placement below-left of the face. Match these details to input 1 exactly, without inventing a new crest, star, globe, or expression. Keep the existing left-flowing pearl/lilac wisps, pose, lighting and soft edges. Genuine RGBA transparency, no scene fragments or baked checkerboard. Keep every wisp and lantern inside the frame with transparent margin. Output only the isolated companion; do not redraw the gameplay scene.
```

Both outputs have RGBA transparency. Attempt 1 invents a turret-like crest and
changes the mouth/lantern proportions. Attempt 2 retains an enlarged four-point
star crest and differs from the supplied character. Direct visual inspection
rejected both; no fidelity, import or runtime acceptance is inferred.
Local outputs, hashes and alpha inspection are recorded in
`Artifacts/QA/UI01/g-spirit-rejected-after-pr19/inspection.json`.

Both outputs are 1434x1097 RGBA, alpha extrema 0..255, four corner alpha values
zero. SHA-256: attempt 1
`b4020b05cfce7b560ec166643de330f4b9da35324ef345619a973be96f82c2b8`;
attempt 2 `b7f4af117a56180766bbf2e5b606d341c147aef5ad1f79c65aae30b1b4731d4e`.
Original reference SHA-256 remains
`306dae4f6352749edcf1d8edf73f26339a4ba6407b4a394ec50b5898418bedae`.
