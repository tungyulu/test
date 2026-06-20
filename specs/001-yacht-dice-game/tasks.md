# Tasks: 快艇骰子遊戲（Yacht Dice）

**Input**: Design documents from `/specs/001-yacht-dice-game/`

**Prerequisites**: plan.md ✓, spec.md ✓, research.md ✓, data-model.md ✓, contracts/ui-contract.md ✓, quickstart.md ✓

**Tests**: No test tasks generated — no TDD requirement in spec.

**Organization**: Single-file deliverable (`yacht.html`). All tasks write into that one file, so parallelization within phases means sections can be developed simultaneously and merged. Tasks are grouped by user story for independent delivery.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Section can be developed in parallel with other [P] tasks in the same phase (different logical sections of the same file)
- **[Story]**: Which user story this task belongs to

---

## Phase 1: Setup

**Purpose**: Create the HTML skeleton — all subsequent tasks fill into this shell.

- [x] T001 Create `yacht.html` with HTML5 doctype, `<meta viewport>`, Tailwind CDN script tag, Google Fonts Noto Sans TC link, page `<title>快艇骰子</title>`, and empty `<div id="app"></div>` mount point + `<script>` block

**Checkpoint**: `yacht.html` opens in browser showing a blank white page with no console errors (CDN scripts load).

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core data structures and pure scoring logic — no rendering. MUST be complete before any user story.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [x] T002 [P] Add inline SVG dice-face helper `dieSVG(value, held)` returning an SVG string for faces 1–6 (white background, black pips, rounded rect border, amber tint when held) in `yacht.html` `<script>`
- [x] T003 [P] Implement `initState(mode)` factory returning a fresh `GameState` object (`phase:'playing'`, `mode`, `players[2]` each with blank `Scorecard`, `dice[5]` each `{value:null, held:false}`, `round:1`, `rollsLeft:3`, `rollPhase:false`) in `yacht.html` `<script>`
- [x] T004 Implement `score(categoryId, dice)` covering all 13 categories (Aces–Sixes sum matching face; Three/Four of a Kind; Full House 25; Small Straight 30; Large Straight 40; Yacht 50; Chance) and `computeScoreboard(scorecard)` returning `{upperSubtotal, upperBonus, lowerSubtotal, grandTotal}` in `yacht.html` `<script>`

**Checkpoint**: Open browser console and call `score('yacht', [{value:1},{value:1},{value:1},{value:1},{value:1}])` — expect `50`. Call `score('fullHouse', [{value:3},{value:3},{value:3},{value:5},{value:5}])` — expect `25`.

---

## Phase 3: User Story 1 — 完成一局完整遊戲 (Priority: P1) 🎯 MVP

**Goal**: A human-vs-human (or solo) 13-round game loop works end-to-end in the browser.

**Independent Test**: Open `yacht.html`, pick 2-player mode, play 13 rounds manually, see game-over screen with totals. (quickstart.md V-01)

### Implementation for User Story 1

- [x] T005 [US1] Implement `rollDice()` — for each die where `!held`, randomize `value` 1–6; decrement `rollsLeft`; set `rollPhase = true`; call `render()` in `yacht.html`
- [x] T006 [US1] Implement `toggleHold(i)` — flip `dice[i].held` when `state.rollPhase && state.rollsLeft > 0`; call `render()` in `yacht.html`
- [x] T007 [US1] Implement `selectCategory(categoryId)` — write `score(categoryId, dice)` into current player's scorecard; reset dice to `{value:null, held:false}` × 5, `rollsLeft:3`, `rollPhase:false`; if both players have filled all 13 categories set `phase:'gameover'`; else advance `currentPlayerIndex` (and increment `round` when wrapping back to player 0); call `render()` in `yacht.html`
- [x] T008 [US1] Implement `render()` dispatcher → calls `renderMenu()`, `renderPlaying()`, or `renderGameover()` based on `state.phase`; sets `document.getElementById('app').innerHTML` in `yacht.html`
- [x] T009 [US1] Implement `renderMenu()` — returns HTML with game title, one-line description, two buttons (`startGame('1p')` / `startGame('2p')`) in `yacht.html`
- [x] T010 [US1] Implement `renderPlaying()` — returns HTML for: (a) header bar with round/player indicator; (b) 5 dice using `dieSVG`, each clickable for `toggleHold`; (c) roll button showing `剩餘 ${rollsLeft} 次`, disabled when `rollsLeft===0`; (d) two-column scorecard table: category rows showing filled score OR preview score (gray, clickable) OR dash; subtotal/bonus/total rows; current player column highlighted in `yacht.html`
- [x] T011 [US1] Implement `renderGameover()` — returns HTML for final dual-column scorecard (all cells filled), section total rows, winner column highlighted green, "再玩一次" button calling `resetGame()` in `yacht.html`
- [x] T012 [US1] Implement `startGame(mode)`, `resetGame()`, and wire all event handlers via `onclick` attributes on rendered HTML elements; initialize with `render()` call at script end in `yacht.html`

