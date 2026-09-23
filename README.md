# WordQuest: The Living Lexicon

A vocabulary adventure project. The repository contains the supplied planning
packages, verified environment inventory, an Unreal-generated C++ foundation and
G reconstruction candidates. The first playable G screen is not implemented yet.
The Win64 Development game and editor targets compile successfully.

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
| `Tools/` | Reference validation and build scripts; future import/content tooling |
| `Game/` | Unreal-generated WordQuest project, configuration and source |
| `Artifacts/` | Generated screenshots, recordings, test reports and packaged builds |

Empty directories contain `.gitkeep` files so the structure can be retained in Git.
`Artifacts` output is ignored, but its directory placeholders are retained.
`Game/Build` is reserved for build resources and is not ignored.

This layout is a starting point, not a mandatory final architecture. Evolve it to suit
established Unreal conventions and demonstrated project needs, updating this map and
affected references when paths change.

## Current milestone

P00/UI00 inventory and bounded UI01/UI02 G work are authorized. Unreal generated
`Game/WordQuest.uproject` and its C++ module/targets using UE 5.8.2. The editor build
passes after installing the missing .NET Framework 4.8 SDK; no gameplay, motion or
device acceptance is claimed.
Art candidates and the prototype fixture remain unapproved for release.

See [environment](Docs/Setup/ENVIRONMENT.md),
[resume instructions](Docs/Setup/RESUME-G-PROOF.md),
[internal PR review](Docs/Setup/PR-REVIEW.md),
[UI00 inventory](Docs/QA/UI00/INVENTORY.md) and
[art handoff](ArtSource/G-ASSET-HANDOFF.md).

```powershell
python Tools/AssetImport/verify_references.py
python Tools/BuildScripts/build_wordquest.py
```

The first intended proof remains faithful G gameplay with live controls, frozen
reference comparison, gentle motion and physical-phone evidence. Resolve G before H/I.

## Git and assets

`.gitignore` excludes Unreal caches, generated binaries and ordinary build outputs.
`.gitattributes` declares Git LFS handling for common artwork and Unreal binary assets.
Git LFS 3.7.1 was verified and repository-local LFS configuration and hooks initialized
for the initial commit. Other checkouts must also have Git LFS installed and initialized
before working with these assets. Keep planning originals intact, editable reconstructions
in `ArtSource`, and imported runtime assets in `Game/Content`.

The existing root [LICENSE](LICENSE) is preserved. Record the provenance and usage
rights of future third-party artwork, audio and fonts in `ArtSource/Licenses`.
