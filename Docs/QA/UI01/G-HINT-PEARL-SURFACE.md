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
native control states, Unreal automation and dedicated review are recorded below.

## Storage failure and recovery

Clean source `a877a5c5479cbb2b7193f019267f744a315a980e` first attempts archive
`20261006-220235-677524`. C++ build passes, but cook fails with Zen oplog creation
HTTP 507 Insufficient Storage and UAT exit 25. Its retained manifest correctly
marks evidence incomplete; no package/runtime acceptance is claimed for it.
C: has about 2.1GB free during diagnosis, near/below Zen's existing low-space
threshold. The failure log/manifest remain in that run; copied helper output
is `failed-first-package-helper.log` in the ignored Hint evidence folder.

Automatic approval review rejects removing ten redundant staging directories,
with the message "blocked by policy" and no more detailed reason. No directory
is deleted. Instead native `compact.exe /C /EXE:LZX` losslessly compresses only
the EXE/PDB pairs in ten older successful staging copies. Exact workspace paths
and both staged/archived binaries are checked against recorded manifests before
compression; all 20 staged hashes remain identical afterward. Archived builds,
manifests, captures, source assets and machine security policy are preserved.
Free space rises from 2,303,156,224 to 7,005,872,128 bytes, about 4.7GB recovered.
Raw file paths/hashes are in `stage-compression.json` in the ignored evidence
folder. This scoped local recovery is not a new repository cleanup policy.
Retry uses the same clean commit without runtime/source/config changes.

## Clean packaged verification

Archive `Artifacts/Packages/Win64/20261006-222520-298494/` passes Win64 Development
BuildCookRun in 144.92s, full cook 522 packages with zero errors/warnings.
Its complete manifest records tested head `a877a5c`, clean starting worktree,
unchanged head/worktree/inputs and SHA-256
`252e524a9942bde70f441e20944c1bceb067575b55a0ca1d834b702eaf7d68db`.
All 49 payload hashes/sizes verify before each launch. Existing scoped Private/
Public LocalSubnet firewall refresh succeeds automatically on attempt one at
22:28:05.7505994 UTC; no permission/task/ACL changes.

All 14 packaged captures complete with native/helper exit zero, matching clean
source/package provenance, requested dimensions and all applicable state, cue,
layout, actual text size, action-content, keyboard, focus, pointer and reading-
scroll predicates true. No native Error/Fatal lines occur. All final PNGs were
inspected; the 1768x3560 whole-screen view is viewer-resized to 1017x2048.
Enlarged action frames expose both stacked controls. Held Hint has visible native
press/focus feedback without consuming a hint/evaluating; actual routed pointer
and keyboard Hint routes produce one assisted evaluation and disabled live
controls. Some result-reading frames leave controls partly/wholly offscreen;
their state evidence does not claim control visibility in those frames. These
are Windows offscreen/synthetic checks, not manual pointer/touch or phone evidence.

The final reference-size comparison has exactly 29,714 changed Hint-region
pixels and zero outside versus PR #49's packaged baseline. Eight-point error and
candidate sample RGBs equal the final Editor trial (3.0833). Other controls, live
reading text, wordmark, companion and background are pixel-identical in this
comparison. Current initial PNG SHA-256:
`5c50d4514ac23912f6b6010eacbf50064a8cdfb8ec9ecdd63683a730fe298daf`.
Editor/package differs only at known 964 Pause/plaque pixels in
[362,38,855,198), maximum channel delta one. Raw hashes, protocols and comparison:
`Artifacts/QA/UI01/HintSurface20261006/verification.json` and adjacent scripts.

Capture folders under `Artifacts/QA/UI01/`:

