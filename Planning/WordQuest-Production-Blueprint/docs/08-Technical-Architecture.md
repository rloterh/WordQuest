# Technical architecture

## Principles

Offline-first core learning, deterministic scoring, data-driven curriculum, presentation separated from learning state, and a small backend with clear authority. No runtime AI dependency in the campaign. Use a modular monolith rather than distributed services until scale or ownership makes a split necessary.

## Client modules

| Module | Responsibility | Must not own |
|---|---|---|
| LexiconDomain | Senses, accepted answers, progression and scoring | Widgets/network |
| LearningScheduler | Due skills, evidence rules, queue composition | Rewards and rendering |
| SessionRuntime | Mission state machine and attempt lifecycle | Store verification |
| Presentation | UMG screens, input, animation events | Canonical mastery writes |
| WorldPresentation | Scenes, characters, Niagara, cinematics | Entitlement decisions |
| ContentRuntime | Bundle resolution, schema/version compatibility | Editorial approval |
| Persistence | Journal, snapshots, migration and recovery | UI-derived truth |
| PlatformServices | Audio/input lifecycle, purchases, secure tokens | Hard-coded business logic |
| SyncClient | Outbox, retries, account migration and reconciliation | Trusting client purchase claims |
| Telemetry | Consent-aware event queue and crash breadcrumbs | Raw sentence/audio capture by default |

Prefer pure C++ data/logic where practical, wrapped by Unreal-facing classes. Use GameInstance subsystems for long-lived services only when appropriate; keep screen widgets short-lived and disposable. A single composition root wires dependencies. Avoid a giant all-purpose GameInstance or Blueprint event graph.

Suggested repository areas: `Source/WordQuest/Domain`, `Learning`, `Sessions`, `Persistence`, `UI`, `Platform`; `Content/WordQuest` for assets; `ContentSource` for reviewed data; `Tools` for validators/importers; `Tests`; `docs`; `evidence`. Exact layout follows project conventions established at P02.

## Session state machine

States: Loading → Intro → Presenting → AwaitingInput → Evaluating → Feedback → NextEncounter → Result → Complete. Pause/background can suspend any safe state. Network state is orthogonal. Failed content loading transitions to a recoverable error with retry or return.

Every submission gets an attempt UUID before evaluation. The evaluator returns a structured outcome: correct/incorrect/accepted_variant, assistance, rationale ID, skill evidence and presentation event. Persistence records the outcome atomically before rewards or animation. Duplicate submissions with the same ID return the same outcome. Presentation completion must not be the only trigger that saves progress.

## Local persistence

Use a versioned event journal plus compact snapshots through a replaceable persistence adapter. Implementation may use supported local storage mechanisms, but atomic write/rename and backup recovery must be demonstrated on both platforms. Do not select an unmaintained SQLite plugin without a compatibility check.

Stored entities: profile, preferences, content versions, session checkpoints, attempts, skill evidence, mission completion, restoration grants, entitlements cache, sync outbox. Each record includes schema version. Checksums detect corruption, not malicious tampering. Keep a last-known-good snapshot; quarantine corrupt files and offer recovery. Migration fixtures cover at least N-1 → N and interrupted migration. Never overwrite an unknown newer save format.

## Backend baseline

Proposed managed PostgreSQL with a small TypeScript API, object storage/CDN for signed content bundles, and platform purchase verification. Choose the actual provider after region, cost, maintenance, and SDK checks; Supabase is a candidate, not a dependency mandated by the user's unrelated projects. No need for Redis, Kubernetes, microservices, or real-time multiplayer infrastructure at launch.

Services: identity, profile sync, entitlement verification, content manifest, consent-aware analytics intake, support intake, optional AI gateway. Admin authoring/publishing is separate from player access. Client-facing credentials cannot publish content or grant campaign access.

## API contracts, proposed

- `GET /v1/content/manifest?client_version=...&platform=...`: compatible signed bundle metadata; no secrets.
- `POST /v1/sync`: authenticated device ID, cursor, batch of uniquely identified events; returns acknowledgements, authoritative grants and new cursor. Limit batch sizes and body sizes.
- `POST /v1/purchases/verify`: platform transaction token/ID with idempotency key; server verifies through current platform mechanism and returns entitlement version.
- `GET /v1/entitlements`: authenticated current grants and revocation state.
- `POST /v1/support/content`: content ID/version, problem category and optional user explanation; rate limited.
- `DELETE /v1/account`: authenticated deletion request with status/recovery behavior documented.
- Optional `POST /v1/tutor/feedback`: approved sense ID/version plus bounded response; structured feedback, refusal/uncertainty states, strict quota.

Standard error envelope: code, retryable, safe message key, request ID. Never leak stack traces or store receipt contents to logs. Retry only idempotent operations with bounded exponential backoff and jitter. A versioned OpenAPI contract is produced during implementation, not guessed from current vendor SDKs in this plan.

## Merge and trust

Attempts deduplicate by UUID; preserve distinct offline attempts. Mission completion is monotonic per content-defined mission ID; restoration rewards grant exactly once per first completion. Cosmetic inventory merges through grant IDs. Preferences use last explicit change with a sensible conflict policy. Scheduler projections rebuild from merged attempts using a pinned algorithm version; do not simply take whichever device reports higher mastery.

Guest-to-account merge presents a concise explanation and preserves both attempt histories. Account deletion creates a tombstone so a stale device cannot silently recreate deleted server data. Document which local data remains and provide local reset. Store transactions, refunds, and campaign entitlements are server/platform-authoritative. Offline learning is permitted, but competitive rankings must not trust arbitrary client mastery reports.

## Content delivery

Each bundle carries content version, schema version, minimum client, IDs, hashes, locale and editorial release ID. Verify integrity and a trusted manifest signature using an approved cryptographic library. Download to temporary storage, validate fully, then activate atomically. Keep the last compatible bundle. An in-progress session stays pinned to its content version; never change an answer key mid-question.

Revoked/incorrect items can be disabled by manifest; offline clients may retain old versions until reconnection. Reports preserve the original content version. Correcting a flawed item does not punish the player or delete unrelated progress.

## Security and data handling

Tokens use platform-secure storage. Never ship service-role secrets, AI keys or signing private keys. Enforce ownership on every data access; test cross-user attempts. Restrict admin publishing, separate staging/production, rotate secrets, maintain dependency inventory. Keep raw writing/audio out of default telemetry. Runtime tutor text is ephemeral unless the user explicitly saves it; policy and implementation must agree.

## Delivery and environments

Local, staging and production have distinct configuration and credentials. Build artifacts record commit, engine/toolchain, content hash and config version. CI validates code/content and packages supported targets on appropriate hosts. CI without Mac access cannot certify iOS. A content rollback and a binary rollback are separate operations; mobile store rollback may require a new release, so remote flags and compatible bundles are essential.
