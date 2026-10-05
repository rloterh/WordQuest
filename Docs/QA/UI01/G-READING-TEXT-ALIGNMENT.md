# G clue and question-prompt alignment

PR #46 is owner-merged into `dev` at `50c0549` (2026-10-05, 02:58:43 UTC).
This bounded UI01 correction moves only the live clue and question prompt using
the existing licensed Liberation Sans reading composite. No font size, weight,
tracking, asset, license, draft fixture, original reference or learning/control
handler changes. Missing either reading FontFace retains the previous anchors.

With that composite available, the clue vertical slot moves down two reference
units and its horizontal anchor remains 152. The prompt
horizontal offset moves from 117 to 120 and its vertical slot moves down four.
Existing measured heights, readability floor, actual 200% text, point rounding,
per-character overflow wrapping and subsequent flow anchors remain. Minimum
block heights and gaps reserve space for these small optical offsets; native
large/long/narrow checks must verify their resulting layout.

## Baseline and verification in progress

The immutable G original's fixed-region navy glyph bounds (R<65, G<60, B<125)
put the first clue line at [174,797,710,823), 536x26, center (442,810), versus the
PR #46 packaged baseline at [173,795,710,821), 537x26, center (441.5,808).
The original prompt is [189,930,697,962), 508x32, center (443,946), versus native
[185,927,695,957), 510x30, center (440,942). These are measured extent/placement
differences, not original-font identity or full fidelity acceptance. Font width,
height, letterform and antialiasing differences remain outside this correction.
The prior package is `20261005-023755-packaged-capture-initial` under
`Artifacts/QA/UI01/`. Diagnostics are QA output, never product art.

## Real Editor and fallback evidence

Initial real Editor build passes in 67.45s (`WordQuestEditor-20261005-030246.log`).
Preflight `20261005-030354-capture-initial` passes, but a proposed half-unit
sideways clue offset gives no overall horizontal improvement and is removed.
The final Editor build passes in 22.79s (`WordQuestEditor-20261005-030727.log`),
then final preflight `20261005-030750-capture-initial` passes with complete evidence.
Its reading crop and the original crop were inspected. Final glyph extents are:

| Role | Original bounds / center | Final native bounds / center |
|---|---|---|
| Clue line 1 | [174,797,710,823) / (442,810) | [173,797,710,823) / (441.5,810) |
| Clue line 2 | [205,840,682,873) / (443.5,856.5) | [207,839,676,872) / (441.5,855.5) |
| Prompt | [189,930,697,962) / (443,946) | [188,931,698,961) / (443,946) |

Clue widths/heights and prompt 510x30 size remain unchanged. The first clue line's
vertical center matches and the second is one pixel high rather than three; the
prompt center matches, with width/height/letterform differences still disclosed.
Only 16,348 pixels in the clue/prompt diagnostic regions change versus the prior
package, apart from known 964 Editor/package Pause/plaque pixels with maximum
channel delta one. Word, answer A and mode bounds remain identical. Raw metrics,
input hashes and QA crops are under `Artifacts/QA/UI01/ReadingAnchors20261005/`.

Editor missing-Bold-font captures `20261005-030451-capture-initial` (884x1780) and
`20261005-030515-capture-large` (390x844, safe-zone 0.9, actual 200%) both pass.
Both full PNGs were inspected and are RGB-identical to the corresponding PR #46
fallback images `20261005-022822-capture-initial` and `20261005-022846-capture-large`.
Those captures precede removal of the unused half-unit reading-face clue offset;
the fallback branch is unchanged. The genuine Bold FontFace is restored unchanged
at SHA-256 `ddb17ec624e8c6e8d68b607cbbd14e5302111b07e158074cc101e69de0a78715`.
This is an Editor omission test, not corrupt-package or physical-device evidence.

Existing 82 Python QA tests, six supplied-reference hash/dimension checks and ten
source/runtime SVG parity checks pass. No binaries are committed.

## Clean package and native matrix

Clean source `6fe265c41dc83352c9ee88ef42a487f7a6295303` builds/cooks successfully
in 157.26s, with 521 cooked packages and zero cook errors/warnings. Archive
`Artifacts/Packages/Win64/20261005-031044-154956/` has complete evidence and
unchanged source head/worktree/inputs. Manifest SHA-256:
`53333ecab95906e58741037ae7cc295eecbd64969db35ed9b758c63760c9372e`.
All 49 archived payload hashes/sizes are verified before each native launch.
Existing scoped LocalSubnet firewall refresh succeeds automatically on attempt
one at 03:13:45.1476712 UTC. No permission/task/ACL policy changes are made.

