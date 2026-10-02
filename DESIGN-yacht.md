---
name: 快艇骰子 · Regatta
description: Yacht dice as a yacht race seen from above, with a drenched chart-blue sea, a 350-point course, ICS signal flags on a halyard, and the race committee's white results board.
colors:
  sea: "#0b3a82"
  sea-deep: "#082e6a"
  contour: "rgba(168,204,255,.17)"
  sounding: "rgba(176,204,246,.42)"
  rose: "#ff5aa9"
  sand: "#e9cd7c"
  signal-red: "#e1262b"
  signal-yellow: "#ffcd00"
  signal-blue: "#1d4fc0"
  signal-black: "#101318"
  signal-white: "#f8f7f2"
  flag-outline: "#0a1c3d"
  on-sea: "#f8f7f2"
  on-sea-2: "#bfd2f3"
  ink: "#0d1626"
  ink-2: "#34466a"
  preview-tint: "#e3eafa"
  preview-zero-tint: "#edf0f6"
  preview-zero-ink: "#4f6491"
  win-tint: "#fff2b3"
  key-yellow-hover: "#ffd93d"
typography:
  title:
    fontFamily: "'Noto Sans TC', 'PingFang TC', 'Microsoft JhengHei', system-ui, sans-serif"
    fontSize: "clamp(52px, 13vw, 128px)"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: ".02em"
  result:
    fontFamily: "'Noto Sans TC', 'PingFang TC', 'Microsoft JhengHei', system-ui, sans-serif"
    fontSize: "clamp(40px, 7cqw, 96px)"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: ".03em"
  bar-title:
    fontFamily: "'Noto Sans TC', 'PingFang TC', 'Microsoft JhengHei', system-ui, sans-serif"
    fontSize: "19px"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: ".06em"
  key:
    fontFamily: "'Noto Sans TC', 'PingFang TC', 'Microsoft JhengHei', system-ui, sans-serif"
    fontSize: "17px"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: ".06em"
  row-head:
    fontFamily: "'Noto Sans TC', 'PingFang TC', 'Microsoft JhengHei', system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 700
  status:
    fontFamily: "'Noto Sans TC', 'PingFang TC', 'Microsoft JhengHei', system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 700
    lineHeight: 1.5
  body:
    fontFamily: "'Noto Sans TC', 'PingFang TC', 'Microsoft JhengHei', system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 500
    lineHeight: 1.6
    letterSpacing: ".06em"
  rule-note:
    fontFamily: "'Noto Sans TC', 'PingFang TC', 'Microsoft JhengHei', system-ui, sans-serif"
    fontSize: "11.5px"
    fontWeight: 500
    lineHeight: 1.3
  total:
    fontFamily: "'Archivo', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "clamp(44px, 7cqw, 104px)"
    fontWeight: 900
    lineHeight: .86
    letterSpacing: "-.01em"
    fontVariation: "'wdth' 66"
  board-total:
    fontFamily: "'Archivo', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "30px"
    fontWeight: 900
    fontVariation: "'wdth' 66"
  board-cell:
    fontFamily: "'Archivo', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "20px"
    fontWeight: 800
    fontFeature: "'tnum'"
    fontVariation: "'wdth' 72"
  chart-label:
    fontFamily: "'Archivo', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "11px"
    fontWeight: 800
    fontVariation: "'wdth' 66"
  preview:
    fontFamily: "'Permanent Marker', 'Archivo', system-ui, sans-serif"
    fontSize: "21px"
    fontWeight: 400
    lineHeight: 1
rounded:
  tag: "2px"
  key: "3px"
  die: "20%"
  round: "50%"
spacing:
  chart-inset: "120px"
  chart-inset-phone: "58px"
  halyard: "66px"
  halyard-phone: "44px"
  die-gap: "16px"
  die-gap-phone: "8px"
  key-gap: "12px"
  board-pad: "18px 18px 28px"
  board-pad-phone: "6px 12px 24px"
