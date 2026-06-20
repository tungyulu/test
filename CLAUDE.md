# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static HTML project with no build system, package manager, or server-side code. All files are standalone HTML pages that open directly in a browser.

## Files

- **`index.html`** — Japan road trip itinerary (東京—熱海—河口湖 秋季紅葉巡航), an 8-day travel schedule rendered as a two-column layout with a sticky sidebar nav and timeline-style day cards.
- **`betting.html`** — Sports betting tracker (世界盃運彩投注紀錄) for parlay/system bets, with combinatorics calculations, real-time profit/loss dashboard, and localStorage persistence.

## Architecture

### `index.html`
Pure static page; no JavaScript logic beyond `lucide.createIcons()`. Layout: fixed sidebar + scrollable main content area. Styling via Tailwind CDN + inline `<style>`. Icons from Lucide CDN.

### `betting.html`
Single-file app with all state, logic, and rendering in one `<script>` block:
- **Storage**: `localStorage` under key `wc-betting-tracker-v1`; `load()`/`save()` handle serialization.
- **Data model**: `tickets[]` array, each ticket has `selections[]` (individual legs) and `groups[]` (parlay configurations with `size`, `stakePer`, optional `manualOdds`).
- **Combinatorics**: `combinations(arr, k)` generates all C(n,k) combos; `computeTicket()` iterates every group's combos to calculate staked/returned/potential amounts. Per-combo payout is rounded to the nearest integer (`Math.round`).
- **Rendering**: `render()` → `renderDashboard()` + `renderTickets()` rebuilds the entire DOM on every state change (no virtual DOM or framework).
- **Form**: Modal-based add/edit flow; `syncGroupCounts()` keeps parlay-size checkboxes in sync with leg count.
- **Import/Export**: JSON and CSV export via `Blob` + `<a>` download; JSON import via `FileReader`.

## External Dependencies (CDN only)

Both pages load from CDN — no local dependencies to install:
- Tailwind CSS (`cdn.tailwindcss.com`)
- Lucide icons (`unpkg.com/lucide@latest`)
- Google Fonts — Noto Sans TC

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan at
`specs/001-yacht-dice-game/plan.md`.
<!-- SPECKIT END -->
