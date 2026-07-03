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


def _unwrap_n(t: str, cmd: str, skip: int) -> str:
    """Replace \\cmd{a}...{content} with content, skipping `skip` leading args."""
    tag = "\\" + cmd
    out, i = [], 0
    while (j := t.find(tag, i)) >= 0:
        out.append(t[i:j])
        k = j + len(tag)
        groups = []
        while len(groups) <= skip and k < len(t):
            while k < len(t) and t[k] in " \n\t":
                k += 1
            if k < len(t) and t[k] == "[":            # optional arg
                depth = 1; k += 1
                while k < len(t) and depth:
                    depth += (t[k] == "[") - (t[k] == "]"); k += 1
                continue
            if k >= len(t) or t[k] != "{":
                break
            depth, start = 1, k + 1; k += 1
            while k < len(t) and depth:
                depth += (t[k] == "{") - (t[k] == "}"); k += 1
            groups.append(t[start:k - 1])
        out.append(groups[skip] if len(groups) > skip else "")
        i = k
    out.append(t[i:])
    return "".join(out)


def _normalize_tables(t: str) -> str:
    """Rewrite tabularx/tabu into plain tabular pandoc can parse."""
    t = re.sub(r"\\begin\{tabularx\}\{[^}]*\}\{([^}]*)\}",
               lambda m: r"\begin{tabular}{" + re.sub(r"X(\[[^\]]*\])?", "l", m.group(1)) + "}", t)
    t = t.replace(r"\end{tabularx}", r"\end{tabular}")
    t = re.sub(r"\\begin\{tabu\}(?:\s*to\s*[^\{]*?)?\{([^}]*)\}",
               lambda m: r"\begin{tabular}{" + re.sub(r"X(\[[^\]]*\])?", "l", m.group(1)) + "}", t)
    t = t.replace(r"\end{tabu}", r"\end{tabular}")
    return t


def fix_tex(t: str) -> str:
    """Neutralize constructs pandoc's LaTeX reader can't parse or mis-handles."""
    t = re.sub(r"\\cite[a-zA-Z]*<[^>]*>", r"\\cite", t)      # \cite<see>{k} -> \cite{k}
    # apacite textual citations pandoc drops -> natbib \citet (author (year))
    t = re.sub(r"\\(shortciteA|citeA|citeN)\b", r"\\citet", t)
    t = re.sub(r"\\cmidrule(\([^)]*\))?\s*\{[^}]*\}", "", t)  # partial rules leak as cells
    t = re.sub(r"\\cline\{[^}]*\}", "", t)
    t = _normalize_tables(t)
    t = _unwrap_n(t, "resizebox", 2)                         # \resizebox{w}{h}{T} -> T
    t = _unwrap_n(t, "scalebox", 1)                          # \scalebox{s}{T} -> T
    t = _unwrap_n(t, "adjustbox", 1)
    for cmd in ("centerline", "mbox", "hbox"):               # wrappers around block envs
        t = _unwrap(t, cmd)
    return t


def pandoc(main: str, cwd: Path, to: str, extra: list[str]) -> str:
    src = fix_tex(flatten(cwd / main, cwd))
    cmd = ["pandoc", "-f", "latex", "-t", to, "--wrap=none", *extra]
    r = subprocess.run(cmd, cwd=cwd, input=src, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"pandoc failed ({to}):\n{r.stderr[:1200]}")
    return r.stdout


# Residual LaTeX to strip from converted output (math-mode noise pandoc keeps).
_MATH_NOISE = [
    (re.compile(r"\\label\{[^}]*\}"), ""),                      # equation labels
    (re.compile(r"\\(vspace|hspace|vphantom|phantom|hphantom)\*?\{[^{}]*\}"), ""),
    (re.compile(r"\\rotatebox\{[^}]*\}\{([^{}]*)\}"), r"\1"),   # keep inner content
    (re.compile(r"\\setcounter\{[^}]*\}\{[^}]*\}"), ""),
    (re.compile(r"\\mathds\{1\}"), r"\\mathbb{1}"),
    (re.compile(r"\\(footnotesize|scriptsize|normalsize|small|large|Large|huge|"
                r"displaystyle|textstyle|nonumber|notag)\b"), ""),
]


