---
name: 投資作戰表 · 計畫存摺
description: The owner's forward investment plan printed as a Taiwanese bank passbook opened flat on its green cloth cover, with pre-printed form-green lettering, dot-matrix navy entries and one red bank-seal ink.
colors:
  desk: "#134a3a"
  desk-ink: "#e4eee6"
  paper: "#eef3e6"
  paper-2: "#e2ead6"
  form: "#2c654b"
  due: "#46765e"
  rule: "rgba(44, 101, 75, .34)"
  rule-2: "rgba(44, 101, 75, .62)"
  ink: "#22305e"
  seal: "#ad2228"
  seal-wash: "rgba(173, 34, 40, .07)"
  dark-desk: "#0a1a13"
  dark-desk-ink: "#cfe0d4"
  dark-paper: "#16231c"
  dark-paper-2: "#1c2b23"
  dark-form: "#8fc6a8"
  dark-due: "#6fa58a"
  dark-rule: "rgba(143, 198, 168, .26)"
  dark-rule-2: "rgba(143, 198, 168, .5)"
  dark-ink: "#cdd8f3"
  dark-seal: "#ff8d8a"
  dark-seal-wash: "rgba(255, 141, 138, .08)"
typography:
  holder-title:
    fontFamily: "'Form Ming', 'Noto Serif TC', 'Songti TC', 'PMingLiU', serif"
    fontSize: "34px"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: ".06em"
  page-head:
    fontFamily: "'Form Ming', 'Noto Serif TC', 'Songti TC', 'PMingLiU', serif"
    fontSize: "21px"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: ".12em"
  fold-head:
    fontFamily: "'Form Ming', 'Noto Serif TC', 'Songti TC', 'PMingLiU', serif"
    fontSize: "15px"
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: ".1em"
  clause-head:
    fontFamily: "'Form Ming', 'Noto Serif TC', 'Songti TC', 'PMingLiU', serif"
    fontSize: "14px"
    fontWeight: 700
    lineHeight: 1.6
    letterSpacing: ".06em"
  form-label:
    fontFamily: "'Form Ming', 'Noto Serif TC', 'Songti TC', 'PMingLiU', serif"
    fontSize: "13px"
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: ".3em"
  column-head:
    fontFamily: "'Form Ming', 'Noto Serif TC', 'Songti TC', 'PMingLiU', serif"
    fontSize: "12px"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: ".14em"
  seal-text:
    fontFamily: "'Form Ming', 'Noto Serif TC', 'Songti TC', 'PMingLiU', serif"
    fontSize: "12px"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: ".04em"
  entry:
    fontFamily: "'Pin Dots', ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0"
    fontFeature: "'tnum'"
  body:
    fontFamily: "system-ui, -apple-system, 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.7
  clause-body:
    fontFamily: "system-ui, -apple-system, 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "14.5px"
    fontWeight: 400
    lineHeight: 1.7
  note:
    fontFamily: "system-ui, -apple-system, 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "12.5px"
    fontWeight: 400
    lineHeight: 1.55
rounded:
  focus: "2px"
  seal-square: "4px"
  page: "8px"
  seal-round: "50%"
spacing:
  page-pad: "26px 30px 22px"
  page-pad-phone: "20px 16px 16px"
  spine: "18px"
  spread-gap: "28px"
  spread-gap-phone: "14px"
  form-row: "10px 0 9px"
  ledger-cell: "9px 6px 8px"
  form-label-col: "88px"
  form-label-col-phone: "74px"
