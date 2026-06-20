# Research: Root Navigation Hub

**Feature**: 002-root-nav-hub | **Date**: 2026-06-21

---

## Decision 1: GSAP Stagger Entrance Pattern

**Decision**: Use `gsap.from('.nav-card', { y: 32, autoAlpha: 0, stagger: 0.12, duration: 0.5, ease: 'power2.out' })` triggered on `DOMContentLoaded`.

**Rationale**: `autoAlpha` manages both `opacity` and `visibility` cleanly; `y` offset gives a "rise in" feel consistent with the betting.html and yacht.html entrance animations already in the repo. `stagger: 0.12` spreads 3 cards across ~360ms — perceptible but not sluggish.

**Alternatives considered**:
- CSS-only `@keyframes` + `animation-delay` — simpler but harder to coordinate with `prefers-reduced-motion` and later interactivity (hover GSAP tweens).
- `gsap.fromTo` — unnecessary when the start state is known (card starts hidden, ends fully visible).

---

## Decision 2: prefers-reduced-motion Handling

**Decision**: Wrap the entire animation block in `gsap.matchMedia()` with a `(prefers-reduced-motion: reduce)` condition. Inside the reduced-motion branch, call `gsap.set('.nav-card', { autoAlpha: 1 })` to make cards immediately visible.

**Rationale**: `gsap.matchMedia()` is the idiomatic GSAP v3 approach (matches the betting.html pattern already in the repo). It handles media-query changes at runtime (e.g., user toggles OS setting while page is open) automatically.

**Alternatives considered**:
- `window.matchMedia('(prefers-reduced-motion: reduce)').matches` one-shot check — simpler, but doesn't respond to runtime changes and is less idiomatic for projects already using GSAP matchMedia.

---

## Decision 3: Hover Animation

**Decision**: On `(hover: hover) and (pointer: fine)` devices, use `gsap.to(card, { y: -6, scale: 1.03, boxShadow: '...', duration: 0.25 })` on `mouseenter` and reverse on `mouseleave`. Bind after initial animation completes (in `onComplete` callback or after stagger).

**Rationale**: Limits hover to true pointer devices (same guard used in betting.html). Scale + lift is the established micro-interaction pattern in this repo.

**Alternatives considered**:
- Pure CSS `:hover` transitions — simpler, but can't be cleanly suppressed by `gsap.matchMedia()` reduced-motion branch. Mixing CSS transitions and GSAP tweens on the same properties causes conflicts.

---

## Decision 4: Layout — Tailwind Grid

**Decision**: `grid grid-cols-1 md:grid-cols-3 gap-6` inside a `max-w-4xl mx-auto` container. Each card is a full `<a>` block element styled as a rounded card.

**Rationale**: Matches the `grid grid-cols-2 lg:grid-cols-4` pattern in betting.html. Three equal-width cards work best in a 3-column grid; below `md` (768 px) they stack vertically, satisfying the ≥360 px requirement.

**Alternatives considered**:
- Flexbox — less predictable equal-width behavior with 3 items; CSS Grid is cleaner for this use case.
- 2-column + 1 centered below — asymmetric and harder to maintain.

---

## Decision 5: Card Link Element

**Decision**: Each card is an `<a href="...">` block (not a `<div onclick>`), with `rel="noopener"` omitted (same-tab, same-origin). This ensures keyboard navigation and screen reader compatibility without JS.

**Rationale**: FR-007 requires JS-disabled navigation. Making the card itself the anchor is the only approach that satisfies this without JS. `rel="noopener"` is only needed for `target="_blank"` (new-tab), which was explicitly declined.

---

## Decision 6: File Rename Approach

**Decision**: `git mv index.html trip.html` — renames the file and preserves git history. The new `index.html` (hub) is created fresh.

**Rationale**: Preserves blame/log history for the itinerary page. No internal links inside `index.html` (Japan itinerary) reference itself by URL, so no content changes are needed after rename.

---

## Decision 7: CDN Stack

**Decision**: Load in this order: Tailwind CDN → GSAP CDN → Google Fonts (preconnect). No SplitText or ScrollTrigger plugins needed.

**Rationale**: Hub page needs only `gsap.core` (tweens, matchMedia) — no scroll-driven animation or text splitting. Keeping the CDN surface minimal reduces load time and matches SC-002 (< 2s).

**GSAP CDN**: `https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js` (same version as betting.html).
