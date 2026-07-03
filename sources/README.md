# sources/ — drop paper files here to update the site

This folder is **git-ignored** (never committed, never deployed). Put raw paper
files here when you want an AI agent to add or update a paper.

## What to put here

For each paper, make a subfolder named with the paper's **slug** and put inside:

- the **final PDF** — the exact version you want published;
- the **main manuscript `.tex`** and **every file it `\input`s** (sections,
  tables, figures' `.tex`) — unzipped, with the folder structure preserved;
- the **`.bib`** file(s) the paper uses.

```
sources/
  wealth-of-stagnation/
    decomp_v04.tex          <- main manuscript
    introduction.tex, ...   <- \input-ed sections
    Tables/ Plots/ ...       <- \input-ed tables etc.
    References.bib
    WealthofStagnation.pdf   <- final PDF
```

Slugs for existing papers are in `../papers.yaml`. Reuse a paper's slug to
**update** it; use a new slug to **add** a new paper.

## Then

Tell the agent: **"update the site from sources/"**. The agent follows
[`../AGENTS.md`](../AGENTS.md). It may ask you to confirm which `.tex` is the
final manuscript, the metadata (authors, date, keywords), and the paper's status
(working vs. forthcoming/published). When it's done it runs `check.py` and
deploys.

> Note: `.tex` sources must be the version that compiles to the **final PDF** —
> the site's text is verified against the PDF. If they don't match, the agent
> will flag it and ask you.
