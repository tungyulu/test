# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static HTML project with no build system or package manager. All HTML files are standalone pages that open directly in a browser. The only non-page file is `usage-dashboard.js`, a zero-dependency Node.js script (Node 18+) that also acts as an optional local server for `usage.html`.

## Files

- **`index.html`** — Site hub / navigation page (我的小工具). Displays four destination cards linking to the sub-pages below. Served at the GitHub Pages root (`https://tungyulu.github.io/test/`).
- **`trip.html`** — Japan road trip itinerary (東京—熱海—河口湖 秋季紅葉巡航), an 8-day travel schedule as a tabbed app shell (總覽 / 逐日行程 / 住宿 / 美食 / 交通) with timeline-style day cards inside the itinerary panel.
- **`betting.html`** — Sports betting tracker (世界盃運彩投注紀錄) for parlay/system bets, with combinatorics calculations, real-time profit/loss dashboard, and localStorage persistence.
- **`yacht.html`** — Yacht dice game (快艇骰子), 5-dice 13-category game supporting 1P-vs-CPU and 2P modes with greedy CPU AI and GSAP animations.
- **`usage.html`** — Claude Code usage dashboard (方案額度儀表板) showing `/usage`-style limit bars with auto-refresh. Works standalone (paste-token direct mode) or served by `usage-dashboard.js --serve`.
- **`usage-dashboard.js`** — Node.js CLI that renders the same usage data as a terminal dashboard (`node usage-dashboard.js`, `--once`, `--interval N`), plus `--serve [port]` which hosts `usage.html` at `http://localhost:8787` and proxies the Anthropic usage API.

## Architecture

### `index.html`
Single-file static hub page. No state, no localStorage. Four `<a class="nav-card">` block links in a custom CSS grid (`.card-grid`, `repeat(2, 1fr)`, single column under 600px). GSAP entrance animation (stagger) and hover lift, both guarded via `window.matchMedia` checks for `prefers-reduced-motion` and `(hover: hover) and (pointer: fine)`. Uses `gsap.set` + `gsap.to` (not `gsap.from` or `gsap.matchMedia` object form — the latter fires the callback once per matching condition and causes duplicate tweens).

### `trip.html`
Tabbed app shell (modeled on an external Hokkaido itinerary page): a sticky top tab bar switches five panels — `panel-overview` (route dot-map, stop cards, flights, pre-trip checklist), `panel-days` (D1–D8 timeline cards + day-chip row), `panel-stay` (lodging cards per stop), `panel-food` (restaurant picks grouped by area, each with a Google Maps search link + 💡 note; includes Gusto 河口湖店 & 新宿靖国通店 alongside Negishi), `panel-transport` (car-rental placeholder — Yokohama pick-up/return, fields marked ⚠️ 待補 — plus N'EX airport legs, D2–D4 drive routes with warnings, and D5–D8 Tokyo rail notes). Vanilla JS only: `showTab()` / `gotoDay()` / `gotoFood()` toggle `.hidden`, sync tab styles, and `history.replaceState` the hash; init routing supports `#overview/#days/#stay/#food/#transport`, legacy `#day-N`, `#food-*`, `#transport-*`, `#flight-info`. GSAP animations: header entrance + parallax and day-card hover lift live in a single `gsap.matchMedia().add(objectForm, cb)` block (conditions: animate/reduce/canHover); `animatePanelIn()` staggers panel cards on every tab switch (with `clearProps` so the sticky day-chip row isn't broken by leftover transforms); `initDaysReveal()` lazily creates the ScrollTrigger.batch day-card reveal the first time the days panel is shown (panels are `display:none`, so measuring earlier would be wrong). All animation is skipped under `prefers-reduced-motion` and the page degrades gracefully if the GSAP CDN fails. Day cards keep only a one-line 用餐建議 amber note linking into the food panel. Styling via Tailwind CDN + inline `<style>`; icons from Lucide CDN.

