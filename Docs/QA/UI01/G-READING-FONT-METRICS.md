# G reading font metrics

The owner merged [PR #31](https://github.com/rloterh/WordQuest/pull/31) into `dev`
on 2026-10-03 at 05:16:39 UTC (`8377541`). This bounded UI01 candidate addresses
the remaining live word/clue/prompt/answer text metrics against the immutable G
reference. The prior packaged native baseline is
`Artifacts/QA/UI01/20261003-050715-packaged-capture-initial`.

## Candidate and integration

Unmodified, pinned Liberation Sans 2.1.5 Regular/Bold files and their unchanged
SIL OFL license are in `ArtSource/Fonts/LiberationSans`; see its provenance for
upstream links, hashes and glyph inspection. Unreal's initialized isolated editor
imports genuine `G_ReadingRegular` / `G_ReadingBold` FontFaces. The helper refuses
an existing destination and checks both source hashes before import. Font import
requires Slate initialization; do not use the texture-only commandlet workflow.

The transient runtime composite copies the existing engine composite, replacing
only Regular/Bold faces. Existing fallback faces and script routing remain. If
either reading asset is missing, live text uses the default engine family.
Mode/badges/result symbols/progress/Pause controls and display faces are unchanged.
Word/clue/prompt/answer reference pixel sizes are 76/36/32/32; feedback retains 29.
The existing point-size rounding, readability floor, 200% enlargement, wrapping,
measurement, scrolling and focus reveal remain. No fixture or scoring changes.
The license is staged unchanged as a visible NonUFS package resource.
Minimum word/clue block heights of 95/92 reference units compensate for the
shorter candidate line boxes; measured long/large text can still expand them.

## Verification in progress

Read-only native/reference navy-pixel bounds reveal baseline width/height
differences: word 422x64 vs reference 450x71, first clue line 556x28 vs 536x26,
prompt 515x34 vs 508x32, answer A 447x34 vs 397x30. Thresholds and fixed regions
are recorded in `Artifacts/QA/UI01/reading-font-baseline-metrics.json`.
These diagnostic bounds are affected by generated antialiasing and are not exact
font identification or acceptance tolerances by themselves. Preliminary local
font measurements inform the candidate; actual Unreal checks are still required.

The genuine imports contain each full unchanged source font (offsets 1407/1386
in Regular/Bold assets). All current draft fixture characters are present in
both faces. Import completion marker, saved FontFace types and normal shutdown
are recorded in `Artifacts/Logs/UI01/reading-font-import.log`, `.json` and
`reading-font-import-verification.json`. No errors; one NVIDIA TSR driver warning
is unrelated to font import. The GUI executable's native exit code was not captured;
the shell launch/wait result is not presented as an engine exit code.

Actual Editor compilation passed in 46.52s (six actions), then in 24.93s (four
actions) after the reading-height adjustment. Logs are
`Artifacts/Logs/Build/WordQuestEditor-20261003-052731.log` and `-053150.log`.
Dirty preflight `20261003-052858-capture-initial` exposed the line-box shift;
adjusted `20261003-053251-capture-initial` passed and its PNG was inspected.
Matched-region candidate bounds are word 445x69, clue 537x26, prompt 510x30,
answer A 397x30. Each is closer to the corresponding reference bounds than
the prior native family. This is measured similarity, not original-font identity
or static fidelity acceptance. All 66 Python QA tests, six reference hashes and
seven SVG source/runtime pairs pass. Final clean cooked and fallback checks remain.

Import, native builds/captures, licensed payload checks, package, tests and dedicated
read-only review are in progress. Simplified art, exact lettering/type/color,
editorial/manual accessibility, UI02 motion, real-phone/offline/performance and
release gates remain open. No new H/I work, deployment or release is included.
