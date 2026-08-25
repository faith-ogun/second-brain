# 1 · Setup, in twenty minutes

No account, no server, no subscription. Obsidian is free and your notes are files on your disk.

## Step 1 · Get the template (2 min)

```bash
git clone https://github.com/faith-ogun/second-brain.git
cp -R second-brain/vault-template ~/MyBrain
```

Call it whatever you like. `~/MyBrain` is used throughout these docs.

## Step 2 · Open it in Obsidian (3 min)

Download Obsidian from <https://obsidian.md>, choose **Open folder as vault**, and point it at
`~/MyBrain`. That is the whole install. Nothing uploads anywhere.

Then enable four plugins under Settings, Community plugins:

| Plugin | Why |
|---|---|
| **Dataview** | turns your frontmatter into live tables. This is what makes the MOCs useful |
| **Templater** | new notes fill in their own frontmatter and date |
| **Tag Wrangler** | rename and merge tags safely, which you will need by month two |
| **Advanced Tables** | markdown tables stop being painful |

Under Settings, Core plugins, make sure Graph view, Daily notes and Templates are on. Point Daily
notes at `90_Daily/` and Templates at `99_Templates/`.

## Step 3 · Make it yours (10 min)

Three files, in this order. Nothing else matters yet.

1. **`CLAUDE.md`** at the vault root. Fill in the three bracketed lines at the top: your name, the
   work, and what you will mostly ask for. Then rename the rooms in the table if my names do not fit
   your field.
2. **`_meta/VAULT.md`**. Answer the "what this vault is for" paragraph. Write it properly. Every
   later decision hangs off it, and a vague answer here produces a junk drawer.
3. **`_meta/MOC.md`**. Delete the room MOCs you will not use.

If you rename a room, rename it in `CLAUDE.md` too. Those two must agree or the agent will file
things where you cannot find them.

## Step 4 · Point an agent at it (5 min)

```bash
cd ~/MyBrain
claude
```

Claude Code reads `CLAUDE.md` on the way in, so it starts knowing your rules. Then test it with
something real, not a toy:

> Read `_meta/VAULT.md`, then create a literature note for this paper: [paste an abstract or a DOI].
> Follow the filing rules in `CLAUDE.md`.

Check the result against the rules yourself. Frontmatter complete? Real title? `## Related` block
with actual links? If any of that is missing, the fix is almost always a sentence added to
`CLAUDE.md`, not a longer prompt. **The rules file is the thing you tune.**

## Step 5 · Seed it (ongoing)

An empty vault is not useful, and building conventions with nothing to file is theory. Put in
whatever already exists: the papers you have read this year, the people you work with, the current
state of the project. It does not need to be complete, it needs to be enough that the next note has
something to link to.

## What not to do in week one

- Do not build automations. One loop, later, once you know what annoys you.
- Do not import ten years of notes. You will import ten years of mess.
- Do not add more plugins. The four above cover it.
- Do not spend a day on the folder scheme. The numbering has gaps for a reason.

Next: [the idea](02-the-idea.md), or skip straight to [the filing rules](04-filing-rules.md).
