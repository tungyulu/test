---
name: NBA 拍賣選秀板 · Fantasy Data App
description: A clean fantasy-sports data app played straight. White modules on a cool grey page, one violet accent for actions and for "mine", every number in a condensed tabular face, judged by colour and plain labels.
colors:
  page: "#F2F3F6"
  panel: "#FFFFFF"
  panel-2: "#F6F7F9"
  panel-3: "#ECEEF2"
  line: "#E3E6EB"
  line-2: "#CFD4DC"
  ink: "#101318"
  ink-2: "#465062"
  ink-3: "#626B7C"
  accent: "#6927DA"
  accent-hover: "#5720BD"
  accent-ink: "#FFFFFF"
  accent-soft: "#F3EEFF"
  accent-line: "#D6C7FB"
  up: "#067647"
  down: "#C01F14"
  up-soft: "#E6F5EC"
  down-soft: "#FDECEA"
  strong: "#1F55C2"
  strong-soft: "#E6EEF9"
  heat-3: "#1F55C2"
  heat-2: "#6E98E6"
  heat-1: "#CBDBF7"
  heat-0: "#ECEEF2"
  heat-n1: "#F7D4D0"
  heat-n2: "#E8857C"
  heat-n3: "#C01F14"
  heat-ink-3: "#FFFFFF"
  heat-ink-2: "#0D1F42"
  heat-ink-1: "#0D1F42"
  heat-ink-0: "#101318"
  heat-ink-n1: "#3D1311"
  heat-ink-n2: "#2B0B09"
  heat-ink-n3: "#FFFFFF"
  dark-page: "#0D0F13"
  dark-panel: "#161920"
  dark-panel-2: "#1C2028"
  dark-panel-3: "#232833"
  dark-line: "#262B35"
  dark-line-2: "#343B47"
  dark-ink: "#EDEFF3"
  dark-ink-2: "#B0B7C3"
  dark-ink-3: "#8F97A6"
  dark-accent: "#B9A2FF"
  dark-accent-hover: "#CDBBFF"
  dark-accent-ink: "#1A0E3D"
  dark-accent-soft: "#241C3C"
  dark-accent-line: "#4A3B7E"
  dark-up: "#4ADE8B"
  dark-down: "#FF7B70"
  dark-strong: "#8DB8FF"
  dark-heat-3: "#7DAEFF"
  dark-heat-2: "#2F5FA6"
  dark-heat-1: "#1F3657"
  dark-heat-0: "#232833"
  dark-heat-n1: "#48231F"
  dark-heat-n2: "#A3433B"
  dark-heat-n3: "#FF7B70"
typography:
  record:
    fontFamily: "'Sofia Sans Condensed', 'Barlow Condensed', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "62px"
    fontWeight: 800
    lineHeight: 0.92
    letterSpacing: "-.01em"
    fontFeature: "tnum"
  verdict:
    fontFamily: "'Sofia Sans Condensed', 'Barlow Condensed', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "46px"
    fontWeight: 800
    lineHeight: 1
    fontFeature: "tnum"
  money:
    fontFamily: "'Sofia Sans Condensed', 'Barlow Condensed', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "36px"
    fontWeight: 800
    lineHeight: 1
    fontFeature: "tnum"
  figure:
    fontFamily: "'Sofia Sans Condensed', 'Barlow Condensed', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "26px"
    fontWeight: 800
    lineHeight: 1
    fontFeature: "tnum"
  figure-sm:
    fontFamily: "'Sofia Sans Condensed', 'Barlow Condensed', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 600
    lineHeight: 1
    fontFeature: "tnum"
  cat-label:
    fontFamily: "'Sofia Sans Condensed', 'Barlow Condensed', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: ".04em"
  app-title:
    fontFamily: "'Noto Sans TC', system-ui, -apple-system, 'PingFang TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "20px"
    fontWeight: 800
    lineHeight: 1.25
    letterSpacing: ".01em"
  panel-title:
    fontFamily: "'Noto Sans TC', system-ui, -apple-system, 'PingFang TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "18px"
    fontWeight: 800
    lineHeight: 1.3
  body:
    fontFamily: "'Noto Sans TC', system-ui, -apple-system, 'PingFang TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.55
  button:
    fontFamily: "'Noto Sans TC', system-ui, -apple-system, 'PingFang TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "14px"
    fontWeight: 600
    lineHeight: 1.2
  column-head:
    fontFamily: "'Noto Sans TC', system-ui, -apple-system, 'PingFang TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "12px"
    fontWeight: 700
    lineHeight: 1.2
  note:
    fontFamily: "'Noto Sans TC', system-ui, -apple-system, 'PingFang TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.55
