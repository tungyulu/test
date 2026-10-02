---
name: NBA 拍賣選秀板 · 戰術板
description: A 9-cat fantasy league board run as the coach's magnetic tactics whiteboard, with the model's numbers printed in board blue, names on magnet strips, and the judging done in four dry-erase marker inks.
colors:
  wall: "#34414E"
  board: "#F3F5F4"
  board-2: "#E8EDEE"
  ghost: "rgba(52, 64, 76, .13)"
  print: "#8EA8C3"
  print-2: "#C9D6E2"
  print-ink: "#3D5C7C"
  ink: "#1C2024"
  ink-2: "#44515E"
  m-blue: "#1D52BA"
  m-red: "#C42E28"
  m-green: "#0F7A42"
  m-red-soft: "rgba(196, 46, 40, .10)"
  on-blue: "#FFFFFF"
  strip: "#FFFFFF"
  strip-edge: "#CDD6DF"
  strip-side: "#B8C3CE"
  tape: "#FFFFFF"
  tape-mine: "#FFD84A"
  tape-mine-edge: "#E9BE1F"
  tape-mine-side: "#C9A313"
  mine-tint: "#FFF6CC"
  tape-dark: "#22262A"
  tape-dark-ink: "#F3F5F4"
  paper: "#FFFFFF"
  tape-clear: "rgba(176, 192, 210, .42)"
  alu: "#C3C9CF"
  alu-hi: "#E6E9EC"
  alu-lo: "#8E969E"
  cap: "#2A2E33"
  groove: "rgba(40, 50, 60, .14)"
  pen-body: "#F4F6F7"
  pen-cap: "#23272B"
  pen-cap-blue: "#0E2C66"
  rail-green: "#095A30"
  rail-red: "#9A1F1A"
  tile-3: "#1D52BA"
  tile-2: "#7EA4E4"
  tile-1: "#C9D8F4"
  tile-0: "#E3E8EB"
  tile-n1: "#F4CDC9"
  tile-n2: "#E5867E"
  tile-n3: "#C42E28"
  tile-ink-blue: "#10223F"
  tile-ink-red-1: "#3D1311"
  tile-ink-red-2: "#2B0B09"
  select: "rgba(255, 216, 74, .6)"
typography:
  title:
    fontFamily: "'Noto Sans TC', system-ui, -apple-system, 'PingFang TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "19px"
    fontWeight: 900
    lineHeight: 1.3
    letterSpacing: ".02em"
  tape:
    fontFamily: "'Noto Sans TC', system-ui, -apple-system, 'PingFang TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "17px"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: ".02em"
  body:
    fontFamily: "'Noto Sans TC', system-ui, -apple-system, 'Segoe UI', 'PingFang TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.55
  note:
    fontFamily: "'Noto Sans TC', system-ui, -apple-system, 'PingFang TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "12.5px"
    fontWeight: 400
    lineHeight: 1.5
  printed-label:
    fontFamily: "'Noto Sans TC', system-ui, -apple-system, 'PingFang TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "13.5px"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: ".03em"
  column-head:
    fontFamily: "'Noto Sans TC', system-ui, -apple-system, 'PingFang TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "12px"
    fontWeight: 700
    lineHeight: 1.2
  print-number-lg:
    fontFamily: "'Sofia Sans Condensed', 'Barlow Condensed', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "28px"
    fontWeight: 800
    lineHeight: 1
    fontFeature: "'tnum'"
  print-number:
    fontFamily: "'Sofia Sans Condensed', 'Barlow Condensed', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "21px"
    fontWeight: 800
    lineHeight: 1
    fontFeature: "'tnum'"
  print-label-latin:
    fontFamily: "'Sofia Sans Condensed', 'Barlow Condensed', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "11.5px"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: ".03em"
  tile-number:
    fontFamily: "'Sofia Sans Condensed', 'Barlow Condensed', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 700
    lineHeight: 1
    fontFeature: "'tnum'"
  marker-record:
    fontFamily: "'Kalam', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "66px"
    fontWeight: 700
    lineHeight: 1.08
  marker-rank:
    fontFamily: "'Kalam', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "52px"
    fontWeight: 700
    lineHeight: 1.12
  marker-verdict:
    fontFamily: "'Kalam', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "42px"
    fontWeight: 700
    lineHeight: 1
  marker-money:
    fontFamily: "'Kalam', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "32px"
    fontWeight: 700
    lineHeight: 1.15
  marker-cell:
    fontFamily: "'Kalam', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "24px"
    fontWeight: 700
    lineHeight: 1
