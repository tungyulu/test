# Implementation Plan: 快艇骰子遊戲（Yacht Dice）

**Branch**: `001-yacht-dice-game` | **Date**: 2026-06-21 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-yacht-dice-game/spec.md`

## Summary

Build a single-file `yacht.html` Yacht dice game matching Nintendo Switch's 51 Worldwide Games ruleset. Pure vanilla HTML/CSS/JS with Tailwind CDN — no build steps, hosted on GitHub Pages at `https://tungyulu.github.io/yacht.html`. Supports 1P-vs-CPU and 2P modes, 13 scoring categories, greedy CPU AI, and responsive layout.

## Technical Context

**Language/Version**: HTML5 + Vanilla JavaScript (ES2022) + CSS via Tailwind CDN

**Primary Dependencies**: Tailwind CSS (cdn.tailwindcss.com), Google Fonts Noto Sans TC — CDN only, no npm

**Storage**: N/A (no localStorage required; game state is in-memory only)

**Testing**: Manual browser testing per quickstart.md validation scenarios

**Target Platform**: Static file served via GitHub Pages; opens in any modern browser (Chrome 100+, Edge 100+, Safari 15+)

**Project Type**: Single-page web application (static HTML)

**Performance Goals**: CPU turn completes in ≤2s; dice roll animation ≤400ms; no frame drops during render

**Constraints**: Single `.html` file; no external image/JS/CSS beyond the two CDN sources; works on file:// and https://

**Scale/Scope**: 1 file, 2 players, 13 rounds, ~600–900 lines of HTML/JS/CSS

## Constitution Check

Constitution is a template (no project-specific rules set). No gate violations.

## Project Structure

### Documentation (this feature)

```text
specs/001-yacht-dice-game/
├── plan.md          ← this file
├── spec.md          ← feature specification
├── research.md      ← Phase 0 research
├── data-model.md    ← Phase 1 data model
├── quickstart.md    ← Phase 1 validation guide
├── contracts/
│   └── ui-contract.md   ← Phase 1 UI contract
└── tasks.md         ← Phase 2 output (created by /speckit-tasks)
```

### Source Code (repository root)

```text
yacht.html           ← single deliverable file
```

No separate src/ or tests/ directories. All logic is inline in `yacht.html` following the same convention as `betting.html`.

## Complexity Tracking

No constitution violations.

---

## Phase 1 Design Summary

### Data Model (see data-model.md)

- **Die**: `{ value: 1–6|null, held: boolean }` × 5
- **Scorecard**: 13 category fields, `null` = unused, `number` = filled (irreversible)
- **Player**: `{ name, scorecard, isCpu }`
- **GameState**: `{ phase, mode, players[2], currentPlayerIndex, round, dice[5], rollsLeft, rollPhase }`

### Scoring Rules

| Category | Score |
|----------|-------|
| Aces–Sixes | Sum of matching face values |
| Three/Four of a Kind | Sum of all dice (if condition met), else 0 |
| Full House | 25 (3+2 match), else 0 |
| Small Straight | 30 (4 consecutive), else 0 |
| Large Straight | 40 (5 consecutive), else 0 |
| Yacht | 50 (all 5 same), else 0 |
| Chance | Sum of all dice (always) |
| Upper Bonus | +35 if upper subtotal ≥ 63 |

### CPU Strategy (Greedy)

1. After each roll, score all available categories with current dice
2. Hold dice that maximize the best-scoring available category
3. Repeat up to 2 rerolls
4. Select the highest-scoring available category

### UI Layout

- Menu → Playing → Game Over (phase-driven rendering)
- Single `render()` called on every state change (same as betting.html)
- Scorecard: 2-column table (player per column), category rows, subtotal/bonus/total rows
- Dice: 5 inline SVG dice with click-to-hold
- Responsive: works at 375px (mobile); no horizontal overflow

### Key Implementation Sections (for tasks.md)

1. HTML skeleton + Tailwind/Font CDN links
2. SVG dice face definitions (inline, 6 variants)
3. `GameState` initialization and `render()` dispatcher
4. `rollDice()` + `toggleHold()` + dice animation (CSS keyframe)
5. `score(categoryId, dice)` — all 13 category scoring functions
6. `selectCategory(categoryId)` — fill scorecard, advance turn/round, check gameover
7. `computeScoreboard(scorecard)` — derived: upperSubtotal, bonus, lowerSubtotal, grandTotal
8. `renderMenu()` — mode selection screen
9. `renderPlaying()` — dice area + roll button + dual-column scorecard with previews
10. `renderGameover()` — final scorecard + winner highlight + replay button
11. `cpuTurn()` — greedy AI with setTimeout-based sequencing
12. Manual validation (quickstart.md V-01 through V-06)
