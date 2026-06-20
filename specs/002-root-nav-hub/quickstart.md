# Quickstart & Validation Guide: Root Navigation Hub

**Feature**: 002-root-nav-hub | **Date**: 2026-06-21

---

## Prerequisites

- A modern browser (Chrome 100+, Edge 100+, Safari 15+, Firefox 100+)
- An internet connection (CDN assets: Tailwind, GSAP, Google Fonts)
- The repository files at their final state:
  - `index.html` — hub page (new)
  - `trip.html` — Japan itinerary (renamed from old `index.html`)
  - `betting.html` — sports betting tracker (unchanged)
  - `yacht.html` — yacht dice game (unchanged)

---

## How to Run

Open `index.html` directly in a browser (no server required):

```
# Windows
start index.html

# macOS / Linux
open index.html
```

Or, for GitHub Pages, navigate to: `https://tungyulu.github.io/test/`

---

## Validation Scenarios

### V-01 — Hub page loads at root URL

**Steps**: Open `https://tungyulu.github.io/test/` (or `index.html` locally).

**Expected**: Page loads with a header, three destination cards, and no console errors.

**Pass criteria**:
- [ ] Three cards visible: Autumn Road Trip, 運彩投注紀錄, 快艇骰子
- [ ] No 404 or JS errors in browser console
- [ ] Page background is dark (`slate-950`)

---

### V-02 — Card navigation (same tab)

**Steps**: Click each card in turn.

**Expected**: Each card navigates to its destination in the same browser tab.

**Pass criteria**:
- [ ] "Autumn Road Trip" → `trip.html` loads (Japan itinerary content visible)
- [ ] "運彩投注紀錄" → `betting.html` loads (betting tracker visible)
- [ ] "快艇骰子" → `yacht.html` loads (dice game visible)
- [ ] All navigations open in the same tab (no new tab opened)

---

### V-03 — Entrance animation on load

**Steps**: Hard-refresh the hub page on a desktop (motion-enabled) device. Watch the cards.

**Expected**: The three cards animate in sequentially (stagger ~120ms apart) rising from below with a fade-in.

**Pass criteria**:
- [ ] Cards are invisible at first frame, then animate to full opacity
- [ ] Cards appear in left → center → right order (or top → bottom on mobile)
- [ ] Animation completes within ~700ms of page load

---

### V-04 — Reduced-motion preference

**Steps**: Enable "Reduce motion" in OS settings (macOS: Accessibility → Display → Reduce motion; Windows: Ease of Access → Display → Show animations = Off). Reload the hub page.

**Expected**: Cards appear immediately at full opacity — no animation.

**Pass criteria**:
- [ ] All three cards are visible instantly on load (no fade or slide)
- [ ] No layout shift or invisible cards

---

### V-05 — Hover feedback (desktop)

**Steps**: On a desktop browser with a mouse, hover over each card.

**Expected**: Each hovered card lifts slightly (y-offset) and scales up with an indigo shadow.

**Pass criteria**:
- [ ] Hover feedback is smooth (no jank)
- [ ] Moving mouse rapidly between cards does not leave a card stuck in the hovered state

---

### V-06 — Responsive layout

**Steps**: Open DevTools, resize viewport to 360 px wide.

**Expected**: Cards stack in a single column; all three are fully visible without horizontal scrolling.

**Pass criteria**:
- [ ] No horizontal scrollbar at 360 px
- [ ] All card content (emoji, title, description) is fully readable

---

### V-07 — JavaScript disabled

**Steps**: In browser DevTools, disable JavaScript. Reload the hub page.

**Expected**: All three cards are visible as plain links and navigate correctly when clicked.

**Pass criteria**:
- [ ] Three cards render with visible text (no blank/invisible state)
- [ ] Each card link navigates to the correct page when clicked
- [ ] No broken layout due to missing JS

---

## Reference

- UI layout and animation spec: [`contracts/ui-contract.md`](contracts/ui-contract.md)
- Card content: [`data-model.md`](data-model.md)
- Full feature spec: [`spec.md`](spec.md)
