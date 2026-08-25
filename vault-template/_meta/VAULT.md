---
title: "Vault guide"
type: style-guide
status: current
tags: [type/style-guide, topic/vault-structure]
last-reviewed: 2026-08-25
---

# Vault guide

The operating manual for this vault, written for the human. The agent-facing version of the same
rules is in `CLAUDE.md` at the vault root. If you change one, change both.

## What this vault is for

[One paragraph. What work does this vault serve, and what would make it a success? Write this before
you write anything else, because every later decision hangs off it.]

## The reframe

This is not a system to build. It is a system to **wire together and instrument**. The pieces
already exist: you have files, you have an agent, you have work. What was missing was a place for
the durable facts and the timestamped record to live, and a written convention so an agent can find
its way around without being told twice.

The build cost is near zero on purpose. If it starts costing real time, you have gone wrong.

## The five harness pieces

| Piece | What it is | Where it lives |
|---|---|---|
| Procedural memory | how the agent should behave | `CLAUDE.md`, this file, `99_Templates/` |
| Tools | what the agent can actually do | your agent's file access, plus any connectors you add |
| A loop with a stop | multi-step work that ends with a human | the one loop below |
| Semantic memory | durable facts | `10_` to `50_`, and `people/` |
| Episodic memory | what happened and when | `90_Daily/`, and `00_Inbox/` before it is filed |

## The naming rule

Real, human titles. Never a date alone, never a code alone. Obsidian rewrites every link when you
rename, so a decent title today costs nothing and can be improved forever.

## The one loop

Instrument **one** loop properly before you add a second. Mine is the paper-a-day loop:

1. a paper arrives
2. the agent digests it into a note in `20_Literature/`
3. today's daily note records that it was read
4. **the agent links it** to the part of the project it touches and any claim it supports or threatens
5. I approve, or send it back

Step 4 is the one that compounds. Step 5 is not optional.

Other loops worth instrumenting later, one at a time: the supervisor or manager update, the grant
section, the weekly review itself.

## The weekly review

Friday, fifteen minutes. Three questions:

1. Did it help me learn anything?
2. Did it survive contact with a real reader?
3. What broke or annoyed me?

Then: `00_Inbox/` to zero, link or bin the orphans in the graph view, promote real decisions out of
the daily notes, and name one bottleneck for the next fortnight.

## Guardrails

> [!warning] Your moat is the work, not the workflow
> This makes you faster and a better reader. It is not the thing you are judged on. If the vault
> starts competing with the work for attention, the vault loses.

> [!warning] Build nothing that is a project
> Only the near-zero-cost, immediate-payoff parts: the rooms, the conventions, one loop, the weekly
> review. Everything else waits until the real deliverable is out of the door.

## Obsidian setup

Free, local, no account needed. Plugins worth having on day one:

- **Dataview**, so frontmatter becomes live tables
- **Templater**, so new notes fill their own frontmatter
- **Tag Wrangler**, so you can rename and merge tags safely
- Core plugins on: Graph view, Outline, Daily notes, Templates

## Related

- [[MOC]] · [[tag-conventions]] · [[callout-conventions]]
