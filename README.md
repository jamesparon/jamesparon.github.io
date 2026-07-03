# jamesparon.github.io

Source for a search- and LLM-discoverable index of James D. Paron's working
papers. Per-paper HTML pages carry Google Scholar `citation_*` tags, JSON-LD
structured data, and the **full paper text with mathematics in TeX/MathJax**,
plus a sitemap, `robots.txt`, and `llms.txt`. Humans are pointed to
[jamesparon.com](https://jamesparon.com); each PDF is the definitive version.

## How content is produced

Two stages, so the heavy LaTeX conversion runs locally while GitHub Pages
rebuilds are fast and dependency-light:

1. **`tex_to_content.py` (local)** — converts each paper's final LaTeX
   manuscript (in the git-ignored `sources/`) to `content/<slug>.md` (TeX math)
   and `content/<slug>.html` (MathJax) using pandoc. Every conversion is
   **verified against the paper's final PDF** (word overlap) before it's used,
   guarding against outdated/wrong `.tex`. The `content/` files are committed.
2. **`build.py` (local + CI)** — reads `papers.yaml` + `content/` and renders
   `site/`. Uses the PDF only for the clean abstract. No pandoc/sources needed,
   so it runs in GitHub Actions.

> **Content rule:** the manuscript `.tex` used for each paper must be the one
> that compiles to the final PDF (verified by `tex_to_content.py`). Never use
> slides, code, notes, or older/other manuscript versions. `sources/` and
> `*.zip` are git-ignored and never deployed.

## Add or update a paper

1. Drop the final PDF in `pdfs/` and the manuscript project in `sources/`.
2. Add a block to `papers.yaml` (metadata + `tex_dir`/`tex_main`; `legacy_pdf`
   if it had an old root URL).
3. `./.venv/bin/python tex_to_content.py <slug>` — check overlap is high (~0.8+).
4. Commit `content/` + the PDF + `papers.yaml`; push to `main`. CI deploys.

## Build locally

```bash
python -m venv .venv && ./.venv/bin/pip install -r requirements.txt
brew install pandoc                      # for tex_to_content.py only
./.venv/bin/python tex_to_content.py     # sources/ -> content/  (local)
./.venv/bin/python build.py              # content/ -> site/
```

## Layout

| Path | Purpose |
|------|---------|
| `papers.yaml` | Paper metadata + manuscript paths (the file you edit) |
| `tex_to_content.py` | LaTeX → `content/` converter (local; needs pandoc + sources) |
| `build.py` | `content/` + `papers.yaml` → `site/` (local + CI) |
| `content/` | Committed LaTeX-derived text (`.md` TeX math, `.html` MathJax) |
| `templates/`, `static/style.css` | Jinja2 templates and styles |
| `pdfs/` | Final paper PDFs (definitive version; source of the abstract) |
| `sources/` | Raw LaTeX projects — git-ignored, never deployed |
| `.github/workflows/build.yml` | CI build + deploy to GitHub Pages |
| `site/` | Generated output (git-ignored; built in CI) |

Deployment source: **Settings → Pages → Build and deployment → GitHub Actions.**
