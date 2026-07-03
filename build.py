#!/usr/bin/env python3
"""Static-site generator for jamesparon.github.io.

Reads papers.yaml, extracts the abstract + full text from each paper's FINAL
PDF (the sole content source — never from the sources/ project folders), and
emits a machine-readable, search- and LLM-discoverable site under ./site:

  site/index.html                     landing page (paper list + Person JSON-LD)
  site/papers/<slug>/index.html       per-paper page (full text + citation_* + JSON-LD)
  site/papers/<slug>/paper.pdf        the PDF, in the SAME dir as its page (Google Scholar rule)
  site/papers/<slug>/index.md         clean markdown mirror for LLMs
  site/<legacy>.pdf                   original URLs preserved (e.g. /CLP.pdf)
  site/cv/index.html + site/ParonCV.pdf
  site/sitemap.xml  robots.txt  llms.txt  llms-full.txt  static/style.css

Run:  ./.venv/bin/python build.py   (or via .github/workflows/build.yml in CI)
"""
from __future__ import annotations

import html
import json
import re
import shutil
from datetime import date, datetime
from pathlib import Path

import fitz  # PyMuPDF
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).parent.resolve()
SITE_URL = "https://jamesparon.github.io"
OUT = ROOT / "site"

env = Environment(
    loader=FileSystemLoader(str(ROOT / "templates")),
    autoescape=select_autoescape(["html", "xml"]),
    trim_blocks=True,
    lstrip_blocks=True,
)


# --------------------------------------------------------------------------- #
# PDF text extraction (final PDF is the ONLY content source)
# --------------------------------------------------------------------------- #
def extract_pdf_text(pdf_path: Path) -> str:
    """Return the full text of a PDF in reading order (PyMuPDF)."""
    doc = fitz.open(pdf_path)
    try:
        return "\n".join(page.get_text("text") for page in doc)
    finally:
        doc.close()


def clean_text(raw: str) -> str:
    """Normalize extracted PDF text into readable paragraphs.

    PyMuPDF emits one newline per visual line and (usually) a blank line
    between paragraphs. De-hyphenate line-broken words, split paragraphs on
    blank lines, and reflow the lines within each paragraph.
    """
    text = raw.replace("\x0c", "\n\n")            # form feed -> paragraph break
    text = text.replace("\u00ad", "")              # soft hyphen
    text = re.sub(r"-\n(?=[a-z])", "", text)        # de-hyphenate line-broken words
    paras = re.split(r"\n[ \t]*\n", text)          # paragraph breaks = blank lines
    cleaned = []
    for para in paras:
        para = re.sub(r"\s+", " ", para).strip()
        if para:
            cleaned.append(para)
    return "\n\n".join(cleaned)


def extract_abstract(fulltext: str) -> str:
    """Pull the abstract verbatim from the extracted text.

    Looks for an 'Abstract' heading and stops at Keywords / JEL / an
    'Introduction' section heading, whichever comes first.
    """
    m = re.search(r"\bAbstract\b[\s:.]*", fulltext, re.IGNORECASE)
    if not m:
        return ""
    tail = fulltext[m.end():]
    # After reflow, paragraph text is space-joined, so match on words/markers.
    stops = [
        r"\bKeywords\b", r"\bJEL\b",
        r"\b\d+\.?\s+Introduction\b", r"\bIntroduction\b",
        r"∗", r"\s\*\s+[A-Z]",          # acknowledgements footnote (∗ or plain *)
        r"\bFirst draft\b",
    ]
    end = len(tail)
    for pat in stops:
        sm = re.search(pat, tail)
        if sm and sm.start() < end:
            end = sm.start()
    abstract = re.sub(r"\s+", " ", tail[:end]).strip()
    # Guard against runaway matches (bad extraction): cap length.
    return abstract[:3000].strip()


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def sort_key(paper: dict):
    d = paper["date"]
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
        try:
            return datetime.strptime(d, fmt)
        except ValueError:
            continue
    return datetime.min


def citation_date(d: str) -> str:
    """ISO date -> Google Scholar 'YYYY/MM/DD' (or 'YYYY/MM')."""
    return d.replace("-", "/")


def paragraphs_html(text: str) -> str:
    return "\n".join(f"<p>{html.escape(p)}</p>" for p in text.split("\n\n") if p.strip())


def safe_jsonld(obj: dict) -> str:
    """Serialize a dict for embedding in a <script type=application/ld+json>."""
    return json.dumps(obj, ensure_ascii=False, indent=2).replace("</", "<\\/")


# --------------------------------------------------------------------------- #
# Meta / structured data builders
# --------------------------------------------------------------------------- #
def author_sameas(site: dict) -> list[str]:
    return [u for u in (site.get("orcid"), site.get("scholar"), site.get("gsb"),
                        site.get("homepage")) if u]


def person_node(site: dict) -> dict:
    return {
        "@type": "Person",
        "name": site["author_name"],
        "jobTitle": "Assistant Professor of Finance",
        "affiliation": {"@type": "Organization", "name": site["affiliation"]},
        "url": site["homepage"],
        "mainEntityOfPage": site["homepage"],
        "sameAs": author_sameas(site),
    }