rounded:
  hairline: "4px"
  tile: "6px"
  small: "8px"
  control: "10px"
  toast: "12px"
  panel: "14px"
  pill: "999px"
spacing:
  gutter-phone: "16px"
  gutter-tablet: "24px"
  gutter-desktop: "32px"
  panel-pad-phone: "16px"
  panel-pad: "20px 22px"
  stack-phone: "16px"
  stack: "20px"
  row-pad: "10px"
  bar-height: "61px"
components:
  panel:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    rounded: "{rounded.panel}"
    padding: "{spacing.panel-pad}"
  button:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.control}"
    padding: "0 16px"
    height: "40px"
  button-hover:
    backgroundColor: "{colors.panel-2}"
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-ink}"
    typography: "{typography.button}"
    rounded: "{rounded.control}"
    padding: "0 16px"
    height: "40px"
  button-primary-hover:
    backgroundColor: "{colors.accent-hover}"
  button-small:
    rounded: "{rounded.small}"
    padding: "0 12px"
    height: "34px"
  button-warn:
    backgroundColor: "{colors.down-soft}"
    textColor: "{colors.down}"
    rounded: "{rounded.control}"
  chip:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink-2}"
    rounded: "{rounded.pill}"
    padding: "0 12px"
    height: "34px"
  chip-selected:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-ink}"
    rounded: "{rounded.pill}"
  chip-punt:
    backgroundColor: "{colors.down-soft}"
    textColor: "{colors.down}"
    rounded: "{rounded.pill}"
  input:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "0 12px"
    height: "40px"
  tag:
    backgroundColor: "{colors.panel-3}"
    textColor: "{colors.ink-2}"
    rounded: "{rounded.pill}"
    padding: "1px 7px"
  tag-target:
    backgroundColor: "{colors.up-soft}"
    textColor: "{colors.up}"
    rounded: "{rounded.pill}"
  tag-over:
    backgroundColor: "{colors.down-soft}"
    textColor: "{colors.down}"
    rounded: "{rounded.pill}"
  badge-mine:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.accent}"
    rounded: "{rounded.pill}"
    padding: "2px 8px"
  rank-pill:
    backgroundColor: "{colors.panel-3}"
    textColor: "{colors.ink-2}"
    rounded: "{rounded.pill}"
    padding: "4px 12px"
  grade-s:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.panel}"
    rounded: "{rounded.tile}"
  grade-a:
    textColor: "{colors.ink}"
    rounded: "{rounded.tile}"
  heat-tile:
    backgroundColor: "{colors.heat-0}"
    textColor: "{colors.heat-ink-0}"
    rounded: "{rounded.tile}"
    height: "30px"
  heat-tile-strong:
    backgroundColor: "{colors.heat-3}"
    textColor: "{colors.heat-ink-3}"
    rounded: "{rounded.tile}"
  heat-tile-weak:
    backgroundColor: "{colors.heat-n3}"
    textColor: "{colors.heat-ink-n3}"
    rounded: "{rounded.tile}"
  nav-key:
    backgroundColor: "{colors.panel-2}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "0 14px"
    height: "44px"
  nav-key-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-ink}"
    rounded: "{rounded.control}"
    height: "44px"
  player-chip:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "6px 8px 6px 10px"
    height: "44px"
  toast:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.panel}"
    rounded: "{rounded.toast}"
    padding: "6px 6px 6px 16px"
