# UX, interaction, and accessibility specification

## Information architecture

Primary destinations: Journey, Practice, Lexicon, Profile. Journey is the default home. Settings and support remain accessible from every safe pause point. Purchase is offered at a clear chapter boundary and from a dedicated campaign page. Do not occupy the primary navigation with a store.

Portrait phones are the primary layout. Tablets use a wider scene with a bounded reading panel. Windows uses a landscape composition with keyboard support after mobile qualification. Never stretch a phone layout across a desktop without reconsidering spacing and reading width.

## Screen contracts

| Screen | Primary action | Required secondary states |
|---|---|---|
| Welcome | Start adventure | Continue existing save, accessibility shortcut, legal links |
| Goal/diagnostic | Choose path or skip | Honest estimate, progress, pause/resume |
| Journey | Continue mission | Completed, locked with reason, downloaded, downloading |
| Mission intro | Enter | Back, optional recap, loading failure |
| Challenge | Submit answer | Hint, undo, audio, pause, disabled/selected/feedback |
| Explanation | Continue | Why alternatives fail, review word, report issue |
| Mission result | Continue journey | Replay, strengthened words, restoration progress |
| Practice | Begin capped session | No due words, weak skills, optional new trail |
| Lexicon | Open word | Search, filters, empty result, offline audio |
| Word detail | Practice this sense | Meaning, audio, examples, collocations, evidence |
| Campaign purchase | Unlock campaign | Localized price, pending, cancelled, failed, restore |
| Profile/sync | Manage progress | Guest warning, merge preview, conflict, deletion |
| Settings | Adjust experience | Text, motion, sound, input, reminders, downloads |
| Support | Report problem | Content ID included, offline queued report, contact |

## Challenge layout

At a 390×844 logical design reference: top region holds a compact progress indicator and pause; central region holds the scene and essential text; lower region holds the interaction; bottom holds submit/hint controls above the safe area. Treat proportions as a starting composition, not fixed coordinates. The native keyboard must not cover the clue or submit control.

Body target 18–20 logical units with comfortable leading. Support approximately 150–200% text enlargement through reflow and scrolling; exact platform mapping is verified in implementation. Minimum touch area target 48 logical units on Android and at least platform-equivalent comfortable size on iOS. Test long words, repeated letters, large fonts, notches, and narrow devices.

## Input rules

Touch-down gives immediate visual response; touch-up inside commits selection. Selection is distinct from submission for multiple choice. Ignore duplicate submit events using attempt IDs, not only a button disable. Drag interactions always have a tap alternative. Keyboard focus is visible, traversal is logical, and Escape/back opens pause or navigates safely rather than losing progress.

Audio replay does not advance the question or count as a wrong answer. A spoken clue cannot be the only route to a correct answer. Pronunciation playback has text/transcription equivalent as appropriate.

## Feedback language

Correct: 'Exactly—equivocal leaves more than one interpretation open.'
Near miss: 'Plausible, but this sentence emphasizes uncertainty rather than disagreement.'
After help: 'You found it with a clue. We will revisit it later.'
No connection: 'Your progress is saved on this device. Sync will resume when you reconnect.'
No due review: 'Your review is up to date. Explore a new trail or continue the story.'

Avoid 'Wrong!', faux praise for every tap, vocabulary-size claims from tiny diagnostics, and punitive streak copy.

## Accessibility requirements

- Full untimed core campaign; optional timers clearly isolated.
- No colour-only correctness or completion cues; pair with icon and text.
- Reduced motion removes camera travel, repeated particles, screen shake and large spatial transitions while preserving outcome feedback.
- Independent music, effects, voice, and haptics controls; subtitles for narrative speech.
- Screen-reader labels and focus order must be tested on actual target platforms. Unreal's platform accessibility limitations are an early feasibility risk, not something a designer can mark complete from a mockup.
- Reflowed large text; meaning and controls remain visible without shrinking type to fit.
- High-contrast reading surface, restrained glow behind text, no rapid flashing.
- Allow guided alternatives for letter rearrangement and for motor-intensive gestures.
- Meaning/usage scoring is independent of accent and reading speed.

Use current platform accessibility guidance during implementation. Contrast targets are design checks; do not claim complete legal or WCAG conformance from a visual audit alone.

## Save and interruption behavior

Commit an attempt before issuing a reward animation. Pause on backgrounding; stop timers and audio where appropriate. Resume at the last safe interaction boundary without resubmitting. A interrupted restoration cinematic resumes or skips to the persisted final state. A lost network does not reset a challenge.

## First-time experience

One interaction concept per step. Explain hints only when relevant. Offer the diagnostic after the first success or as an optional initial choice; never require a 20-question test before seeing the game. Introduce advanced words with supportive context immediately.

## Prototype validation

Observe at least five intended users with minimal guidance. Tasks: start as guest, solve an unfamiliar target, find explanation, use hint, replay audio, resume after interruption, change text size, find a word, distinguish mission score from retained knowledge. Record confusion and unintended taps. Revise repeated failure points before high-cost polish.
