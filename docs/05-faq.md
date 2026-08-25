# 5 · Questions people actually ask

**Do I need Obsidian?**
No. It is markdown files in folders, so any editor works. Obsidian gives you three things that are
genuinely hard to replace: backlinks, the graph view, and Dataview turning frontmatter into live
tables. It is free and local, so there is not much reason to avoid it.

**Do I need Claude Code specifically?**
No. Any agent that can read and write files in a directory works. Claude Code happens to read a
`CLAUDE.md` on the way in, which is why the rules live in that filename. With another tool, paste the
rules file at the start of a session instead.

**Why not a vector database?**
For a personal vault, file names plus grep plus a good link structure genuinely outperform embeddings,
because your notes have titles you chose and links you made deliberately, and both encode intent that
a similarity score does not. A vector store starts winning somewhere in the tens of thousands of
documents. At 300 notes it is infrastructure you maintain for no gain.

**How is this different from Notion, Roam, Tana?**
Mostly it is not, at the level of features. The difference is that this is plain files on your disk,
which means an agent can operate on it with ordinary file tools and no API, and it will survive any
company going under. The conventions here would port to any of those tools.

**How long before it is useful?**
Honestly, about a fortnight of real use, and the first week feels like pure overhead because you are
paying for structure you have not yet drawn on. The moment it flips is usually the first time you ask
a question and the answer is already written down.

**How many notes do I need?**
Enough that a new note has something to link to. In practice fifty is where it starts feeling alive.

**What if I fall behind?**
Nothing breaks. Notes are not a streak. Fall behind for a month, come back, run the weekly review,
and file what accumulated. The vault does not care.

**Isn't this just procrastination with extra steps?**
It can absolutely become that, which is why there is a guardrail about it in `_meta/VAULT.md`. The
test: if you have spent more time this week improving the vault than using it, stop and go do the
work. Your moat is the work, not the workflow.

**Will this work outside research?**
Yes. The rooms are the only research-specific part, and you should rename them anyway. The
transferable pieces are the three memories, the numbered rooms, the frontmatter contract, the
`## Related` block, one instrumented loop, and the weekly review. A lawyer, a founder or a journalist
would keep all of that and change every folder name.

**Can I use this for a team?**
The conventions work. The mechanics need thought: put it in git, agree the tag namespace before you
start, and be aware that `90_Daily/` is personal in a way the other rooms are not.

**What is the one thing to get right?**
The `## Related` block. If you keep only one rule, keep that one.
