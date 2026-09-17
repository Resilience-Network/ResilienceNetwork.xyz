# Contributing to ResilienceNetwork.xyz

Thank you for contributing to the official Resilience Network web portal! This document outlines the standards, branch conventions, and pull request procedures for this repository.

---

## 0. Git Branching & Contribution Rules

> [!CAUTION]
> ### CRITICAL: NEVER COMMIT DIRECTLY TO THE `main` BRANCH
> - **NEVER commit directly to `main` under any circumstances.**
> - All new features, style refinements, bug fixes, and documentation updates MUST be developed on a dedicated topic branch:
>   - `feature/<name>`: New web features, sections, interactive modules
>   - `style/<name>`: Visual styling, CSS refinements, animations
>   - `fix/<name>`: Bug fixes, layout regressions, cross-browser compatibility
>   - `docs/<name>`: Documentation, guides, copy updates
>   - `chore/<name>`: Build scripts, tooling, CI workflows
> - All changes MUST be submitted via GitHub Pull Requests (`gh pr create`) and merged only after review.

---

## 1. Commit Message Guidelines

Use clear, descriptive commit messages adhering to the Conventional Commits format:

```text
<type>(<scope>): <concise summary>

[optional body]
```

### Types:
- `feat`: A new feature, page, or UI component
- `fix`: A bug fix or visual defect remediation
- `style`: CSS design system, typography, or animation enhancements
- `docs`: Documentation changes
- `refactor`: Code restructuring without visual or functional changes
- `chore`: Tooling, workflow, or repo maintenance

### Examples:
- `feat(landing): implement animated 3D cryptographic crucible`
- `style(canvas): enhance starfield and rising ember particle effects`
- `docs(deployment): add GitHub Pages custom domain instructions`

---

## 2. Web Development Standards

1. **Semantic HTML5**: Always use semantic tags (`<header>`, `<main>`, `<section>`, `<footer>`, `<nav>`) with proper accessibility landmarks.
2. **Vanilla CSS**:
   - Utilize CSS Custom Properties (`:root` variables) for colors, spacing, and typography tokens.
   - Avoid external CSS libraries (Tailwind, Bootstrap) unless explicitly decided.
   - Ensure fluid responsive design across mobile (360px+), tablet (768px+), and desktop (1280px+).
3. **Performant JavaScript**:
   - Keep scripts lightweight and native.
   - Use `requestAnimationFrame` for custom canvas rendering.
   - Clean up event listeners and intervals when needed.
4. **Typography**: Google Fonts (`Outfit`, `JetBrains Mono`) with robust system fallbacks.

---

## 3. Pull Request Process

1. Create a topic branch:
   ```bash
   git checkout -b feature/my-new-feature
   ```
2. Develop changes and verify locally with a static server:
   ```bash
   python3 -m http.server 8000
   ```
3. Commit with standard commit messages.
4. Push to origin:
   ```bash
   git push -u origin feature/my-new-feature
   ```
5. Open a Pull Request:
   ```bash
   gh pr create --title "[FEAT:UI] Concise Title" --body "..."
   ```
6. Address review comments before merging.
