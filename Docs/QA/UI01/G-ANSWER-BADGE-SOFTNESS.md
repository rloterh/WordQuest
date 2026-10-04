# G answer badge fill and rim refinement

PR #38 is merged at `04a14fb`. This bounded UI01 correction refines the existing
editable badge's darker upper band and concentrated rim against the immutable G
gameplay reference. It does not accept final art or expand the proof's scope.

## Source

`ArtSource/UI/G/Vector/G-Answer-Badge-v002.svg` stages to the existing raw runtime
resource `Game/Content/UI/G/Vector/G_AnswerBadge.svg`. The 70x70 canvas, centered
34-radius face and maximum 34.75-radius outer extent remain. A lighter four-stop
lilac gradient and two low-opacity rim layers replace the single 1.5-width stroke.
The preserved v001 master has SHA-256
`bb6b04596b5dfbdf725c9890fba888880e6e9423a8697efabc6b6ebdc062c8a8`.
New source/runtime SHA-256:
`c857ad37c5ee85b8ebb0878247efbe8c47118a7cf3ffff144e93ea0d6cfc2967`.
The staging helper selects v002; explicit LF attributes retain exact parity.

No C++, new font, texture import, binary asset or package setting changes.
Existing live A-D letters, 70-reference-unit/32-unit-minimum sizing, 200% scaling,
selected navy border/marker, row focus and disabled feedback remain native.
Missing SVG retains the existing solid native badge. SVG decoration remains
noninteractive and excluded from assistive naming. Scoring/draft fixtures are
unchanged. The original reference remains the authority.

A separate built-in imagegen spirit extraction was rejected for broad headband,
altered facial details and alpha residue. Exact prompt/output hash/disposition:
`ArtSource/Companions/G/Reconstruction/G-Spirit-Reconstruction-20261004-ATTEMPT.md`.
Neither that output nor changes to the current spirit are imported/committed.
This badge revision is authored SVG; no imagegen/raster paintover is used for it.

## Preliminary verification

Editor build check: `Artifacts/Logs/Build/WordQuestEditor-20261004-122053.log`,
exit 0, zero actions, 8.30 seconds (warm check, not new native compilation).
All 67 existing Python QA checks, eight staged SVG pairs and six original reference
hashes pass. Git LFS is available; this increment adds no binary art.

Dirty editor capture `20261004-122135-capture-initial/native.png` was inspected
at 884x1780 alongside the original and PR #38's native baseline
`20261003-151412-packaged-capture-initial/native.png`.
The fill is more uniform at the top and lower rim remains visible. Native vector
edges/letterform and exact original softness still differ; no visual acceptance
is claimed. The process exits 0; requested dimensions, initial state and native
option cues pass. Clean packaged evidence is pending.

Read-only comparison changes 12,777 pixels, bounds [137, 1000, 207, 1406),
all within the four badge regions; no pixels outside those regions change.
Six fixed 5x5 interior medians at x158, offsets 8/16/28/40/52/60 avoid the letter
and rim. Reference top is 1003, native top 1000; this documented 3px alignment
does not move the UI. Mean absolute channel difference falls from 1.33 to 0.61.
Opaque navy ink against those six final fill samples has minimum contrast 9.60:1.
These small local samples do not measure rim softness, antialiased text, all-state
contrast, manual accessibility or overall fidelity. Raw comparison/crops and
50% overlay are under `Artifacts/QA/UI01/BadgeMaterial`.

Omission capture `20261004-122656-capture-longselectedfocus` (390x844, simulated
0.9 safe area, intrinsic 200% text) exits 0 and passes state, option cues, text/
action content and leading selected-answer visibility checks. Its PNG was inspected:
solid native B badge/live letter, navy selected ring and `>` marker remain visible
at the start of the long answer; content scrolls. Only the owned runtime SVG was
moved to an ignored holding path, then restored in `finally` to its exact hash.
The parity helper correctly failed while absent. Raw record:
`Artifacts/QA/UI01/BadgeMaterial/fallback.json`. This is a dirty Editor omission
test, not packaged corruption or manual/device accessibility acceptance.

## Clean packaged verification

