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
| `G-Header-Divider-v001.svg` | `Game/Content/UI/G/Vector/G_HeaderDivider.svg` | 214x29 viewBox; tapered short gold lines, diamond terminals and faceted central star |
| `G-Reading-Divider-v001.svg` | `Game/Content/UI/G/Vector/G_ReadingDivider.svg` | 314x29 viewBox; longer matching lines and central star |
| `G-Pause-Bars-v001.svg` | `Game/Content/UI/G/Vector/G_PauseBars.svg` | 24x30 viewBox; two white rounded bars, runtime tint follows skin availability |

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
retained; it now checks all five masters/runtime copies.

No rights clearance beyond supplied-reference provenance is established. Release
clearance and faithful-art acceptance remain open.