rounded:
  tape: "2px"
  check: "3px"
  magnet: "4px"
  trade-strip: "5px"
  key: "6px"
  grid: "7px"
  rail: "8px"
  pen: "999px 4px 4px 999px"
  pill: "999px"
  round: "50%"
spacing:
  gut-phone: "14px"
  gut-tablet: "24px"
  gut-desktop: "28px"
  rail-w-phone: "5px"
  rail-w: "12px"
  zone-pad: "18px 14px 24px"
  row-pad: "9px 12px"
  row-pad-phone: "6px 10px 7px"
  tile-gap: "3px"
  strip-gap: "6px"
components:
  key:
    backgroundColor: "{colors.strip}"
    textColor: "{colors.ink}"
    rounded: "{rounded.key}"
    padding: "5px 13px"
    height: "36px"
  key-solid:
    backgroundColor: "{colors.m-blue}"
    textColor: "{colors.on-blue}"
    rounded: "{rounded.key}"
    padding: "5px 13px"
    height: "36px"
  key-warn:
    backgroundColor: "{colors.m-red-soft}"
    textColor: "{colors.m-red}"
    rounded: "{rounded.key}"
    padding: "5px 13px"
    height: "36px"
  key-rail:
    backgroundColor: "{colors.alu-hi}"
    textColor: "{colors.ink}"
    rounded: "{rounded.key}"
    padding: "3px 11px"
    height: "32px"
  magnet-strip:
    backgroundColor: "{colors.strip}"
    textColor: "{colors.ink}"
    rounded: "{rounded.magnet}"
    padding: "2px 9px 1px"
  magnet-strip-mine:
    backgroundColor: "{colors.tape-mine}"
    textColor: "{colors.ink}"
    rounded: "{rounded.magnet}"
    padding: "2px 9px 1px"
  trade-strip:
    backgroundColor: "{colors.strip}"
    textColor: "{colors.ink}"
    rounded: "{rounded.trade-strip}"
    padding: "6px 10px 5px 9px"
  label-tape:
    backgroundColor: "{colors.tape}"
    textColor: "{colors.ink}"
    typography: "{typography.tape}"
    rounded: "{rounded.tape}"
    padding: "4px 11px 3px"
  label-tape-mine:
    backgroundColor: "{colors.tape-mine}"
    textColor: "{colors.ink}"
    typography: "{typography.tape}"
    rounded: "{rounded.tape}"
    padding: "4px 11px 3px"
  chip:
    backgroundColor: "{colors.strip}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "3px 12px"
    height: "32px"
  chip-pressed:
    backgroundColor: "{colors.m-blue}"
    textColor: "{colors.on-blue}"
    rounded: "{rounded.pill}"
  chip-punt-pressed:
    backgroundColor: "{colors.m-red-soft}"
    textColor: "{colors.m-red}"
    rounded: "{rounded.pill}"
  cat-tile:
    backgroundColor: "{colors.tile-0}"
    textColor: "{colors.ink}"
    typography: "{typography.tile-number}"
    rounded: "{rounded.magnet}"
    height: "34px"
  cat-tile-strong:
    backgroundColor: "{colors.tile-3}"
    textColor: "{colors.on-blue}"
    rounded: "{rounded.magnet}"
  cat-tile-weak:
    backgroundColor: "{colors.tile-n3}"
    textColor: "{colors.on-blue}"
    rounded: "{rounded.magnet}"
  marker-pen:
    backgroundColor: "{colors.pen-body}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pen}"
    padding: "3px 22px 3px 13px"
    height: "32px"
  marker-pen-primary:
    backgroundColor: "{colors.m-blue}"
    textColor: "{colors.on-blue}"
    rounded: "{rounded.pen}"
    padding: "3px 22px 3px 13px"
    height: "32px"
  field:
    backgroundColor: "{colors.strip}"
    textColor: "{colors.ink}"
    rounded: "{rounded.key}"
    padding: "5px 10px"
    height: "36px"
  tooltip:
    backgroundColor: "{colors.tape-dark}"
    textColor: "{colors.tape-dark-ink}"
    rounded: "{rounded.check}"
    padding: "7px 10px"
    width: "240px"
  taped-sheet:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.tape}"
    padding: "26px 24px 20px"
