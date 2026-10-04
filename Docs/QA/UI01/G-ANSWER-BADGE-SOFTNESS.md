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

## Remaining gates

Full UI01 material/brand/companion identity, editorial fixture approval, UI02
motion, manual/platform input and screen reader, Android/phone, isolated offline
play, performance and all original release gates remain open.
