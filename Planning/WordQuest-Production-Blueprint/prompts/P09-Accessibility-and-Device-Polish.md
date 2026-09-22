# P09 — Accessibility and Device Polish

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P08

**Read:** 05-UX-and-Accessibility.md; 11-QA-Performance-and-Research.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Perform a focused accessibility and device pass on the actual slice. Test large text/reflow, screen-reader labels and focus on the target platforms, touch targets, visible keyboard focus, tap alternatives, no-colour/no-audio completion, reduced motion, subtitles and interruption handling. Identify engine limitations with actual reproduction evidence.

Profile sustained gameplay and scene transitions. Fix measured CPU/GPU/layout/overdraw/texture costs before adding more effects. Exercise low storage, slow/absent connection, backgrounding and native keyboard variants. Preserve teaching clarity while optimizing.

## Required deliverables and pass conditions

Deliver completed accessibility matrix and performance captures by named device/build, plus remaining defects with severity and fixes. Demonstrate all core modes without timing or drag dependence. Required failures block G3; do not substitute a desktop mockup for physical-device behavior.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P09/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.
