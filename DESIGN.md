---
name: 旅のしおり · 關東秋季紅葉巡航
description: The trip itinerary as a two-ink risograph booklet printed on coloured paper stocks.
colors:
  ink: "#2a4a9b"
  ink-rule: "rgba(42, 74, 155, .38)"
  red: "#e3443f"
  red-ink: "#c42c36"
  red-ink-deep: "#a8222c"
  paper: "#ffffff"
  desk: "#2a4a9b"
  lemon: "#f4df6a"
  mizu: "#bedcee"
  wakakusa: "#cae2a6"
  momo: "#f5c4c0"
  fuji: "#d6caea"
  staple: "#a3a9b4"
typography:
  display:
    fontFamily: "'Zen Maru Heavy', 'Huninn Shiori', sans-serif"
    fontSize: "clamp(60px, 17.5vw, 96px)"
    fontWeight: 900
    lineHeight: 1.02
    letterSpacing: ".04em"
  numeral:
    fontFamily: "'Zen Maru Heavy', 'Huninn Shiori', sans-serif"
    fontSize: "66px"
    fontWeight: 900
    lineHeight: .82
  headline:
    fontFamily: "'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "30px"
    fontWeight: 400
    lineHeight: 1.3
  headline-day:
    fontFamily: "'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "24px"
    fontWeight: 400
    lineHeight: 1.4
  title:
    fontFamily: "'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "21px"
    fontWeight: 400
    lineHeight: 1.4
  body:
    fontFamily: "'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "15.5px"
    fontWeight: 400
    lineHeight: 1.8
  body-small:
    fontFamily: "'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "13.5px"
    fontWeight: 400
    lineHeight: 1.75
  label:
    fontFamily: "'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: ".16em"
  stub-time:
    fontFamily: "'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "23px"
    fontWeight: 400
    lineHeight: 1
    fontFeature: "'tnum' 1, 'lnum' 1"
rounded:
  checkbox: "2px"
  sheet: "3px"
  sm: "4px"
  stub: "6px"
  tab: "7px 7px 0 0"
  pill: "999px"
  round: "50%"
spacing:
  xs: "6px"
  sm: "10px"
  md: "14px"
  lg: "20px"
  xl: "30px"
  gutter: "20px"
  gutter-wide: "40px"
components:
  cover-button:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "0 16px"
    height: "46px"
  cover-button-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
  cover-button-today:
    backgroundColor: "{colors.red-ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.sm}"
    padding: "0 16px"
    height: "46px"
  cover-button-today-hover:
    backgroundColor: "{colors.red-ink-deep}"
  index-tab:
    backgroundColor: "{colors.mizu}"
    textColor: "{colors.ink}"
    rounded: "{rounded.tab}"
    padding: "11px 12px 8px"
    height: "40px"
  index-tab-today:
    backgroundColor: "{colors.red-ink}"
    textColor: "{colors.paper}"
  ticket-stub:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.stub}"
    height: "64px"
  hanko:
    textColor: "{colors.red-ink}"
    rounded: "{rounded.round}"
    size: "48px"
  ruled-box:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "16px 14px 12px"
  chip:
    backgroundColor: "{colors.mizu}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "2px 9px"
  tag:
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "1px 6px"
  arrival-stamp:
    textColor: "{colors.ink}"
    rounded: "{rounded.round}"
    size: "116px"
---

# Design System: 旅のしおり · 關東秋季紅葉巡航

> Scope: this system covers the **Japan autumn road-trip itinerary** (`trip.html`) only. The other pages in this repository (betting tracker, yacht dice, usage dashboard, golf analyzer, blackjack trainer, investment notes, etc.) each carry their own unrelated look and are not described here. `trip-v1.html` is the pre-redesign page, kept only as a legacy link; it is not part of this system.

## Overview

**Creative North Star: "The Two-Ink Shiori"**

The itinerary is the hand-made 旅のしおり two friends staple together before a trip, printed on a risograph with exactly two drums. Federal Blue prints every word and every rule; riso red is reserved for what cannot slip. Each page is a sheet of stock: white paper for reading, coloured 色上質紙 (レモン, 水色, 若草, 桃, 藤) for the cover, page bands, index tabs and chips. The sheets sit on a desk of the same blue ink, so the booklet reads as an object laid down rather than an app shell.

