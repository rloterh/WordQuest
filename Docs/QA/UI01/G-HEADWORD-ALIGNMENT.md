# G live headword alignment

PR #45 is owner-merged at `b0d3b24` (2026-10-05, 02:00:45 UTC). This bounded UI01
correction refines only the live word role using the existing genuine licensed
Liberation Sans reading composite. No font file, imported asset, license, fixture,
art or learning/control handler changes. It does not identify the font originally
used in a generated reference image or accept exact letterforms/antialiasing.

With the reading composite available, reference word pixels move from 76 to 77,
the measured/drawn font uses letter spacing -5, horizontal slot offset moves from
107 to 110 reference units and vertical offset is raised by 1.5 units. Measurement
uses the same font information as drawing. Existing readability floor, point-size
rounding, actual 200% enlargement, per-character overflow wrapping, minimum
95-unit block height, measured expansion and downstream flow remain. Missing
either reading FontFace retains the previous 76-pixel/default-family/zero-spacing/
107-offset/unraised fallback. Other text roles use zero spacing as before.

## Preliminary evidence

Fixed-region navy glyph bounds (R<65, G<60, B<125, word region [150,680,730,780))
measure the original at 450x71, center (446,731.5), versus prior packaged native
445x69, center (443.5,731.5). These are diagnostic extents, not font identity or
whole-screen acceptance. Existing clue/prompt/answer/mode differences remain.

The first real Editor build passes in 66.99s
(`Artifacts/Logs/Build/WordQuestEditor-20261005-021830.log`). Initial dirty preflight
`20261005-022052-capture-initial` passes and its full screen and original/baseline/
candidate word crops were inspected. It reaches 450x70 and horizontal center 446,
but vertical center 733 is lower than the target; the 1.5-unit raise addresses this
before final verification. Only word-region pixels change, apart from the known
964 Pause/plaque Editor/package pixels at maximum channel delta one. Diagnostics
and raw comparison are under `Artifacts/QA/UI01/WordType20261005/` and are not
product art.

The final real Editor build passes in 44.49s
(`Artifacts/Logs/Build/WordQuestEditor-20261005-022516.log`). Aligned preflight
`20261005-022601-capture-initial` passes: word bounds [221,697,671,767), 450x70,
center (446,732). The remaining half-pixel vertical-center difference and one-pixel
height difference are disclosed. Other measured text roles remain unchanged.
Only 5,657 word-region pixels change, plus the same 964 one-level Pause/plaque
Editor/package variations. Final full screen and word crop were inspected.

With the Bold reading asset temporarily omitted, native fallback captures
`20261005-022822-capture-initial` and `20261005-022846-capture-large` both pass
(884x1780 default; 390x844 safe-zone 0.9 at actual 200%). Both PNGs were inspected;
the enlarged screen intentionally scrolls. The asset is restored byte-for-byte
at SHA-256 `ddb17ec624e8c6e8d68b607cbbd14e5302111b07e158074cc101e69de0a78715`.
Against historical fallback `20261003-113737-capture-initial`, glyph bounds remain
[243,694,643,755). A strict threshold-mask equality diagnostic failed: 30 edge
pixels cross the navy threshold, with maximum channel difference three at those
pixels. This is not a pixel-identical fallback claim; historical background/art
changes also differ. Native logs confirm default Roboto loading and word size 57,
while the source preserves the previous fallback parameters.

## Clean package and native matrix

Source commit `474165c8119443acedfadcedf5ff15d5dd6be218` is packaged from a clean
worktree in `Artifacts/Packages/Win64/20261005-023452-848621/`. BuildCookRun passes
in 155.13s; 521 packages cook with zero errors/warnings. The manifest records
unchanged head/worktree/inputs and complete evidence, SHA-256
`b62e01f64736a0b3977a9e1fc0c71f8b3315d60acaf1b1bc1f2b4f324008676a`.
All 49 payload hashes/sizes are verified before each launch. Existing scoped
LocalSubnet firewall refresh succeeds automatically in one attempt at
02:37:51.1662876 UTC; no security/task/ACL changes are made.

