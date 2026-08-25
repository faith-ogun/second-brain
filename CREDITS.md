# Credits

## The framing: Sean Chen

The memory model and the harness idea in this repo are not mine. They come from **Sean Chen**, an
ex-Google engineer who explains AI agent architecture better than anyone I have found, and whose
20-minute walkthrough of agent harnesses, loop engineering and evals is the reason this vault has
the shape it does.

What I took from him, directly:

- **The harness metaphor.** A large language model is a very powerful horse. Without a harness it
  runs somewhere random. The harness is not a limit on the model, it is what makes the power usable.
- **The three memories.** Procedural (how to behave), semantic (durable facts), episodic (a
  timestamped record of what happened). Naming them separately is what lets you build for each one.
- **The loop, and the end-loop guardrail.** An agent doing multi-step work needs an explicit
  condition that says when to stop and hand back. Without it you get either an infinite loop or a
  confident wrong answer.
- **Evals as a feedback loop**, not a one-off benchmark. Trace the run, judge it, diagnose, fix, ship.

His material:

- YouTube, on harnesses and loop engineering: <https://www.youtube.com/watch?v=GrNbuWWJYiI>
- Related talks on agent memory and graph engineering are on the same channel
- <https://seanchen.io>

> Verification note: the transcript I worked from was shared without full attribution, and I have
> matched it to Sean Chen. If you are Sean and I have credited you incorrectly, or you would like
> this worded differently, open an issue and I will fix it immediately.

## What is mine

Everything downstream of the idea:

- The decision to make **a filesystem be all three memories at once**, rather than standing up a
  database. Obsidian's vault plus an agent's file tools is enough.
- The **room scheme**, the numbering with gaps, and which rooms earn their place.
- The **frontmatter contract** (`title`, `type`, `status`, `tags`, `last-reviewed`) and the tag
  taxonomy that makes filing decidable by an agent rather than a judgement call.
- The **`## Related` block** as a required part of every note, which is what turns a folder of files
  into something with a shape.
- The **Maps of Content** pattern in `_meta/`, and the rule that a room without a MOC will rot.
- **The paper-a-day loop** as the single first thing to instrument, and the argument for doing only
  one.
- The **weekly review**, the two guardrails, and the conventions that survived a year of daily use
  on a real PhD. Most of the ones that did not survive are not in here, which is most of the value.

## Also standing on

- **Obsidian**, for a local-first markdown app that never held my notes hostage. <https://obsidian.md>
- **Zettelkasten**, and Niklas Luhmann's argument that the links are the thinking, which is a much
  older idea than any of this.
- **Andrej Karpathy's Software 3.0**, for the framing that the model is the substrate rather than a
  feature bolted onto an app.
- **Anthropic's Claude Code and Claude Science**, for making the agent side of this work in practice,
  in particular the convention that an agent reads a `CLAUDE.md` on the way into a directory.

## Licence

Documentation and templates: MIT. Take it, fork it, rename the rooms, throw away the parts that do
not fit your work. Attribution appreciated but not required.
