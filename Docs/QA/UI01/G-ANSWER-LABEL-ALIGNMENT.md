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
symbols/wrapped rows, Unreal automation and dedicated review are pending.
No binary assets are committed.

Full static type/art/material fidelity, UI02 motion, manual/platform accessibility,
draft fixture editorial approval, Android/phone, isolated offline, performance and
original release gates remain open. No later milestone, deployment or release;
the owner retains merge decisions.
