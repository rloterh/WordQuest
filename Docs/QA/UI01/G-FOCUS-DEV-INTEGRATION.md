# Integrate the owner-merged G focus correction into dev

GitHub confirms owner merges on 2026-10-02 (UTC):

- PR #15: base `dev`, 10:32:08, merge `551a085a8d9a9cd75d0b4dd1793cef7c04427810`.
- PR #16: base `feature/g-answer-badge-material`, 10:32:56, merge
  `032f3b21a6c323a67f22ff5a24e9d3d8ccb3fd8b`.

The latter merge happened after #15, so Git ancestry and the actual diff confirm
that #16's focus correction is not on `origin/dev`. Both closed PRs remain intact.
Branch `feature/g-focus-dev-integration` starts at `origin/dev` (`551a085`) and
locally integrates the owner's merged feature branch. It does not merge remotely,
deploy, release or introduce new gameplay/art. The owner retains merge authority.

## Identity and verification

Clean integration source: `d17f909ce515bc78f670067bbd18a70b9f930613`.
Its `Game` tree is exactly identical to tested implementation `7e68d60`, Git tree
`0a3199112ffadb093cefc8867c311c25f4a71504`. Its `Tools/QA` tree also matches,
`78ee356d52300685bfed4647f883988ece8bd69b`. No binary assets, original references,
fixture, scoring, generated project structure or toolchain settings change.

The full Win64 package and 24 capture checks recorded in
[oversized-answer focus](G-OVERSIZED-ANSWER-FOCUS.md) remain evidence for that
identical implementation. Packaging/Game-target checks were not repeated during
this integration; no new archive is claimed.

Fresh checks on the clean integration head:

- Real editor target: six actions, 14.77 seconds, exit 0;
  `Artifacts/Logs/Build/WordQuestEditor-20261002-103453.log`.
- Native selected oversized answer: `20261002-103539-capture-longselectedfocus`,
  844x390, 200%, badge/selected marker/first line visible, state/dimensions/leading
  gate pass, exit 0. Optional desktop tooltip suppression recorded in metadata.
- Native submission/Pause regression: `20261002-103557-capture-keydisabled`,
  390x844, simulated 0.9 inset, all state/key/focus/final visibility gates pass,
  exit 0. Normal tooltip behavior retained.
- Both PNGs were directly inspected. The remaining oversized text still needs
  scrolling; this is not whole-row or physical-input acceptance.
- Two Unreal context tests pass, zero failed/not run, exit 0;
  `Artifacts/QA/UI01/20261002-103615-automation-initial`.
- All 27 Python tests pass. All six supplied reference hashes pass unchanged.
  Diff whitespace check passes.

Capture directories above live under `Artifacts/QA/UI01`; raw evidence stays
local and ignored. Dedicated read-only review against `origin/dev` is pending.

Static art fidelity, manual/platform accessibility, editorial approval,
phone/offline, performance, UI02 motion and release gates remain open. The screen
still uses a single draft EQUIVOCAL fixture and prototype `3 / 7` progress.
