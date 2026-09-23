# Internal PR review

Use the installed, signed-in Codex CLI for a dedicated review in this checkout.
This keeps findings local; source context is processed by the configured Codex
service, so this is not an offline model. No GitHub bot, API secret or automatic
merge is configured. Repository review rules live in `AGENTS.md`.

From the repository root, for PR #1 (base `dev`):

```powershell
git fetch origin dev
codex login status
python Tools/Review/review_pr.py --base origin/dev
```

The helper records base/head SHAs, starting worktree status and process exit status
under timestamped `Artifacts/Reviews` directories. It separates the report from
connector/CLI diagnostics and requests a read-only sandbox with no approvals.
It uses the existing Codex model, login and connector configuration. Connector
startup warnings do not themselves mean a review failed; inspect the report and
exit status. Use a clean worktree for an unambiguous commit-based review.

Use the actual PR base for later reviews. Run on the final changes, triage findings, fix confirmed defects,
and rerun affected checks. An exit code of zero means the review completed, not
that its findings are resolved. Do not run simultaneous writers during review.
Summarize results under `Docs/QA`; raw transcripts remain ignored in `Artifacts`.

Before merging a foundation change, verify the editor target compiles and opens,
review findings are resolved or explicitly accepted, and PR claims match evidence.
UI fidelity, packaging and phone acceptance remain separate gates. The owner
retains the merge decision.

Optional future GitHub automation: enable Code review for this connected repository
in Codex settings, then request `@codex review` in a PR or enable Automatic reviews.
That account-level setting has not been enabled by these repository changes.

Sources checked 2026-09-23:
- [Codex CLI review](https://learn.chatgpt.com/docs/codex/cli)
- [GitHub review setup](https://learn.chatgpt.com/docs/third-party/github)

Local CLI verified: `codex-cli 0.154.0-alpha.6.2`; `codex review --help` supports
`--base`, `--commit` and `--uncommitted`; authentication uses the existing ChatGPT
login. CLI availability depends on the installed Codex/IDE extension being on PATH.
