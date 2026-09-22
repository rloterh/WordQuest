# WordQuest — G/H/I UI, Realms & Motion Addendum

Prepared for Robert Loterh • 21 September 2026 • v1.1 visual-direction addendum

This package extends the original WordQuest Production Blueprint. It captures Robert's preference for the exact G/H/I concepts, theme variety on app opening, animated environments, and possible Wordmaster characters/teams. It provides original reference images, three new home-screen concepts, production requirements, and bounded execution prompts. No Unreal UI, rigged character, decomposed art asset, animation or packaged game has been implemented here.

## Immediate decisions

- Launch with **G Celestial Reverie**, **H Moonlit Wisteria**, and **I Starlight Library** as the three visual realms.
- Proposed default: **Surprise me** selects a realm at a fresh visit; keep that realm across screens for the session. Provide fixed and companion-linked modes.
- Preserve the original gameplay images as authoritative visual targets. Do not ask a coding agent to freely reinterpret them.
- Create layered art and real UI controls, then add restrained ambient motion. A flattened screenshot is not a responsive animated interface.
- Recommend three optional launch companions using the three existing spirits. Plan stable data IDs for expansion now; defer twelve fully produced Houses/characters and multiplayer teams.
- Next implementation proof: one faithful G gameplay screen with live text/controls and one moving cloud layer, running on a real phone. Then H/I and the rest of the screen family.

## Read in order

1. [Decisions and blueprint integration](docs/01-Decisions-and-Integration.md)
2. [Realm behavior and character settings](docs/02-Realm-Behavior.md)
3. [Reference fidelity contract](docs/03-Reference-Fidelity.md)
4. [Screen and component system](docs/04-Screens-and-Components.md)
5. [Living environments and motion](docs/05-Motion-and-Living-Environments.md)
6. [Asset preparation and Unreal handoff](docs/06-Asset-and-Unreal-Pipeline.md)
7. [Companions and future Houses](docs/07-Companions-and-Houses.md)
8. [QA, performance and acceptance](docs/08-QA-and-Acceptance.md)
9. [Production sequence and capacity](docs/09-Production-Sequence.md)
10. [Sources and limitations](docs/10-Sources-and-Limitations.md)
11. [Execution prompt index](prompts/00-Execution-Index.md)

## Visual references

| Realm | Original gameplay target | New home concept |
|---|---|---|
| G — Celestial Reverie | [G gameplay](references/G-Celestial-Reverie-Gameplay.png) | [G home draft](references/G-Celestial-Reverie-Home-Draft.png) |
| H — Moonlit Wisteria | [H gameplay](references/H-Moonlit-Wisteria-Gameplay.png) | [H home draft](references/H-Moonlit-Wisteria-Home-Draft.png) |
| I — Starlight Library | [I gameplay](references/I-Starlight-Library-Gameplay.png) | [I home draft](references/I-Starlight-Library-Home-Draft.png) |

Original gameplay targets express the user-selected visual direction. Home screens are newly generated proposals, not owner-approved final layouts. Their example progress values are mock data. Keep the original image files unchanged; the included manifest records their actual dimensions and hashes.

## Use with the earlier package

Extract beside the original planning directory. Attach this README, document 01, the selected realm reference, and the relevant UI prompt in the coding workspace. Follow the integration map: these tasks extend P01/P06/P07/P09 and do not bypass environment checks, learning tests or platform qualification. Read the original P00 first if it has not run.

A separate combined Markdown guide accompanies the ZIP for convenient reading. The ZIP is the complete handoff because it also includes images and structured specifications.
