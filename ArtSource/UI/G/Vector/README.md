# G action icon candidates

These are hand-authored editable SVG reconstructions informed by the immutable
G Celestial Reverie gameplay reference. They are not exact original-pixel
extractions or accepted production art. No image generation or raster editing
was used for this increment. Reference composition and icon identity are the
targets; shape, faceting and lighting still require visual acceptance.

| Editable master | Runtime resource | Geometry |
| --- | --- | --- |
| `G-Hint-Bulb-v001.svg` | `Game/Content/UI/G/Vector/G_HintBulb.svg` | 40x56 viewBox; rounded navy bulb outline and two base bars |
| `G-Check-Star-v001.svg` | `Game/Content/UI/G/Vector/G_CheckStar.svg` | 48x48 viewBox; curved four-point gold star with white/lilac facets |

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
keeps the icon separate from its live button label. Missing resources collapse
the icon and its spacing. `DefaultGame.ini` declares the vector directory for UFS
staging, but a packaged build has not verified that path. Native desktop evidence
and remaining gates are in `Docs/QA/UI01/G-ACTION-ICONS.md`.

No rights clearance beyond supplied-reference provenance is established. Release
clearance and faithful-art acceptance remain open.
