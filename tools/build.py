#!/usr/bin/env python3
"""Build the static site from src/ into the repository root.

Usage:  python3 tools/build.py

Each page source in src/pages/ is an HTML fragment that starts with a JSON
metadata comment:

    <!--meta
    {"path": "protocol/consensus/", "title": "...", "description": "...", ...}
    -->

The script wraps fragments in the shared layout (header, status strip,
footer), numbers <section id> / <h2> pairs as §1, §2 ... on "doc" pages,
builds the contents rail, wraps tables for horizontal scrolling, and writes
<path>/index.html at the repository root. Facts that appear on every page
(revision, manifest, dates) live in src/site.json and nowhere else.

The output is plain static HTML; hosting needs no build step. Commit both
src/ and the generated files.
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
SITE = json.loads((SRC / "site.json").read_text())

NAV = [
    ("protocol", "Protocol", "/protocol/"),
    ("assurance", "Assurance", "/assurance/"),
    ("status", "Status", "/status/"),
    ("decisions", "Decisions", "/decisions/"),
    ("developers", "Developers", "/developers/"),
    ("log", "Log", "/log/"),
]

META_RE = re.compile(r"^\s*<!--meta\s*(\{.*?\})\s*-->\s*", re.S)
SECTION_RE = re.compile(r'<section id="([a-z0-9-]+)"([^>]*)>\s*<h2>(.*?)</h2>', re.S)


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def header(active: str) -> str:
    items = []
    for key, label, href in NAV:
        attr = ""
        if key == active:
            attr = ' class="is-section"'
        items.append(f'<li><a href="{href}"{attr}>{label}</a></li>')
    s = SITE
    return f"""<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="bar">
    <a class="brand" href="/" aria-label="Resilience Network, home">
      <img src="/assets/img/logo-192.png" width="32" height="32" alt="">
      <span>Resilience Network</span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul>{''.join(items)}</ul>
    </nav>
  </div>
</header>
<div class="status-strip" role="note" aria-label="Network status">
  <div class="inner">
    <span class="item"><span class="dot" aria-hidden="true"></span>Pre-mainnet research network</span>
    <span class="item">No public testnet yet</span>
    <span class="item opt">Protocol manifest r{s['manifest']}</span>
    <span class="item opt">Shielded transfers experimental</span>
    <a href="/status/">Current status</a>
  </div>
</div>"""


def footer() -> str:
    s = SITE
    return f"""<footer class="site-footer">
  <div class="stamp">
    <p>Content verified against the reference implementation at <code class="src">{s['revision']}</code> ({s['revision_date']}), protocol manifest r{s['manifest']}. Numbers on this site describe that revision, not a deployed network.</p>
  </div>
  <div class="cols">
    <div class="about">
      <h2>Resilience Network</h2>
      <p>An experimental proof-of-stake network. The source code is private during pre-mainnet development; paths shown in monospace refer to files in the reference implementation.</p>
    </div>
    <div>
      <h2>Protocol</h2>
      <ul>
        <li><a href="/protocol/">Overview</a></li>
        <li><a href="/protocol/consensus/">Consensus</a></li>
        <li><a href="/protocol/execution/">Execution</a></li>
        <li><a href="/protocol/accounts/">Accounts</a></li>
        <li><a href="/protocol/privacy/">Privacy</a></li>
        <li><a href="/protocol/network/">Network and economics</a></li>
      </ul>
    </div>
    <div>
      <h2>Evidence</h2>
      <ul>
        <li><a href="/assurance/">Assurance</a></li>
        <li><a href="/status/">Status</a></li>
        <li><a href="/decisions/">Decisions</a></li>
        <li><a href="/log/">Log</a></li>
      </ul>
    </div>
    <div>
      <h2>Build</h2>
      <ul>
        <li><a href="/developers/">Developers</a></li>
        <li><a href="/glossary/">Glossary</a></li>
      </ul>
    </div>
    <div>
      <h2>Contact</h2>
      <ul>
        <li><a href="/security/">Security and disclosure</a></li>
        <li><a href="mailto:{s['contact']}">{s['contact']}</a></li>
      </ul>
    </div>
  </div>
  <div class="legal">
    <span>Nothing on this site is an offer of any asset. RSC is the protocol's native unit for fees, staking and rewards.</span>
    <span>Site updated {s['site_date']}</span>
  </div>
