# Native QA verdict integrity

After the owner merged PR #19 into `dev` at `b02a7cc`, the next bounded UI01
follow-up fixes verification metadata. Previously a native crash/nonzero exit or
600-second timeout after writing a valid capture/report returned command failure
but could persist `evidence_complete: true`. A reader using that field alone
could treat incomplete execution as successful evidence. Automation also accepted
two successes with nonzero or missing unfinished-test counts.

`run_g_proof.py` now requires native exit zero before persisting complete evidence.
Automation additionally requires `failed`, `notRun` and `inProcess` all explicitly
zero. Existing state, dimensions, routed input, focus and answer-start contracts
remain in force. Gameplay, imported assets and engine-generated files are unchanged.

## Verification

Clean implementation `38d34a70169f760498d9c8751bac2b08570bfd93`:

- Four runner-level regression tests exercise saved `run.json` and CLI return values,
  using synthetic late failure/timeout and unfinished-report fixtures. The actual
  `origin/dev` baseline produces eight expected failing subcases, no errors;
  successful baseline cases still pass. Raw baseline:
  `Artifacts/QA/UI01/G-Proof-Evidence-Baseline.log`. These fixtures are not native
  screenshots, real crashes, timeout measurements or visual evidence.
- All 31 Python tests pass: `python -m unittest discover -s Tools/QA -p 'test_*.py'`.
- Real editor target check passes, up to date, zero actions, 1.28 seconds, exit 0:
  `Artifacts/Logs/Build/WordQuestEditor-20261002-121210.log`.
- Fresh native automation passes both `WordQuest.Context` tests with failed,
  notRun and inProcess zero; exit 0 and complete verdict:
  `Artifacts/QA/UI01/20261002-121226-automation-initial`.
- Fresh editor-backed 884x1780 initial capture passes state/dimensions/exit and was
  visually inspected: `Artifacts/QA/UI01/20261002-121302-capture-initial`.
- The corrected helper also passes a fresh 390x844 simulated safe-area 0.9
  `keydisabled` check against the existing PR #19 Win64 package, with seven routed
  steps, focus/visibility and final state passing; PNG visually inspected:
  `Artifacts/QA/UI01/20261002-121405-packaged-capture-keydisabled`.
  All 48 archived payload hashes were verified before launch. Package source is
  `55ce793a6e43a3e4443480560419fa19823f84b8`; its entire tracked `Game` tree equals
  the current tree. Manifest SHA-256:
  `6289b6a95de4695d96fa8e8f64882fe2f68d662635cd3730940213832ea5bbb5`.
  No new game compilation/cook/archive is claimed for this Python-only correction.
- Six original references, seven source/runtime SVG pairs, LFS status and whitespace
  checks pass. Native logs show no Error/Fatal lines. Editor capture retains engine
  TSR, editor-widget registration and template SpawnActor warnings; packaged capture
  retains the existing TSR/SpawnActor warnings. This is not a warning-free claim.

Dedicated read-only Codex review at clean
`1f3b7f3fa604d0526fbfe50ab3ac0172a1fd74f5` against actual `origin/dev`,
`b02a7cc1263ea4d96653c47ec5067f80cb3acfbd`, completed with exit 0 and no
actionable introduced defects. Head/worktree stayed unchanged. Raw evidence:
`Artifacts/Reviews/20261002-121513`. Tests were not rerun in the read-only review
environment; connector startup/permission diagnostics do not constitute test
results. Subsequent review/publication records change documentation only.
[PR #20](https://github.com/rloterh/WordQuest/pull/20) was merged by the owner into
`dev` at `7cc53bfd389d9e71879d28faae1da18958833a96`,
2026-10-02 13:23:01 UTC. GitHub has no configured
status checks; the local evidence above supplies the recorded validation.

## Art experiment and gates

Two built-in imagegen companion extraction attempts were inspected and rejected
for changed crest, expression and lantern proportions. No new PNG was adopted or
imported; original reference and existing companion texture remain unchanged.
[Exact prompts and hashes](../../../ArtSource/Companions/G/Reconstruction/G-Spirit-Extraction-20261002-PROMPTS.md)
are retained; rejected local files/alpha inspection remain ignored under
`Artifacts/QA/UI01/g-spirit-rejected-after-pr19`.

Static fidelity, manual/platform accessibility, fixture editorial approval,
phone/offline, performance, UI02 motion and release acceptance remain open.