---

# Design System: NBA 拍賣選秀板 · Fantasy Data App

## Overview

**Creative North Star: "The Box Score, Played Straight"**

The page is the category-standard fantasy-sports data app at the craft level of Yahoo Fantasy, Sleeper, ESPN Fantasy and Basketball Monster, borrowing none of their branding, logos, colours-as-identity or layouts. There is no metaphor and no costume: white modules on a cool grey page, a near-black ink, one violet accent, and a condensed tabular face for every number. Judgement is carried by colour and plain labels (green / red money with a sign, a blue-to-red diverging scale on the nine categories, 要補 / 前三 labels), never by decoration.

Density is high and orderly. League, roster and player data sit in aligned rows and columns with fixed tracks so numbers compare vertically; nothing the owner checks often hides behind extra taps or nested panels. The dark theme is the same app on a near-black page with charcoal panels and lighter tints, not a different world. Motion is state change only.

The 2026-10-02 owner decision retired the previous tactics-board look; nothing from it (magnets, label tape, marker inks, handwriting face, aluminium chrome) is part of this system.

**Key Characteristics:**
- Cool grey page, white panels with a 1px rule and a faint shadow; charcoal on near-black in dark.
- One violet accent: primary actions, selection, focus and my team.
- Every number in Sofia Sans Condensed with tabular figures; Noto Sans TC for all text.
- Money in green / red with an explicit + / − sign.
- A seven-step blue-to-red diverging scale for category heat and ranks, with the number printed in every tile.
- Aligned rows and columns for all data; a fixed bottom bar on every width.

## Colors

A neutral, cool-grey product palette with a single violet voice, two money colours and one diverging data scale. Light values are on `:root`; dark values (the `dark-*` tokens) are applied under `@media (prefers-color-scheme: dark)` guarded `:root:not([data-theme="light"])` and repeated verbatim under `:root[data-theme="dark"]`.

### Primary
- **Product Violet** (accent; dark: dark-accent): primary buttons (套用這筆交易), the filled 交易 key in the bottom bar, pressed chips and segmented buttons, checked checkboxes, the focus ring and caret, links in the sources line, and my team. Hover deepens to Violet Hover (accent-hover; dark: lighter). Text on it is accent-ink.
- **Violet Wash** (accent-soft, with accent-line as its 1px inset): my team's rows in the league table and player table, checked trade rows, the 我的 badge, a top-3 rank pill, the snapped roster rows after a trade, the bottom readout flash.

### Secondary
- **Win Green** (up, up-soft): money won, positive trade swings, 值得搶 and win tags, the free-agent owner label, the receipt's check icon.
- **Loss Red** (down, down-soft): money lost, negative swings, weak categories (要補), injury-risk outline tag, punted chips (struck through), the destructive warn button, input error borders, storage failure.

### Tertiary
- **Diverging Category Scale** (heat-3 … heat-n3 with matching heat-ink-3 … heat-ink-n3): blue = strong, grey = neutral, red = weak. Used for player heat cells, team profile cells and the league table's rank cells. Each background step has its own text colour so every tile carries a readable number.
- **Strong Blue** (strong): the text colour of a top-3 category rank (前三), rookie-class tags and highlighted punt text in notes.

### Neutral
- **Cool Page** (page): the body background behind the panels.
- **Panel White** (panel): panels, app bar, bottom bar, controls, sticky column heads.
- **Panel Tint** (panel-2): row hover, table heads, secondary nav keys, trade cells.
- **Pill Grey** (panel-3): tags, the season pill, the neutral rank pill, the zero heat step, tier tracks.
- **Hairline** (line) and **Control Rule** (line-2): row dividers and panel borders; control borders and column-head underlines.
- **Ink** (ink), **Slate** (ink-2), **Muted Slate** (ink-3): primary text; secondary text and notes; column heads, ranks and hints. Hierarchy uses all three, each measured at least 4.5:1 on every surface it sits on in both themes (lowest light pair: ink-3 on panel-3, 4.62:1).

