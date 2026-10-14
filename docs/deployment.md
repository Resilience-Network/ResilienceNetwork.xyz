# Deployment and verification

## Hosting

The site is static. Serve the repository root as-is; no build runs at deploy time. Any static host works (Cloudflare Pages or Workers static assets, GitHub Pages, S3 and a CDN). The host must:

- serve `index.html` for directory paths such as `/protocol/consensus/`;
- serve `404.html` for missing paths;
- serve `/.well-known/security.txt` as `text/plain`.

`src/`, `tools/` and `docs/` are published along with the site. They contain nothing private, but a host can exclude them.

## Redirects

The previous site's addresses (`protocol.html`, `research.html`, `status.html`, `decisions.html`, `get-started.html`) are generated as small pages that redirect immediately, configured in `src/site.json`. A host-level 301 can replace them later.

## Before merging

1. `python3 tools/build.py`
2. `python3 -m http.server 8000`, then check every touched page at 375, 768 and 1280 px.
3. Check internal links and fragments. Any HTML link checker works; the build output has no external links except fonts and `mailto:`.
4. Confirm no console errors and no horizontal scroll.
