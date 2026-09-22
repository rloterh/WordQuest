# WordQuest: The Living Lexicon

A vocabulary adventure project. This repository currently contains the supplied
planning packages and an initial directory skeleton; game development has not begun.

## Planning references

- [Production Blueprint](Planning/WordQuest-Production-Blueprint/README.md)
- [UI Realms Addendum](Planning/WordQuest-UI-Realms-Addendum/README.md)
- [Combined Production Blueprint](Planning/WordQuest-Complete-Production-Blueprint.md)
- [Combined UI Realms Guide](Planning/WordQuest-UI-Realms-Guide.md)
- [Current project status](Docs/Progress/PROJECT-STATUS.md)

The two ZIP packages are extracted under `Planning` with their internal paths and
contents unchanged. The addendum contains six original reference images. Its G/H/I
gameplay references govern the visual direction; the home-screen images remain drafts.
The addendum supersedes the earlier visual direction, while the original learning,
security, accessibility and release requirements remain applicable.

The initial session transcript is retained locally as optional historical context and
excluded from Git. The curated planning documents and recorded decisions provide the
shared project reference.

## Directory map

| Directory | Purpose |
| --- | --- |
| `Planning/` | Supplied specifications, prompts, examples and original reference images |
| `Docs/` | Decisions, architecture, setup, progress and QA records |
| `ArtSource/` | Editable environments, companions, UI, audio, fonts and license records |
| `ContentSource/` | Editable vocabulary, challenges, missions, narrative and schemas |
| `Tools/` | Future content validation, asset import and build scripts |
| `Game/` | Future Unreal project, with initial content and source directories |
| `Artifacts/` | Generated screenshots, recordings, test reports and packaged builds |

Empty directories contain `.gitkeep` files so the structure can be retained in Git.
`Artifacts` output is ignored, but its directory placeholders are retained.
`Game/Build` is reserved for build resources and is not ignored.

This layout is a starting point, not a mandatory final architecture. Evolve it to suit
established Unreal conventions and demonstrated project needs, updating this map and
affected references when paths change.

## Current boundary

Only file and folder organization is complete. No execution prompt, toolchain
inventory, engine setup, asset reconstruction or implementation has been started.
Examples remain in the planning packages and are not production content.

Unreal must generate `Game/WordQuest.uproject`, `WordQuest.Build.cs`,
`WordQuest.Target.cs` and `WordQuestEditor.Target.cs` during a later authorized setup
task. They are intentionally absent; the `Game` skeleton is not an Unreal project yet.

The later inventory task starts from UI00 and incorporates the original P00 checks.
The first intended implementation milestone is a faithful animated G gameplay screen
with live controls, verified on a real phone. Neither task is started by this scaffold.

## Git and assets

`.gitignore` excludes Unreal caches, generated binaries and ordinary build outputs.
`.gitattributes` declares Git LFS handling for common artwork and Unreal binary assets.
Git LFS 3.7.1 was verified and repository-local LFS configuration and hooks initialized
for the initial commit. Other checkouts must also have Git LFS installed and initialized
before working with these assets. Keep planning originals intact, editable reconstructions
in `ArtSource`, and imported runtime assets in `Game/Content`.

The existing root [LICENSE](LICENSE) is preserved. Record the provenance and usage
rights of future third-party artwork, audio and fonts in `ArtSource/Licenses`.
