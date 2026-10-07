---
name: 東京近郊即時影像 · 車站告示系統
description: The trip's live-camera and weather companion as a Japanese railway station, with an LED departure board, 運行情報 panels, white 駅名標 and cameras hung as platform ITV monitors; also the trip itinerary's station edition, read from a 構內圖 of eight platforms.
colors:
  ground: "#e2e1db"
  ground-ink: "#17191c"
  sign: "#fbfbf8"
  sign-ink: "#15171a"
  sign-2: "#41464e"
  sign-rule: "#d3d2cc"
  plate: "#fbfbf8"
  plate-ink: "#15171a"
  plate-2: "#41464e"
  plate-rule: "#d3d2cc"
  plate-soft: "#efeee9"
  navy: "#1c2943"
  navy-ink: "#ffffff"
  exit: "#ffd100"
  exit-ink: "#111111"
  housing: "#0b0c0d"
  housing-2: "#191b1e"
  housing-rule: "#2c2f33"
  housing-ink: "#e9e9e6"
  housing-2ink: "#a9adb3"
  led-off: "#24221f"
  amber: "#ffa526"
  green: "#4fe070"
  red: "#ff4d3d"
  tk: "#80c241"
  ys: "#00a7e3"
  hf: "#f15a22"
  iz: "#00a29a"
  go: "#17703d"
  warn: "#8f5600"
  stop: "#b3261e"
  stop-solid: "#c3261b"
  go-lamp: "#2fbf5a"
  warn-lamp: "#f2a516"
  stop-lamp: "#e53a2c"
  fac: "#26292e"
  fac-ink: "#ffffff"
  ticket: "#e3efe8"
  ticket-rule: "#9cc0aa"
  ticket-ink: "#13261b"
  slab: "#cdccc5"
  tactile: "#f2c200"
  rail: "#6b6f75"
  caution: "#ffe680"
  caution-ink: "#1d1a00"
  focus: "#0a62d0"
typography:
  station-name:
    fontFamily: "'Noto Sans TC', 'PingFang TC', 'Hiragino Sans', 'Microsoft JhengHei', sans-serif"
    fontSize: "30px"
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: ".12em"
  line-head:
    fontFamily: "'Noto Sans TC', 'PingFang TC', 'Hiragino Sans', 'Microsoft JhengHei', sans-serif"
    fontSize: "22px"
    fontWeight: 900
    lineHeight: 1.25
    letterSpacing: ".04em"
  title:
    fontFamily: "'Noto Sans TC', 'PingFang TC', 'Hiragino Sans', 'Microsoft JhengHei', sans-serif"
    fontSize: "19px"
    fontWeight: 900
    lineHeight: 1.25
    letterSpacing: ".02em"
  poster-head:
    fontFamily: "'Noto Sans TC', 'PingFang TC', 'Hiragino Sans', 'Microsoft JhengHei', sans-serif"
    fontSize: "14px"
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: ".06em"
  body:
    fontFamily: "'Noto Sans TC', 'PingFang TC', 'Hiragino Sans', 'Microsoft JhengHei', sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.65
  caption:
    fontFamily: "'Noto Sans TC', 'PingFang TC', 'Hiragino Sans', 'Microsoft JhengHei', sans-serif"
    fontSize: "14px"
    fontWeight: 700
    lineHeight: 1.4
  small:
    fontFamily: "'Noto Sans TC', 'PingFang TC', 'Hiragino Sans', 'Microsoft JhengHei', sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.45
  romaji:
    fontFamily: "Hind, 'Noto Sans TC', 'PingFang TC', sans-serif"
    fontSize: "14px"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: ".04em"
  figure:
    fontFamily: "Hind, 'Noto Sans TC', 'PingFang TC', sans-serif"
    fontSize: "17px"
    fontWeight: 600
    lineHeight: 1.1
    fontFeature: "'tnum'"
  badge:
    fontFamily: "Hind, 'Noto Sans TC', 'PingFang TC', sans-serif"
    fontSize: "13px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: ".02em"
  eki-day:
    fontFamily: "'Eki TC', 'Eki JP', 'PingFang TC', 'Noto Sans TC', 'Hiragino Sans', sans-serif"
    fontSize: "32px"
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: ".14em"
  facility-head:
    fontFamily: "'Eki TC', 'Eki JP', 'PingFang TC', 'Noto Sans TC', 'Hiragino Sans', sans-serif"
    fontSize: "18px"
    fontWeight: 900
    lineHeight: 1.3
    letterSpacing: ".06em"
  ticket-time:
    fontFamily: "'Eki Latin', 'Eki TC', 'Eki JP', 'PingFang TC', sans-serif"
    fontSize: "24px"
    fontWeight: 700
    lineHeight: 1
rounded:
  hairline: "2px"
  sign: "3px"
  housing: "4px"
  badge-s: "5px"
  badge: "6px"
  badge-l: "8px"
  round: "50%"
spacing:
  gutter: "16px"
  panel-x: "12px"
  panel-y: "10px"
  key-gap: "6px"
  stack: "10px"
  column-gap: "14px"
  column-gap-wide: "18px"
  area: "18px"
  region: "28px"
  bracket: "14px"
