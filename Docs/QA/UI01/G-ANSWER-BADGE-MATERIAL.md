# G answer badge material candidate

After the owner merged PR #14 at `3312e95`, this bounded UI01 increment adds
an editable shaded disc behind the existing live A–D letters. The original G
reference has a softer blue-lilac fill and pale lower rim than the previous solid
native badges. The original reference remains the visual target; this is a
reconstruction candidate, not accepted final art or a new visual direction.

## Source and native integration

`ArtSource/UI/G/Vector/G-Answer-Badge-v001.svg` is a hand-authored 70x70 vector
disc with explicit percentage-based gradient coordinates. It contains no letter
or learning content. Unchanged runtime copy:
`Game/Content/UI/G/Vector/G_AnswerBadge.svg`; both SHA-256:
`bb6b04596b5dfbdf725c9890fba888880e6e9423a8697efabc6b6ebdc062c8a8`.
The existing staging/parity helper now handles seven resources. Existing masters,
raster sources, Unreal binary assets and all supplied references are unchanged.
No raster editing, original-pixel extraction or image generation was used.
Git explicitly retains LF for these two new SVGs so their documented bytes remain
stable across checkouts; no existing SVG/reference line-ending policy is changed.

Each existing answer badge size box now contains an overlay: a noninteractive
Slate vector image and the existing native border/live letter. The selected navy
border, `>` selection marker and answer-button outline remain separate state
cues. No correctness cue appears before submission. Missing SVG collapses only
the decoration and restores the original solid fill/edge; selection still works.
The ornament is excluded from hit testing/accessibility; the answer button retains
its semantic label and interaction region. Native screen-reader service acceptance
is unverified.

Existing badge diameter (70 reference pixels, 32-unit minimum), 200% scaling,
letter font, row measurements, focus routing, scoring, draft fixture and actions
are unchanged. `/Game/UI/G` cook inclusion and `UI/G/Vector` UFS staging already
cover this resource; no packaging setting was changed. No `.uasset` was fabricated
or imported for this SVG path.

## Preliminary native comparison

The real editor build passed: six actions, 12.93 seconds, exit 0.
Log: `Artifacts/Logs/Build/WordQuestEditor-20261002-082005.log`.
Dirty candidate native runs `20261002-082052-capture-initial` and
`20261002-082202-capture-selected` both exited 0 at 884x1780 and passed their
expected state tuples/dimensions. Direct inspection against the immutable original
shows lighter discs and pale rims, with separate live letters; selected C retains
the navy ring, marker and row outline without evaluation. The native and original
font/material edges still differ; this is not UI01 acceptance.

Read-only RGB comparison against prior packaged native
`20261002-050724-packaged-capture-initial` finds 14,845 changed pixels, all inside
the four badge regions (union bounding box x137..206/y1004..1409). Outside those
regions the captures are identical. Twelve documented first-badge interior points
(x148/154/188/196 crossed with y1024/1036/1048) avoid the live letter; their mean
absolute RGB-channel difference from the original decreases from 10.56 to 0.83
on the 0..255 scale. This is a small local color sample, not a global fidelity,
contrast or acceptance score. Exact points/colors, image hashes and exclusion
regions are in `Artifacts/QA/UI01/G-Answer-Badge-Comparison.json`.

Missing-SVG fallback was inspected in dirty editor run
`20261002-082401-capture-focus`, 390x844 with simulated 0.9 inset: original solid
badges/live letters and focused B remain intact, with no selection/evaluation,
correct dimensions and exit 0. Only the new owned runtime SVG was temporarily
moved within the workspace; parity correctly failed (exit 1), and the exact bytes
were restored in `finally`. Context is retained in
`Artifacts/QA/UI01/BadgeFallback/fallback-context.json`. This is an editor omission
test, not packaged corruption or physical-device evidence.

## Clean cooked verification

Clean source `b7426996cf614f24f342c2571c6dc39bc40f7e9e` passes the editor target,
Win64 Development game build (five actions, 18.80 seconds), full cook, stage and
archive. Package: `Artifacts/Packages/Win64/20261002-082621-605383`.
Editor/UAT exits 0; head, worktree and recorded input invariants are unchanged.
UAT completed in 78.13 seconds, including a transient local Zen connection error
that its built-in staging retry recovered. No engine/security setting was changed
and no bypass was added. Successful staging is recorded after that recovery.
Manifest SHA-256:
`3dc11ad3edec8966e0de9c46f6777abe89e308004d9f318dcd322f8ce1ce6e93`.