**Checkpoint**: Full 2-player game completable in browser, scores match manual calculation (quickstart.md V-02).

---

## Phase 4: User Story 2 — CPU 自動出牌 (Priority: P2)

**Goal**: Single-player mode works — CPU automatically rolls, holds dice, and selects a category each turn.

**Independent Test**: Select single-player, complete one full game watching CPU take all its turns automatically. (quickstart.md V-04)

### Implementation for User Story 2

- [x] T013 [P] [US2] Implement `selectDiceToHold(categoryId, dice)` — returns array of booleans (which dice to hold) based on category: upper cats → hold matching face; ToaK/FoaK/Yacht → hold the most-frequent face; Full House → hold both groups; straights → hold the longest consecutive run; Chance → hold dice ≥4 in `yacht.html`
- [x] T014 [US2] Implement `cpuTurn()` — greedy loop: `setTimeout(400)` → compute best available category → `selectDiceToHold` → set `dice[i].held` → `rollDice()` → repeat up to 2 rerolls → `setTimeout(400)` → `selectCategory(bestCat)` in `yacht.html`
- [x] T015 [US2] In `selectCategory()`, after advancing to CPU player trigger `cpuTurn()`; in `renderPlaying()` add "CPU 思考中…" overlay and disable all interactive elements when `state.cpuThinking` flag is true in `yacht.html`

**Checkpoint**: 1P game runs fully automatically for CPU turns; no console errors; CPU completes turn in ≤2s (quickstart.md V-04).

---

## Phase 5: User Story 3 — 上區獎勵與最終計分板 (Priority: P2)

**Goal**: Upper bonus (+35 when ≥63) correctly displayed during and after game; final scorecard shows all sections.

**Independent Test**: Fill upper section to ≥63; confirm +35 appears. (quickstart.md V-03)

### Implementation for User Story 3

- [x] T016 [US3] In `renderPlaying()` scorecard, add upper-bonus row below the six upper categories showing `{upperSubtotal}/63` in gray while incomplete, and `+35 ✓` in green once `upperSubtotal ≥ 63` (using `computeScoreboard()`) in `yacht.html`
- [x] T017 [US3] In `renderGameover()`, add section breakdown rows: upper subtotal, bonus (+35 or –), lower subtotal, grand total; style winner column with `bg-green-100 font-bold`; handle tie case (both highlighted) in `yacht.html`

**Checkpoint**: Upper bonus row visible during play; final scorecard totals correct (quickstart.md V-03).

---

## Phase 6: User Story 4 — 新遊戲 / 重新開始 (Priority: P3)

**Goal**: After game over, player can return to the mode-selection menu cleanly.

**Independent Test**: Finish a game, click "再玩一次", confirm all state resets and menu renders.

### Implementation for User Story 4

- [x] T018 [US4] Implement `resetGame()` — set `state = { phase:'menu' }` and call `render()`; ensure the "再玩一次" button in `renderGameover()` calls this function in `yacht.html`

**Checkpoint**: "再玩一次" → menu appears, scorecard/dice fully reset, can start a fresh game.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Animation, responsive layout, edge-case hardening, final validation.

