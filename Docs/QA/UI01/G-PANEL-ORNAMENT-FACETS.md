# G panel ornament facet candidate

Owner-merged PR #34 (`58b21fa`, 2026-10-03 10:32:21 UTC) separates the small lilac
star from the reading panel. This bounded UI01 correction refines that ornament's
directional material against the immutable original: the reference has violet
upper-left/lower-right faces, a pale upper-right face, warmer lower-left bevel
and small luminous center. V001's pale upper-left face and continuous light cross
were a visible difference in the inspected reference-size rendering.

Editable `ArtSource/UI/G/Vector/G-Panel-Star-v002.svg` preserves the 36x42 canvas,
viewBox, outer path coordinates and .8-unit stroke width. Gradients, directional
facets and a compact center glint replace the old cross. Earlier v001 is unchanged.
The staging helper copies v002 byte-identically to the existing `G_PanelStar.svg`;
eight SVG pairs are still checked. An LF attribute preserves this new master.
Adjacent provenance pins the source/runtime hash, preserved master and original.
No raster generation/editing, source-pixel extraction, new binary, C++, native
placement/size, texture, fonts, learning content, scoring or motion change occurs.
Decoration remains hit-test invisible and excluded from assistive labels;
existing missing-SVG omission and old-panel fallback paths are unchanged.

## Preliminary verification

Editor target check `Artifacts/Logs/Build/WordQuestEditor-20261003-103611.log`
passes, exit 0, up to date, zero actions, 5.64s. This is not a fresh compilation.
Dirty native `20261003-103618-capture-initial` exits 0 with expected 884x1780
dimensions, initial state/cue checks and complete evidence. Its full PNG and
enlarged ornament crop were inspected alongside original and previous packaged
native baseline (`20261003-100205-packaged-capture-initial`). Facet direction
and center highlight improve those specific differences; exact shape, bevel,
blur/lighting and complete visual fidelity remain unapproved.
All 66 Python QA tests (0.473s), eight SVG pairs and six supplied reference hashes
pass. Git LFS 3.7.1 is available; no new binary asset is introduced.

## Final clean verification

Implementation source is `ad9a86a0cecee8842257ab67557ead5817438afc`, clean during
package, captures and automation. Full Win64 BuildCookRun succeeds, exit 0,
107.39s, 516 cooked packages, 0 errors/warnings, at
`Artifacts/Packages/Win64/20261003-104033-344173`. Editor and Game target checks
are up to date, zero actions, 2.19s and 2.05s respectively; no fresh compilation
is claimed for this art-only change. Head/worktree/input invariants pass.
All 49 archived payloads match manifest sizes/hashes. Manifest SHA-256:
`cb0fef9ea7229b8534e5f23ea4b46980760f0003361782a7243ba2a00281a939`.

UnrealPak extraction exits 0. Packaged `G_PanelStar.svg` exactly matches master
and runtime, SHA-256
`f48cc9ea9c8e6f75eb63b508b7c931e5c700efe49506af8802b6f54c560f5fb5`.
Raw extraction/verification is under `Artifacts/QA/UI01/PanelStar`.
The existing protected firewall task covers this exact package executable at
10:42:40 UTC, Private/Public LocalSubnet, without new elevation. This is a
successful scoped refresh, not manual OS dialog verification.
Both existing Unreal Context tests pass at `20261003-104618-automation-initial`
(2 succeeded, none failed/not run/in process, exit 0, complete evidence).
All 66 Python QA tests, eight SVG pairs and original reference hashes pass.

All nine final native PNGs below were inspected. Each records source above,
empty worktree, matching package identity/hash verification, exit 0, expected
dimensions and passing applicable state/cue/focus/layout evidence. No Error/Fatal
log lines were found. Runs are under `Artifacts/QA/UI01`; timestamps are UTC.
`PanelStar/batch.json` and `PanelStar/verification.json` record cases, PNG hashes,
archive verification and the scoped comparison.

| Run on 2026-10-03 | Case / dimensions / text / simulated inset |
| --- | --- |
| `20261003-104348-packaged-capture-initial` | Initial, 884x1780, 100% |
| `20261003-104400-packaged-capture-selected` | Selected C, 884x1780, 100% |
| `20261003-104411-packaged-capture-correct` | Correct feedback, 884x1780, 100% |
| `20261003-104421-packaged-capture-initial` | High resolution, 1768x3560, 100% |
| `20261003-104432-packaged-capture-initial` | Narrow initial, 260x640, 100%, .9 |
| `20261003-104442-packaged-capture-large` | Enlarged initial, 390x844, 200%, .9 |
| `20261003-104452-packaged-capture-initial` | Landscape initial, 844x390, 100%, .9 |
| `20261003-104502-packaged-capture-actions` | Landscape actions, 844x390, 200%, .9 |
| `20261003-104512-packaged-capture-keymodal` | Synthetic modal/text toggle focus, 390x844, 200%, .9 |

The star renders separately at native/reference, narrow and landscape scales;
enlarged text keeps its independent decoration size. Tall content scrolls and
controls/modal focus remain visible in applicable checks. The raw high-resolution
dimensions were verified; the viewer displayed a resized image.

## Native reference comparison

Matched initial final PNG SHA-256 is
`911bdcd8c3009b9614b02d54ddc912e24a84db8198e0782c1f72fac72520e220`.
Prior merged PR #34 baseline hash is
`a6a95b4dff7f971f19fabfe353b7b6f7489911b1b3eb4fed2b7ef3c16df27086`.
The immutable original hash remains
`306dae4f6352749edcf1d8edf73f26339a4ba6407b4a394ec50b5898418bedae`.
Read-only RGB comparison changes 376 pixels, bounds [425,553,459,589), with
zero changes outside ornament region [423,549,461,593). This scoped initial
comparison establishes unchanged surrounding rendering, not universal fidelity.
All three input files remain byte-identical after analysis. Original/baseline/final
enlarged ornament crops and a diagnostic half-opacity overlay were inspected.
The reference's face direction and small center glint are better represented;
the reference has a broader/softer bevel and different highlight/contour finish,
which remain open. No overall pixel score is used as acceptance.

## Remaining gates

Dedicated read-only review against actual `dev` follows. Same-engine Android
platform receipt is still absent and adb lists no device (fresh local check).
Scope stays within G UI01. Original-font/wordmark/companion identity, panel/surface material,
full UI01 acceptance, fixture editorial approval, manual/platform accessibility,
Android/physical phone, offline isolation, performance, UI02 motion and original
release gates remain open. Synthetic/offscreen evidence does not pass device gates.
