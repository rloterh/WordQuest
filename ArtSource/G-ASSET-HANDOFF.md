# G reconstruction handoff — not accepted production art

All work derives from immutable
`Planning/WordQuest-UI-Realms-Addendum/references/G-Celestial-Reverie-Gameplay.png`
(884x1780; hash recorded in original manifest). Original remains unchanged.
Built-in imagegen performed the edits. No CLI/API fallback, paid plugin, manual
paintover or Blender layer document has been used or claimed. On 2026-09-23 Unreal
imported the clean plate, panel v002 and spirit v001 for the native engineering proof;
that import does not change their unapproved art disposition.
Exact prompts are in `G-GENERATION-PROMPTS.md`; output metadata in `G-ASSETS.json`.

A further spirit extraction attempt on 2026-09-23 was rejected: 1191x1321 RGB,
baked checkerboard and altered face. It was neither imported nor committed. Exact
prompt: "Precise asset extraction from the supplied original WordQuest gameplay
image. Isolate ONLY the small flowing white/lilac lantern-carrying spirit in the
upper-left scene (approximately x82–289, y276–461 on the original 884x1780 canvas).
Output a tightly framed PNG on genuine transparent alpha, not black/white/checkerboard.
Preserve the original spirit exactly: same modest eye size and spacing, small smiling
mouth, tilted rounded face, white/lavender wisps sweeping to the left, small gold
circlet, and the same small gold lantern hanging below-left. Preserve the original
silhouette, face proportions, lantern-to-body scale, direction and painterly lighting.
Do not redesign, add stars in eyes, enlarge the head/eyes/lantern, make a new mascot,
add limbs, or add glitter. The only change is removal of every background/UI pixel
around the original spirit. Transparent fine wisps and clean alpha edges without
colored fringe. No text, no logo, no panel, no palace, no clouds."

## Review disposition

- `Environments/G/Reconstruction/G-Clean-Plate-v001.png`: inspected working clean
  environment, 884x1779 RGB. Title, interface and companion removed. Visible palace,
  moon, columns and foliage closely follow the reference, but regenerated pixels are
  not identical. Hidden lower landscape is reconstructed cloud fill. Restore one-pixel
  canvas-height difference and compare architecture/foreground against original.
- `Companions/G/Reconstruction/G-Spirit-v001-Candidate.png`: genuine RGBA; original
  flowing silhouette/lantern concept retained, but mouth, eyes, lantern and fine wisps
  differ. **Not accepted as faithful identity**. Re-extract/mask original source pixels
  or commission a traced paintover with matched face, proportions and light.
- `UI/G/Reconstruction/G-Panel-v001-Rejected.png`: **rejected**. RGB checkerboard was
  baked into the image. Retained only to explain the alpha correction; never import it.
- `UI/G/Reconstruction/G-Panel-v002-Candidate.png`: RGBA correction, corner alpha 0;
  blank surface has no educational text. Needs edge-fringe cleanup, proportion and
  gold-bevel comparison. A correct alpha channel does not establish visual acceptance.

## Concrete missing deliverables

On 2026-10-01 a blank pearl answer-skin v002 candidate was added under
`UI/G/Reconstruction` and imported as `/Game/UI/G/G_AnswerSkin`. Native initial and
enlarged focused-answer captures show its separate live text/badges and retained
focus outline. Its generated bevel/texture, cropped external shadow, edge treatment
and proportions still differ from the original. It is not accepted fidelity or
release art. Exact prompts, unchanged raster master and UV/import provenance are
stored alongside the source PNG; no layered source is claimed. The remaining items
below still require art work and acceptance, including the purple check skin.

1. Faithful spirit RGBA at the original x82–289/y276–461 placement, clean anti-aliased
   perimeter, same face and lantern. Provide separate local lantern-emission mask.
2. Blank panel matching original x65–823/y521–1618. Supply non-stretching top/corners/
   bottom and repeatable center/edges or documented nine-slice insets. Clean halos on
   both dark navy and bright cloud backgrounds.
3. Isolated cloud bank with overscan and matching clean plate underneath. Return
   frozen placement, pivot, motion bounds and alpha convention. Never slide a duplicated
   cloud over its original baked pixels or move the rigid castle silhouette.
4. Blank pearl answer skin and purple check skin with pressed, selected, focus and
   disabled treatment. Badges/letters and all instructional text remain live widgets.
5. Clean brand mark, progress plaque, divider ornament, hint/pause icons and font
   sources with redistribution licenses and glyph/metric evidence.

Use sRGB exports with straight alpha unless the importer explicitly converts it.
Retain source masks, painted hidden regions and editable layers in the artist's real
layered format, plus export settings and provenance. Do not fabricate `.blend` or
other editable-source files from a filename alone. No rights clearance beyond the
supplied reference provenance has been established; release clearance remains open.

## Runtime handoff after static art and build prerequisites

Use one common Context Detective screen; realm data selects art/fonts/skins, while
answer correctness and assistance are independent of presentation. Keep educational
text out of textures. At t=0 no option is selected; selecting marks only selection,
and submitting yields deterministic feedback. Duplicate submit must not create
duplicate rewards. Fixture approval is separately recorded in `Docs/Decisions`.

UI02 follows accepted UI01. Use a local cloud layer and small lantern emission pulse,
full/reduced/battery profiles, inactive cancellation and explicit frozen time/seed.
Exclude reading and control masks. Do not animate these unresolved candidates and
call a motion render accepted.
