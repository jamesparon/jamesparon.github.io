---
title: "Make jamesparon.github.io a search- and LLM-discoverable paper site"
type: feat
status: completed
date: 2026-07-03
---

# ✨ Make `jamesparon.github.io` a search- and LLM-discoverable paper site

## Overview

`jamesparon.github.io` currently hosts ~8 academic working-paper PDFs (plus `ParonCV.pdf`) as **raw files with no HTML around them**. GitHub Pages renders only a 2-line `README.md` as the landing page. Because the papers live only as PDFs — with even their embedded Title/Author metadata fields blank — search engines index them weakly, **Google Scholar cannot index them at all** (it needs an HTML abstract page with `citation_*` tags), and web-crawling LLMs (ClaudeBot, GPTBot, PerplexityBot, Google-Extended) cannot reliably read them, since they crawl HTML/text and do not render JS or reliably parse PDFs.

This plan converts the repo into a **metadata-driven static site** that acts as the *machine-readable layer* for James Paron's research: one HTML landing page per paper carrying full readable text + Google Scholar meta tags + JSON-LD structured data, a root index, and the supporting discoverability files (`sitemap.xml`, `robots.txt`, `llms.txt`, `llms-full.txt`). Humans are still funneled to the main site **jamesparon.com** and to the PDFs. A single `build.py` runs in **GitHub Actions** on every push, so adding a future paper is *commit a PDF/source + one YAML entry*.

**Decisions locked in (from planning dialogue):**
- **Content depth:** full paper text on-page, machine-readable. *(user decision)*
- **Single source of truth = the FINAL PDF (hard constraint).** All website content is derived **only** from the final published PDFs already in the repo. **No** content is ever taken from supporting materials — code, slides, notes, data, literature, response letters, or older/alternative manuscript versions — because those may be outdated or wrong. The LaTeX project folders the author provided are **NOT used as a content source.** *(user decision — supersedes the earlier "prefer LaTeX source" plan)*
- **Build/deploy:** **GitHub Actions CI** (no local toolchain to add a paper). *(user decision)*
- **Crawlers:** **allow everything** — AI answer/search bots *and* AI-training bots — for maximum discoverability. *(user decision)*
- **Source-folder safety (hard constraint):** the provided project zips/folders under `sources/` are treated as **read-only, git-ignored, never-deployed** inputs. They are retained *only* as an optional, manually-gated math-rendering reference (see Content Ingestion); the generator never edits them and never publishes anything from them. *(user decision)*

## Problem Statement

The goal is that (1) the papers are easily found by search engines and Google Scholar, (2) a web-browsing LLM can answer a person's detailed questions about a paper's **content and results** by reading machine-readable text, while (3) human searchers are still routed to `jamesparon.com` and read the PDFs. The current setup fails all three because:

- **No per-paper HTML pages.** Google Scholar's inclusion guidelines require each article/abstract in its own HTML (or PDF) file with `citation_*` meta tags in `<head>`; a bare PDF "is processed as if it had no meta tags at all." (see origin research: Google Scholar inclusion guidelines)
- **No machine-readable text.** All content is locked in PDFs. A controlled 2026 GEO experiment found AI answer engines cite **HTML pages, not PDFs** and never cited alternate-format URLs — the on-page HTML text is what LLMs actually ingest.
- **Blank PDF metadata.** `pdfinfo` shows empty Title/Author on every PDF, so even PDF-level signals are missing.
- **No discoverability scaffolding.** No `sitemap.xml`, no `robots.txt`, no `llms.txt`, no structured data, no Open Graph tags. Nothing tells crawlers what exists or invites them in.
- **README-only landing page** gives neither humans nor machines an index of the work.

## Proposed Solution

A **`build.py` static generator** (run in GitHub Actions) reads a single hand-edited `papers.yaml` and, per paper, extracts the content **from the final PDF only** and renders:

