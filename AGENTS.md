# Agent instructions

## Required workflow

- Never commit directly to `main`. Use a topic branch (`feature/`, `fix/`, `docs/`, `style/`, `chore/`) and merge through a pull request after review and verification.
- Follow [CONTRIBUTING.md](CONTRIBUTING.md) for branch names, commit messages and pull requests.
- Inspect the working tree before editing. Preserve unrelated changes and assets.

## How the site is built

- Pages are fragments in `src/pages/`; shared facts live in `src/site.json`. Never edit generated HTML directly: run `python3 tools/build.py` and commit source and output together.
- Light mode only. Do not add a dark theme, glow effects or decorative animation.
- No frameworks or npm dependencies. HTML, one stylesheet and one small script. Every page must read fully without JavaScript.
- Read [docs/architecture.md](docs/architecture.md) before changing styles and [docs/content.md](docs/content.md) before changing any claim.

## Content discipline

- Every number and claim must match the chain repository at the revision named in `src/site.json`. If you cannot find a source, do not publish the claim.
- Label claims with the status badges defined in `docs/content.md`. Internal reviews are never called audits.
- The chain repository is private: refer to source files as plain `<code class="src">path</code>` text, not links.
- Security findings appear as posture only (counts and areas) until fixes ship.

## Verification

- `python3 tools/build.py` succeeds.
- No broken internal links or fragments, and no horizontal scroll at 375, 768 and 1280 px wide.
- No console errors. Keyboard focus is visible.
- Claims re-checked against the chain repository; a fresh-eyes reviewer is preferred for any change to numbers.