### Named Rules
**The One Violet Rule.** Violet means "act here" or "this is mine": primary action, selection, focus, my team. It never colours a grade, a category, money or decoration.

**The Signed Money Rule.** Money is up or down with an explicit + or − in front of the figure; the colour never carries the sign alone.

**The Printed Number Rule.** Every heat or rank tile prints its number. Colour ranks the cell; the number is the data.

**The Ink Grade Rule.** Grades are ink, not accent: S is a solid ink tile with panel-coloured text, A is an ink outline, B–D sit on Pill Grey.

## Typography

**Body Font:** Noto Sans TC (with system-ui, -apple-system, PingFang TC, Microsoft JhengHei)
**Number Font:** Sofia Sans Condensed with tabular figures (with Barlow Condensed, then Noto Sans TC)

**Character:** A plain, legible CJK sans for every word, paired with a condensed, tabular numeral face that lets wide rows of figures align and stay large inside narrow columns. Weights are heavy (700–800) for figures and titles, regular for prose.

### Hierarchy
- **Record** (800, 62px, 0.92; 54px when my-team panel is ≤ 460px): the weekly W–L record in my team panel, the largest thing on the page.
- **Verdict** (800, 46px, 1): the trade's weekly $ verdict.
- **Money** (800, 36px; 32px narrow): my $/week figure.
- **Figure** (800, 26px): player prices, category ranks in my panel; 18–22px for index scores, league ranks and rank-pill numbers.
- **Small figure** (600–800, 14–17px): roster prices and values, trade-cell swings, table numbers.
- **Category label** (700, 11–12px, .03–.04em, number face): PTS / REB / … above tiles and in column heads.
- **App title** (800, 18px; 20px ≥ 760px) and **Panel title** (800, 18px; 22px for my team).
- **Body** (400, 15px, 1.55): base text; names in rows at 14–15px / 700.
- **Button** (600, 14px; 13.5px small).
- **Column head** (700, 12px, ink-3): sticky table heads, roster heads.
- **Note** (400, 12.5–13px, ink-2): panel notes, row notes, legends; panel notes cap at 760px, method text at 75–80ch.

### Named Rules
**The Two Faces Rule.** Noto Sans TC for every word, Sofia Sans Condensed tabular for every number, including the numbers in buttons, pills and the bottom readout. No handwriting, display or script face.

## Layout

Single centred column, max 1440px, with a page gutter of 16px on phones, 24px from 760px and 32px from 1100px. Panels stack with a 16px gap (20px from 760px). Panels pad 16px on phones and 20px / 22px from 760px.

- **Top area:** on phones the order is my team → league table → 我碰到各隊 → my roster. From 1100px it is two columns, my team and roster on the left (min 400px, 5fr) and the league table with 我碰到各隊 on the right (7fr). In auction mode the right column hides and the grid falls back to one column.
- **Trade calculator:** partner picker, then give / get lists side by side with the result below; at a container width ≥ 1040px the result becomes a third column with a left rule; ≤ 600px everything stacks.
- **Player table:** one shared grid for the sticky column head and every row, fixed tracks (34px · 1fr · 80px · 56px · 294px · 210px). Below a 980px container the heat moves to a third grid row; ≤ 640px the row reads name + price → tags + note → heat → index + owner + key. From 1420px a 288px sticky side column holds rookies and auction boxes.
- **Bottom bar:** fixed on every width, 60px tall plus the safe-area inset; the body pads for it, and scroll padding keeps anchors clear of it.
- Panels resize their insides with container queries (my team, league, versus list, roster, trade, result, player table, method).

