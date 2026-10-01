---
name: 東京近郊即時影像 · 車站告示系統
description: The trip's live-camera and weather companion as a Japanese railway station, with an LED departure board, 運行情報 panels, white 駅名標 and cameras hung as platform ITV monitors.
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
  go-lamp: "#2fbf5a"
  warn-lamp: "#f2a516"
  stop-lamp: "#e53a2c"
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
---

# Design System: 東京近郊即時影像 · 車站告示系統

> Scope: this system covers `livecam.html` only. It is its own world: `trip.html` keeps root `DESIGN.md`, the hub keeps `DESIGN-hub.md`, the blackjack pages keep `DESIGN-blackjack.md`. The two links between this page and the trip booklet do not carry either look across.

## Overview

**Creative North Star: "The Station Concourse"**

The page is a Japanese railway station. You walk in through a yellow 出口 sign and reach a black LED departure board (発車標) that shows the day's itinerary in dot-matrix light. Beside it are the station's 運行情報 displays: navy-headed enamel panels that carry the weather, the Fuji lamps, the speed-limit notice and the current picks. Further down the concourse every camera area gets a white 駅名標 standing on its own line. Each sign has a line-colour band, a ringed station-number badge, the name in kana, kanji and romaji, and the previous and next stations. The area's cameras hang below the sign from brackets, like platform ITV monitors.

Everything is signage. Surfaces are flat enamel, painted housing or lit LED. Depth comes from objects hanging and standing (a bracket, a housing, a sign edge), never from soft shadows. Only the LED board moves, and it moves in LED grammar: whole-dot steps, column-by-column wipes, hard on and off. The signs never animate.

Confirmed rejection, from the direction contract: the category default of a dark CCTV wall made of same-size thumbnail cards under a hero. In this world the monitors belong to the station signs; they never form a free-standing grid of cards.

**Key Characteristics:**
- A station's three kinds of signage: an LED board for time-bound plans, navy-headed enamel panels for status, white 駅名標 for places.
- LED text is real dot matrix: GNU Unifont 16-dot bitmaps drawn dot by dot on canvas, with the unlit dots visible.
- Four line colours (TK / YS / HF / IZ) are the page's own grouping and the only chromatic accents on the signs.
- Filled JIS-style pictograms from one inline SVG sprite; no outline icon sets, no emoji.
- Night platform in dark mode: the concourse and panels go dark, the 駅名標 and exit sign stay lit.

## Colors

The palette is platform concrete, white enamel and black LED housing. The accents are the safety yellow of the exit sign, navy for guide posters, four line colours and three LED colours.

### Primary
- **Line Colours** (`tk` yellow-green, `ys` sky blue, `hf` orange, `iz` teal): one per region (東京都心 TK, 橫濱・湘南 YS, 箱根・富士 HF, 熱海・伊豆 IZ). A region's colour paints the 6px rule under its line head, the route-diagram track and station rings, the 9px band across each 駅名標 and the ring of its station badges. It is set as `--line` through the `l-tk/ys/hf/iz` class on the region, so every child inherits it.
- **Guide Navy** (`navy`, with `navy-ink` white at 14.5:1): the heads of the 案内 posters (`panel-h`, the day panel head), the selected track plate and the plate border.

### Secondary
- **Exit Yellow** (`exit`, with `exit-ink` at 12.9:1): the 出口 sign that leads home (`index.html`), and the text-selection colour. The sign's EXIT key reverses it: yellow letters on the ink block.
- **LED Amber / Green / Red** (`amber`, `green`, `red`, lit on `housing` at 9.9 / 11.4 / 6.0:1): the only colours an LED may show. On the board, green is for titles and times, amber for route steps and readings, and red for notes, deadlines and a wet day's rain chance. The same three mark the monitor status labels (LIVE green, 夜間 amber, 無畫面 red) and the active countdown (amber before the trip, red 旅行中).
- **Unlit Dot** (`led-off`): the dim cell drawn behind every LED position.

### Tertiary
- **Status Ink** (`go`, `warn`, `stop`; 5.9 / 5.8 / 6.3:1 on `plate`): the text colour of readings on the enamel (`st-go/warn/stop`), wet rain chances, the 攝影 tag and the law's closing line.
- **Status Lamps** (`go-lamp`, `warn-lamp`, `stop-lamp`): the 12px round lamps of the Fuji visibility panel. They are fills only, never text.