def _strip_math_noise(s: str) -> str:
    for pat, rep in _MATH_NOISE:
        s = pat.sub(rep, s)
    return s


def _strip_common(s: str) -> str:
    """Cleanups common to markdown and HTML output."""
    s = s.replace("`<!-- -->`{=html}", "").replace("<!-- -->", "")
    s = re.sub(r"\{=html\}", "", s)
    s = s.replace('\\"', '"')                                   # unescape quotes
    # stray table/spacing tokens pandoc emits from unconverted layout
    s = re.sub(r"(?m)^\s*(to \.?\d[\d.]*|-?\d+(?:\.\d+)?(?:cm|in|pt|em))\s*$", "", s)
    s = re.sub(r"<span>-?\d+(?:\.\d+)?(?:cm|in|pt|em)</span>", "", s)
    s = re.sub(r"\*\*\[\]\*\*|(?<=\s)\[\](?=\s)", "", s)        # stray empty [] markers
    # redundant equation env inside $$/\[ ... \] display delimiters trips MathJax
    s = re.sub(r"\\(begin|end)\{equation\*?\}", "", s)
    # a `tabular` used only to lay out aligned-equation columns inside math:
    # flatten into a single stacked \begin{aligned} block so MathJax renders it.
    if "\\begin{tabular}" in s:
        s = re.sub(r"\\begin\{tabular\}\{[^}]*\}", "", s)
        s = s.replace(r"\end{tabular}", "")
        s = re.sub(r"\$\s*\\begin\{aligned\}(\[[a-z]\])?", r"\\begin{aligned}", s)
        s = re.sub(r"\\end\{aligned\}\s*\$", r"\\end{aligned}", s)
        # merge adjacent aligned blocks (column gap "& &" / "& {1cm} &") into one
        s = re.sub(r"\\end\{aligned\}\s*&[^&]*&\s*\\begin\{aligned\}(\[[a-z]\])?",
                   r"\\\\", s)
    return _strip_math_noise(s)


def clean_md(md: str) -> str:
    """Strip pandoc cross-ref cruft and non-content bits, keep text + TeX math."""
    # Dangling refs to unnumbered targets: "([\[eq:x\]](#eq:x))" -> drop (+ wrapping parens)
    md = re.sub(r"\(?\[\\?\[[^\]]*\\?\]\]\(#[^)]*\)\)?", "", md)
    md = re.sub(r"\[([^\]]+)\]\(#[^)]*\)\{[^}]*\}", r"\1", md)   # [2](#sec){...} -> 2
    md = re.sub(r"\[([^\]]+)\]\(#[^)]*\)", r"\1", md)            # [2](#sec) -> 2
    md = re.sub(r"\{#[^}]*\}", "", md)                          # {#sec:foo}
    md = re.sub(r"\{[^}\n]*reference-type[^}\n]*\}", "", md)     # {reference-type=...}
    md = re.sub(r"\{\.[^}\n]*\}", "", md)                       # {.class}
    md = re.sub(r"^:::.*$", "", md, flags=re.M)                 # fenced-div markers
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", md)                # images
    md = re.sub(r"\{width=\"[^\"]*\"[^}]*\}", "", md)
    md = _strip_common(md)
    md = re.sub(r"[ \t]{2,}", " ", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


def clean_html(h: str) -> str:
    h = re.sub(r"<figure[^>]*>.*?</figure>", "", h, flags=re.S)   # drop image figures
    h = re.sub(r"<img[^>]*>", "", h)
    h = re.sub(r'\s(id|data-reference[a-z-]*|reference-type)="[^"]*"', "", h)
    h = re.sub(r'<a href="#[^"]*"[^>]*>\s*\[[^\]]*\]\s*</a>', "", h)  # dangling label links -> drop
    h = re.sub(r'<a href="#[^"]*"[^>]*>(.*?)</a>', r"\1", h, flags=re.S)  # internal links -> text
    h = _strip_common(h)
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
    # Supplementary bib for citations missing from the uploaded .bib, built from
    # the PDF by gen_supplement_bib.py (committed, hand-editable).
    supp = ROOT / "bib_supplements" / f"{slug}.bib"
    if supp.exists():
        bibs.append(supp)
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
