# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static HTML project with no build system, package manager, or server-side code. All files are standalone HTML pages that open directly in a browser.

## Files

- **`index.html`** — Site hub / navigation page (我的小工具). Displays three destination cards linking to the sub-pages below. Served at the GitHub Pages root (`https://tungyulu.github.io/test/`).
- **`trip.html`** — Japan road trip itinerary (東京—熱海—河口湖 秋季紅葉巡航), an 8-day travel schedule rendered as a two-column layout with a sticky sidebar nav and timeline-style day cards.
- **`betting.html`** — Sports betting tracker (世界盃運彩投注紀錄) for parlay/system bets, with combinatorics calculations, real-time profit/loss dashboard, and localStorage persistence.
- **`yacht.html`** — Yacht dice game (快艇骰子), 5-dice 13-category game supporting 1P-vs-CPU and 2P modes with greedy CPU AI and GSAP animations.

## Architecture

### `index.html`
Single-file static hub page. No state, no localStorage. Three `<a class="nav-card">` block links in a `grid grid-cols-1 md:grid-cols-3` layout. GSAP entrance animation (stagger) and hover lift, both guarded via `window.matchMedia` checks for `prefers-reduced-motion` and `(hover: hover) and (pointer: fine)`. Uses `gsap.set` + `gsap.to` (not `gsap.from` or `gsap.matchMedia` object form — the latter fires the callback once per matching condition and causes duplicate tweens).

### `trip.html`
Pure static page; no JavaScript logic beyond `lucide.createIcons()`. Layout: fixed sidebar + scrollable main content area. Styling via Tailwind CDN + inline `<style>`. Icons from Lucide CDN.

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

## External Dependencies (CDN only)

All pages load from CDN — no local dependencies to install:
- Tailwind CSS (`cdn.tailwindcss.com`)
- GSAP 3.12.5 (`cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/`) — core + ScrollTrigger (betting), SplitText (yacht)
- Lucide icons (`unpkg.com/lucide@latest`) — trip, betting
- Google Fonts — Noto Sans TC (all pages)

## GSAP Usage Notes

- **`index.html`**: Use `window.matchMedia().matches` + `gsap.set`/`gsap.to`. Do NOT use `gsap.matchMedia().add(objectForm)` — it fires the callback once per matching condition, causing duplicate stagger tweens.
- **`betting.html`** / **`yacht.html`**: Use `gsap.matchMedia().add(objectForm, cb)` — these pages already do so correctly, reading `ctx.conditions` inside a single callback.

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan at
`specs/002-root-nav-hub/plan.md`.
<!-- SPECKIT END -->
