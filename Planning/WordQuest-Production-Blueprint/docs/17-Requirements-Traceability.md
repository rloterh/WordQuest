# Requirements traceability

All evidence is pending implementation. This table describes required proof; it is not a completion claim. Store exact artifact links and build IDs in the implementation evidence reports.

| Requirement | Implement/verify tasks | Required evidence |
|---|---|---|
| PR-001 | [P02](../prompts/P02-Project-Foundation.md), [P06](../prompts/P06-UX-and-Design-System.md) | Guest start and relaunch |
| PR-002 | [P03](../prompts/P03-Content-Schemas-and-Validation.md), [P13](../prompts/P13-Editorial-Publishing-Toolchain.md), [P15](../prompts/P15-Full-Campaign-and-Content-Production.md) | Editorial rubric and approved coverage |
| PR-003 | [P04](../prompts/P04-Core-Challenge-Modes.md) | Context answer/rationale checks |
| PR-004 | [P04](../prompts/P04-Core-Challenge-Modes.md) | Tile multiset/input tests |
| PR-005 | [P04](../prompts/P04-Core-Challenge-Modes.md), [P13](../prompts/P13-Editorial-Publishing-Toolchain.md) | Semantic contrast review |
| PR-006 | [P04](../prompts/P04-Core-Challenge-Modes.md), [P13](../prompts/P13-Editorial-Publishing-Toolchain.md) | Repair variants and rationale |
| PR-007 | [P08](../prompts/P08-Narrative-and-Slice-Campaign.md), [P15](../prompts/P15-Full-Campaign-and-Content-Production.md) | Capstone walkthrough and reachable ending |
| PR-008 | [P05](../prompts/P05-Learning-and-Durable-Saves.md) | Scheduler replay and evidence rules |
| PR-009 | [P06](../prompts/P06-UX-and-Design-System.md), [P15](../prompts/P15-Full-Campaign-and-Content-Production.md) | Word-detail audio/search/device checks |
| PR-010 | [P05](../prompts/P05-Learning-and-Durable-Saves.md), [P17](../prompts/P17-Beta-Qualification.md) | Interrupted-write/migration/recovery |
| PR-011 | [P11](../prompts/P11-Backend-and-Cloud-Sync.md), [P17](../prompts/P17-Beta-Qualification.md) | Two-device merge and deletion |
| PR-012 | [P05](../prompts/P05-Learning-and-Durable-Saves.md), [P12](../prompts/P12-Purchases-and-Entitlements.md), [P17](../prompts/P17-Beta-Qualification.md) | Airplane-mode entitled campaign |
| PR-013 | [P01](../prompts/P01-Mobile-Feasibility.md), [P09](../prompts/P09-Accessibility-and-Device-Polish.md), [P17](../prompts/P17-Beta-Qualification.md) | Actual accessibility/device matrix |
| PR-014 | [P07](../prompts/P07-Hero-Art-and-Motion-Pipeline.md), [P09](../prompts/P09-Accessibility-and-Device-Polish.md), [P17](../prompts/P17-Beta-Qualification.md) | Art rubric, motion and frame capture |
| PR-015 | [P11](../prompts/P11-Backend-and-Cloud-Sync.md), [P13](../prompts/P13-Editorial-Publishing-Toolchain.md), [P19](../prompts/P19-Release-Rehearsal.md) | Signed bundle activation/rollback |
| PR-016 | [P12](../prompts/P12-Purchases-and-Entitlements.md), [P17](../prompts/P17-Beta-Qualification.md) | Store sandbox transaction matrix |
| PR-017 | [P10](../prompts/P10-Slice-Research-and-Go-No-Go.md), [P14](../prompts/P14-Analytics-and-Operational-Controls.md), [P17](../prompts/P17-Beta-Qualification.md) | Metrics schema and honest cohort study |
| PR-018 | [P18](../prompts/P18-Store-and-Policy-Preparation.md), [P19](../prompts/P19-Release-Rehearsal.md), [P20](../prompts/P20-Independent-Release-Review.md), [P21](../prompts/P21-Authorized-Launch-and-First-Month.md) | Release dossier and authorized status |
| PR-019 | [P16](../prompts/P16-Optional-AI-Lab.md) | 200-case evaluation or explicit disabled status |
| PR-020 | [P03](../prompts/P03-Content-Schemas-and-Validation.md), [P13](../prompts/P13-Editorial-Publishing-Toolchain.md), [P15](../prompts/P15-Full-Campaign-and-Content-Production.md) | Author-review-publish workflow and rights |
| NF-001 | [P01](../prompts/P01-Mobile-Feasibility.md), [P09](../prompts/P09-Accessibility-and-Device-Polish.md), [P17](../prompts/P17-Beta-Qualification.md) | Sustained named-device profiler evidence |
| NF-002 | [P05](../prompts/P05-Learning-and-Durable-Saves.md), [P12](../prompts/P12-Purchases-and-Entitlements.md), [P17](../prompts/P17-Beta-Qualification.md) | Save/transaction interruption tests |
| NF-003 | [P06](../prompts/P06-UX-and-Design-System.md), [P09](../prompts/P09-Accessibility-and-Device-Polish.md) | Small/large layouts and text reflow |
| NF-004 | [P02](../prompts/P02-Project-Foundation.md), [P19](../prompts/P19-Release-Rehearsal.md) | Clean-clone reproducible build |
| NF-005 | [P11](../prompts/P11-Backend-and-Cloud-Sync.md), [P16](../prompts/P16-Optional-AI-Lab.md), [P20](../prompts/P20-Independent-Release-Review.md) | Secret/authorization audit |
| NF-006 | [P05](../prompts/P05-Learning-and-Durable-Saves.md), [P09](../prompts/P09-Accessibility-and-Device-Polish.md) | Lifecycle/keyboard/audio resume |
| NF-007 | [P17](../prompts/P17-Beta-Qualification.md), [P20](../prompts/P20-Independent-Release-Review.md) | Severity ledger with no blocking defects |
| NF-008 | [P13](../prompts/P13-Editorial-Publishing-Toolchain.md), [P15](../prompts/P15-Full-Campaign-and-Content-Production.md) | Human signoff and provenance |
| NF-009 | [P05](../prompts/P05-Learning-and-Durable-Saves.md), [P16](../prompts/P16-Optional-AI-Lab.md), [P17](../prompts/P17-Beta-Qualification.md) | Network/AI outage fallback |

All mandatory PR requirements except optional PR-019 must pass for the proposed launch. PR-019 may be explicitly disabled without reducing core campaign completeness. Windows and expansion features are outside v1.0 scope unless an owner decision changes that baseline.
