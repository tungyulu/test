---
name: 00981A 持股異動日報 · 重大訊息公告
description: One active ETF's daily basket read as a formal disclosure notice — a white ruled sheet on a blue-grey desk, an ink-reversed title bar, a 主旨 sentence and numbered 說明 tables, navy only where you can press.
colors:
  desk: "#e6ebf1"
  paper: "#ffffff"
  paper-2: "#f4f7fb"
  ink: "#15171c"
  ink-2: "#4a5160"
  rule: "#9aa7b9"
  hair: "#d4dbe5"
  head: "#d9e3f0"
  act: "#24467a"
  act-ink: "#ffffff"
  up: "#c1121f"
  down: "#0b7339"
  bar: "#15171c"
  bar-ink: "#ffffff"
  dark-desk: "#101215"
  dark-paper: "#1a1d22"
  dark-paper-2: "#21252c"
  dark-ink: "#e9ebef"
  dark-ink-2: "#aeb5c2"
  dark-rule: "#56617a"
  dark-hair: "#323946"
  dark-head: "#273449"
  dark-act: "#a8c1f0"
  dark-act-ink: "#101215"
  dark-up: "#ff7066"
  dark-down: "#4fd38a"
  dark-bar: "#273449"
  dark-bar-ink: "#e9ebef"
typography:
  title:
    fontFamily: "'Noto Sans TC', system-ui, -apple-system, 'PingFang TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "24px"
    fontWeight: 900
    lineHeight: 1.3
    letterSpacing: ".02em"
  form-label:
    fontFamily: "'LXGW WenKai TC', 'BiauKai', 'DFKai-SB', 'Kaiti TC', serif"
    fontSize: "24px"
    fontWeight: 700
    lineHeight: 1.35
  subject:
    fontFamily: "'Noto Sans TC', system-ui, -apple-system, 'PingFang TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "24px"
    fontWeight: 700
    lineHeight: 1.5
  item-head:
    fontFamily: "'Noto Sans TC', system-ui, -apple-system, 'PingFang TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "15px"
    fontWeight: 700
    lineHeight: 1.5
  body:
    fontFamily: "'Noto Sans TC', system-ui, -apple-system, 'PingFang TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.65
  figure:
    fontFamily: "'Source Sans 3', 'Noto Sans TC', system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 700
    lineHeight: 1.5
    fontFeature: "'tnum', 'lnum'"
  small:
    fontFamily: "'Noto Sans TC', system-ui, -apple-system, 'PingFang TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.5
  state-tag:
    fontFamily: "'Noto Sans TC', system-ui, -apple-system, 'PingFang TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "13px"
    fontWeight: 700
    lineHeight: 1.4
rounded:
  none: "0"
spacing:
  sheet-max: "1040px"
  sheet-gutter: "16px"
  sheet-gutter-phone: "8px"
  label-col: "5.2em"
  row-body: "14px 16px 18px"
  row-body-phone: "4px 12px 16px"
  item-gap: "22px"
  halves-gap: "20px"
  cell-pad: "0 10px"
  row-min: "46px"
  head-row-min: "34px"
  tap: "44px"
components:
  sheet:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    width: "{spacing.sheet-max}"
  title-bar:
    backgroundColor: "{colors.bar}"
    textColor: "{colors.bar-ink}"
    typography: "{typography.title}"
    padding: "14px 18px 13px"
  form-label:
    textColor: "{colors.ink}"
    typography: "{typography.form-label}"
    width: "{spacing.label-col}"
  subject:
    textColor: "{colors.ink}"
    typography: "{typography.subject}"
  table-head:
    backgroundColor: "{colors.head}"
    textColor: "{colors.ink-2}"
    typography: "{typography.small}"
    height: "{spacing.head-row-min}"
    padding: "{spacing.cell-pad}"
  table-row:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    height: "{spacing.row-min}"
    padding: "{spacing.cell-pad}"
  table-row-hover:
    backgroundColor: "{colors.paper-2}"
  stock-name:
    textColor: "{colors.act}"
    typography: "{typography.item-head}"
  key:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.act}"
    typography: "{typography.state-tag}"
    rounded: "{rounded.none}"
    height: "{spacing.tap}"
    padding: "0 10px"
  key-hover:
    backgroundColor: "{colors.paper-2}"
  key-pressed:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
  select:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.act}"
    rounded: "{rounded.none}"
    height: "{spacing.tap}"
    padding: "0 30px 0 10px"
  search-input:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: "{spacing.tap}"
    padding: "0 10px"
  state-new:
    textColor: "{colors.ink}"
    typography: "{typography.state-tag}"
    padding: "0 5px"
  state-add:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.state-tag}"
    padding: "1px 7px"
  state-cut:
    textColor: "{colors.ink}"
    typography: "{typography.state-tag}"
    padding: ".5px 6.5px"
  state-out:
    textColor: "{colors.ink}"
    typography: "{typography.state-tag}"
    padding: "1px 7px"
  price-up:
    textColor: "{colors.up}"
    typography: "{typography.figure}"
  price-down:
    textColor: "{colors.down}"
    typography: "{typography.figure}"
  holding-cell:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    padding: "9px 11px 10px"
    height: "84px"
  holding-cell-open:
    backgroundColor: "{colors.head}"
  detail:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    padding: "12px 12px 14px"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.small}"
    padding: "5px 9px"
