# WordQuest: The Living Lexicon — Production Blueprint

Prepared for Robert Loterh • 20 September 2026 • Planning baseline v1.0

**An advanced vocabulary adventure with the tactile pleasure, charm, and production discipline of a premium casual game.** WordQuest is a working title, not a cleared commercial name.

This package is the preproduction specification and execution system. No game, asset library, production backend, or store build has been implemented by producing these documents. Examples are design fixtures, not approved release content. The prompts cover the route to a shippable product; executing them successfully means meeting their evidence gates, including human editorial review, device tests, and store requirements. Prompt completion alone is not proof of readiness or a promise of chart success.

## Start here

1. Read [the executive direction](docs/00-Executive-Direction.md).
2. Read [scope and requirements](docs/01-Product-Requirements.md), then [the game design](docs/02-Game-Design.md).
3. Review [engine and tools](docs/07-Engine-and-Tools.md) and [production roadmap](docs/12-Production-Roadmap.md).
4. Extract this entire package into a new project workspace, preserving relative paths. Keep planning files together under `planning/` if placing them in a game repository.
5. Open that workspace in your coding environment. Attach this README and [the execution index](prompts/00-Execution-Index.md). Run [P00: environment and evidence](prompts/P00-Environment-and-Evidence.md). It inspects and records; it does not start game implementation.
6. Continue with P01 and subsequent eligible prompts in dependency order after implementation is authorized. Each prompt defines artifacts, checks, and stop conditions. Technical gates can pass on evidence without repeatedly asking the owner for routine permission.

## Documentation map

| Document | Purpose |
|---|---|
| [00 Executive direction](docs/00-Executive-Direction.md) | Product promise, audience, ambition, assumptions |
| [01 Product requirements](docs/01-Product-Requirements.md) | Requirements, scope, launch definition |
| [02 Game design](docs/02-Game-Design.md) | Core loop, modes, progression, difficulty, rewards |
| [03 Curriculum](docs/03-Curriculum-and-Mastery.md) | Advanced-word selection, learning model, editorial quality |
| [04 Narrative and levels](docs/04-Narrative-and-Level-Design.md) | World, characters, first chapter, level recipes |
| [05 UX and accessibility](docs/05-UX-and-Accessibility.md) | Screens, flows, text entry, edge states |
| [06 Art, motion, and sound](docs/06-Art-Motion-and-Sound.md) | Visual identity, asset budgets, animation contracts |
| [07 Engine and tools](docs/07-Engine-and-Tools.md) | Unreal/Blender strategy, tool verification, setup |
| [08 Architecture](docs/08-Technical-Architecture.md) | Modules, persistence, content delivery, backend |
| [09 Data and authoring](docs/09-Data-and-Content-Pipeline.md) | Schemas, content workflow, sample records |
| [10 AI production](docs/10-AI-Production-Workflow.md) | GPT-6/Fable workflow, editor automation, runtime AI |
| [11 Quality and metrics](docs/11-QA-Performance-and-Research.md) | Tests, performance, playtests, retention and learning |
| [12 Roadmap](docs/12-Production-Roadmap.md) | Milestones, capacity, costs, ownership, critical path |
| [13 Business and live operations](docs/13-Business-and-LiveOps.md) | Monetization, acquisition, ongoing content |
| [14 Release and operations](docs/14-Release-and-Operations.md) | Stores, support, monitoring, rollback |
| [15 Decisions and risks](docs/15-Decisions-and-Risks.md) | Defaults, unresolved matters, escalation triggers |
| [16 Sources](docs/16-Source-Register.md) | Verified references and verification limits |
| [17 Traceability](docs/17-Requirements-Traceability.md) | Requirement → prompt → evidence |
| [18 First ten working days](docs/18-First-Ten-Working-Days.md) | Practical local starting sequence |
| [Execution index](prompts/00-Execution-Index.md) | Ordered implementation prompts and handoff rules |
| [Creative prompt library](prompts/Creative-Asset-Prompts.md) | Concept, UI, Blender, motion, VFX, and audio briefs |
| [Recovery and review prompts](prompts/Review-and-Recovery-Prompts.md) | Resume, review, bug, performance, and content repair |

Templates include an agent-instructions template, project status, decision record, evidence report, asset manifest, editorial record, and release checklist. `examples/` contains illustrative structured content. `MANIFEST.json` contains file sizes and checksums. `PACKAGE-VALIDATION.md` describes the checks actually run on this package.

## Baseline in one table

| Area | Planning decision |
|---|---|
| Audience | Adults 18+ who already read English comfortably and want advanced vocabulary |
| Platforms | Android first for validation; Android and iOS for v1.0; Windows after mobile qualification |
| Presentation | Portrait-first 2.5D adventure; readable 2D interaction over stylized dimensional scenes |
| Engine | Unreal 5.8.2 as user-reported candidate; pin only after installed-build and mobile checks |
| Art | Blender 5.x pipeline, exact installed version recorded at P00 |
| Launch | 600 reviewed word senses; 3 districts; 60 authored missions; 4 core challenge modes plus story capstones |
| Slice | 120 reviewed senses; 12 missions; one district; all core systems demonstrated |
| Learning | Sense-specific recall, context, precision, usage, spaced review; no trivial target words |
| Offline | Core purchased/downloaded campaign and review playable offline |
| Revenue | Free opening chapter plus one-time full-campaign unlock; optional cosmetics later |
| AI | Strong during production; optional bounded tutor, not required for launch or core scoring |
| Release claim | Complete premium first release, followed by measured expansion—not a guaranteed ranking |

Owner decisions can amend these defaults through a decision record. Preserve requirement IDs and update traceability when changing scope. Do not silently replace Unreal, introduce subscriptions, reduce the vocabulary standard, or declare a gate passed without evidence.
