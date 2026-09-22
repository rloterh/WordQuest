# P19 — Release Rehearsal

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P18; candidate identifiers frozen

**Read:** 14-Release-and-Operations.md; ../templates/RELEASE-CHECKLIST.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Rehearse production operations in the appropriate nonpublic environment: compatible content rollback, optional-feature disable, failed sync recovery, purchase incident triage, backup restore, monitoring alerts and support intake. Verify clean build reproducibility and archive commit/content/config/toolchain identifiers.

Run the release checklist against concrete evidence. Distinguish content rollback, backend rollback and store binary replacement. Ensure no migration makes a rollback unsafe without a documented recovery plan. Recheck final free/purchased/offline experience.

## Required deliverables and pass conditions

Deliver rehearsal log, rollback/recovery commands appropriate to actual infrastructure, monitoring ownership, support runbook and candidate release dossier. No real user data destruction or unapproved public rollout. Every unchecked checklist item has a disposition and owner.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P19/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.
