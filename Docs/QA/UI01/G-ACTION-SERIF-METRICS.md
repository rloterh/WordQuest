# G action serif metrics

The owner merged PR #32 into `dev` at `3d76c9f` on 2026-10-03, 08:20:47 UTC.
This bounded UI01 correction measures live Hint/Check lettering against the
immutable original G gameplay image. The reference-size packaged baseline is
`Artifacts/QA/UI01/20261003-054319-packaged-capture-initial`.

## Candidate integration

The existing Cormorant action face is already genuine weight 700. This change
addresses its thin/high-contrast letterforms with unmodified Liberation Serif
Bold 2.1.5, also weight 700. This is a licensed candidate, not identification of
the reference's exact font. Archive/file/license provenance and glyph coverage
are in `ArtSource/Fonts/LiberationSerif/PROVENANCE.md`.

Unreal's initialized isolated editor imports a separate `G_ActionBold` FontFace
through `Tools/AssetImport/import_g_action_serif.py`. The helper verifies its
pinned TTF hash, refuses an existing destination, checks FontFace type and save,
and exits its own editor after logging success. Source/imported assets use LFS.
The existing staged Liberation Fonts OFL license is identical to the new adjacent
license; the package does not need a second identical copy.

The transient action composite copies the engine composite and replaces only
Bold, preserving fallback faces/script routing. Only Hint/Check and their disabled
labels use it. Missing candidate falls back to the existing display composite
and its former 34px size, 20px gaps and zero optical top padding;
brand/Pause/reading faces remain. Candidate reference pixel size is 31, with the
existing minimum size, point rounding and 200% enlargement. Icon/label groups
use 26/14 reference-unit Hint/Check gaps and 3 units of optical top padding;
the same gaps are included in wrap measurement. Groups continue to be measured,
wrapped and stacked by existing layout. No fixture,
scoring, artwork, hit-region or focus behavior is intentionally changed.

## Verification in progress

Matched label regions use navy R<65/G<60/B<125 for Hint and white R/G/B>225 for
Check. Original bounds are Hint 59x24 and Check 188x24; baseline bounds are 62x22
and 191x25. These fixed-region threshold diagnostics depend on generated
antialiasing; they are not exact font identity, contrast or global fidelity scores.
Real Editor compilation passed, six actions in 84.49 seconds, exit 0:
`Artifacts/Logs/Build/WordQuestEditor-20261003-083201.log`.
All 66 Python QA tests, six original reference hashes and seven SVG pairs pass.
Genuine import exited 0 with the completion marker, saved FontFace and no errors;
one existing NVIDIA TSR driver warning is unrelated to import. Raw evidence is
`Artifacts/Logs/UI01/action-serif-import.log`, `.json`, `-process.json` and
`-verification.json`. The 371,537-byte asset SHA-256 is
`202014e98b769b50a57d600ae182298db7ab7acf4c958dc0c2f573bbca1537dd`;
its unchanged full 370,096-byte TTF occurs at offset 1385.

Dirty native preflights `20261003-083525-capture-initial` and
`20261003-083921-capture-initial` passed and were inspected. The latter exposed
excessive 6-unit baseline compensation; final compensation is 3. Actual recompiles
passed four actions in 27.95s and 26.20s, respectively, in
`Artifacts/Logs/Build/WordQuestEditor-20261003-083738.log` and `-084129.log`.
Clean packaged comparison follows; no final fidelity claim is based on these drafts.

Missing-candidate omission tests `20261003-084005-capture-initial` (884x1780)
and `20261003-084021-capture-actions` (390x844, simulated .9 inset, 200%) both
exited 0 with complete evidence. The reference-size fallback PNG is RGB-identical
to the prior merged packaged baseline; the enlarged fallback was inspected with
both live labels and Check focus visible. Expected missing FontFace warnings are
recorded, and the temporarily moved new owned asset was restored with its exact
SHA-256 in `Artifacts/QA/UI01/action-serif-fallback.json`. The later 6-to-3 padding
adjustment affects only the candidate branch; fallback still uses zero top padding.
This is an editor omission test, not package corruption or physical-device evidence.

## Clean cooked verification

Clean implementation `4ab90b22f9ba95f50e312471e929c3edec140e70` passed both
Unreal Context tests (2 succeeded, 0 failed/not-run/in-process, exit 0) in
`Artifacts/QA/UI01/20261003-084346-automation-initial`. Full Win64 Development
package `Artifacts/Packages/Win64/20261003-084436-283895` passed the actual Editor
check (3 link/metadata actions, 5.65s), Game compilation (5 actions, 57.56s),
full cook/stage/archive (BuildCookRun 176.95s), exit 0. Cook reported 0 errors and
0 warnings. Source head/worktree/recorded inputs remained unchanged.
All 49 archive payload hashes verify; manifest SHA-256 is
`e3feabd0a5feb38bf293f6d709d769e7e028cecb3bf7b14715d5f69fac062d43`.
The already-installed optional firewall task automatically covered this archive's
exact executable path at 08:47:53 UTC, without another UAC prompt.