### Neutral
- **Platform Concrete** (`ground`, `theme-color`) with **Concrete Ink** (`ground-ink`, 13.4:1): the page floor, the line heads, the route-diagram labels and the footer rule.
- **Station Sign White** (`sign`) with `sign-ink` (17.3:1), `sign-2` for the sign's sub-line, and `sign-rule` for the sign's 1px edge.
- **Panel Enamel** (`plate`) with `plate-ink`, `plate-2` (9.2:1, secondary lines such as hints, sources and the Japanese caption line), `plate-rule` for the 1px row rules, and `plate-soft` for tool-button hover.
- **Housing Black** (`housing`, the LED board and ticker window), **Housing Charcoal** (`housing-2`, the board head, monitor hoods, brackets and the sticky line selector), `housing-rule` for the board's internal rules, `housing-ink` and `housing-2ink` (7.7:1) for the board's static labels.
- **Focus Blue** (`focus`): the 3px focus outline, 2px offset, on everything.

Local, non-token values live with their objects: the badge and number-plate white `#fff` / `#111`, the monitor keys `#2c2f34` (hover `#3d4148`), the monitor glass `#050607`, and the line-selector button rule `#4a4e55` and separator `#3a3e44`.

### Named Rules
**The Signs Stay Lit Rule.** Dark mode is a station at night. `ground`, `plate` and the status inks change, and `navy` lifts to `#2a3a5c`. The 駅名標 (`sign`, which dims only to `#ecebe6`), the exit sign, the badges, the number plates and the LED housing keep their colours. A dark-mode screen still shows white station signs.

**The Three LEDs Rule.** An LED shows amber, green or red and nothing else. Green names (titles, times, cities), amber informs (steps, readings), red warns (notes, deadlines, a wet rain chance). The JS constants `AMB / GRN / RED` and the `LIFT` / `SHADE` tables are keyed by these exact hex values, so a new LED colour needs all three tables updated, not just the CSS token.

**The Line Is the Accent Rule.** Line colours appear only as signage geometry: bands, rules, rings and the route track. They never fill a panel or set body text.

## Typography

**Body / Display Font:** Noto Sans TC (Google Fonts, weights 400 / 500 / 700 / 900), falling back to PingFang TC, Hiragino Sans and Microsoft JhengHei
**Latin / Figure Font:** Hind (Google Fonts, weights 500 / 600 / 700), for romaji, station codes, times and temperatures
**LED Face:** GNU Unifont (SIL OFL 1.1), as 8×16 and 16×16 bitmaps inlined in the `LEDG` table. It is never a CSS font.

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

### Named Rules
**The Bilingual Sign Rule.** Place names are written the way a station writes them: kana over kanji over romaji on the 駅名標, a romaji line under the next- and previous-station names, and the Japanese sign term set after a poster head. The second language always sits **beside or below** its name in the same object. It never floats above a heading as a label of its own.

**The Lit Text Is Bitmap Rule.** Anything shown on the LED board, the board clocks or the weather ticker is drawn from Unifont bitmaps on canvas, with a screen-reader copy in a `.sr` span next to it. After changing any text the board can show, run `tools/led-glyphs.py`. A character missing from the table is rasterised from the browser font at 16px as a fallback, so it still renders, only less crisply.

## Layout

One centred column, max 1400px with a 16px gutter. It reads top to bottom like a walk through the station: concourse first, then the platforms.

- **Top bar:** the exit sign, the title and the theme button. Below 700px the title wraps to its own row under the exit sign and theme button, and keys drop to 36px.
- **Top grid:** the board, track plates and day panel (`.trip`), then the 運行情報 column (`.unko`: the now panel, the speed-limit strip, the picks). It is one column below 1100px. From 1100px it is `1.32fr / 1fr` with an 18px gap, the board left and status right. The intro and how-to (`.guide`) repeat that split.
- **Board grid:** every row is a time column of `--tcol` = 40 dots (five half-width glyphs) beside the step column. Title and note rows span both.
- **Track plates:** eight equal columns, 5px gap, 50px high.
- **Day panel:** stacks its weather and camera halves; from 700px they sit side by side with a 1px rule between.
- **Line selector:** a sticky (top 0) charcoal bar that scrolls sideways. It runs full bleed until 1432px, then becomes a 4px-radius bar inside the column.
- **Platforms:** each region has its line head, route diagram (stations `flex: 1 0 76px`, horizontal scroll), and one area per station. The monitor grid is two columns on phones (gap 12px 10px) and `auto-fill, minmax(250px, 1fr)` from 700px (gap 16px 14px). Picks are one column, three columns between 560 and 1099px, and back to one in the desktop status column. The notes split in two from 900px.
- **LED pitch:** `--led-pitch` is 1.3 CSS px per dot (2 from 1100px), so the board reads larger on desktop without changing its dot count per glyph.
- **First viewport (390px phone):** exit sign and title strip, the full-width board, the D1–D8 plates, then the start of the white day panel with its weather rows.