1. **Root `index.html`** — lists every paper (title, authors, date, abstract) with `Person` JSON-LD identifying James Paron and linking (`sameAs`) to ORCID / Google Scholar / GSB / `jamesparon.com`.
2. **`/papers/<slug>/index.html`** per paper — full readable text as real HTML + `citation_*` meta tags + `ScholarlyArticle` JSON-LD + Open Graph/Twitter tags + a **self-referencing canonical** + a prominent human CTA to `jamesparon.com` and the PDF.
3. **`/papers/<slug>/paper.pdf`** — the PDF **copied into the same subdirectory** as its landing page (Google Scholar requires `citation_pdf_url` to sit in the same subdir).
4. **`/papers/<slug>/index.md`** — a clean plain-text/markdown mirror for direct LLM/tool fetching.
5. **Root discoverability files:** `sitemap.xml` (HTML + PDF + `.md` URLs), `robots.txt` (permissive, AI bots named explicitly), `llms.txt` (curated index), `llms-full.txt` (concatenated full text of all papers).
6. **Backward-compatible redirects** so existing links like `jamesparon.github.io/CLP.pdf` (already referenced from `jamesparon.com`) keep working.

**Why github.io stays indexed while humans go to jamesparon.com:** the two sites are kept as **differentiated content tiers** — github.io is the *deep machine-readable record* (full text + all metadata), jamesparon.com is the *human presentation* (bio, teasers, "read the paper"). Different depth/purpose ⇒ not duplicate content, so both can rank. Funneling is done with **links + author JSON-LD `url`/`mainEntityOfPage` → jamesparon.com**, NOT with a cross-domain canonical (which would de-index github.io). Each github.io page is **self-canonical**.

## Technical Approach

### Architecture: chosen build method

