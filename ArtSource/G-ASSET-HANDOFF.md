# G reconstruction handoff — not accepted production art

All work derives from immutable
`Planning/WordQuest-UI-Realms-Addendum/references/G-Celestial-Reverie-Gameplay.png`
(884x1780; hash recorded in original manifest). Original remains unchanged.
Built-in imagegen performed the raster reconstructions. No CLI/API fallback, paid plugin, manual
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
  On 2026-10-02 two new built-in reconstructions were rejected for gold ornament/
  face/lantern differences and were not imported. The preserved v001 now has a
  documented UV frame and aspect-preserving reference-region placement; this
  changes framing only. Exact prompts/provenance are under `Companions/G/Reconstruction`;
  evidence is in `Docs/QA/UI01/G-SPIRIT-FRAMING.md`. Identity remains unaccepted.
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

The subsequent blank progress-plaque v002 candidate is imported as
`/Game/UI/G/G_ProgressPlaque`. Its unchanged RGBA master, exact prompts and UV/import
provenance are under `UI/G/Reconstruction`. Native captures show live centered
`3 / 7` on the separate plaque and both hidden in compact landscape. The generated
core's proportions are adapted to the reference bounds; gold brightness/thickness,
bevel, purple lighting and edge noise still differ. No faithful-art acceptance or
layered source is claimed. See `Docs/QA/UI01/G-PROGRESS-PLAQUE.md`.

Hint/Check/Pause v001 surface candidates now live under `UI/G/Reconstruction`,
imported as `G_HintSkin`, `G_CheckSkin` and `G_PauseSkin`. Check/Pause v002 cleanup
attempts were rejected, not imported. Exact prompt sets and unchanged master hashes,
alpha/UV bounds and import settings are in `G-ACTION-SKINS-*`. Native normal,
enlarged-focus, hint-assisted disabled and paused captures were inspected. Gloss,
gold, geometry, fringe and font metrics still differ. Hint bulb and Check star
were absent in that increment. These are unapproved raster art candidates with no layered source claimed.
See `Docs/QA/UI01/G-ACTION-SKINS.md`.

The subsequent separate Hint bulb and four-point Check star candidates are
hand-authored editable SVGs under `UI/G/Vector`, copied without alteration to
`Game/Content/UI/G/Vector`. They render through native Slate vector brushes beside
live labels; no image generation or raster editing was used for these icons.
Native reference-size, enlarged, disabled, narrow-focus and missing-resource
captures were inspected. Shape, faceting and lighting acceptance remain open.
See the vector README and `Docs/QA/UI01/G-ACTION-ICONS.md`; UFS staging is declared,
but a packaged build has not verified these raw resources.

Short/long gold divider and rounded Pause-bar candidates now join the editable
SVGs under `UI/G/Vector`. Native normal, enlarged, narrow-focus, pause/resume,
landscape and missing-resource evidence is recorded in
`Docs/QA/UI01/G-VECTOR-ORNAMENTS.md`. These replace font-dependent decoration;
line taper, bevel/light and exact art acceptance remain open. Pause's actual button,
semantic name and text fallback remain intact. No layered raster source is claimed.

On 2026-10-02 the local Win64 Development archive verified the draft JSON and all
five SVGs inside its pak with exact input hashes, plus native cooked texture/font
and vector rendering. See `Docs/QA/UI01/G-WIN64-PACKAGE-PROOF.md`. This closes that
desktop resource-path check only; it does not accept art, offline/device or release
gates. Earlier unverified-package statements describe their original increments.

1. Faithful spirit RGBA at the original x82–289/y276–461 placement, clean anti-aliased
   perimeter, same face and lantern. Provide separate local lantern-emission mask.
2. Blank panel matching original x65–823/y521–1618. Supply non-stretching top/corners/
   bottom and repeatable center/edges or documented nine-slice insets. Clean halos on
   both dark navy and bright cloud backgrounds.
3. Isolated cloud bank with overscan and matching clean plate underneath. Return
   frozen placement, pivot, motion bounds and alpha convention. Never slide a duplicated
   cloud over its original baked pixels or move the rigid castle silhouette.
4. Faithful accepted answer/action skins with pressed, selected, focus and disabled
   treatment. Candidates exist; further art correction and acceptance remain open.
   Badges/letters and all instructional text remain live widgets.
5. Accepted brand mark, progress plaque, divider ornament, Hint/Check/Pause icons
   and font sources with redistribution licenses and glyph/metric evidence.
   Hint/Check SVG and plaque candidates exist; faithful-art acceptance remains open.
   A separate outlined G wordmark candidate with authored gold/capital/swash
   ornament is now under `UI/G/Vector`; its OFL font source and optional builder
   are documented in the vector README and `Docs/QA/UI01/G-WORDMARK.md`.
   It does not identify or accept the original title lettering.

Use sRGB exports with straight alpha unless the importer explicitly converts it.
The G answer badge now also has an editable shaded SVG disc candidate under
`UI/G/Vector/G-Answer-Badge-v001.svg`, reused beneath live A–D letters. Selected
state is a separate native ring/marker; absent SVG retains the original solid
badge. Cooked resource and native state evidence are in
`Docs/QA/UI01/G-ANSWER-BADGE-MATERIAL.md`. This does not accept the answer skin,
badge material or typography as final art.

Retain source masks, painted hidden regions and editable layers in the artist's real
layered format, plus export settings and provenance. Do not fabricate `.blend` or
other editable-source files from a filename alone. No rights clearance beyond the
supplied reference provenance has been established; release clearance remains open.

The preserved v001 wordmark now has a v002 editable material candidate under
`UI/G/Vector`. It retains glyph/ornament paths and placement while adding warm
gradient, ivory rim and offset bevel layers. Cooked SVG bytes and normal-size title-
only pixel differences are verified; eight packaged captures were inspected.
See `Docs/QA/UI01/G-WORDMARK-BEVEL.md` and adjacent v002 provenance. This does not
identify or accept the original font, letterforms, flourishes or final brand art.

A v003 wordmark master now reconstructs W with authored closed curves while
preserving the v001/v002 masters, other eight licensed glyph outlines, transforms,
Q swash, ornament and v002 material treatment. Nine clean packaged captures were
inspected; cooked bytes match the master and reference-size changes stay inside
the title. Two lower-tip samples improve to within one pixel vertically of the
reference. Exact contours and original lettering/art remain unapproved. Provenance
is beside the SVG; evidence is in `Docs/QA/UI01/G-WORDMARK-CAPITAL.md`.

Both divider masters also have v002 material candidates, preserving their v001
path geometry and native reading positions. Gradients and directional star facets
are verified in a clean Win64 package with exact cooked-byte matches; all eight
native captures were inspected. See `Docs/QA/UI01/G-DIVIDER-BEVEL.md` and the
adjacent vector provenance. Line/taper, star shape/light and static fidelity
acceptance remain open. Earlier unverified statements describe their original work.

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