</footer>"""


def number_sections(body: str, numbered: bool) -> tuple[str, list[tuple[str, str, str]]]:
    toc: list[tuple[str, str, str]] = []
    counter = 0

    def repl(m: re.Match) -> str:
        nonlocal counter
        sid, attrs, title = m.group(1), m.group(2), m.group(3).strip()
        if "data-unnumbered" in attrs:
            n = ""
        else:
            counter += 1
            n = f"§{counter}" if numbered else ""
        toc.append((sid, n, re.sub(r"<[^>]+>", "", title)))
        num = f'<span class="n">{n}</span>' if n else ""
        return (f'<section id="{sid}"{attrs}>\n<h2>{num}{title}'
                f'<a class="anchor" href="#{sid}" aria-label="Link to this section">#</a></h2>')

    return SECTION_RE.sub(repl, body), toc


def wrap_tables(body: str) -> str:
    body = re.sub(r"<table", '<div class="table-wrap"><table', body)
    return body.replace("</table>", "</table></div>")


def toc_html(toc, pager) -> str:
    items = "".join(
        f'<li><a href="#{sid}"><span class="n">{n}</span><span>{esc(t)}</span></a></li>' for sid, n, t in toc
    )
    pg = ""
    if pager:
        links = []
        if pager.get("prev"):
            links.append(f'<a href="{pager["prev"][1]}">Previous: {esc(pager["prev"][0])}</a>')
        if pager.get("next"):
            links.append(f'<a href="{pager["next"][1]}">Next: {esc(pager["next"][0])}</a>')
        pg = f'<div class="pager">{"".join(links)}</div>'
    return f'<nav class="toc" aria-label="On this page"><h2>On this page</h2><ol>{items}</ol>{pg}</nav>'


def cite_block(meta) -> str:
    key = "resilience-" + meta["path"].strip("/").replace("/", "-")
    url = SITE["origin"] + "/" + meta["path"]
    return f"""<details class="cite">
<summary>Cite this page</summary>
<pre><code>@misc{{{key},
  title  = {{{{{meta['h1']}}}}},
  author = {{{{Resilience Network}}}},
  year   = {{{SITE['revision_date'][:4]}}},
  note   = {{Reference implementation {SITE['revision']}, protocol manifest r{SITE['manifest']}}},
  url    = {{{url}}}
}}</code></pre>
</details>"""


def page_head(meta) -> str:
    crumbs = ""
    if meta.get("crumbs"):
        parts = [f'<a href="{h}">{esc(t)}</a>' for t, h in meta["crumbs"]]
        crumbs = f'<div class="crumbs">{" / ".join(parts)}</div>'
    badge = meta.get("badge", "")
    lead = f'<p class="lead">{meta["lead"]}</p>' if meta.get("lead") else ""
    asof = f'<p class="asof">{meta["asof"]}</p>' if meta.get("asof") else ""
    return f"""<div class="page-head">
  <div class="wrap">
    {crumbs}
    {badge}
    <h1>{meta['h1']}</h1>
    {lead}
    {asof}
  </div>
</div>"""


def render(meta: dict, body: str) -> str:
    layout = meta.get("layout", "doc")
    if layout == "doc":
        body, toc = number_sections(body, meta.get("numbered", True))
        body = wrap_tables(body)
        tail = ""
        if meta.get("sources"):
            tail += f'<p class="sources">Sources: {meta["sources"]}</p>'
        if meta.get("cite"):
            tail += cite_block(meta)
        has_toc = meta.get("toc", True) and toc
        rail = toc_html(toc, meta.get("pager")) if has_toc else ""
        cls = "doc" if has_toc else "doc no-toc"
        content = f"""{page_head(meta)}
<div class="wrap">
  <div class="{cls}">
    {rail}
    <article class="prose">
{body}
{tail}
    </article>
  </div>
</div>"""
    else:  # "raw": page provides its own structure
        content = wrap_tables(body)

    title = meta["title"]
    full_title = "Resilience Network" if title == "Resilience Network" else f"{title} | Resilience Network"
    desc = esc(meta.get("description", SITE["description"]))
    canonical = SITE["origin"] + "/" + meta["path"]
    robots = '<meta name="robots" content="noindex">' if meta.get("noindex") else ""
    return f"""<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
{robots}
<meta name="theme-color" content="#002fa6">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Resilience Network">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE['origin']}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/img/logo-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/img/logo-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap">
<link rel="stylesheet" href="/assets/css/site.css?v={SITE['asset_version']}">
<script src="/assets/js/site.js?v={SITE['asset_version']}" defer></script>
</head>
<body>
{header(meta.get("nav", ""))}
<main id="main">
{content}
</main>
{footer()}
</body>
</html>
"""


def redirect_page(target: str, label: str) -> str:
    url = SITE["origin"] + target
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Moved to {esc(label)} | Resilience Network</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{url}">
<meta http-equiv="refresh" content="0; url={target}">
</head>
<body>
<p>This page moved to <a href="{target}">{esc(label)}</a>.</p>
</body>
</html>
"""


def main() -> int:
    pages = sorted((SRC / "pages").glob("*.html"))
    written = []
    for p in pages:
        raw = p.read_text()
        m = META_RE.match(raw)
        if not m:
            print(f"missing meta: {p}", file=sys.stderr)
            return 1
        meta = json.loads(m.group(1))
        body = raw[m.end():]
        out_path = meta["path"]
        out = ROOT / (out_path + "index.html" if out_path.endswith("/") or out_path == "" else out_path)
        if out_path == "":
            out = ROOT / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(meta, body))
        written.append((meta, out))

    for old, (target, label) in SITE["redirects"].items():
        (ROOT / old).write_text(redirect_page(target, label))

    # sitemap
    urls = []
    for meta, _ in written:
        if meta.get("noindex"):
            continue
        urls.append(f"  <url><loc>{SITE['origin']}/{meta['path']}</loc><lastmod>{SITE['site_date']}</lastmod></url>")
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"
    )
    print(f"built {len(written)} pages, {len(SITE['redirects'])} redirects")
    return 0


if __name__ == "__main__":
    sys.exit(main())