**The Aligned Rows Rule.** League, roster and player data are rows on one shared grid with fixed tracks and 1px rules between them, never separate cards and never `auto` tracks that size per row.

## Elevation & Depth

Nearly flat. Panels lift off the grey page with a 1px Hairline border and a faint offset shadow; floating layers (toast, tooltip) take a stronger shadow. Inside a panel, depth is only tonal: hover and selection tint rows, they never lift.

### Shadow Vocabulary
- **Panel** (`--shadow-1`; light `0 1px 2px rgba(16,24,40,.05), 0 1px 3px rgba(16,24,40,.06)`, dark `0 1px 2px rgba(0,0,0,.45)`): every panel.
- **Float** (`--shadow-2`; light `0 8px 24px rgba(16,24,40,.14), 0 2px 6px rgba(16,24,40,.08)`, dark `0 10px 28px rgba(0,0,0,.55), 0 2px 6px rgba(0,0,0,.4)`): the undo toast and tooltips.
- **Control** (`--shadow-0`; light `0 1px 2px rgba(16,24,40,.05)`, dark `0 1px 2px rgba(0,0,0,.35)`): standard buttons.
- **Bar** (`--shadow-bar`; light `0 -2px 10px rgba(16,24,40,.06)`, dark `0 -2px 12px rgba(0,0,0,.45)`): the fixed bottom bar's upward edge.

### Named Rules
**The No-Nesting Rule.** A panel never sits inside a panel. Sub-sections inside a panel are separated by a 1px rule and a small heading, not by another bordered, shadowed box.

## Shapes

Softly rounded, product-standard. Panels 14px; buttons, inputs, nav keys and trade player chips 10px; small buttons, tooltips and the 32px desktop remove key 8px; heat / rank tiles, grades, checkboxes and the focus ring 6px; the 要補 / 前三 label 4px; tags, chips, badges and pills fully round (999px). Borders are 1px (1.5px on checkboxes and the A grade outline). The off (punted) heat tile is a dashed 1px outline with a struck-through number. Icons are a small inline SVG sprite on a 24-unit grid, 2px round strokes, drawn at 14–20px.

## Components

### Buttons
- **Shape:** gently rounded (10px; small 8px), 40px tall (small 34px), 44px under `(pointer: coarse)`.
- **Standard:** Panel White with a Control Rule border and the control shadow, ink text, 600 14px; hover Panel Tint, active Pill Grey.
- **Primary:** Product Violet fill and border, accent-ink text; hover Violet Hover. One per decision (套用這筆交易).
- **Warn:** Loss Red wash with a red border and red text, for the two-step destructive confirm.
- **Remove key:** a borderless 44px icon key (32px for a fine pointer in a wide roster row), muted until hover turns it red on a red wash.
- **Focus:** a 2px violet outline, 2px offset, on every focusable element.

### Chips
- **Style:** fully round, 34px (44px coarse), Panel White with a Control Rule border, slate number-face label.
- **State:** pressed = violet fill with accent-ink text; a pressed punt chip = red wash, red border, struck-through label. Segmented controls are the same pressed treatment inside one 10px bordered group.

### Tags and badges
- **Tags:** small round pills (700 11.5px) on Pill Grey; 值得搶 / win in green on its wash, 易溢價 in red on its wash, risk as a red outline, rookie class in Strong Blue on the Strong Wash (`--strong-soft`: light `#E6EEF9`, dark `rgba(141,184,255,.14)`).
- **我的 badge:** Violet Wash with a 1px accent-line inset and violet text; a solid violet 我的 tag marks the owner column in the player table.
- **Rank pill:** 第 n 名 / 14 隊 on Pill Grey with the number in 800 18px ink; top three turns it violet wash, the bottom three red wash.

### Cards / Containers
- **Corner Style:** 14px.
- **Background:** Panel White (dark: charcoal).
- **Shadow Strategy:** the Panel shadow; see Elevation.
- **Border:** 1px Hairline.
- **Internal Padding:** 16px, 20px / 22px from 760px. A title row (800 18px title, optional slate note) and an optional foot separated by a 1px rule.