components:
  exit-sign:
    backgroundColor: "{colors.exit}"
    textColor: "{colors.exit-ink}"
    rounded: "{rounded.sign}"
    height: "40px"
  departure-board:
    backgroundColor: "{colors.housing}"
    textColor: "{colors.housing-ink}"
    rounded: "{rounded.housing}"
  board-head:
    backgroundColor: "{colors.housing-2}"
    textColor: "{colors.housing-ink}"
    padding: "9px 12px 8px"
  track-plate:
    backgroundColor: "{colors.sign}"
    textColor: "{colors.sign-ink}"
    rounded: "{rounded.sign}"
    height: "50px"
  track-plate-selected:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.navy-ink}"
  poster-head:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.navy-ink}"
    typography: "{typography.poster-head}"
    padding: "8px 12px"
  panel:
    backgroundColor: "{colors.plate}"
    textColor: "{colors.plate-ink}"
    rounded: "{rounded.housing}"
    padding: "10px 12px 12px"
  station-sign:
    backgroundColor: "{colors.sign}"
    textColor: "{colors.sign-ink}"
    typography: "{typography.station-name}"
    rounded: "{rounded.sign}"
    padding: "10px 12px 8px"
  station-badge:
    backgroundColor: "#ffffff"
    textColor: "#111111"
    typography: "{typography.badge}"
    rounded: "{rounded.badge}"
    size: "30px"
  monitor-hood:
    backgroundColor: "{colors.housing-2}"
    rounded: "{rounded.housing}"
  monitor-key:
    backgroundColor: "#2c2f34"
    textColor: "#e9e9e6"
    rounded: "{rounded.sign}"
    width: "38px"
    height: "32px"
  caption-strip:
    backgroundColor: "{colors.plate}"
    textColor: "{colors.plate-ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sign}"
    padding: "7px 10px 9px"
  tool-button:
    textColor: "{colors.plate-ink}"
    rounded: "{rounded.sign}"
    height: "38px"
    padding: "0 11px"
  tool-button-on:
    backgroundColor: "{colors.plate-ink}"
    textColor: "{colors.plate}"
  line-selector:
    backgroundColor: "{colors.housing-2}"
    textColor: "{colors.housing-ink}"
    padding: "8px 16px"
  facility-sign:
    backgroundColor: "{colors.fac}"
    textColor: "{colors.fac-ink}"
    typography: "{typography.facility-head}"
    rounded: "{rounded.housing}"
    padding: "9px 12px"
  facility-tile:
    backgroundColor: "{colors.fac}"
    textColor: "{colors.fac-ink}"
    rounded: "{rounded.sign}"
    padding: "9px 10px 10px"
    height: "76px"
  facility-tile-exit:
    backgroundColor: "{colors.exit}"
    textColor: "{colors.exit-ink}"
  key-button:
    backgroundColor: "{colors.fac}"
    textColor: "{colors.fac-ink}"
    rounded: "{rounded.sign}"
    height: "44px"
    padding: "0 14px"
  key-button-today:
    backgroundColor: "{colors.stop-solid}"
    textColor: "#ffffff"
  platform-slab:
    backgroundColor: "{colors.slab}"
    rounded: "{rounded.hairline}"
    padding: "5px 0"
  platform-row:
    backgroundColor: "{colors.sign}"
    textColor: "{colors.sign-ink}"
    rounded: "{rounded.hairline}"
    padding: "8px 8px 8px 6px"
  ticket:
    backgroundColor: "{colors.ticket}"
    textColor: "{colors.ticket-ink}"
    rounded: "{rounded.housing}"
    height: "76px"
  ticket-time:
    typography: "{typography.ticket-time}"
    width: "84px"
  station-seal:
    textColor: "{colors.stop}"
    rounded: "{rounded.round}"
    size: "50px"
  guide-board-head:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.navy-ink}"
    padding: "7px 14px"
  must-board-head:
    backgroundColor: "{colors.stop-solid}"
    textColor: "#ffffff"
    padding: "7px 14px"
  caution-note:
    backgroundColor: "{colors.caution}"
    textColor: "{colors.caution-ink}"
    rounded: "{rounded.housing}"
    padding: "10px 12px"
  stamp-pad:
    backgroundColor: "{colors.plate-soft}"
    rounded: "6px"
    size: "128px"
---

# Design System: 東京近郊即時影像 · 車站告示系統

