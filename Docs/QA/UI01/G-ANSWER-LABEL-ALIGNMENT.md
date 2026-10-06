# G answer label alignment

PR #47 is owner-merged at `6bee47b` (2026-10-05, 08:21:35 UTC). This bounded
UI01 correction adjusts only the existing licensed reading face's answer-label
gap and baseline. No font file/size/weight/tracking, asset, license, draft fixture,
supplied reference or learning/control handler changes. Missing either reading
FontFace retains previous default-family spacing and zero label padding.

Reading-face marker reservation changes from 37 to 33 reference units multiplied
by viewport/text scale, retaining the 18-pixel floor. Actual reserved width still
feeds label-wrap measurement. Two reference units of positive top label padding
align short rows optically; padding is included in measured row-height growth for
wrapped/long text. Badge geometry, identifier alignment rules, button hit areas,
font enlargement and other reading anchors retain their existing behavior.
Native checks must verify enlarged symbols, wrapping, result reading and routing.

## Baseline and verification in progress

Matched original/native navy glyph extents use R<65, G<60, B<125 and label-only
regions x=[230,744), y=[1009,1073), [1121,1185), [1233,1297), [1345,1409).
Raw analysis/crops live in `Artifacts/QA/UI01/AnswerLabels20261006/` and remain QA
output, never product assets. Baseline is PR #47 package
`20261005-031351-packaged-capture-initial` under `Artifacts/QA/UI01/`.

| Label | Original bounds | Prior native bounds |
|---|---|---|
| A | [241,1025,638,1055) | [245,1023,642,1053) |
| B | [242,1137,438,1167) | [246,1135,446,1165) |
| C | [243,1249,500,1279) | [247,1247,506,1277) |
| D | [243,1362,526,1392) | [247,1359,533,1389) |

All label heights are 30 pixels. Native A width already matches 397; B/C/D widths
remain 200/259/286 versus original 196/257/283. Placement correction does not
identify the original font or accept exact letterforms/antialiasing. Real build,
native comparison, fallback, clean package and dedicated review are recorded below.

## Editor and fallback evidence

Real Editor build `WordQuestEditor-20261006-134920.log` passes in 63.64s; native
preflight `20261006-135025-capture-initial` passes. Its four-unit padding trial
moves labels four pixels down, overshooting A-C by two; reduce padding to two.
Final real build `WordQuestEditor-20261006-140059.log` passes in 58.10s and final
preflight `20261006-140159-capture-initial` completes with exit zero. All four
final label crops were inspected. Final native glyph bounds are A
[241,1025,638,1055), B [242,1137,442,1167), C [243,1249,502,1279), D
[243,1361,529,1391). Left edges match all originals, and A-C vertical bounds
match; D stays one pixel high. B/C/D width differences and letterforms remain.
Matching A's fixed-region glyph bounds does not establish pixel identity.
Only 18,064 label-region pixels change versus the prior package, apart from
known 964 Editor/package Pause/plaque pixels with maximum channel delta one.

With the genuine Bold reading FontFace temporarily omitted, captures
`20261006-135717-capture-initial` (884x1780) and `20261006-135850-capture-large`
(390x844, safe-zone 0.9, actual 200%) both pass and their full PNGs were inspected.
They are RGB-identical to prior fallback `20261005-030451-capture-initial` and
`20261005-030515-capture-large`. Captures precede the final padding reduction;
the fallback branch remains zero padding and unchanged measurement. The asset
is restored unchanged at SHA-256
`ddb17ec624e8c6e8d68b607cbbd14e5302111b07e158074cc101e69de0a78715`.
This is an Editor missing-asset test, not corrupt-package or phone evidence.

Existing 82 Python QA tests, six supplied-reference hash/dimension checks and ten
source/runtime SVG parity checks pass. Raw metrics/hashes and ignored comparison
scripts live in `Artifacts/QA/UI01/AnswerLabels20261006/`; Python log is
`Artifacts/Logs/UI01/answer-label-python-checks.log`. Clean package, enlarged
symbols/wrapped rows, Unreal automation and dedicated review are recorded below.
No binary assets are committed.

## Clean package and native verification

Clean source `a9f14a4b32423ea848e0dad57d56134d6f098f48` passes Win64 BuildCookRun
in 219.09s; 521 packages cook with zero errors/warnings. Archive
`Artifacts/Packages/Win64/20261006-141120-420075/` records complete evidence and
unchanged head/worktree/inputs. Manifest SHA-256:
`217e37ec784cb48cc8ca5544570a8ce87b6ed0c1c374a1dc208a5bddcb059429`.
All 49 payload hashes/sizes verify before every launch. Existing scoped
LocalSubnet firewall refresh succeeds automatically on attempt two at
14:16:02.5752884 UTC; existing retry/diagnostic handling is used without changing
permission, task or ACL policy.