### `betting.html`
Single-file app with all state, logic, and rendering in one `<script>` block:
- **Storage**: `localStorage` under key `wc-betting-tracker-v1`; `load()`/`save()` handle serialization.
- **Data model**: `tickets[]` array, each ticket has `selections[]` (individual legs) and `groups[]` (parlay configurations with `size`, `stakePer`, optional `manualOdds`).
- **Combinatorics**: `combinations(arr, k)` generates all C(n,k) combos; `computeTicket()` iterates every group's combos to calculate staked/returned/potential amounts. Per-combo payout is rounded to the nearest integer (`Math.round`).
- **Rendering**: `render()` → `renderDashboard()` + `renderTickets()` rebuilds the entire DOM on every state change (no virtual DOM or framework).
- **Form**: Modal-based add/edit flow; `syncGroupCounts()` keeps parlay-size checkboxes in sync with leg count.
- **Import/Export**: JSON and CSV export via `Blob` + `<a>` download; JSON import via `FileReader`.

### `yacht.html`
Single-file app with phase-driven rendering (`menu` → `playing` → `gameover`):
- **State**: `{ phase, mode, players[], currentPlayerIndex, round, dice[5], rollsLeft, rollPhase, cpuThinking }` — all in-memory, no persistence.
- **Scoring**: `score(categoryId, dice)` covers all 13 Yacht categories; `computeScoreboard()` derives upper subtotal, +35 bonus, lower subtotal, grand total.
- **CPU AI**: Greedy — scores all available categories after each roll, holds dice that maximize the best-scoring category, rerolls up to twice.
- **Animations**: GSAP dice-roll squash/stretch, hold toggle bounce, score-cell flash, gameover stagger. SplitText used for menu title. All wrapped in `gsap.matchMedia()`.

### `usage.html` + `usage-dashboard.js`
Claude Code plan-usage dashboard. Data comes from `GET https://api.anthropic.com/api/oauth/usage` (OAuth Bearer token + `anthropic-beta: oauth-2025-04-20` header); both files share the same normalization logic (prefer `limits[]` — session / weekly_all / weekly_scoped — falling back to `five_hour`/`seven_day`) and severity thresholds (<80 cyan, ≥80 yellow, ≥95 red).

`usage.html` auto-detects its data source on load:
- **Local-server mode** (preferred): if same-origin `GET /api/usage` returns JSON, the page uses it. Run `node usage-dashboard.js --serve [port]` (default 8787, binds 127.0.0.1 only) — the server reads `~/.claude/.credentials.json` per request (so Claude Code token refresh is picked up) and proxies the API; no token pasting, no CORS.
- **Direct mode** (GitHub Pages / `file://`): user pastes their `claudeAiOauth.accessToken` (stored in localStorage `claude-usage-token`) and the page calls the API directly. The API does not send `Access-Control-Allow-Origin`, so browsers typically block this — a fetch `TypeError` shows a guidance card pointing to `--serve` mode. 401/403 re-opens the token card.

Other page state: refresh interval (1/5/15 min) in localStorage `claude-usage-interval`; on fetch failure the last data stays visible with a yellow warning (matching the CLI behavior). The CLI's terminal modes (default loop, `--once`, `--interval`) are unchanged from the original script; `--serve` reuses the shared `fetchUsage()`.

## External Dependencies (CDN only)

All pages load from CDN — no local dependencies to install:
- Tailwind CSS (`cdn.tailwindcss.com`)
- GSAP 3.12.5 (`cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/`) — core + ScrollTrigger (trip, betting), SplitText (yacht); index loads core only.
- Lucide icons (`unpkg.com/lucide@latest`) — trip, betting
- Google Fonts — Noto Sans TC (all pages)

## GSAP Usage Notes

- **`index.html`**: Use `window.matchMedia().matches` + `gsap.set`/`gsap.to`. Do NOT use `gsap.matchMedia().add(objectForm)` — it fires the callback once per matching condition, causing duplicate stagger tweens.
- **`trip.html`** / **`betting.html`** / **`yacht.html`**: Use `gsap.matchMedia().add(objectForm, cb)` — these pages already do so correctly, reading `ctx.conditions` inside a single callback.

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan at
`specs/002-root-nav-hub/plan.md`.
<!-- SPECKIT END -->