components:
  key-primary:
    backgroundColor: "{colors.signal-yellow}"
    textColor: "{colors.signal-black}"
    typography: "{typography.key}"
    rounded: "{rounded.key}"
    padding: "0 22px"
    height: "52px"
  key-primary-hover:
    backgroundColor: "{colors.key-yellow-hover}"
  key-secondary:
    backgroundColor: "{colors.signal-white}"
    textColor: "{colors.ink}"
    typography: "{typography.key}"
    rounded: "{rounded.key}"
    padding: "0 22px"
    height: "52px"
  roll-key:
    backgroundColor: "{colors.signal-yellow}"
    textColor: "{colors.signal-black}"
    rounded: "{rounded.key}"
    width: "260px"
    height: "62px"
  die:
    backgroundColor: "{colors.signal-white}"
    textColor: "{colors.signal-black}"
    rounded: "{rounded.die}"
    size: "clamp(52px, calc((100cqw - 2 * 120px - 4 * 16px) / 5), 84px)"
  results-board:
    backgroundColor: "{colors.signal-white}"
    textColor: "{colors.ink}"
    padding: "{spacing.board-pad}"
    width: "380px"
  preview-cell:
    backgroundColor: "{colors.preview-tint}"
    textColor: "{colors.signal-blue}"
    typography: "{typography.preview}"
    rounded: "{rounded.tag}"
    height: "32px"
  preview-cell-hover:
    backgroundColor: "{colors.signal-blue}"
    textColor: "{colors.signal-white}"
  preview-cell-zero:
    backgroundColor: "{colors.preview-zero-tint}"
    textColor: "{colors.preview-zero-ink}"
    typography: "{typography.preview}"
    rounded: "{rounded.tag}"
  last-cell:
    backgroundColor: "{colors.signal-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.board-cell}"
  win-cell:
    backgroundColor: "{colors.win-tint}"
    textColor: "{colors.ink}"
  player-tag-p1:
    backgroundColor: "{colors.signal-red}"
    textColor: "#ffffff"
    rounded: "{rounded.tag}"
    padding: "6px 10px 6px 8px"
  player-tag-p2:
    backgroundColor: "{colors.signal-yellow}"
    textColor: "{colors.signal-black}"
    rounded: "{rounded.tag}"
    padding: "6px 10px 6px 8px"
  top-bar:
    backgroundColor: "{colors.sea-deep}"
    textColor: "{colors.on-sea}"
    typography: "{typography.bar-title}"
    height: "56px"
  buoy:
    backgroundColor: "{colors.signal-yellow}"
    textColor: "{colors.signal-black}"
    typography: "{typography.chart-label}"
    rounded: "{rounded.round}"
    size: "24px"
---

# Design System: 快艇骰子 · Regatta

> Scope: `yacht.html` (the Yacht dice game) only. This world is separate from root `DESIGN.md` (trip booklet), `DESIGN-hub.md` (site hub), `DESIGN-livecam.md` (station) and `DESIGN-blackjack.md` (pocket LCD).

## Overview

**Creative North Star: "The Regatta Chart"**

The page is a game of Yacht run as a yacht race and seen from above. A drenched chart-blue sea fills the viewport, with pale depth contours around two shoals, scattered soundings and, on desktop, a sand islet and a magenta compass rose. A rounded-rectangle course runs around the chart. Each scored category moves the player's boat along it by those points, so the lead is a distance you can see. The dice you hold hang as International Code of Signals numeral pennants from a white halyard. The scorecard is the race committee's white results board, ruled in black, with previews in grease pencil and scored cells stamped in.

Colour is flag colour, flat and at full strength: signal red, yellow, blue, black and white on chart blue. Players are flags too: P1 sails red, P2 sails yellow. Motion is sailing and hoisting only. Fonts come from Google Fonts. The owner declined inlining them, so this is the one external request.

