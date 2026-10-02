---
version: 1
slug: "nba-auction-html"
primary_target: "nba-auction.html"
related_targets: []
---

# nba-auction.html · NBA 拍賣選秀板

Scope: the owner's fantasy-basketball tool for the 2026-27 season (14-team 9-cat H2H league, team 創沒有未來). Visitor mode: **Operate** (the owner is in a task: check standing, judge weak categories, price trade offers and pickups). Phone and desktop equally, all season. Second redesign (2026-10-02): the tactics-board world is retired and replaced by the category standard, at the owner's request after the critique. Every capability, number, rule and the analytic engine stay exactly as they are (PRODUCT.md, NBA section); the auction tools stay in the page, hidden in league mode, for next season's draft.

Binding from the owner (2026-10-02): first view = my standing and weak categories; numbers stay comparable in aligned rows and columns (never split into separate cards); nothing checked often hides behind extra taps; the player table keeps all of its information, only repeated explanation goes.

In this build, from the critique: remove the duplicated explanation (the line restating rank and W–L under the record, the 要補 line that repeats the flagged ranks, the rank legend line; on phones the nine category labels repeated in every league row become one sticky label row); after 套用 keep a receipt with undo instead of the empty state; the roster's remove key is guarded and undoable, with 44px targets.

Memorable moment: the trade result reads like a box score of the deal: who goes, who comes, the weekly dollars, and the nine category swings, and after 套用 the receipt stays on screen with undo.

## Direction contract

THESIS: A clean fantasy-sports data app played straight. White modules on a cool grey page, one violet accent for actions and for "mine", every number in a condensed tabular face, judged by colour and plain labels rather than by a metaphor. It sits beside Yahoo Fantasy, Sleeper, ESPN Fantasy and Basketball Monster at their craft level without borrowing their branding or layouts, and refuses the retired tactics-board costume (magnets, tape, marker hand, aluminium chrome) or any substitute costume.

OWN-WORLD: the canon. Light: cool grey page, white panels with a 1px grey rule and a faint offset shadow, near-black ink with slate secondary text. Violet accent for primary actions, selection, focus and my team (violet tint plus a 我的 badge). Money in green / red with +/−. The blue↔red diverging scale for category heat and ranks, with the number printed in every cell. Dark: near-black page, charcoal panels, lighter tints. Noto Sans TC for all text, Sofia Sans Condensed with tabular figures for every number; no handwriting face. Parts: app bar, section panels with a title row, data tables with sticky column heads, pill tags, chips, standard buttons, a bottom section bar.

STORY: open → my team header (record, rank, $/week, season) → the nine category ranks, weak ones red and labelled 要補, top three blue → the toughest opponent → the league table, one tap opens a roster in place → my margin against every team → my roster → the trade calculator: pick players, read the verdict for both teams and the nine category swings, apply, and a receipt stays with undo → suggested trades and pickups → the player table with search, filters and heat.

FIRST VIEWPORT: phone: app bar (back, title, season, theme) → my team panel: 創沒有未來 with the 我的 badge, 5.7–3.3 largest, a 第 1 名 / 14 pill, +$142/週 in green, the season estimate → the nine-cell category strip → the toughest-opponent line → the league table's first rows. A bottom bar on every width: readout (#1 · +$142/週) and 聯盟 / 交易 / 球員 as 44px keys, 交易 filled violet. Desktop: my team and roster on the left, the league table and 我碰到各隊 on the right, the trade calculator below.

FORM: the category standard (canon), pinned by the owner after the 2026-10-02 critique found the style about 60 % of the problem (「整個拿掉」, a clean data app like the critique's neutral-style capture); bar products Yahoo Fantasy, Sleeper, ESPN Fantasy and Basketball Monster (craft level, not composition). Seed key 18eac78c (direction roll, mode operate, assigned index 4; degraded: the roll service is blocked by this environment's egress policy, so no challengers). Disclosure: the roll was run at the finish, after the build, not before it; the owner's pin beats the roll either way, so the assignment did not change the direction. Code-led (no image generation). Signature interaction: the trade result as the deal's box score (removable player chips, the weekly $ verdict, before → after for both teams, the nine category swings as the headline numbers), then the receipt with undo. Motion is state change only (≤ 200 ms), none under reduced motion.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN-nba.md, and every shipping raster carrying its provenance