---

# Design System: NBA 拍賣選秀板 · 戰術板

> Scope: `nba-auction.html` (the NBA fantasy board) only. This world is separate from root `DESIGN.md` (trip booklet), `DESIGN-hub.md` (site hub), `DESIGN-livecam.md` (station), `DESIGN-blackjack.md` (pocket LCD) and `DESIGN-yacht.md` (regatta).

## Overview

**Creative North Star: "The Coach's Tactics Board"**

The page is the manager's locker-room tactics whiteboard. Cool white melamine sits in an aluminium frame: side rails at every width, black corner caps at the top and at the ends of the marker tray, and at very wide screens the whole board hangs on a locker-room wall. The model's numbers are printed on the board in board blue: ruled grids, column heads, a faint court behind the trade magnets. Every player and team name sits on a flat magnet strip with a visible thickness edge, and headings are laminated label tape. The coach's dry-erase marker does the judging: a circled rank, the week's win–loss written large, the money in green or red, red rings around weak category ranks, blue ticks on strong ones, a drawn double arrow between traded magnets. A faint, half-erased old play shows behind my board.

Density is a working board, not a dashboard. The wall of about 240 players and the 14-team league board are ruled rails with one row per name, and every column is printed once at the top. Night is the black glass board with liquid-chalk inks; the material stays the same and only the surfaces and inks change.

Confirmed rejections, from the direction contract: the category default of a dark sports-analytics dashboard (KPI tiles, neon accents, player headshots), and its opposite, a plain white spreadsheet.

**Key Characteristics:**
- Melamine board in an aluminium frame with black corner caps, at every width; a sticky marker tray at the bottom holds the jump links as marker pens.
- Printed parts are board-blue lines with no fill; names are magnet strips; headings are label tape (yellow for my team).
- Four marker inks only: black, blue (strong), red (weak or losing), green (money or winning).
- Category ranks and per-player heat are square magnet tiles on a blue-to-red scale.
- Noto Sans TC for all Chinese, Sofia Sans Condensed with tabular figures for printed numbers, Kalam for the marker's digits and Latin only.
- Motion is lifting, snapping and marker strokes; all of it is static under reduced motion.

## Colors

A whiteboard palette: one cool melamine surface, board-blue print, aluminium hardware, four marker inks, and a yellow tape that marks what is mine.

### Primary
- **Marker Blue** (`m-blue`): the strong ink. Blue ticks on top-3 ranks, the blue ring around a top-3 rank in the tally, rookie and 2026-class tags, the punt hint, and the system's one action colour: the 交易 primary pen, solid keys (確定, 我買的), pressed chips and segment buttons, checked trade strips, a grade S badge, the focus ring and the input caret. Text on it is `on-blue`.

### Secondary
- **Marker Red** (`m-red`): weak or losing. Rings around weak category ranks, the bottom-3 tally ring, the 要補 coach line, losing money, 易溢價 and risk tags (risk dashed), punted chips (struck through on `m-red-soft`), warn keys, roster removal hover, validation errors.
- **Marker Green** (`m-green`): money and winning. The weekly $ and season estimate when positive, a winning trade verdict, pickup gains, 值得搶 tags and 自由球員 owners. On the aluminium tray the green and red readouts use the darker `rail-green` / `rail-red`.

### Tertiary
- **Mine Yellow** (`tape-mine`, with `tape-mine-edge` and the thickness edge `tape-mine-side`): my team's label tape, my magnets in the wall, roster and league board, and the 我的 owner tag. **Mine Tint** (`mine-tint`) fills my rows in the wall and a roster row whose magnet just snapped in. `select` is the same yellow at .6 for text selection.

