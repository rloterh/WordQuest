# P11 — Backend and Cloud Sync

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** P05 and G3 proceed decision

**Read:** 08-Technical-Architecture.md; 14-Release-and-Operations.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Select the smallest supported managed backend meeting cost, region and operational needs; record an ADR. Implement optional identity, guest-to-account merge, sync outbox, idempotent batch API, per-user authorization, signed content manifest/bundle delivery and account deletion. Keep local play functional without an account.

Merge attempts by ID, grant rewards once, rebuild learning projections deterministically and preserve content versions. Do not trust client entitlement claims or higher self-reported mastery. Implement retry/backoff, schema compatibility and deletion tombstones. Provide a versioned API contract and staging configuration.

## Required deliverables and pass conditions

Test cross-user denial, offline divergent devices, interrupted sync, guest merge, duplicated events, corrupted/unsigned bundle rejection, bundle rollback and stale sync after deletion. Deliver migration scripts, API spec, least-privilege config and staging evidence. No production secrets in repository/client and no public deployment claim without actual deployment.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P11/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.
