# G authored reading-panel candidate

The owner merged PR #33 into `dev` at `373de75` on 2026-10-03, 09:20:43 UTC.
This bounded UI01 correction addresses the generated panel's bright/thick rim,
high shoulders, oversized star and outer fringe. The immutable original remains
the visual target. Its reference-size prior packaged native baseline is
`Artifacts/QA/UI01/20261003-084848-packaged-capture-initial`.

## Attempt and authored candidate

A built-in imagegen edit using the preserved panel v002 and original gameplay
reference was rejected: the outer fringe remained and the star stayed too large.
It was not imported. The exact prompt, output hash and disposition are recorded
in `ArtSource/UI/G/Reconstruction/G-Panel-v003-ATTEMPT.md`. No CLI/API fallback,
raster paintover or replacement of supplied references was used.

The subsequent authored `ArtSource/UI/G/Vector/G-Reading-Panel-v001.svg` contains
an editable contour, narrow pale champagne/ivory rim, restrained inner shading,
pearl/lilac gradients, subtle fixed-seed grain and local soft shadow. It contains
no text, dividers, controls or star. Its simplified surface is a candidate; it
does not reproduce every painterly detail or accept exact fidelity.
The separate `G-Panel-Star-v001.svg` is a small subdued lilac four-point ornament,
staged byte-identically as `Game/Content/UI/G/Vector/G_PanelStar.svg`.

Pinned development-only resvg-py 0.5.0 / resvg 0.48.1 renders the blank panel at
1.5x (1185x1710 RGBA). `render_g_reading_panel.py --check` reproduces it without
writing. Ordinary builds use checked-in export/Unreal assets without this renderer.
The full-size BGRA8 surface is approximately 7.73 MiB before engine bookkeeping,
versus about 6 MiB for the old source dimensions; this is a source-size calculation,
not measured GPU memory or phone performance. Earlier PNG/Unreal assets are preserved.

Unreal's actual texture commandlet imports a separate `G_ReadingPanel` with
sRGB/UI compression/group, bilinear filtering, no mips and no streaming. The helper
checks the pinned export hash, imported Texture2D type and successful save.
Both new PNG and genuine Unreal texture use configured LFS.

## Native integration

The logical panel is 790x1140. Fixed top/bottom cuts at 220/1010 preserve arch and
corners; only the body stretches as long/enlarged text or feedback grows. The
lower corner curves start exactly at the 1010 cut. Native placement retains the
existing 220/130 reference-unit top/bottom heights, panel bounds and 80-unit lower
padding. The separate 36x42 star occupies x424/y550 at the reference size and
scales with composition; it remains decorative and hit-test invisible.
Missing authored texture selects the preserved old texture and its original UV
cuts, and collapses the separate star to avoid a duplicate legacy ornament.
Missing star SVG omits only decoration. Reading text, actions, scoring, focus,
scrolling and draft fixture remain independent of this artwork.

## Import and fallback checks

Actual Editor compilation passed six actions in 78.95s, exit 0:
`Artifacts/Logs/Build/WordQuestEditor-20261003-094236.log`.
Dirty native preflight `20261003-094445-capture-initial` exited 0 with complete
dimension/state/cue evidence and was compared directly with the original. Its
thin rim, shoulder contour and smaller separate star are closer in those respects;
the surface remains simpler/flatter and final material acceptance is open.
The final source moves the start of the lower curves to the exact fixed-slice
boundary; final import/package evidence is recorded below. All 66 Python QA tests and the
six original reference hashes pass; runtime SVG parity now checks eight pairs.

Final authored import exited 0, reporting 0 errors/warnings and its completion
marker in `Artifacts/Logs/UI01/reading-panel-import-final.log`. Its report is
`Artifacts/Logs/UI01/reading-panel-import.json`.
Export SHA-256 is `b179748f71d1977d1df26f0f7985418e867d94e0ac8d8f270fbe2981e8bfa734`;
the genuine saved asset is 557,502 bytes, SHA-256
`337cb0d335db5076c8bf69b4f2c351eea4ec461822780d1bfef14d9eee6aa5ac`.
The earlier preflight used the preliminary lower-curve start and export; it is
not final cooked evidence. Final source/export hashes are in adjacent provenance.

Missing-texture runs `20261003-095327-capture-initial` (884x1780) and
`20261003-095349-capture-actions` (390x844, simulated .9 inset, 200%) exited 0
with complete applicable native evidence. Initial fallback is RGB-identical to
the merged PR #33 packaged baseline; enlarged actions/focus were inspected.
The new owned texture was temporarily moved, then restored with its exact hash
in `reading-panel-fallback.json`. Its missing-package warnings are expected.
This is an editor omission test; it does not corrupt or qualify a packaged game.

Final `reading-panel-alpha-final.json` records RGBA dimensions 1185x1710, alpha
range 0–255, nonzero bounds [17,21,1168,1677), and transparent four corners.
Each row at alpha >=128 has no internal split/hole. These are scoped contour
checks, not a claim about every alpha threshold or final material fidelity.
The final PNG reproduces exactly, both LFS pointer hashes match their actual
files, eight SVG source/runtime pairs match, and all six original reference
hashes remain unchanged.

## Final clean build and package

