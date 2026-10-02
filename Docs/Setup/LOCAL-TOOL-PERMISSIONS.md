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
