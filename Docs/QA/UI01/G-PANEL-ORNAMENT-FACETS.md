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

## Final verification in progress

Clean package/native comparison and dedicated read-only review follow. Scope stays
within G UI01. Original-font/wordmark/companion identity, panel/surface material,
full UI01 acceptance, fixture editorial approval, manual/platform accessibility,
Android/physical phone, offline isolation, performance, UI02 motion and original
release gates remain open. Synthetic/offscreen evidence does not pass device gates.