| Run | Case | Dimensions / text |
|---|---|---|
| `20261006-222810-packaged-capture-initial` | Initial comparison | 884x1780 / 100% |
| `20261006-222823-packaged-capture-initial` | Initial double-size | 1768x3560 / 100% |
| `20261006-222833-packaged-capture-initial` | Phone-shaped initial | 390x844 / 100% |
| `20261006-222843-packaged-capture-actions` | Enlarged stacked actions | 390x844 / 200% |
| `20261006-222853-packaged-capture-actions` | Narrow enlarged actions | 260x640 / 200% |
| `20261006-222904-packaged-capture-actionfocus` | Narrow Check focus | 260x640 / 100% |
| `20261006-222915-packaged-capture-pointerhintpress` | Held virtual Hint | 260x640 / 200% |
| `20261006-222926-packaged-capture-pointerhint` | Virtual assisted submit | 390x844 / 200% |
| `20261006-222940-packaged-capture-pointerclick` | Virtual answer/check regression | 260x640 / 200% |
| `20261006-222954-packaged-capture-hint` | Hint-used feedback | 260x640 / 200% |
| `20261006-223005-packaged-capture-correct` | Disabled Hint after correct submit | 390x844 / 200% |
| `20261006-223016-packaged-capture-keyhint` | Routed keyboard Hint/submit | 884x1780 / 100% |
| `20261006-223028-packaged-capture-keytab` | Routed Hint focus | 390x844 / 100% |
| `20261006-223040-packaged-capture-scrollfeedback` | Feedback reading end | 844x390 / 200% |

Safe-zone is 1 for reference/double-size and 0.9 otherwise; tooltips are disabled.
Actions/scroll modes intrinsically use 200%; actionfocus uses actual 100%.
Both Unreal Context tests pass with complete clean-source evidence in
`20261006-223055-automation-initial`: two succeeded, zero failed/not-run/in-progress.
Dedicated read-only review against the dependency branch is recorded below.

## Dedicated review and dependency

`python Tools/Review/review_pr.py --base origin/feature/g-answer-cue-proof`
completes with exit zero in `Artifacts/Reviews/20261006-223449/`. It reviews clean
head `c92c4a514e6de166b05c8f8862a68adfb078d9db` against actual dependency base
`3dc14ea084a13611b83a535b4315030794f4b1ba`; head and worktree remain unchanged.
The report identifies no actionable introduced defects. Original-reference
verification passes, and all new asset hashes match provenance. The reviewer
cannot independently run renderer reproduction due to local filesystem permissions;
the primary byte-identical reproduction passes as recorded above. The reviewer
does not independently rerun Unreal builds/runtime/device checks. Raw `review.txt`
and `run.json` remain ignored. Later commits record review/publication only;
runtime source/art remains the clean packaged `a877a5c`.

At the publication check, PR #49 still reported open, so publication used its branch as the actual base.
The Hint diff can be reviewed independently, but PR #49 must be merged first.
No implementation-agent merge is performed; read-only review never authorizes
merge or accepts original outstanding gates.

## Publication

Non-draft [PR #50](https://github.com/rloterh/WordQuest/pull/50) was published on
`feature/g-hint-pearl-surface` against `feature/g-answer-cue-proof`, the actual
branch for then-open PR #49. Runtime source/art remains the clean tested
`a877a5c`; subsequent commits are documentation only. The published sequence was
to merge #49, retarget #50 to `dev`, and recheck its actual base/diff before merge.
GitHub now confirms the owner merged #49 into `dev` at 22:58:22 UTC on 2026-10-06
(`25eb382`), then #50 into its unchanged feature-branch base at 22:58:40 UTC
(`269d6aa`). The Hint changes therefore still need integration into `dev`.
See [dev integration evidence](G-HINT-DEV-INTEGRATION.md). The implementation agent
does not merge PRs; original gates remain open.

Full UI01 type/art/material fidelity, UI02 motion, manual/platform accessibility,
draft fixture editorial approval, Android/phone, isolated offline, performance and
original release gates remain open. No later milestone, deployment or release;
the owner retains merge decisions.
