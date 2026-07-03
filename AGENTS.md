# AGENTS.md — how to update this site

You are an AI agent asked to **add or update a paper** on James D. Paron's
research site. This file gets you up to speed. Read it fully, then follow the
procedure. **When something is ambiguous, ask the user — don't guess.**

## What this repo is

`jamesparon.github.io` is a machine-readable, search- and LLM-discoverable index
of James Paron's working papers, live at <https://jamesparon.github.io/>. The
goal is to **maximize discoverability** (Google, Google Scholar, AI crawlers)
while keeping **jamesparon.com** as the human landing page. Each paper's **PDF is
the definitive version**; the site links to it and funnels humans to jamesparon.com.

## Architecture — two stages

1. **`tex_to_content.py`** (runs LOCALLY; needs `sources/` + `pandoc`): converts
   each paper's final LaTeX manuscript → `content/<slug>.md` (text with math in
   TeX math mode, for LLMs) + `content/<slug>.html` (MathJax, for the page). It
   **verifies the output against the paper's PDF** (word overlap).
2. **`build.py`** (runs LOCALLY and in CI; needs neither sources nor pandoc):
   reads `papers.yaml` + `content/` + `pdfs/` → `site/`. Uses the PDF only for
   the abstract. Also emits BibTeX, OG preview images, sitemap, robots.txt, llms.txt.

Helpers: **`gen_supplement_bib.py`** fills citations missing from a paper's `.bib`
using its PDF reference list. **`check.py`** is the one-command health check.
Deploy: push to `main` → GitHub Actions builds and deploys to Pages.

## Hard rules — do not violate

- **Content comes from the FINAL manuscript `.tex`, verified against the final
  PDF** (word overlap should be ≥ ~0.8). The `.tex` must be the one that compiles
  to the posted PDF — **never** slides, notes, code, or older/other versions.
- **If the `.tex` doesn't match its PDF** (low overlap, or the tex has
  sections/citations the PDF lacks), **STOP and ask the user** which version is
  authoritative and whether they'll post an updated PDF.
- `sources/` and `*.zip` are **git-ignored and never deployed**. `content/`,
  `pdfs/`, `bib_supplements/`, `papers.yaml` **are committed**.
- Preserve legacy PDF URLs (`legacy_pdf` in papers.yaml) so old links don't break.

## Setup (once per machine)

```bash
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
brew install pandoc     # macOS; or: sudo apt-get install pandoc  (only tex_to_content.py needs it)
```

## How the user uploads files

For each paper, the user drops a folder `sources/<slug>/` containing the **final
PDF**, the **main `.tex` + all its `\input` files** (unzipped, structure
preserved), and the **`.bib`**. See `sources/README.md`.

## Procedure: add or update a paper

1. **Identify the paper + slug.** Keep existing slugs stable (see papers.yaml).
   In `sources/<slug>/`, find the main manuscript `.tex`: it has `\documentclass`
   or `\begin{document}` and its `\title` matches the PDF. **If there are several
   candidates or versions, ask the user which is final.**
2. **Place the PDF** in `pdfs/` and set `pdf` + `legacy_pdf` in papers.yaml.
3. **Edit `papers.yaml`** for the paper:
   - Metadata: `title`, `authors` (order matters), `date` (ISO) + `date_display`,
     `keywords`, `jel`, `status` (`working` or `forthcoming`), `venue` (if
     forthcoming), `pdf`, `legacy_pdf`.
   - `tex_dir`: the folder under `sources/` that **contains** the main tex
     (e.g. `sources/<slug>` or `sources/<slug>/paper`).
   - `tex_main`: the main tex filename, relative to `tex_dir`.
   - Home-page order = papers.yaml order; working papers list first, then a
     Publications section (papers with `status: forthcoming`).
4. **Convert:** `./.venv/bin/python tex_to_content.py <slug>`
   - Confirm printed `overlap` ≥ ~0.8 and `rawcite` = 0. **Low overlap ⇒ wrong or
     mismatched .tex — investigate or ask the user.**
