#!/usr/bin/env python3
"""One-command health check for the site. Run after any update.

Rebuilds the site and verifies, per paper and site-wide, that the conversion is
clean and complete. Uses only committed files (content/, pdfs/, papers.yaml) —
does NOT need sources/ or pandoc, so it can run in a fresh checkout.

Usage:  ./.venv/bin/python check.py            # rebuild + full check
        ./.venv/bin/python check.py --no-build # check existing site/ only
"""
from __future__ import annotations

import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

import fitz  # PyMuPDF
import yaml

ROOT = Path(__file__).parent.resolve()
CONTENT = ROOT / "content"
SITE = ROOT / "site"
MIN_OVERLAP = 0.72  # tex-vs-PDF word overlap below this => likely wrong/stale .tex

# (name, regex) artifact patterns that must NOT appear in content/*.md
ARTIFACTS = {
    "unresolved_cite": r"\*\*[A-Za-z][A-Za-z0-9:_-]+\?\*\*",
    "dropped_citeA": r"\\cite[AN]\b",
    "html_comment": r"\{=html\}",
    "dangling_ref": r"\[\\?\[[^\]]*\\?\]\]\(#",
    "raw_table": r"\\begin\{(tabular|tabularx|tabu)\}",
    "cmidrule_cell": r"(?m)^\| [0-9]-[0-9]",
    "eq_label": r"\\label\{",
    "nested_equation": r"\\begin\{equation",
    "spacing_junk": r"(?m)^\s*(to \.?\d|-\d+cm)\s",
}


def words(t: str) -> set[str]:
    return set(re.findall(r"[a-z]{4,}", t.lower()))


def pdf_words(pdf: Path) -> set[str]:
    doc = fitz.open(pdf)
    try:
        return words("\n".join(p.get_text("text") for p in doc))
    finally:
        doc.close()


def html_ok(path: Path) -> bool:
    try:
        HTMLParser().feed(path.read_text())
        return True
    except Exception:
        return False


def main():
    build = "--no-build" not in sys.argv
    if build:
        print("Rebuilding site ...")
        r = subprocess.run([sys.executable, str(ROOT / "build.py")],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print("BUILD FAILED:\n" + r.stderr[-2000:])
            sys.exit(1)

    data = yaml.safe_load((ROOT / "papers.yaml").read_text())
    papers = data["papers"]
    problems = 0

    print(f"\n{'paper':38s} {'overlap':>7s} {'cites?':>6s}  artifacts")
    print("-" * 74)
    for p in papers:
        slug = p["slug"]
        md_f, html_f = CONTENT / f"{slug}.md", CONTENT / f"{slug}.html"
        if not md_f.exists() or not html_f.exists():
            print(f"{slug:38s}  MISSING content/{slug}.md|.html")
            problems += 1
            continue
        md = md_f.read_text()
        pw = pdf_words(ROOT / p["pdf"])
        overlap = len(pw & words(md)) / max(1, len(pw))
        found = [name for name, pat in ARTIFACTS.items() if re.search(pat, md)]
        flags = []
        if overlap < MIN_OVERLAP:
            flags.append("LOW-OVERLAP")
        flags += found
        if flags:
            problems += 1
        print(f"{slug:38s} {overlap:7.2f} {('OK' if not found else 'BAD'):>6s}  "
              f"{', '.join(flags) if flags else 'clean'}")

    # Site-wide checks
    print("\nSite-wide:")
    site_pages = list(SITE.rglob("*.html")) if SITE.exists() else []
    bad_html = [f for f in site_pages if not html_ok(f)]
    print(f"  HTML pages: {len(site_pages)}, parse failures: {len(bad_html)}")
    problems += len(bad_html)

    # Every paper must ship its full set of files
    required = ["index.html", "paper.pdf", "index.md", "citation.bib", "preview.png"]
    for p in papers:
        d = SITE / "papers" / p["slug"]
        missing = [f for f in required if not (d / f).exists()]
        if missing:
            print(f"  MISSING for {p['slug']}: {missing}")
            problems += 1
    for f in ["index.html", "sitemap.xml", "robots.txt", "llms.txt", "llms-full.txt"]:
        if not (SITE / f).exists():
            print(f"  MISSING site/{f}")
            problems += 1
    if SITE.exists():
        n_urls = (SITE / "sitemap.xml").read_text().count("<loc>")
        print(f"  sitemap URLs: {n_urls}")

    print("\n" + ("✅ ALL CHECKS PASSED" if problems == 0
                  else f"❌ {problems} problem(s) — see above"))
    sys.exit(0 if problems == 0 else 1)


if __name__ == "__main__":
    main()
