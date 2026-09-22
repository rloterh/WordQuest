# P03 — Content Schemas and Validation

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P02

**Read:** 03-Curriculum-and-Mastery.md; 09-Data-and-Content-Pipeline.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Implement versioned JSON schemas and cross-record validation for senses, challenges, missions and manifests. Use example fixtures only as drafts. Enforce stable IDs, skill/mode enums, answer references, accepted variants, tile multiset correctness, prerequisite DAG, coverage and release-only editorial/rights/audio requirements. Build a deterministic importer into engine-consumable assets without hand-editing production data in multiple places.

Create a 30-sense prototype batch with the curriculum lead. AI drafts are clearly marked; route them to human review. Keep a held-out transfer item per sense and detect obvious duplicate contexts. The tool must reject unapproved release exports while allowing draft previews. Produce actionable errors with record ID and field path.

## Required deliverables and pass conditions

Run valid and intentionally invalid fixtures including repeated letters, duplicate IDs, multiple answer ambiguity flags, dangling references and missing release approval. Demonstrate draft preview, approved export and deterministic reimport. Deliver schema, validator, importer, editorial queue, coverage report and human-review status. Do not claim all prototype content reviewed unless evidence exists.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P03/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.
