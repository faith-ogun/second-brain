---
title: "Tag conventions"
type: style-guide
status: current
tags: [type/style-guide, topic/vault-structure]
last-reviewed: 2026-08-25
---

# Tag conventions

Folders answer *where does this live*. Links answer *what does this mean*. Tags answer *what kind of
thing is this*, and nothing else. Keep them to three namespaces and the vault stays searchable.

## `type/`

Mirrors the `type` field in frontmatter. One per note.

`type/paper` · `type/result` · `type/method` · `type/meeting` · `type/person` · `type/grant`
· `type/concept` · `type/reference` · `type/strategy` · `type/moc` · `type/style-guide`

## `status/`

Mirrors the `status` field. One per note.

`status/current` (live and being used) · `status/active` (in progress) · `status/done`
· `status/archived` (kept for the record, not in use)

## `topic/`

The subject. As many as genuinely apply, usually one to three.

- lowercase, hyphenated: `topic/single-cell`, not `topic/SingleCell`
- **reuse before inventing.** Search the vault first. Two tags meaning the same thing is worse than
  one imperfect tag
- name the subject, not the project. `topic/chromatin` outlives `topic/aim-2`

## What not to tag

- Do not tag the folder. `10_Research/` already says that.
- Do not tag a one-off. If a tag will only ever have one note, it is a link, not a tag.
- Do not build hierarchies deeper than one level. `topic/genomics/chromatin/atac` is a folder
  wearing a costume.

## Related

- [[VAULT]] · [[MOC]] · [[callout-conventions]]