**Approach: standalone `build.py` + GitHub Actions** (evaluated against native Jekyll and a hybrid — see Alternatives). Decisive reason: the requirement for *full machine-readable paper text on every page* means text must be pre-extracted by a script regardless; once that's true, pure Jekyll's "no toolchain" advantage evaporates, and Jekyll 3.10 (GitHub Pages' pinned version) cannot generate N pages from one data file without a non-whitelisted plugin. Publishing via Actions also escapes the Jekyll 3.x/plugin-whitelist pin entirely.

### Repository structure

```
jamesparon.github.io/
├── .github/workflows/build.yml     # runs build.py, deploys ./site via actions/deploy-pages
├── build.py                        # reads papers.yaml, ingests content, renders templates
├── requirements.txt                # jinja2, pyyaml, pymupdf (PDF fallback); pandoc/latexml via apt in CI
├── papers.yaml                     # THE file you edit per new paper
├── templates/
│   ├── base.html                   # <head>: citation_* + JSON-LD + OG/Twitter + canonical
│   ├── index.html                  # landing page (paper list + Person JSON-LD)
│   ├── paper.html                  # per-paper: full text + metadata + PDF/CTA links
│   └── paper.md.j2                 # markdown mirror template
├── static/
│   └── style.css                   # minimal, readable, mobile-friendly
├── pdfs/                            # the 8 paper PDFs move here (SOLE content source); ParonCV.pdf stays out of papers.yaml
│   ├── WealthofStagnation.pdf ... HAAP.pdf
│   └── ParonCV.pdf
├── sources/                        # GIT-IGNORED, NEVER DEPLOYED, READ-ONLY: author's raw project zips.
│   └── <slug>.zip                  #   NOT a content source — optional math-render reference only (see Ingestion)
├── .gitignore                      # ignores site/, sources/, *.zip, __MACOSX, .DS_Store
├── docs/plans/                     # this plan
├── .nojekyll                       # disable Jekyll (we publish our own HTML)
└── site/                           # GENERATED (emitted in CI; git-ignored locally)
    ├── index.html
    ├── papers/<slug>/index.html
    ├── papers/<slug>/paper.pdf
    ├── papers/<slug>/index.md
    ├── sitemap.xml  robots.txt  llms.txt  llms-full.txt
    └── static/style.css
```

### `papers.yaml` — the only file edited per paper

```yaml
# Author-level metadata used across the site
site:
  author_name: "James D. Paron"
  affiliation: "Stanford University Graduate School of Business"
  homepage: "https://jamesparon.com"
  orcid: "https://orcid.org/0009-0001-5768-6424"
  scholar: "https://scholar.google.com/citations?user=OhpTkHEAAAAJ"
  gsb: "https://www.gsb.stanford.edu/faculty-research/faculty/james-d-paron"

papers:
  - slug: wealth-of-stagnation
    title: "The Wealth of Stagnation: Falling Growth, Rising Valuations"
    authors: ["James D. Paron"]
    date: 2026-01-19
    institution: "Stanford University"          # -> citation_technical_report_institution
    keywords: ["innovation", "growth", "asset prices", "valuations", "R&D", "concentration"]
    jel: []                                       # optional
    pdf: pdfs/WealthofStagnation.pdf              # SOLE content source for this paper
    ssrn: ""                                       # optional -> citation ids + JSON-LD sameAs
    doi: ""                                        # optional (fill once published)
    legacy_pdf: WealthofStagnation.pdf            # old root URL to redirect from
```

Paper inventory to seed `papers.yaml` (extracted from the current PDFs — titles/authors/dates verified against page 1):

| slug | title | authors | date |
|---|---|---|---|
| wealth-of-stagnation | The Wealth of Stagnation: Falling Growth, Rising Valuations | Paron | 2026-01-19 |
| depopulation | Making Room on an Empty Planet: The Spatial Consequences of Depopulation | de Silva, Paron | 2026-06-25 |
| treasury-ai | U.S. Treasury Investors Are Long in AI | Kung, Lustig, Paron | 2026-06 |
| who-gains-interest-rates | Who Gains When Interest Rates Fall? | Catherine, Miller, Paron, Sarin | 2026-03-20 |
| racial-wealth-gap | A Dynamic Model of the Racial Wealth Gap | Catherine, Lu, Paron | 2025-12-16 |
| sovereign-default | Sovereign Default and the Decline in Interest Rates | Miller, Paron, Wachter | 2025-11-21 |
| representativeness | Associative Learning and Representativeness | Kahana, Paron, Wachter | 2025-12-06 |
| heterogeneous-agent-asset-pricing | Heterogeneous-Agent Asset Pricing: Timing and Pricing Idiosyncratic Risks | Paron | 2022-12-15 |

*(Current filenames CLP/CMPS/HAAP/MPW map to racial-wealth-gap / who-gains-interest-rates / heterogeneous-agent-asset-pricing / sovereign-default respectively. `ParonCV.pdf` is intentionally excluded from `papers.yaml` but may get its own simple page + redirect.)*

### Content ingestion (`build.py`) — final PDF is the sole content source

**Governing rule:** every character of website content for a paper comes from that paper's **final PDF** in `pdfs/`. Nothing is ever sourced from the `sources/` project folders — no code, slides, notes, data, literature, response letters, or older/alternative manuscript versions — because those may be outdated or contradict the published paper. This is a hard correctness constraint, not a preference.

For each paper, `build.py` reads **only** the `pdf:` file and writes exclusively under `site/`:

1. **Extract text from the final PDF** using **PyMuPDF** (`page.get_text("blocks")` sorted for column order) — top-rated for two-column academic layout and speed. (License note: PyMuPDF is AGPL-3.0 — fine for an open personal site; swap to pdfplumber/`pdftotext -layout` if a permissive license is preferred.)
2. Parse **page 1** for the abstract, keywords, and JEL codes (verified reliably extractable on all current PDFs).
3. Emit the full extracted text into the HTML body + the `index.md` mirror + `llms-full.txt`, labeled as a machine-readable transcript of the PDF, with a "read the definitive PDF" CTA. The **PDF remains authoritative**; the transcript is explicitly a derived convenience for machines.

**On the provided `sources/` zips:** they are retained *only* as an optional, human-in-the-loop reference if we later want to hand-improve math/equation rendering for a specific paper. Using them would require (a) identifying the exact manuscript `.tex` that compiles to the *final* PDF, (b) verifying byte-for-byte that its rendered output matches the final PDF, and (c) still excluding every non-manuscript file. Given the folders contain multiple manuscript versions and heavy supporting material, this is **deferred and off by default** — the shipped pipeline is PDF-only. The zips are git-ignored and never deployed. *(Note: `depopulation.zip` is ~3.3 GB and several others are 100 MB+; they must never be committed.)*

### Per-paper `<head>` — the discoverability payload

Google Scholar `citation_*` tags (working-paper scheme; switch to `citation_journal_title`/`volume`/etc. once published):

```html
<link rel="canonical" href="https://jamesparon.github.io/papers/wealth-of-stagnation/">
<meta name="citation_title" content="The Wealth of Stagnation: Falling Growth, Rising Valuations">
<meta name="citation_author" content="Paron, James D.">
<meta name="citation_publication_date" content="2026/01/19">
<meta name="citation_technical_report_institution" content="Stanford University">
<meta name="citation_pdf_url" content="https://jamesparon.github.io/papers/wealth-of-stagnation/paper.pdf">
<meta name="citation_abstract_html_url" content="https://jamesparon.github.io/papers/wealth-of-stagnation/">
<meta name="citation_keywords" content="innovation; growth; asset prices; valuations">
<meta name="citation_language" content="en">
<link rel="alternate" type="text/markdown" href="index.md">
```

`ScholarlyArticle` + `Person` JSON-LD (abstract as text, authors as linked `Person` with affiliation + `sameAs` to ORCID/Scholar/GSB, `encoding` → the PDF, author `url` → jamesparon.com). Open Graph/Twitter tags (`og:type=article`, `article:author` → jamesparon.com, `summary_large_image` with an auto-generated title card). *(Full example blocks captured in the origin research and to be templated in `templates/base.html`.)*

### Root discoverability files

- **`robots.txt`** — `User-agent: * / Allow: /`, then explicit `Allow` blocks naming GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-Web, anthropic-ai, PerplexityBot, Perplexity-User, Google-Extended, Applebot-Extended, Bytespider, CCBot (per "allow everything" decision), ending with `Sitemap: https://jamesparon.github.io/sitemap.xml`.
- **`sitemap.xml`** — every landing page, every `paper.pdf`, every `index.md`, plus root, with `lastmod`.
- **`llms.txt`** — H1 + blockquote summary + `## Papers` / `## Author` / `## PDFs` link lists (points to each `index.md`). Publish as cheap insurance (adoption is low but rising; the real work is the HTML).
- **`llms-full.txt`** — concatenation of every paper's full extracted text, for single-fetch LLM ingestion.

### Backward-compatible URLs

Existing links (`jamesparon.github.io/CLP.pdf`, etc.) are referenced from `jamesparon.com` and elsewhere and **must not break**. `build.py` emits, for each `legacy_pdf`, a small HTML redirect (`<meta http-equiv="refresh">` + `<link rel="canonical">`) or copies the PDF to its old root path, redirecting to the new `/papers/<slug>/`. Verify each old URL still resolves post-deploy.

### GitHub Actions workflow (`.github/workflows/build.yml`)

On push to `main`: checkout → `apt-get install` LaTeXML/pandoc (for TeX papers) → `pip install -r requirements.txt` → `python build.py` (emits `./site`) → `actions/upload-pages-artifact` → `actions/deploy-pages`. Publishing via Actions means we're **not** limited to Jekyll 3.x or whitelisted plugins. Fallback path documented: run `build.py` locally, commit `site/` + `.nojekyll` if the author ever prefers no CI.

## Implementation Phases

### Phase 1: Foundation & scaffolding
- Create `docs/plans/` (done — this file), `templates/`, `static/`, `pdfs/`, add `.nojekyll`, `.gitignore` (`site/`, `sources/`, `*.zip`, `__MACOSX`, `.DS_Store`).
- **Immediately git-ignore `sources/` and the `*.zip` files** so the multi-GB project folders can never be committed or deployed.
- Move the 8 paper PDFs into `pdfs/`; keep `ParonCV.pdf`.
- Author `papers.yaml` seeded from the inventory table above (fill real ORCID/Scholar IDs — flagged TODO).
- **Deliverable:** metadata + assets in place. **Success:** `papers.yaml` validates; all PDFs present; `git status` shows no zip/sources tracked.

### Phase 2: Generator core (PDF-only content)
- `build.py`: load YAML, extract text from the **final PDFs only** (PyMuPDF), Jinja2 templates (`base/index/paper`), emit `site/` with per-paper HTML (full `citation_*` + JSON-LD + OG), root `index.html`, `index.md` mirrors, `sitemap.xml`, `robots.txt`, `llms.txt`, `llms-full.txt`, PDFs copied into `/papers/<slug>/paper.pdf`.
- Legacy redirects for old root PDF URLs.
- **Deliverable:** full site generated from the final PDFs. **Success:** local `python build.py` produces a valid `site/`; HTML validates; `citation_pdf_url` sits in same subdir as its page; **no content traces back to any `sources/` file** (spot-check that on-page text matches the PDF, not slides/notes).

### Phase 3: Content QA pass
- Review each generated page against its final PDF: abstract/keywords/JEL correct, extracted body readable, no garbled sections that misrepresent results, authors/date/title exact.
- Flag any paper whose PDF extraction is poor enough to mislead; for those, trim the on-page transcript to the cleanly-extractable sections (abstract + intro + results) rather than risk publishing garbled text. (Optional, deferred, per-paper: hand-improve math using the manuscript `.tex` **only** after verifying it matches the final PDF.)
- **Deliverable:** vetted content. **Success:** every page faithfully reflects its final PDF and only its final PDF.

### Phase 4: CI/CD & deploy
- `.github/workflows/build.yml`; enable GitHub Pages "GitHub Actions" source.
- **Deliverable:** push-to-deploy. **Success:** a push rebuilds and publishes; live URLs resolve.

### Phase 5: Verification & registration
- Google Search Console: verify property, submit `sitemap.xml`. Validate JSON-LD (Rich Results Test) and `citation_*` tags (view-source on live pages). Confirm legacy PDF URLs still work. Add papers to the author's Google Scholar profile to speed clustering. Spot-check that ClaudeBot/GPTBot-style fetches see full text (curl the pages).
- **Deliverable:** indexed & registered. **Success criteria in Acceptance Criteria below.**

## Alternative Approaches Considered

- **Native Jekyll, no build (rejected):** GitHub's blessed path, but Liquid cannot read PDFs, so full text would be hand-pasted per paper; Jekyll 3.10 can't fan out N pages from one data file without a non-whitelisted plugin. The full-text requirement kills its only advantage.
- **Hybrid Jekyll + extraction script (rejected):** inherits the Python toolchain cost of the script *and* Jekyll's 3.10/Liquid constraints — two systems, no net benefit for a non-web-developer.
- **Leave as PDFs, just add metadata + robots/sitemap (rejected):** doesn't give LLMs readable text and Scholar still needs HTML abstract pages; fails goals (1) and (2).
- **Cross-domain canonical github.io → jamesparon.com (rejected):** would consolidate indexing onto jamesparon.com and **de-index** the github.io machine layer — the opposite of the goal. Use self-canonical + differentiated tiers + link-funneling instead.

## System-Wide Impact

- **Interaction graph:** `git push` → GitHub Actions → `build.py` reads `papers.yaml` (+ `pdfs/`, optional `sources/`) → renders `site/` → `deploy-pages` publishes. Downstream: Google/Scholar crawl HTML pages → follow `citation_pdf_url` to PDFs; AI crawlers read HTML + `index.md` + `llms-full.txt`; humans hit landing pages → CTA → jamesparon.com/PDF.
- **Error propagation:** a bad TeX conversion or extraction for one paper must not fail the whole build — per-paper try/except that falls back (TeX→PDF extraction→abstract-only) and logs a warning, so one paper never blocks deploy.
- **State/lifecycle risks:** `site/` is fully regenerated each run (no partial state). The one persistent hazard is **broken legacy URLs** — mitigated by explicit redirects and a post-deploy link check. Source-folder mutation is prevented by the read-only rule + git-ignored `sources/`.
- **API-surface parity / duplicate content:** github.io and jamesparon.com must stay *differentiated tiers*; if jamesparon.com later mirrors identical abstracts, revisit canonical strategy.
- **Integration scenarios worth manual test:** (a) Scholar sees a new paper's `citation_*` and links the PDF; (b) an LLM asked "what does Paron's stagnation paper find?" retrieves the on-page text; (c) an old `CLP.pdf` link still resolves; (d) a link preview (Slack/X) renders the OG card; (e) adding a paper = one YAML entry + PDF triggers a correct rebuild.

## Acceptance Criteria

### Functional
- [ ] Root `index.html` lists all 8 papers with title, authors, date, abstract, and a link to jamesparon.com.
- [ ] Each paper has `/papers/<slug>/index.html` with full readable text, `citation_*` tags, `ScholarlyArticle` JSON-LD, OG/Twitter tags, self-canonical, and a PDF + jamesparon.com CTA.
- [ ] `citation_pdf_url` resolves to `/papers/<slug>/paper.pdf` (same subdirectory).
- [ ] `/papers/<slug>/index.md` and root `llms.txt` + `llms-full.txt` exist and contain real text.
- [ ] `sitemap.xml` lists all HTML pages, PDFs, and `.md` mirrors; `robots.txt` allows all named crawlers and references the sitemap.
- [ ] Every pre-existing PDF URL (e.g. `/CLP.pdf`) still resolves (redirect or copy).
- [ ] **All published content derives solely from the final PDFs**; nothing from `sources/` (code/slides/notes/data/old versions) appears anywhere on the site.
- [ ] `sources/` and `*.zip` are git-ignored and absent from the deployed `site/` and from git history.
- [ ] Adding a paper requires only: add the final PDF + one `papers.yaml` entry.

### Non-functional / quality gates
- [ ] JSON-LD passes Google's Rich Results Test; `citation_*` tags present in initial HTML (no JS required).
- [ ] Pages are mobile-readable and lightweight (no heavy JS beyond MathJax where needed).
- [ ] Per-paper build failure degrades gracefully and never blocks deploy.
- [ ] `sitemap.xml` submitted and accepted in Google Search Console.

## Success Metrics

- Papers appear in Google Scholar under the author's profile within a few index cycles.
- github.io paper pages appear in Google web results for paper-title queries.
- An LLM (e.g. Claude/ChatGPT with browsing) can correctly answer a specific question about a paper's results, citing the github.io page.
- Link previews render correctly on X/Slack/LinkedIn.
- Zero broken inbound links from jamesparon.com after cutover.

## Dependencies & Risks

- **Author IDs (provided, locked in):** ORCID `0009-0001-5768-6424`, Google Scholar `OhpTkHEAAAAJ`, GSB `https://www.gsb.stanford.edu/faculty-research/faculty/james-d-paron`, homepage `https://jamesparon.com`. These populate the `Person`/`author` `sameAs` graph.
- **Paper links = the github.io-hosted PDFs themselves.** No separate SSRN/DOI links per paper (papers are working papers hosted here). `citation_pdf_url` and JSON-LD `encoding.contentUrl` point at the github.io `/papers/<slug>/paper.pdf`. Add `doi`/`ssrn` per paper later if/when published.
- **Zip cleanup is deferred:** delete `sources/*.zip` only after the site is built, reviewed, and the author confirms it's good. Until then they stay git-ignored in the working tree.
- **Content-provenance (highest-priority risk):** the site must never surface outdated/wrong material from the `sources/` project folders. Mitigation: PDF-only pipeline, git-ignored sources, and the Phase 3 QA pass that checks each page against its final PDF.
- **PDF extraction of heavy math/tables is lossy** — acceptable because the PDF stays authoritative; where extraction is too garbled to be trustworthy, Phase 3 trims the transcript to cleanly-extractable sections rather than publish misleading text.
- **Large binaries:** the provided zips (up to ~3.3 GB) must stay out of git — enforced via `.gitignore` from Phase 1.
- **llms.txt adoption is still low (2026)** — treated as cheap insurance; the HTML text is the real lever.
- **Duplicate content** if jamesparon.com later mirrors the same text — keep tiers differentiated.
- **PyMuPDF AGPL-3.0** — fine for open personal use; swap to pdfplumber/`pdftotext` if a permissive license is desired.

## Documentation Plan

- Update `README.md` to describe the generator, the "add a paper" workflow, and the read-only-sources rule.
- Short `CONTRIBUTING`/comment block in `build.py`; inline TODOs for author IDs.

## Sources & References

### Internal
- Current PDFs at repo root (8 papers + `ParonCV.pdf`); `README.md` is the only non-PDF committed file. Live site currently renders README via GitHub's default Jekyll 3.10.0 + jekyll-seo-tag 2.8.0.

### External (from planning research, 2026)
- Google Scholar inclusion / indexing guidelines: https://scholar.google.com/intl/en/scholar/inclusion.html#indexing
- schema.org ScholarlyArticle: https://schema.org/ScholarlyArticle
- GitHub Pages dependency versions (Jekyll 3.10.0, plugin whitelist): https://pages.github.com/versions/
- About GitHub Pages and Jekyll (static files, supported plugins): https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll
- Custom GitHub Actions workflows for Pages: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- AI crawlers explained (GPTBot/ClaudeBot/PerplexityBot, 2026): https://www.anagram.ai/blog/ai-crawlers-explained-gptbot-claudebot-perplexitybot-and-how-to-let-them-in-2026
- GEO experiment, HTML vs Markdown citation behavior: https://otterly.ai/blog/geo-experiment-html-vs-markdown/
- State of llms.txt 2026: https://presenc.ai/research/state-of-llms-txt-2026
- Google: consolidate duplicate URLs / canonical: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- PDF parser comparison (academic layouts): https://arxiv.org/html/2410.09871v1 ; PyMuPDF: https://pymupdf.readthedocs.io/ ; pdfplumber: https://github.com/jsvine/pdfplumber
- LaTeXML: https://math.nist.gov/~BMiller/LaTeXML/ ; pandoc: https://pandoc.org/
- Open Graph protocol: https://ogp.me/
