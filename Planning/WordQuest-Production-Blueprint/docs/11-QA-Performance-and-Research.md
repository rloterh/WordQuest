# Quality assurance, performance, and product research

## Evidence levels

L0: authored specification. L1: automated local checks. L2: running editor/staging demonstration. L3: packaged physical-device evidence. L4: target-user observation. L5: operational/store evidence. Each feature requires the relevant levels; a screenshot cannot substitute for L3 performance or L4 comprehension.

## Provisional device budgets

These are project targets, not measured results or store limits. P01 names actual devices and revises budgets from evidence.

| Metric | Initial target | Measurement |
|---|---|---|
| Mid-tier active play | 60 FPS target; p95 frame time ≤20 ms | 20-minute physical-device run |
| Supported low tier | Stable 30 FPS; p95 ≤35 ms | Same sequence with low profile |
| Touch response | visible response within 100 ms target | High-frame-rate recording |
| Peak working memory | ≤700 MB on 4 GB Android target | Platform profiler; include scene transitions |
| Cold start to playable | ≤5 seconds after initial setup | Ten cold launches; median and p95 |
| Base delivery | ≤250 MB compressed aspiration | Actual store-style package report |
| Full campaign download | ≤750 MB aspiration | Bundle sizes incl. audio |
| Core offline | All installed entitled missions and review | Airplane-mode matrix |
| Reliability | ≥99.5% crash-free sessions in meaningful beta sample | Report numerator, denominator, build |

Measure frame hitches, shader compilation, thermal throttling and battery behavior. Do not reduce reading clarity to pass a GPU budget. A device excluded from support is explicitly documented; an emulator does not qualify it.

## Test pyramid

Domain tests: answer normalization, repeated tiles, option shuffle, assistance rules, distinct-context evidence, delayed retention, queue caps, mission prerequisites, duplicate submissions, grant idempotency. Property/invariant tests where valuable: no negative interval, no hint-treated-as-unaided, no reward duplication, no impossible tile solutions, no missing-reference release.

Integration: save interrupted mid-write, backup restore, old-schema migration, two-device divergent attempts, guest merge, deleted-account stale sync, revoked item, interrupted bundle activation, corrupt bundle, purchase pending/cancelled/refunded, entitlement restore.

UI/device: small screen, largest text, keyboard, tap alternative, screen reader, reduced motion, all audio off, background/resume, incoming call, low storage, loss of connection, slow download, device rotation policy, cold start.

Content: every release record validated, editor signoff, answer rationale, audio match, rights, coverage, capstone ambiguity. Semantic review is not replaceable by unit tests.

## Required scenario matrix

Q01 duplicate submit emits one attempt and one grant. Q02 kill app after answer before celebration preserves outcome. Q03 wrong answer plus revealing hint cannot grant unaided recall. Q04 same question repeated instantly cannot count as retained. Q05 clock moved forward/backward cannot repeatedly farm rewards. Q06 offline purchase cannot fabricate entitlement. Q07 refund updates connected clients while offline policy is documented. Q08 corrupted content falls back safely. Q09 large text preserves complete clue and controls. Q10 no-audio/no-motion campaign remains completable. Q11 free campaign boundary permits review of previously learned free senses. Q12 two-device merge preserves attempts and avoids duplicate restoration. Q13 withdrawn question does not punish prior progress. Q14 account deletion does not resurrect on stale sync. Q15 resumed cinematic never grants twice.

## Playtest progression

Discovery: 8–12 intended adult learners; interview motivations and word-study frustrations. Prototype: 5–8 observed users; test comprehension, interaction and desire to continue. Slice: 20–30 users across ability/device range; examine repeated use and delayed learning. Beta: recruit a larger cohort appropriate to confidence needs; do not pretend a handful of users establishes business viability.

Ask players to explain a word in their own terms and apply it in a new context. Observe whether they understand why a distractor fails. Measure whether they return without compensation or researcher reminders separately from scheduled research sessions.

## Metrics dictionary

Activation: first mission completed / eligible new installs. D1/D7/D30 retention: proportion of an install cohort returning in a specified day window; publish the exact timezone/window and exclude only predeclared invalid installs. Mission completion: completion / mission starts. Hint rate: assisted attempts / attempts. Delayed retention: correct unaided held-out responses / eligible delayed responses, with attrition reported. Weekly retained senses: unique senses newly meeting the stated delayed evidence rule per active learner. Do not count all exposures as words learned.

Initial product discussion targets: activation ≥70%, D1 ≥35%, D7 ≥15%, D30 ≥8%. These are provisional internal hypotheses, not published industry benchmarks or forecasts. Reassess with audience, channel, sample size and confidence intervals. Good retention without meaningful learning is a product failure; learning gains with no voluntary return mean the game loop needs work.

## Telemetry events

session_start/end; mission_start/complete; challenge_presented; attempt_submitted; hint_used; explanation_opened; sense_stage_changed; review_due/completed; restoration_granted; bundle_download/activated/failed; purchase_started/result/restored; sync_failed/recovered; content_reported. Shared fields: anonymous/consented profile ID, build, content/config version, session ID, device class, locale and event ID. No raw writing, audio, email or receipt in standard analytics.

## Art and motion QA

Capture a standard scene set before/after each visual milestone. Review safe areas, baseline alignment, line breaks, word lengths, animation overlap, translucent overdraw, texture blur, letter contrast and aliasing. Pair visual comparison with hands-on play; a screenshot cannot reveal input lag or animation fatigue.

## Exit policy

No unresolved severity-1/2 defect affecting crash, data loss, purchase, content correctness, security or campaign completion. Lower issues have owner, impact and disposition. A flaky required test is a defect to investigate, not a reason to ignore the gate. Record actual results in the evidence template.