Tested runtime/package source: clean
`5bb13608ab8287a6f4c5016cf11cbb539fd8f49a`.
`python Tools/BuildScripts/package_g_win64.py` passes the real Editor/Game checks
with zero actions (2.59/3.01 seconds; no fresh C++ compilation is claimed).
Full Win64 Development build/cook/stage/archive passes; 518 packages,
zero cook errors/warnings, BuildCookRun 160.51 seconds. Package:
`Artifacts/Packages/Win64/20261004-122858-730711`.
Manifest SHA-256:
`f4d8b5dbcc0b83986f6749476065f890f7b711e6a9a6bc5db792a472713863ef`.
Head/worktree/input invariants and all 49 payload size/hash checks pass.
Automatic local firewall refresh covers the exact new packaged executable at
12:32:47.0458184 UTC on the second identical bounded task invocation; no new
firewall policy, protected task or privileged installer is changed here.

Corrected UnrealPak extraction exits 0; all 876 badge bytes match master/runtime,
with the recorded hash. The first verification command mistakenly used
`-Extract=directory`; this tool treated it as creation and refused the existing
pak (exit 1). That failed log is retained as `BadgeExtract.log`. Using the
documented separate arguments `-Extract <directory>` succeeds, recorded in
`BadgeExtract-corrected.log`. All archive hashes were rechecked before the
corrected invocation, and the pak hash remains unchanged afterward.
The failed verification command is not a failed application build or accepted
extraction result. Raw verification script/result:
`Artifacts/QA/UI01/BadgeMaterial/verify.py` and `verification.json`.

All runs below exit 0, verify the matching package hashes, pass their requested
state/dimension/native cue checks and record clean `5bb1360` source. Every PNG
was viewed, including the actual high-resolution image (the viewer displayed a
1017x2048 resize; raw dimensions are 1768x3560). Runs live under
`Artifacts/QA/UI01`; .9 denotes simulated safe-zone ratio, not a phone inset test.

| Run | Proof | Window / text / safe zone |
| --- | --- | --- |
| `20261004-123324-packaged-capture-initial` | Unselected initial | 884x1780 / 100% / 1 |
| `20261004-123347-packaged-capture-selected` | Selected C, separate ring/marker | 884x1780 / 100% / 1 |
| `20261004-123402-packaged-capture-correct` | Correct A, disabled options, explanation | 884x1780 / 100% / 1 |
| `20261004-123417-packaged-capture-wrong` | Wrong B, disabled options, explanation | 884x1780 / 100% / 1 |
| `20261004-123432-packaged-capture-initial` | High-resolution initial | 1768x3560 / 100% / 1 |
| `20261004-123451-packaged-capture-initial` | Narrow initial, scrollable actions | 260x640 / 100% / .9 |
| `20261004-123506-packaged-capture-actionfocus` | Focused Check, actions revealed | 260x640 / 100% / .9 |
| `20261004-123521-packaged-capture-actions` | Landscape enlarged actions | 844x390 / intrinsic 200% / .9 |
| `20261004-123537-packaged-capture-hint` | Assisted correct feedback | 390x844 / explicit 200% / .9 |
| `20261004-123552-packaged-capture-longfocus` | Focused long B, leading content visible | 390x844 / intrinsic 200% / .9 |
| `20261004-123607-packaged-capture-longselectedfocus` | Selected/focused long B | 260x640 / intrinsic 200% / .9 |

Both existing Unreal `WordQuest.Context` tests pass, zero failed/not-run/in-process,
exit 0, clean source, in `20261004-123719-automation-initial/Report`.
The final native initial PNG matches preflight exactly, SHA-256
`7e431bf97c79a3f853dafdacdd7f8e3af8bfd35b11150afa7b945f86c26781b0`.
The scoped comparison reproduces the recorded pixel/sample results. Original,
baseline and final crops and the 50% overlay were inspected; remaining letter,
edge and companion mismatches are visible. The overlay is diagnostic, not proof
of accepted fidelity or a runtime image. Earlier v001 badge, spirit source and
genuine spirit asset retain their original hashes; no binary asset changes.

Dedicated read-only review against actual `origin/dev` is pending. Subsequent
evidence/review/publication records change documentation only; tested runtime
remains `5bb1360`. None of these checks authorizes a merge.

## Remaining gates

Full UI01 material/brand/companion identity, editorial fixture approval, UI02
motion, manual/platform input and screen reader, Android/phone, isolated offline
play, performance and all original release gates remain open. Fresh local checks
still find no same-engine Android platform receipt; adb lists no physical device.
Installed Android Studio does not supply the missing Unreal platform.