def paper_head_meta(paper: dict, site: dict) -> str:
    """Build the full <head> discoverability payload for a paper page."""
    url = f"{SITE_URL}/papers/{paper['slug']}/"
    pdf_url = f"{url}paper.pdf"
    cdate = citation_date(paper["date"])
    inst = paper.get("institution") or site["institution"]

    metas: list[tuple[str, str]] = [
        ("citation_title", paper["title"]),
    ]
    for a in paper["authors"]:
        metas.append(("citation_author", a))
    metas += [
        ("citation_publication_date", cdate),
        ("citation_technical_report_institution", inst),
        ("citation_pdf_url", pdf_url),
        ("citation_abstract_html_url", url),
        ("citation_language", "en"),
    ]
    if paper.get("keywords"):
        metas.append(("citation_keywords", "; ".join(paper["keywords"])))

    lines = [f'<meta name="{n}" content="{html.escape(c, quote=True)}">' for n, c in metas]

    # Open Graph / Twitter
    desc = paper["abstract_short"]
    og = {
        "og:type": "article",
        "og:title": paper["title"],
        "og:description": desc,
        "og:url": url,
        "og:site_name": "James D. Paron — Research",
        "article:author": site["homepage"],
        "article:published_time": paper["date"],
    }
    for k, v in og.items():
        lines.append(f'<meta property="{k}" content="{html.escape(v, quote=True)}">')
    for k, v in {"twitter:card": "summary", "twitter:title": paper["title"],
                 "twitter:description": desc}.items():
        lines.append(f'<meta name="{k}" content="{html.escape(v, quote=True)}">')

    lines.append('<link rel="alternate" type="text/markdown" href="index.md">')

    # JSON-LD ScholarlyArticle
    jsonld = {
        "@context": "https://schema.org",
        "@type": "ScholarlyArticle",
        "headline": paper["title"],
        "name": paper["title"],
        "abstract": paper["abstract"],
        "datePublished": paper["date"],
        "inLanguage": "en",
        "url": url,
        "author": [
            {"@type": "Person", "name": a,
             **({"affiliation": {"@type": "Organization", "name": site["affiliation"]},
                 "url": site["homepage"], "sameAs": author_sameas(site)}
                if a == site["author_name"] else {})}
            for a in paper["authors"]
        ],
        "publisher": {"@type": "Organization", "name": inst},
        "encoding": {"@type": "MediaObject", "contentUrl": pdf_url,
                     "encodingFormat": "application/pdf"},
    }
    if paper.get("keywords"):
        jsonld["keywords"] = paper["keywords"]
    lines.append(
        '<script type="application/ld+json">\n' + safe_jsonld(jsonld) + "\n</script>"
    )
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# Build
# --------------------------------------------------------------------------- #
def build():
    data = yaml.safe_load((ROOT / "papers.yaml").read_text())
    site = data["site"]
    papers = data["papers"]
    build_day = date.today().isoformat()

    # Fresh output dir
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "papers").mkdir(parents=True)
    (OUT / "static").mkdir(parents=True)

    # Process each paper: extract from the FINAL PDF only.
    for p in papers:
        pdf_path = ROOT / p["pdf"]
        if not pdf_path.exists():
            raise SystemExit(f"Missing PDF for {p['slug']}: {pdf_path}")
        fulltext = clean_text(extract_pdf_text(pdf_path))
        p["fulltext"] = fulltext
        abstract = extract_abstract(fulltext)
        p["abstract"] = abstract
        p["abstract_short"] = (abstract[:297] + "…") if len(abstract) > 300 else abstract
        p["url"] = f"{SITE_URL}/papers/{p['slug']}/"
        p["authors_str"] = ", ".join(p["authors"])

    papers.sort(key=sort_key, reverse=True)

    paper_tpl = env.get_template("paper.html")
    md_tpl = env.get_template("paper.md.j2")

    sitemap_urls: list[tuple[str, str]] = [(f"{SITE_URL}/", build_day)]

    for p in papers:
        pdir = OUT / "papers" / p["slug"]
        pdir.mkdir(parents=True, exist_ok=True)
        # PDF copied into the paper's own subdir (Google Scholar requires this)
        shutil.copy2(ROOT / p["pdf"], pdir / "paper.pdf")
        # Preserve the original root URL (e.g. /CLP.pdf) as a real PDF copy
        if p.get("legacy_pdf"):
            shutil.copy2(ROOT / p["pdf"], OUT / p["legacy_pdf"])

        head_meta = paper_head_meta(p, site)
        (pdir / "index.html").write_text(paper_tpl.render(
            site=site, site_url=SITE_URL,
            page_title=f"{p['title']} — James D. Paron",
            page_description=p["abstract_short"],
            canonical=p["url"], head_meta=head_meta,
            paper=p,
            abstract_html=paragraphs_html(p["abstract"]),
            fulltext_html=paragraphs_html(p["fulltext"]),
            keywords_str="; ".join(p["keywords"]),
            jel_str=", ".join(p["jel"]),
        ))
        (pdir / "index.md").write_text(md_tpl.render(
            site=site, site_url=SITE_URL, paper=p,
            keywords_str=", ".join(p["keywords"]), jel_str=", ".join(p["jel"]),
        ))
        sitemap_urls += [
            (p["url"], p["date"] if len(p["date"]) == 10 else build_day),
            (f"{p['url']}paper.pdf", build_day),
            (f"{p['url']}index.md", build_day),
        ]

    # CV: simple page + preserve URL
    cv = data.get("cv")
    if cv:
        (OUT / "cv").mkdir(exist_ok=True)
        shutil.copy2(ROOT / cv["pdf"], OUT / "cv" / "ParonCV.pdf")
        if cv.get("legacy_pdf"):
            shutil.copy2(ROOT / cv["pdf"], OUT / cv["legacy_pdf"])
        (OUT / "cv" / "index.html").write_text(env.get_template("cv.html").render(
            site=site, site_url=SITE_URL,
            page_title="Curriculum Vitae — James D. Paron",
            page_description=f"Curriculum vitae of {site['author_name']}, {site['affiliation']}.",
            canonical=f"{SITE_URL}/cv/",
        ))
        sitemap_urls.append((f"{SITE_URL}/cv/", build_day))

    # Landing page
    person_jsonld = safe_jsonld({"@context": "https://schema.org", **person_node(site)})
    (OUT / "index.html").write_text(env.get_template("index.html").render(
        site=site, site_url=SITE_URL,
        page_title=f"{site['author_name']} — Research Papers",
        page_description=(f"Working papers by {site['author_name']}, {site['affiliation']}. "
                          "Full abstracts and machine-readable text for each paper."),
        canonical=f"{SITE_URL}/", papers=papers,
        person_jsonld=person_jsonld, has_cv=bool(cv),
    ))

    # static assets
    shutil.copy2(ROOT / "static" / "style.css", OUT / "static" / "style.css")
    (OUT / ".nojekyll").write_text("")  # serve artifact as-is, no Jekyll processing

    # robots.txt / sitemap.xml / llms.txt / llms-full.txt
    write_robots(OUT)
    write_sitemap(OUT, sitemap_urls)
    write_llms(OUT, site, papers)

    print(f"Built {len(papers)} papers -> {OUT}")


