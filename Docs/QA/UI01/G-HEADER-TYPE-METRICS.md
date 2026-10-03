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

## Final clean package and behavior

Implementation source `2b3893c7adffb4be6e22e8cca48773b11f574f12` was clean throughout
automation, packaging and final captures. Both Unreal Context tests passed at
`20261003-114119-automation-initial` (2 succeeded, none failed/not run/in process,
exit 0, complete evidence). Full Win64 package
`Artifacts/Packages/Win64/20261003-114426-925753` passed, exit 0, complete evidence,
unchanged head/worktree/inputs. Editor packaging check relinked three actions in
14.54s; prior actual source compilation is recorded above. Game source compilation
passed three actions in 69.56s. BuildCookRun took 384.63s, 516 cooked packages,
0 errors/warnings. Low-memory cook diagnostics and lengthy finalization did not
prevent success; no runtime/device performance acceptance is inferred.

All 49 archive payload sizes/hashes match the manifest. Manifest SHA-256:
`ee78c32e31c7cda51546f68d8c906e1126ded5917c94515bb727aad1f69cab77`.
The existing protected firewall task covered this exact new package executable at
11:52:55 UTC, Private/Public LocalSubnet, without new elevation for the refresh.
This is scoped local configuration evidence, not manual Windows dialog inspection.
UnrealPak extraction exits 0; both cooked reading `.ufont` files contain their full
unchanged TTF source at offset 4, with the same cooked hashes recorded in the earlier
reading-font evidence. Staged license bytes match the unmodified source, SHA-256
`93fed46019c38bbe566b479d22148e2e8a1e85ada614accb0211c37b2c61c19b`.
Raw extraction and verification are under `Artifacts/QA/UI01/HeaderType`.

Every final native PNG below was inspected. All 16 runs exit 0, verify the package
hashes, record expected dimensions/clean source identity and pass applicable native
state/cue/reading/focus/layout/text-scaling checks with complete evidence.
No Error/Fatal log lines were found. Paths are under `Artifacts/QA/UI01`; times
are 2026-10-03 UTC. `HeaderType/batch.json` / `verification.json` retain exact
case metadata, applicable checks and PNG hashes.

| Run | Case / dimensions / text / simulated inset |
| --- | --- |
| `20261003-115504-packaged-capture-initial` | Initial, 884x1780, 100% |
| `20261003-115526-packaged-capture-selected` | Selected C, 884x1780, 100% |
| `20261003-115541-packaged-capture-correct` | Correct feedback, 884x1780, 100% |
| `20261003-115555-packaged-capture-wrong` | Wrong feedback, 884x1780, 100% |
| `20261003-115609-packaged-capture-initial` | High resolution, 1768x3560, 100% |
| `20261003-115626-packaged-capture-initial` | Narrow initial, 260x640, 100%, .9 |
| `20261003-115640-packaged-capture-actionfocus` | Narrow action focus, 260x640, 100%, .9 |
| `20261003-115652-packaged-capture-actions` | Enlarged actions, 390x844, 200%, .9 |
| `20261003-115703-packaged-capture-actions` | Landscape actions, 844x390, 200%, .9 |
| `20261003-115715-packaged-capture-hint` | Assisted/disabled feedback, 390x844, 200%, .9 |
| `20261003-115726-packaged-capture-keytab` | Synthetic Tab, 390x844, 100%, .9 |
| `20261003-115738-packaged-capture-keymodal` | Modal/text-toggle focus, 390x844, 200%, .9 |
| `20261003-115749-packaged-capture-keydisabled` | Disabled traversal, 390x844, 100%, .9 |
| `20261003-115801-packaged-capture-keyretry` | Retry focus, 390x844, 200%, .9 |
| `20261003-115812-packaged-capture-longfocus` | Long-label focus, 390x844, 200%, .9 |
| `20261003-115824-packaged-capture-longselectedfocus` | Narrow long selected focus, 260x640, 200%, .9 |

Mode loses decorative spacing at narrow sizes and wraps whole words at 200% where
necessary. Native scrolling, growing feedback and focused controls remain usable
in the applicable cases. Raw 1768x3560 dimensions are verified; the inspection
viewer displayed a resized image. These checks use Windows offscreen rendering
and synthetic input, not manual keyboard, physical touch or assistive services.

## Final reference comparison

Final matched initial PNG SHA-256 is
`d70d52a3d342153af94630b03b897c5516511f1f78d4fd4b26b784efc6cce7f2`, identical
to the preflight image. `HeaderType/metrics.json` reproduces the table above.
Original/baseline hashes remain
`306dae4f6352749edcf1d8edf73f26339a4ba6407b4a394ec50b5898418bedae` and
`911bdcd8c3009b9614b02d54ddc912e24a84db8198e0782c1f72fac72520e220`.
Matched initial RGB comparison changes 4,082 pixels with combined bounds
[250,185,634,636), all inside the separate mode [240,605,645,645) and progress
[395,180,486,220) regions. Zero pixels change outside those glyph/shadow regions;
surrounding initial art and reading geometry match the prior native screen.
This is scoped evidence, not a claim about every responsive state or full fidelity.
Original/baseline/final detail crops and a half-opacity diagnostic overlay were
inspected. All three input images remain unchanged after analysis. Dimensions
and face character improve, while the disclosed center/height/letterform differences
and overall art acceptance remain open.

## Internal review

Dedicated read-only review completed at `Artifacts/Reviews/20261003-120519`,
actual `origin/dev` base `5160d1afbd2c496ac2ee291c68aba4f9e59ff8ca`, reviewed head
`c06263381b01542bfbb727a733c41499e5da6201`. This adds only evidence docs beyond
the tested source. Starting worktree was empty, exit 0, and head/worktree unchanged.
No actionable introduced defects were found. Reviewer confirmed consistent font
sizing/measurement and fallback but did not independently rerun build/runtime
checks; their evidence above is separate. Connector diagnostics did not prevent
the completed review. Subsequent review/publication records change documentation
only. The owner retains the merge decision; this is not art or release acceptance.

## Remaining gates

Fresh local prerequisites
still show no same-engine Android platform receipt and adb lists no device.
Full UI01 art/material/brand/companion identity, editorial approval,
manual/platform accessibility, Android/physical phone, offline isolation,
performance, UI02 motion and original release gates remain open. Offscreen
Windows rendering/synthetic input does not pass manual or physical-device gates.
