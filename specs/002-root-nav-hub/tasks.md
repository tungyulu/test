# Tasks: Root Navigation Hub

**Input**: Design documents from `specs/002-root-nav-hub/`

**Prerequisites**: plan.md ✓, spec.md ✓, research.md ✓, data-model.md ✓, contracts/ui-contract.md ✓, quickstart.md ✓

**Note**: No test tasks generated — not requested in spec. Manual validation via quickstart.md V-01 through V-07.

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different files, no dependencies on incomplete tasks)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)
- All tasks modify or validate a single file: `index.html` (repo root)

---

## Phase 1: Setup

**Purpose**: Rename the existing itinerary page so `index.html` is free for the hub.

- [x] T001 Rename `index.html` → `trip.html` using `git mv index.html trip.html` (preserves git history; no content changes needed)

**Checkpoint**: `git status` shows `index.html` renamed to `trip.html`; opening `trip.html` in browser shows the Japan itinerary unchanged.

---

## Phase 2: Foundational (HTML Skeleton)

**Purpose**: Create the bare `index.html` with CDN links and body structure that all three user stories build on.

**⚠️ CRITICAL**: Phases 3–5 cannot begin until this phase is complete.

- [x] T002 Create `index.html` at repo root with HTML5 boilerplate: `<!DOCTYPE html>`, `<html lang="zh-TW">`, `<head>` containing `<meta charset="UTF-8">`, `<meta name="viewport">`, `<title>我的小工具</title>`, and body with class `bg-slate-950 text-slate-100 min-h-screen`
- [x] T003 Add CDN `<script>` and `<link>` tags to `<head>` of `index.html`: Tailwind CSS (`cdn.tailwindcss.com`), GSAP 3.12.5 (`cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js`), Google Fonts preconnect + Noto Sans TC link, and inline `<style>` setting `body { font-family: 'Noto Sans TC', sans-serif; }`

**Checkpoint**: Open `index.html` in browser — dark background visible, no console CDN errors, Noto Sans TC applied.

---

## Phase 3: User Story 1 — Navigate to a sub-page from the hub (Priority: P1) 🎯 MVP

**Goal**: All three destination cards are visible and clickable, navigating to the correct page in the same tab.

**Independent Test**: Open `index.html`, verify three labelled cards appear, click each one and confirm correct page loads in same tab (quickstart.md V-01, V-02).

### Implementation for User Story 1

- [x] T004 [US1] Add `<header>` to `index.html` with a centered site title (`我的小工具`) and tagline (`選擇想前往的頁面`) styled with gradient background `from-indigo-900 via-slate-900 to-slate-950` and `border-b border-white/10`, matching the visual language of `betting.html`
- [x] T005 [US1] Add `<main>` to `index.html` containing a `max-w-4xl mx-auto px-6 py-12` wrapper with a `grid grid-cols-1 md:grid-cols-3 gap-6` card grid
- [x] T006 [US1] Add three `<a>` block cards inside the grid in `index.html`, each with class `nav-card` and styled as `bg-white/5 border border-white/10 rounded-2xl p-6 flex flex-col gap-3 transition active:scale-95`; card 1: emoji 🍁, title "Autumn Road Trip", desc "東京→熱海→河口湖 秋季紅葉巡航・8日行程", `href="trip.html"`; card 2: emoji 🏆, title "運彩投注紀錄", desc "世界盃複式串關・盈虧自動計算", `href="betting.html"`; card 3: emoji 🎲, title "快艇骰子", desc "5顆骰子・13類別・支援雙人與 CPU 對戰", `href="yacht.html"`
- [x] T007 [US1] Validate quickstart.md V-01 and V-02: open `index.html` in browser, confirm 3 cards visible with correct titles, click each card and verify same-tab navigation to `trip.html`, `betting.html`, `yacht.html` respectively

**Checkpoint**: User Story 1 fully functional — hub navigates correctly to all three sub-pages. This is a shippable MVP.

---

## Phase 4: User Story 2 — Animated entrance on page load (Priority: P2)

**Goal**: Cards animate in with a stagger on page load; reduced-motion users see cards appear instantly.

**Independent Test**: Hard-refresh hub page on motion-enabled device and observe stagger entrance; enable OS reduce-motion and reload to confirm instant appearance (quickstart.md V-03, V-04).

### Implementation for User Story 2

- [x] T008 [US2] Add a `<script>` block at the bottom of `<body>` in `index.html` with a `gsap.matchMedia()` call containing two conditions: `(prefers-reduced-motion: no-preference)` → `gsap.from('.nav-card', { y: 32, autoAlpha: 0, stagger: 0.12, duration: 0.5, ease: 'power2.out' })`; `(prefers-reduced-motion: reduce)` → `gsap.set('.nav-card', { autoAlpha: 1 })`
- [x] T009 [US2] Validate quickstart.md V-03 and V-04: hard-refresh confirms stagger entrance (cards rise in left→center→right within ~700ms); enable OS reduce-motion and reload confirms instant visibility with no animation

