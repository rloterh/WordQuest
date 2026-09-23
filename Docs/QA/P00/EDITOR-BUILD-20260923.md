# Editor build follow-up: 2026-09-23

## Dependency fix

The owner requested a real build, fixes for failures, installation of the missing
.NET Framework dependency and internal PR review. Visual Studio Installer modified
the existing Build Tools 2022 installation with these two component IDs:

- `Microsoft.Net.Component.4.8.SDK`
- `Microsoft.Net.Component.4.8.TargetingPack`

The first non-elevated attempt returned 5007; its log explicitly required elevation
for passive mode. The elevated installer completed with exit 0 and no restart.
Verified NETFXSDK registry entry `4.8` pointing to
`C:\Program Files (x86)\Windows Kits\NETFXSDK\4.8\` and the v4.8 reference assembly
`mscorlib.dll`. No engine source changes or dependency-check bypass were needed.

Installer logs are in the local Windows temporary directory:
`dd_installer_20260923020840.log`, `dd_installer_elevated_20260923020919.log` and
`dd_setup_20260923020949.log`. The installer reported a channel-cache warning but
completed successfully; actual compilation below verifies the required dependency.

Microsoft references checked that day:
- [Installer command-line options](https://learn.microsoft.com/en-us/visualstudio/install/use-command-line-parameters-to-install-visual-studio?view=vs-2022)
- [Build Tools component IDs](https://learn.microsoft.com/en-us/visualstudio/install/workload-component-id-vs-build-tools?view=vs-2022)

## Real editor build: passed

Command: `python Tools/BuildScripts/build_wordquest.py` from repository root.

- UE 5.8.2, changelist 56702186, Win64 Development, `WordQuestEditor`.
- MSVC toolchain 14.44.35222; Windows SDK 10.0.26100.0.
- All 7 actions completed, including `UnrealEditor-WordQuest.dll` and target metadata.
- Result `Succeeded`, exit 0, total execution time 189.25 seconds.
- Full ignored log: `Artifacts/Logs/Build/WordQuestEditor-20260923-021027.log`.
- Previous standalone game-target success remains recorded in `EVIDENCE.md`.

## Editor startup and scope

Launched the verified engine executable with the repository's
`Game/WordQuest.uproject`, recording a dedicated log at
`Artifacts/Logs/Runtime/Editor-20260923.log`. The compiled `WordQuest` DLL loaded
at 02:32:39 UTC, engine initialization completed, and map checking reported
**0 errors and 0 warnings**. Initial startup took 1156.66 seconds while compiling
the first shader cache. The running editor was visually inspected with its
template world, normal toolbar and no blocking dialog.

Captured evidence: `Artifacts/Captures/P00/WordQuest-Editor-20260923.png` (ignored).

First startup expanded the generated renderer/map defaults in `DefaultEngine.ini`;
those settings are retained. It also generated Android File Server settings with
a development token. The unused `AndroidFileServer` plugin is now explicitly
disabled in the project descriptor and its generated config section removed before
commit. Engine source confirms `PostInitProperties` otherwise writes a new token
to default config. No token is committed and no firewall setting was changed.

After this fix, the editor build passed again (18.85 seconds, exit 0), with log
`Artifacts/Logs/Build/WordQuestEditor-20260923-035659.log`. A fresh editor startup
is being verified separately in `Artifacts/Logs/Runtime/Editor-20260923-Verified.log`.

No G gameplay, packaged game, Android build, phone acceptance or UI01/UI02 gate is
claimed. The generated template still needs its documented mobile-renderer setup.
