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
source/runtime SVG parity checks pass. Clean package/matrix, Unreal automation
and dedicated read-only review are pending. No binaries are committed.

Full static type/art/material fidelity, UI02 motion, manual/platform accessibility,
draft fixture editorial approval, Android/phone, isolated offline, performance and
original release gates remain open. No later milestone, deployment or release;
the owner retains merge decisions.