Density is a printed booklet's, not a dashboard's: one page per day, generous 1.8 body leading, sections divided by rules rather than boxes. Depth is paper only. There is a faint multiply grain over every sheet, a halftone gutter at the foot of the cover, a deliberate red-plate misregistration behind the heavy numerals, and a displacement filter that roughens stamps and hand-ruled checkboxes. Optional material is folded away into 付録 slips; the red ticket stubs carry the day's hard commitments.

Confirmed rejections: cream grounds, terracotta, gradients used as fills, glass, card shadows, and the timeline-of-cards app shell.

**Key Characteristics:**
- Two inks only (blue, red) on white or coloured stock; everything else is paper.
- Hierarchy by size and rule weight, never by grey tint.
- Rules are the structure: 1.5px solid, 1px dashed cuts, 4px double rules, 2px dotted leaders.
- Heavy rounded numerals with a red misregistration shadow for the title, day numbers and countdown.
- Red belongs to hard commitments: booking times, deadlines, hanko, stamps, today.
- One authored motion: the ink press.

## Colors

A two-drum riso palette: one cool blue ink, one warm red ink, and five pale paper stocks.

### Primary
- **Federal Blue Ink** (`ink`): every line of text, every rule, every border, every icon stroke. Also the desk the booklet lies on (`desk`, same value) and the halftone and grain tints (at 22% and 7.5% multiply).
- **Ink Rule** (`ink-rule`): the same blue thinned for hairlines between list rows (dishes, checklist items, phone rows), link underlines at rest, and the memo page's ruled lines. Rules only, never text.

### Secondary
- **Riso Red** (`red`): the second drum as ink on paper: the cover countdown stamp, the 到著章 impression, the misregistered plate behind heavy numerals, the red check mark and its strike-through. Graphic marks only.
- **Legible Red** (`red-ink`): red used for text and state: stub times on booked and due stubs, hanko text and rings, the `must` box border and heading, today's tab and plan row, the double rule under today's band, link hover, and the dashed focus ring.
- **Pressed Red** (`red-ink-deep`): hover state of the red today button only.

### Neutral
- **White Stock** (`paper`): every reading sheet, stub, box and button face.
- **レモン Lemon** (`lemon`): the cover, chapter bands for lodging/transport/food/checklist/back cover, the selection highlight and the marker-pen underline (`.mark`).
- **水色 Mizu** (`mizu`), **若草 Wakakusa** (`wakakusa`), **桃 Momo** (`momo`), **藤 Fuji** (`fuji`): per-day and per-chapter stocks for page bands, index tabs, chips, contents dots and plan-row numbers. The stock is set once per page via a `--stock` variable and every coloured piece on that page inherits it.
- **Staple Steel** (`staple`): the two staples on the cover spine. A physical object, not ink; never use it for text or rules.