Source `38cbc1c33b13ea8ef8f232828cc013a7c3871ba6` was clean throughout both
Unreal Context tests (`20261003-095603-automation-initial`: 2 succeeded, none
failed/not run/in process), full packaging and the final captures.
`Artifacts/Packages/Win64/20261003-095701-943554/run.json` records Editor check
exit 0 (up to date, 2.19s), actual Game compilation (five actions, 52.41s),
and successful BuildCookRun (199.15s, 516 cooked packages, 0 errors/warnings).
The earlier six-action Editor compilation is the actual rebuild evidence.
Cook reported low available physical memory and continued successfully; this
does not establish acceptable runtime/device performance.

The cook log records `G_ReadingPanel` as BGRA8, 1185x1710, one mip. The packaged
native screen visibly uses the authored panel and separate star. UnrealPak
extraction of `G_PanelStar.svg` matches its source bytes exactly, SHA-256
`6e5ff094cfb2493f310f3d078253f846817b391c2c175b57aa89dfed4cb95ad2`.
All 49 archive payload hashes match the package manifest; manifest SHA-256 is
`4573a9b70fb06066bab4960e9c9a8e810a8e5be8b2a57ea0ba81e1a7f1220bad`.
Head, worktree and recorded input invariants passed. The existing protected
firewall task automatically covered this exact new executable at 10:00:42 UTC,
Private/Public LocalSubnet; no new elevation prompt was needed for the refresh.
This does not claim a manual Windows dialog inspection or change firewall policy.

## Final packaged rendering and behavior

All 16 native PNGs below were inspected. Every run exited 0, recorded expected
dimensions, passed applicable native state/cue/focus/layout checks, verified
the package hashes, and has complete evidence at the clean source above.
No Error/Fatal log lines were found. Runs are under `Artifacts/QA/UI01`; all
timestamps are 2026-10-03 UTC. `authored-panel-capture-verification.json`
records each PNG hash and applicable checks.

| Run | Case | Dimensions / text / simulated inset |
| --- | --- | --- |
| `20261003-100205-packaged-capture-initial` | Initial | 884x1780, 100% |
| `20261003-100218-packaged-capture-selected` | Selected C | 884x1780, 100% |
| `20261003-100229-packaged-capture-correct` | Correct feedback | 884x1780, 100% |
| `20261003-100239-packaged-capture-wrong` | Wrong feedback | 884x1780, 100% |
| `20261003-100249-packaged-capture-initial` | High resolution | 1768x3560, 100% |
| `20261003-100301-packaged-capture-initial` | Narrow initial | 260x640, 100%, .9 |
| `20261003-100312-packaged-capture-actionfocus` | Narrow action focus | 260x640, 100%, .9 |
| `20261003-100323-packaged-capture-actions` | Enlarged actions | 390x844, 200%, .9 |
| `20261003-100334-packaged-capture-actions` | Landscape actions | 844x390, 200%, .9 |
| `20261003-100344-packaged-capture-hint` | Assisted/disabled feedback | 390x844, 200%, .9 |
| `20261003-100355-packaged-capture-keytab` | Synthetic Tab | 390x844, 100%, .9 |
| `20261003-100406-packaged-capture-keymodal` | Modal focus/text toggle | 390x844, 200%, .9 |
| `20261003-100417-packaged-capture-keydisabled` | Disabled traversal | 390x844, 100%, .9 |
| `20261003-100429-packaged-capture-keyretry` | Retry focus | 390x844, 200%, .9 |
| `20261003-100440-packaged-capture-longfocus` | Long-label focus | 390x844, 200%, .9 |
| `20261003-100450-packaged-capture-longselectedfocus` | Narrow long selected focus | 260x640, 200%, .9 |

Portrait/landscape actions and growing feedback remain inside the panel; scroll
clipping and visible focus are expected for tall content. Top arch and lower
corners keep their fixed slice heights. The 1768x3560 raw dimensions are verified
in metadata; the inspection viewer displayed a resized image.
These are offscreen Windows captures and synthetic input, not manual keyboard,
physical touch, assistive-service or Android evidence.

## Reference comparison and limits

`authored-panel-analysis.json` pins the immutable original, prior PR #33 native
baseline and final initial PNG (`a6a95b4dff7f971f19fabfe353b7b6f7489911b1b3eb4fed2b7ef3c16df27086`).
Matched initial rendering changes 469,487 RGB pixels within [47,509,836,1644),
with zero changes outside the panel region [47,509,837,1650). This is a composited
region check, not a claim that only raw skin pixels change.
Nine sampled normal reading backgrounds against opaque ink RGB(24,20,83) have
minimum contrast 12.87:1. This does not qualify all states, antialiased glyphs,
disabled controls or platform accessibility.

Inspected top/bottom crops compare original, baseline and final rendering directly;
the half-opacity overlay is diagnostic only. The finer, quieter rim, lower
shoulder contour and smaller lilac star improve those specific differences.
The surface remains flatter/simpler, the star facets differ, and exact outline,
material and whole-screen identity are not accepted. Earlier sources remain
available for comparison/fallback.

## Remaining gates

The same UE 5.8 Android platform receipt is still absent and adb lists no device.
Android Studio alone does not supply that missing engine platform support.
Original-font/wordmark/companion identity, panel/surface finish and full UI01 art
acceptance remain open. Fixture editorial approval, manual/platform accessibility,
Android tooling/physical phone, offline isolation, performance, UI02 motion and
release gates remain. Native offscreen/synthetic proof is not physical-device evidence.
