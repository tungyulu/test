# Data Model: Root Navigation Hub

**Feature**: 002-root-nav-hub | **Date**: 2026-06-21

> This is a static page with no runtime data persistence. The "data model" describes the fixed card configuration baked into the HTML at build time.

---

## NavCard (static configuration)

Each of the three destination cards is described by:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `emoji` | string (1–2 chars) | Visual icon representing the destination | `"🍁"` |
| `title` | string | Human-readable name of the destination | `"Autumn Road Trip"` |
| `description` | string | One-line summary of the destination app | `"東京→熱海→河口湖 秋季紅葉巡航・8日行程"` |
| `href` | string (relative URL) | Path to the destination file | `"trip.html"` |

### Concrete Card Definitions

| # | emoji | title | description | href |
|---|-------|-------|-------------|------|
| 1 | 🍁 | Autumn Road Trip | 東京→熱海→河口湖 秋季紅葉巡航・8日行程 | `trip.html` |
| 2 | 🏆 | 運彩投注紀錄 | 世界盃複式串關・盈虧自動計算 | `betting.html` |
| 3 | 🎲 | 快艇骰子 | 5顆骰子・13類別・支援雙人與 CPU 對戰 | `yacht.html` |

### Validation Rules

- All `href` values must point to files that exist in the repository root.
- `title` and `description` must be non-empty strings.
- Card order is fixed: 1 → 2 → 3 (no user-configurable ordering).

---

## File Inventory (after feature delivery)

| File | Role | Action |
|------|------|--------|
| `index.html` (new) | Hub page (this feature) | Create |
| `trip.html` | Japan itinerary (existing content) | Rename from `index.html` |
| `betting.html` | Sports betting tracker | No change |
| `yacht.html` | Yacht dice game | No change |

---

## State Model

No runtime state. The page has no interactive state beyond:
- GSAP animation in-flight (managed by GSAP internals; no application state needed).
- CSS hover state on `.nav-card` (managed by GSAP tween on `mouseenter`/`mouseleave`).