### Neutral
- **Melamine** (`board`) is the page and board surface; **Melamine 2** (`board-2`) is row hover, low-value rows and the cat-cell hover. **Ghost** (`ghost`) strokes the erased plays.
- **Board Print**: `print` is every printed rule that frames (grids, rail borders, column heads, the court at .5 opacity, checkbox borders, scrollbar thumbs); `print-2` is the 1px rules between rows and zones; `print-ink` is printed small text (heads, labels, rank numbers, `/14`).
- **Marker Black** (`ink`) is body text, the neutral ring and the trade arrow; **Ink 2** (`ink-2`) is secondary text and notes.
- **Magnet** (`strip`, `strip-edge`, and the thickness edge `strip-side`) for strips, keys, chips, fields and round magnets. **Label Tape** (`tape`) for headings. **Black Tape** (`tape-dark` / `tape-dark-ink`) for tooltips. **Paper** (`paper`) and **Clear Tape** (`tape-clear`) for the method sheet taped to the board.
- **Aluminium** (`alu`, `alu-hi`, `alu-lo`) for the top rail, side rails and tray; **Corner Cap** (`cap`) for the caps; the tray's pen groove is `groove`, pens are `pen-body` with a `pen-cap` (blue pen: `pen-cap-blue`). **Wall** (`wall`) only shows beyond 1520px.
- **Category Tiles**: `tile-3`, `tile-2`, `tile-1` (strong to mildly strong), `tile-0` (neutral), `tile-n1`, `tile-n2`, `tile-n3` (mildly weak to weak). Tile text is `on-blue` on the two ends, `tile-ink-blue` on the light blues, `tile-ink-red-1` / `tile-ink-red-2` on the light reds, `ink` on neutral.

### Night board
Under `prefers-color-scheme: dark` (unless the 白板 switch is set) or the 黑板 switch, the board becomes black glass and the inks become liquid chalk: board `#17191C`, board-2 `#202328`, print `#3F5D7D`, print-2 `#2C3846`, print-ink `#8FB0D2`, ink `#EEF0EC`, ink-2 `#B4BEC8`, blue `#7DB4FF`, red `#FF8077`, green `#64DB9B`, on-blue `#0B1A33`, strip `#262A2F` with a near-black thickness edge, aluminium `#4A5158` / `#646C74` / `#31363C`, caps `#0F1113`. Label tape stays light (`#E6E9EB`, mine `#E9C33A`) with dark tape ink, and the tooltip turns to light tape. The tile scale reverses its depth (`#7DB4FF` … `#2A2E33` … `#FF8077`). The choice persists in localStorage `nba-auction-theme` and is applied before first paint.

### Named Rules
**The Four Inks Rule.** Anything handwritten or judged is one of four marker inks: black (neutral), blue (strong), red (weak or losing), green (money or winning). There is no fifth ink, no neon, and no other accent; yellow is tape, never ink.

**The Printed Board Rule.** Printed parts (the tally, the nine-rank grid, the trade result box, printed headings, column heads, the court) are `print` lines with no fill. Never turn them into filled cards.

**The Yellow Is Mine Rule.** Yellow tape, yellow magnets and the yellow tint belong to my team only.

## Typography

**Chinese:** Noto Sans TC 400 / 500 / 700 / 900 (`--sans`), for every Chinese character, printed or not.
**Printed numerals and labels:** Sofia Sans Condensed 500–800 (`--print-face`), always with tabular figures.
**Marker hand:** Kalam 700 (`--marker-face`), digits and Latin only.

**Character:** a solid printed Chinese sans and a narrow printed numeral face for what the board says, and one loose marker hand for what the coach writes over it.

