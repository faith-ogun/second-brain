# How to work in this vault

You are working inside a markdown knowledge vault. This file is the procedural memory: it tells you
how to behave here. Read it before doing anything, and follow it exactly, because consistency is the
only thing that makes this vault navigable later.

Replace the bracketed lines below with your own before you start.

- **Owner:** [your name]
- **The work:** [one sentence on the project this vault serves]
- **Today's job, usually:** [what you mostly ask for. e.g. digest papers, draft sections, track admin]

## The rooms

| Folder | What goes in it |
|---|---|
| `00_Inbox/` | anything unsorted. cleared weekly. never leave something here permanently |
| `10_Research/` | the project itself: aims, methods, results, decisions |
| `20_Literature/` | one note per paper, plus concept notes |
| `30_Grants/` | applications, deadlines, reports, funder admin |
| `40_Outreach/` | talks, supervisor or manager updates, conferences, peer review |
| `50_Side/` | side projects, learning, anything not the main work |
| `90_Daily/` | one note per day, `YYYY-MM-DD.md`. append-only |
| `99_Templates/` | the shape of each note type. copy, do not edit, unless asked |
| `_meta/` | how the vault works, and the Maps of Content |
| `people/` | one note per human |

## Filing rules

When you create a note, all of the following are required.

1. **Pick the room by what the note IS, not what it is about.** A paper about a method goes in
   `20_Literature/` because it is a paper. A note describing how you run that method goes in
   `10_Research/` because it is a method.
2. **Give it a real, human title.** Never a bare date, never a code. `Deng 2023 - developing cortex
   MPRA` is a title. `paper_04.md` is not. Renaming later is free because links follow.
3. **Write the frontmatter**, exactly these fields, in this order:
   ```yaml
   ---
   title: "The same as the H1 below"
   type: paper            # paper|result|method|meeting|person|grant|concept|reference|strategy
   status: current        # current|active|done|archived
   tags: [type/paper, topic/whatever]
   last-reviewed: YYYY-MM-DD
   ---
   ```
4. **Open with an H1 that matches the title.**
5. **End with a `## Related` block** containing at least two `[[wikilinks]]`. This is not decoration.
   A note with no links is invisible to the graph and will be lost. If you genuinely cannot think of
   two, link the room's Map of Content in `_meta/` and say why in one line.
6. **Add the note to the relevant MOC** in `_meta/` if it is significant. Not every note; the ones a
   future reader would need signposted.
7. **Record it in today's daily note** in `90_Daily/`, one line, so the episodic record is complete.

## Tags

Tags are facets, not folders. Three namespaces only:

- `type/` mirrors the frontmatter `type`
- `status/` mirrors the frontmatter `status`
- `topic/` is the subject. lowercase, hyphenated, reuse existing ones before inventing new ones

Before inventing a `topic/` tag, grep the vault for something close. Tag sprawl is the most common
way a vault stops being searchable.

## Links

- Links carry the meaning; folders only carry tidiness.
- Link the specific note, not the folder.
- A link to a note that does not exist yet is fine and often useful. It marks the gap.
- When you link a person, link `people/Their Name`, and create the note if it is missing.

## Writing style

- Plain and factual. No filler, no salesmanship, no "it is worth noting that".
- Say what is known, what is uncertain, and what is not known, and mark which is which.
- **Never invent a citation, a number, a date or a result.** If you do not have it, write
  `TODO: confirm` and say so in your reply. A blank is recoverable; a fabricated fact is not.
- Keep the owner's voice. This is their notebook, not your essay.

## The loop, and where it stops

Multi-step work follows: trigger, retrieve, work, file and link, then **stop and hand back**.

You are not the approval node. Draft, file, and say what you did and what you were unsure about. Do
not delete notes, do not rewrite someone's existing note wholesale, and do not reorganise folders
unless explicitly asked. Additive by default.

## Weekly

If asked for the weekly review: empty `00_Inbox/` by filing each note properly, list any notes with
no inbound links, and surface decisions buried in `90_Daily/` that should be permanent notes.
