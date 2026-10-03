# G wordmark Q-swash candidate

The owner merged PRs #27 and #28 into `dev` on 2026-10-02, 21:50:42 and
21:50:59 UTC. This bounded UI01 change uses a v004 editable master to reconstruct
the reference's Q loop and two tapered ribbons. The older outlined Q descender
and flat tail did not reproduce that silhouette. The font file and earlier
masters are preserved; this is a derivative graphic, not a modified font or
accepted original lettering.

A baseline editor capture at clean `77d4fde` (`20261002-215625-capture-initial`)
and two dirty native preflights (`215840` and `220121`, same date, capture-initial)
pass their state/dimension/cue checks. Both revised preflights were inspected.
The first revision's loop was too broad and ribbon branch too thin; the second
revision narrows the loop and gives the upturned branch a fuller taper. A parity
check after rebuilding intentionally caught the stale runtime copy, which was
then restaged and passes. Final corrected packaging and native verification are recorded below;
no acceptance is established by these preliminary checks.

Reproduction preserves v001 after CRLF/LF normalization; v002/v003/v004 reproduce
byte-identically. Original bytes are restored after every reproduction check.
Seven non-Q licensed glyph paths, authored W, fit transform, gradient definitions
and under-title ornament match the prior master. An initial XML comparison included
inter-element tail whitespace and rejected an extra blank line; the corrected
comparison excludes that tail while retaining all W attributes/children. Evidence:
`Artifacts/QA/UI01/wordmark-swash-integrity.py` and `.json`. All 63 existing Python
QA tests pass. Master/runtime/provenance are documented in the vector README.

The Android engine receipt remains absent and adb lists no device. The supported
Computer Use inventory still fails with a missing native-pipe connection, so no
manual desktop/Launcher control is claimed. Art, editorial, manual/platform
accessibility, phone/offline/performance, UI02 motion and release gates remain open.

The first clean package at `5a55ed4` (`20261002-220533-074642`) passed both
real targets, cook/stage/archive, nine inspected native contracts and both Unreal
tests. However, reference-size pixel analysis found 6,220 changed pixels outside
the lower-Q region: removing its descender shortened the shared glyph gradient's
object bounds, unintentionally changing shading on other lettering. This package
is preliminary, not the final art evidence. Raw batch/analysis files are retained
with the `wordmark-swash-unpinned-gradient-` prefix; the archive is unchanged.

The correction gives the shared glyph path separate gradients mapped explicitly
to its original vertical bounds. Original local gradients remain for W/ornament.
Dirty native preflight `20261002-221346-capture-initial` reduces changes outside
the lower-Q region to three pixels, each differing by one RGB byte level. Final
clean packaging and captures verify this corrected material mapping.

## Final clean package

Corrected implementation: `389455c8f1380571568a66cc9453978b7cc6b9de`, clean
worktree. Final v004 master, runtime copy and extracted cooked SVG have SHA-256
`99c52f406eb50596945f32b2ccd43faec3112c44f942e90ea1c84f6b5bae0428`.
No C++, scoring, fixture, font binary or generated project files changed.

Package: `Artifacts/Packages/Win64/20261002-221607-819952`.
The real Editor/Game target checks pass with zero actions because C++ is unchanged;
Editor 1.83 seconds, Game 1.69 seconds. Full Development cook/stage/archive passes
with UAT exit 0, BuildCookRun 69.45 seconds. All 48 archived payload hashes are
recorded and verified before every final launch. Source head, worktree and input
invariants pass. Manifest SHA-256:
`85c28491957ad7512da888e63b5a2332c183a16dde7e3c5c6c282fd07275d0a1`.
UnrealPak extraction exits 0; pak hash remains unchanged and the extracted SVG
matches runtime/master exactly. `WordmarkExtract.json` records the command/hash.
Builds, packages, raw comparisons and captures remain local under ignored Artifacts.

## Final native checks

All nine final packaged captures pass native/helper exit, dimensions and applicable
state/cue/focus/reflow contracts. Each PNG was directly inspected. Native logs have
no Error/Fatal lines. Batch/reproduction:
`Artifacts/QA/UI01/wordmark-swash-batch.py` and `.json`. All runs are 20261002.