5. **Unresolved citations** (`rawcite` > 0, i.e. `**key?**` in `content/<slug>.md`)
   mean the paper cites keys not in its `.bib` (often a shared master `.bib` that
   wasn't uploaded):
   - `./.venv/bin/python gen_supplement_bib.py <slug>` — parses the PDF reference
     list into `bib_supplements/<slug>.bib`.
   - It prints UNMATCHED keys; add those by hand to `bib_supplements/<slug>.bib`
     (they're usually well-known papers you can identify from context/the PDF).
   - Re-run `tex_to_content.py <slug>` until `rawcite` = 0.
6. **Verify:** `./.venv/bin/python check.py` → must end with **`✅ ALL CHECKS PASSED`**.
7. **Eyeball** `site/index.html` and `site/papers/<slug>/index.html`: math renders,
   citations are author-year, tables/text read cleanly.
8. **Deploy** (below).

## When to ASK the user (don't guess)

- Multiple `.tex` candidates/versions → which is the final manuscript.
- `.tex` doesn't match the PDF (low overlap, or tex has content the PDF lacks).
- Citations missing from the `.bib` and no shared/master `.bib` provided → OK to
  fill from the PDF, or do they have the bib?
- Metadata you can't infer: author order, status (working/forthcoming/published)
  and venue, keywords/JEL not in the PDF.
- Whether an upload is a NEW paper or an UPDATE to an existing slug.

## Deploy

```bash
git add papers.yaml pdfs/ content/ bib_supplements/   # sources/ is git-ignored
git commit -m "feat: add/update <paper>"
git push origin main
```

GitHub Actions ("Build and deploy site") builds + deploys. Watch it:
`gh run watch <run-id> --exit-status`.

**Transient deploy failures are common and are GitHub's fault, not the site's.**
If the **build** job succeeds but the **deploy** job fails with "Deployment
failed, try again later" (or gets stuck at "syncing_files"), just re-run it:
`gh run rerun <run-id> --failed`. It goes through on retry.

Verify live: `curl -s -o /dev/null -w "%{http_code}\n" https://jamesparon.github.io/papers/<slug>/`

## Known gotchas (handled in the pipeline; watch for new variants)

- **apacite `\citeA`/`\citeN`** → pandoc silently drops them (blank citations).
  `fix_tex` maps them to `\citet`. New citation macros → add to `fix_tex`.
- **Shared master `.bib`/macros** (e.g. `../../../shared/latex/jwstyle.tex`) may
  not be uploaded → citations/macros stay raw. Ask for the shared file, fill from
  the PDF (`gen_supplement_bib.py`), or add MathJax macros in `templates/paper.html`.
- **`tabularx`/`tabu`/`\resizebox` tables** are normalized in `fix_tex`
  (`_normalize_tables`, `_unwrap_n`). New table wrappers → extend those.
- **Figure images are not published** (only captions); the PDF is authoritative.
- **`sources/` is deleted after each update.** You can only regenerate a paper's
  content by re-uploading its sources. To fix a small committed-content artifact
  without sources, edit `content/<slug>.{md,html}` directly, then run `check.py`.

## File map

| Path | Role |
|------|------|
| `papers.yaml` | Metadata + manuscript paths — **the file you edit per paper** |
| `tex_to_content.py` | LaTeX → `content/` (local; needs pandoc + sources) |
| `gen_supplement_bib.py` | PDF reference list → `bib_supplements/<slug>.bib` |
| `build.py` | `content/` + `papers.yaml` → `site/` (local + CI) |
| `check.py` | Health check (rebuild + verify) |
| `templates/`, `static/style.css` | Jinja2 templates + styles |
| `content/` | Committed LaTeX-derived text (`.md` TeX math, `.html` MathJax) |
| `bib_supplements/` | Committed PDF-derived citation fills |
| `pdfs/` | Final PDFs (definitive; source of the abstract) |
| `sources/` | Raw uploads — git-ignored, never deployed |
| `.github/workflows/build.yml` | CI build + deploy |