Confirmed rejections: the category default of green felt, a dice cup, and a white scorecard table under a header; nautical clip-art (rope, anchors, wheels).

**Key Characteristics:**
- One drenched sea (`sea`), with every chart mark printed on it at low alpha. Magenta lives only in the compass rose.
- One lap = 350 points. Distance along the course is the score.
- Signal flags drawn to the ICS patterns and hung hoist-up from a horizontal line.
- A flat white committee board with black rules. Grease-pencil previews, stamped scores.
- Archivo condensed numerals, Noto Sans TC for Chinese, Permanent Marker for previews only.

## Colors

A signal-flag palette on a nautical chart: five full-strength flag colours, chart blue with its printed marks, and a white board printed in navy ink.

### Primary
- **Chart Blue** (`sea`): html/body, the chart and the menu; the page's `theme-color`. **Deep Water** (`sea-deep`) is the top bar, with a `rgba(168,204,255,.18)` hairline under it.

### Secondary
- **Signal Yellow** (`signal-yellow`): the primary keys (擲骰, 單人對 CPU, 再玩一次), the buoys, the held-die ring, P2's colour (mainsail, wake, turn underline, header tag), the board's "last row" mark, the big 快艇 status line, `::selection` and the global focus ring.
- **Signal Red** (`signal-red`): P1's colour (mainsail, wake, turn underline, header tag), and the red fields of the flags.

### Tertiary
- **Signal Blue** (`signal-blue`): flag fields, the finish flag, and the board's preview ink and preview hover fill.
- **Chart Magenta** (`rose`): the compass rose only (rings, ticks, needle, N).
- **Sand** (`sand`): the desktop islet, with a dashed half-alpha shoreline.

### Neutral
- **Signal White** (`signal-white`, also `on-sea`): dice, the results board, the white key, the halyard and bunting lines, the course centreline (at .5 alpha), the start line, hulls and jibs.
- **Signal Black** (`signal-black`): pips, buoy rims and numbers, mast and sail outlines, text on yellow. **Flag Outline** (`flag-outline`) is the 1.4px stroke around every sprite flag.
- **Chart Print**: **Contour** (`contour`) and **Sounding** (`sounding`), the sea's printed marks. **Pale Print** (`on-sea-2`) is secondary text on the sea (who, sub-lines, round label, back link, the disabled roll key).
- **Board Ink** (`ink`): board text and every rule. **Board Ink 2** (`ink-2`) is the rule notes, sums, zero scores and the board's sub-heading.
- **Board Tints:** **Preview Tint** (`preview-tint`) under a live preview, and **Preview Zero** (`preview-zero-tint` / `preview-zero-ink`) for a preview worth 0. **Winner Tint** (`win-tint`) marks the winning column at game end, on both columns for a tie.

### Named Rules
**The Flag Colours Rule.** Anything that signals is a flag colour (red, yellow, blue, black or white), flat and at full strength. It never gets a gradient, a glow or a tint ramp. Chart marks (contours, soundings, the course) are white or pale blue at low alpha. Nothing else on the sea is semi-transparent.

**The Magenta Rose Rule.** Chart magenta prints the compass rose and nothing else.

**The Players Are Flags Rule.** P1 is red and P2 is yellow, everywhere: mainsail, wake, turn underline and header tag. The sail number is white on red and black on yellow.

## Typography

**Chinese:** Noto Sans TC 500 / 700 / 900 (`--cn`, falling back to PingFang TC and Microsoft JhengHei).
**Numerals:** Archivo, a variable family loaded at `wdth 62–125`, `wght 500–900` (`--num`). It is always set condensed, with `font-stretch` 66–80 %: sail-number lettering.
**Grease pencil:** Permanent Marker (`--hand`), for board previews only.

**Character:** heavy condensed sail numbers and a solid Chinese sans, with one loose hand for the numbers that aren't committed yet.

