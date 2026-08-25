# 3 · Instrumenting your first loop

## Instrument one thing

The temptation is to automate everything at once. Do not. Pick the single task you do most often,
instrument it end to end, and leave it alone for a month. You learn more from one loop running for
thirty days than from five loops running for three.

Pick the loop that is **frequent, low-stakes, and currently annoying**. Frequent, so you get
feedback fast. Low-stakes, so a bad output costs you nothing. Annoying, so you will actually keep
using it.

## The shape of a loop

Every loop here has the same five steps:

1. **Trigger.** Something arrives. A paper, a meeting, a result, a deadline.
2. **Retrieve.** The agent reads the rules and whatever prior notes are relevant.
3. **Work.** It does the actual job.
4. **File and link.** The output lands in the right room with a real title, complete frontmatter,
   and a `## Related` block. Today's daily note records it.
5. **Stop.** You read it and approve, or send it back.

Steps 1 to 3 save you time once. **Step 4 is the only one that compounds**, because it is the step
that makes the vault worth more tomorrow than it was today. If you are going to cut a corner, do not
cut that one.

## Worked example: the paper-a-day loop

The one I run.

**Trigger.** A paper turns up, from a feed or from a colleague.

**Prompt.**

> Digest this paper into a note in `20_Literature/` using `99_Templates/paper.md`. Follow the filing
> rules in `CLAUDE.md`. Then link it to whichever part of my project it touches, and to any claim it
> supports or threatens. Add a line to today's daily note. Tell me what you were unsure about.

**What lands.** A literature note with the frontmatter filled in, a "what I take from it" section
that is mine to correct, and links out to the project. A line in `90_Daily/`.

**What I do.** Read it, fix the interpretation, approve. Usually two minutes. If I disagree with
how it linked something, that is the interesting part, and it usually means my project notes are
vague rather than the agent being wrong.

## Tuning

When the output is wrong, resist writing a longer prompt. Add a sentence to `CLAUDE.md` instead.

The prompt is for this task. The rules file is for every task, forever. A rule you write once fixes
the problem permanently and for every future session; a prompt you improve fixes it once. Over a few
months `CLAUDE.md` becomes the most valuable file in the vault, and it is entirely made of mistakes
you decided not to repeat.

## Loops worth adding later

One at a time, once the first is boring:

- **The update loop.** Read the last N daily notes, draft the supervisor or manager update.
- **The section loop.** Pull every note tagged with a topic, draft a grant or report section, with
  every claim linked to its source note.
- **The return loop.** After time away, summarise what the vault says happened while you were gone.
- **The review loop.** The weekly review itself, run as a prompt.

## The weekly review

Fifteen minutes on Friday. Three questions: did it help me learn, did it survive contact with a real
reader, what annoyed me?

Then the mechanical part: `00_Inbox/` to zero, open the graph view and either link or delete the
orphans, promote real decisions out of the daily notes into permanent notes.

Skip this and the vault becomes a junk drawer within about two months. No tooling prevents that.
Only the fifteen minutes does.

Next: [the filing rules](04-filing-rules.md).