components:
  page:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.page}"
    padding: "{spacing.page-pad}"
  page-head:
    textColor: "{colors.form}"
    typography: "{typography.page-head}"
  form-row:
    textColor: "{colors.ink}"
    typography: "{typography.entry}"
    padding: "{spacing.form-row}"
  ledger-row-due:
    textColor: "{colors.due}"
    typography: "{typography.entry}"
    padding: "{spacing.ledger-cell}"
  ledger-row-printed:
    textColor: "{colors.ink}"
    typography: "{typography.entry}"
    padding: "{spacing.ledger-cell}"
  ledger-row-next:
    backgroundColor: "{colors.seal-wash}"
    textColor: "{colors.ink}"
    typography: "{typography.entry}"
  seal-round:
    textColor: "{colors.seal}"
    typography: "{typography.seal-text}"
    rounded: "{rounded.seal-round}"
    size: "46px"
  seal-round-phone:
    size: "40px"
  seal-square:
    textColor: "{colors.seal}"
    rounded: "{rounded.seal-square}"
    size: "64px"
  form-tag:
    textColor: "{colors.form}"
    padding: "3px 5px 2px"
  fold-summary:
    textColor: "{colors.form}"
    typography: "{typography.fold-head}"
    height: "48px"
  top-bar-link:
    textColor: "{colors.desk-ink}"
    height: "44px"
---

# Design System: 投資作戰表 · 計畫存摺

> Scope: `invest.html` (the investment plan) only. This world is separate from root `DESIGN.md` (trip booklet), `DESIGN-hub.md` (site hub), `DESIGN-livecam.md` (station), `DESIGN-blackjack.md` (pocket LCD), `DESIGN-yacht.md` (regatta) and `DESIGN-nba.md` (fantasy data app).

## Overview

**Creative North Star: "The Plan Passbook"**

The plan is a bank passbook (存摺) opened flat on its own green cloth cover. The desk is the cover, and on it lie three two-page spreads and a back cover. Each spread has pale green security paper with a fine wave guilloche, a stitched spine between the pages and a folio in the corner. The pages are 存戶資料 · 交易明細, then 庫存明細 · 約定事項, then 約定價位 · 短線約定, then the 封底, which holds the folded history. The form is pre-printed in form green: page heads in Ming lettering over a double rule, field labels, column heads, clause numbers. What the plan has to say sits on that form as passbook-printer entries in dot-matrix navy ribbon ink with tabular figures.

Progress is read where the printing stops. Rows whose date has passed are printed in ribbon ink. Rows still to come wait in a lighter green as the planned line, and a dashed red 以下未印 rule marks the place in between. The next row carries a round red 下一筆 seal on a faint red wash. Red is the bank seal's ink and nothing else: the next entry, hard deadlines, stop rules and the 印鑑 box. Gains and losses are never coloured.

The world comes in two states. Light is a green cloth desk with pale paper. Dark is a night desk with dim paper, light ribbon ink and a lighter seal. Two inlined faces carry the world: `'Form Ming'` for what the bank printed and `'Pin Dots'` for what the printer struck. A third voice, the system sans, carries running prose and long notes.

Confirmed rejections (from the direction contract): the finance-dashboard default (metric cards, donuts, red/green tiles); a hero number as the progress readout; and any bank, broker or fund logo, or anything that could pass for a real institution's document.

**Key Characteristics:**
- A green cloth desk, with paper pages arranged in spreads and a stitched spine between them.
- Form green for everything pre-printed and ribbon navy for every entry. One red, the seal.
- The ledger shows progress through printed versus due ink and a dashed 以下未印 line.
- Round and square red seals, rotated a few degrees, are the only marks that look stamped.
- Ruled, tabular and flat: rules and double rules, no cards and no shadows.

## Colors

A three-ink print palette on security paper: pre-printed form green, passbook ribbon navy and bank-seal red, set on a green cloth desk.

### Primary
- **Form Green** (`form`): every pre-printed element: page heads, folios, field labels, column heads, clause numbers and titles, tags, the 印鑑 box label, the ledger row numbers, and the long notes under entries. It reaches 6.1:1 on paper (8.4:1 in dark).
- **Cover Cloth** (`desk`): the page background around the book, the passbook's own cover. Only the top bar sits on it, in `desk-ink`.