**Checkpoint**: User Stories 1 AND 2 functional — hub navigates and animates correctly.

---

## Phase 5: User Story 3 — Hover feedback on cards (Priority: P3)

**Goal**: On desktop pointer devices, hovering a card plays a smooth lift + shadow animation; no hover artefacts on touch devices.

**Independent Test**: On a desktop browser, hover each card and observe lift (y:-6, scale:1.03, indigo shadow); rapid mouse movement between cards leaves no stuck state (quickstart.md V-05).

### Implementation for User Story 3

- [x] T010 [US3] Inside the `(prefers-reduced-motion: no-preference)` branch of `gsap.matchMedia()` in `index.html`, add a nested `gsap.matchMedia()` for `(hover: hover) and (pointer: fine)` — bind `mouseenter` and `mouseleave` on each `.nav-card` element: `mouseenter` → `gsap.to(card, { y: -6, scale: 1.03, boxShadow: '0 16px 40px rgba(79,70,229,0.30)', duration: 0.25, overwrite: 'auto' })`; `mouseleave` → `gsap.to(card, { y: 0, scale: 1, boxShadow: '0 0px 0px rgba(0,0,0,0)', duration: 0.25, overwrite: 'auto' })`
- [x] T011 [US3] Validate quickstart.md V-05: hover each card on desktop — smooth lift plays; move mouse rapidly between cards — no card left stuck in hovered state

**Checkpoint**: All three user stories complete and independently functional.

---

## Phase 6: Polish & Cross-Cutting Validation

**Purpose**: Responsive layout, no-JS fallback, and full quickstart checklist sign-off.

- [x] T012 [P] Validate quickstart.md V-06 in `index.html`: open DevTools, set viewport to 360px wide, confirm all three cards stack in a single column with no horizontal scrollbar and all text fully readable
- [x] T013 [P] Validate quickstart.md V-07 in `index.html`: disable JavaScript in DevTools, reload hub page, confirm cards render with visible text and each link navigates correctly
- [x] T014 Run full quickstart.md checklist V-01 through V-07 in `index.html` and confirm all seven scenarios pass; record any failures before closing

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies — start immediately
- **Phase 2 (Foundational)**: Depends on Phase 1 (T001) — blocks Phases 3–5
- **Phase 3 (US1 P1)**: Depends on Phase 2 — independent of Phases 4 and 5
- **Phase 4 (US2 P2)**: Depends on Phase 2 — independent of Phase 5; requires GSAP CDN from T003
- **Phase 5 (US3 P3)**: Depends on Phase 4 (builds on the same `gsap.matchMedia()` block as T008)
- **Phase 6 (Polish)**: Depends on Phases 3–5 complete; T012 and T013 can run in parallel

### User Story Dependencies

- **US1 (P1)**: Can start after Phase 2 — no dependency on US2 or US3
- **US2 (P2)**: Can start after Phase 2 — no dependency on US1 or US3
- **US3 (P3)**: Depends on US2 (T008) — adds to the same `gsap.matchMedia()` block

### Within Each User Story

- Implementation task → validation task (sequential within each story phase)

### Parallel Opportunities

- T012 and T013 (Phase 6) can run in parallel — different validation dimensions, no file conflicts

---

## Parallel Example: Phase 6

```
# These two validation tasks are independent — run simultaneously:
T012: DevTools viewport → 360px → check no horizontal scroll
T013: DevTools disable JS → reload → check card links work
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: `git mv index.html trip.html`
2. Complete Phase 2: HTML skeleton + CDN links in `index.html`
3. Complete Phase 3: Header + card grid + 3 anchor cards
4. **STOP and VALIDATE**: V-01 and V-02 pass → hub navigates correctly
5. Deployable MVP at this point

### Incremental Delivery

1. Phase 1 + Phase 2 → skeleton ready
2. Phase 3 (US1) → navigation MVP ✓ deploy
3. Phase 4 (US2) → entrance animation ✓ deploy
4. Phase 5 (US3) → hover polish ✓ deploy
5. Phase 6 → full validation sign-off ✓

---

## Notes

- All implementation is in a single file: `index.html` (repo root)
- T001 must use `git mv` (not file rename) to preserve git history for `trip.html`
- Cards must be native `<a>` elements (not `div` + `onclick`) to satisfy V-07 (JS-disabled navigation)
- GSAP hover bindings must use `overwrite: 'auto'` to prevent animation stacking on rapid mouse movements
- No `target="_blank"` — all links open in the same tab (clarified in spec)
- No SplitText, ScrollTrigger, or other GSAP plugins needed — core GSAP only
