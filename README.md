# ResilienceNetwork.xyz

The public research site for **Resilience Network**, an experimental proof-of-stake blockchain with BFT finality, an EVM execution layer, native account authorization and Orchard shielded transfers.

Live: <https://resiliencenetwork.xyz>

The site publishes the protocol's specifications, its evidence (tests, threat models, internal reviews, load results) and its current status, each tied to a specific revision of the reference implementation. It is light mode only, written as a research document, and ships as plain static HTML.

## Structure

```text
src/
  site.json            Facts shown on every page: revision, manifest, dates, contact, redirects
  pages/*.html         One fragment per page, with a JSON metadata comment at the top
tools/build.py         Wraps fragments in the shared layout and writes the pages below
assets/css/site.css    Design tokens and components (single stylesheet)
assets/js/site.js      Progressive enhancement only: mobile menu, contents highlighting
assets/img/            Logo sizes, favicon and social image
index.html             Generated: home
protocol/ ...          Generated: protocol overview and five specification pages
assurance/ status/ decisions/ developers/ log/ glossary/ security/
404.html               Generated: not-found page
protocol.html, research.html, status.html, decisions.html, get-started.html
                       Generated redirects from the previous site's addresses
sitemap.xml            Generated
robots.txt, .well-known/security.txt
logo.png               Original brand insignia (full resolution)
docs/                  How the site is designed, built, verified and deployed
```

## Editing

1. Edit a fragment in `src/pages/` or a fact in `src/site.json`.
2. Run `python3 tools/build.py` (Python 3.9+, no dependencies).
3. Preview with `python3 -m http.server 8000` and open <http://localhost:8000>.
4. Commit both the source and the generated files. Hosting serves the generated files directly; there is no build step at deploy time.

When the reference implementation changes, update `src/site.json` (revision, date, manifest) and every affected number, then re-verify claims against the chain repository at that revision. See [docs/content.md](docs/content.md).

## Documentation

- [docs/README.md](docs/README.md): index
- [docs/architecture.md](docs/architecture.md): design system and page anatomy
- [docs/content.md](docs/content.md): content rules and how to keep claims true
- [docs/deployment.md](docs/deployment.md): hosting and verification
- [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md)
