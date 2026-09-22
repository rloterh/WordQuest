# P05 — Learning and Durable Saves

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P04

**Read:** 03-Curriculum-and-Mastery.md; 08-Technical-Architecture.md; 11-QA-Performance-and-Research.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Implement per-sense/per-skill evidence and the initial deterministic scheduler. Keep encounter/recognition/recall/application/retention rules distinct. Store assistance, contexts and timestamps so hints and instant repetition cannot inflate mastery. Build a capped daily queue and introduce new senses conservatively.

Implement attempt journal, snapshots, backups, schema versions and safe session checkpoints. Persist before celebration/reward and support kill/relaunch at each transaction boundary. Handle device clock changes without repeated daily grants. Define migration and unknown-newer-save behavior. Connect mission progression and restoration grants with exactly-once IDs; knowledge evidence must remain separate from game score.

## Required deliverables and pass conditions

Test guided-correct versus unaided, recognition versus recall, distinct contexts, 7-day rule using controlled clocks, queue limits, duplicate grant prevention, corrupted snapshot fallback and interrupted writes. Demonstrate airplane-mode play and relaunch continuity on device. Deliver migration fixtures and a scheduler replay report.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P05/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.