All 14 packaged captures below complete with native/helper exit zero, matching
clean source/package provenance, expected dimensions and all applicable native
layout, state, text-size, focus, pointer and reading-scroll predicates true. No
native Error/Fatal lines occur. All final PNGs were inspected; the 1768x3560 PNG
was viewer-resized to 1017x2048 for full-screen inspection. Narrow enlarged text
wraps per character and uses existing scrolling; these are offscreen Windows
captures and synthetic routes, not manual input or physical-device evidence.
Raw runs live under `Artifacts/QA/UI01/`.

| Capture run | Case | Dimensions / text |
|---|---|---|
| `20261005-023755-packaged-capture-initial` | Initial reference size | 884x1780 / 100% |
| `20261005-023809-packaged-capture-initial` | Initial double size | 1768x3560 / 100% |
| `20261005-023821-packaged-capture-initial` | Initial phone-shaped | 390x844 / 100% |
| `20261005-023831-packaged-capture-initial` | Initial enlarged | 390x844 / 200% |
| `20261005-023842-packaged-capture-initial` | Initial narrow enlarged | 260x640 / 200% |
| `20261005-023853-packaged-capture-pointerpress` | Held virtual pointer | 260x640 / 200% |
| `20261005-023903-packaged-capture-pointerclick` | Virtual answer/check route | 390x844 / 100% |
| `20261005-023919-packaged-capture-pointerresumed` | Virtual pause/resume | 260x640 / 200% |
| `20261005-023935-packaged-capture-longfocus` | Long answer focused | 390x844 / 200% |
| `20261005-023946-packaged-capture-longselectedfocus` | Long selected answer focused | 260x640 / 200% |
| `20261005-023956-packaged-capture-correct` | Correct feedback | 884x1780 / 100% |
| `20261005-024008-packaged-capture-wrong` | Wrong feedback | 390x844 / 200% |
| `20261005-024020-packaged-capture-hint` | Assisted feedback | 390x844 / 200% |
| `20261005-024032-packaged-capture-scrollfeedback` | Reading feedback scroll | 844x390 / 200% |

Safe-zone is 1 for reference/double-size cases and 0.9 for the others; tooltips
are disabled in every capture. The long/scroll modes intrinsically use 200% text.
The packaged reference-size PNG SHA-256 is
`99b0971f068499ee8377a5df7a9200144dccb4e0598fe2b5f1c1d616a15b7720`.
Against PR #45 package `20261005-014353-packaged-capture-initial`, exactly 5,657
pixels change inside the word diagnostic region and zero outside. Word glyph
bounds/center equal the final preflight's 450x70/(446,732). Clue, prompt, answer A
and mode extents remain identical to that prior package. Editor/package differs
only at 964 Pause/plaque pixels in bounds [362,38,855,198), maximum channel delta
one. Reference SHA remains
`306dae4f6352749edcf1d8edf73f26339a4ba6407b4a394ec50b5898418bedae`.
Raw verified metrics, hashes and case predicates are in
`Artifacts/QA/UI01/WordType20261005/verification.json`; diagnostic crops and the
half-opacity comparison are QA output, never product assets.

Existing 82 Python QA tests pass (`headword-type-python-checks.log`); both Unreal
automation tests pass with complete evidence (`20261005-024050-automation-initial`;
`WordType20261005/automation-helper.log`).
The supplied six reference hash/dimension checks and ten source/runtime SVG parity
checks pass. Source code is the only runtime change; no binaries are committed.

## Dedicated review

`python Tools/Review/review_pr.py --base origin/dev` completes with exit zero in
`Artifacts/Reviews/20261005-024255/`. It reviews clean head `d64ebc9` against
actual base `b0d3b24`; head and worktree remain unchanged. The report finds no
actionable introduced defects and confirms the disclosed fallback/layout and
acceptance limits. It does not independently rerun builds/runtime checks. Connector
startup/shutdown warnings remain in diagnostics; the dedicated review completes
normally. Subsequent documentation records evidence/publication only. The owner
retains the merge decision; review does not accept any outstanding gate.

Full static type/art/material fidelity, UI02 motion, manual/platform accessibility,
draft fixture editorial approval, Android/phone, isolated offline, performance and
original release gates remain open. No H/I/later milestone, deployment, release
or implementation-agent merge is performed.
