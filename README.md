# jamesparon.github.io

Source for a search- and LLM-discoverable index of James D. Paron's working
papers. A small static-site generator (`build.py`) turns `papers.yaml` + the
final PDFs into per-paper HTML pages with Google Scholar `citation_*` tags,
JSON-LD structured data, full machine-readable text, a sitemap, `robots.txt`,
and `llms.txt`. Humans are pointed to [jamesparon.com](https://jamesparon.com);
each PDF remains the definitive version of its paper.

## Add or update a paper

1. Drop the **final PDF** into `pdfs/`.
2. Add a block to `papers.yaml` (title, authors, date, keywords, JEL, `pdf`,
   and `legacy_pdf` if it had an old root URL).
3. Commit and push to `main` — GitHub Actions rebuilds and deploys.

> **Content rule:** every field and all on-page text comes from the **final
> PDF only**. Never source content from slides, code, notes, or draft/older
> manuscript versions. The `sources/` folder (raw project files) is
> git-ignored and is **not** a content source.

## Build locally

```bash
python -m venv .venv && ./.venv/bin/pip install -r requirements.txt
./.venv/bin/python build.py   # outputs ./site
```

## Layout

| Path | Purpose |
|------|---------|
| `papers.yaml` | Paper metadata (the file you edit) |
| `build.py` | Generator (extracts text from PDFs, renders `site/`) |
| `templates/` | Jinja2 HTML/markdown templates |
| `static/style.css` | Styles |
| `pdfs/` | Final paper PDFs (sole content source) |
| `.github/workflows/build.yml` | CI build + deploy to GitHub Pages |
| `site/` | Generated output (git-ignored; built in CI) |

Deployment source: **Settings → Pages → Build and deployment → GitHub Actions.**