### Named Rules
**The Two Drums Rule.** Text and rules print in blue or red and nothing else. White text appears only knocked out of a solid red or blue fill (today's tab and button, the hovered cover button, the out-of-booklet tabs on the desk).

**The Red Is a Promise Rule.** Red marks a booking time, a deadline, a hanko, a stamp or today. A suggestion, a tip or a highlight never gets red; the lemon marker underline is for emphasis.

**The Red Plate Rule.** `red` is for large graphic marks; any red text under display size uses `red-ink`, which holds 5.58:1 on white.

## Typography

**Display Font:** Zen Maru Heavy (Zen Maru Gothic Black, SIL OFL), with Huninn Shiori fallback
**Body Font:** Huninn Shiori (jf open 粉圓 Regular, SIL OFL 1.1), with PingFang TC, Noto Sans TC, Microsoft JhengHei
**Label/Mono Font:** none distinct; figures use tabular lining numerals (`.num`).

**Character:** A soft, round Taiwanese hand-lettered body face paired with a single weight of heavy rounded gothic for numbers and the title, like a rubber-stamped cover on a friendly photocopied booklet.

Both faces are inlined as WOFF2 data URIs so the page is fully styled offline. Huninn Shiori is subset to the glyphs on the page and must be re-subset with `tools/trip-font.py` after any text edit. Zen Maru Heavy is a 20-glyph subset restricted by `unicode-range` to 關東秋季紅葉巡航, the digits 0–9 and 日目; changing the title means re-fetching that subset.

### Hierarchy
- **Display** (900, clamp(60px, 17.5vw, 96px), 1.02, vertical-rl): the cover title only, set vertically down the right side with a red plate offset 3px/2.5px behind it.
- **Numeral** (900, 66px, 0.82): the day number in each day band (with a 2.5px/2px red plate), and at 50px the cover countdown number.
- **Headline** (400, 30px, 1.3): chapter band titles (目錄, 日程表, 住宿…). Day band titles run at 24px/1.4, balanced.
- **Title** (400, 21px, 1.4): lodging and transport entry headings; area group headings at 20px.
- **Body** (400, 15.5px, 1.8): prose, capped at 36em. Slip bodies and checklist text at 15px; stub subjects at 16px.
- **Body Small** (400, 13.5px, 1.75): notes, stub details (13px), dates in the plan, box headings.
- **Label** (400, 14px, 0.16em tracking): section headings (今天的約定, 附錄, 用餐) followed by a 1.5px rule running to the margin.
- **Stub Time** (400, 23px, 1, tabular): the time in a ticket stub; 17px when the stub carries a word instead of a time.

### Named Rules
**The Size Not Grey Rule.** Secondary text is never tinted grey or faded. It is smaller, and that is all: `.dim` shrinks to 0.92em in full ink.

**The One Heavy Rule.** The heavy face exists only for the title, the countdown and day numerals. Its subset cannot set anything else, and nothing else should want it.

## Layout

A single column booklet, max 760px, centred on the blue desk. On phones every sheet runs edge to edge with a 20px gutter; sheets are separated by a 10px strip of desk. From 800px the desk gains padding (36px 24px 72px), sheets round to 3px corners and 14px gaps, gutters widen to 40px, and the index tabs wrap onto the booklet's top edge with day tabs showing only the number.

The cover fills the first viewport (`100svh`, capped at 960px on desktop): a two-column grid with the kind, dates, route and countdown stamp on the left, the vertical title on the right, and the action buttons along the bottom edge. A sticky index-tab strip sits directly under the cover and stays pinned; `scroll-padding-top: 58px` keeps anchored pages clear of it.

Each page is a coloured band (folio number top right, a 4px double rule beneath) followed by a white body. Vertical rhythm steps through 6, 10, 14, 20 and 30px: 30px above section headings, 22–26px around meal notes and boxes, 10px between stubs. Nothing sits in a side rail; on a 390px phone every pixel of width goes to content.

## Elevation & Depth

Flat by construction. There are no shadows anywhere. Depth is conveyed the way paper conveys it: coloured stock against white stock against the blue desk, a 7.5% multiply grain over each sheet, halftone dots fading up the cover's foot, the red plate misregistered behind heavy type, and a roughening displacement filter (`#rough`) on stamps, hanko and checkboxes so they read as pressed ink.

### Named Rules
**The Paper Only Rule.** No `box-shadow`, no blur, no gradient fills. If something needs to stand forward, give it a different stock or a heavier rule.

## Shapes

Mostly square paper with small practical radii. Buttons, boxes, tags, warnings and embedded maps use 4px; ticket stubs 6px with punched half-circle notches where the dashed perforation meets the edge; index tabs 7px on their top corners only; chips and route tags are full pills; hanko, stamps, contents dots and plan numbers are circles. Hand-ruled checkboxes are 2px squares with a roughened stroke.

Rule vocabulary is the form language: 1.5px solid for boxes, stubs and row dividers; 1px or 1.5px dashed for 切り取り線 cuts, slips, the lodging line and warnings; 4px double for the foot of every page band and the head of meal notes, plan tables, dish lists and asides; 2px dotted for contents leaders.

## Components

### Buttons
Printed labels on a stiff card: plain, bordered, confident.
- **Shape:** gently squared (4px), 46px minimum height.
- **Primary (cover):** white stock, blue text, 1.5px blue border, 16px side padding, icon plus label.
- **Hover:** fills solid blue with white text (150ms colour transition only).
- **Today:** solid legible red with white text, shown only during the trip; hover deepens to pressed red.
- **Text button:** underlined 13.5px blue text with no box (checklist reset), 44px tall hit area, red on hover.

### Chips
- **Style:** 12.5px pill with a 1.5px blue border, filled with the page or day stock (e.g. `D2 · 11/08` on 若草).
- **Tags:** inline 12.5px bordered labels at 4px radius that wrap cleanly across lines; `.tag.red` switches the border to legible red for hard facts. Route summaries on the plan page use a 13px pill variant.

### Cards / Containers
There are no cards. Containers are ruled.
- **Ruled box:** 1.5px blue border at 4px, 16px 14px 12px padding, with its heading set into the top rule on a white knock-out.
- **Must box:** the same with a 2px legible-red border and red heading, for hard constraints.
- **Meal note:** a band opened by a 4px double rule and closed by a 1.5px rule, fork icon label.
- **Warning:** 1.5px dashed blue border, caution icon, 14px text.
- **Entry:** lodging/transport records separated by 1.5px rules, with a chip, a duration and a hanko on the first line.

### Inputs / Fields
- **Checklist item:** a visually hidden checkbox driving a 26px hand-ruled square (2px roughened blue stroke). Checking pops a red check mark in (scale 0.5 to 1.12, rotate -6deg, 180ms springy ease) and strikes the text through in red. Focus is a 2px dashed red ring offset 3px.
- **Error / Disabled:** none in the build.

### Navigation
- **Index tabs:** a sticky strip of 14px stock-coloured tabs on the blue desk, 7px top corners, dropped 5px until active. Active tab rises to its line and gains a 3px legible-red top edge; this is instant, tabs do not animate. Today's day tab is solid red with white text; past days show a small check. Two outline tabs on the desk leave the booklet (live cams, the legacy page). On phones the strip scrolls horizontally and keeps the active tab in view.
- **Contents:** stock dot, title, dotted leader, page number, 46px rows.
- **Plan table:** round stock numbers, date, title and lodging per day, opened by a double rule; today's row turns its number and title red.
- **Links:** blue with a thin ink-rule underline offset 3px; map links carry a masked pin; hover turns red with a full-strength underline.

### Ticket Stub (signature)
The day's hard commitments. A white stub with a 1.5px blue border and 6px radius, divided by a dashed perforation 78px in (92px on desktop) with punched half-circle notches top and bottom. The time sits in the tear-off (23px, red on booked and due stubs), the subject and detail beside it, and a rotated circular hanko at the right: 予約済 and 締切 or a due date in a solid red ring, 還沒訂 in a dashed ring (red when a booking window opens on a date, blue when it is simply still to do).

### Hanko
Rotated (-10 to -12deg) circular seals, 44–52px, 2–2.5px legible-red ring and text, multiplied and roughened. The 今天 hanko sits in today's band beside the folio.

### Appendix Slip
Everything optional folds into a `<details>` slip: 48px summary rows separated by 1px dashed cuts, a chevron and an icon, 15px body indented 26px. The body opens without animation.

### 到著章 (Arrival Stamp)
A 116px dashed blue circle at the foot of each day page reading 到著章. Tapping presses a red station stamp into it: 200ms, scale 1.18 to 1 with the rotation settling 6deg, multiply blend, rough filter, 92% opacity. Tap again to lift it. Persisted per device (localStorage `shiori-stamps-v1`).

### Today
Today's page is marked by three things together: the band's double rule turns legible red, a rough red 今天 hanko lands in the band, and its index tab is solid red. The band itself keeps its stock; there is no red-filled band.

### Memo and Back Cover
The back cover carries phone numbers and links in 50px rows over ink-rule hairlines, a 180px memo area ruled every 36px in ink-rule, and a centred 13px colophon.

## Do's and Don'ts

### Do:
- **Do** print every word and rule in `ink` or `red-ink`; use `red` only for large marks (stamps, plates, check marks).
- **Do** set a page's stock once with a `stock-*` class and let the band, tab, chips and dots inherit `--stock`.
- **Do** put each day's bookings and deadlines in ticket stubs with a hanko, and fold everything optional into 付録 slips.
- **Do** close every page band with a 4px double rule, and use 1px dashed cuts for slips and tear-off lines.
- **Do** build hierarchy from size alone (15.5px body, 13.5px small, 14px tracked labels).
- **Do** keep tap targets at 44–50px and body text at AA contrast on its stock.
- **Do** re-subset Huninn Shiori with `tools/trip-font.py` after changing any text.
- **Do** mark today with the red double rule, the 今天 hanko and the red tab together.

### Don't:
- **Don't** add box shadows, blur, glass or gradient fills; depth is stock, rule and grain.
- **Don't** use cream or terracotta grounds.
- **Don't** tint secondary text grey or reduce its opacity.
- **Don't** give suggestions, tips or highlights red.
- **Don't** fill today's band red; the band keeps its stock.
- **Don't** animate tabs, page changes or reveals; the only authored motion is the ink press and the check-mark pop.
- **Don't** set anything but the title, countdown and day numerals in Zen Maru Heavy.
- **Don't** add a side rail or marker column that costs phone width.
- **Don't** load CSS, fonts or icons from a CDN; the booklet must render fully styled offline.
