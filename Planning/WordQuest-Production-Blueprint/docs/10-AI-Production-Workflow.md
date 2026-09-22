# AI-assisted production workflow

## Roles for GPT-6 and Fable 5.1

Use the strongest available reasoning/coding capability for architecture, difficult defects, test design and integration. Use a separate review pass for semantic errors, edge cases, and compliance with the game's contracts. Either named assistant can implement or review depending on actual tool access and observed performance. The plan does not assume an unverified benchmark advantage or invent Fable's provider/API.

Record model label, tool version, task, output, evidence and cost/time where available. Compare assistants on the same small representative tasks: one C++ domain change, one content validator, one Unreal editor asset task, one visual correction, one bug diagnosis. Choose by successful verified output, not marketing adjectives.

## Task packet

Every prompt gets: objective, relevant documents only, current status, baseline commit, owned files, dependency state, constraints, acceptance evidence, and exact stop condition. Do not paste the entire planning bundle into every task. For visual work attach the approved reference plus the interaction and motion spec. A screenshot alone cannot specify behavior.

Official Codex guidance emphasizes concrete context, reproducible steps and verification. Our task packets apply that approach; the particular production roles here are design choices. [Official prompting guidance](https://learn.chatgpt.com/docs/prompting)

## Working loop

Inspect existing state → identify the smallest complete task → implement → build/run → inspect the result → correct defects → record evidence → review → integrate. Never treat a generated diff as tested software. Do not repeatedly ask the owner to approve ordinary refactors within the accepted scope. Escalate product changes, purchases, credentials, destructive actions and public release when needed.

If multiple agents are explicitly authorized in the implementation environment, separate by disjoint source files or worktrees. One writer owns each binary Unreal/Blender asset at a time. Never concurrently edit the same `.uasset`, `.umap`, or `.blend`. Cross-review can be sequential. Multi-agent execution is optional; the plan works with one assistant.

## Unreal and Blender automation

Text is the preferred source for C++, configuration, content JSON and deterministic scripts. Blueprints and binary assets require editor-supported operations. Agents must not fabricate binary asset bytes or claim an asset exists because a script was written. Where editor scripting is supported by the pinned build, use it to import assets, create documented structures, validate names and perform repeatable batch actions.

Unreal Python is an editor automation route, not the shipped mobile gameplay language. Confirm exact APIs in the installed engine before generating automation. Blender Python scripts should create reproducible collections/materials/export settings and operate in a disposable copy before modifying valuable art sources.

If the agent cannot control the editor, it must supply a numbered manual recipe with exact objects/properties, expected screenshot and verification steps. Mark the result blocked on editor execution. A C++ compile does not prove a UMG screen or Niagara effect behaves correctly.

## Evidence contract

Each milestone report records commit, files/artifacts, actual commands, exit results, device/build, content version, screenshots/video where relevant, remaining defects and gate disposition. Evidence paths must exist. A simulated result is labelled simulated. Failed tests remain visible after fixes with the final passing result linked. An unavailable device is a blocker, never an implied pass.

## Prompt execution discipline

Run one numbered task at a time unless dependency-independent work has explicit ownership. Continue routine corrective work inside a task until its criteria pass. If an environmental blocker prevents completion, deliver the concrete partial artifacts and exact recovery action. Do not rewrite the roadmap to label incomplete work complete.

At a context reset, read project status and the latest evidence report, inspect the repo, then resume the first incomplete dependency. Do not restart finished architecture or regenerate all assets. Update status after a meaningful completed unit.

## Runtime AI boundary

The campaign, answer keys, learning evidence and offline review use deterministic approved content. Optional AI lab feedback is advisory. It can explain a sense, suggest a corrected sentence, or role-play a bounded scenario. It cannot silently grant mastery, change published definitions, set prices, or publish new curriculum.

Gateway input: approved sense ID/version, bounded user text, task type. Output: structured judgment (appropriate/needs_revision/uncertain), short explanation, revised example and evidence reference. Keep secrets server-side; set quotas, timeouts and spending alerts. Treat user text as data, not instructions. Reject tool-use instructions embedded in responses; no arbitrary network/tool access.

On outage or uncertain judgment: show a reviewed explanation and allow practice to continue. Do not fail the learner. Voice input is optional, consent-based and separate from pronunciation claims; speech recognition errors and accents must not reduce knowledge scores.

## AI evaluation gate

Create at least 200 representative reviewed examples spanning valid usage, subtle misuse, multiple senses, nonsense, prompt injection, sensitive personal text and dialect variation. Human raters judge correctness, helpfulness and unjustified certainty. Initial target: no critical factual/privacy failure, at least 95% acceptable feedback on the evaluated set, and clearly reported uncertainty for ambiguous cases. This is an internal release target, not a claim that the model meets it now. Track latency/cost on actual requests and compare against a deterministic fallback.

If the optional lab fails, keep it off and ship the complete core game. No subscription or expensive API dependency is required for the launch experience.
