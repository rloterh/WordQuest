# Release, support, and operations runbook

## Release definition

A release candidate is a reproducible signed build containing the promised approved content, with entitlement handling, save migration, accessibility, performance and operational evidence. This plan does not authorize public publication or purchases today. The execution sequence prepares a reviewable candidate; the owner decides release when the gates pass.

## Platform prerequisites

Android: pinned engine-compatible SDK/NDK/JDK, required architectures, package name, signing-key custody, current target API and store packaging requirements, real-device qualification and current testing obligations for the actual developer account.

iOS: supported engine/Xcode/macOS combination, Mac build path, physical iPhone testing, bundle ID, certificates/profiles, required privacy disclosures and store account. Windows-only editor work cannot certify iOS. Record exact values from official requirements during P00/P18 rather than freezing guessed versions in this dated plan.

Windows expansion: chosen distribution channel, supported architecture, installer/package signing, DPI/input/accessibility, persistence paths, updates and commerce differences. Do not assume the Android purchase SDK works on Windows.

## Store-readiness checklist

- Brand/title cleared sufficiently for commercial use; business and support identity supplied by owner.
- Accurate description, original icon, real gameplay screenshots, preview footage, age/content questionnaire and category.
- Purchase products configured, price approved, sandbox purchase/restore/refund behavior demonstrated.
- Privacy policy, data disclosures, account deletion behavior and permissions match actual implementation.
- Relevant font, image, audio, dictionary, engine and plugin rights recorded.
- Review access or demonstration instructions provided where necessary; staging credentials never shipped in the client.
- All content in screenshots is present; no unsupported learning, score or ranking claims.
- Current rules checked for each intended geography/storefront, including region-specific commerce differences.

Apple's current guidelines cover complete metadata, tested builds, review access and purchase information. Google provides its app-creation and setup workflow. They change; recheck at submission. [Apple review guidelines](https://developer.apple.com/app-store/review/guidelines/) · [Google Play setup](https://support.google.com/googleplay/android-developer/answer/9859152)

## Release candidate sequence

1. Freeze candidate code/content/config identifiers; produce changelog and known-issues list.
2. Build from clean checkout using pinned tools; archive logs and hashes.
3. Run required domain/content/integration gates; execute physical-device matrix.
4. Validate production-like backend, least-privilege access, purchase sandbox and content signatures.
5. Exercise backup restore, bundle rollback, disable flag and support intake.
6. Produce store metadata, disclosures, screenshots, and review notes.
7. Present candidate evidence and unresolved owner decisions.
8. After explicit owner publication decision, submit/distribute through the intended platform workflow.
9. Use available staged distribution controls and monitor before widening exposure.

## Monitoring

Dashboards: crash-free sessions by build/device, startup and frame regressions, content activation errors, sync backlog, purchase verification failures, item reports, support response time and backend cost. Alert thresholds begin conservative and are tuned to traffic. A sudden transaction or save failure is urgent even at low volume.

## Incident classes

Critical: save loss, incorrect entitlements, privacy exposure, widespread crash, blocked campaign, systematically wrong teaching. Disable affected optional features/content where safe, preserve evidence, communicate concretely, and begin repair. Do not clear users' saves to hide a migration problem.

High: repeated device-specific crash, broken audio bundle, unfair capstone, stuck download. Contain by config/content rollback or platform hotfix; publish a known-issue note where appropriate.

Low: cosmetic clipping or minor copy error without semantic impact. Schedule a patch with a regression check.

## Rollback

Content: revert manifest to a compatible prior bundle, preserve IDs and account for withdrawn items; keep session pinning. Backend: revert deploy where compatible; use backward-compatible migrations and tested restore procedures. Client: disable risky features remotely and prepare corrected store build; a store binary cannot be assumed instantly reversible.

## Support and data requests

Support report contains build/device, content ID/version, safe error code and optional user explanation. Avoid raw receipt, private message or audio attachments by default. Document response ownership, refund routing, account deletion, local reset and lost-device recovery. Deletion requests must propagate to active storage and respect a documented backup retention policy; verify current requirements with appropriate advice for the actual business.

## Post-launch first month

Daily early review of crashes/purchases/content failures; weekly cohort and learning review; one controlled content update after rollback proof; support taxonomy; first cost report; decision on acquisition expansion. Freeze discretionary new features during an unresolved reliability or content-quality incident.