### Inputs / Fields
- **Style:** 40px (44px coarse), Panel White, 1px Control Rule border, 10px radius, 14px text; selects carry a themed chevron image; search has an inset icon.
- **Focus:** border turns violet plus a 3px violet selection ring; no outline.
- **Error:** `aria-invalid` turns the border red; error messages are red 700.
- **Checkbox:** 20px, 6px radius, 1.5px rule; checked = violet fill with a themed tick.

### Navigation
- **App bar:** Panel White strip with a bottom Hairline, 56px: back link (44px target), the title, the season pill (hidden ≤ 480px), and the theme key cycling 自動 / 淺色 / 深色.
- **Bottom bar:** fixed on every width; a readout link (rank · record · $/week · weak categories in red, in the number face) then 聯盟 / 交易 / 球員 as 44px keys on Panel Tint, 交易 filled violet. Narrow screens drop the weak list and the record before shrinking the keys.

### Category strip and heat tiles
- My team's nine category ranks are a ruled nine-cell strip: number-face label, the rank in 800 26px, and a 要補 (red, on a red wash cell) or 前三 (Strong Blue) label.
- Heat and rank tiles are 6px squares (28–34px tall) on the diverging scale with their own text colour; hover or focus draws a 2px ink outline and opens a tooltip.

### League table
- Expandable rows on one grid: rank, team name (+ 我的 badge), weekly W–L and $/week, nine rank tiles, money detail, chevron. My row is Violet Wash with a violet rank. One tap opens the roster in place as a ruled two- or three-column list (draft price → value). ≤ 720px container the column head becomes sticky and the row wraps to three lines.

### Trade result (signature)
The deal's box score: the moved players as removable 44px player chips on both sides of a swap icon (hover turns their border red), the weekly $ verdict at 46px in green or red with the season figure beside it, a before → after table for both teams, then the nine category swings as headline cells (signed number, the new win rate under it, a green or red wash when the swing is ≥ 5 points). After 套用 it is replaced by a receipt (green check, who went where, before → after of record, money and weak categories) with an undo key, and an ink toast offers undo above the bottom bar.

### Motion
State change only, ≤ 200 ms: background / border / colour transitions at .15s ease-out on keys, chips, rows and summaries; the league chevron rotates in .2s; a new player chip and the toast rise 4–6px in .2s. Under `prefers-reduced-motion` nothing transitions or animates.

## Do's and Don'ts

### Do:
- **Do** keep violet for primary actions, selection, focus and my team only (The One Violet Rule).
- **Do** print every figure in the number face with tabular figures, and every money figure with an explicit + or −, in up / down.
- **Do** print the number inside every heat and rank tile, using that step's own text colour.
- **Do** put league, roster and player data in ruled rows on one shared grid with fixed column tracks.
- **Do** give every key and control a 44px target under `(pointer: coarse)`, and keep the fixed bottom bar on every width.
- **Do** check every new text / surface pair at ≥ 4.5:1 in both themes, and define every new token in all three theme blocks.
- **Do** keep motion to state changes of ≤ 200 ms and none under reduced motion.

### Don't:
- **Don't** reintroduce the retired tactics board or any substitute costume: no magnets, label tape, marker inks, handwriting face, aluminium rails or other metaphor.
- **Don't** borrow Yahoo, ESPN, Sleeper or Basketball Monster branding, logos, colours-as-identity or layouts, and don't add NBA or team logos or player photos.
- **Don't** colour grades or categories with the accent; grades are ink.
- **Don't** nest a panel inside a panel, or split rows of data into separate cards.
- **Don't** use `auto` tracks in the player table's row grid.
- **Don't** let colour alone carry a judgement: weak and strong ranks also carry 要補 / 前三, money carries a sign.