---

# Design System: 00981A 持股異動日報 · 重大訊息公告

> Scope: `etf-00981a.html` (00981A 持股異動日報) only. This world is separate from root `DESIGN.md` (trip booklet, `trip-v2.html`), `DESIGN-hub.md` (site hub), `DESIGN-livecam.md` (station: `livecam.html`, `trip.html`), `DESIGN-blackjack.md` (pocket LCD), `DESIGN-yacht.md` (regatta), `DESIGN-nba.md` (fantasy data app) and `DESIGN-invest.md` (passbook). Recorded from the shipped build on 2026-10-14.

## Overview

**Creative North Star: "The Disclosure Notice"**

The page is one formal notice per trading day, the kind a listed company files on 公開資訊觀測站 and a government office writes as 公文. A white sheet lies on a cool blue-grey desk. An ink-reversed title bar names it, a ruled header grid gives the date, the notice number and the comparison, and the body runs in fixed form rows: 主旨 (one sentence saying what the manager bought and sold), 說明 (numbered items: 一、買進 and 二、賣出 as two hard halves, 三、行情, 四、誰拉、誰拖), 附表 (一、持股一覽 as a cell grid, 二、持股明細 as a sortable table) and 備註. The structure is the form, not decoration.

Hierarchy comes from three type sizes, weight, reversal and 1px rules. Only three hues carry meaning: navy marks what can be pressed, and red and green mark price direction. Buy and sell state is never a colour. It is drawn as line form in ink, the way a clerk would mark a printed table. The page is dense and calm on purpose: everything is visible, and the only thing that opens is a stock's own history, in place under the row or cell that was tapped.

The confirmed rejections are the broker-app card dashboard and the dark quote terminal. The dark theme stays a dimmed document, not a terminal.

**Key Characteristics:**
- A white document sheet on a blue-grey desk, square corners, 1px blue-grey rules everywhere.
- Ink-reversed title bar; pale-blue header rows on every table and fact grid.
- Kai-face form labels (主旨 / 說明 / 附表 / 備註 and the 一、二、 numerals); Noto Sans TC for everything else, Source Sans 3 tabular figures for numbers.
- Three type sizes only: 24 / 15 / 13.
- Navy on pressable things only; red up and green down on price change only.
- Buy / sell state as line form: double = new, filled = add, dashed = cut, outlined and struck = out.
- A stock's history opens in place, one at a time, never in a modal.

## Colors

A near-monochrome document palette (ink, paper, blue-grey rules) with exactly three meaningful hues: one navy for action and the Taiwan quote pair for price.

### Primary
- **Notice Navy** (act): links, keys, selects, the stock names in the 主旨 and in every table row and cell, the fold and 再列 buttons, the close key, the focus ring and the checkbox accent. In dark mode it becomes **Pale Signal Blue** (dark-act) on the same roles; text on a navy fill uses act-ink.

### Secondary
- **Quote Red** (up) and **Quote Green** (down): the Taiwan convention, red up and green down, on every price change, NAV and index move, the 說明三 fact deltas and the 說明四 contribution bars (weight × change). Every coloured figure also carries a sign and a ▲ / ▼ arrow, so colour is never the only signal. Dark mode lifts them to dark-up / dark-down.

### Neutral
- **Desk Blue-Grey** (desk): the page behind the sheet and the utility bar.
- **Notice White** (paper): the sheet, table bodies, cells, keys and the open detail.
- **Rule Wash** (paper-2): row hover, the open table row, key hover, the fold button.
- **Form Header Blue** (head): table header rows, fact-grid labels, the open holding cell, the chart's area fill and text selection.
- **Notice Ink** (ink): all body text, the state tags' lines and fills, the chart line, the pressed segment key and the tooltip ground.
- **Secondary Ink** (ink-2): column heads, notes, codes, sold and parked rows, axis labels. It holds ≥ 6:1 on paper, head and desk in both themes.
- **Strong Rule** (rule): outer table frames, section dividers, key and input borders, the sheet edge.
- **Hairline** (hair): cell dividers inside a table or grid.
- **Title Bar** (bar / bar-ink): the reversed title. In light mode it is the ink itself; in dark mode it is the head blue (dark-bar), so the bar stays the darkest-reading band without becoming a white slab.