### Secondary
- **Ribbon Navy** (`ink`): the printer's ink. Every dot-matrix entry, printed ledger rows, the holder title, clause body text, the ratio-scale bars and the filled meter cells. It reaches 11.3:1 on paper.

### Tertiary
- **Seal Red** (`seal`): bank-seal ink. It marks the next entry (seal, date, `seal-wash` row), the hard-deadline row date (11/04), the 以下未印 cut line, the stop-rule clause and steps, the 提醒 key, the ratio-scale target brackets, focus rings, link hover and text selection.

### Neutral
- **Security Paper** (`paper`) and **Spine Paper** (`paper-2`): the page surface, and the darker strip down the stitched spine.
- **Due Green** (`due`): ledger entries and key samples that are planned but not yet printed. It is lighter than form green and still 4.6:1 on paper, so a due row stays readable. The difference from a printed row is hue and weight of ink, never legibility.
- **Rule** (`rule`) and **Strong Rule** (`rule-2`): 1px row rules, and the 1.5px or 3px double rules for heads, carries and frames. Both are form green at partial alpha.
- **Desk Ink** (`desk-ink`): top-bar text on the cloth (8.5:1).

### Named Rules
**The Seal Ink Rule.** Red is the bank's seal and nothing else. It marks only the next entry, the cut line, hard deadlines, stop rules, the target brackets, the 印鑑 seal and focus. Gains, losses and up/down figures stay in ribbon navy, uncoloured.

**The Printed Line Rule.** A ledger row's ink states its status. Due rows are `due` green, printed rows (date before today) are `ink` navy, and the next row is sealed. Never mark status with a badge, an icon or a background tile.

## Typography

**Display Font:** 'Form Ming' (Noto Serif TC 700 subset, inlined; fallbacks Noto Serif TC, Songti TC, PMingLiU)
**Entry Font:** 'Pin Dots' (generated from GNU Unifont 16-dot bitmaps, one round dot per lit pixel, inlined; fallback ui-monospace)
**Body Font:** system sans (system-ui, PingFang TC, Noto Sans TC, Microsoft JhengHei)

**Character:** Ming serif lettering is the bank's printed form, and pin dots are the printer striking the owner's entries over it. The sans is the plain voice that explains.

### Hierarchy
- **Holder title** (Form Ming 700, 34px / 28px phone, 1.15, .06em, ribbon navy): 投資作戰表 on page 1 only.
- **Page head** (Form Ming 700, 21px, 1.3, .12em, form green): one per page, above a 3px double rule, with the folio (12px, .1em) set at the right.
- **Fold head** (Form Ming 700, 15px, .1em): the back-cover summary.
- **Clause head** (Form Ming 700, 14px, .06em): 第N條 at 12px with .2em tracking, then the clause name.
- **Form label** (Form Ming 700, 13px, .3em, .12em on phones): `dt` labels on the holder page, the slip keys on page 6 (.2em), and the ratio-scale names.
- **Column head** (Form Ming 700, 12px, .14em, nowrap): ledger and table heads over a 1.5px strong rule.
- **Seal text** (Form Ming 700, 12px / 11px): the text inside the seals and tags.
- **Entry** (Pin Dots 400, 16px, 1.5, tabular, `font-synthesis: none`): every dated line, amount, balance, price, percentage and stock code. Nothing is ever bolded or synthesised in this face.
- **Body** (sans 400, 15px, 1.7) and **clause body** (14.5px, 1.7): running prose in ribbon navy. Emphasis inside prose (`.act`, `.pick`, `.stop`) is weight 600 to 700.
- **Note** (sans 400, 12.5–13px, 1.55–1.65, form green): the `.nt` line under each entry, the `.why` / `.pre` / `.fine` / `.skip` lines and the legends.

### Named Rules
**The Form-and-Entry Rule.** If the bank would have pre-printed it (heads, labels, column titles, clause numbers), set it in Form Ming in form green. If the printer struck it (dates, amounts, balances, codes, prices), set it in Pin Dots. Never cross them: no dot-matrix headings and no Ming numerals.

