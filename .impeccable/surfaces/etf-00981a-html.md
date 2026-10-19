---
version: 1
slug: "etf-00981a-html"
primary_target: "etf-00981a.html"
related_targets: []
---

# etf-00981a.html — 持股異動日報 (00981A, 00403A, 00988A, 00411A)

2026-10-19: the page now serves four Uni-President active ETFs behind folder tabs above the sheet (`?f=TICKER`). The contract below still holds for each fund; global funds (00988A, 00411A) count foreign stocks in shares, print prices with their currency and convert amounts to NTD. An overview tab (`?f=ALL`) uses the same notice form for all four funds on one day: 主旨, 說明 共同買進 / 共同賣出 / 看法分歧, 附表 per fund.

Scope: one page, Operate mode. Audience: the owner, mostly on a phone after the close (evening, indoors), checking what the 00981A manager bought and sold today. Job: today's buys and sells first, then the holdings' day change, then any stock's history. Constraints: every existing function stays (day picker, 1/5/20/60-day comparison, contribution, sortable/searchable holdings, parked rule, per-stock history and trade log, hash state, theme); the user rejects "too fancy / hard to read" and "information hidden behind taps". Not an official notice: the page names its source and says it is a personal summary.

## Direction contract

THESIS: The day's basket read as a formal disclosure notice: one 主旨 sentence says what the manager bought and sold, numbered 說明 items carry buys and sells as two hard halves in ruled tables. It refuses the broker-app card dashboard and the dark quote terminal.

OWN-WORLD: A white document sheet on a blue-grey desk; ink-black text; 1px blue-grey ruled cells with pale-blue header rows; an ink-reversed title bar; 主旨 / 說明 / 附表 labels in a Kai face; three type sizes only (24 / 15 / 13), rank by weight, reversal and rules; navy appears only on pressable things; red / green only for price change; buy / sell state as line form (double = new, solid = add, dashed = cut, outlined and struck = out).

STORY: The owner reads the 主旨 in one breath, checks lots and amounts in 說明一 / 二, glances at 說明三 / 四 for the market and who pulled the fund, and opens any stock in place for its history.

FIRST VIEWPORT: At 390px: a thin utility bar; the reversed title bar 「00981A 持股異動日報」; a ruled header grid (資料日期 in ROC form with weekday, 第 N 號, the comparison select, previous / next keys); the 主旨 label and the 24px sentence whose stock names are links; 說明一 買進 begins above the fold. On desktop 說明一 and 說明二 sit side by side as equal halves.

FORM: assigned candidate 5 of 7 (公開資訊觀測站 重大訊息 × 公文 主旨／說明), seed key 32b86c9b. Signature interaction: a stock opens its history in place, under the row or cell that was tapped (one open at a time), never in a modal. Motion: only the detail opening (≤200 ms), none under reduced motion.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