### Named Rules
**The Pressable Navy Rule.** Navy appears only on something that responds to a tap: a link, key, select, stock name, fold button or the focus ring. Never use it for headings, labels, figures or decoration.

**The Quote Colour Rule.** Red and green mean price direction (red up, green down) and nothing else, always with a sign and a ▲ / ▼ arrow. A buy or a sell is never red or green.

**The Line Form Rule.** Buy and sell state is drawn in ink as a frame: a double line means new (新增), a filled ink tag or a solid 2px frame means add (加碼), a dashed line means cut (減碼), and an outlined, struck-through tag means out (剔除). Sold rows grey to secondary ink with the name struck through.

## Typography

**Display Font:** none. The title is Noto Sans TC at its heaviest weight.
**Body Font:** Noto Sans TC (with system-ui, PingFang TC, Microsoft JhengHei)
**Label Font:** LXGW WenKai TC 700, a fixed subset for 主旨說明附表備註, 一二三四五 and 、： (with BiauKai, DFKai-SB, Kaiti TC)
**Figure Font:** Source Sans 3 with tabular, lining numerals (falling back to Noto Sans TC)

**Character:** A government form's two voices: the brush-derived Kai of the printed form labels, and a plain sans for what is filled in. Numbers line up in tabular columns like a filed schedule.

### Hierarchy
- **Title** (900, 24px, 1.3, .02em): the reversed title bar 「<ticker> 持股異動日報」 only.
- **Form label** (Kai 700, 24px, 1.35): 主旨 / 說明 / 附表 / 備註 in the left label column. The same face at item size sets the 一、二、 numerals and the 備註 list markers.
- **Subject** (700, 24px, 1.5, `text-wrap: pretty`): the one 主旨 sentence; its stock names are navy underlined links and its counts are tabular figures.
- **Item head** (700, 15px, 1.5): 說明 and 附表 item headings, stock names in rows and cells, the detail heading.
- **Body** (400, 15px, 1.65): running text and table values.
- **Figure** (Source Sans 3, 15px, tabular): every number; bold where it is the cell's main value.
- **Small** (400, 13px): column heads, notes, codes, sub-lines, keys, the utility bar, axis labels, the tooltip.
- **State tag** (700, 13px, 1.4): the 新增 / 加碼 / 減碼 / 剔除 tags.

### Named Rules
**The Three Sizes Rule.** Only 24, 15 and 13px exist. Rank comes from weight, reversal and rules, never from a fourth size.

**The Form Voice Rule.** Kai is reserved for what the form itself prints: the four row labels, the item numerals and the 備註 markers. Content is never set in Kai, and a new label needs its characters added to the Kai subset.

## Layout

The sheet is at most 1040px wide, centred, with a 16px gutter below 1072px and 8px at ≤ 420px. A thin utility bar (home link, theme key) sits outside the sheet on the desk.

Inside, every section is a two-column form row: a 5.2em label column (the Kai label, hair rule on its right) and the body (14px 16px 18px). At ≤ 560px the label stacks above the body. Items inside a body are 22px apart. The header grid is four label / value cells (1 : .8 : 1 : 1.4) that become two columns at ≤ 760px and label-beside-value lines at ≤ 560px.

說明一 and 說明二 are equal halves with a 20px gap from 900px up and stack below 900px. Their tables drop the column head at ≤ 560px and fold amount and change into a secondary line. The market facts are a four-column grid, two at ≤ 760px. The holdings grid auto-fills 128px cells (108px at ≤ 560px) with dense packing. The full holdings table has nine fixed columns and a sticky head from 900px up; below that it becomes name + main value with a secondary line. Every interactive target is at least 44px.

## Elevation & Depth

The system is flat. The page's one lift is the sheet itself, which in light mode carries a soft two-layer ambient shadow so it reads as paper on a desk. Dark mode drops it; the sheet separates from the desk by tone and its rule edge. Everything inside the sheet is grouped by 1px rules and header-row tint, never by shadow.

### Shadow Vocabulary
- **Sheet lift** (`box-shadow: 0 1px 2px rgba(20,30,50,.06), 0 8px 24px rgba(20,30,50,.06)`): the sheet only, light mode only.