## Elevation & Depth

The system has no shadows. Depth is conveyed physically: housings are solid dark blocks, enamel signs sit on concrete with a 1px rule, and monitors hang from a drawn charcoal bracket (a 4×14px post under a 38×4px bar) inside the 14px top padding of each camera. The board's one sense of light is its own lit dots against visible unlit dots.

### Shadow Vocabulary
- **Lamp rim** (`box-shadow: inset 0 0 0 1.5px rgba(0,0,0,.25)`): the only `box-shadow` on the page, the rim of a Fuji status lamp. It is a hard inset ring, not a drop shadow.

### Named Rules
**The Hung, Not Lifted Rule.** If an object needs to read as separate from the concourse, mount it: a bracket, a housing edge or a sign rule. Don't use blur shadows, glow or hover lifts. Hover changes are underline, border colour or a flat background swap.

## Shapes

The geometry is industrial and nearly square. Signs, plates, keys and buttons are 3px. Housings, panels and monitors are 4px. Hairline tags and labels are 2px. The station badge is a colour-ringed square with a white face: 30px with a 3px ring at 6px radius (`l` 44px, 4px ring, 8px radius; `s` 26px, 2.5px ring, 5px radius; the `line` variant widens to fit the two letters). Route-diagram stations are 20px white circles with a 4px line ring on a 5px track. Monitors are 16:9 with a 5px charcoal frame (4px top, where the hood meets it). The speed-limit sign is a true regulatory circle: white face, red ring, blue numerals, drawn as an SVG `<symbol>`.

## Components

### Exit Sign (出口)
The way home to `index.html`. It is a 40px (36px on phones) yellow plate at 3px radius: a reversed ink key with 出口 over Hind EXIT, then a left-arrow pictogram and 我的小工具 at 14px / 700. Hover underlines the destination. It sits in the top bar's first slot and nowhere else.

