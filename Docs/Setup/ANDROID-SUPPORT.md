# Add Android support to the existing engine

On 2026-10-02 the owner confirmed Epic Games Launcher installed this engine.
Fresh read-only inspection confirms:

- `%ProgramData%/Epic/EpicGamesLauncher/Data/Manifests/89E077949B8842AEF5F79AF771ADF574.item`
  identifies `Unreal Engine`, app `UE_5.8`, at
  `C:/Program Files/Epic Games/UE_5.8`, launch executable
  `Engine/Binaries/Win64/UnrealEditor.exe`.
- `%ProgramData%/Epic/UnrealEngineLauncher/LauncherInstalled.dat` includes `UE_5.8`,
  app version `5.8.2-56702186+++UE5+Release-5.8-Windows` at that same path.
- `Engine/Binaries/Android/UnrealGame.target` is still absent.
- The installed Android SDK's `adb devices -l` lists no device.

This resolves installation-manager identification, not Android qualification.
The initial P00 empty Launcher inventory remains historical evidence.

In **Epic Games Launcher → Unreal Engine → Library**, open the dropdown for the
existing **UE 5.8.2** installation, select **Options**, enable **Android** under
target platforms and choose **Apply**. Preserve the existing engine/version.
[Epic's installation guide](https://dev.epicgames.com/documentation/unreal-engine/install-unreal-engine)
and [mobile guide](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-creating-mobile-games)
describe optional platform support. Checked 2026-10-02.

Native Launcher control is unavailable in this session, so the owner performs this
UI step. No platform download, engine update, manifest editing or installation
completion is claimed. SDK/JDK compatibility remains unresolved until actual
Turnkey/platform results and packaging are inspected. Then connect and authorize a
physical phone for adb. Commands and unchanged physical-device acceptance gates
are in [Resume G proof](RESUME-G-PROOF.md).
