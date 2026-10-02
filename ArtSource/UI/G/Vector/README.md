# G vector icon and divider candidates

These are hand-authored editable SVG reconstructions informed by the immutable
G Celestial Reverie gameplay reference. They are not exact original-pixel
extractions or accepted production art. No image generation or raster editing
was used for this increment. Reference composition and icon identity are the
targets; shape, faceting and lighting still require visual acceptance.

| Editable master | Runtime resource | Geometry |
| --- | --- | --- |
| `G-Hint-Bulb-v001.svg` | `Game/Content/UI/G/Vector/G_HintBulb.svg` | 40x56 viewBox; rounded navy bulb outline and two base bars |
| `G-Check-Star-v001.svg` | `Game/Content/UI/G/Vector/G_CheckStar.svg` | 48x48 viewBox; curved four-point gold star with white/lilac facets |
| `G-Header-Divider-v002.svg` | `Game/Content/UI/G/Vector/G_HeaderDivider.svg` | 214x29 viewBox; preserved tapered lines/terminals/star with gold gradients and ivory facets |
| `G-Reading-Divider-v002.svg` | `Game/Content/UI/G/Vector/G_ReadingDivider.svg` | 314x29 viewBox; matching long divider with the same material treatment |
| `G-Pause-Bars-v001.svg` | `Game/Content/UI/G/Vector/G_PauseBars.svg` | 24x30 viewBox; two white rounded bars, runtime tint follows skin availability |
| `G-Wordmark-v004.svg` | `Game/Content/UI/G/Vector/G_Wordmark.svg` | 430x140 viewBox; authored W, adapted Q bowl/looped swash, seven other licensed outlines and retained ivory/gold ornament |
| `G-Answer-Badge-v001.svg` | `Game/Content/UI/G/Vector/G_AnswerBadge.svg` | 70x70 viewBox; lilac shaded disc and pale rim, with no baked letter |

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

The wordmark's remaining eight letters outline the repository's unmodified
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
python Tools/AssetImport/build_g_wordmark.py --revision v003
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
placement are preserved. The builder defaults to v003; explicit v001/v002 options
reproduce the older revisions. See `G-Wordmark-v003-PROVENANCE.json` and
`Docs/QA/UI01/G-WORDMARK-CAPITAL.md` for verification and remaining limitations.
No raster edit, new font or original-lettering acceptance is claimed.

No rights clearance beyond supplied-reference provenance is established. Release
clearance and faithful-art acceptance remain open.

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
