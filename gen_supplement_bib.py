#!/usr/bin/env python3
"""Fill in citations missing from a paper's uploaded .bib, using its FINAL PDF.

Some papers reference a shared master .bib that wasn't uploaded, so pandoc's
citeproc leaves those keys unresolved (rendered as **key?**). This script parses
the PDF's reference list, matches each unresolved LaTeX cite key to a reference
entry (by first-author surname prefix + year, as encoded in the key), and writes
a supplementary BibTeX file bib_supplements/<slug>.bib. tex_to_content.py then
feeds that to citeproc so the citation renders as it does in the PDF
(e.g. "(Bordalo et al. 2016)").

The generated .bib is committed and can be hand-edited for any straggler keys.

Usage:  ./.venv/bin/python gen_supplement_bib.py <slug> [<slug> ...]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import fitz  # PyMuPDF
import yaml

ROOT = Path(__file__).parent.resolve()
SUPP = ROOT / "bib_supplements"


def parse_pdf_refs(pdf: Path) -> list[dict]:
    """Parse the References section into {authors:[(surname,initials)], year, title}."""
    doc = fitz.open(pdf)
    try:
        t = "\n".join(p.get_text() for p in doc)
    finally:
        doc.close()
    refs = t[t.rfind("\nReferences"):]
    refs = re.sub(r"-\n", "", refs)
    refs = re.sub(r"\s+", " ", refs)
    years = list(re.finditer(r"\((\d{4})[a-z]?\)", refs))
    author_tail = re.compile(
        r"((?:[A-Z][A-Za-z’'´.-]+,\s+(?:[A-Z]\.[-\s]*)+,?\s*(?:and\s+)?){1,})\s*$")
    entries, prev = [], 0
    for i, m in enumerate(years):
        chunk = refs[prev:m.start()]
        am = author_tail.search(chunk)
        block = am.group(1) if am else chunk[-160:]
        pairs = re.findall(r"([A-Z][A-Za-z’'´-]+),\s+((?:[A-Z]\.[-\s]*)+)", block)
        tail = refs[m.end(): (years[i + 1].start() if i + 1 < len(years) else m.end() + 200)]
        title = tail.strip(". ").split(". ")[0][:90]
        prev = m.end()
        if pairs:
            entries.append({"authors": [(s, re.sub(r"\s+", " ", ini).strip())
                                        for s, ini in pairs],
                            "year": m.group(1), "title": title})
    return entries


def key_parts(key: str):
    """(author_prefixes, year, is_etal) from a natbib-style cite key."""
    k = re.sub(r"(Macro|Stock|Rep|MAC|Pred|Insights|QJE|ReStud|JF|JFE)$", "", key)
    ym = re.search(r"(\d{2,4})$", k.replace(":", ""))
    if not ym:
        return None, None, False
    y = ym.group(1)
    year = y if len(y) == 4 else ("20" + y if int(y) <= 26 else "19" + y)
    base = k[:k.index(":")] if ":" in k else k[:ym.start()]
    etal = "etal" in base.lower()
    base = re.sub(r"etal", "", base, flags=re.I)
    parts = re.findall(r"[A-Z][a-z]+", base) or [base]
    return [p[:4].lower() for p in parts], year, etal


def match(key: str, entries: list[dict]):
    prefs, year, _etal = key_parts(key)
    if not prefs:
        return None
    cands = [e for e in entries
             if e["year"] == year and e["authors"]
             and e["authors"][0][0].lower().startswith(prefs[0])]
    if len(cands) > 1 and len(prefs) > 1:  # disambiguate by 2nd author
        c2 = [e for e in cands if len(e["authors"]) > 1
              and e["authors"][1][0].lower().startswith(prefs[1])]
        cands = c2 or cands
    return cands[0] if cands else None


def bib_entry(key: str, e: dict) -> str:
    authors = " and ".join(f"{s}, {ini}" for s, ini in e["authors"])
    title = e["title"].replace("{", "").replace("}", "")
    return (f"@article{{{key},\n  author = {{{authors}}},\n"
            f"  year = {{{e['year']}}},\n  title = {{{title}}},\n}}\n")


def unresolved_keys(slug: str) -> list[str]:
    md = (ROOT / "content" / f"{slug}.md").read_text()
    return sorted(set(re.findall(r"\*\*([A-Za-z][A-Za-z0-9:_-]+)\?\*\*", md)))


def main():
    data = yaml.safe_load((ROOT / "papers.yaml").read_text())
    by_slug = {p["slug"]: p for p in data["papers"]}
    SUPP.mkdir(exist_ok=True)
    for slug in sys.argv[1:]:
        p = by_slug[slug]
        keys = unresolved_keys(slug)
        entries = parse_pdf_refs(ROOT / p["pdf"])
        out, matched, missing = [], [], []
        for k in keys:
            e = match(k, entries)
            if e:
                out.append(bib_entry(k, e))
                matched.append(k)
            else:
                missing.append(k)
        header = (f"% Auto-generated from pdfs/{Path(p['pdf']).name} for keys missing\n"
                  f"% from the uploaded .bib. Hand-edit stragglers below if needed.\n\n")
        (SUPP / f"{slug}.bib").write_text(header + "\n".join(out))
        print(f"{slug}: parsed {len(entries)} refs; matched {len(matched)}/{len(keys)} keys")
        if missing:
            print(f"  UNMATCHED (add by hand to bib_supplements/{slug}.bib): {missing}")


if __name__ == "__main__":
    main()
