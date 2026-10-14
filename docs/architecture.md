# Architecture and design system

## Intent

A research document for a protocol that is still being proven. The design borrows from specification documents and engineering drawings rather than from product marketing: a cool paper ground with a faint drafting grid behind page titles, numbered sections, ruled tables, numbered figures, and status badges on claims. The brand's royal blue carries links and emphasis; the shield's gold marks the current location (active navigation, contents rail, lock markers) and is never used for text.

The one memorable element is on the home page: the development genesis commitment, printed in full as the network's identity.

## Tokens (`assets/css/site.css`)

| Token | Value | Use |
| --- | --- | --- |
| `--paper` | `#fafbfd` | Page background |
| `--panel` | `#f0f3f9` | Alternate bands, notes, code |
| `--ink` | `#121a33` | Text and heavy rules |
| `--ink-2`, `--muted` | `#3d4763`, `#5f6880` | Secondary text |
| `--rule` | `#d8deea` | Hairlines |
| `--blue` | `#002fa6` | Brand, links (from `logo.png`) |
| `--blue-deep` | `#001c66` | Status strip, hover |
| `--gold` | `#fdc703` | Location marks only (from `logo.png`) |
| `--st-*` | | Status badge colors |

Type: Source Serif 4 (optical sizes) for all text and headings; IBM Plex Mono only for literal values such as hashes, paths, constants and code. Body 17 px, line height 1.62, reading measure 42 rem.

## Page anatomy

- **Header** with the logo and six sections; a **status strip** under it states what is true today on every page.
- **Page head** with breadcrumbs, optional status badge, title, lead and as-of line, over the drafting grid.
- **Doc layout**: a sticky contents rail (generated from `<section id>` and `<h2>`) and a single reading column. Sections are numbered §1, §2 and the numbers hang in the margin on wide screens.
- **Footer** with the verification stamp generated from `src/site.json`.

## Components

`badge` (`b-impl`, `b-exp`, `b-prop`, `b-hist`, `b-int`, `b-no`, `b-plain`), `note` and `note warn`, `pull`, `params` tables, `register` (home feature list), `defaults` row, `manifest` card, `gates` checklists, `terms` definition list, `stories` disclosure lists, `cite` blocks.

## Figures

Figures are inline SVG inside `figure.fig`, drawn with the classes at the end of the stylesheet (`bx`, `bx-a`, `ln`, `t`, `s`, and so on) so they follow the tokens. Each has a `<title>` for screen readers, a numbered caption, a 680-unit-wide viewBox, and one arrow marker per path. Text stays at 11.5 px or larger at full width.

## Accessibility and robustness

Skip link, landmarks, one `h1`, labelled navigation, visible focus, `scope` on table headers, reduced-motion respected, print stylesheet, and full content without JavaScript.