### Hierarchy
- **Title** (Noto 900, clamp 52–128px): 快艇骰子 on the menu, under the YACHT bunting.
- **Result** (Noto 900, clamp 40–96px; 40px <980): 「X 獲勝」 / 平手.
- **Total** (Archivo 900, 66 %, clamp 44–104px by container width, line-height .86; 50px <980): the two plaques on the chart.
- **Bar title** (Noto 900 19px; 16px <980) beside the Y flag. The round count is Archivo 800 22px at 70 % (19px <980).
- **Key** (Noto 900 17px, .06em). The roll key is 21px (18px <980).
- **Board:** row heads Noto 700 15px over 11.5px rule notes (notes hidden ≤400px); cells Archivo 800 20px at 72 %, tabular; sums Archivo 700 15px at 76 %; total Archivo 900 30px at 66 %.
- **Status** (Noto 700 15px; 14px <980) with a 500 `on-sea-2` tail. The 快艇 line goes to 20px yellow.
- **Chart labels:** buoys Archivo 800 at 66 % (11px desktop, 9px phone), soundings Archivo 500 10px at 80 %, sail numbers Archivo 900 10px at 70 %, 起航 Noto 700 11px at .24em.

### Named Rules
**The Sail Number Rule.** Every number is Archivo, condensed (66–80 %). Chinese is Noto Sans TC. Don't set numbers in Noto or at Archivo's normal width.

**The Grease Pencil Rule.** Permanent Marker writes only the uncommitted preview on an open board cell. A scored number is always Archivo.

## Layout

The page is one fixed-height game (`100dvh`). There is no page scroll except on short phones.

- **≥980px:** a two-column grid. The chart takes `minmax(0,1fr)` and the board `minmax(380px,420px)`, under a 56px top bar, with `min-height: 720px`. The chart is a four-row grid (`1fr auto auto 1fr`) padded by the chart inset (120px), so the deck (the plaques) and the dock (status, rack, roll key) sit centred inside the loop. The board is a full-height white column that scrolls on its own.
- **<980px:** a single column. Under a 46px top bar, the loop is 240px tall (`--loop-h`) and holds only the plaques, with the course drawn around them. The dock follows below the loop, still on the sea: status, rack and roll key. The board takes the remaining height as its own scroll region (`overscroll-behavior: contain`, sticky header row). Its 成績板 heading is hidden. Pennants shrink to 22×33, the halyard drop to 44px and the die gap to 8px.
- **Short viewports** (<980px wide and ≤640px tall): the game drops its fixed height, the board stops scrolling separately, and the page scrolls as a whole.
- **Dice:** 58px on phones (52px ≤370px). On desktop the size is `clamp(52px, (container − 2·inset − 4·gap)/5, 84px)`.
- **Menu:** the same chart at full height (min 560px), with the bunting, title, sub-line, two keys and back link centred. Padding is 120/24px, or 72/20px <980.
- **Chart geometry** is drawn in JS to the loop's pixel size and redrawn on resize, keeping the boats where they are. On phones (chart <640 wide or <400 tall) the course inset is 42px, the lane offset 14px and the corner radius 52px, with boats at ×0.7. On desktop those are 70 / 22 / 110px, with boats at ×1.1.

## Elevation & Depth

The chart is flat: depth is printed (contours and soundings), never shaded. The results board, keys, buoys and flags are flat. The dice are the only objects with height: they sit on the chart with a soft drop, and a held die lifts higher.

### Shadow Vocabulary
- **Die at rest** (`0 6px 12px rgba(0,0,0,.32), inset 0 -4px 0 rgba(13,22,38,.10)`): every rolled die.
- **Die held** (`0 12px 16px rgba(0,0,0,.34), inset 0 -4px 0 rgba(13,22,38,.10)`), plus `translateY(-6px)`: a die hoisted toward the halyard.