### LED Departure Board (発車標) (signature)
The day's itinerary.
- **Housing:** `housing`, 4px radius, a 1px black edge. The `housing-2` head holds the label (16px 700, with 本日の行程 in `housing-2ink` when it shows today), D-number and date in Hind, the countdown (amber; red and bold during the trip) and two LED clocks labelled 日本 and 台灣. Below are a column header row (時刻 / 行程 plus a car or train pictogram for the day's mode) and a foot linking to the full day in `trip.html`.
- **Rows:** a green title row; one row per route step, with the time in green (red when it is a deadline) and the step in amber; and an optional red ※ note row. Rows are separated by 1px `#16181a` rules.
- **Dots:** each dot is `dp = round(pitch × devicePixelRatio)` device pixels.
  - At dp ≥ 3 a lit dot fills `dp − max(1, floor(dp/4))` of its cell, leaving a gap.
  - At dp 2 the cell is filled in a dark shade of the LED colour and one bright pixel is lit in a lifted tint, keeping full brightness while the grid still shows.
  - At dp 1 dots are solid.
  - The unlit pattern (`led-off`, `dp − 1` square) is painted under every glyph cell. Wrapped lines are 16 dots high with a 3-dot gap.
- **Scrolling:** only step rows longer than the board scroll. One shared clock moves every scrolling row 24 dot-columns a second in whole-dot steps, with a 40-column gap before the loop. Rows pause on hover or touch, when off-screen and when the tab is hidden.
- **Wrapping:** titles and notes wrap so a deadline is never half off the board. Breaks fall between glyphs, never inside a run of Latin letters or digits. No line starts with closing punctuation (；，。、）》」』：！？) and none ends with opening punctuation (（《「『).
- **Day change:** the dots come on column by column from the left, 7 columns per 16ms, each row starting 24ms after the one above.
- **Reduced motion:** nothing scrolls (long rows wrap instead), the wipe is skipped, and the weather section opens as the comparison table instead of the ticker.

### Track Plates
Eight 50px buttons, D1–D8, one per trip day: Hind 700 20px D-number over the 10.5px date, on a white plate with a 1.5px navy border. The pressed day turns navy with white text. Today carries a small red 今天 tab at the top right. Hover darkens the border to `sign-ink`.

### 案内 Panel
The status and guide container: an enamel `plate` body, 4px radius, `overflow: hidden`, under a navy head (8px 12px; heading 14px 700, optional Japanese sign term at .8 opacity, optional right-hand note or tool). The body is 10px 12px 12px. Lists inside are separated by 1px `plate-rule` lines with no boxes or cards inside panels. The day panel (D# 這天的天氣與攝影機) uses the same head. Its weather rows are area, a 28px wear pictogram, Hind temperatures and the rain chance (`stop` at ≥ 50 %), with the conditions line in `plate-2`.

### Weather Ticker
A `housing` window (3px radius, 7px 10px) inside the now panel holding one scrolling LED row: city in green, reading in amber, a wet rain chance in red. 展開比較 swaps it for the `wxgrid` table (`auto-fill, minmax(142px, 1fr)`); the choice persists in localStorage `tk_wxgrid`.

### Fuji Lamps
A three-column list of status lamps (12px round `go/warn/stop-lamp`, inset rim) beside the place name and an 11.5px `plate-2` reading.

### Speed-Limit Strip
An enamel strip (10px 12px, 4px radius) with the 46px 30 km/h regulatory sign, the rule in 14.5px 700, its date in 12px `plate-2`, and an underlined 自駕注意事項 link. It switches to driving mode and scrolls to the full law block (110px sign, `stop`-coloured closing line).

### 駅名標 Station Sign (signature)
One per camera area, standing at the top of its cameras.
- **Body:** `sign` white, 3px radius, 1px `sign-rule` edge, laid out in three columns.
  - Left: the large station badge.
  - Centre: kana, kanji (Station Name) and romaji, with an optional `sign-2` sub-line.
  - Right: the area's current temperature in Hind 20px, the conditions, and a reversed 夜間 LED tag (amber on housing) after sunset.
- **Band:** a 9px line-colour band across the full width.
- **Prev / next row:** left and right arrow pictograms with the neighbouring station's name and a 10.5px romaji line, walking the line among the areas currently shown. Hover underlines the name.

### Route Diagram
One per line, above its signs: a 5px line-colour track with a white 4px-ringed station dot per area, the station name at 12.5px and its code (TK01…) in Hind 10px. Each station is a link to its sign, and the row scrolls sideways when it overflows.

### Platform ITV Monitor (signature)
One per camera, hung from a charcoal bracket.
- **Hood:** `housing-2`, 4px top radius. It holds a white number plate (Hind 700 11px, `TK01-1` = line + station + camera index) and two rubber keys (38×32, `#2c2f34`, 3px; hover `#3d4148`): a star pictogram for favourite (amber when pressed, persisted in `tk_fav`) and a pin for Google Maps.
- **Screen:** 16:9 dark glass (`#050607`) in a 5px charcoal frame. It shows the live thumbnail and, top left, a black LED status label in Hind 700 11px: LIVE green, 夜間 amber, 無畫面 red. A YouTube tag shows bottom right on hover or focus. After sunset a caption bar explains the dark picture.
- **Caption strip:** a separate enamel sign below the housing (5px gap, 3px radius, 1px rule) with the place name (Caption), the reason line and the Japanese line. The whole monitor and strip is one link, and hover underlines the name.

### Line Selector
The sticky charcoal bar of filters. Each button is 40px, 3px radius, with a 1.5px `#4a4e55` border and an `s` station badge of its line. The pressed button is a white plate with dark text, and hover whitens the border. A 1px separator divides lines from modes, and the frame-age note sits at the right in `housing-2ink`.

### Tool Button
The enamel panel's control: 38px, 3px radius, a 1.5px `plate-ink` border, transparent, 13px, with an optional 15px pictogram. Hover fills `plate-soft`. Expanded (`aria-expanded="true"`) reverses to ink with enamel text. Inside a navy head it takes the head's white, and expanded turns white with navy text. The theme button is the same shape on the concourse in `ground-ink`; it cycles 跟隨系統 → 淺色 → 深色 (persisted in `tk_theme`, applied before first paint).

### Pictograms
One inline SVG sprite of filled JIS-style pictograms on a 24-unit grid (`p-left/right` arrows, car, train, star / star outline, pin, Fuji, road, sun, moon, auto, info, external, grid, bag), used as `<svg class="pg"><use href="#p-…"/></svg>` at 1em in `currentColor`. The wear pictograms (短袖 … 羽絨＋手套帽子, by temperature threshold) are filled garments whose detail lines are cut back out in `plate`; scarf strokes (≥ 1.9) stay in ink.

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

### Don't:
- **Don't** lay the cameras out as a free-standing wall of same-size thumbnail cards under a hero; monitors always hang under their station sign.
- **Don't** animate signs, panels or monitors: no fades, slides, hover lifts or easing. Motion belongs to the LED board alone.
- **Don't** add blur shadows, glow or gradients; separation is a bracket, a housing edge or a 1px rule.
- **Don't** set LED text in a CSS web font or invent a fourth LED colour.
- **Don't** fill panels or set body text in line colours, or present TK / YS / HF / IZ as real railway lines.
- **Don't** float the second-language term above a heading as a label; it sits beside or below its name.
- **Don't** use emoji or outline icon sets.
