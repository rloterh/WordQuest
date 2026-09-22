# Production roadmap, staffing, and cost control

## Schedule stance

There is no reliable single completion date without staffing, weekly availability, device access and observed content throughput. Use milestones with exit evidence. For a solo engineer with targeted contract art/editorial help, a polished 600-sense release could plausibly take 12–24+ months; a small experienced team might target 6–12+ months. These are rough planning scenarios, not commitments. Unreal learning, asset revisions, editorial work and store operations can dominate the schedule despite fast AI coding.

## Milestones

| Gate | Deliverable | Planning effort window | Exit evidence |
|---|---|---|---|
| G0 Environment | Local facts, supported versions, device/build access | 2–5 working days | P00 inventory and risks |
| G1 Feasibility | Representative packaged mobile benchmark | 1–2 weeks | P01 physical-device report |
| G2 Fun prototype | 30 senses, 3 missions, basic review/save | 3–5 weeks | P02–P05 + observed test |
| G3 Production slice | 120 senses, 12 missions, one polished district | 6–10 additional weeks | P06–P10 and slice report |
| G4 Feature alpha | Complete systems and authoring workflow | 4–8 additional weeks | P11–P14 integration evidence |
| G5 Content beta | 600 senses, 60 missions, all art/audio | 8–16+ additional weeks | P15–P17 content/device reports |
| G6 Release candidate | Store builds, purchases, operations and fixes | 4–8 additional weeks | P18–P20 evidence |
| G7 Launch/operate | Staged launch and first content cycle | Ongoing | P21 operational review |

Windows overlap only when responsible people and resources exist; do not add columns and present the sum as a promise. Solo work and specialist availability may stretch these windows. Content production begins after the schema is stable and continues through alpha; it is a critical path, not final polish.

## Ownership

Robert: product owner, engineering lead and release decision. AI assistants: implementation, documentation, draft assets/content and review assistance, subject to evidence. Needed human functions: vocabulary editor/lexicographer, art/animation judgment, target-user research, platform/device QA, and business/legal/account ownership. One person can cover several functions, but their hours still count. Plan targeted contractor help for editorial and hero art if budget allows.

## Content capacity model

Launch minimum = 600 senses × 6 reviewed items = 3,600 items, plus definitions, examples and audio. If complete review averages 4–8 items per reviewer-hour, item review alone is approximately 450–900 hours. Measure actual throughput on the first 30 senses; difficult precision items may take longer. Add drafting, rework, audio, testing and metadata. AI reduces drafting effort but does not remove semantic verification.

## Cost worksheet

Track actual local currency and quotes rather than inventing software prices. Lines: engineering time; editorial hours; concept/3D/animation; music/audio rights; test phones; Mac/iPhone access; engine/marketplace obligations; developer accounts; AI subscriptions and usage; backend/CDN; crash monitoring; localization; acquisition tests; support. Separate one-time investment, monthly operating costs and per-user variable costs.

Formula: total production = labour + art/audio + hardware + tools/accounts + contingency. Operating monthly = fixed services + active users × storage/egress/support + optional AI calls × measured cost. Begin with a 20–30% contingency as an owner-adjustable planning allowance, not a statistical guarantee. Verify current engine licensing and all commercial terms before revenue.

## Critical path

Toolchain/device proof → input/readability proof → core loop → content schema → learning/save correctness → hero art slice → editorial throughput → complete curriculum/campaign → purchase/platform qualification → beta evidence → release. Delay expensive full-world art until the loop survives observed playtesting.

## Backlog organization

Epics: platform foundation; curriculum tooling; challenge system; learning; narrative; art/audio; accessibility; persistence/sync; commerce; content production; research/analytics; release/operations. Each ticket contains requirement ID, concrete user outcome, dependencies, files/assets, acceptance evidence and owner. Keep stories small enough to build and verify without a month-long opaque branch.

Weekly cadence: select outcomes from blockers and gate dependencies; integrate working changes; review a device build; examine content throughput and player evidence; update risk/cost forecast. The demo should show the actual game, not slides alone.

## Scope adjustment rules

Preserve advanced learning, input quality, core offline play, save integrity and a complete story arc. First defer runtime AI lab, social play, extra cosmetics, extensive voice acting, Windows, and optional cinematics. Reducing the 600-sense/60-mission promise is an explicit release scope decision with marketing updates. Do not quietly ship a prototype as the planned full release.

## Procurement sequence

Immediately: inventory existing tools/hardware; no purchase required for the planning package. Before G1: required compatible compiler/Android tooling and access to representative devices. Before iOS qualification: Mac/Xcode/iPhone and relevant account access. Before G3: editorial and art capacity. Before commerce: verified store accounts, business identity, rights and tax/payment setup. Before launch: support contact, monitoring and current submission requirements.