UnrealPak extraction of `G_ActionBold.ufont` passed with `-Extract <directory>`.
Its 370,104 bytes contain the exact original TTF at offset 4, between a font array
length and the empty geometry-array count. Cooked SHA-256:
`5af19fb5f8d7eb14bc963796633414ca1a12a6f7ffefbefbf0a3b78715fadc19`.
Every packaged native log confirms loading this cooked resource. The adjacent
source license and existing staged Liberation Fonts license are byte-identical;
both TTF/FontFace LFS pointers match actual files. Raw extraction/verification:
`Artifacts/QA/UI01/action-serif-extract.log`, `verify-action-serif-package.py`
and `action-serif-package-verification.json`.

All 15 final packaged captures use that clean implementation and verified archive.
Each exited 0, passed applicable state/cue/content-fit/reading/focus checks, recorded
correct PNG dimensions and complete evidence, with no Error/Fatal log messages.
Every PNG was inspected directly; these are native offscreen/synthetic checks.
Runs under `Artifacts/QA/UI01`:

| Run | Window | Inspected state |
| --- | --- | --- |
| `20261003-084848-packaged-capture-initial` | 884x1780 | Normal live labels, original comparison |
| `20261003-084900-packaged-capture-selected` | 884x1780 | Selected C, active labels |
| `20261003-084910-packaged-capture-correct` | 884x1780 | Correct A, disabled Answer checked |
| `20261003-084919-packaged-capture-wrong` | 884x1780 | Wrong B, disabled Answer checked |
| `20261003-084929-packaged-capture-initial` | 1768x3560 | Matching composition at 2x window size |
| `20261003-084939-packaged-capture-initial` | 260x640 | Narrow 100% reflow; Check below viewport |
| `20261003-084949-packaged-capture-actionfocus` | 260x640 | Stacked 100% groups, Check focus |
| `20261003-084958-packaged-capture-actions` | 390x844 | Stacked 200% groups, Check focus |
| `20261003-085008-packaged-capture-actions` | 844x390 | Landscape 200% groups, Check focus |
| `20261003-085018-packaged-capture-hint` | 390x844 | Assisted correct A, 200% disabled labels wrap |
| `20261003-085028-packaged-capture-keytab` | 390x844 | Routed control cycle, final Hint focus |
| `20261003-085038-packaged-capture-keymodal` | 390x844 | Pause, focused 200% text setting |
| `20261003-085048-packaged-capture-keydisabled` | 390x844 | Disabled actions skipped, Pause focus |
| `20261003-085058-packaged-capture-keyretry` | 390x844 | Routed retry, 200% selected A focus |
| `20261003-085108-packaged-capture-longfocus` | 390x844 | 200% long draft option, focused B |

All non-reference windows use simulated .9 safe-area insets; no phone safe-area
claim is made. Batch/check records are `action-serif-batch.py`, `.json` and
`action-serif-capture-verification.json`. Python QA remains 66 passing tests;
original six references and seven SVG source/runtime pairs remain unchanged.

## Final matched-size comparison

Original/native/baseline PNG hashes, fixed regions/thresholds and read-only
diagnostics are in `Artifacts/QA/UI01/action-serif-analysis.py` / `.json`.
The native final is `20261003-084848-packaged-capture-initial/native.png`, SHA-256
`d80f534ef44150269ba66dee071fc391e163ed8f4efddb7c49889986cd71c801`.
Side-by-side details and the 50% overlay were inspected.

| Diagnostic | Original | Prior native | Candidate native |
| --- | --- | --- | --- |
| Hint core bounds | 59x24 | 62x22 | 59x21 |
| Check core bounds | 188x24 | 191x25 | 184x22 |
| Hint core pixel count | 450 | 363 | 457 |
| Check core pixel count | 980 | 786 | 985 |
| Hint core center | 275.5, 1511 | 272, 1507 | 275.5, 1510.5 |
| Check core center | 624, 1511 | 627.5, 1505.5 | 624, 1510 |

The stronger letterforms and centers are closer; Hint width matches this threshold,
while Check is 4px narrower and both labels remain shorter. This is not an
improvement in every metric or accepted exact lettering. Core counts describe
thresholded rendered stroke coverage, not a contrast or fidelity score.
All 4,214 changed RGB pixels are inside the two documented live-label regions
(difference bounds x239..724/y1487..1529, half-open); zero changes occur outside
them. Icons, skins, reading panel and backdrop pixels are identical in this
matched initial comparison. All input PNG hashes remain unchanged. No raster
source editing or new contrast certification is claimed.

Fresh prerequisites still show missing engine Android target support and no adb
device. The existing Android handoff remains applicable.

## Remaining gates

The panel rim/star, companion identity, wordmark and generated surface materials
remain unfinished. Exact art/font fidelity, editorial fixture approval, manual
input/accessibility, Android support and phone evidence, offline isolation,
performance, UI02 motion and release acceptance remain open. Native offscreen
captures and synthetic input do not establish these gates.
