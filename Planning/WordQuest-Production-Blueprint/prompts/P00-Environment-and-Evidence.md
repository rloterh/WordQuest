# P00 — Environment and Evidence

Copy this task into GPT-6, Fable 5.1, or another verified coding-agent environment with repository/tool access. Attach its listed references and current status.

**Dependencies:** None; planning/inspection only

**Read:** 00-Executive-Direction.md; 07-Engine-and-Tools.md; 15-Decisions-and-Risks.md

## Execution contract

Work in the real project workspace. Read its existing instructions and PROJECT-STATUS.md, inspect the baseline, and preserve unrelated changes. Load only relevant planning files. Resolve paths from the actual planning-package location; document paths below are relative to `docs/` unless otherwise stated.

Implement only this task within current authorization. Continue routine fixes until its acceptance criteria pass. Use installed-tool evidence and current official APIs; do not invent commands, editor access, binaries, test results or reviewer signoff. Record actual verification in an evidence report. If a material dependency is missing, finish safe independent work and report the concrete blocker. Update status and the first next eligible task. Do not publish, purchase, or make destructive account changes without authorization.

## Task

Inspect the actual local Windows workspace and available tools. Verify the user-reported Unreal 5.8.2 and Blender 5 installations from their real version output and installation metadata; do not silently substitute a different engine or upgrade. Record compiler, SDK/NDK/JDK compatibility, GPU/RAM/free disk, Android devices, Mac/Xcode/iPhone access, and developer-account readiness without exposing credentials. Determine what the selected GPT-6/Fable environment can actually do: filesystem, shell, builds, screenshots and editor operations. Preserve the Fable label without inventing its API.

Inventory any existing project before proposing a new one. If none exists, recommend a concrete project path and repository structure. Compare installed tools with official requirements for the pinned engine. Produce a capability matrix and a short missing-resource list. Separate facts, defaults and unresolved owner choices. This task must not start gameplay implementation, buy tools, change system installations or publish anything.

## Required deliverables and pass conditions

Create docs/ENVIRONMENT.md, docs/TOOLCHAIN-LOCK.md (provisional where necessary), docs/DECISIONS.md and PROJECT-STATUS.md. Record exact commands and version outputs, redacting secrets. List required manual checks for devices or editor access that cannot be inspected. Identify the next eligible task and whether implementation authorization exists.

## Handoff

Report outcome (pass/fail/blocked/disabled), changed artifacts, actual checks, remaining risks and next dependency-eligible task. Save evidence under `evidence/P00/` and update PROJECT-STATUS.md. A written plan for an editor action is not evidence that the action ran.
