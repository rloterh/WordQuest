# G Hint pearl surface

This bounded UI01 correction addresses the Hint surface's colder face and flatter
rim/gloss versus the immutable G gameplay reference. The owner reports a merge,
but GitHub still reports PR #49 open and `dev` at `e931166` on the latest
2026-10-06 check. This branch starts from its tested head `3dc14ea`. The actual
review/publication base and dependency will be recorded honestly; no agent merge.

## Editable source and native integration

`ArtSource/UI/G/Vector/G-Hint-Surface-v001.svg` is a hand-authored 287x113 pearl/
lilac surface with curved edge light, layered warm gold and restrained reflection/
glint paths. It contains no baked label/bulb and no extracted original pixels.
The development-only pinned resvg-py 0.5.0 / resvg 0.48.1 renderer exports 574x226
RGBA to `ArtSource/UI/G/Exports/G-Hint-Surface-v001.png`. Reproduction:

```powershell
python Tools/AssetImport/render_g_hint_surface.py --check
```

Unreal's texture commandlet runs `Tools/AssetImport/import_g_hint_surface.py`,
which pins the inspected export and creates genuine `/Game/UI/G/G_HintReverie`
with sRGB UI compression/group, bilinear filtering and no mips/streaming. Final
import log `Artifacts/Logs/UI01/hint-surface-final-import.log` records
`WORDQUEST_HINT_SURFACE_IMPORT_COMPLETE`, success, zero errors/warnings and
574x226 dimensions. Import report is `hint-surface-import.json` beside that log.
Master/export/asset hashes and preserved fallback ownership/settings are in
`ArtSource/UI/G/Vector/G-Hint-Surface-v001-PROVENANCE.json`.

Native decoration prefers the authored full-UV texture, then existing generated
`G_HintSkin` with its previous framed UVs, then native fill/outline. Existing
horizontal .195/vertical .45 nine-slice margins, responsive slot and texture-sized
drawing are preserved. Decorative hit-test/accessibility settings, live label/
bulb, enabled tint, native hover/press/focus, control geometry, text parameters,
draft fixtures and learning/input handlers retain their behavior. Git LFS 3.7.1,
its process filter and PNG/uasset attributes were verified before binary commit.
Old art and all supplied planning/reference bytes remain unchanged.

## Comparison and Editor evidence

The same eight opaque-face points are fixed before drawing:
(143,1479), (240,1479), (340,1479), (125,1513), (360,1513), (140,1540),
(240,1540), (338,1540). Baseline is PR #49's clean packaged
`20261006-213041-packaged-capture-initial` at 884x1780/100%. QA samples, crops and
50% overlay remain ignored under `Artifacts/QA/UI01/HintSurface20261006/`;
they never become product assets. Original G SHA-256 remains
`306dae4f6352749edcf1d8edf73f26339a4ba6407b4a394ec50b5898418bedae`.

Real Editor build `WordQuestEditor-20261006-215119.log` passes in 32.23s. First
dirty preflight `20261006-215152-capture-initial` passes and is inspected; its
eight-point color error improves 11.7083 to 5.4167, but the rim appears too flat.
Final source adds an inner pearl lip/gold crest and adjusts lower pearl tones.
Genuine reimport and final preflight `20261006-215618-capture-initial` pass.
Its same-point mean absolute channel error is 3.0833 versus baseline 11.7083;
individual channels do not all improve. Exactly 29,714 Hint-region pixels change,
with zero outside except known 964 Editor/package Pause/plaque pixels at maximum
channel delta one. Crops and overlay were inspected; complete package comparison
follows separately. Art-only final edits require reimport/capture, not a repeated
C++ build; runtime source remains the built integration.

The new surface is more editable and these local colors are closer. Gold/bevel,
painted reflection detail, shadow/fringe and live type/placement remain different.
The normal action row is still a few pixels above the original; this material
increment preserves its geometry. The local sample statistic is neither a
whole-material metric nor full UI01 acceptance.

All 96 Python QA tests pass in 0.473s, with log in this ignored evidence folder.
Six immutable reference hash/dimension checks, ten staged SVG parity pairs and
byte-identical Hint export reproduction pass. No new synthetic tests mirror the
reversible art integration; native state/input/resize/fallback checks are required.

## Missing-art checks

All four deliberate missing-art Editor runs below pass with native/helper exit
zero and complete state/cue evidence. Held Hint captures also pass ordered pointer/
hover/capture, actual 200% text, action-content fit and teardown cancellation:
pressing does not consume a hint or evaluate an answer. Every PNG was inspected.
Only the two owned assets are moved to a verified ignored holding directory and
restored in `finally`; both hashes match provenance. No asset deletion/substitution.

| Fallback | Initial 884x1780/100% | Held Hint 260x640/200%, safe .9 |
|---|---|---|
| Generated, authored absent | `20261006-215841-capture-initial` | `20261006-215859-capture-pointerhintpress` |
| Native, both textures absent | `20261006-215919-capture-initial` | `20261006-215938-capture-pointerhintpress` |

Generated initial is exactly RGB-identical to prior Editor baseline
`20261006-140159-capture-initial`. Native fill preserves the separate live bulb,
Hint label and interactive press outline. Raw summary is
`Artifacts/QA/UI01/HintSurface20261006/fallback.json`. These dirty-source missing-
optional-art tests are not corrupt-package or phone evidence. Clean Win64 package,
native control states, Unreal automation and dedicated review remain in progress.

Full UI01 type/art/material fidelity, UI02 motion, manual/platform accessibility,
draft fixture editorial approval, Android/phone, isolated offline, performance and
original release gates remain open. No later milestone, deployment or release;
the owner retains merge decisions.
