# Decisions, assumptions, and risk register

## Defaults adopted for planning

| ID | Decision | Reason | Revisit trigger |
|---|---|---|---|
| D01 | Adults 18+ first | Serious advanced vocabulary; focused audience | Owner selects teen/school market |
| D02 | Portrait 2.5D | Readable touch play with premium scene depth | Device/user test contradicts |
| D03 | Unreal candidate, early gate | Existing installation and art tooling | Packaging, accessibility or performance fails |
| D04 | 600 senses / 60 missions | Complete bounded first campaign | Capacity/budget evidence requires owner change |
| D05 | Four modes + capstones | Variety with manageable engineering | Repeated boredom or weak transfer |
| D06 | Deterministic campaign | Fair scoring, offline reliability, cost control | New mode requires bounded evaluated AI |
| D07 | Guest/offline-first | Low friction and reliable access | Specific business necessity |
| D08 | One-time campaign unlock | Clear value and finite content promise | Owner chooses funded live-service model |
| D09 | Android validation; Android+iOS v1 | Fast local proof plus broad mobile release | iOS resources remain unavailable |
| D10 | Human editorial signoff | Semantic quality and trustworthy teaching | Never removed solely to accelerate output |

## Owner inputs to collect without blocking this planning package

Weekly hours; available budget range; solo/contractor/team preference; target device models; Mac/iPhone access; launch countries; business/store-account status; preferred visual references; desired paid/free model; desired name; accessibility commitments; whether Windows must join first release. P00 records known answers and default assumptions. Do not ask the owner to restate facts already supplied.

## Risk register

| ID | Risk | Probability/impact estimate | Mitigation | Trigger/owner |
|---|---|---|---|---|
| R01 | Unreal overhead on target phones | Medium/high | Packaged benchmark, baked scenes, bounded fallback comparison | G1 engineering |
| R02 | Beautiful but repetitive quiz loop | High/high | Observe voluntary replay before mass art/content | G2/G3 product |
| R03 | Ambiguous or unnatural advanced content | High/high | Human review, alternatives rationale, item reports | Every batch editor |
| R04 | Content workload exceeds capacity | High/high | Measure 30-sense throughput, budget editorial help | G2 owner |
| R05 | iOS build/signing resources absent | Medium/high | Identify Mac/iPhone route early | G0 owner |
| R06 | Generated assets lack consistency/rights | Medium/high | Style bible, reconstruction, rights manifest | Art review |
| R07 | Binary asset conflicts | Medium/medium | Asset locks, one writer, small ownership units | Engineering lead |
| R08 | Save/sync/purchase duplication | Medium/high | IDs, journals, authority and interruption tests | G4 engineering |
| R09 | AI tutor confident errors/cost | Medium/high | Optional flag, human-rated evals, quota, fallback | AI lab owner |
| R10 | Scope inflation | High/high | Fixed launch contract, change records | Weekly product |
| R11 | Weak market acquisition | Medium/high | Positioning tests, cohort economics, capped spend | Beta/owner |
| R12 | Inaccessible text/input despite polish | Medium/high | Early real-device screen reader and large-text proof | G1/G3 UX |
| R13 | Tool/model/version assumptions false | Medium/medium | Local inventory and official compatibility checks | P00 engineering |
| R14 | Store/legal/commercial blockers | Medium/high | Current requirement checks before candidate | Release owner |

Probability labels are planning judgments, not calculated forecasts. Update with observed evidence and mitigation status.

## Escalation rules

Engineering chooses routine module structure, tests, bugs and optimization within the accepted charter. Ask for a concrete owner decision when changing audience, engine, paid model, launch-platform commitment, content promise, budget, account identity, or public release. Present options with consequences and a recommendation. Missing test evidence is a blocker to the claim, not a reason to invent success.

## Decision log format

Date; ID; question; facts; assumptions; options; chosen action; owner; cost/schedule impact; affected requirements/docs/prompts; revisit trigger. A later explicit owner decision supersedes this planning baseline. Keep change history and update all affected counts.
