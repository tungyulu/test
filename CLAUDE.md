# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static HTML project with no build system or package manager. All HTML files are standalone pages that open directly in a browser. The only non-page file is `usage-dashboard.js`, a zero-dependency Node.js script (Node 18+) that renders a terminal usage dashboard; it has no local-server mode.

## Files

- **`index.html`** — Site hub / navigation page (我的小工具). Displays six destination cards linking to the sub-pages below. Served at the GitHub Pages root (`https://tungyulu.github.io/test/`).
- **`trip.html`** — Japan road trip itinerary (關東秋季紅葉巡航: 東京 / 河口湖 / 湘南), an 8-day travel schedule as a tabbed app shell (總覽 / 逐日行程 / 住宿 / 美食 / 交通) with timeline-style day cards inside the itinerary panel.
- **`betting.html`** — Sports betting tracker (世界盃運彩投注紀錄) for parlay/system bets, with combinatorics calculations, real-time profit/loss dashboard, and localStorage persistence.
- **`yacht.html`** — Yacht dice game (快艇骰子), 5-dice 13-category game supporting 1P-vs-CPU and 2P modes with greedy CPU AI and GSAP animations.
- **`usage.html`** — Claude Code usage dashboard (方案額度儀表板) showing `/usage`-style limit bars with auto-refresh. Standalone paste-token direct mode only (no local-server mode).
- **`usage-dashboard.js`** — Node.js CLI that renders usage data as a terminal dashboard (`node usage-dashboard.js`, `--once`, `--interval N`, `--selftest`), enhanced with reset countdowns, a projected time-to-limit estimate, a big LED-style clock, live CPU/RAM bars, and (when the `ccusage` CLI is installed) today's/week's/month's spend with a 7-day sparkline.
- **`dyson.html`** — Static research report (Dyson 選購 — 四家 AI 交叉比對): a cross-comparison of four AI answers about which Dyson vacuum to buy, laid out as verdict panel, rank matrix, divergence cards, hallucination table, weighted-score bars, and a to-verify list. Content-only, no interactivity.
- **`invest.html`** — Static investment playbook (投資作戰表 — 2026 年 9～12 月): a personal Taiwan-stock strategy note snapshotted at 2026-09-02, laid out as a 9-stock battle-plan table (target %, add/take-profit/defense price zones), per-stock cards with price ladders, monthly NT$20,000 allocation paths, a target-allocation bar chart, and a price-trigger quick table. Content-only, no interactivity — same self-contained pattern as `dyson.html`.

## Architecture

### `index.html`
Single-file static hub page. No state, no localStorage. Six `<a class="nav-card">` block links in a custom CSS grid (`.card-grid`, `repeat(2, 1fr)`, single column under 600px — six cards lay out 2/2/2). GSAP entrance animation (stagger) and hover lift, both guarded via `window.matchMedia` checks for `prefers-reduced-motion` and `(hover: hover) and (pointer: fine)`. Uses `gsap.set` + `gsap.to` (not `gsap.from` or `gsap.matchMedia` object form — the latter fires the callback once per matching condition and causes duplicate tweens).