- [x] T019 [P] Add `@keyframes diceRoll` CSS animation (translate+rotate shake, ~400ms) to `yacht.html` `<style>` block; apply class to dice elements during `rollDice()` via a brief class toggle
- [x] T020 [P] Verify responsive layout at 375px viewport in DevTools: scorecard table fits without horizontal body overflow; dice row wraps cleanly; font size readable — fix any Tailwind classes as needed in `yacht.html`
- [x] T021 Audit all disabled-state conditions per ui-contract.md: roll button disabled after 3 rolls; held-click noop before first roll and after 3rd roll; category click noop on already-filled cells and before first roll; CPU turn blocks all interaction in `yacht.html`
- [x] T022 Run all 6 quickstart.md validation scenarios (V-01 through V-06) in Chrome and Edge; document and fix any failures in `yacht.html`

---

## Phase 8: Convergence

- [ ] T023 Resolve GSAP CDN constraint violation per plan: Constraints (contradicts) — either (a) remove `<script>` tags for `gsap.min.js` and `SplitText.min.js` from `yacht.html` and replace the five GSAP animation functions (`animateMenuIn`, `animateDiceRoll`, `animateHoldToggle`, `animateScoreCell`, `animateGameoverIn`) with CSS `@keyframes` + class-toggle equivalents as T019 originally specified, or (b) update `plan.md` Constraints section to explicitly document GSAP CDN (cdn.jsdelivr.net) as an approved dependency alongside Tailwind and Google Fonts

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies — start immediately
- **Phase 2 (Foundational)**: Depends on Phase 1 — **blocks all user stories**
- **Phase 3 (US1)**: Depends on Phase 2 — MVP deliverable
- **Phase 4 (US2)**: Depends on Phase 3 (needs `rollDice`, `selectCategory` to exist)
- **Phase 5 (US3)**: Depends on Phase 3 (needs scorecard rendering skeleton)
- **Phase 6 (US4)**: Depends on Phase 3 (needs `renderGameover`)
- **Phase 7 (Polish)**: Depends on Phases 3–6 being complete

### User Story Dependencies

- **US1 (P1)**: Can start after Phase 2 — no story dependencies
- **US2 (P2)**: Depends on US1 (game loop must exist before CPU can play)
- **US3 (P2)**: Depends on US1 (scorecard rendering must exist); independent of US2
- **US4 (P3)**: Depends on US1 (renderGameover must exist); independent of US2/US3

### Within Each Phase

- T002 and T003 (Phase 2) can be developed in parallel — different functions
- T013 (US2) can be developed in parallel with T014/T015 — pure helper function
- T005–T012 (US1) must be done in order: rollDice before selectCategory; rendering after logic
- T019 and T020 (Phase 7) can be done in parallel — independent concerns

### Parallel Opportunities

```
Phase 2:  T002 ‖ T003  →  then T004
Phase 3:  T005 → T006 → T007 → T008 → T009 → T010 → T011 → T012 (sequential)
Phase 4:  T013 ‖ (T014 → T015)
Phase 5:  T016 → T017 (sequential within US3)
Phase 7:  T019 ‖ T020  →  T021 → T022
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001)
2. Complete Phase 2: Foundational (T002–T004)
3. Complete Phase 3: User Story 1 (T005–T012)
4. **STOP and VALIDATE**: Run quickstart.md V-01 and V-02 — 2P game works, scores correct
5. Ship `yacht.html` to GitHub Pages — MVP playable

### Incremental Delivery

1. Phase 1 + 2 → foundation in place
2. Phase 3 → MVP (2P game works) → deploy
3. Phase 4 → add CPU → deploy (1P mode enabled)
4. Phase 5 → add bonus/totals display polish → deploy
5. Phase 6 → add restart → deploy
6. Phase 7 → polish, animation, mobile fix → final deploy

---

## Notes

- All tasks write into a single file: `yacht.html`
- [P] within a phase means the logical section can be authored independently and assembled
- No localStorage — state is ephemeral; no migration concerns
- CPU greedy strategy defined in data-model.md — implement exactly as specified
- Score rules are the reference; quickstart.md V-02 table is the acceptance oracle
- Tailwind utility classes preferred over custom CSS (except the dice animation keyframe)