> Scope: this system covers `livecam.html` and `trip.html` (the itinerary's station edition, rebuilt in this world). Root `DESIGN.md` now records `trip-v2.html`, the booklet edition, which keeps its own look. The hub keeps `DESIGN-hub.md` and the blackjack pages keep `DESIGN-blackjack.md`. Where a rule or value applies to one page only, the text says so; everything else holds on both.

## Overview

**Creative North Star: "The Station Concourse"**

The page is a Japanese railway station. You walk in through a yellow 出口 sign and reach a black LED departure board (発車標) that shows the day's itinerary in dot-matrix light. Beside it are the station's 運行情報 displays: navy-headed enamel panels that carry the weather, the Fuji lamps, the speed-limit notice and the current picks. Further down the concourse every camera area gets a white 駅名標 standing on its own line. Each sign has a line-colour band, a ringed station-number badge, the name in kana, kanji and romaji, and the previous and next stations. The area's cameras hang below the sign from brackets, like platform ITV monitors.

Everything is signage. Surfaces are flat enamel, painted housing or lit LED. Depth comes from objects hanging and standing (a bracket, a housing, a sign edge), never from soft shadows. Only the LED board moves, and it moves in LED grammar: whole-dot steps, column-by-column wipes, hard on and off. The signs never animate.

Confirmed rejection, from the direction contract: the category default of a dark CCTV wall made of same-size thumbnail cards under a hero. In this world the monitors belong to the station signs; they never form a free-standing grid of cards.

The trip itinerary (`trip.html`) is the same station read from its concourse map (構內圖). Eight days are 1–8番線 on four island platforms with rails, yellow 点字ブロック edges and a grey slab. Lodging, transport, food and the checklist are facilities under charcoal facility signs, named Chinese first with the station term beside them (住宿 · 飯店口, 交通 · みどりの窓口, 美食 · 美食街, 行前準備 · 改札口), so a reader who has never seen a Japanese station still finds them. Each day is a platform under its own 駅名標. Hard commitments are pale green マルス tickets with round red station-stamp seals, and the rest of the plan sits on navy 案内 boards. The LED board carries the trip, the dates, the countdown and, before the trip, the next dated deadline. Pressing the 駅スタンプ is the one non-LED motion. The contract's refusal for that page: a stack of paper sections or a card timeline.

**Key Characteristics:**
- A station's three kinds of signage: an LED board for time-bound plans, navy-headed enamel panels for status, white 駅名標 for places.
- LED text is real dot matrix: GNU Unifont 16-dot bitmaps drawn dot by dot on canvas, with the unlit dots visible.
- Four line colours (TK / YS / HF / IZ) are the page's own grouping and the only chromatic accents on the signs.
- Filled JIS-style pictograms from one inline SVG sprite; no outline icon sets, no emoji.
- Night platform in dark mode: the concourse and panels go dark, the 駅名標 and exit sign stay lit.
- On trip.html the station adds charcoal facility signs, pale green マルス tickets, island platforms with yellow tactile edges, and red ink that only marks a promise.

## Colors

The palette is platform concrete, white enamel and black LED housing. The accents are the safety yellow of the exit sign, navy for guide posters, four line colours and three LED colours.

### Primary
- **Line Colours** (`tk` yellow-green, `ys` sky blue, `hf` orange, `iz` teal): one per region (東京都心 TK, 橫濱・湘南 YS, 箱根・富士 HF, 熱海・伊豆 IZ). A region's colour paints the 6px rule under its line head, the route-diagram track and station rings, the 9px band across each 駅名標 and the ring of its station badges. It is set as `--line` through the `l-tk/ys/hf/iz` class on the region, so every child inherits it.
- **Guide Navy** (`navy`, with `navy-ink` white at 14.5:1): the heads of the 案内 posters (`panel-h`, the day panel head), the selected track plate and the plate border.

### Secondary
- **Exit Yellow** (`exit`, with `exit-ink` at 12.9:1): the 出口 sign that leads home (`index.html`), and the text-selection colour. The sign's EXIT key reverses it: yellow letters on the ink block.
- **LED Amber / Green / Red** (`amber`, `green`, `red`, lit on `housing` at 9.9 / 11.4 / 6.0:1): the only colours an LED may show. On the board, green is for titles and times, amber for route steps and readings, and red for notes, deadlines and a wet day's rain chance. The same three mark the monitor status labels (LIVE green, 夜間 amber, 無畫面 red) and the active countdown (amber before the trip, red 旅行中).
- **Unlit Dot** (`led-off`): the dim cell drawn behind every LED position.
- **Facility Charcoal** (`fac`, with `fac-ink` white at 14.6:1; trip.html): the facility signs that head the map and each chapter, the map's facility tiles, the meal-plate head, the key buttons and the icon tiles of the exit footer. The English term beside a facility heading is `#c9ccd1` (9.1:1). The 出口 tile and the footer head use Exit Yellow instead.
- **マルス Ticket Green** (`ticket`, `ticket-rule`, `ticket-ink` at 13.5:1; trip.html): the commitment ticket. The ground carries a 12px diagonal hairline 地紋 (`#78a58a` at .18), and `ticket-rule` draws the 1px edge and the 2px dashed perforation.
- **Caution Yellow** (`caution`, with `caution-ink` at 14.1:1; trip.html): the caution note, a filled yellow strip with a caution pictogram for things to watch that are not commitments.
- **点字ブロック Yellow** (`tactile`; trip.html): the 8px tactile strip along a platform's outer edge, drawn as a 9×8 SVG tile with a `#c79a00` dot. It is a fill only, never text, and it stays the same at night.

### Tertiary
- **Status Ink** (`go`, `warn`, `stop`; 5.9 / 5.8 / 6.3:1 on `plate`): the text colour of readings on the enamel (`st-go/warn/stop`), wet rain chances, the 攝影 tag and the law's closing line.
- **Status Lamps** (`go-lamp`, `warn-lamp`, `stop-lamp`): the 12px round lamps of the Fuji visibility panel. They are fills only, never text.
- **Promise Red** (`stop-solid`; trip.html): the solid red behind white text (5.8:1) and in outlines: the today outline and 今天 tab on map and day header, the today key and tab, and the must board's 2px border and head. Red text on trip.html (ticket times, seals, must sub-heads) is `stop`. Neither changes meaning in dark mode; `stop-solid` keeps its value. Checked checklist keys fill `go`.

### Neutral
- **Platform Concrete** (`ground`, `theme-color`) with **Concrete Ink** (`ground-ink`, 13.4:1): the page floor, the line heads, the route-diagram labels and the footer rule.
- **Station Sign White** (`sign`) with `sign-ink` (17.3:1), `sign-2` for the sign's sub-line, and `sign-rule` for the sign's 1px edge.
- **Panel Enamel** (`plate`) with `plate-ink`, `plate-2` (9.2:1, secondary lines such as hints, sources and the Japanese caption line), `plate-rule` for the 1px row rules, and `plate-soft` for tool-button hover.
- **Housing Black** (`housing`, the LED board and ticker window), **Housing Charcoal** (`housing-2`, the board head, monitor hoods, brackets and the sticky line selector), `housing-rule` for the board's internal rules, `housing-ink` and `housing-2ink` (7.7:1) for the board's static labels.
- **Platform Slab** (`slab`) and **Rail Steel** (`rail`; trip.html): the island platform's surface (its 番線 label in Hind 11px `plate-2`, 5.9:1) and the rails with sleepers between islands, drawn at .7 opacity. Both are neutral; line colour never reaches them.
- **Focus Blue** (`focus`): the 3px focus outline, 2px offset, on everything.

Local, non-token values live with their objects: the badge and number-plate white `#fff` / `#111`, the monitor keys `#2c2f34` (hover `#3d4148`), the monitor glass `#050607`, and the line-selector button rule `#4a4e55` and separator `#3a3e44`. On trip.html: key hover `#3a3f46`, today-key hover `#9e1d14`, the board's today row `#1d0d0b` and row hover `#16181b`, the parking key `#1d5fb8`, the facility sub-line `#c9ccd1` and meta `#dfe1e4`, the exit-yellow sub-line `#3b3500`, and the stamp ink `#c3261b` (`#ff6a5c` at night).

Dark values for the trip.html tokens: `fac #2c3036`, `ticket #1f2b25`, `ticket-rule #3d5a49`, `ticket-ink #dcebe2`, `slab #2a2c30`, `rail #8a8f96`, `caution #4a3f0a`, `caution-ink #fff1b3`. `fac-ink`, `tactile` and `stop-solid` stay. The page shares `tk_theme` with livecam.html, so one choice themes both.

### Named Rules
**The Signs Stay Lit Rule.** Dark mode is a station at night. `ground`, `plate` and the status inks change, and `navy` lifts to `#2a3a5c`. The 駅名標 (`sign`, which dims only to `#ecebe6`), the exit sign, the badges, the number plates and the LED housing keep their colours. A dark-mode screen still shows white station signs.

**The Three LEDs Rule.** An LED shows amber, green or red and nothing else. Green names (titles, times, cities), amber informs (steps, readings), red warns (notes, deadlines, a wet rain chance). The JS constants `AMB / GRN / RED` and the `LIFT` / `SHADE` tables are keyed by these exact hex values, so a new LED colour needs all three tables updated, not just the CSS token. A dimmed LED (a step that has passed) is the same colour at its SHADE tone (`LED.dim`), never grey: at dot size 2 the shade fills three of the cell's four pixels and the bright pixel stays unlit, because a full shade cell there is nearly as bright as a lit dot.

**The Line Is the Accent Rule.** Line colours appear only as signage geometry: bands, rules, rings and the route track. They never fill a panel or set body text. On trip.html the same holds: the 駅名標 band, the ringed 番線 badges on map, tabs and day headers, the chip ring and the 8px band on a hotel entry. Rails and slabs are neutral steel and concrete.

**The Red Is a Promise Rule.** On trip.html red (`stop` text, `stop-solid` fills, LED red) marks a hard commitment only: a booked / due / opens ticket time, a round station-stamp seal, a must board (red border, red head, 注意), the board's 下一個期限 row (on both pages), livecam's red 次 and a next step's last-two-hours countdown, today (outline, 今天 tab, today key, today board row) and the stamped 到著章. Everything else prints in ink, navy or charcoal. An unconfirmed time (待確認) is not a promise: its ticket stays ink with a dashed ink seal. An option not yet booked is not a must: it sits on a navy board, and only its own deadline prints red.

Days map to lines by place: 橫濱, 江之島 and 鎌倉 are YS (D1, D3, D4), 河口湖 is HF (D2), and 新宿, 銀座, 澀谷 and 成田 are TK (D5–D8). IZ does not occur on trip.html.

## Typography

**Body / Display Font:** Noto Sans TC (Google Fonts, weights 400 / 500 / 700 / 900), falling back to PingFang TC, Hiragino Sans and Microsoft JhengHei
**Latin / Figure Font:** Hind (Google Fonts, weights 500 / 600 / 700), for romaji, station codes, times and temperatures
**LED Face:** GNU Unifont (SIL OFL 1.1), as 8×16 and 16×16 bitmaps inlined in the `LEDG` table. It is never a CSS font.
**trip.html faces (offline):** the same families as inlined WOFF2 subsets, so nothing loads from a font CDN. `'Eki TC'` is Noto Sans TC 400 / 700 for every character on the page plus 900 for heading and station-name characters only. `'Eki JP'` is Noto Sans JP 400 / 700 for the Japanese kanji forms Noto Sans TC lacks (営, 峠, 焼 …). `'Eki Latin'` is Hind 600 / 700. Body stacks are `Eki TC, Eki JP, PingFang TC, Noto Sans TC, …` and figures `Eki Latin, Eki TC, …`. Run `python3 tools/trip-font.py` after any text edit; `--check` lists missing glyphs.

**Character:** the plain, heavy gothic of Japanese wayfinding, with a sturdy humanist Latin for the romaji line and the numbers, and a true bitmap for anything lit.

### Hierarchy
- **Station Name** (900, 30px, 1.15, .12em): the kanji on a 駅名標. Kana above it is 12px at .2em; romaji below is Hind 600, 14px.
- **Line Head** (900, 22px, .04em): a region's name above its 6px line-colour rule.
- **Title** (900, 19px, .02em): the page title in the top bar, followed by a Hind 600 12px romaji subtitle.
- **Poster Head** (700, 14px, .06em): the white heading in a navy 案内 head. The Japanese sign term after it (運行情報, ご案内) is 11px at .12em.
- **Body** (400, 15px, 1.65): the page default; panel paragraphs are 13.5–14px.
- **Caption** (700, 14px; 13.5px below 700px): the camera's Chinese place name on its sign strip, with the place prefix at weight 400. The reason line is 12.5px and the Japanese line is 11px `plate-2` (hidden on phones).
- **Figures** (Hind 600, 17px with tabular numerals): temperatures on the day panel. Area now-temperatures are 20px and road readings 15px.
- **Badge** (Hind 700): the line letters at 9px and the number at 13px (`l` 11 / 19px, `s` 8 / 11px).
- **Platform Station Name** (900, 32px, 1.15, .14em; trip.html): the kanji on a day's 駅名標; kana 12px at .22em, Hind 600 14px romaji. The day's title below the sign is 900 at 23px (26px from 700px).
- **Facility Head** (900, 18px, .06em; trip.html): the heading on a facility sign, with the Hind 600 12px English term beside it. Group heads inside a board are 900 16px; hotel names 900 19px.
- **Ticket Time** (Hind 700, 24px; trip.html): the ticket's time column; a word in place of a time is 16px Eki TC. What is 700 16px, detail 13px. The 番線 badge number is Hind 700 21px (24px on the day header).

### Named Rules
**The Bilingual Sign Rule.** Place names are written the way a station writes them: kana over kanji over romaji on the 駅名標, a romaji line under the next- and previous-station names, and the Japanese sign term set after a poster head. The second language always sits **beside or below** its name in the same object. It never floats above a heading as a label of its own.

**The Lit Text Is Bitmap Rule.** Anything shown on the LED board, the board clocks or the weather ticker is drawn from Unifont bitmaps on canvas, with a screen-reader copy in a `.sr` span next to it. After changing any text the board can show, run `tools/led-glyphs.py`. A character missing from the table is rasterised from the browser font at 16px as a fallback, so it still renders, only less crisply. trip.html carries its own table: run `python3 tools/led-glyphs.py --page trip.html`.

**The LED Is for Boards Rule.** Lit dot matrix appears only on departure boards, the board clocks and the countdown digit (drawn at scale 2). Headings, tickets, tabs and chapter text are never LED. Small status tags printed on black (the facility count, the 今天 tab under the sign) are CSS text like the monitors' LIVE label, not lit dots.

## Layout

One centred column, max 1400px with a 16px gutter. It reads top to bottom like a walk through the station: concourse first, then the platforms.

- **Top bar:** the exit sign, the title and the theme button. Below 700px the title wraps to its own row under the exit sign and theme button, and keys drop to 36px.
- **Top grid:** the board, track plates and day panel (`.trip`), then the 運行情報 column (`.unko`: the now panel, the speed-limit strip, the picks). It is one column below 1100px. From 1100px it is `1.32fr / 1fr` with an 18px gap, the board left and status right. The intro and how-to (`.guide`) repeat that split.
- **Board grid:** every row is a time column of `--tcol` = 40 dots (five half-width glyphs) beside the step column. Title and note rows span both.
- **Track plates:** eight equal columns, 5px gap, 50px high.
- **Day panel:** stacks its weather and camera halves; from 700px they sit side by side with a 1px rule between.
- **Line selector:** a sticky (top 0) charcoal bar that scrolls sideways, ordered 看板 | the three modes | 全部 and the lines, so the modes are in view on a 375px phone. It runs full bleed until 1432px, then becomes a 4px-radius bar inside the column.
- **Platforms:** each region has its line head, route diagram (stations `flex: 1 0 76px`, horizontal scroll), and one area per station. The monitor grid is two columns on phones (gap 12px 10px) and `auto-fill, minmax(250px, 1fr)` from 700px (gap 16px 14px). Picks are one column, three columns between 560 and 1099px, and back to one in the desktop status column. The notes split in two from 900px.
- **LED pitch:** `--led-pitch` is 1.3 CSS px per dot (2 from 1100px), so the board reads larger on desktop without changing its dot count per glyph.
- **First viewport (390px phone):** exit sign and title strip, the full-width board, the D1–D8 plates, then the start of the white day panel with its weather rows.

**trip.html** uses the same 1400px column and 16px gutter.
- **Top bar:** exit sign, title with a Hind romaji line, then the 上一版 v2 / 初版 v1 keys and the theme button. Below 700px the title takes its own row; below 361px the exit sign compacts.
- **Concourse (`.top`):** one column on phones in the order board, map, timetable; below 700px the timetable's LED board folds behind a 48px 「發車時刻表 · 8 天一覽」 summary (the map above already lists the days), and below 480px the concourse map is compact: facility tiles put the pictogram beside the name with the station term underneath (no pictogram below 360px), the seal legend fits one row from about 370px (two rows on narrower phones), and the platforms slim down (one 8px rail per island, 5px tactile strips, no 番線 pair labels, 59px for a one-line row). There is no flights chapter: CX450 / CX451 are D1 and D8 tickets, and `#flight-info` is D1's departure ticket. From 1100px it is `1fr / 1.25fr` with an 18px gap: the hero board and the 時刻表 stack on the left, and the 構內圖 spans both rows on the right, sticky at 12px.
- **Map:** facility tiles three across (two rows, above and below the platforms), then four island platforms, one column on phones and two from 760px. Each island is rails, a slab with two platform rows and the 番線 label between them, and rails again.
- **Line selector:** the same sticky charcoal bar with 44px chips: 目錄 and 日程表, one ringed badge per day followed by its place name (新宿, 銀座 …) and date, the chapters 住宿, 交通, 美食 and 行前準備, and dashed out-links to livecam.html and the older editions. Each chapter chip carries its station term as an 11.5px `housing-2ink` second word; below 700px the second words and the dates hide. The chip lights when its section's top passes 120px.
- **Day platform:** sign, title, then a plate body (14px padding; 18 / 22px from 700px). From 1100px the body is `1fr / .82fr`: tickets span both columns, the plan runs left, and 附錄 slips and the stamp pad sit right.
- **Tickets** stack on phones and sit two across from 900px, as do the dishes in 美食街. Below 480px a ticket regrids so the text gets the width: a 66px tear-off (time 21px) spans both rows, the subject sits beside a 44px seal, and the detail runs full width underneath (`.stub-body` becomes `display: contents`). 飯店口 and みどりの窓口 put their boards two across from 1100px.

## Elevation & Depth

The system has no shadows. Depth is conveyed physically: housings are solid dark blocks, enamel signs sit on concrete with a 1px rule, and monitors hang from a drawn charcoal bracket (a 4×14px post under a 38×4px bar) inside the 14px top padding of each camera. The board's one sense of light is its own lit dots against visible unlit dots.

On trip.html the tactile strip, the rails with sleepers and the ruled memo lines in the footer are hard-stop pattern tiles (an SVG tile or `repeating-linear-gradient` with abrupt stops). They are drawn objects, not shading.

### Shadow Vocabulary
- **Lamp rim** (`box-shadow: inset 0 0 0 1.5px rgba(0,0,0,.25)`): the only `box-shadow` on the page, the rim of a Fuji status lamp. It is a hard inset ring, not a drop shadow.

### Named Rules
**The Hung, Not Lifted Rule.** If an object needs to read as separate from the concourse, mount it: a bracket, a housing edge or a sign rule. Don't use blur shadows, glow or hover lifts. Hover changes are underline, border colour or a flat background swap. On trip.html objects stand instead: platform rows sit on a slab between rails, tickets lie flat with a perforation, chapters stand under a facility sign.

## Shapes

The geometry is industrial and nearly square. Signs, plates, keys and buttons are 3px. Housings, panels and monitors are 4px. Hairline tags and labels are 2px. The station badge is a colour-ringed square with a white face: 30px with a 3px ring at 6px radius (`l` 44px, 4px ring, 8px radius; `s` 26px, 2.5px ring, 5px radius; the `line` variant widens to fit the two letters). Route-diagram stations are 20px white circles with a 4px line ring on a 5px track. Monitors are 16:9 with a 5px charcoal frame (4px top, where the hood meets it). The speed-limit sign is a true regulatory circle: white face, red ring, blue numerals, drawn as an SVG `<symbol>`.

trip.html adds four forms. **Station-stamp seals** are 50px circles (44px in entries, group heads and checklist rows) with a 2.5px ring, set at −10°: solid red for 已預約 / 期限 / a date, dashed red when booking opens later, dashed ink for 還沒訂 and 待確認. Seal words are Chinese (they were 予約済 / 締切 until 2026-10-06), never below 11px, and never wrap. **Tickets** are 4px rectangles split by a 2px dashed perforation. **The stamp pad** is a 128px square with a 2px dashed edge at 6px radius, holding an 88px circle. **The 番線 badge** is a 44px square with a 3px ring at 7px radius (52px, 4px ring, 8px radius on the day header; 28px, 2.5px ring, 5px radius in the line selector). Platform rows and the slab are 2px.

## Components

### Exit Sign (出口)
The way home to `index.html`. It is a 40px (44px on phones, like the version and theme keys beside it) yellow plate at 3px radius: a reversed ink key with 出口 over Hind EXIT, then a left-arrow pictogram and 我的小工具 at 14px / 700. Hover underlines the destination. It sits in the top bar's first slot and nowhere else.

### LED Departure Board (発車標) (signature)
The day's itinerary.
- **Housing:** `housing`, 4px radius, a 1px black edge. The `housing-2` head holds the label (16px 700, with 本日の行程 in `housing-2ink` when it shows today), D-number and date in Hind, the countdown (amber; red and bold during the trip) and two LED clocks labelled 日本 and 台灣. Below are a column header row (時刻 / 行程 plus a car or train pictogram for the day's mode) and a foot linking to the full day in `trip.html`.
- **Today (livecam):** on today's board, in Japan time, the last timed step that has passed and every step above it are drawn at their SHADE tones (the `.sr` twin adds 「，已過」); the title and the ※ note never dim. The first timed step still to come gets a red 次 before its time and, after its text, the time left (還有 N 小時 N 分 / 還有 N 分 / 就是現在) in amber, red within 120 minutes; that row wraps instead of scrolling. With every timed step past there is no marker; other days show neither. Times right-align in their column, which widens from 40 to 56 dots (`--tcol-n`) only while a step is marked. The board refreshes every 30 s and on wake / bfcache return, rebuilding only the rows whose state changed, without a wipe.
- **下一個期限 (livecam, before the trip):** the same row as trip.html's — a 44px link (1px `housing-rule`, 3px radius, hover `#16181b`) between the board head and the column header, label 下一個期限 over 次の締切, a static wrapped LED row (date red, task amber, days left red) linking to `trip.html#ck-<id>`. Its `DUES` list is identical to trip.html's; it reads trip.html's ticks from localStorage `trip-checklist-v1` on the same device and hides when none is left or once the trip starts.
- **Rows:** a green title row; one row per route step, with the time in green, red when it is booked (the step then ends with 「・已預約」 in amber) or a deadline (「…（截止）」); and an optional red ※ note row. Rows align to the top. Board times are Japan time (D1 shows 13:50 台北起飛 with 台灣 12:50 in brackets). The head label is the page's h2 (`.bh-t`). Rows are separated by 1px `#16181a` rules.
- **Dots:** each dot is `dp = round(pitch × devicePixelRatio)` device pixels.
  - At dp ≥ 3 a lit dot fills `dp − max(1, floor(dp/4))` of its cell, leaving a gap.
  - At dp 2 the cell is filled in a dark shade of the LED colour and one bright pixel is lit in a lifted tint, keeping full brightness while the grid still shows.
  - At dp 1 dots are solid.
  - The unlit pattern (`led-off`, `dp − 1` square) is painted under every glyph cell. Wrapped lines are 16 dots high with a 3-dot gap.
- **Scrolling:** only step rows longer than the board scroll, and only from 700px; on phones they wrap (`wrapPhone`) because a moving row on a phone is read in fragments. One shared clock moves every scrolling row 24 dot-columns a second in whole-dot steps, with a 40-column gap before the loop. Rows pause on hover or touch, when off-screen and when the tab is hidden.
- **Wrapping:** titles and notes wrap so a deadline is never half off the board. A segment can be kept whole (`keep`): the time left and a deadline's date and days left never break inside. Breaks fall between glyphs, never inside a run of Latin letters or digits. Latin runs include '-' and '–' (T-CAT, 11:00–11:30 stay whole). No line starts with closing punctuation (；，。、）》」』：！？・) and none ends with opening punctuation (（《「『). The last wrapped line holds at least three visible glyphs (glyphs are pulled down from the line above), and no wrapped line starts with a space — the same rule as trip.html.
- **Day change:** the dots come on column by column from the left, 7 columns per 16ms, each row starting 24ms after the one above.
- **Reduced motion:** nothing scrolls (long rows wrap instead), the wipe is skipped, and the weather section opens as the comparison table instead of the ticker.

### Track Plates
Eight buttons, D1–D8, one per trip day, each with its place (1 橫濱 … 8 成田): on phones two rows of four, 48px tall (D-number and place over the date); from 700px eight across, 62px tall (number, place, date stacked); a white plate with a 1.5px navy border. The pressed day turns navy with white text. Today carries a small red 今天 tab at the top right. Hover darkens the border to `sign-ink`.

### 案内 Panel
The status and guide container: an enamel `plate` body, 4px radius, `overflow: hidden`, under a navy head (8px 12px; heading 14px 700, optional Japanese sign term at .8 opacity, optional right-hand note or tool). The body is 10px 12px 12px. Lists inside are separated by 1px `plate-rule` lines with no boxes or cards inside panels. The day panel (D# 這天的天氣與攝影機) uses the same head. Its weather rows are area, a 28px wear pictogram, Hind temperatures and the rain chance (`stop` at ≥ 50 %), with the conditions line in `plate-2`. Until the day is inside the 16-day forecast the rows show 「11 月平年（不是預報）」 instead: JMA November normals (mostly 1991–2020; 成田 2003–2020, 辻堂 1992–2020), mean max / min per area (the `NORMALS` table, each row naming its station; 箱根's station measures rain only, so it has no value), wear advice from those, and an 11.5px 700 `plate-2` 平年 tag (1px `plate-rule`, 2px radius) where the rain chance would be; the hint names the date the forecast takes over. Today's readings are never presented as a trip day's weather. 看完整行程 and the camera rows are 44px.

### Weather Ticker
A `.wx-state` line (info pictogram, message, a 44px 重試 key) above it reports loading, nothing available, 「顯示上次更新 HH:MM 的資料」 from the cache (localStorage `tk_wx_v1`; "current" readings older than three hours are dropped), or saved data that does not reach today. The 帶什麼 tool and pack list sit outside the weather block, so they stay reachable offline; 展開比較 and 富士山看得到嗎 hide when there is no data. Then a `housing` window (3px radius, 7px 10px) inside the now panel holding one scrolling LED row: city in green, reading in amber, a wet rain chance in red. 展開比較 swaps it for the `wxgrid` table (`auto-fill, minmax(142px, 1fr)`); the choice persists in localStorage `tk_wxgrid`.

### Fuji Lamps
A three-column list of status lamps (12px round `go/warn/stop-lamp`, inset rim) beside the place name and an 11.5px `plate-2` reading. After dark a clear reading turns warn: 「雲少・天黑看不清」. The lamps are the only source of a Fuji claim anywhere on the page: a pick may say 富士山露臉 only when its own lamp is go, or, for 鎌倉 and 小田原 (no lamp), when most of the six are go.

### Speed-Limit Strip
An enamel strip (10px 12px, 4px radius) with the 46px 30 km/h regulatory sign, the rule in 14.5px 700, its date in 12px `plate-2`, and an underlined 自駕注意事項 link. It switches to driving mode and scrolls to the full law block (110px sign, `stop`-coloured closing line).

### 駅名標 Station Sign (signature)
One per camera area, standing at the top of its cameras.
- **Body:** `sign` white, 3px radius, 1px `sign-rule` edge, laid out in three columns.
  - Left: the large station badge.
  - Centre: kana, kanji (Station Name) and romaji, with an optional `sign-2` sub-line.
  - Right: the area's current temperature in Hind 20px, the conditions, and a reversed 夜間 LED tag (amber on housing) after sunset.
- **Band:** a 9px line-colour band across the full width.
- **Prev / next row:** left and right arrow pictograms with the neighbouring station's name and a 10.5px romaji line (44px tall links), walking the line among the areas currently shown. Hover underlines the name.

### Route Diagram
One per line, above its signs: a 5px line-colour track with a white 4px-ringed station dot per area, the station name at 12.5px and its code (TK01…) in Hind 10px. Each station is a link to its sign, and the row scrolls sideways when it overflows.

### Platform ITV Monitor (signature)
One per camera, hung from a charcoal bracket.
- **Hood:** `housing-2`, 4px top radius. It holds a white number plate (Hind 700 11px, `TK01-1` = line + station + camera index) and two rubber keys (38×32 with a mouse, 44×44 at `(max-width:699px), (pointer:coarse)`; `#2c2f34`, 3px; hover `#3d4148`): a star pictogram for favourite (amber when pressed, persisted in `tk_fav`) and a pin for Google Maps.
- **Screen:** 16:9 dark glass (`#050607`) in a 5px charcoal frame. It shows the live thumbnail and, top left, a black LED status label in Hind 700 11px: 載入中 in `housing-2ink` until the first real frame, then LIVE green, 夜間 amber, 停格 (neutral) when the page is offline, 無畫面 red — including YouTube's 120×90 placeholder, which has its own message (the stream may have stopped). Offline (`navigator.onLine` false, or three failed frames and no success in a round) the root carries `is-offline` and monitors say 目前離線／連上網路後會自動重抓. Picks never include a camera without a picture, and without weather they make no sky claim (「依各地日夜自動挑（天氣取不到）」). A YouTube tag shows bottom right on hover or focus. After sunset a caption bar explains the dark picture.
- **Caption strip:** a separate enamel sign below the housing (5px gap, 3px radius, 1px rule) with the place name (Caption), the reason line and the Japanese line. The whole monitor and strip is one link, and hover underlines the name.

### Line Selector
The sticky charcoal bar of filters. Each button is 44px (padding 0 9px 0 6px, gap 5px on phones), 3px radius, with a 1.5px `#4a4e55` border and an `s` station badge of its line. The pressed button is a white plate with dark text, and hover whitens the border. After a filter change the viewport is placed on purpose, because hiding cameras changes the page height: a line button lands on that line's head just under the bar (or, if that line shows nothing under the current mode, the first shown line or the empty note); turning 自駕・路面 on lands on the road readings; everything else — 全部, the modes, turning a mode off — keeps what is being read (the road readings, a line head or an area, if it is on screen) at the same place while it is still shown, otherwise the first shown line or the empty note. The first key, 看板, scrolls back to the board (and during the trip re-selects today); 1px separators divide it, the modes and the lines; the frame-age note sits at the right in `housing-2ink` and reads 「目前離線・畫面停在 HH:MM」 when offline.

### Tool Button
The enamel panel's control: 44px (padding 0 12px; inside a navy head 44px with −6px vertical margins; an `aria-disabled` state), 3px radius, a 1.5px `plate-ink` border, transparent, 13px, with an optional 15px pictogram. Hover fills `plate-soft`. Expanded (`aria-expanded="true"`) reverses to ink with enamel text. Inside a navy head it takes the head's white, and expanded turns white with navy text. The theme button is the same shape on the concourse in `ground-ink`; it cycles 跟隨系統 → 淺色 → 深色 (persisted in `tk_theme`, applied before first paint).

### Pictograms
One inline SVG sprite of filled JIS-style pictograms on a 24-unit grid (`p-left/right` arrows, car, train, star / star outline, pin, Fuji, road, sun, moon, auto, info, external, grid, bag), used as `<svg class="pg"><use href="#p-…"/></svg>` at 1em in `currentColor`. The wear pictograms (短袖 … 羽絨＋手套帽子, by temperature threshold) are filled garments whose detail lines are cut back out in `plate`; scarf strokes (≥ 1.9) stay in ink.

### Concourse Board and Countdown (trip.html)
The hero board uses the same housing and head as livecam's: 本次旅程 with ご案内 and a Hind year, and the 日本 / 台灣 LED clocks. It has three rows: the trip name and 8天7夜 in green, the dates in amber, and the route in amber, scrolling. The rows wipe in on load, 40ms apart. Below them a `count` window (1px `housing-rule`, 3px radius) holds the countdown digit, drawn at scale 2 with every dot doubled, beside a 15px label and a 13px `housing-2ink` sub-line. Before the trip the digit counts down in red, during the trip it shows the day number in red with a red label, and after the trip it shows 完 in green. Before the trip a 下一個期限 row follows the countdown: a 44px link (1px `housing-rule`, 3px radius, hover `#16181b`) to the checklist row, with the label 下一個期限 over 次の締切 and one LED row that wraps and never scrolls (a promise row keeps its date in view) — the date in red, the task in amber, the days left in red. It names the first deadline in the script's `DUES` list (10/28 Z booking, 11/5 seat selection) that is not marked `done` in the page, not past, and not ticked on this phone, and hides when none is left: the countdown already names 11/07. Key buttons follow below.

### Key Buttons (trip.html)
44px charcoal keys at 3px radius, 14px 700 with an 18px pictogram (日程表, 行前準備 n / 15). Hover is `#3a3f46`. The today key (今天的行程 · N番線) is `stop-solid`, shown only during the trip; the 行前準備 key steps aside from the first day on. After the trip every platform and day chip is marked past.

### 構內圖 Concourse Map (trip.html, signature)
The page's contents under a facility sign (目錄, with 構內圖 · STATION MAP as its term).
- **Facility tiles:** charcoal tiles (min 76px, 3px radius) with a 28px white pictogram tile, the facility name 14px 700 and a 12px sub-line carrying the station term: 行前準備 · 改札口 (with the checklist count in green on black), 交通 · みどりの窓口 (its 租車 · N'EX tail hides below 420px), 日程表 · 時刻表, 美食 · 美食街, 住宿 · 飯店口, and 出口 in exit yellow. Hover underlines the name.
- **Island platforms:** rails, an 8px tactile strip on the outer edge of each platform row, the slab, and two platform rows. Each row is a link: a ringed 番線 badge in the day's line colour, the title 14.5px 700, then the date in Hind and the move pictograms with the night's lodging in 12.5px `sign-2`.
- **States:** today is outlined 3px in `stop-solid` (inset) with a red 今天 tab. Past days dim the badge to .55 and add 「· 已出發」. Hover underlines the title. Titles balance their lines.
- **Legend:** a short 13px block under the platforms: the three seals at 44px with what each means (訂好了, 這個時間前要到、要做完, 還要訂), and a sentence saying the 到著章 at the foot of each day is tapped to stamp.

### 發車時刻表 Timetable Board (trip.html)
A second LED board inside the 時刻表 chapter. Each of its eight rows links to its day: the date in green in the time column, and the title in amber, wrapping rather than scrolling. Today's row turns both red on a `#1d0d0b` ground. Hover is `#16181b`. Flights follow as tickets in their own chapter.

### Day Platform Header (trip.html, signature)
A 駅名標 per day. The large 番線 badge sits left. Kana, kanji (Platform Station Name) and romaji are centred. The date (Hind 700 21px), the weekday and the mode pictograms with a short label sit right. A 10px line band follows, then the prev / next platforms (44px links) with their 番線 and date (the first points back to 日程表). The day's title follows on the plate. Today outlines the sign 3px red and hangs a 今天 tab in red on housing from its top edge.

### マルス Ticket (trip.html, signature)
One per hard commitment, under 今天的約定. It is a three-column grid (min 76px): the time column (min 84px, Ticket Time) behind the dashed perforation, what and detail, and the seal. The time is red for booked, due and opens; plain items stay ink. A ticket in Taiwan time (D1's 12:50 departure) prints that time and carries its Japan time in `data-jst` for the strip below. A ticket for a place carries an action row under its detail: 44px keys on the plate ground (1px `ticket-rule`, 3px radius, 13.5px 700, a 16px pictogram) — 地圖 (Google Maps), 撥號 (tel:, official numbers only) or 時刻表 (the operator's page) — whose accessible names add the place. On phones the row spans the text columns.

On today's platform an LED strip under the sign, labelled 下一個約定 over 次の約定, shows the next ticket without scrolling (it wraps): time in red when booked or due, subject in amber, then the time left (還有 N 小時 N 分) in amber, turning red in the last two hours; it says 今天的約定都結束了 at the end. Used tickets lose the green ground and the red: plate ground, dashed edge, `plate-2` time and dotted seal, and 「· 已過」 after the subject; their text keeps full contrast because a used ticket can still hold a parking or check-out note. A day with nothing booked shows a 1.5px dashed `plate-rule` note instead. When a booking or deadline changes, update the ticket and the prose that mentions it together.

### 案内 and Must Boards (trip.html)
A board is 1px `plate-rule`, 4px radius, 10px 14px 12px, under a navy head (7px 14px, 14px 700). Lists inside use square 6px bullets separated by 1px rules. A must board has a 2px `stop-solid` border and a red head that starts with 注意 in 900.

### Meal Plate, Lodging Line, Caution Notes (trip.html)
The meal plate is a ruled box under a charcoal head with a 22px white fork tile (用餐). A day states its lodging once: the 宿 ticket (D1 check-in, D2–D5); only D6 and D7, which have no lodging ticket, keep a plain `宿：…` board line. The caution note is a `caution` strip with a pictogram for things to watch that are not commitments; its text sits in one span so the flex row never splits it into columns. D5 carries the leave-by moment that protects its booking (19:10 離開 Sunshine City); on D4 the must board's head carries it (還車 · 16:30–17:00 離開鎌倉，20:00 前還到関内店), so in the plan body the 20:00 return is stated by the ticket and the must board only (the folded slips keep their own timing notes).

### 附錄 Slips (trip.html)
Optional material folds into `details` rows (48px summary, 700 14.5px, a chevron that flips with no transition) between 1px rules, under a 附錄 section rule. The 時間軸估算 slip is the faint variant (400, `plate-2`). The hour-by-hour plans of D2–D5 live there as station timetables; D5's afternoon chain moved out of its prose on 2026-10-06. Other days' prose still cites times in passing (a pick-up, opening hours, a sunset, D8's check-out and flight); a new day should keep its own chain in a slip. A single leave-by moment that protects a booking may stand as a caution note (D5: 19:10 離開 Sunshine City). Print opens all of them.

### 駅スタンプ Pad (trip.html)
A 128px dashed square in `plate-soft` labelled 駅スタンプ on its top edge, with an empty 到著章 circle and an 11px 點一下蓋章 hint. Pressing it lands a red SVG ink stamp at .92 opacity, multiply blend, rotated per day. Every platform has its own stamp, like a real 駅スタンプ: a frame (double circle, rounded square or octagon), the station's landmark in single-ink line and fill (Yokohama the Cosmo Clock wheel, Kawaguchiko Fuji over its reflection, Enoshima the Sea Candle, Kamakura the Great Buddha, Shinjuku the Metropolitan Government towers and a golf flag, Ginza the Wako clock tower, Shibuya Hachikō by the crossing, Narita the flight home), `N番線 · date` on the top, romaji and the station name below. The press takes 0.2s, from +6° and 1.18× scale; it is skipped under reduced motion and persists in `shiori-stamps-v1`.

### Facility Chapters (trip.html)
住宿, 交通, 美食 and 行前準備 (terms 飯店口, みどりの窓口, 美食街, 改札口) each stand under a facility sign (charcoal, 4px top radius, 30px white pictogram tile, Facility Head, Hind term, 13px meta line) above a plate body.
- **Hotel entries:** 1px rule with an 8px top band in the night's line colour (from its chip), the line-ringed chip and nights, a seal, the hotel in 900 19px, and dotted facts.
- **Transport and food groups:** a 1px ruled group under a navy head (900 16px, an optional chip and seal; the seal turns white on navy). Inside, boards lose their frame and become sub-heads.
- **Checklist (行前準備 · 改札口):** fifteen rows in four groups, each under a section rule with its own n / x count: 有期限 (dated, by date), 出發前辦好, 打包, and 當天再看 (read again on the road). Rows sit between 1px rules with a 28px square key (2px ink, 4px radius). A ticked key fills `go` with a white check; the text turns `plate-2` and strikes through, except in 當天再看, where it stays as it is. Dated rows carry a seal. Every row has the anchor `ck-<id>` that the 下一個期限 row links to. Ids are stable for localStorage `trip-checklist-v1`; `d4-timing` was folded into `car-return` on 2026-10-06.

**The One Container Level Rule.** Inside a facility board (a navy-headed `group` in みどりの窓口 or 美食街) nothing draws a second box. An inner 案内 board drops its border and head fill and becomes a bold 14.5px sub-head over a 2px navy rule (red rule and `stop` text for a must board). Hotel entries are the single container of 飯店口, each banded 8px in its line colour.

### 出口 Footer (trip.html)
The back of the station under an exit-yellow facility sign: two phone lists, 緊急求助 (110, 119, the JNTO visitor hotline, the Taipei representative office's Yokohama and Tokyo emergency lines) and 住宿・租車・餐廳・航班 (each night's hotel, the rental shop, the 焼肉 booking, Cathay Pacific Japan), then the link list. Rows are 52px with a 30px charcoal pictogram tile, a 12px `plate-2` note under the name and the number in Hind 700 right. Numbers come from official pages only; Hotel BUSTEL publishes none, so it is not listed. Ruled memo lines every 36px and the colophon in `plate-2` close the page.

## Do's and Don'ts

### Do:
- **Do** put time-bound plans on the LED board, status on navy-headed 案内 panels, and places on white 駅名標. Each kind of information has its own kind of signage.
- **Do** draw every lit character from the Unifont table on canvas with its unlit dots, keep a `.sr` text copy beside it, and re-run `tools/led-glyphs.py` after changing board text.
- **Do** keep LED colours to amber, green and red with their meanings (green names, amber informs, red warns), and update `AMB/GRN/RED`, `LIFT` and `SHADE` together.
- **Do** move LEDs only in whole-dot steps or column wipes, pause scrolling on hover, touch and off-screen, and wrap instead of scrolling under reduced motion.
- **Do** carry a region's line colour through `--line` on its bands, rules, rings and route track, and give every new area a badge code on its line (TK05, YS03…).
- **Do** hang every camera from its bracket with a hood number plate (`LINE` + number + `-` + index) and a separate caption sign strip.
- **Do** keep the 駅名標, exit sign, badges and housings lit in dark mode; only the concourse, panels and status inks change.
- **Do** use the filled pictogram sprite for every icon, at 1em in `currentColor`.
- **Do** put every hard commitment on trip.html on a マルス ticket (time behind the perforation, seal at the right) and update the ticket and the prose that mention it together.
- **Do** head trip.html's chapters with a charcoal facility sign (white pictogram tile, 900 heading, Hind term beside) and keep one container level inside.
- **Do** keep red for promises: booked / due / opens times, seals, must boards and today.
- **Do** rebuild trip.html's inlined faces with `python3 tools/trip-font.py` and its LED table with `python3 tools/led-glyphs.py --page trip.html` after any text edit.
- **Do** draw tactile edges, rails and sleepers as hard-stop patterns (SVG tile, repeating stripes); they are drawn objects, not shading.

### Don't:
- **Don't** lay the cameras out as a free-standing wall of same-size thumbnail cards under a hero; monitors always hang under their station sign.
- **Don't** animate signs, panels or monitors: no fades, slides, hover lifts or easing. Motion belongs to the LED board alone (trip.html's 駅スタンプ press, 0.2s, is the single exception).
- **Don't** add blur shadows, glow or gradients; separation is a bracket, a housing edge or a 1px rule (hard-stop pattern tiles that draw rails, sleepers and ruled memo lines are drawings, not gradients).
- **Don't** set LED text in a CSS web font or invent a fourth LED colour.
- **Don't** fill panels or set body text in line colours, or present TK / YS / HF / IZ as real railway lines.
- **Don't** float the second-language term above a heading as a label; it sits beside or below its name.
- **Don't** use emoji or outline icon sets.
- **Don't** nest a bordered box inside a facility board, or a card inside a ticket.
- **Don't** use red or `stop-solid` for emphasis, hover or decoration on trip.html; it means a commitment.
- **Don't** fill a trip.html platform, ticket or board with a line colour; line colours ring badges and band signs.
