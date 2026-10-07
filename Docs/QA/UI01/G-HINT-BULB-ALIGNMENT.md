# G Hint bulb alignment

PR #51 is owner-merged into `dev` at `10110a1` on 2026-10-06, 23:31:36 UTC.
This bounded UI01 correction measures the separate Hint bulb against the original
G gameplay image. The initial diagnostic considered the action row; measured live
label centers are within one pixel while the bulb is 5.5px high and 2px wide.
The change therefore refines only that icon's authored geometry.

## Source and diagnostic limits

`ArtSource/UI/G/Vector/G-Hint-Bulb-v002.svg` preserves the 40x56 canvas and navy
rounded outline with two base bars. It lowers the silhouette five source units,
narrows/shifts the head left and increases stroke width from 2.8 to 3.4. V001
stays unchanged. The existing staging helper selects v002; targeted LF attributes
keep master/runtime bytes identical across checkouts. No new native code, binary
asset, font, fixture, hit area or input handler is included. Missing optional SVG
continues to collapse its decoration and gap while retaining the live Hint label.

Provenance: `ArtSource/UI/G/Vector/G-Hint-Bulb-v002-PROVENANCE.json`.
Master and staged SHA-256:
`88a9b612b8389587b5dc1b9350483720193c3f1d543a290db62b09c70cfe4a57`.
Preserved v001 SHA-256:
`4d191fffb3384d3ade4a9471667a9a8d176a89ecdcd0c8c270560f4f617e86da`.
There is no imagegen, raster editing or original-reference pixel extraction.

Read-only diagnostic region [176,1475,222,1545), threshold R<65/G<60/B<125:

| Image | Opaque ink bounds, half-open | Size | Center | Threshold pixels |
|---|---|---|---|---|
| Original | [182,1487,214,1536) | 32x49 | (198,1511.5) | 366 |
| Prior native | [182,1482,216,1530) | 34x48 | (199,1506) | 288 |
| Candidate Editor | [182,1487,214,1535) | 32x48 | (198,1511) | 382 |

These threshold-dependent antialiased bounds do not identify an exact silhouette,
prove no clipping, measure contrast or accept global fidelity. A half-pixel center
and one-pixel height difference remain. The original's contour/shading, shared
surface/rim placement, live type shape and Check star remain imperfect. Hint/Check
label and star diagnostic bounds remain unchanged. The full Editor pixel diff
against the prior final Editor capture lies in [181,1481,217,1536), wholly within
the bulb region. Captures/crops/overlay are diagnostics, not product artwork.

## Initial checks

Real UE 5.8.2 Editor target succeeds (up-to-date), 2.45 seconds, exit zero:
`Artifacts/Logs/Build/WordQuestEditor-20261006-233504.log`.
All 96 existing Python QA tests, six immutable references and ten staged SVG
parity pairs pass. Git LFS 3.7.1 is verified; this change adds only text assets.

Dirty native preflight `20261006-233515-capture-initial` completes at 884x1780,
100% text with native/helper exit zero and expected unselected state/cues.
The full screen and matched action crops are inspected against the original.

Two missing-SVG checks deliberately move only the owned runtime icon into an
absolute-path-verified ignored holding folder and restore it in `finally`:

| Run under `Artifacts/QA/UI01/` | Observation |
|---|---|
| `20261006-233735-capture-initial` | 884x1780, 100%, live centered Hint label, no bulb/gap |
| `20261006-233818-capture-actions` | 260x640, intrinsic 200%, safe-zone 0.9, both stacked labels fit and Check focus remains visible |

Both native/helper exits are zero, applicable state/cue/layout/focus/action-content
checks pass and both PNGs are inspected. The SVG is restored to its unchanged
v002 hash and all ten parity pairs pass again. These are dirty-source omission
checks, not tests of a damaged package or a phone.

To leave headroom above the existing Zen low-disk threshold before packaging,
native lossless NTFS compression is applied only to EXE/PDB staging copies from
the two known successful #49/#50 runs. All four logical hashes and matching archive
hashes verify before compression; all four staged hashes verify afterward.
Free space rises from 4,129,988,608 to 5,071,265,792 bytes. Archives are unchanged;
no files are deleted or moved, and no machine policy changes. Raw report is
`Artifacts/QA/UI01/ActionAlignment20261006/stage-compression.json`.

## Clean packaged verification

Clean source/art head `d528389c17c33bd88cf9c8edc222411e7483fc1f` produces real
Win64 Development archive `Artifacts/Packages/Win64/20261006-233948-619171`.
BuildCookRun succeeds in 144.05 seconds, 522 cooked packages, zero errors/warnings;
native/helper exits zero. Complete manifest records unchanged head/worktree/inputs.
All 49 payload size/hash pairs verify before every packaged launch and once again
at completion. Manifest SHA-256:
`26b9d5bc625850dd5f88b0a467c14b33e21ffa7b51b50a6670b07760d609c484`.
The existing scoped owner firewall task refreshes the new executable successfully
on attempt two at 23:42:36.0349819 UTC, Private/Public LocalSubnet. Its policy and
task permissions are unchanged.