### `trip.html`
Tabbed app shell (modeled on an external Hokkaido itinerary page): a sticky top tab bar switches five panels — `panel-overview` (route dot-map, stop cards, flights, pre-trip checklist), `panel-days` (D1–D8 timeline cards + day-chip row), `panel-stay` (lodging cards per stop), `panel-food` (restaurant picks grouped by area, each with a Google Maps search link + 💡 note; includes Gusto 河口湖店/新宿靖国通店/藤澤 and 焼肉ここから alongside Negishi), `panel-transport` (booked Toyota Rent-a-Car 関内店 details — GR Yaris, 11/08 10:30 pick-up to 11/11 10:30 return — plus N'EX airport legs, D2–D4 drive routes with warnings, and D5–D8 Tokyo rail notes). Vanilla JS only: `showTab()` / `gotoDay()` / `gotoFood()` toggle `.hidden`, sync tab styles, and `history.replaceState` the hash; init routing supports `#overview/#days/#stay/#food/#transport`, legacy `#day-N`, `#food-*`, `#transport-*`, `#flight-info`. GSAP animations: header entrance + parallax and day-card hover lift live in a single `gsap.matchMedia().add(objectForm, cb)` block (conditions: animate/reduce/canHover); `animatePanelIn()` staggers panel cards on every tab switch (with `clearProps` so the sticky day-chip row isn't broken by leftover transforms); `initDaysReveal()` lazily creates the ScrollTrigger.batch day-card reveal the first time the days panel is shown (panels are `display:none`, so measuring earlier would be wrong). All animation is skipped under `prefers-reduced-motion` and the page degrades gracefully if the GSAP CDN fails. Day cards keep only a one-line 用餐建議 amber note linking into the food panel. Styling via Tailwind CDN + inline `<style>`; icons from Lucide CDN.

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
Claude Code plan-usage dashboard. Data comes from `GET https://api.anthropic.com/api/oauth/usage` (OAuth Bearer token + `anthropic-beta: oauth-2025-04-20` header); both files independently normalize the response the same way (prefer `limits[]` — session / weekly_all / weekly_scoped — falling back to `five_hour`/`seven_day`) and use the same severity thresholds (<80 cyan, ≥80 yellow, ≥95 red).

`usage.html` still probes same-origin `GET /api/usage` once on load (`detectMode()`) before falling back, but there is no longer any server in this repo that serves that endpoint, so it always ends up in:
- **Direct mode** (the only supported mode): user pastes their `claudeAiOauth.accessToken` (stored in localStorage `claude-usage-token`) and the page calls the Anthropic API directly from the browser. The API does not send `Access-Control-Allow-Origin`, so browsers typically block this — a fetch `TypeError` shows a guidance card pointing the user at the terminal CLI (`node usage-dashboard.js`) instead. 401/403 re-opens the token card.

Other page state: refresh interval (1/5/15 min) in localStorage `claude-usage-interval`; on fetch failure the last data stays visible with a yellow warning (matching the CLI's own stale-data behavior).

`usage-dashboard.js` is terminal-only (`--once`, `--interval N`, `--selftest` for injecting fake data without hitting the API). Beyond the shared limits normalization, it independently tracks a rolling percent-history per limit `kind` to project an ETA to 100%, shells out to the `ccusage` CLI (best-effort, silently omitted if not installed) for cost/burn-rate/spend breakdown, and renders CPU/RAM usage bars and an LED-style clock — none of that lives in `usage.html`.

### `dyson.html`
Content-only static page — the odd one out: **no JS at all and no CDN requests** (system font stack, inline `<style>`, zero external assets), so it renders identically offline. It also does not share the site's dark `--bg`/`--cyan` tokens; it carries its own light-first palette (`--bg`/`--surface`/`--ink`/`--accent`/`--ok`/`--split`/`--suspect`) redefined under both `@media (prefers-color-scheme: dark)` (guarded `:root:not([data-theme="light"])`) and `:root[data-theme="dark"]`. Layout is plain flex/grid sections — verdict panel, `.duel` two-column tool matrix, `table.matrix` rank grid, `.card` divergence entries, a hallucination table, `.chart` weighted-score bars (widths hard-coded inline as `%` of 5.0), `.paths` cost breakdown, and an `ol.todo` list. Wide tables sit in `.scroll` (`overflow-x: auto`); a single 680px breakpoint collapses `.facts`/`.duel`/`.paths`/`.claim` to one column. A `← 回小工具首頁` link at the top of `.wrap` goes back to `index.html`. Edits here are content edits — keep the chip/impact vocabulary (`chip-ok` / `chip-split` / `chip-suspect`) consistent with what the text claims.

## External Dependencies (CDN only)

All pages except `dyson.html` and `invest.html` (which are fully self-contained) load from CDN — no local dependencies to install:
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
