# Execution index

These are bounded work orders, not one enormous 'build the whole game' prompt. They cover implementation through release, but their gates require actual execution, human review and external platform/account access. All code remains unimplemented at package delivery.

## Operating procedure

1. Place the planning package in the intended project workspace.
2. Run P00 with this index and relevant documents attached. It inspects only.
3. When implementation is authorized, run P01 and proceed in dependency order.
4. At each task, load project status plus the named references. The assistant must inspect actual work before editing.
5. Review tangible artifacts and evidence. Technical routine work can continue autonomously; material product changes and public publication use owner decisions.
6. If a task is blocked, do not mark it passed. Continue only independent eligible tasks.
7. P16 is optional; explicitly disabling it satisfies the release dependency for that optional feature.
8. A complete sequence means all required gates passed. It does not guarantee store approval, user demand or commercial ranking.

## Task order and dependencies

| Task | Prompt | Prerequisite |
|---|---|---|
| P00 | [Environment and Evidence](P00-Environment-and-Evidence.md) | None; planning/inspection only |
| P01 | [Mobile Feasibility](P01-Mobile-Feasibility.md) | P00; implementation authorized |
| P02 | [Project Foundation](P02-Project-Foundation.md) | P01 engine decision passed |
| P03 | [Content Schemas and Validation](P03-Content-Schemas-and-Validation.md) | P02 |
| P04 | [Core Challenge Modes](P04-Core-Challenge-Modes.md) | P03; approved prototype items available |
| P05 | [Learning and Durable Saves](P05-Learning-and-Durable-Saves.md) | P04 |
| P06 | [UX and Design System](P06-UX-and-Design-System.md) | P04 and P05 |
| P07 | [Hero Art and Motion Pipeline](P07-Hero-Art-and-Motion-Pipeline.md) | P06; approved style direction |
| P08 | [Narrative and Slice Campaign](P08-Narrative-and-Slice-Campaign.md) | P05 through P07 |
| P09 | [Accessibility and Device Polish](P09-Accessibility-and-Device-Polish.md) | P08 |
| P10 | [Slice Research and Go No Go](P10-Slice-Research-and-Go-No-Go.md) | P03 through P09; slice content reviewed |
| P11 | [Backend and Cloud Sync](P11-Backend-and-Cloud-Sync.md) | P05 and G3 proceed decision |
| P12 | [Purchases and Entitlements](P12-Purchases-and-Entitlements.md) | P11; owner commercial/account inputs available |
| P13 | [Editorial Publishing Toolchain](P13-Editorial-Publishing-Toolchain.md) | P03; G3 proceed decision |
| P14 | [Analytics and Operational Controls](P14-Analytics-and-Operational-Controls.md) | P11; stable event contracts |
| P15 | [Full Campaign and Content Production](P15-Full-Campaign-and-Content-Production.md) | P10 proceed; P13; established art pipeline |
| P16 | [Optional AI Lab](P16-Optional-AI-Lab.md) | P11 and P14; optional feature only |
| P17 | [Beta Qualification](P17-Beta-Qualification.md) | P09 and P11–P15; P16 passed or disabled |
| P18 | [Store and Policy Preparation](P18-Store-and-Policy-Preparation.md) | P17 technical candidate; owner account/legal inputs |
| P19 | [Release Rehearsal](P19-Release-Rehearsal.md) | P18; candidate identifiers frozen |
| P20 | [Independent Release Review](P20-Independent-Release-Review.md) | P19 |
| P21 | [Authorized Launch and First Month](P21-Authorized-Launch-and-First-Month.md) | P20 GO; explicit owner publication authorization |

## Suggested assistant use

Choose GPT-6 or Fable 5.1 based on verified task performance and tool access. Use a second fresh review pass for high-risk changes; either model can fill it. Do not assume these named tools have identical commands or context capacities. If multiple workers are authorized, keep binary asset ownership exclusive and branch/worktree boundaries explicit.

## Resume message

Read PROJECT-STATUS.md, the latest evidence report, and the selected task. Inspect the current repository and baseline commit. Identify the first unmet acceptance criterion, complete it, run the relevant checks, and update evidence. Do not restart completed work or reinterpret a blocked task as complete.

## Reference companions

[Creative asset prompts](Creative-Asset-Prompts.md) · [Review and recovery prompts](Review-and-Recovery-Prompts.md) · [AI production workflow](../docs/10-AI-Production-Workflow.md)
