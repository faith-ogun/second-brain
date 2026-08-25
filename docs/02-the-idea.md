# 2 · Why a folder of text files works

## The problem

A language model knows a great deal about the world and nothing about you. Every session starts
cold. You paste in context, get good work, close the window, and tomorrow you do it again. That is
not a memory, it is a treadmill.

## The three memories

An agent that is useful over weeks rather than minutes needs three different kinds of memory, and
they are genuinely different things:

**Procedural memory** is *how to behave*. How you like notes written, where things go, what never to
do. It is stable, small, and read at the start of every session. It belongs in one file the agent
reads automatically.

**Semantic memory** is *durable facts*. What the project is, what a method does, what a paper found,
who a person is. One note per thing, written once, updated when it changes. It is retrieved on
demand, not held in your head.

**Episodic memory** is *what happened and when*. You read this on Tuesday, you decided that in
March, the experiment failed in a specific way in June. It is append-only and timestamped, and it is
the memory people most reliably fail to keep.

Most people building "AI memory" reach for a vector database at this point. You usually do not need
one, because:

- **procedural memory** is a file the agent reads on the way in
- **semantic memory** is a folder of notes with real titles, which an agent can search by name
- **episodic memory** is a folder of dated files, which is already a time series

A filesystem does all three. It is inspectable, greppable, diffable, portable, and it will still
open in twenty years.

## The harness

Sean Chen's metaphor, and it is the right one: the model is a very powerful horse. Without a harness
it runs somewhere random, and the harness is not a limit on the power, it is what makes the power
usable.

The harness here is five things: the rules file, the agent's file tools, the loop, the semantic
notes, and the episodic record. Four of them are folders. One is a markdown file.

## The stop condition

An agent doing multi-step work needs an explicit condition that says when to stop and hand back to a
human. This is the part people skip, and it is the part that matters most in research, where a
confident wrong answer is worse than no answer.

In this vault the stop is always the same: the agent drafts and files, then stops, and you approve.
Never delegate the approval node. Everything else here is convention you can change; that one is
structural.

## Why the links matter more than the folders

A folder tells you where a note sits. A link tells you what it means.

The single highest-value habit in this whole system is the `## Related` block at the bottom of every
note. A paper filed perfectly and linked to nothing is a paper you will never see again. The same
paper linked to the result it supports and the claim it threatens will surface exactly when you need
it, because you will arrive at it from the thing you were already thinking about.

Folders keep things tidy. Links do the thinking.

Next: [the loop](03-the-loop.md).
