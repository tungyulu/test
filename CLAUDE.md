# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static HTML project with no build system or package manager. All HTML files are standalone pages that open directly in a browser. The only non-page file is `usage-dashboard.js`, a zero-dependency Node.js script (Node 18+) that renders a terminal usage dashboard; it has no local-server mode.

## Files

- **`index.html`** — Site hub / navigation page (我的小工具). Displays seven destination cards linking to the sub-pages below. Served at the GitHub Pages root (`https://tungyulu.github.io/test/`).
- **`trip.html`** — Japan road trip itinerary (關東秋季紅葉巡航: 東京 / 河口湖 / 湘南), an 8-day travel schedule as a tabbed app shell (總覽 / 逐日行程 / 住宿 / 美食 / 交通) with timeline-style day cards inside the itinerary panel.
- **`betting.html`** — Sports betting tracker (世界盃運彩投注紀錄) for parlay/system bets, with combinatorics calculations, real-time profit/loss dashboard, and localStorage persistence.
- **`yacht.html`** — Yacht dice game (快艇骰子), 5-dice 13-category game supporting 1P-vs-CPU and 2P modes with greedy CPU AI and GSAP animations.
- **`usage.html`** — Claude Code usage dashboard (方案額度儀表板) showing `/usage`-style limit bars with auto-refresh. Standalone paste-token direct mode only (no local-server mode).
- **`usage-dashboard.js`** — Node.js CLI that renders usage data as a terminal dashboard (`node usage-dashboard.js`, `--once`, `--interval N`, `--selftest`), enhanced with reset countdowns, a projected time-to-limit estimate, a big LED-style clock, live CPU/RAM bars, and (when the `ccusage` CLI is installed) today's/week's/month's spend with a 7-day sparkline.
- **`dyson.html`** — Static research report (Dyson 選購 — 四家 AI 交叉比對): a cross-comparison of four AI answers about which Dyson vacuum to buy, laid out as verdict panel, rank matrix, divergence cards, hallucination table, weighted-score bars, and a to-verify list. Content-only, no interactivity.
- **`golf.html`** — Golf ball-flight tracker (高爾夫球軌跡追蹤): load a local face-on slow-motion swing video, step frames, set a pixel scale from a known length (club length), mark/auto-track the ball after impact and the club head before impact, fit launch speed + launch angle (ball) and club-head speed + attack angle (club), then run a drag + Magnus flight simulation (carry, apex, time, lateral curve) drawn as side/top charts and overlaid on the video. Video never leaves the browser.
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