**The Third Voice Rule.** Long CJK notes and running prose are set in the system sans, in form green for notes and navy for prose. The direction contract doesn't name this voice. The build adopted it because long CJK notes in Pin Dots or Ming were hard to read, and the finish review accepted that on ship. Keep it to explanatory lines. It never carries a heading, a label or a figure.

## Layout

The book is a column of spreads (max 1200px, 24px side padding, 28px gap) on the cloth. A spread is a three-track grid, `1fr 18px 1fr`: left page, stitched spine, right page. The pages stretch to equal height, and their outer corners are rounded on the outside edge only. The back cover is a single full-width page.

Inside a page, everything is ruled rows rather than boxes. Form rows use an 88px label column (74px on phones). Ledger cells are padded 9px 6px 8px, with fixed date (92px), amount and balance (76px) columns. The ledger keeps two blank numbered rows before 過次頁, so the page reads as a form with room left. Phrase spans (`.seg`, inline-block) make CJK lines break between phrases, and every note uses `text-wrap: pretty`.

- **≤ 1000px:** the spine goes away and pages stack singly (14px gap), each with all four corners rounded.
- **≤ 600px:** pages pad at 20px 16px 16px and the book at 6px 10px. Ledger rows fold into two-line entries: row number, date, then the summary on line 1, and 存入 / 結存 with sans prefixes on line 2. The seal shrinks to 40px in the top-right corner, and the next-row wash runs 8px past the text edges. Only the first of two consecutive blank rows is shown. The 目標 column of the holdings table is dropped, because the ratio scales show it.

## Elevation & Depth

The book is flat. Depth comes only from print: rules, a 3px double rule under page heads and above warnings, a 1.5px strong rule at carries and frames, a dashed stitched spine, and the paper's guilloche. Nothing has a box-shadow. The round seal uses `mix-blend-mode: multiply` in light mode, so it soaks into the paper and its wash like ink. Dark mode turns the blend off.

### Named Rules
**The Printed Depth Rule.** No shadows, glows or gradients on surfaces. A page sits apart from the desk by colour alone, and anything grouped is framed by a rule.

## Shapes

Pages have 8px corners on their outer edge (left page left-only, right page right-only, all four when stacked or on the back cover). The round seal is a 2px red ring rotated −10°. The key's sample seal is 40px and the ledger seal 46px (40px on phones). The square 印鑑 seal is a 3px red frame with 4px corners rotated −4°, holding two vertical columns of characters (緩衝 / 優先) read right to left, inside a 92px square ruled frame. Form tags and frames are square, with 1px or 1.5px strong-rule borders. The meter is ten 18×10px square cells, one per NT$1,000, with a partial cell. The ratio scale is a 10 %-tick ruler with a solid navy bar for the current value and an open red bracket (1.5px, dashed legs) for the target band. The only curves in the paper are the guilloche waves.

## Components

### Page and spread
- **Page:** `paper` with the guilloche: a 160×36 three-wave SVG tile veiled by a `paper` layer at .89 opacity, so the lines show at about 11 %. It holds a head row (Ming title left, folio right) over a 3px double `rule-2`, 16px above the content.
- **Spine:** an 18px `paper-2` strip with a 2px dashed stitch in `rule-2` (7px on, 7px off) down its centre. Desktop only.

### Holder form (存戶資料)
- A `dl` of ruled rows with a Ming label and a dot-matrix value, followed by a sans note in form green. The 下一筆 value is in seal red, and its note is the day count the script computes.
- The cash meter (`.meter`) has ten cells. Filled cells are navy and the partial cell is a hard-stop navy fill at `--p`.
- The key (這本存摺怎麼看) is a framed legend, with a 1px `rule-2` border and 14px 16px 12px padding. It shows a due date sample, a printed date sample and the seal sample, each beside its meaning.