def write_robots(out: Path):
    ai_bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-Web",
               "anthropic-ai", "PerplexityBot", "Perplexity-User", "Google-Extended",
               "Applebot-Extended", "Bytespider", "CCBot"]
    lines = ["User-agent: *", "Allow: /", ""]
    for bot in ai_bots:
        lines += [f"User-agent: {bot}", "Allow: /", ""]
    lines.append(f"Sitemap: {SITE_URL}/sitemap.xml")
    (out / "robots.txt").write_text("\n".join(lines) + "\n")


def write_sitemap(out: Path, urls: list[tuple[str, str]]):
    body = ['<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lastmod in urls:
        body.append(f"  <url><loc>{html.escape(loc)}</loc><lastmod>{lastmod}</lastmod></url>")
    body.append("</urlset>")
    (out / "sitemap.xml").write_text("\n".join(body) + "\n")


def write_llms(out: Path, site: dict, papers: list[dict]):
    # /llms.txt — curated index
    lines = [f"# {site['author_name']} — Research Papers", "",
             f"> Machine-readable index of working papers by {site['author_name']} "
             f"({site['affiliation']}). Each link is a plain-text/markdown version of a "
             f"paper with its full abstract and text extracted from the definitive PDF. "
             f"Author's main site: {site['homepage']}", "", "## Papers", ""]
    for p in papers:
        lines.append(f"- [{p['title']}]({p['url']}index.md): "
                     f"{p['date_display']}, {p['authors_str']}. Full text.")
    lines += ["", "## Author", "",
              f"- [About {site['author_name']}]({site['homepage']}): "
              f"Assistant Professor of Finance, {site['affiliation']}.",
              f"- [Google Scholar]({site['scholar']})",
              f"- [ORCID]({site['orcid']})", "", "## PDFs", ""]
    for p in papers:
        lines.append(f"- [{p['title']} (PDF)]({p['url']}paper.pdf)")
    (out / "llms.txt").write_text("\n".join(lines) + "\n")

    # /llms-full.txt — everything in one file
    chunks = [f"# {site['author_name']} — Research Papers (full text)",
              f"# Source of truth: the linked PDFs at {SITE_URL}. "
              f"Text below is extracted from those final PDFs.", ""]
    for p in papers:
        chunks += ["=" * 78, f"TITLE: {p['title']}",
                   f"AUTHORS: {p['authors_str']}", f"DATE: {p['date_display']}",
                   f"URL: {p['url']}", f"PDF: {p['url']}paper.pdf"]
        if p["keywords"]:
            chunks.append(f"KEYWORDS: {', '.join(p['keywords'])}")
        if p["jel"]:
            chunks.append(f"JEL: {', '.join(p['jel'])}")
        chunks += ["", "ABSTRACT:", p["abstract"], "", "FULL TEXT:", p["fulltext"], ""]
    (out / "llms-full.txt").write_text("\n".join(chunks) + "\n")


if __name__ == "__main__":
    build()
