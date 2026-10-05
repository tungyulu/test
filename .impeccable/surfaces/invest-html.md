---
version: 1
slug: "invest-html"
primary_target: "invest.html"
related_targets: []
---

# invest.html · 投資作戰表

Scope: the owner's forward investment plan. Visitor mode: **Operate** (the owner checks where the plan stands and what to do next). Phone and desktop. Redesign on 2026-10-05 at the owner's request: replace the report look (verdict panels, chips, many sections) and show only the future plan; past material folds into one collapsed section at the end. Product truth: PRODUCT.md, investment section.

Binding from the owner (2026-10-05): the first view answers "how far has the plan come"; past info (9/29 trades, September review, versions, sources) is collapsed, not shown; current holdings stay, but only value, share and role.

Memorable moment: the plan reads as a passbook. Dated future entries are pre-printed; entries whose date has arrived print in ink, and a red 「下一筆」 seal sits on the next one, so where the printing stops is where the plan is.

## Direction contract

THESIS: The plan as a Taiwanese bank passbook (存摺), opened flat. The page refuses the finance-dashboard default (metric cards, donuts, red/green tiles) and the report it replaces: progress is read where the printed ledger stops, not from a hero number.

OWN-WORLD: cover-green desk (#134a3a) around pale green security-paper pages with a fine guilloche; pre-printed form lettering and rules in form green, entries in dot-matrix navy ink with tabular figures, one red bank-seal ink for the next entry, deadlines and stop rules. Parts: page spreads with a stitched spine, ruled ledger with row numbers and 承前頁 carry-forward, numbered 約定事項 clauses, a 約定價位 table, a 庫存 page with ruled ratio scales, round red seals. Dark: night desk, dim paper, light ink.

STORY: open → 存戶頁 + 交易明細 spread: next entry sealed, buffer 結存, the short-term exit date → 庫存明細 (holdings and targets) → 約定事項 (rules) → 約定價位 (price conditions) → 短線約定 (the ETF choice) → back page with the folded history.

FIRST VIEWPORT: desktop: one passbook spread across the viewport, left page 存戶資料 (title, plan version, monthly DCA, buffer floor, short-term status with days to 11/4), right page the ledger from 承前頁 3,168 through 12/07, the 下一筆 seal on 10/07. Phone: the 存戶頁 summary then the ledger as two-line entries.

FORM: bank passbook, IMPECCABLE'S PICK (position 1 on the ordered list), chosen by the owner over the assigned 工程告示牌 (position 4) and the canon; seed key 6d5eb978 (direction, operate, degraded: no challengers, roll service blocked). Code-led (no image generation). Signature interaction: date-aware printing (rows on or before today print in ink, the next row gets the seal stamp, a day count to the next entry and to 11/4), computed on load; motion only the seal's stamp (≤ 200 ms), none under reduced motion.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
