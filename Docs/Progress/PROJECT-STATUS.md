# Project status

## Current stage: kickoff foundation; G proof incomplete

Owner authorized P00/UI00 inventory, UI01/UI02 G proof and appropriate PRs on
2026-09-22. Working branch: `kickoff/g-visual-proof`, based on clean `dev` at
`ebc3059`. No merge, game deployment or release is authorized.

## Completed work

- Read governing indexes, precedence and milestone specifications; visually inspected
  original G/H/I gameplay images. Six original hashes verified against the manifest.
- Verified UE 5.8.2 CL 56702186, Blender 5.1.0, Windows C++/SDK and Android tooling.
- Unreal's New Project dialog generated Blank C++ / Mobile / Scalable project in
  `Artifacts/ProjectGeneration/WordQuest`. Its ten source/config/project files were
  copied without overwriting existing work into `Game`; staging retained locally.
- Changed generated EngineAssociation from a local GUID to portable `5.8`; the build
  helper checks exact 5.8.2/CL. Original module/target code remains intact.
- Created environment, companion and panel reconstruction candidates in `ArtSource`.
  No candidate is approved or imported; identity and edge issues remain.
- Transcribed EQUIVOCAL prototype fixture, with review pending and no release claim.
- Retained Git exclusions/LFS handling; added `.slnx` exclusion.
- Standalone Win64 Development game target compiled and linked successfully with
  MSVC 14.44.35222 / Windows SDK 10.0.26100.0. Output:
  `Game/Binaries/Win64/WordQuest.exe` (ignored). This is the blank generated module,
  not a playable G screen, cooked package or runtime test.
- On 2026-09-23, installed .NET Framework 4.8 SDK and targeting pack with VS
  Installer (exit 0). The real Win64 Development editor build then passed:
  7 actions, 189.25 seconds, exit 0. No engine dependency checks were bypassed.
- Added repository-specific internal PR review rules and a local Codex workflow.
  Initial dedicated review reported no actionable introduced defects.
- The real editor loaded the compiled WordQuest module and template world;
  map checking reported zero errors/warnings. Editor-open evidence is recorded in
  `Docs/QA/P00/EDITOR-BUILD-20260923.md`. Initial shader compilation took about
  19 minutes. This is a foundation smoke check, not a G gameplay acceptance test.
- Disabled the unused Android File Server plugin and removed its automatically
  generated token/settings before commit. The editor build passed again.

## Blocking evidence

1. Android engine binaries/target receipt are absent. Turnkey accepted Win64, but
   Android-only verification found no platform to check despite returning exit 0.
   This is not an Android pass. SDK/JDK compatibility remains unresolved.
2. No adb-connected phone; Mac/iPhone access and target device models unknown.
3. Static art fidelity, font identification/licensing and fixture approval remain open.

The firewall dialog triggered by initial UBA execution needs user handling; automation
has not changed security settings. Subsequent builds use `-NoUBA`. PowerShell script
execution is restricted; helpers use installed Python without changing that policy.
The successful game build still reported UBA local execution; no firewall-policy
change or complete removal of UBA internals is claimed.

## Gate state

P00/UI00 inventory is recorded with missing resources. P01 mobile feasibility,
UI01 static fidelity, UI02 motion and physical-device acceptance are **not passed**.
No G gameplay screen, interaction, motion, G runtime capture, package or device test
has been implemented/executed. Generated images are working art only.

## Resume

Read [environment](../Setup/ENVIRONMENT.md), [toolchain](../Setup/TOOLCHAIN-LOCK.md),
[decisions](../Decisions/DECISIONS.md), [UI00 inventory](../QA/UI00/INVENTORY.md) and
[asset handoff](../../ArtSource/G-ASSET-HANDOFF.md). Use
`python Tools/BuildScripts/build_wordquest.py` to reproduce the editor build.
Keep missing mobile evidence explicit. Finish G static proof before UI02 or H/I.
Preserve all supplied planning packages and original images unchanged.