### Named Rules
**The Ruled Depth Rule.** Inside the sheet, depth is a rule or a header tint, never a shadow, card or gradient. A group gets a 1px rule frame and a pale-blue head row.

## Shapes

Square everywhere: the sheet, tables, keys, selects, the search field, cells, tags and the detail all have 0 radius. Outer frames and dividers between sections are the 1px strong rule; dividers inside a table or grid are the 1px hairline. Line weight and line style carry meaning only for buy / sell state (double, solid, dashed, struck). The select's chevron is a drawn 2px corner in navy.

## Components

### Fund tabs
Four square folder tabs sit on the top edge of the sheet, one per fund (ticker in 15px bold tabular figures over the short name in 13px secondary ink), equal widths, 1px strong-rule frames without a bottom edge, rule-wash ground and navy ticker. The current fund's tab takes the title bar's reversed ground and overlaps the sheet edge by 1px, so tab and bar read as one band. Added 2026-10-19 with the three new funds.

### Title bar and header grid
Ink-reversed bar with the 24px title and a 13px line naming the source and saying it is not an official notice. Below it the ruled header grid: each cell has a pale-blue label row and a value row (資料日期 in ROC form with weekday, 編號 第 N 號, the comparison select, the previous / day / next key group). A status line under it reports loading; its warning state is bold.

### Keys and selects
- **Shape:** square (0), 1px strong-rule border, 44px tall.
- **Default:** white ground, navy 13px bold label or navy chevron icon.
- **Hover:** rule-wash ground. **Disabled:** secondary ink at .45 opacity.
- **Pressed segment** (the detail's weight / lots switch): ink fill with white text.
- **Focus:** a 2px navy outline at 2px offset on every focusable element.
- The previous / next keys and the day select join into one bar (the select loses its side borders).

### Ruled tables
- **Frame:** 1px strong rule; pale-blue head row (34px min) with 13px secondary-ink column heads, right-aligned except the first.
- **Rows:** 46px min, hairline between rows, rule-wash on hover; the stock name is a navy bold button whose hit area covers the whole row.
- **Sort heads** (持股明細): the active head turns ink and bold with a masked chevron; ascending flips it.
- **Folds:** a full-width 44px rule-wash button in navy bold under the table (再列, show parked / sold rows).

### State tags
Inline 13px bold tags in ink: 新增 double 3px frame, 加碼 filled ink with white text, 減碼 1.5px dashed frame, 剔除 1px frame with a strike. The same tags explain themselves in the 備註.

### Holdings grid (附表一)
Square button cells sharing hairline borders: navy bold name (ellipsized), the weight in bold tabular figures with the code, the day's change in quote colour, and the state tag. The cell's frame repeats the state: inset double 4px frame for new, a 2px solid frame for add, an inset dashed frame for cut. The open cell takes the header blue.

### In-place detail (signature)
Tapping a stock name (in the 主旨, a row or a cell) opens that stock's history directly under it, one at a time, never in a modal. In tables it is inserted after the row; in the grid it spans the full row width after the cell. It holds the heading with code, a 44px square close key, a ruled fact grid (pale-blue labels), a weight / lots segment switch, an SVG line chart (ink line, header-blue area, hairline grid, dashed crosshair, an ink-reversed tooltip) and a ruled trade log. It opens with a 180ms fade and 4px drop, none under reduced motion. Its state is in the URL hash.

### Contribution bars (說明四)
A three-column ruled table: stock, a 10px bar in quote red or green proportional to the contribution, and the bp figure.

### Market facts (說明三)
A ruled definition grid: pale-blue label, bold tabular value, and a 13px delta line in quote colour with arrow and sign.

## Do's and Don'ts

### Do:
- **Do** keep every section a labelled form row: Kai label left, content right, a strong rule between rows.
- **Do** put a pale-blue head row on every table and fact grid, and frame it with a 1px strong rule.
- **Do** write a price change with a sign and a ▲ / ▼ arrow as well as the quote colour.
- **Do** mark a new buy / sell state with one of the four line forms in ink.
- **Do** open a stock's history in place under what was tapped, one at a time, with its state in the hash.
- **Do** keep every tap target at least 44px and every text / ground pair at least 4.5:1 in both themes.

### Don't:
- **Don't** use navy on anything that cannot be pressed.
- **Don't** colour a buy or a sell red or green, or a price change anything but red up / green down.
- **Don't** add a fourth type size or set content in the Kai face.
- **Don't** round corners, add cards, shadows or gradients inside the sheet.
- **Don't** open a stock's history in a modal, a drawer or a new page.
- **Don't** turn the dark theme into a quote terminal; it is the same document, dimmed.