### Hierarchy
- **Title** (Noto 900, 19px; 22px ≥760px) on label tape in the top rail. Zone headings are **Tape** (Noto 700, 17px).
- **Marker tally:** rank **#n** (Kalam 52px, ringed) next to a printed `/14` (Sofia 700 22px, `print-ink`), the week's **W–L** largest (Kalam 66px), then **$/週** (Kalam 32px, green or red) and one printed line (Noto 500 13.5px with Sofia 800 15.5px figures). Below a 460px container: 40 / 18 / 50 / 28px.
- **Marker cell** (Kalam 24px) for the nine rank numbers on my board; **Marker verdict** (Kalam 42px, with a 19px category delta) for the trade.
- **Print numbers:** wall price (Sofia 800 28px; 24px on phones), index (800 24px), rank numbers in the wall and the league (800 21px, `print-ink`), W–L on the league board (800 21px), roster figures (600–800 14–16px), tile numbers (700 14px).
- **Printed labels:** `.ph` printed headings (Noto 700 13.5px, `print-ink`, over a 1.5px `print` rule), column heads (Noto 700 12px), Latin category heads (Sofia 700 11.5px, .03em).
- **Body** (Noto 15px / 1.55); notes and sub-lines 12.5–13.5px in `ink-2`; zone notes max 72ch.

### Named Rules
**The No Chinese Handwriting Rule.** Kalam writes digits, `#`, `$`, `+ −` and Latin only. No Traditional Chinese marker face exists, so Chinese is always Noto Sans TC, even inside a marker line (週 in `+$142/週` falls back to Noto).

**The Tabular Print Rule.** Every printed number is Sofia Sans Condensed with `tabular-nums`, so columns of figures line up.

## Layout

The page is one board (`.frame`, max 1480px) with the aluminium top rail, a stack of zones divided by 1.5px `print-2` rules, and the sticky marker tray at the bottom. Gutters are 14px, 24px ≥760px and 28px ≥1100px; the side rails are 5px on phones and 12px ≥760px.

- **Top grid:** on phones my board → league board → 我碰到各隊 → my roster, in one column. At ≥1100px my board and roster form the left column (`minmax(400px, 5fr)`) and the league board with 我碰到各隊 under it the right (`7fr`), split by a `print-2` rule. In auction mode the right column is hidden and the grid is one column.
- **Then** 交易試算 → the player wall (controls, wall, side column of rookies and auction boxes; the side is 288px and sticky at ≥1360px) → the taped method sheet (max 1040px).
- **Player wall:** a sticky printed column head and the rows share one grid of fixed tracks: rank 34px, name `minmax(0, 1fr)`, price 80px, index 56px, heat 294px (nine 30px tiles), team 210px. Below a 980px container the heat moves to a third row (tiles up to 54px). At ≤640px: name + price → tags + note → heat → index, owner, draft $ and key; the heat labels then live only in the sticky head. The team column is the owner over the draft price, right-aligned, beside the key.
- **League board:** rank 26px, name strip `minmax(214px, 1fr)`, W–L 88px, nine rank tiles `minmax(210px, 252px)`, money 80px, chevron 18px. Below a 720px container the tiles drop to their own row with visible labels and the head is hidden. An opened team shows its roster in one, two (≥480px) or three (≥760px) ruled columns.
- **Trade board:** pick → give / get → result in two columns; at ≥1040px give, a round swap magnet, get and the result side by side over the printed court; ≤600px one column with 300px scroll lists.
- **Containers, not viewports,** drive every inner change (`me`, `lg`, `vs`, `roster`, `tr`, `pl`).

### Named Rules
**The Fixed Track Rule.** Every row of the wall is its own grid, so every track is a fixed width except the single `minmax(0, 1fr)` name track. Never use `auto` tracks there; they would size per row and break the column alignment.

**The Ruled Rail Rule.** The wall, my roster and the league rosters are ruled rails: one bordered list with 1px `print-2` rules between rows and no gaps. Never split them into separate cards.

## Elevation & Depth

Depth is physical and shallow. The board and every printed part are flat. Objects stuck on the board have a real, small thickness: magnets cast a tight two-layer shadow and show a 2.5px darker bottom edge, a picked magnet lifts with a longer shadow, label tape and the taped sheet sit just above the surface, and category tiles carry a 2px inset bottom edge. The aluminium rail and tray are the only gradients (brushed metal), plus the faint laminate sheen on label tape; the tray casts a shadow up onto the board. Beyond 1520px the frame casts a shadow on the wall.