### Ledger (交易明細)
- Columns are 序, 日期, 摘要, 存入 and 緩衝結存. The first row is 承前頁 and the last is 過次頁, both above a strong rule.
- **Due row:** entries in `due` green. **Printed row:** entries in `ink`. **Hard row:** the date is in seal red. **Next row:** `seal-wash` background, a red date, and the round 下一筆 seal at the right of the summary cell (58px reserved). **Today row:** the same, with the seal reading 今天.
- **Cut line:** a 1.5px dashed seal-red rule labelled 以下未印 (Ming 11px, .2em) at its right end. The script moves it to just above the first unprinted row.
- **Tag:** a square 1px-ruled Ming label (11px) beside a summary, for example 待確認.
- When every row is printed, the page shows the done note (本頁已印滿…) in seal-red Ming.

### Tables (庫存明細, 約定價位, history)
- These share the ledger's head and cell rules. Stock codes are Pin Dots inside a 600-weight name. A sum row sits above a strong rule in form green. On the price page, each stock's group row sits over a strong rule, with the reference close floated right in a form-green note.

### Ratio scales
- Each row has a 74px Ming name, the ruler and a 64px Pin Dots value. A legend below explains the navy bar (current) and the red bracket (target, or a cap for satellites).

### Clauses (約定事項)
- A numbered list of ruled items. Each item has a Ming clause head (第N條 + name) above sans body text. The stop-rule clause is seal red at weight 600.

### Order slip (短線約定)
- A 1.5px strong-rule frame. Its rows have an 88px Ming key, then a bold pick, then a form-green reason. On phones the key stacks above the content. Below the slip come the execution steps: Pin Dots counters, with the two stop steps in seal red. Then 這次不買 and the 提醒 note, which has a red Ming key above a 3px double rule.

### Back cover fold
- A `details` element between strong rules. The summary is Ming 15px, at least 48px tall, with a sans hint and an 18px SVG chevron that turns 180° when the fold is open. Inside are the past trades, the review, the version log and the sources, with wide tables in a horizontal scroller (min 520px).

### Top bar
- It sits on the cloth in desk ink at 13px. On the left is the back link: an SVG chevron on the 24-unit grid with a 1.8 stroke, at least 44px tall, underlined on hover. On the right is the disclaimer.

### Motion
- **Seal stamp:** the next or today seal stamps in once on load. It goes from opacity 0 and scale 1.35 to rest over .18s `cubic-bezier(.2,.8,.2,1)`, after a .25s delay. It plays only with JS and when reduced motion is not requested.
- **Fold chevron:** a .18s ease-out rotation.
- Nothing else moves.

## Do's and Don'ts

### Do:
- **Do** keep every surface either the cloth desk or passbook paper, with pages in spreads joined by a stitched spine on wide screens.
- **Do** set pre-printed form text in Form Ming in form green, every figure, date and code in Pin Dots, and explanatory notes in the system sans.
- **Do** show plan status through ledger ink (due green, printed navy, next sealed) and keep the 以下未印 line where the printing stops.
- **Do** keep red for the seal's jobs only: the next entry, the cut line, hard deadlines, stop rules, target brackets, the 印鑑 seal and focus.
- **Do** run `python3 tools/invest-font.py` after any text edit, so both inlined subsets cover the new characters.
- **Do** keep every text token at or above 4.5:1 on its paper in both themes (`due` is the floor at 4.6:1).
- **Do** fold ledger rows into two lines at ≤ 600px rather than scrolling the table sideways.

### Don't:
- **Don't** add metric cards, donuts, hero numbers or red/green gain-loss colouring.
- **Don't** add any bank, broker or fund logo, or anything that could pass for a real institution's document.
- **Don't** add shadows, glows or surface gradients. Depth is rules and ink.
- **Don't** set headings or labels in Pin Dots, or figures in Form Ming or the sans.
- **Don't** use red for anything a seal would not mark.
- **Don't** add motion beyond the single seal stamp and the fold chevron.
