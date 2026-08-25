# 4 · The filing rules

The complete convention. This is the reference; the agent-facing version is `CLAUDE.md` in the vault
root. If you change one, change both.

## Choose the room by what the note IS

Not what it is about. This is the rule people get wrong first.

A paper about a method goes in `20_Literature/`, because it is a paper. A note on how *you* run that
method goes in `10_Research/`, because it is a method. A note on the person who invented it goes in
`people/`. The subject is the same in all three; the type is different, and the type decides.

| Folder | What goes in it | Test |
|---|---|---|
| `00_Inbox/` | anything unsorted | "I am in a hurry" |
| `10_Research/` | the project: aims, methods, results, decisions | "this is my work" |
| `20_Literature/` | one note per paper, plus concept notes | "someone else wrote this" |
| `30_Grants/` | applications, deadlines, reports | "money or a funder" |
| `40_Outreach/` | talks, updates, conferences, peer review | "someone outside will see it" |
| `50_Side/` | side projects, learning | "mine, but not the main thing" |
| `90_Daily/` | one note per day | "this happened today" |
| `people/` | one note per human | "this is a person" |

## Titles

Real and human. Never a bare date, never a code, never `notes_final_v2`.

Good: `Deng 2023 - developing cortex MPRA`, `Why the May cohort was excluded`, `Simon Furney`.
Bad: `paper_04`, `2026-08-25-notes`, `meeting`.

Renaming is free. Obsidian rewrites every link that points at the note. So write a decent title now
and improve it whenever a better one occurs to you.

## Frontmatter

Every note. Same fields, same order.

```yaml
---
title: "Identical to the H1 below"
type: paper
status: current
tags: [type/paper, topic/chromatin]
last-reviewed: 2026-08-25
---
```

| Field | Rule |
|---|---|
| `title` | matches the H1. quoted, because colons break YAML |
| `type` | one of: paper, result, method, meeting, person, grant, concept, reference, strategy, moc, style-guide, daily |
| `status` | one of: current, active, done, archived |
| `tags` | the `type/` tag always, `status/` if useful, then `topic/` |
| `last-reviewed` | ISO date. this is what lets you find rotting notes later |

`last-reviewed` looks like bureaucracy and is not. It is the only field that tells you which of your
"durable facts" have quietly stopped being true.

## The `## Related` block

**Required. At the bottom. At least two links.**

```markdown
## Related
- [[Deng 2023 - developing cortex MPRA]] · [[Six analytical layers]]
- [[_meta/MOC-literature]]
```

If you genuinely cannot find two, link the room's MOC and write one line saying why the note is
isolated. That line is usually the interesting part.

A note with no inbound or outbound links is invisible. It will not show in the graph, it will not
surface when you are working nearby, and you will rewrite it in eight months without realising.

## Tags

Three namespaces. `type/`, `status/`, `topic/`. Nothing else.

`topic/` is lowercase and hyphenated, and you **reuse before you invent**. Search the vault first.
Two tags meaning the same thing is worse than one imperfect tag, and tag sprawl is the most common
way a vault quietly stops being searchable.

Do not build tag hierarchies. `topic/genomics/chromatin/atac` is a folder wearing a costume.

## Callouts, for epistemic status

Use these to mark which sentences are established and which are guesses.

```markdown
> [!note] plain context, uncontroversial
> [!hypothesis] believed but not shown. say what would kill it
> [!warning] a trap, a confound, a limit
> [!quote] someone else's words, with the source
> [!todo] an action, with an owner
```

**A hypothesis must never be written as a note.** If a reader cannot tell what you have shown from
what you hope, the vault has lost the only property that makes it worth keeping.

## Never

- Never invent a citation, a number, a date or a result. Write `TODO: confirm` instead.
- Never delete someone's note. Mark it `status/archived`.
- Never reorganise folders without being asked. Additive by default.
- Never file to `00_Inbox/` permanently. It is a queue, not a room.
