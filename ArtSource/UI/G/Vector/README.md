# G vector icon and divider candidates

## Editable Check surface

`G-Check-Surface-v001.svg` is a blank 388x113 violet/pale-gold surface with soft
bevel and four static glints. It renders at 2x using the same development-only
resvg renderer (`python Tools/AssetImport/render_g_check_surface.py --check`).
Unreal imports the PNG as `G_CheckReverie`; native nine-slice scaling preserves
the live label/star, controls and earlier generated texture fallback. This PNG
pipeline adds no staged runtime SVG pair. Provenance and native/package evidence
are in `G-Check-Surface-v001-PROVENANCE.json` and `Docs/QA/UI01/G-CHECK-SURFACE.md`.
The simplified material remains an unapproved reconstruction.

## Refined answer badge

`G-Answer-Badge-v002.svg` stages as `G_AnswerBadge.svg`. It preserves the 70x70
canvas, centered circular face and outer extent while lightening the upper lilac
fill and splitting the rim into two thin translucent layers. v001 stays unchanged;
letters and selected/focus feedback remain live native widgets. No raster or
binary asset is added. Exact hashes, native evidence and remaining limits are in
`G-Answer-Badge-v002-PROVENANCE.json` and
`Docs/QA/UI01/G-ANSWER-BADGE-SOFTNESS.md`. Fidelity is not yet accepted.

## Authored reading panel and separate star

`G-Reading-Panel-v001.svg` is a blank editable 790x1140 panel with a thin pale
gold/ivory rim, restrained gradient/grain surface and fixed corner regions.
`python Tools/AssetImport/render_g_reading_panel.py --check` reproduces its 1.5x
RGBA export using the same development-only renderer below. Unreal imports the
export as `G_ReadingPanel`; the earlier panel remains the missing-asset fallback.
The separate `G-Panel-Star-v002.svg` stages as `G_PanelStar.svg`; the parity helper
now checks eight pairs. Source/export/asset provenance and native evidence are in
`G-Reading-Panel-v001-PROVENANCE.json` and `Docs/QA/UI01/G-AUTHORED-READING-PANEL.md`.
These are unapproved reconstructions with simpler material than the original.

Star v002 preserves v001's canvas, outer path and native placement. It replaces
the continuous pale cross with violet directional facets, a pale upper-right
face, warmer lower-left face and small center glint. Earlier v001 remains unchanged.
`G-Panel-Star-v002-PROVENANCE.json` supersedes the earlier panel provenance's
staged-star entry only; panel source/export/texture are unchanged. See
`Docs/QA/UI01/G-PANEL-ORNAMENT-FACETS.md` for native/package comparisons and limits.

## Authored pearl surface export

`G-Answer-Pearl-v001.svg` is a separate editable blank surface candidate. A thin
ivory/lilac rim, broad diffuse gradients and soft shadow replace the previous
generated skin's rolled gloss. Its 690x119 canvas contains a 666x95 core at (12,4).
The 2x rendered `../Exports/G-Answer-Pearl-v001.png` (1380x238) is imported by Unreal as
`/Game/UI/G/G_AnswerPearl`; it is not loaded as a runtime SVG. Native nine-slice
insets (56,48,56,68 reference units; doubled in texture pixels) retain
corners/shadow while the center grows. Earlier
generated PNG/texture are preserved. No supplied pixels are changed; no imagegen
or raster paintover is used. Material and full fidelity acceptance remain open.

Reproduce the export using the development-only renderer, outside tracked source:

```powershell
python -m pip install --only-binary=:all: --target Artifacts/Tools/resvg resvg-py==0.5.0
python Tools/AssetImport/render_g_answer_pearl.py --check
```

