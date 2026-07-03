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
from collections import Counter
from datetime import date, datetime
from pathlib import Path

import fitz  # PyMuPDF
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).parent.resolve()
SITE_URL = "https://jamesparon.github.io"
OUT = ROOT / "site"
CONTENT = ROOT / "content"  # committed LaTeX-derived text (see tex_to_content.py)

env = Environment(
    loader=FileSystemLoader(str(ROOT / "templates")),
    autoescape=select_autoescape(["html", "xml"]),
    trim_blocks=True,
    lstrip_blocks=True,
)


# --------------------------------------------------------------------------- #
# PDF text extraction (final PDF is the ONLY content source)
#
# Footnotes, running heads, and page numbers are typeset in a smaller font than
# the body. Because PDF text comes out in geometric (top-to-bottom) order, that
# small-font material gets spliced into the middle of the body and breaks
# sentences that continue across a page. We classify each text block by its font
# size, keep only body-size (and larger, e.g. headings) blocks, drop the small
# ones, and then stitch sentences that span block/page boundaries back together
# so the paper reads continuously for an LLM/crawler.
# --------------------------------------------------------------------------- #
def _body_font_size(pages: list[dict]) -> float:
    """Most common font size across the document, weighted by character count."""
    sizes: Counter = Counter()
    for d in pages:
        for b in d.get("blocks", []):
            if b.get("type") != 0:  # text blocks only
                continue
            for line in b["lines"]:
                for span in line["spans"]:
                    t = span["text"].strip()
                    if t:
                        sizes[round(span["size"] * 2) / 2] += len(t)
    return sizes.most_common(1)[0][0] if sizes else 10.0


def extract_pdf_blocks(pdf_path: Path) -> tuple[list[str], list[str]]:
    """Return (body_blocks, note_blocks) split by font size.

    A block goes to notes if its largest span is clearly smaller than the body
    font (footnotes, running heads, page numbers). The 1.5pt margin keeps
    near-body content \u2014 e.g. a \\small abstract or block quote \u2014 in the body.
    """
    doc = fitz.open(pdf_path)
    try:
        pages = [page.get_text("dict") for page in doc]
    finally:
        doc.close()
    threshold = _body_font_size(pages) - 1.5
    body_blocks: list[str] = []
    note_blocks: list[str] = []
    for d in pages:
        for b in d.get("blocks", []):
            if b.get("type") != 0:
                continue
            spans = [s for line in b["lines"] for s in line["spans"] if s["text"].strip()]
            if not spans:
                continue
            block_max = max(s["size"] for s in spans)
            text = "\n".join("".join(s["text"] for s in line["spans"]) for line in b["lines"])
            (note_blocks if block_max < threshold else body_blocks).append(text)
    return body_blocks, note_blocks


def clean_blocks(blocks: list[str]) -> list[str]:
    """Reflow blocks into paragraphs and rejoin sentences split across blocks."""
    paras: list[str] = []
    for blk in blocks:
        blk = blk.replace("\u00ad", "")                       # soft hyphen
        blk = re.sub(r"-[ \t]*\n[ \t]*(?=[a-z])", "", blk)   # de-hyphenate line breaks
        p = re.sub(r"\s+", " ", blk).strip()
        if p:
            paras.append(p)
    # Merge continuations: a paragraph that doesn't end with sentence-ending
    # punctuation is almost always a sentence cut by a page/footnote break (or,
    # if short, a heading). Merge it with the next block when the next starts
    # lowercase OR the current block is long enough to not be a heading.
    ends_sentence = re.compile(r'[.!?:;\u201d")\]]\s*$')
    merged: list[str] = []
    for p in paras:
        prev = merged[-1] if merged else ""
        if prev and not ends_sentence.search(prev) and (p[:1].islower() or len(prev) > 80):
            if re.search(r'[A-Za-z]-$', prev):        # word hyphenated across a block break
                merged[-1] = prev[:-1] + p
            else:
                merged[-1] = prev + " " + p
        else:
            merged.append(p)
    return merged


def clean_text(raw: str) -> str:
    """Normalize a plain text blob into reflowed paragraphs (used for fallbacks)."""
    text = raw.replace("\x0c", "\n\n")
    text = text.replace("\u00ad", "")
    text = re.sub(r"-\n(?=[a-z])", "", text)
    return "\n\n".join(
        re.sub(r"\s+", " ", p).strip()
        for p in re.split(r"\n[ \t]*\n", text) if p.strip()
    )


def extract_abstract(fulltext: str) -> str:
    """Return the abstract as its own paragraph/block.

    The abstract is a single block bounded by paragraph breaks, so we find the
    'Abstract' heading and take that block (or the next one if 'Abstract' is a
    standalone heading), then trim any trailing Keywords/JEL line. This is far
    more robust than scanning for a section heading that may be absent.
    """
    paras = [p.strip() for p in fulltext.split("\n\n") if p.strip()]
    for i, para in enumerate(paras):
        m = re.match(r"Abstract\b[\s:.\-]*", para, re.IGNORECASE)
        if not m:
            continue
        rest = para[m.end():].strip()
        if len(rest) < 100 and i + 1 < len(paras):
            rest = paras[i + 1]          # 'Abstract' was a standalone heading
        rest = re.split(r"\b(?:Keywords|JEL)\b", rest)[0].strip()
        return re.sub(r"\s+", " ", rest)[:3000].strip()
    return ""


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

    # Open Graph / Twitter (large image card)
    desc = paper["abstract_short"]
    img = f"{url}preview.png"
    og = {
        "og:type": "article",
        "og:title": paper["title"],
        "og:description": desc,
        "og:url": url,
        "og:site_name": "James D. Paron — Research",
        "og:image": img,
        "article:author": site["homepage"],
        "article:published_time": paper["date"],
    }
    for k, v in og.items():
        lines.append(f'<meta property="{k}" content="{html.escape(v, quote=True)}">')
    for k, v in {"twitter:card": "summary_large_image", "twitter:title": paper["title"],
                 "twitter:description": desc, "twitter:image": img}.items():
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
# BibTeX + social-preview image
# --------------------------------------------------------------------------- #
def bibtex(paper: dict, site: dict) -> str:
    """A BibTeX @techreport entry for a working paper."""
    first = paper["authors"][0].split()[-1].lower()
    year = paper["date"][:4]
    key = f"{first}{year}{paper['slug'].split('-')[0]}"
    authors = " and ".join(paper["authors"])
    inst = paper.get("institution") or site["institution"]
    fields = [
        ("title", paper["title"]),
        ("author", authors),
        ("year", year),
        ("institution", inst),
        ("type", "Working Paper"),
        ("url", paper["url"]),
    ]
    body = ",\n".join(f"  {k} = {{{v}}}" for k, v in fields)
    return f"@techreport{{{key},\n{body}\n}}"


