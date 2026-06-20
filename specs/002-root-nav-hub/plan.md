# Implementation Plan: Root Navigation Hub

**Branch**: `002-root-nav-hub` | **Date**: 2026-06-21 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `specs/002-root-nav-hub/spec.md`

## Summary

Create a new `index.html` hub page for `https://tungyulu.github.io/test/` that displays three destination cards linking to the existing sub-pages. The existing `index.html` (Japan itinerary) is renamed to `trip.html`. Cards animate in with GSAP stagger on load; hover feedback plays on pointer devices. The page is responsive (single → 3-column grid), works without JavaScript, and respects `prefers-reduced-motion`.

## Technical Context

**Language/Version**: HTML5 + Vanilla JavaScript (ES2022)

**Primary Dependencies**: Tailwind CSS (cdn.tailwindcss.com), GSAP 3.12.5 (cdnjs.cloudflare.com), Google Fonts Noto Sans TC — CDN only, no npm

**Storage**: N/A (pure static page, no localStorage)

**Testing**: Manual browser validation per quickstart.md (V-01 through V-07)

**Target Platform**: Static file served via GitHub Pages; opens in any modern browser (Chrome 100+, Edge 100+, Safari 15+)

**Project Type**: Single-file static web application

**Performance Goals**: Fully rendered in < 2s on broadband; entrance animation completes in ≤ 700ms

**Constraints**: Single `index.html` file; CDN-only dependencies; no build system; must work on `file://` and `https://`

**Scale/Scope**: 1 new file (`index.html`), 1 rename (`index.html` → `trip.html`), ~80–120 lines of HTML/CSS/JS

## Constitution Check

Constitution is a template (no project-specific rules set). No gate violations.

## Project Structure

### Documentation (this feature)

```text
specs/002-root-nav-hub/
├── plan.md              ← this file
├── spec.md              ← feature specification
├── research.md          ← Phase 0 research
├── data-model.md        ← Phase 1 data model
├── quickstart.md        ← Phase 1 validation guide
├── contracts/
│   └── ui-contract.md   ← Phase 1 UI contract
└── tasks.md             ← Phase 2 output (created by /speckit-tasks)
```

### Source Code (repository root)

```text
index.html      ← NEW hub page (this feature's deliverable)
trip.html       ← RENAMED from index.html (Japan itinerary; no content changes)
betting.html    ← unchanged
yacht.html      ← unchanged
```

No `src/` or `tests/` directories. Single-file pattern consistent with `betting.html` and `yacht.html`.

## Complexity Tracking

No constitution violations.

---

## Phase 1 Design Summary

### Data Model (see data-model.md)

Three static NavCards baked into HTML:

| # | emoji | title | href |
|---|-------|-------|------|
| 1 | 🍁 | Autumn Road Trip | `trip.html` |
| 2 | 🏆 | 運彩投注紀錄 | `betting.html` |
| 3 | 🎲 | 快艇骰子 | `yacht.html` |

No runtime state. GSAP manages animation state internally.

### UI Layout

- Full-viewport dark page (`bg-slate-950`) matching existing sub-pages
- Centered header with site name + tagline
- `grid grid-cols-1 md:grid-cols-3 gap-6 max-w-4xl mx-auto` card grid
- Each card: `<a href>` block with emoji, `<h2>` title, `<p>` description, arrow indicator

### GSAP Animation Plan

```
gsap.matchMedia().add({
  '(prefers-reduced-motion: no-preference)': () => {
    // Entrance stagger
    gsap.from('.nav-card', { y: 32, autoAlpha: 0, stagger: 0.12, duration: 0.5, ease: 'power2.out' });
    // Hover on pointer devices
    gsap.matchMedia().add('(hover: hover) and (pointer: fine)', () => {
      // bind mouseenter/mouseleave on each .nav-card
    });
  },
  '(prefers-reduced-motion: reduce)': () => {
    gsap.set('.nav-card', { autoAlpha: 1 });
  }
});
```

### Key Implementation Steps (for tasks.md)

1. `git mv index.html trip.html` — rename Japan itinerary, preserving git history
2. Create `index.html` skeleton: `<!DOCTYPE html>`, `<head>` with CDN links (Tailwind, GSAP, Fonts)
3. Add `<header>` with site title and tagline
4. Add `<main>` with 3-column card grid; each card is a full `<a href>` block
5. Write GSAP entrance animation block inside `gsap.matchMedia()`
6. Write GSAP hover bindings (pointer-device guard)
7. Manual validation: run through V-01 → V-07 in quickstart.md
