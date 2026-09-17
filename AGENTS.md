# Agent Instructions

## Required Workflow

- **Never commit directly to `main`**. Always use a dedicated topic branch (e.g. `feature/<name>`, `docs/<name>`, `style/<name>`, `chore/<name>`) and submit changes through `gh pr create`; merge only after review and verification pass.
- Follow [CONTRIBUTING.md](CONTRIBUTING.md) for branch naming, PR conventions, and commit formatting.
- Inspect the working tree before editing. Preserve unrelated changes, assets, and documentation.

## Start with Relevant Context

- Read [docs/README.md](docs/README.md) for an overview of the website structure and architecture.
- Review [docs/architecture.md](docs/architecture.md) for the design token system, animations, and canvas mechanics.
- Check [docs/deployment.md](docs/deployment.md) for hosting and domain configurations.

## Development & Design Discipline

- **Pure & Lightweight**: Prioritize clean, semantic HTML5, Vanilla CSS custom properties, and performant Vanilla JavaScript. Avoid introducing heavy external frameworks or dependencies unless explicitly requested.
- **Rich Aesthetics**: Maintain the modern dark mode design system, glowing gradients, glassmorphism, responsive typography, and 60fps micro-animations.
- **Accessibility & SEO**: Ensure valid semantic structure (`<header>`, `<main>`, `<footer>`, single `<h1>`), accessible ARIA attributes, and accurate metadata.
- **Zero Broken Links / Placeholders**: Never leave placeholder images or dead links.

## Verification

- Verify local rendering using a static HTTP server:
  ```bash
  python3 -m http.server 8000
  ```
- Test across mobile, tablet, and desktop viewports.
- Check browser console for errors, unhandled exceptions, or rendering layout shifts.
