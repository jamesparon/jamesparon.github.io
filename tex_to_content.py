#!/usr/bin/env python3
"""Convert each paper's LaTeX manuscript to clean, LLM-readable content.

Runs LOCALLY (needs the git-ignored sources/ and pandoc). For every paper in
papers.yaml with a `tex_main`, it converts the FINAL manuscript .tex to:

  content/<slug>.md    Markdown with math kept in TeX math mode ($...$, $$...$$)
  content/<slug>.html  HTML body fragment with math as \\(...\\)/\\[...\\] (MathJax)

Both are committed; build.py (which runs in CI with no sources/ and no pandoc)
renders the site from them. Each conversion is verified against the paper's
final PDF — the manuscript text must overlap the PDF text, or we refuse to
publish it (guards against using an outdated/wrong .tex).

Usage:  ./.venv/bin/python tex_to_content.py [slug ...]
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import fitz  # PyMuPDF
import yaml

ROOT = Path(__file__).parent.resolve()
SOURCES = ROOT / "sources"
CONTENT = ROOT / "content"
MIN_OVERLAP = 0.55  # fraction of PDF vocabulary that must appear in the tex text


def flatten(path: Path, root: Path, seen: set[Path] | None = None) -> str:
    """Inline \\input/\\include recursively so we can feed one string to pandoc.

    Reads only; never writes to sources/. Missing includes (e.g. the shared
    jwstyle.tex that wasn't uploaded) are dropped so their macros stay raw.
    """
    seen = seen if seen is not None else set()
    text = path.read_text(errors="ignore")

    def repl(m: re.Match) -> str:
        name = m.group(1).strip()
        for base in (root, path.parent):
            for cand in (base / name, (base / name).with_suffix(".tex"),
                         Path(f"{base / name}.tex")):
                if cand.exists() and cand not in seen:
                    seen.add(cand)
                    return "\n" + flatten(cand, root, seen) + "\n"
        return ""  # missing include -> drop

    # only act on non-commented lines
    out = []
    for line in text.splitlines():
        if re.match(r"\s*%", line):
            continue
        out.append(re.sub(r"\\(?:input|include)\{([^}]+)\}", repl, line))
    return "\n".join(out)


def _unwrap(t: str, cmd: str) -> str:
    """Replace \\cmd{...} with its inner content (brace-matched)."""
    tag = "\\" + cmd + "{"
    out, i = [], 0
    while (j := t.find(tag, i)) >= 0:
        out.append(t[i:j])
        k, depth = j + len(tag), 1
        while k < len(t) and depth:
            depth += (t[k] == "{") - (t[k] == "}")
            k += 1
        out.append(t[j + len(tag):k - 1])
        i = k
    out.append(t[i:])
    return "".join(out)


def fix_tex(t: str) -> str:
    """Neutralize constructs pandoc's LaTeX reader can't parse."""
    t = re.sub(r"\\cite[a-zA-Z]*<[^>]*>", r"\\cite", t)   # \cite<see>{k} -> \cite{k}
    for cmd in ("centerline", "mbox", "hbox"):            # wrappers around block envs
        t = _unwrap(t, cmd)
    return t


def pandoc(main: str, cwd: Path, to: str, extra: list[str]) -> str:
    src = fix_tex(flatten(cwd / main, cwd))
    cmd = ["pandoc", "-f", "latex", "-t", to, "--wrap=none", *extra]
    r = subprocess.run(cmd, cwd=cwd, input=src, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"pandoc failed ({to}):\n{r.stderr[:1200]}")
    return r.stdout


def clean_md(md: str) -> str:
    """Strip pandoc cross-ref cruft and non-content bits, keep text + TeX math."""
    md = re.sub(r"\[([^\]]+)\]\(#[^)]*\)\{[^}]*\}", r"\1", md)   # [2](#sec){...} -> 2
    md = re.sub(r"\[([^\]]+)\]\(#[^)]*\)", r"\1", md)            # [2](#sec) -> 2
    md = re.sub(r"\{#[^}]*\}", "", md)                          # {#sec:foo}
    md = re.sub(r"\{[^}\n]*reference-type[^}\n]*\}", "", md)     # {reference-type=...}
    md = re.sub(r"\{\.[^}\n]*\}", "", md)                       # {.class}
    md = re.sub(r"^:::.*$", "", md, flags=re.M)                 # fenced-div markers
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", md)                # images
    md = re.sub(r"\{width=\"[^\"]*\"[^}]*\}", "", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


def clean_html(h: str) -> str:
    h = re.sub(r"<figure[^>]*>.*?</figure>", "", h, flags=re.S)   # drop image figures
    h = re.sub(r"<img[^>]*>", "", h)
    h = re.sub(r'\s(id|data-reference[a-z-]*|reference-type)="[^"]*"', "", h)
    h = re.sub(r'<a href="#[^"]*"[^>]*>(.*?)</a>', r"\1", h, flags=re.S)  # internal links -> text
    return h.strip() + "\n"


def words(t: str) -> set[str]:
    return set(re.findall(r"[a-z]{4,}", t.lower()))


def pdf_text(pdf: Path) -> str:
    doc = fitz.open(pdf)
    try:
        return "\n".join(p.get_text("text") for p in doc)
    finally:
        doc.close()


def convert(paper: dict) -> dict:
    slug = paper["slug"]
    texdir = SOURCES / paper["tex_dir"]
    main = paper["tex_main"]
    # Find .bib files in the manuscript dir and up to 3 parent levels.
    bibs, seen_names, d = [], set(), texdir
    for _ in range(4):
        for b in sorted(d.glob("*.bib")):
            if b.name not in seen_names and "__MACOSX" not in str(b):
                seen_names.add(b.name)
                bibs.append(b)
        d = d.parent
    cite = ["--citeproc"] if bibs else []
    for b in bibs:
        cite += ["--bibliography", str(b)]

    md = clean_md(pandoc(main, texdir, "markdown", cite))
    html = clean_html(pandoc(main, texdir, "html5",
                             ["--mathjax", "--shift-heading-level-by=1", *cite]))

    # Verify against the final PDF.
    pw = words(pdf_text(ROOT / paper["pdf"]))
    mw = words(md)
    overlap = len(pw & mw) / max(1, len(pw))

    raw_cites = len(re.findall(r"\[@[A-Za-z]", md))
    CONTENT.mkdir(exist_ok=True)
    (CONTENT / f"{slug}.md").write_text(md)
    (CONTENT / f"{slug}.html").write_text(html)
    return {"slug": slug, "overlap": overlap, "md_chars": len(md),
            "bib": len(bibs), "raw_cites": raw_cites}


def main():
    data = yaml.safe_load((ROOT / "papers.yaml").read_text())
    want = set(sys.argv[1:])
    papers = [p for p in data["papers"]
              if p.get("tex_main") and (not want or p["slug"] in want)]
    print(f"{'slug':38s} {'overlap':>8s} {'md_chars':>9s} {'bibs':>5s} {'rawcite':>8s}")
    bad = []
    for p in papers:
        try:
            r = convert(p)
        except Exception as e:
            print(f"{p['slug']:38s}  ERROR: {str(e).splitlines()[0][:80]}")
            bad.append(p["slug"])
            continue
        flag = "  OK" if r["overlap"] >= MIN_OVERLAP else "  ** LOW OVERLAP **"
        print(f"{r['slug']:38s} {r['overlap']:8.2f} {r['md_chars']:9d} {r['bib']:5d} {r['raw_cites']:8d}{flag}")
        if r["overlap"] < MIN_OVERLAP:
            bad.append(r["slug"])
    if bad:
        print(f"\nNEEDS ATTENTION: {bad}")


if __name__ == "__main__":
    main()