| Run | Proof / dimensions | Observed result |
|---|---|---|
| 221808 | initial, 884x1780 | New Q loop/sweeps; unchanged live reading and empty cues |
| 221819 | correct, same | Revised title with readable disabled answers, result and explanation |
| 221829 | pausefocus, 260x640 | Compact title separate from focused Pause control |
| 221839 | initial, 844x390 | Compact title retained; reading region scrolls |
| 221848 | large, 390x844 | Decorative title retained; live 200% reading reflows |
| 221858 | keydisabled, same | Disabled-control traversal and explicit Resume preserve result/evaluation |
| 221907 | keyretry, same | Retry clears result/Hint; selected enlarged A remains visible; scroll can hide title |
| 221917 | interruptsubmitted, same | Assisted incorrect attempt preserved across synthetic notifications/explicit Resume |
| 221927 | modalcycle, 260x200 | Short-window Pause scrolling, focused Retry, Shift/Tab and text toggle pass |

The first five suppress tooltips for comparison; other routes use normal tooltips.
Non-reference runs simulate .9 safe area. These are synthetic native input/lifecycle
checks, not manual keyboard, screen-reader, OS interruption or physical-phone
acceptance. Both `WordQuest.Context` tests pass with failed/notRun/inProcess zero
and native exit 0 at clean corrected source:
`20261002-222028-automation-initial`. All 63 Python QA tests, six immutable reference
hashes, seven master/runtime pairs, LFS configuration and whitespace checks pass.
No new tests mirroring the vector code were added; reproduction, cooked-byte
checks and actual native rendering verify this bounded graphic change.

## Read-only reference comparison

Final initial and correct comparisons against PR #27 each find 2,821 changed
pixels, all within the existing title `[229,23,659,163)`. Of these, 2,818 lie in
lower-Q region `[443,90,620,154)`. The three outside that smaller region differ by
one RGB byte level. Their coordinates/values are retained in
`Artifacts/QA/UI01/wordmark-swash-analysis.json`; the adjacent `.py` reproduces
analysis. Other glyph paths/W/placement are unchanged; this does not claim every
unchanged path renders byte-identically. Original local gradient definitions remain;
separate shared-glyph gradients pin the prior bounds at y=3.121..117.709.

Final initial PNG SHA-256:
`6d2229cf9d3836430007c8192f0c9d60b0113db541ddb5806e6597bf10cabd7c`.
Final correct PNG SHA-256:
`5d1a7dd1c14cf90277b3868dc2a30a293379faf18ddb393b452fc5837609281f`.

In sample `[500,125,615,154)`, lowest warm opaque-core Y is reference 147,
previous v003 149 and final v004 147. Predicate:
`R>170, G>130, B>120, R>G+4, R>B+8`. This is one anchor diagnostic, not silhouette
or material acceptance. Enlarged read-only reference/native inspection figures
show the added loop and curled branch; the reference's precise taper, loop/bowl
junction, letterforms and lighting remain different. A 50% full-screen diagnostic
was directly inspected; it also shows the existing panel, type and companion
mismatches. The original reference/native input bytes are unchanged.

`g-wordmark-swash-comparison.html` embeds the unchanged images with the existing
adjustable overlay. The supported Browser skill connection returned
`privileged native pipe bridge is not available; browser-client is not trusted`.
Browser/slider interaction is therefore unverified; no fallback browser automation
or native helper bypass was attempted. Static diagnostic inspection is separate.

## Remaining acceptance

Companion identity, panel/control finish, precise lettering and static fidelity
remain candidates. EQUIVOCAL and the displayed `3 / 7` remain unapproved prototype
fixtures. Editorial, manual/platform accessibility, full contrast, phone/offline/
performance, UI02 motion and release gates remain open. The Android support receipt
is absent and adb lists no device; no new phone or GUI-control evidence is claimed.
The owner retains merge authority; no agent merge, game deployment or release occurs.

Dedicated read-only Codex review of clean
`7e053d1eb4ec1124dec2c1a4ba102a6546f23ccf` against actual `origin/dev`
(`77d4fdeae4c4ea4e47e2760eba79b38f0dc0e35e`) completed with exit 0 and no
actionable introduced defects. Head/worktree remained unchanged. The reviewer
independently checked SVG parity and the six references; its Python test run had
not completed, and it did not independently repeat native builds, rendering or
device acceptance. The author's final 63-test run completed separately as recorded
above. Raw review evidence: `Artifacts/Reviews/20261002-222323`. Subsequent
review/publication records change documentation only.

Published as regular [PR #29](https://github.com/rloterh/WordQuest/pull/29)
against `dev`; no agent merge was performed.