### `golf.html`
Single-file app, vanilla JS in one IIFE (state + detection + physics + rendering); GSAP core only for the entrance stagger (guarded `typeof gsap`, page works without it). Fonts from Google Fonts; no Tailwind.
- **Frames**: hidden `<video>` (muted, playsinline) drawn onto an offscreen full-res canvas (`frameCanvas`, `willReadFrequently`), then scaled onto the visible `#view` canvas with overlays. Frame N is reached by seeking `currentTime = (N + 0.5) / playFps` and waiting for `seeked`. Two fps settings: **播放幀率** (`playFps`, used for stepping) and **拍攝幀率** (`captureFps`, used for real time — slow-mo exports play at 30 fps but each frame is 1/240 s). `impactFrame` anchors `k = 0`; if unset, the first ball mark is used.
- **Scale**: two clicks on a known length (club-length presets or custom) → `scale.mPerPx`. Every metric readout requires it.
- **Marks**: `ballPts` / `clubPts` are `Map<absFrame, {x, y, auto}>` in video pixels. Click modes (`scale` / `ball` / `club` / `none`) via `[data-mode]` buttons; switching mode scrolls the canvas back into view if it is off-screen.
- **Auto-tracking** (`autoTrack` → `detectBlob`): frame differencing between consecutive full-frame `ImageData` within a search window around the predicted position (`2·last − before` when two points exist, else `last`), threshold → 4-connected components → filter by area (derived from the ball radius in px) → score = distance to prediction + polarity penalty (auto-detected bright/dark object vs surroundings, or forced via `#polarity`) + size-similarity penalty for the ball. The blob at the previous position (ghost) is excluded. Club mode uses `anchorBottom`: the centroid of the component's bottom band only, so the moving shaft doesn't drag the point up. A step whose displacement is wildly inconsistent with the previous one stops tracking and asks the user to correct by clicking. Marking two consecutive frames manually before auto-tracking is the recommended flow (the follow-through club head competes with the ball in the first frames).
- **Fits**: `fitBall` — least squares `X = vx·t`, `Y = vy·t − ½gt²` through the first tracked point → `v0`, `launch`, `dirSign`, RMS residual. `fitClub` — mean speed over the last ≤3 intervals before impact and attack angle from the last interval; then estimates ball speed / launch / spin from the `CLUBS` table (Trackman tour averages: smash factor, launch, AoA, spin, ball speed) scaled by measured club speed and AoA.
- **Simulation** (`simulate`): RK4 at 5 ms, drag `Cd = 0.20 + 0.50·S`, lift `Cl = 0.14 + 0.80·S` with spin ratio `S = rω/v` capped at 0.35, spin decay τ = 25 s (`AERO`). Calibrated to Driver 71.5 m/s / 11° / 2700 rpm ≈ 260 yd and 7i 53.6 m/s / 16.5° / 7000 rpm ≈ 166 yd. Axes: x downrange, y up, z right; positive spin-axis tilt curves right. Face/path inputs derive axis tilt `(face − path) · 40/(loft+1)` and start direction `0.8·face + 0.2·path`. Output: side/top charts on two canvases, dashed overlay projected onto the video from the first ball mark using the scale, and a real-time rAF flight animation.
- **Persistence**: settings only (fps, scale preset, club, search radius, threshold, polarity) under localStorage `golf-tracker-v1`; marks and video are not persisted. Export: JSON of marks + fits + sim params, PNG of the current canvas.
- `window.__golf` exposes state and the pure functions for testing.

### `dyson.html`
Content-only static page — the odd one out: **no JS at all and no CDN requests** (system font stack, inline `<style>`, zero external assets), so it renders identically offline. It also does not share the site's dark `--bg`/`--cyan` tokens; it carries its own light-first palette (`--bg`/`--surface`/`--ink`/`--accent`/`--ok`/`--split`/`--suspect`) redefined under both `@media (prefers-color-scheme: dark)` (guarded `:root:not([data-theme="light"])`) and `:root[data-theme="dark"]`. Layout is plain flex/grid sections — verdict panel, `.duel` two-column tool matrix, `table.matrix` rank grid, `.card` divergence entries, a hallucination table, `.chart` weighted-score bars (widths hard-coded inline as `%` of 5.0), `.paths` cost breakdown, and an `ol.todo` list. Wide tables sit in `.scroll` (`overflow-x: auto`); a single 680px breakpoint collapses `.facts`/`.duel`/`.paths`/`.claim` to one column. A `← 回小工具首頁` link at the top of `.wrap` goes back to `index.html`. Edits here are content edits — keep the chip/impact vocabulary (`chip-ok` / `chip-split` / `chip-suspect`) consistent with what the text claims.

## External Dependencies (CDN only)

All pages except `dyson.html` and `invest.html` (which are fully self-contained) load from CDN — no local dependencies to install (`golf.html` loads only GSAP core + Google Fonts):
- Tailwind CSS (`cdn.tailwindcss.com`)
- GSAP 3.12.5 (`cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/`) — core + ScrollTrigger (trip, betting), SplitText (yacht); index and golf load core only.
- Lucide icons (`unpkg.com/lucide@latest`) — trip, betting
- Google Fonts — Noto Sans TC (all pages)

## GSAP Usage Notes

- **`index.html`**: Use `window.matchMedia().matches` + `gsap.set`/`gsap.to`. Do NOT use `gsap.matchMedia().add(objectForm)` — it fires the callback once per matching condition, causing duplicate stagger tweens.
- **`trip.html`** / **`betting.html`** / **`yacht.html`** / **`golf.html`**: Use `gsap.matchMedia().add(objectForm, cb)` — these pages already do so correctly, reading `ctx.conditions` inside a single callback.

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan at
`specs/002-root-nav-hub/plan.md`.
<!-- SPECKIT END -->