### Named Rules
**The Only Dice Float Rule.** Shadows belong to the dice. Every other element is printed flat on the chart or the board.

## Shapes

The course is a rounded rectangle with corner radius `r`, minus the lane offset for the outer lane. Dice are rounded squares at 20 % of their side; the held ring sits 6px outside with radius +5px. Keys are near-square (3px corners), and board tags and preview cells are 2px. Buoys are circles. An unrolled die is an empty dashed outline (2px, `rgba(191,210,243,.55)`). Flags keep their true silhouettes:
- numeral pennants: a tapered trapezoid (28×40, 9-unit fly);
- A: a swallowtail;
- C, H, T and Y: rectangles.

The board is a plain unrounded panel. Its rules are 1px between rows and 3px under the header, under 六點 (the upper/lower split) and above 總計.

## Components

### The chart and course
- **Sea:** a seeded random generator (keyed to the chart size) draws five contour rings around each of two shoals, plus soundings (16 on phones, 34 on desktop), some with a subscript fraction. Soundings are kept out of the centre, where the deck sits. On desktop the innermost ring of the lower-right shoal is the sand islet, and the magenta compass rose (40px radius, 36 ticks, needle, N) sits in the loop's lower-left corner. Phones get neither.
- **Course:** a white dashed centreline (1.4px, `6 7` dash, .5 alpha) that runs counter-clockwise from the start line, mid-way along the bottom leg. Yellow buoys stand at 50, 100 … 300 points, each labelled with its distance. The 起航 line (2.5px white, labelled below) is also the finish. Once the game is over, a blue flag flies on it.
- **Lanes:** P1 sails the inner lane (centreline offset `+d`) and P2 the outer (`−d`). A score of 350 or more parks the boat just short of the line.
- **Wake:** each lane is a path with `pathLength="350"` in the player's colour (4px, round caps). It is revealed by `stroke-dasharray: <points> 360`, so the drawn wake is exactly the score.
- **Boat token:** a side-view yacht with a white hull and jib, a mainsail in the player's colour carrying the sail number, and a black mast. On the top leg the boat mirrors (`scaleX(−1)`), but its sail number is counter-flipped so it stays readable. The boat whose turn it is gets a 2.4px hull stroke. The same token is the player icon in keys, plaques and board header tags.
- **Spinnaker:** a full spinnaker in the player's colour, hidden at `scale(0)`. It is set only when 快艇 scores 50.

### Plaques (the totals)
A boat icon, the player's name (700 14px, `on-sea-2`, white on turn) and the total in Archivo. The active player gets a 5px underline in their colour. At game end the underline marks the winner, and nobody on a tie.

### Signal flags
The sprite holds ICS numeral pennants 1–6 and letter flags Y A C H T. Each is drawn for hanging from a horizontal line (hoist at the top), outlined in `flag-outline`.
- **Bunting:** the menu flies Y-A-C-H-T from a 2px white line that overhangs it by 28px each side. The flags unfurl one by one.
- **Board icons:** upper rows carry their numeral pennant (13×19), 快艇 carries Y, and the top bar title carries Y.

### The halyard rack
Five dice hang under a 2px white halyard that overhangs the row by 18px (12px on phones). The halyard drop is 66px (44px <980). Holding a die:
- lifts it 6px with the held shadow;
- rings it in 3px yellow;
- unfurls its numeral pennant from the line (`scaleY` from the hoist).

Dice are white with black pips (r 5.6 on a 60-unit face). An unrolled die is a dashed outline. Each die is a `button` with `aria-pressed` and a spoken label.