All 16 packaged captures complete with native/helper exit zero, matching clean
source/package provenance and dimensions, and all applicable native state, cue,
layout, text-size, focus, pointer and reading-scroll checks true. No native
Error/Fatal lines occur. Every final PNG was inspected; the 1768x3560 full-screen
view is viewer-resized to 1017x2048. Narrow/enlarged text retains measured wrapping
and scrolling; long row heights change as the actual available label width grows.
Visible 200% long-selected `>` and wrong-state `×` cues fit beside the labels;
normal correct-state square-root cue remains clear. Some enlarged selected/correct
frames show initial reading or feedback with the chosen row offscreen: their native
cue/state evidence is not a glyph-visibility proof for that offscreen row. These
are Windows offscreen/synthetic checks, not manual or phone acceptance.
Raw folders live under `Artifacts/QA/UI01/`.

| Capture run | Case | Dimensions / text |
|---|---|---|
| `20261006-141609-packaged-capture-initial` | Initial reference size | 884x1780 / 100% |
| `20261006-141625-packaged-capture-initial` | Initial double size | 1768x3560 / 100% |
| `20261006-141638-packaged-capture-initial` | Initial phone-shaped | 390x844 / 100% |
| `20261006-141651-packaged-capture-initial` | Initial enlarged | 390x844 / 200% |
| `20261006-141703-packaged-capture-initial` | Initial narrow enlarged | 260x640 / 200% |
| `20261006-141716-packaged-capture-selected` | Selected state | 390x844 / 200% |
| `20261006-141741-packaged-capture-correct` | Narrow correct feedback | 260x640 / 200% |
| `20261006-141805-packaged-capture-pointerpress` | Held virtual pointer | 260x640 / 200% |
| `20261006-141829-packaged-capture-pointerclick` | Virtual answer/check | 390x844 / 100% |
| `20261006-141851-packaged-capture-pointerresumed` | Virtual pause/resume | 260x640 / 200% |
| `20261006-141909-packaged-capture-longfocus` | Long answer focused | 390x844 / 200% |
| `20261006-141923-packaged-capture-longselectedfocus` | Long selected answer focused | 260x640 / 200% |
| `20261006-141938-packaged-capture-correct` | Correct feedback | 884x1780 / 100% |
| `20261006-141950-packaged-capture-wrong` | Wrong feedback | 390x844 / 200% |
| `20261006-142002-packaged-capture-hint` | Assisted feedback | 390x844 / 200% |
| `20261006-142015-packaged-capture-scrollfeedback` | Reading feedback scroll | 844x390 / 200% |

Safe-zone is 1 for reference/double-size and 0.9 otherwise. Tooltips are disabled;
long/scroll modes intrinsically use 200% text. Initial packaged PNG SHA-256:
`b323f60730f9627a2458bd664c1373117aabc7cf10da69ed99ce870d15ca321d`.
Final packaged label bounds equal the final preflight bounds above. Exactly
18,064 pixels change inside the four label diagnostic regions and zero outside,
versus PR #47's packaged baseline. Other reading roles, badges, skins and control
positions remain pixel-identical in this reference-size initial comparison.
Editor/package differs only at the known 964 Pause/plaque pixels in
[362,38,855,198), maximum channel delta one. The original reference hash remains
`306dae4f6352749edcf1d8edf73f26339a4ba6407b4a394ec50b5898418bedae`.
Raw verification/metrics/hashes live in
`Artifacts/QA/UI01/AnswerLabels20261006/verification.json`.

Both Unreal Context automation tests pass at the same clean source in
`20261006-142034-automation-initial`, with complete evidence. No tests are added
for the reversible spacing adjustment; existing Python/native checks exercise
reflow, enlarged content, state and routing. Dedicated read-only review against
actual `origin/dev` completes as recorded below.

## Dedicated review

`python Tools/Review/review_pr.py --base origin/dev` completes with exit zero in
`Artifacts/Reviews/20261006-143037/`. It reviews clean head `8bb6328` against
actual base `6bee47b`; head and worktree remain unchanged. The report identifies
no actionable introduced defects and confirms preserved fallback behavior,
padding-aware row measurement and explicit outstanding gates. It does not
independently rerun builds/runtime checks. Subsequent commits record review and
publication only; runtime source remains the tested `a9f14a4`. The owner retains
the merge decision; review does not accept any outstanding gate.

## Publication

Non-draft [PR #48](https://github.com/rloterh/WordQuest/pull/48) is open against
`dev` on `feature/g-answer-label-align`. Following the tested runtime commit,
commits contain documentation only. The implementation agent does not merge.
After owner merge, continue bounded UI01 comparison of remaining text-shape and
art/material differences before UI02 acceptance work.

Full static type/art/material fidelity, UI02 motion, manual/platform accessibility,
draft fixture editorial approval, Android/phone, isolated offline, performance and
original release gates remain open. No later milestone, deployment or release;
the owner retains merge decisions.