All nine packaged captures complete with native/helper exit zero, clean source and
matching package provenance, requested dimensions and all applicable state, cue,
layout, actual text size, action-content, pointer, keyboard and scroll predicates
true. There are no native Error/Fatal lines. All full PNGs are inspected; the
1768x3560 whole-screen view is viewer-resized to 1017x2048.

| Run under `Artifacts/QA/UI01/` | Case | Dimensions / text |
|---|---|---|
| `20261006-234240-packaged-capture-initial` | Frozen comparison | 884x1780 / 100% |
| `20261006-234254-packaged-capture-initial` | Double-size | 1768x3560 / 100% |
| `20261006-234305-packaged-capture-initial` | Phone-shaped initial | 390x844 / 100% |
| `20261006-234316-packaged-capture-actions` | Stacked enlarged controls | 390x844 / intrinsic 200% |
| `20261006-234327-packaged-capture-actions` | Narrow stacked controls | 260x640 / intrinsic 200% |
| `20261006-234338-packaged-capture-pointerhintpress` | Held virtual Hint | 260x640 / 200% |
| `20261006-234348-packaged-capture-pointerhint` | Routed assisted evaluation | 390x844 / 200% |
| `20261006-234402-packaged-capture-keyhint` | Routed keyboard Hint/submit | 884x1780 / 100% |
| `20261006-234414-packaged-capture-scrollfeedback` | Feedback reading end | 844x390 / intrinsic 200% |

Safe-zone is 1 for reference/double-size/keyboard and 0.9 otherwise; tooltips are
disabled. Both stacked enlarged controls are visible in action frames. Held Hint
retains native press/focus feedback without consuming a hint or evaluating; routed
pointer/keyboard Hint produces one assisted evaluation with disabled live controls.
Held-press/reading frames can leave other controls offscreen; they do not establish
simultaneous visibility. The reading-end landscape frame retains the feedback end,
not full feedback at once. These are Windows offscreen/synthetic checks, not manual
pointer/touch, platform accessibility or phone evidence.

Both Unreal Context tests succeed with complete clean-source evidence in
`20261006-234425-automation-initial`, zero failed/not-run/in-progress.
The installed UnrealPak's separate `-Extract <directory>` arguments extract only
`G_HintBulb.svg`; its bytes and SHA-256 equal the v002 master and runtime copy.
The pak's manifest hash remains unchanged after extraction.

The final reference-size comparison against the retained #50 package has exactly
813 changed pixels inside the fixed bulb region and zero elsewhere, bounds
[181,1481,217,1536). Live labels/star, control surfaces, reading layout, wordmark,
companion and background are pixel-identical in this comparison. The initial PNG
SHA-256 is `cb1c493422d16ba082e64c783c287c87fe5f105477343fe7a1cfde3710b8f34a`.
Editor/package differs only at the known 964 Pause/plaque pixels in
[362,38,855,198), maximum channel delta one. Bulb metrics equal the Editor trial.

Raw scripts/logs/metrics remain ignored under
`Artifacts/QA/UI01/ActionAlignment20261006/`: `assessment.json`, `fallback.json`,
`verification.json`, `final-comparison.json`, package/helper logs and extracted SVG.
The clean artifact source remains `d528389`; later commits update documentation.

## Review and remaining gates

`python Tools/Review/review_pr.py --base origin/dev` completes with exit zero in
`Artifacts/Reviews/20261006-234622/`. It reviews clean head
`4d0741b2aa11cb80eea9b35b1181e680a6cec0f5` against actual base
`10110a1c4e420d08d7bd1e30d18f38ab5ee504fa`; head/worktree remain unchanged.
No actionable introduced defects are found in the bounded SVG, staging or
documentation change. Source/runtime parity and all six supplied references pass.
The reviewer does not independently rerun Unreal builds/runtime/device checks.
Raw `review.txt` and `run.json` remain ignored; later commits record review and
publication only. Review does not authorize a merge or accept outstanding gates.

Non-draft [PR #52](https://github.com/rloterh/WordQuest/pull/52) was published on
`feature/g-hint-bulb-alignment`, directly against `dev`. GitHub confirms owner merge
at 2026-10-06 23:59:23 UTC (`ea8fb8edcd9fdaec3c7cfed487e82cc5ebc7f0cd`).
Runtime/art remains the clean tested `d528389` tree; later commits update
documentation only. The implementation agent does not merge PRs.
Full UI01 fidelity, UI02 motion, manual/platform accessibility, draft-fixture
editorial approval, Android/physical-phone, isolated offline, performance and
original release gates remain open. The owner retains merge decisions; there is
no deployment, release or later milestone work.