UnrealPak extracted `Content/UI/G/Vector/G_AnswerBadge.svg` (exit 0): all 712 bytes
match both source and runtime SVG, with the SHA-256 recorded above. The archive pak
retains its manifest hash. `BadgeExtract.log` and `CookedBadge.json` retain evidence.

All nine clean candidate packaged runs below exit 0, pass requested dimensions
and state checks, verify the archive's payload hashes and were directly inspected.
Metadata records source/package `b742699` with a clean worktree. Raw runs are under
`Artifacts/QA/UI01/`; only the simulated inset runs use 0.9 safe-zone ratio.

| Run | Window | Inspected observation |
| --- | --- | --- |
| `20261002-082919-packaged-capture-initial` | 884x1780 | Four shaded badges with live A–D; no selection/evaluation |
| `20261002-082930-packaged-capture-selected` | 884x1780 | C retains ring, marker and row outline; no evaluation |
| `20261002-082939-packaged-capture-hint` | 390x844, inset | Assisted A, one evaluation; selected ring and disabled badge/letter treatment |
| `20261002-082949-packaged-capture-longfocus` | 390x844, inset | 200% artificial long-answer stress; circular enlarged badges and focused B |
| `20261002-082958-packaged-capture-longfocus` | 844x390 | 200% artificial long-answer stress; oversized B row partially visible (limit below) |
| `20261002-083008-packaged-capture-initial` | 260x640, inset | Minimum-size circular badges, wrapped live options |
| `20261002-083118-packaged-capture-keybuttons` | 390x844, inset | Native Space activates B and Check; repeated Enter leaves one evaluation |
| `20261002-083128-packaged-capture-keytab` | 390x844, inset | Per-key enabled-control traversal and final Hint visibility pass |
| `20261002-083235-packaged-capture-focus` | 844x390 | 100% focused B row and badge fully visible |

The 200% artificial long-answer landscape row exceeds the viewport height; its
badge top is clipped at this scroll position. It is not full-row visibility or
responsive acceptance. Baseline packaged run
`20261002-083402-packaged-capture-longfocus` uses the prior package from `c15ddfd`
(runtime identical to merged `3312e95`) and reproduces the same layout/clipping.
Read-only comparison finds differences only in badge pixels
(x131..264/y0..122), with all other RGB pixels identical; evidence:
`G-Answer-Badge-Landscape-Stress.json`. Long content remains scrollable, while
manual navigation/readability qualification is pending. No new layout regression
is observed. The separate 100% landscape capture exposes the complete focused row.

`keybuttons` passes its routed per-key state checks; `keytab` additionally passes
focus/settings and final focused-control visibility checks. These use synthetic
Slate events, not physical keyboard input or screen-reader certification.
An initial batch invocation used the nonexistent mode `keyactivate`; argument
validation rejected it before launching the game. It was corrected to the existing
`keybuttons` mode above, with no product code change.

Both existing Unreal tests pass at the same clean source: two succeeded, zero
failed/not-run/in-process, exit 0, in `20261002-083137-automation-initial`.
All 22 existing Python tests, six original-reference hashes, seven SVG parity pairs,
LFS integrity and whitespace checks pass. Later
changes record evidence and the two new SVGs' Git LF policy; runtime/source and
physical SVG payload bytes remain unchanged from the tested package.

## Internal review

Dedicated Codex read-only review of clean
`98d22a180f548355a371229cc16faf594a0ab2d4` against actual `origin/dev` base
`3312e95ecb544f2215da9f60c4213f41ccaef072` completed with exit 0 and no actionable
introduced defects. Head/worktree stayed unchanged. The reviewer independently
checked seven SVG parity pairs, six original-reference hashes and diff whitespace;
Unreal builds and runtime/device checks were not independently rerun. Raw evidence:
`Artifacts/Reviews/20261002-083656`. Optional connector startup/shutdown warnings
did not prevent review completion. Subsequent commits record review/publication
only. Review does not authorize merge or replace art/device acceptance.

## Remaining gates

Exact badge/answer-skin material and typography acceptance, companion identity,
panel/brand finish, fixture editorial review, manual pointer/keyboard/screen-reader,
phone/offline, performance, UI02 motion and release gates remain open. The screen
still contains one draft EQUIVOCAL question; `3 / 7` is prototype fixture progress.
Raw captures/logs remain local and ignored under `Artifacts`.
