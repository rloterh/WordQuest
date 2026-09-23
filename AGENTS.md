# WordQuest repository instructions

## Current scope

The owner authorized P00/UI00 inventory and the bounded UI01/UI02 G visual proof on
2026-09-22, with PRs where appropriate. Work on the existing repository; do not create
a new remote, deploy or release the game. Do not expand into later milestones merely
because a planning document lists them. Update `Docs/Progress/PROJECT-STATUS.md` as
work advances. Preserve all original release and physical-device gates.

## Governing references

- `Planning/WordQuest-Production-Blueprint/README.md`: original requirements and index.
- `Planning/WordQuest-UI-Realms-Addendum/README.md`: selected G/H/I visual direction.
- `Planning/WordQuest-UI-Realms-Addendum/docs/01-Decisions-and-Integration.md`:
  integration rules; the addendum supersedes earlier visual guidance, while learning,
  security, accessibility and release requirements remain in force.

Read current status and the relevant specification before editing. Keep context
focused. Separate proposals in the planning documents from confirmed owner decisions.
Preserve existing work and the user's explicit task boundaries.

The initial conversation transcript is optional local history, excluded from Git.
It is not a governing specification or a required dependency for future contributors.

## Structure and asset ownership

- The current layout is a starting proposal, not a
  fixed architecture. Adapt the structure to established Unreal conventions and
  actual project needs as evidence develops. Document meaningful changes and update
  affected paths; preserve working assets and keep changes within the current task.
- Keep supplied planning packages and reference images unchanged.
- Original G/H/I gameplay images are the visual targets; home-screen references are
  draft proposals. Preserve composition, palette, ornament and character identity.
- Store editable art in `ArtSource`, editable learning content in `ContentSource`,
  and imported Unreal assets in `Game/Content`.
- Share scoring, navigation, learning and interface behavior across G/H/I themes.
- Unreal must generate `.uproject`, module build files and target files. Never create
  empty placeholders or fabricate `.uasset`, `.umap` or `.blend` files.
- Use one implementation agent initially and one writer per binary asset. Delegate
  only when the user explicitly authorizes it.
- Verify Git LFS is available and configured before committing binary assets.
- Keep caches and ordinary build outputs out of Git; retain `Game/Build` resources.

## Future milestone and verification

Inventory begins with UI00 and original P00 environment checks. See
`Docs/Setup/ENVIRONMENT.md`, `Docs/Setup/TOOLCHAIN-LOCK.md` and
`Docs/Decisions/DECISIONS.md` for verified tools and unresolved decisions.
Original visual targets live under
`Planning/WordQuest-UI-Realms-Addendum/references/`.

Verification commands from repository root:

- `python Tools/AssetImport/verify_references.py`
- `python Tools/BuildScripts/build_wordquest.py`

The generated project is `Game/WordQuest.uproject`. Read
`Docs/Setup/RESUME-G-PROOF.md` for the NetFxSDK and Android prerequisites and the
UI01/UI02 acceptance sequence. Build success alone does not pass runtime gates.

The first implementation proof is a faithful G Celestial Reverie gameplay screen with
live text and controls, layered gentle motion, reference comparisons and real-phone
evidence. Expand to H/I after the shared approach is demonstrated.

Preserve advanced vocabulary, deterministic campaign scoring and offline core play.
Planning examples and AI drafts are not editorially approved release content. Keep
service secrets out of clients. Maintain accessible controls and reduced-motion paths.

For future implementation, use actual project tooling and proportionate tests. Verify
visual changes in the running engine and on devices when required. Report checks run,
results and unavailable verification honestly; never mark a gate passed on source code
or generated concepts alone. Keep decisions, progress and evidence under `Docs` and
generated captures/builds under `Artifacts`.

## Code review rules

The owner requested internal AI PR review on 2026-09-23. Use Codex's dedicated
review command against the PR's actual base branch; see `Docs/Setup/PR-REVIEW.md`.
Review is read-only and never authorizes a merge or replaces build/device evidence.

- Report actionable introduced defects with severity, file/line and a concrete
  failure scenario. Avoid style-only findings and speculative future requirements.
- Check Unreal-generated project integrity, build helper error propagation,
  toolchain compatibility, LFS ownership and exclusion of caches/build outputs.
- Flag secrets in client/config files, changes to original supplied references,
  nondeterministic scoring, broken offline play and accessibility regressions.
- Distinguish this foundation PR from UI01/UI02: unfinished G assets and draft
  learning fixtures are disclosed follow-up work, not completed runtime evidence.
- Never claim tests, visual fidelity, editorial approval or physical-device gates
  passed unless the recorded evidence supports that exact claim.
