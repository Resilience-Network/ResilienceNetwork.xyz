# Contributing to ResilienceNetwork.xyz

## Branches

Never commit directly to `main`. Work on a topic branch and merge through a pull request:

- `feature/<name>`: new pages or sections
- `fix/<name>`: corrections, including factual corrections
- `docs/<name>`: repository documentation
- `style/<name>`: visual changes
- `chore/<name>`: tooling and maintenance

## Commits

Use Conventional Commits: `<type>(<scope>): <summary>`, for example `fix(consensus): correct jailing window wording`.

## Making a change

1. Edit `src/pages/*.html` or `src/site.json`.
2. Run `python3 tools/build.py`.
3. Preview with `python3 -m http.server 8000`.
4. Check the pages you touched at phone, tablet and desktop widths, and run the link check in [docs/deployment.md](docs/deployment.md).
5. Commit the source and the generated files together and open a pull request that says which chain revision your numbers come from.

## Standards

- Semantic HTML: one `h1` per page, landmarks, labelled navigation, table headers with `scope`.
- Styles only through the tokens in `assets/css/site.css`. No external CSS or JS libraries.
- Fonts: Source Serif 4 for text, IBM Plex Mono for literal values, loaded from Google Fonts with system fallbacks.
- Plain, specific language. No marketing adjectives, no claims without a source.