All 14 packaged captures complete with native/helper exit zero, matching clean
source/package provenance and dimensions, and all applicable native layout, state,
text-size, focus, pointer and reading-scroll predicates true. No native Error/Fatal
lines occur. Every final PNG was inspected; the 1768x3560 full-screen view was
resized by the viewer to 1017x2048. Narrow/enlarged text uses existing measured
wrapping and scrolling. These are Windows offscreen/synthetic checks, not manual
input, platform accessibility or physical-phone evidence. Raw folders are under
`Artifacts/QA/UI01/`.

| Capture run | Case | Dimensions / text |
|---|---|---|
| `20261005-031351-packaged-capture-initial` | Initial reference size | 884x1780 / 100% |
| `20261005-031405-packaged-capture-initial` | Initial double size | 1768x3560 / 100% |
| `20261005-031417-packaged-capture-initial` | Initial phone-shaped | 390x844 / 100% |
| `20261005-031428-packaged-capture-initial` | Initial enlarged | 390x844 / 200% |
| `20261005-031438-packaged-capture-initial` | Initial narrow enlarged | 260x640 / 200% |
| `20261005-031449-packaged-capture-pointerpress` | Held virtual pointer | 260x640 / 200% |
| `20261005-031500-packaged-capture-pointerclick` | Virtual answer/check | 390x844 / 100% |
| `20261005-031515-packaged-capture-pointerresumed` | Virtual pause/resume | 260x640 / 200% |
| `20261005-031530-packaged-capture-longfocus` | Long answer focused | 390x844 / 200% |
| `20261005-031541-packaged-capture-longselectedfocus` | Long selected answer focused | 260x640 / 200% |
| `20261005-031552-packaged-capture-correct` | Correct feedback | 884x1780 / 100% |
| `20261005-031604-packaged-capture-wrong` | Wrong feedback | 390x844 / 200% |
| `20261005-031615-packaged-capture-hint` | Assisted feedback | 390x844 / 200% |
| `20261005-031627-packaged-capture-scrollfeedback` | Reading feedback scroll | 844x390 / 200% |

Safe-zone is 1 for reference/double-size and 0.9 for other cases; tooltips are
disabled. Long/scroll modes intrinsically use 200% text. The initial packaged
PNG SHA-256 is `b26befb07b156490709ba38e1cce643c1870e7ec095c9f926c73f077c9d8b8fe`.
Final packaged reading glyph bounds equal the final preflight table above.
Exactly 16,348 pixels change in the two reading diagnostic regions, zero outside,
versus PR #46's package. Word, answer A and mode extents remain unchanged. The
Editor/package comparison differs only at 964 known Pause/plaque pixels in
[362,38,855,198), maximum channel delta one. Original reference SHA remains
`306dae4f6352749edcf1d8edf73f26339a4ba6407b4a394ec50b5898418bedae`.
The inspected half-opacity comparison still reveals text-shape/art differences;
it does not accept complete fidelity. Raw verification, hashes and metrics live
in `Artifacts/QA/UI01/ReadingAnchors20261005/verification.json`.

Both Unreal Context automation tests pass with complete evidence in
`20261005-031645-automation-initial`, at the same clean source commit. Python,
reference and SVG check logs are recorded in the earlier evidence folder and
`Artifacts/Logs/UI01/reading-anchors-python-checks.log`. Dedicated read-only
review against actual `origin/dev` completes as recorded below.

## Dedicated review

`python Tools/Review/review_pr.py --base origin/dev` completes with exit zero in
`Artifacts/Reviews/20261005-032003/`. It reviews clean head `05c2f3d` against
actual base `50c0549`; source head and worktree remain unchanged. The report
finds no actionable introduced defects and confirms preserved fallback anchors,
measured text sizes/downstream layout and explicit outstanding gates. It does
not independently rerun builds/runtime checks. Subsequent commits record review
and publication only; runtime source remains the tested `6fe265c`. The owner
retains the merge decision, and review does not accept any outstanding gate.

## Publication

Non-draft [PR #47](https://github.com/rloterh/WordQuest/pull/47) is open against
`dev` on `feature/g-reading-text-align`. Following the tested source commit,
commits contain documentation only. The implementation agent does not merge.
After owner merge, continue bounded UI01 comparison of the remaining reading
roles and art/material differences before UI02 acceptance work.

Full static type/art/material fidelity, UI02 motion, manual/platform accessibility,
draft fixture editorial approval, Android/phone, isolated offline, performance and
original release gates remain open. No later milestone, deployment or release;
the owner retains merge decisions.
