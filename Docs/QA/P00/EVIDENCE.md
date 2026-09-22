# P00 / kickoff execution evidence — 2026-09-22

Baseline: clean `dev` at `ebc3059`. Branch: `kickoff/g-visual-proof`.
This record reports actual actions; it does not pass UI01/UI02 or mobile feasibility.

## Commands executed and observed results

| Command / action | Actual result |
| --- | --- |
| `Get-Location`; `git status --short --branch`; `git remote -v`; `git log -5 --oneline` | Confirmed C:\Projects\WordQuest, clean existing repository and dev baseline |
| `Get-Content '<engine>\Engine\Build\Build.version'` | 5.8.2, CL 56702186, compatible CL 55116800 |
| `'<Blender 5.1>\blender.exe' --version` | 5.1.0, adfe2921d5f3 |
| `vswhere.exe -all -products '*' -format json` | Build Tools 2022 17.14.26 / 17.14.36930.0 |
| `'<MSVC 14.44.35207>\bin\Hostx64\x64\cl.exe'` | Banner 19.44.35222; usage output, not a compile |
| Engine-bundled `dotnet.exe --version` | 10.0.203 |
| `java -version`; Android Studio `jbr\bin\java.exe -version` | PATH 17.0.20.1; Studio 25.0.3 |
| Read SDK platform/build-tools directories and NDK `source.properties` | API 34/36/37.0; build-tools 34/35/36; NDK r27d 27.3.13750724 |
| `adb.exe devices -l` | Empty device list |
| CIM OS/CPU/GPU queries and `Get-PSDrive -PSProvider FileSystem` | Hardware snapshot in ENVIRONMENT.md; no performance benchmark |
| `git lfs version`; `git lfs env`; `Test-Path .git\hooks\pre-push` | LFS 3.7.1, filters configured, pre-push hook present |
| `gh auth status`; `gh pr list --state open ...` | Existing remote access available; no open PR at initial inventory; credentials not copied |
| PowerShell `Get-FileHash` of all six references | Six matching SHA-256 values |
| `python Tools/AssetImport/verify_references.py` | Six hash AND dimension checks passed |
| `python -m json.tool ContentSource/Challenges/G-Equivocal-Prototype.json` | JSON parses; not editorial signoff |
| System.Drawing read-only PNG inspection | Spirit RGBA, alpha 0 at corner; panel v001 RGB with baked checkerboard, v002 RGBA with alpha 0 at corner; no full edge-quality pass |
| `git check-attr filter -- <candidate PNG paths>` | LFS applies |
| `git check-ignore ...` | Intermediate build output and Artifacts logs ignored; Game/Build placeholder not ignored |

## Turnkey checks

Executed from repository root:

```powershell
& 'C:\Program Files\Epic Games\UE_5.8\Engine\Build\BatchFiles\RunUAT.bat' Turnkey -command=VerifySdk -platform=Win64+Android -unattended '-ReportFilename=C:\Projects\WordQuest\Artifacts\Logs\P00\TurnkeyReport.txt' '-log=C:\Projects\WordQuest\Artifacts\Logs\P00\Turnkey.log'
& 'C:\Program Files\Epic Games\UE_5.8\Engine\Build\BatchFiles\RunUAT.bat' Turnkey -command=VerifySdk -platform=Android -unattended '-ReportFilename=C:\Projects\WordQuest\Artifacts\Logs\P00\AndroidReport.txt'
```

Combined report contains only Win64: `Status=Valid`, `Current_Sdk=10.0.26100.0`.
Android-only output: `Platform(s) and/or device(s) needed for VerifySdk command`.
Both UAT processes exited 0. **Android did not pass.** Its required engine binaries
and `UnrealGame.target` receipt are absent. No `UpdateIfNeeded` or installer flag was
used. Requested `Turnkey.log` was not produced at that path; do not cite it as evidence.
Actual retained output: `Artifacts/Logs/P00/TurnkeyReport.txt`,
`Artifacts/Logs/P00/AndroidConsole.txt`; AndroidReport is empty.

## Unreal generation and editor build

Computer Use operated the existing Unreal 5.8 New Project dialog: Games → Blank →
C++ → Mobile → Scalable; name WordQuest; location
`C:\Projects\WordQuest\Artifacts\ProjectGeneration`. Clicked Create and inspected
the resulting source and failure dialog. Generation produced ten source/config/project
files, including real .uproject/.Build.cs/.Target.cs files. The empty DefaultEditor.ini
is an engine-generated file, not an invented placeholder. No .uasset/.umap was generated.

Copied only generated `Source`, `Config`, `Content` files and `.uproject` into `Game`
after checking that no destination file existed. Preserved staging and scaffold.
The project association was subsequently changed from machine GUID to `5.8`.

Unreal's initial automatic editor compile failed with RulesError due to missing
NetFxSDK in SwarmInterface. Its log is retained at
`Artifacts/Logs/P00/Initial-Editor-Build-Failure.txt`.

Executed `python Tools/BuildScripts/build_wordquest.py` against `Game`:
same RulesError, build exit **8**, command reported failure. Actual output is
`Artifacts/Logs/Build/WordQuestEditor-20260922-170158.log`. No source compiler or runtime
pass follows from this failure. The helper propagated the error rather than hiding it.

PowerShell `-File` helper attempts were rejected by the existing execution policy.
Replaced these task-created helpers with standard-library Python equivalents; did
not change policy or bypass it. Initial UBA execution raised a Windows firewall prompt.
No permission was granted by automation. Later commands use `-NoUBA`.

## Standalone game target — passed build, no runtime claim

Executed `python Tools/BuildScripts/build_wordquest.py --target Game`. Unreal ran UHT,
compiled the generated module and linked `Game/Binaries/Win64/WordQuest.exe`.
Result: **Succeeded**, exit **0**, 11 actions, 412.39 seconds. Log:
`Artifacts/Logs/Build/WordQuest-20260922-170445.log`.

Selected toolchain: MSVC **14.44.35222** from the 14.44.35207 folder and Windows SDK
**10.0.26100.0**. This verifies the native compiler on the blank game target; it does
not resolve the editor's SwarmInterface dependency. The engine reported a UBA local
executor despite `-NoUBA`; no claim is made that all UBA internals were disabled.
No cooked content, packaged application or executable runtime test was performed.

Final checks: Python helper AST parsing; four generated-art hashes; fixture JSON
structure with no initial selection and no release approval; local documentation
links; staged `git diff --check`; `git lfs fsck` all passed. Generated trailing
whitespace was normalized in three files without changing semantics. No source
planning-package file was changed. Credential-pattern scan found no matching files.

## Not performed / not passed

No gameplay implementation, native G capture, visual overlay, interaction test,
motion recording, texture import, packaged build, physical-phone test, accessibility
qualification, Blender export round trip or human editorial approval. Generated
images remain reconstruction candidates. The original planning packages are intact.

Follow `Docs/Setup/RESUME-G-PROOF.md` after resolving prerequisites. Generated logs
remain local under ignored `Artifacts`; this concise evidence report travels with Git.