Omit `--check` to regenerate from the editable master. See the renderer's
[SVG-to-PNG API](https://resvg-py.readthedocs.io/en/latest/api.html).
Normal builds use checked-in art and require no Python renderer. Import with
`Tools/AssetImport/import_g_answer_pearl.py` through the same texture-only Unreal
Python commandlet described in `Docs/QA/UI01/G-ANSWER-PEARL-SURFACE.md`.
Exact dimensions, hashes and remaining limits are in the adjacent provenance.

## Runtime SVG resources

These are hand-authored editable SVG reconstructions informed by the immutable
G Celestial Reverie gameplay reference. They are not exact original-pixel
extractions or accepted production art. No image generation or raster editing
was used for this increment. Reference composition and icon identity are the
targets; shape, faceting and lighting still require visual acceptance.

| Editable master | Runtime resource | Geometry |
| --- | --- | --- |
| `G-Hint-Bulb-v002.svg` | `Game/Content/UI/G/Vector/G_HintBulb.svg` | 40x56 viewBox; revised optical position, narrower rounded navy outline and two base bars; v001 preserved |
| `G-Check-Star-v002.svg` | `Game/Content/UI/G/Vector/G_CheckStar.svg` | 48x48 viewBox; white/lilac/gold directional facets, violet center and restrained static halo/glints; v001 preserved |
| `G-Header-Divider-v002.svg` | `Game/Content/UI/G/Vector/G_HeaderDivider.svg` | 214x29 viewBox; preserved tapered lines/terminals/star with gold gradients and ivory facets |
| `G-Reading-Divider-v002.svg` | `Game/Content/UI/G/Vector/G_ReadingDivider.svg` | 314x29 viewBox; matching long divider with the same material treatment |
| `G-Pause-Bars-v001.svg` | `Game/Content/UI/G/Vector/G_PauseBars.svg` | 24x30 viewBox; two white rounded bars, runtime tint follows skin availability |
| `G-Wordmark-v004.svg` | `Game/Content/UI/G/Vector/G_Wordmark.svg` | 430x140 viewBox; authored W, adapted Q bowl/looped swash, seven other licensed outlines and retained ivory/gold ornament |
| `G-Answer-Badge-v002.svg` | `Game/Content/UI/G/Vector/G_AnswerBadge.svg` | 70x70 viewBox; refined lilac disc and layered pale rim, with no baked letter |

From the repository root:

```powershell
python Tools/AssetImport/stage_g_action_icons.py
python Tools/AssetImport/stage_g_action_icons.py --check
```

The first command copies the masters; `--check` verifies SVG structure and exact
source/runtime byte parity without writing. The helper prints current SHA256
hashes. Both copies are ordinary Git text. No `.uasset` is fabricated or required
for this raw-resource path.

UE 5.8.2's `FSlateVectorImageBrush` loads and rasterizes the runtime SVGs. UMG
keeps Hint/Check icons separate from their live button labels. Missing Hint/Check
resources collapse the icon and its spacing. Missing divider resources collapse
only their decoration while preserving reading layout. Pause retains its semantic
name/tooltip and uses its original text fallback if its SVG is absent; its vector
is independent of display fonts and remains at least 14x18 logical units inside
the existing minimum 48-unit control. `DefaultGame.ini` declares the directory for UFS
staging. The subsequent local Win64 Development package verifies all five SVGs
inside its pak and in native rendering; see `Docs/QA/UI01/G-WIN64-PACKAGE-PROOF.md`.
Android/iOS packaging remains unverified. Earlier native desktop evidence
and remaining gates are in `Docs/QA/UI01/G-ACTION-ICONS.md` and
`Docs/QA/UI01/G-VECTOR-ORNAMENTS.md`. The staging helper's historical filename is
retained; it now checks all six masters/runtime copies. The sixth resource is a
separate G brand candidate; its new packaged verification is recorded in
`Docs/QA/UI01/G-WORDMARK.md`.

The wordmark's licensed lettering derives from the repository's unmodified
Cormorant Garamond SemiBold (`ArtSource/Fonts/CormorantGaramond`, adjacent OFL and
provenance); revision v003 replaces W with authored reference-guided curves.
It does not identify the reference's lettering. The other five masters remain
unchanged. Its independent ornament paths and font outlines are editable SVG;
no font lookup is needed to render the mark. Only this fixed brand is outlined;
all learning text and control labels remain live widgets. The mark has a custom
`WordQuest` accessibility name; missing SVG retains the live title fallback.
Screen-reader service behavior is unverified.

To rebuild this candidate from its font and authored curves, install the pinned
development-only outline tool outside tracked source, then stage normally:

```powershell
python -m pip install --target Artifacts/Tools/fonttools fonttools==4.61.1
$env:PYTHONPATH = "$PWD/Artifacts/Tools/fonttools"
python Tools/AssetImport/build_g_wordmark.py --revision v004
python Tools/AssetImport/stage_g_action_icons.py
```

The checked-in SVGs are sufficient for normal builds; neither Unreal nor the
parity check requires this Python package. The builder uses
[fontTools SVGPathPen](https://fonttools.readthedocs.io/en/latest/pens/svgPathPen.html)
and transformed glyph outlines. No supplied image pixels are changed or extracted.

Revision v002 keeps the v001 master unchanged and adds separate vector bevel/rim
layers over the same glyph paths and authored ornament. It changes palette/strokes,
not title placement, font source, learning text or interactive controls. Use
`--revision v001` to reproduce the preserved first candidate.
Provenance and remaining limitations are in `G-Wordmark-v002-PROVENANCE.json`
and `Docs/QA/UI01/G-WORDMARK-BEVEL.md`. Letterform, flourish, lighting and faithful
art acceptance remain open. The package claims above describe earlier revisions.

Revision v003 preserves both earlier masters and replaces the W glyph/curls with
authored closed curves. The deeper tips and splayed stems follow the original
reference more closely in native inspection. The remaining eight glyph paths,
their advances/transform, Q swash, under-title ornament, bevel palette and native
placement are preserved. That increment defaulted to v003; explicit v001/v002 options
reproduce the older revisions. See `G-Wordmark-v003-PROVENANCE.json` and
`Docs/QA/UI01/G-WORDMARK-CAPITAL.md` for verification and remaining limitations.
No raster edit, new font or original-lettering acceptance is claimed.

No rights clearance beyond supplied-reference provenance is established. Release
clearance and faithful-art acceptance remain open.

The tenth staged resource is `G-Pause-Surface-v001.svg`: a blank, hand-authored
71x75 blue-violet surface with pale-gold rim and restrained directional lighting.
Its runtime copy is `G_PauseSurface.svg`. The separate Pause-bars icon and native
button retain their semantic/input path. Missing SVG preserves the original
generated texture; missing both preserves the native fill and dark bars/text.
Normal vector rim, existing focus ring and hover/press overlays are separate.
See `G-Pause-Surface-v001-PROVENANCE.json` and `Docs/QA/UI01/G-PAUSE-PEARL-RIM.md`.
Contour, material, manual input, full art and physical-device gates remain open.

The ninth staged resource is `G-Progress-Plaque-v001.svg`: a blank, hand-authored
178x61 progress decoration with curved shoulders, softly shaded purple face and
thin pale-gold bevel. `G_ProgressPlaque.svg` is its byte-identical runtime copy.
The separate native `3 / 7` remains live and semantically labelled. Missing SVG
retains the previous generated texture with its exact framing; compact landscape
hides both decoration and progress. Earlier plaque master/texture are preserved.
See `G-Progress-Plaque-v001-PROVENANCE.json` and
`Docs/QA/UI01/G-PROGRESS-PLAQUE-MATERIAL.md`; full art/device gates remain open.

Divider revision v002 preserves both v001 masters and all path coordinates/canvas
sizes. Explicit-percentage SVG gradients shade the tapered lines and star bevel;
an ivory upper facet and darker lower facet supply directional light. Staging uses
the two v002 masters; runtime names, native placement and reading spacing are
unchanged. No raster edit or image generation is used. See
`G-Divider-v002-PROVENANCE.json` and `Docs/QA/UI01/G-DIVIDER-BEVEL.md` for evidence
and remaining line/taper/star/material acceptance. Earlier package records above
describe their original revisions.

The seventh resource reconstructs the reference's softly shaded answer badge.
Four native overlays reuse that SVG under separate live A–D labels. A transparent
native border supplies the selected navy ring; the existing selection marker and
button outline remain. Missing SVG retains the original solid native badge.
It is decoration with hit testing and accessibility disabled; the answer button
retains the semantic label and interaction region. The existing 70-reference-pixel
badge sizing, 32-unit minimum, 200% text scaling and row measurements are preserved.
No original image pixels were edited/extracted and no raster or binary asset was
generated. The staging helper now checks all seven masters/runtime copies.
Native/cooked verification and remaining differences are recorded in
`Docs/QA/UI01/G-ANSWER-BADGE-MATERIAL.md`.

Revision v004 preserves all three earlier masters. It removes the straight
descender from the Q's outlined graphic, restores the bowl's bottom curve and
adds separate closed loop/tapered ribbon paths based on the gameplay reference.
The font file is unmodified; all other bowl/counter segments, seven other glyphs,
authored W, advances/fit, under-title ornament, gradient definitions, canvas and
native placement remain intact. The builder defaults to v004, with explicit
v001/v002/v003 reproduction retained. See `G-Wordmark-v004-PROVENANCE.json`
and `Docs/QA/UI01/G-WORDMARK-SWASH.md`; exact lettering/art gates remain open.

V004's shared-glyph gradients are explicitly mapped to the previous v003
vertical bounds. Removing the Q descender otherwise changes object-bounding-box
gradient coordinates and unintentionally reshades other letters. W and independent
ornament retain the original local gradients. The material correction has a
separate native preflight and is included in the final package evidence.

Check revision v002 preserves v001 and adds curved edge highlights, revised
violet/gold gradients, smaller glints and reduced grey-blue wash. Reproduce with
`python Tools/AssetImport/render_g_check_surface.py --revision v002 --check`;
the default remains v001 so earlier reproduction commands retain their meaning.
Both exports use the same 388x113 canvas and 2x raster size. Unreal imports v002
as a separate `G_CheckReverieV2` texture, preserving `G_CheckReverie` and the
generated surface as ordered fallbacks. See the v002 provenance and
`Docs/QA/UI01/G-CHECK-MATERIAL-REFINEMENT.md`; reference fidelity is not accepted
on the eight-point color diagnostic alone.

Hint surface v001 is a separate editable pearl/gold SVG without baked label or
bulb. Its 287x113 canvas exports at 2x with
`python Tools/AssetImport/render_g_hint_surface.py --check` using the same pinned
development-only renderer. Unreal imports `G_HintReverie` with full UVs and
the existing responsive nine-slice slot. The original generated `G_HintSkin`
and its UV framing remain as fallback, followed by the native live control.
See `G-Hint-Surface-v001-PROVENANCE.json` and
`Docs/QA/UI01/G-HINT-PEARL-SURFACE.md` for hashes, local comparison and gates.
