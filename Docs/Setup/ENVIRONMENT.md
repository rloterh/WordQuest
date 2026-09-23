# Environment inventory — 2026-09-22

Workspace: `C:\Projects\WordQuest`. Initial commit inspected: `ebc3059`; clean `dev`
tracking `origin/dev`. Existing remote: `https://github.com/rloterh/WordQuest.git`.
No existing Unreal project, learning implementation or navigation was found.
Working branch: `kickoff/g-visual-proof`, based on `dev`.

## Verified locally

| Tool/resource | Evidence | Readiness |
| --- | --- | --- |
| Unreal | `C:\Program Files\Epic Games\UE_5.8`; Build.version: 5.8.2, changelist 56702186, compatible 55116800, `++UE5+Release-5.8` | Candidate retained; production/mobile gate pending |
| Blender | `C:\Program Files\Blender Foundation\Blender 5.1\blender.exe --version`: 5.1.0, hash adfe2921d5f3 | Executable verified; export round trip pending |
| VS Build Tools | vswhere: 2022 17.14.26, installation 17.14.36930.0 | Installed |
| C++ | `VC\Tools\MSVC\14.44.35207\bin\Hostx64\x64\cl.exe`: compiler 19.44.35222 | Actual patch exceeds banned 14.44.35210; game and editor builds passed |
| Windows SDK | Includes 10.0.26100.0 | Within installed engine SDK range |
| Bundled .NET | Engine `Binaries\ThirdParty\DotNet\10.0\win-x64\dotnet.exe --version`: 10.0.203 | Use engine bundled runtime |
| .NET Framework SDK | 4.8 SDK and targeting pack installed 2026-09-23; NETFXSDK registry and v4.8 reference assemblies verified | Editor dependency resolved |
| Git / LFS | 2.53.0.windows.1 / 3.7.1; filters and pre-push hook present | Existing configuration retained |
| GitHub CLI | Authenticated; no open repository PRs at inventory | Existing remote available for requested PR |
| Android Studio | Product metadata AI-261.26222.65.2614.16204760 | Installed; not a packaging pass |
| Android SDK | `%LOCALAPPDATA%\Android\Sdk`; platforms 34, 36, 37.0; build-tools 34.0.0, 35.0.0, 36.0.0 | Needs engine validation |
| NDK | 27.3.13750724, source.properties says r27d | Engine accepts r27c–r29; preferred r27c differs |
| Java | PATH Temurin 17.0.20.1; Android Studio JBR 25.0.3 | Neither is public documentation's JDK 21 recommendation; packaging unresolved |
| Android engine support | `Engine/Binaries/Android` and required UnrealGame target receipts absent; Android-only Turnkey selected no platform | Platform installation required before packaging |
| Android device | `adb devices -l`: empty | Physical-device validation blocked |
| OS | Windows 11 Pro 10.0.26200 | Verified via CIM |
| CPU/RAM | i9-11900H, 8 cores/16 threads; approximately 31.7 GiB usable RAM, 6.1 GiB available at inventory | Build concurrency must respect available memory |
| GPU | Intel UHD 32.0.101.7085; NVIDIA RTX A4000 Laptop 32.0.15.9595 | CIM VRAM field is insufficient to establish actual VRAM |
| Disk | C: approximately 123.7 GiB free; D: approximately 21.9 GiB free | Snapshot, not reserved capacity |
| Mac/Xcode/iPhone | No access established | iOS qualification pending owner hardware details |
| Store accounts/signing | Not inspected; no credentials requested | Later release dependency |

## Compatibility evidence

Read installed `Engine/Config/Windows/Windows_SDK.json` and
`Engine/Config/Android/Android_SDK.json`. Windows accepts SDK 10.0.19041.0 through
10.9.99999.0 and prefers MSVC 14.44 or 14.50 with specified bad patches excluded.
Android local configuration requests API 36/build-tools 36.0.0 and NDK 27.2.12479018.

[Epic's Android requirements](https://dev.epicgames.com/documentation/en-us/unreal-engine/android-development-requirements-for-unreal-engine),
accessed 2026-09-22, instead list API 35, build-tools 35.0.1 and OpenJDK 21.0.3.
Record this discrepancy; use installed engine validation and real packaging to resolve
compatibility. Do not install or upgrade tools based on the planning package alone.
[Epic's Visual Studio guide](https://dev.epicgames.com/documentation/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine)
lists VS 2022 17.14+ for UE 5.8.

## Agent capabilities

Filesystem, PowerShell, Git, native executables, local image viewing and GitHub CLI
are available. Computer Use can inspect the existing Unreal browser; project-dialog
interaction has encountered minimized-window and user-input interruptions. No project
generation or runtime verification is implied by this capability. Image generation is
available to attempt reference-guided working layers, subject to inspection. No Fable
API or external editor/reviewer access has been established. One implementation agent.

## Executed follow-up

Unreal generated Blank C++ / Mobile / Scalable source in
`Artifacts/ProjectGeneration/WordQuest`; its ten project/config/source files were
copied into `Game` with an overwrite guard. Module/build/target files are genuinely
engine-generated. EngineAssociation was normalized to `5.8` for other checkouts;
the build helper verifies exact patch and changelist.

The initial editor compile and repository build helper both failed in SwarmInterface:
`Could not find NetFxSDK install dir`. On 2026-09-23, Visual Studio Installer added
the .NET Framework SDK (4.8) and targeting pack successfully (exit 0). The .NET 10
SDK is a distinct component. A subsequent editor build passed: 7 actions, exit 0,
189.25 seconds. See `Docs/QA/P00/EDITOR-BUILD-20260923.md` for follow-up evidence.

The separate Win64 Development **game** target compiled and linked successfully:
11 actions, MSVC 14.44.35222, Windows SDK 10.0.26100.0, exit 0. The blank module's
executable exists under ignored `Game/Binaries/Win64`. It has not been run or packaged;
gameplay implementation remains pending; editor compilation now passes.

Turnkey reports Win64 SDK valid. Android-only verification selected no platform and
returned 0; inspection confirmed missing engine Android binaries/target receipt.
That exit code is **not** an Android pass. Initial UBA invocation raised a Windows
firewall prompt; no security permission was granted by automation. Later builds use
`-NoUBA`. PowerShell script execution is restricted, so helpers use installed Python
without changing system execution policy. Python 3.14 is available; Pillow is absent,
and no package was installed. PNG inspection used System.Drawing and standard-library
header parsing; originals were never edited.

Immediate needs: accepted art layers/fonts and prototype fixture review.
Later needs: engine Android platform support, resolved
SDK/JDK packaging, named physical phones, iOS resources and release checks.
