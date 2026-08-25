---
title: "Master MOC"
type: moc
status: current
tags: [type/moc]
last-reviewed: 2026-08-25
---

# Master MOC

A Map of Content is a hand-curated index. Search finds a note you already know exists; a MOC tells
you what exists at all. Every room gets one, and **a room without a MOC will rot**, because nothing
signposts the notes nobody has opened in six months.

Keep this page short. It points at the room MOCs; the room MOCs point at the notes.

## The rooms

- **Research** — [[MOC-research]]
- **Literature** — [[MOC-literature]]
- **Grants** — [[MOC-grants]]
- **Outreach** — [[MOC-outreach]]
- **Side** — [[MOC-side]]

## How the vault works

- [[VAULT]] — the operating manual
- [[tag-conventions]] — the tag namespaces
- [[callout-conventions]] — the callout types

## Live views

With Dataview installed, these stay current on their own:

```dataview
TABLE type, status, last-reviewed
FROM "10_Research"
SORT last-reviewed DESC
LIMIT 15
```

Notes nobody has reviewed in a while:

```dataview
TABLE last-reviewed
WHERE last-reviewed AND last-reviewed < date(today) - dur(90 days)
SORT last-reviewed ASC
LIMIT 20
```
