# Feature Specification: Root Navigation Hub

**Feature Branch**: `002-root-nav-hub`

**Created**: 2026-06-21

**Status**: Draft

**Input**: User description: "在這個repo新增一個root html, 讓https://tungyulu.github.io/test/ 這個網頁可以選擇我要去哪個網頁 1是Autumn Road Trip, 2 是 betting.html, 3 yacht.html /gsap-core"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Navigate to a sub-page from the hub (Priority: P1)

A visitor arrives at the site root (https://tungyulu.github.io/test/) and sees a visually appealing landing page listing all three available apps. They click (or tap) one card and are taken directly to that app.

**Why this priority**: This is the entire purpose of the hub page — without navigation working, the feature delivers zero value.

**Independent Test**: Open the root page in a browser, click each of the three cards, and confirm each link opens the correct page.

**Acceptance Scenarios**:

1. **Given** the user opens `https://tungyulu.github.io/test/`, **When** the page loads, **Then** three clearly labelled destination cards are visible: "Autumn Road Trip", "Sports Betting Tracker", and "Yacht Dice Game".
2. **Given** the user clicks the "Autumn Road Trip" card, **When** navigation completes, **Then** `trip.html` is displayed.
3. **Given** the user clicks the "Sports Betting Tracker" card, **When** navigation completes, **Then** `betting.html` is displayed.
4. **Given** the user clicks the "Yacht Dice Game" card, **When** navigation completes, **Then** `yacht.html` is displayed.

---

### User Story 2 - Animated entrance on page load (Priority: P2)

When the hub page finishes loading, the cards animate into view with a polished entrance sequence powered by GSAP, making the experience feel lively rather than static.

**Why this priority**: Visual polish is explicitly requested (`/gsap-core`). The page works without it, so it is a P2 enhancement.

**Independent Test**: Load the hub page and observe that cards animate in (stagger, fade, or slide) and that disabling animations via `prefers-reduced-motion` skips or simplifies the animation.

**Acceptance Scenarios**:

1. **Given** the page loads on a device that allows motion, **When** the DOM is ready, **Then** the three cards animate in sequentially with a stagger effect.
2. **Given** the user has `prefers-reduced-motion: reduce` enabled in their OS, **When** the page loads, **Then** the cards appear immediately without animation.

---

### User Story 3 - Hover feedback on cards (Priority: P3)

On desktop, hovering a card provides visible feedback (e.g., lift, scale, or glow) so users know it is interactive before clicking.

**Why this priority**: Nice-to-have interaction quality; works without it on touch devices.

**Independent Test**: On a desktop browser, hover each card and observe a visible style change animated smoothly.

**Acceptance Scenarios**:

1. **Given** the page is displayed on a device with a fine pointer (mouse), **When** the user hovers a card, **Then** a smooth animated feedback (lift or highlight) plays.
2. **Given** the page is displayed on a touch device, **When** the user views the cards, **Then** no hover artifact is visible; tap targets are large enough for comfortable use.

---

### Edge Cases

- What happens when a destination file is missing? The link still exists; the browser shows its standard 404 page. The hub page itself must not error.
- How does the layout behave on very narrow screens (< 360 px wide)? Cards stack vertically and remain fully readable.
- What if JavaScript is disabled? Cards are plain anchor elements and still navigate correctly; only animations are absent.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The hub page MUST be the file served at `https://tungyulu.github.io/test/` — it MUST be named `index.html` and placed at the repository root.
- **FR-002**: The hub page MUST display exactly three destination cards, each with a title and a short description.
- **FR-003**: Each card MUST be a clickable link that navigates to its target page (`trip.html`, `betting.html`, `yacht.html`) in the same browser tab.
- **FR-004**: Card destinations MUST be: (1) Autumn Road Trip → `trip.html`, (2) Sports Betting Tracker → `betting.html`, (3) Yacht Dice Game → `yacht.html`.
- **FR-005**: The page MUST load GSAP from CDN and animate cards in on load with a stagger entrance.
- **FR-006**: Animations MUST be suppressed (or reduced to opacity-only instant show) when `prefers-reduced-motion: reduce` is active, using `gsap.matchMedia()`.
- **FR-007**: The page MUST be fully usable without JavaScript (links navigate, content is readable).
- **FR-008**: The page layout MUST be responsive — single column on mobile, up to a 3-column grid on wider viewports.

### Key Entities

- **Hub Page** (`index.html`): The new root landing page listing the three destination cards.
- **Destination Card**: A visual tile with a title, short description, emoji/icon, and a link to a sub-page.
- **Existing Japan itinerary page**: Currently `index.html`; MUST be renamed to `trip.html` so the hub can occupy `index.html`.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All three navigation links reach their correct destination pages without any 404 errors.
- **SC-002**: The page is fully rendered and interactive in under 2 seconds on a standard broadband connection.
- **SC-003**: Cards animate in on load on motion-enabled devices; no animation occurs when the OS reduce-motion preference is active.
- **SC-004**: All three cards are visible without horizontal scrolling on screens as narrow as 360 px.
- **SC-005**: The page is visually distinct from the sub-pages and clearly communicates its role as a hub.

## Clarifications

### Session 2026-06-21

- Q: What filename should the existing `index.html` (Japan itinerary) be renamed to? → A: `trip.html`
- Q: Should destination card links open in the same tab or a new tab? → A: Same tab (standard `href`, no `target` attribute)

## Assumptions

- The existing `index.html` (Japan road trip itinerary) is renamed to `trip.html` (confirmed); all internal links within that file are self-contained and require no updates.
- GSAP is loaded from CDN only (no local install); an internet connection is required for animations, but the page degrades gracefully if the CDN is unreachable.
- No authentication, analytics, or server-side logic is needed — this is a pure static page consistent with the rest of the project.
- The site is deployed to GitHub Pages at `https://tungyulu.github.io/test/`; relative paths (e.g., `betting.html`) will resolve correctly.
- Tailwind CSS (CDN) will be used for styling to stay consistent with the existing pages in the repo.
- Google Fonts (Noto Sans TC) will be included for typographic consistency with the other pages.