### Keys
- **Primary** (`key-primary`): yellow, black text. Hover is `key-yellow-hover`, and focus switches the outline to white. Press is `translateY(1px)`.
- **Secondary** (`key-secondary`): white with ink text.
- **Roll key:** the primary key enlarged (260×62; 220×50 <980). It carries 擲骰 and three answering pennants (red-and-white vertical stripes, flown from a staff). Each roll strikes one: it drops 13px and fades to .35. When rolling is over, or on the CPU's turn, it becomes a transparent outline key (2px inset `rgba(191,210,243,.45)`, `on-sea-2` text) reading 選一格計分 / CPU 的回合.
- **Back link:** a chevron plus text in `on-sea-2` that turns white with an underline on hover. In the top bar it is the chevron alone.

### Results board
White committee board, ink text, black rules. The sticky header row shows 類別 plus one tag per player; the active player's tag is filled in their colour. Rows:
- 13 categories, each with an icon and a rule note;
- 上區小計 (with `/ 63` until done);
- 上區獎勵;
- 下區小計 (game end only);
- 總計.

Cell states:
- **Preview:** an open cell for the current roll is a full-width Permanent Marker button in `signal-blue` on `preview-tint` that inverts on hover. A zero preview uses the zero pair. Focus is a blue outline.
- **Scored:** an Archivo number. A zero is `ink-2` 600.
- **Empty:** a dash, with 「未填」 for screen readers.
- **Last row:** each player's most recent cell stays filled `signal-yellow` until their next score (game end clears it).
- **Stamp:** a newly scored cell lands from `scale(1.6)`.
- **Winner:** every cell of the winning column takes `win-tint` at game end.

### Result
At game end the dock swaps to the result:
- a blue finish flag on a white staff, which hoists in;
- the Result headline;
- the score line with Archivo numbers;
- 再玩一次 (yellow) and 回小工具首頁 (white).

### Motion (sailing and hoisting)
- **Sail:** a boat sails to its new total over `min(1500, 650 + Δ·14)` ms with an ease-out quart, its wake drawing behind it. The plaque counts up with it.
- **Hoist:** pennants take .26s `cubic-bezier(.2,.9,.25,1)`. The die lift and ring take .2s. The menu bunting unfurls in 420ms per flag, staggered 70ms. The finish flag hoists in 620ms after 300ms.
- **Tumble:** rerolled dice tumble for .42s (drop, rotate, settle) while their faces flick four times at 70ms.
- **Strike:** a spent roll pennant drops over .3s.
- **Stamp:** a newly scored board cell lands over .7s.
- **Spinnaker:** on a 50-point 快艇 the scorer's spinnaker sets and the boat surges to ×1.9 for 2.6s, while the status reads 「快艇！五顆相同 +50」.
- **Reduced motion:** boats jump straight to their totals, nothing tumbles, stamps or unfurls, and pennant, die and key transitions are off. The spinnaker shows statically for 2.4s.

## Do's and Don'ts

### Do:
- **Do** keep the whole page on the chart-blue sea, with the white committee board as the only other surface.
- **Do** keep one lap at 350 points with buoys every 50, and draw every wake with `pathLength="350"` so its length is the score.
- **Do** use flag colours flat and at full strength, with P1 red and P2 yellow everywhere.
- **Do** draw any new flag to its ICS pattern, hanging hoist-up from a horizontal line, with the 1.4px `flag-outline` stroke.
- **Do** set numbers in condensed Archivo (66–80 %), Chinese in Noto Sans TC, and only previews in Permanent Marker.
- **Do** keep motion to sailing, hoisting, tumbling and stamping, and give every motion an instant reduced-motion path.
- **Do** keep the <980px order (loop with totals → dock → board as its own scroll region) and the short-viewport page-scroll fallback.

### Don't:
- **Don't** use magenta anywhere but the compass rose.
- **Don't** add green felt, a dice cup, or a scorecard table under a plain header.
- **Don't** add nautical clip-art such as rope borders, knots, anchors or ship's wheels. The halyard is a plain 2px white rule.
- **Don't** give anything but the dice a shadow, and never add gradients or glows to the sea or the flags.
- **Don't** write scored numbers in Permanent Marker, or previews in Archivo.
