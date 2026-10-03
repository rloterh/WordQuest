# G live mode and progress typography candidate

The owner merged PR #35 (`5160d1a`, 2026-10-03 11:20:09 UTC). This bounded UI01
correction tests the existing licensed Liberation Sans 2.1.5 reading composite
for live `Context Detective` and `3 / 7` labels against the immutable G original.
No new font, asset, license, raster or SVG revision is introduced. Existing
Regular/Bold FontFaces, composite script/fallback routing and package license
remain unchanged; see `G-READING-FONT-METRICS.md` for their provenance/import.
The counter still shows draft fixture progress, not persisted campaign progress.

## Native integration

Mode uses the genuine Bold face at 25 reference pixels when the reading composite
is available; prior default Regular at 28 pixels remains the missing-composite
fallback. Measurement and the initial fit check use the same font/size/weight.
Its 14-pixel normal readability floor is applied before existing 200% enlargement
and point rounding. Spaced lettering is still dropped when it does not fit; the
plain words can wrap, and the existing 40-unit minimum block remains. Normal
reference text fits that block, preserving downstream reading anchors.
Progress uses the same genuine Bold composite at its existing 35-pixel size,
with prior default Bold when unavailable. Existing white/shadow colors, measured
vertical centering, plaque, compact-landscape visibility and draft string remain.
All other live text, scoring, controls, scrolling, focus and motion are unchanged.

## Preliminary verification

Actual Editor compilation passes four actions, 105.52s, exit 0:
`Artifacts/Logs/Build/WordQuestEditor-20261003-112723.log`.
Dirty native `20261003-113030-capture-initial` passes initial state/cue/dimension
checks at 884x1780, complete evidence and exit 0. Full PNG and diagnostic crops
were inspected against original and prior merged packaged baseline
`20261003-104348-packaged-capture-initial`. Shutdown waited for derived-data cache
writes and then exited normally; this is not runtime performance qualification.
All 66 Python QA tests (0.852s), eight SVG pairs and six reference hashes pass.
Git LFS 3.7.1 is available; no binary files change.

`Artifacts/QA/UI01/HeaderType/preflight-metrics.json` records fixed-region threshold
glyph extents. Mode uses R<65/G<60/B<125 in [200,600,685,645); progress uses
R/G/B>210 in [385,183,500,215). These bounds measure visible threshold pixels,
not exact font identity or complete visual acceptance.

| Label | Original width x height / center | Prior native | Candidate |
| --- | --- | --- | --- |
| Mode | 375x17 / (442.5,625.5) | 382x20 / (442,626) | 376x17 / (441,625.5) |
| Progress | 63x27 / (441.5,199.5) | 68x27 / (441,198.5) | 66x26 / (441,200) |

Mode dimensions and heavier strokes are closer; its horizontal threshold center
is 1.5 pixels left of the original. Progress width/vertical center are closer,
but its glyphs are one pixel shorter. Exact letterforms, kerning, antialiasing,
color/shadow and reference-font identity remain unapproved.

## Missing-font fallback

The owned reading Bold asset was temporarily moved within the workspace and
restored in `finally`, byte-identically with SHA-256
`ddb17ec624e8c6e8d68b607cbbd14e5302111b07e158074cc101e69de0a78715`.
`HeaderType/fallback.json` records the restoration and complete exit-0 runs:
`20261003-113737-capture-initial` (884x1780) and `20261003-113838-capture-actions`
(390x844, simulated .9 inset, 200%). Both PNGs were inspected. Initial mode and
progress crops are RGB-identical to the merged PR #35 native baseline. Other
reading roles use the existing default-family fallback, so whole-screen equality
is not claimed. Missing-package warnings and temporary deletion metadata are
expected. This is an editor omission check, not packaged corruption or device proof.

## Verification in progress and remaining gates

Responsive/native, clean package comparison and dedicated read-only review follow.
Full UI01 art/material/brand/companion identity, editorial approval,
manual/platform accessibility, Android/physical phone, offline isolation,
performance, UI02 motion and original release gates remain open. Offscreen
Windows rendering/synthetic input does not pass manual or physical-device gates.
