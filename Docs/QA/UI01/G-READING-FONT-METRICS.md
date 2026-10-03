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

## Clean cooked verification

Implementation `81418d0acba305c056803e49b7d76df1d2998e2e` passed the actual
Editor target check (6.21s, metadata refresh) and Game compilation (55.65s),
then full Win64 BuildCookRun (188.91s). Archive
`Artifacts/Packages/Win64/20261003-053912-027830` has 49 verified payload hashes,
exit 0 and complete evidence with unchanged source head/worktree/inputs. Manifest
SHA-256: `da434c87f911df3efc93e99be82f3bbafa572d30e0f8d6b8ca5c29be9ea543cf`.
The optional local firewall task automatically covered this new package path.

UnrealPak extraction passed with `-Extract <directory> -Filter=*G_Reading*.ufont`.
The 410,720/414,464-byte Regular/Bold cooked files each contain the exact original
TTF at offset 4, between the array-length and empty-geometry counters. Their hashes
are `f287873dcf43aceba2468aa17c3b0bf4cd598850ff09d7ab9ead2578894f3a97` and
`5dcf6e2a6d111ed706b150901339dd8e3b3c6fd53af210fc85eb2c94dc9ae32c`.
Packaged logs confirm loading both `.ufont` resources. The staged NonUFS license
matches its unmodified source SHA-256. Both TTF/FontFace LFS OIDs match actual files.
Reproduction/hash details are in `reading-font-extract.log` and
`verify-reading-font-package.py` / `reading-font-package-verification.json`
under `Artifacts/QA/UI01`.

All 15 clean packaged runs below exited 0, verified the archive hashes and passed
applicable native state/cue/reading/focus checks, with complete evidence. Every PNG
was inspected. Logs contain no `Error:`/`Fatal:` lines. These are synthetic native
desktop checks, not manual input or physical-device acceptance. Paths are under
`Artifacts/QA/UI01/20261003-`:

| Run suffix | Viewport | Proof |
| --- | --- | --- |
| 054319-packaged-capture-initial | 884x1780 | initial/reference comparison |
| 054333-packaged-capture-selected | 884x1780 | selected C |
| 054343-packaged-capture-correct | 884x1780 | correct A/disabled reading |
| 054353-packaged-capture-wrong | 884x1780 | wrong B/disabled reading |
| 054403-packaged-capture-initial | 1768x3560 | 2x viewport |
| 054414-packaged-capture-initial | 260x640 | narrow, safe .9 |
| 054425-packaged-capture-focus | 844x390 | landscape focus, safe .9 |
| 054435-packaged-capture-large | 390x844 | 200%, safe .9 |
| 054445-packaged-capture-longfocus | 390x844 | long answers, 200%, safe .9 |
| 054455-packaged-capture-longselectedfocus | 260x640 | long selected B, 200%, safe .9 |
| 054506-packaged-capture-correct | 390x844 | 200% correct/feedback, safe .9 |
| 054517-packaged-capture-wrong | 390x844 | 200% wrong/feedback, safe .9 |
| 054528-packaged-capture-actions | 390x844 | 200% actions, safe .9 |
| 054539-packaged-capture-keydisabled | 390x844 | routed disabled navigation, safe .9 |
| 054550-packaged-capture-keyretry | 390x844 | routed retry/200% focus, safe .9 |

`reading-font-batch.py`/`.json` and `reading-font-capture-verification.json` retain
case metadata/checks. The first capture SHA-256 is
`8020aa8fd1a096301401ce15c1e2f138397cd752f0775437a63ef7f79f719c47`.
Both real `WordQuest.Context` tests passed on clean `81418d0`, zero failures/skips,
in `20261003-053751-automation-initial`.

Missing-Bold fallback `20261003-053606-capture-large` passed at 390x844, safe .9,
200%, with expected missing-package warning, complete native evidence and an
inspected readable default-family capture. Only the owned new Bold asset was
temporarily moved within the workspace and restored in `finally`, with exact
hash `ddb17ec624e8c6e8d68b607cbbd14e5302111b07e158074cc101e69de0a78715`.
Its metadata honestly records the temporary deletion. `reading-font-fallback.json`
retains restoration details. This is an editor omission test, not corrupt-package
handling or phone evidence.

## Reference comparison and limits

Read-only `reading-font-analysis.py` / `.json` reproduce the matched-size navy
threshold bounds, diagnostic text crops and 50% original/native overlay. Original
and input capture hashes remain unchanged. All four measured roles improve:

| Role | Original bounds | Prior native | New native |
| --- | --- | --- | --- |
| Word | 450x71 | 422x64 | 445x69 |
| Clue first line | 536x26 | 556x28 | 537x26 |
| Prompt | 508x32 | 515x34 | 510x30 |
| Answer A | 397x30 | 447x34 | 397x30 |

This measures glyph extents in fixed regions with R<65/G<60/B<125, not exact font
identification or a global fidelity score. Letterforms/kerning/vertical offsets
and color still differ. Mode lettering remains byte-identical to prior native
pixels in its diagnostic crop. Other supplied art, fonts and fixtures are unchanged.

There are 602,396 changed pixels versus the prior initial capture, due to live
type and measured reading reflow/panel resampling. Changes remain within the
reading panel/fringe region [45,508,840,1649) plus the viewport end-shadow band
[0,1772,884,1780); zero changes elsewhere. The band has 4,727 changed pixels with
at most 7/255 channel difference. This is consistent with Slate's end-of-scroll
shadow changing as the measured content extent crosses the viewport height;
that explanation is inferred from `SScrollBox::GetEndShadowOpacity` and the native
difference location. No background source pixels were edited. The comparison does
not claim that only font pixels changed or that every layout anchor is exact.

Dedicated read-only review is pending. Simplified art, exact lettering/type/color,
editorial/manual accessibility, UI02 motion, real-phone/offline/performance and
release gates remain open. No new H/I work, deployment or release is included.
Fresh prerequisite check still finds no Android engine target and adb lists no phone.