### Shadow Vocabulary
- **Magnet at rest** (`0 1px 1px rgba(28, 40, 52, .16), 0 2px 5px rgba(28, 40, 52, .07)`): strips, keys, chips, round magnets, segment control.
- **Magnet lifted** (`0 3px 4px rgba(28, 40, 52, .18), 0 10px 18px rgba(28, 40, 52, .15)`): hover on keys, chips and strips; a checked trade strip; the lift and snap keyframes.
- **Tape** (`0 1px 1px rgba(20, 30, 40, .24), 0 2px 6px rgba(20, 30, 40, .09)`): label tape.
- **Tile edge** (`inset 0 -2px 0 rgba(0, 0, 0, .15), 0 1px 1px rgba(20, 30, 40, .12)`): category tiles.
- **Taped sheet** (`0 1px 2px rgba(20, 30, 40, .18), 0 8px 22px rgba(20, 30, 40, .10)`): the method sheet.
- **Tray** (`0 -6px 14px rgba(10, 20, 30, .14)`): the sticky marker tray.
- **Tooltip** (`0 2px 4px rgba(0, 0, 0, .25), 0 8px 18px rgba(0, 0, 0, .18)`): black label tape.

### Named Rules
**The Magnet Thickness Rule.** A name magnet always shows its thickness: a 2.5px `strip-side` bottom edge (`tape-mine-side` on mine). Printed parts never get a shadow or an edge.

## Shapes

Small, near-square corners on things stuck to the board: tape 2px, checkboxes 3px, magnets and tiles 4px, trade strips 5px, keys and fields 6px. Printed frames are softly rounded: the nine-rank grid 7px, rails and the result box 8px. Chips are pills, the swap magnet is a circle, and marker pens are a pill on the left with a squared 13px cap on the right. The corner caps are solid black with one 5px rounded inside corner. Marker marks are seeded hand-drawn SVG paths (rounded caps and joins, 2.2–2.6px): the ring, the tick, the underline under the verdict and the trade lane's double arrow. Each is seeded so a mark keeps its shape until its data changes.

## Components

### Keys and magnets
- **Key** (`key`): a white magnet with a 1px `strip-edge` border and the rest shadow; hover lifts, press drops 1px. **Solid** (`key-solid`) is marker blue for the confirming action; **Warn** (`key-warn`) is red on `m-red-soft`. In the top rail the key is aluminium (`key-rail`), used for the theme switch (自動 / 白板 / 黑板).
- **Chips** (`chip`): pill magnets in Sofia 700 14px. Pressed is marker blue. Punt chips carry a round magnet dot; pressed they turn red, struck through, with a red dot.
- **Fields** (`field`): white inset fields; native selects use the themed chevron image; checkboxes are 19px with a 1.5px `print` border and a blue marker tick when checked. Scroll lists use thin `print` scrollbars.
- **Segment control:** one magnet split by `strip-edge` rules; the pressed segment is blue (auction-only plans).

### Name magnets
A white strip (`magnet-strip`) with the thickness edge, Noto 700, wrapping anywhere for long names. Mine is yellow (`magnet-strip-mine`). Low-value roster rows flatten the magnet onto `board-2` with no shadow. On the league board the name track is at least 214px wide so each team's strip reads on one line.

### Label tape
White laminated tape (`label-tape`) for every zone heading and the title; mine is yellow. The tooltip is black tape (max 240px), with a Sofia 800 18px figure on top.

### Category tiles
Square magnets (`cat-tile`), 34px tall (32px in the wall heat, 44px in the trade result), with a hidden or 10px label over the figure. The seven-step scale runs `tile-3` (strongest) to `tile-n3` (weakest). A punted category is an empty dashed `print` outline with the figure struck through. Hover and focus draw a 2px ink outline; tiles, ranks and tier bars open the tooltip.