def _font(size: int):
    from PIL import ImageFont
    for path in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                 "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
                 "/Library/Fonts/Arial Bold.ttf",
                 "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"):
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def _wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines


def make_og_image(paper: dict, site: dict, out_path: Path):
    """Generate a 1200x630 social-preview card (title + authors + affiliation)."""
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        return False
    W, H = 1200, 630
    cardinal, ink, muted = (140, 21, 21), (26, 26, 26), (110, 110, 110)
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 16], fill=cardinal)                      # top bar
    title_font = _font(58)
    lines = _wrap(d, paper["title"], title_font, W - 160)[:4]
    y = 120
    for ln in lines:
        d.text((80, y), ln, font=title_font, fill=ink); y += 74
    d.text((80, y + 24), ", ".join(paper["authors"]), font=_font(34), fill=muted)
    d.text((80, H - 90), site["affiliation"], font=_font(30), fill=cardinal)
    d.text((80, H - 50), paper["date_display"], font=_font(26), fill=muted)
    img.save(out_path, "PNG")
    return True


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

    # Full text comes from the committed LaTeX-derived content/ files (math in
    # TeX math mode). The abstract is taken from the PDF (clean prose, good for
    # metadata). If a paper has no content/ file, fall back to PDF extraction.
    for p in papers:
        pdf_path = ROOT / p["pdf"]
        if not pdf_path.exists():
            raise SystemExit(f"Missing PDF for {p['slug']}: {pdf_path}")
        body_blocks, note_blocks = extract_pdf_blocks(pdf_path)
        abstract = extract_abstract("\n\n".join(clean_blocks(body_blocks)))
        if not abstract:
            abstract = extract_abstract("\n\n".join(clean_blocks(body_blocks + note_blocks)))
        p["abstract"] = abstract
        p["abstract_short"] = (abstract[:297] + "…") if len(abstract) > 300 else abstract
        p["url"] = f"{SITE_URL}/papers/{p['slug']}/"
        p["authors_str"] = ", ".join(p["authors"])

        html_frag = CONTENT / f"{p['slug']}.html"
        md_file = CONTENT / f"{p['slug']}.md"
        if html_frag.exists() and md_file.exists():
            p["fulltext_html"] = html_frag.read_text()
            p["fulltext_md"] = md_file.read_text()
            p["fulltext_source"] = "tex"
        else:  # fallback: PDF-extracted plain text
            ft = "\n\n".join(clean_blocks(body_blocks))
            p["fulltext_html"] = paragraphs_html(ft)
            p["fulltext_md"] = ft
            p["fulltext_source"] = "pdf"
        print(f"  {p['slug']:38s} src={p['fulltext_source']:3s} "
              f"abstract={len(abstract):4d}  fulltext={len(p['fulltext_md'])}")

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

        bib = bibtex(p, site)
        (pdir / "citation.bib").write_text(bib + "\n")
        make_og_image(p, site, pdir / "preview.png")

        head_meta = paper_head_meta(p, site)
        (pdir / "index.html").write_text(paper_tpl.render(
            site=site, site_url=SITE_URL,
            page_title=f"{p['title']} — James D. Paron",
            page_description=p["abstract_short"],
            canonical=p["url"], head_meta=head_meta,
            paper=p, bibtex=bib,
            abstract_html=paragraphs_html(p["abstract"]),
            fulltext_html=p["fulltext_html"],
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
    make_og_image({"title": f"{site['author_name']} — Research Papers",
                   "authors": ["Working papers in asset pricing, household finance, macro-finance"],
                   "date_display": site["homepage"].replace("https://", "")},
                  site, OUT / "preview.png")

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
             f"paper (full text converted from its LaTeX source, with mathematics in TeX "
             f"math mode). The PDF is the definitive version of each paper. "
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
              f"# Full text is converted from each paper's LaTeX source, with math "
              f"in TeX math mode. The definitive version of each paper is the PDF "
              f"linked at {SITE_URL}.", ""]
    for p in papers:
        chunks += ["=" * 78, f"TITLE: {p['title']}",
                   f"AUTHORS: {p['authors_str']}", f"DATE: {p['date_display']}",
                   f"URL: {p['url']}", f"PDF: {p['url']}paper.pdf"]
        if p["keywords"]:
            chunks.append(f"KEYWORDS: {', '.join(p['keywords'])}")
        if p["jel"]:
            chunks.append(f"JEL: {', '.join(p['jel'])}")
        chunks += ["", "ABSTRACT:", p["abstract"], "", "FULL TEXT:", p["fulltext_md"], ""]
    (out / "llms-full.txt").write_text("\n".join(chunks) + "\n")


if __name__ == "__main__":
    build()
