# G minimum-font enlargement and action wrapping

After owner-merged PR #22 (`9107ff2`), submitted-outcome verification exposed a
text-scaling defect. Applying the minimum font size after scaling meant small-window
text did not double at the 200% setting. Rounding after scaling could also change
the ratio. Learning text, answer letters/cues and action labels now enlarge their
actual rounded normal font size, after its readability floor. For example, at
390x844 with simulated safe-area .9, feedback now uses 11 then 22 font points;
action labels use 12 then 24. Brand, progress and Pause-modal typography retain
their existing treatment; this is not a claim that every screen element scales.

The larger submitted label then exposed horizontal overflow. Enlarged action
labels now wrap within the stacked button's content width, accounting for the
icon, spacing and both padding layers. Measured content determines button height.
Per-character wrapping handles a word too wide for the available width. Normal
size keeps the prior unwrapped layout. No font, art, fixture, scoring, supplied
reference or engine-generated project file is replaced.

Development captures add `--large-text` for initial/selected/correct/wrong/hint/empty
states. It requires actual 200% setting metadata and measured action-content fit.
Unsupported modes reject the flag. Actual font point sizes are logged for ten
roles; paired native runs verify the ratio independently of the setting label.
The native proof additions remain excluded from Shipping builds.

## Build and package

Final clean implementation: `c403030038ef11645475c6e6b5be52826302044d`.
Real editor build: 4 actions, 7.39 seconds, exit 0,
`Artifacts/Logs/Build/WordQuestEditor-20261002-162729.log`.
Clean package editor preparation: 3 actions, 4.20 seconds, `...-163043.log`.
Full Win64 Development build/cook/stage/archive passed: game target 5 actions,
20.79 seconds; BuildCookRun 77.12 seconds; UAT exit 0.

Package: `Artifacts/Packages/Win64/20261002-163043-861386`.
Manifest SHA-256:
`43e5778e42f47ef8fde9720b972a3835a539fcc5cf8c0b40ce3ccc02a3965402`.
All 48 archived payload hashes are recorded and checked before every launch.
Head/worktree/input invariants pass; generated outputs remain ignored.

Preliminary package `20261002-160641-450238` and its 12 captures in
`G-Large-Outcome-Batch.json` predate the scaling correction and are excluded from
final acceptance. Dirty editor capture `20261002-162044-capture-correct` shows
the enlarged submitted label overflow before wrapping. Editor build `...-162516.log`
failed on a local `Padding` variable shadowing UUserWidget's member; it was renamed
to `ContentPadding`. Capture `20261002-162606-capture-correct` launched the older
compiled module after that failed build and was correctly rejected for missing
action-fit metadata. The subsequent rebuild and dirty preflight
`20261002-162811-capture-correct` passed before final clean packaging.

## Native evidence

All 17 fresh packaged captures pass at the final clean implementation, with checked
hashes, state/cue/exit/dimensions contracts and no Error/Fatal log lines. All PNGs
were visually inspected. Every run's measured Hint/Submit content fits its button.
Feedback checks require its full bounds when it fits, or its first line when it
exceeds the viewport. Existing keyboard/focus/answer-start contracts pass where
applicable. Runs are under `Artifacts/QA/UI01`; metadata is
`G-Large-Outcome-Final-Batch.json`.

| Run prefix (20261002-) | Proof / dimensions / text | Evidence |
|---|---|---|
| 163404 | correct, 390x844, safe-area .9, 200% | Full explanation; submitted label wraps inside button |
| 163415 | wrong, same | Cross visible on B; full explanation |
| 163424 | hint, same | Full assisted explanation; wrapped submitted label |
| 163434 | empty, same | Full choose-answer instruction; enabled action groups fit |
| 163443 | correct, 844x390, safe-area .9, 200% | Oversized explanation starts at first line |
| 163453 | wrong, same | Oversized explanation starts at first line |
| 163503 | hint, same | Oversized assisted explanation starts at first line |
| 163512 | empty, same | Full instruction and fitted action content |
| 163522 | hint, 260x200, safe-area .9, 200% | Extreme short viewport: oversized feedback starts at first line |
| 163532 | initial, 884x1780, 200% | Enlarged reading composition retained; content extends below viewport |
| 163542 | initial, 884x1780, 100% | PNG byte-identical to PR #22 |
| 163552 | correct, same | PNG byte-identical to PR #22 |
| 163602 | correct, 390x844, safe-area .9, 100% | Normal-size baseline for four narrow outcomes |
| 163612 | correct, 844x390, safe-area .9, 100% | Normal-size baseline for four landscape outcomes |
| 163622 | hint, 260x200, safe-area .9, 100% | Normal-size baseline for short viewport |
| 163633 | keyretry, 390x844, safe-area .9 | Routed 200% toggle/retry clears result/Hint; selected A and focus remain visible |
| 163642 | longselectedfocus, 260x640, safe-area .9 | 200% long B retains visible option letter/cue/first line; oversized rest extends beyond viewport |

Nine paired comparisons cover the four narrow outcomes, four landscape outcomes
and short-viewport assisted outcome. All ten actual font-size roles are exactly
twice their normal counterparts: mode, word, clue, prompt, first answer label,
marker, letter, Hint label, Submit label and feedback. Data:
`G-Large-Outcome-Font-Comparison.json`. This checks configured native font sizes,
not OS accessibility services or a claim that physical glyph bounds double.

The two 100% reference-size comparisons have zero changed pixels and byte-identical
PNGs: `G-Large-Outcome-Normal-Comparison.json`. Initial SHA-256 remains
`7aa62165b992c5599f993e3947bc5572ce901fde239e1290a34920addec1b99e`; correct outcome
SHA-256 remains `595d4f94ca9452af4b8a22d27b2424d5ee5d2f75f050d9aceb065f20fb948406`.
Reference-size captures suppress tooltips; other captures use normal tooltips.

Both `WordQuest.Context` Unreal tests pass with failed/notRun/inProcess zero:
`20261002-163742-automation-initial`. All 49 Python tests pass, including refusal
of missing/normal-scale enlarged evidence and clipped/missing/duplicate action-fit
metadata. Six original reference hashes, seven SVG pairs, LFS and whitespace checks
pass. Dedicated read-only Codex review completed at clean
`84108bc7f40bd0ded919da5d4b277e30149b0d03` against actual `origin/dev`,
`9107ff22056e94886913b7fc8f1d54e92ab36de2`, exit 0 and no actionable introduced
defects. Head/worktree stayed unchanged. The reviewer independently passed 39 QA
tests and the diff whitespace check; it did not independently rerun engine builds,
captures or physical-device gates. Raw evidence: `Artifacts/Reviews/20261002-164119`.
Subsequent review/publication records change documentation only.
[PR #23](https://github.com/rloterh/WordQuest/pull/23) targets `dev` and is ready
for owner review. GitHub has no configured status checks; validation above is local.

## Limits

These are bounded synthetic native captures and input routes. Offscreen portions
of oversized content require scrolling; manual touch/keyboard scrolling to every
line and action, real platform screen readers, physical text/target sizes and
contrast acceptance remain unverified. The short viewport is a stress case, not
a supported phone-size claim. Correct/assisted selected A may be above the viewport
after revealing its full enlarged explanation; cue metadata is not a claim that
every result cue remains simultaneously visible with feedback.

Art fidelity, draft fixture editorial approval, physical-phone/offline, real OS
interruption, performance, UI02 motion and release gates remain open. Android
support receipt is still absent and adb lists no device on this turn's recheck.
No agent merge, deployment or release is performed.