### My board (the marker tally)
- **Tally:** the circled rank (`ringSVG`, stretched; blue for the top 3, red for the bottom 3, black otherwise), printed `/14`, the W–L largest, then the $/週 in green or red and one printed line with the season estimate.
- **Nine ranks:** a printed grid with 1px `print-2` dividers and Noto 12px heads; a weak rank gets a red ring, a top-3 rank a blue tick. It is redrawn only when the ranks or weak categories change, so the strokes draw once per change.
- **Coach notes:** a marker dash before each line; 要補 in red, 最難打 in black.
- **Ghost play:** a half-erased play (circles, crosses, a dotted run) in `ghost` behind the top right of my board, decoration only.

### League board
Rows are `details` on a ruled rail: printed rank, name magnet, W–L with $/週 under it, nine rank tiles, money and value, chevron (rotates 180° on open). The printed column head sits above on a 1.5px `print` rule.

### Trade board
- **Pick lists:** trade strips (`trade-strip`) with a checkbox, name and value; checked strips lift, rotate −.5° and take a blue border and edge.
- **Result box:** a printed `print` outline. First the **lane**: picked magnets on both sides of the drawn double arrow (tap one to put it back), then the **verdict** (Kalam, green or red, with a drawn underline), before → after lines for both teams, and nine win-rate tiles with their deltas.
- **Court:** printed basketball court lines (`print`, .5 opacity) behind the lists at ≥1040px.
- **Coach's suggestions:** ruled lists with a green marker gain and a 試算 key; a ghost play behind them at ≥900px.

### Navigation (rail and tray)
- **Top rail:** aluminium gradient, back link, title tape, season (Sofia 700 15px, hidden ≤480px), theme key.
- **Marker tray:** sticky at the bottom, aluminium with corner caps at both ends. The readout (rank · W–L · $/週 · weak categories) on the left, then a recessed groove holding three marker pens (聯盟 / 交易 / 球員). 交易 is the blue primary pen. Pens tighten at ≤480px and ≤340px.

### Motion (lift, snap, marker strokes)
- **Marker strokes:** paths draw by `stroke-dashoffset` over .46s `cubic-bezier(.22, .8, .3, 1)`, staggered by a per-mark delay.
- **Lift:** a magnet newly placed on the trade lane lifts in over .22s.
- **Snap:** after 套用 the received players' magnets snap onto my roster over .38s and the row is tinted for 900ms.
- **State transitions:** keys, chips and strips .16s ease-out; the league chevron .2s.
- **Reduced motion:** none of the above runs; marks are shown already drawn and magnets are placed instantly.

The contract asked for 150–250ms; the built marker stroke (.46s) and snap (.38s) run longer, and these values are the record.

## Do's and Don'ts

### Do:
- **Do** keep the aluminium side rails and black corner caps at every width, and the sticky marker tray with 交易 as the one blue primary pen.
- **Do** use only the four marker inks: black, blue for strong, red for weak or losing, green for money or winning.
- **Do** draw printed parts as `print` board-blue lines with no fill.
- **Do** put every player and team name on a magnet strip with its 2.5px thickness edge, yellow for mine.
- **Do** keep the wall, my roster and the league rosters as ruled rails with 1px `print-2` rules and no gaps.
- **Do** give every wall track a fixed width except the one `minmax(0, 1fr)` name track, so columns align across rows.
- **Do** set Chinese in Noto Sans TC, printed numbers in Sofia Sans Condensed with tabular figures, and only digits and Latin in Kalam.
- **Do** keep motion to lifting, snapping and marker strokes, drawn once per data change, and static under reduced motion.

### Don't:
- **Don't** build a dark analytics dashboard of KPI tiles, neon accents or player headshots, or a plain white spreadsheet.
- **Don't** turn printed parts (the tally, the rank grid, the trade result, column heads) into filled cards.
- **Don't** split the wall or rosters into separate cards with gaps between them.
- **Don't** use `auto` grid tracks in the wall rows.
- **Don't** write Chinese in the marker face, or printed figures in Kalam.
- **Don't** add a fifth ink colour, or use yellow for anything that isn't mine.
- **Don't** use gradients anywhere but the aluminium hardware and the label tape's sheen.
