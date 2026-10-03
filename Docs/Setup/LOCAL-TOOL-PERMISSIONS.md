# Local unattended development tools

On 2026-10-02 the owner requested persistent permissions for GPT to use Unreal
and related tools without repeated permission prompts. These settings are local
to the owner's computer; merging this documentation does not grant other machines
access or alter game/release acceptance.

## Saved settings

The already-trusted WordQuest checkout has an untracked `.codex/config.toml`:

```toml
approval_policy = "never"
sandbox_mode = "danger-full-access"
```

Its path is excluded through local `.git/info/exclude`. Other projects retain
their existing defaults. CLI flags and host/managed policies can take precedence.
The current session already had unrestricted shell execution before this change.

The user's existing `$CODEX_HOME/config.toml` gained:

```toml
[computer_use.windows]
always_allowed_app_ids = ["UnrealEditor.exe", "blender.exe", "studio64.exe", "EpicGamesLauncher.exe", "WordQuest.exe"]
```

Each executable was located in the installed toolchain. These names follow the
documented desktop-app identifier format; a live Computer Use inventory has not
yet confirmed their canonical identifiers. Existing user settings were preserved
and a timestamped local backup was made before editing. No personal configuration
or backup is committed. The Computer Use plugins were already enabled.

## Verification and desktop connection

Python `tomllib` parsed both files, confirmed the intended values, and verified
all unrelated user settings were unchanged. `git check-ignore` confirmed the
project config is excluded. The installed CLI loaded the configuration;
`codex doctor --summary` reported unrestricted filesystem, enabled network and
approval Never. This is shell configuration evidence, not a GUI permission test.

The supported `@oai/sky` package initialized, but `sky.list_apps()` returned:

```text
Computer Use native pipe is unavailable: failed to connect native pipe:
The system cannot find the file specified. (os error 2)
```

The diagnostic reported the desktop app installed but not running. The supported
`codex app C:\Projects\WordQuest` command then returned successfully to request
opening the workspace. A second `sky.list_apps()` attempt after that launch
returned the same native-pipe error; native desktop control remains unavailable.

If the native connection remains unavailable, open the desktop app's
**Plugins > Computer Use**, enable it if offered, turn on its server and skill,
and select **Try now**. Review **Settings > Computer use** for the saved apps.
Keep the target app visible in the active, unlocked Windows desktop session.
Once connected, verify the returned Unreal/app identifier and perform an observed
read-only target-window check before claiming unattended GUI access works.

The Computer Use skill prohibits automating the ChatGPT desktop UI, so its host
controls require an owner action. No helper executable was spawned manually and
no security-policy bypass was added. Windows administrator/security dialogs,
managed policies, physical-phone adb authorization, owner merge authority and
all original visual/device/release gates remain separate. No game build or
physical-device acceptance is claimed by this configuration change.

Sources checked 2026-10-02:

- [Config basics](https://learn.chatgpt.com/docs/config-file/config-basic)
- [Configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)
- [Computer Use setup and Windows app policy](https://learn.chatgpt.com/docs/computer-use)

Dedicated read-only PR review of clean `7fc6d40` against actual `origin/dev`
(`e2ef2b0`) completed with exit 0 and no actionable introduced defects. Head
and worktree were unchanged; local evidence is in
`Artifacts/Reviews/20261002-205247`. The review covers this documentation, not a
live GUI permission test.

## Windows Firewall prompts on dated builds

On 2026-10-03 the owner explicitly requested automatic permission for the Windows
Security UnrealGame prompt. Each dated packaged executable has a new full path,
so approving one archive does not cover the next. This is separate from Codex's
already-saved approval Never settings.

A one-time elevated installer completed successfully at 04:58:41 UTC. The local
`WordQuest-Development-Firewall` scheduled task runs as SYSTEM every minute and
can be invoked by the owner with read/execute task access, without further UAC.
Its updater is installed under `C:/ProgramData/WordQuestDevelopmentFirewall`,
owned by Administrators; only SYSTEM/Administrators can write it. The owner has
read/execute access. It never executes project code or accepts arbitrary arguments.
Installer/source/logs are local and excluded under `Artifacts/Tools/WindowsFirewall`.
Personal SIDs and local installation JSON are not committed.

The updater permits inbound traffic from `LocalSubnet` on Private/Public profiles
for the installed UE 5.8 UnrealEditor, UnrealEditor-Cmd and UnrealGame executables,
the project Game binary, and exact WordQuest binaries in recognized dated
Archive paths beneath this checkout. It creates stable program-specific
rules in group `WordQuest local development (owner authorized)`. It removes only
Windows-generated Query User block rules for those exact apps, where present.
Firewall profiles remain enabled and notification settings for other apps are
unchanged. This grants local-network access, not arbitrary internet inbound access.

`package_g_win64.py` invokes `local_firewall.py` before completing a package on a
machine with this installed task. The helper waits for successful refresh and
requires the exact packaged binary in the receipt. Refresh failure leaves package
evidence incomplete; it does not silently claim permission. Other machines skip
the optional task without requesting elevation or changing firewall policy.

Verification: 34 program-specific allow rules; Private/Public, LocalSubnet, task
result 0; protected-file ACL inspected. A non-elevated task invocation and Python
helper refresh for the final art archive succeeded with no new administrator
prompt. Current receipts are `installation.json` / `last-run.json` in the protected
directory. Fresh clean package `20261003-050358-635571` passed with a successful
automatic refresh receipt at 05:06:45 UTC. The new archived executable has an
enabled ActiveStore Allow rule with the intended profile/address scope, and its
native capture launch passed. No additional UAC was required. The desktop pipe
remains unavailable, so no visual inspection of Windows Security is claimed.
The task uses process-only RemoteSigned script policy; global execution policies
were not changed.

To undo this local setup from an administrator PowerShell, remove the named task
and only the named rule group. Keep the firewall enabled. This setup does not grant
general administrator rights, approve owner merges or establish desktop GUI access.

Microsoft references checked 2026-10-03:

- [Program-specific firewall rules and LocalSubnet](https://learn.microsoft.com/en-us/powershell/module/netsecurity/new-netfirewallrule)
- [Scheduled-task access rights](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-security-hardening)
