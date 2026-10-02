---
version: 1
slug: "nba-auction-html"
primary_target: "nba-auction.html"
related_targets: []
---

# nba-auction.html · NBA 拍賣選秀板

Scope: the owner's fantasy-basketball tool for the 2026-27 season (14-team 9-cat H2H league, team 創沒有未來). Visitor mode: **Operate** (the owner is in a task: check standing, judge weak categories, price trade offers and pickups). Phone and desktop equally, all season. Full redesign: new world. Every capability, number, rule and the analytic engine stay exactly as they are (PRODUCT.md, NBA section); the auction tools stay in the page, hidden in league mode, for next season's draft.

Binding from the owner (2026-10-02): first view = my standing and weak categories; numbers stay comparable in aligned rows and columns (never split into separate cards); nothing checked often hides behind extra taps.

Memorable moment: the coach's red marker circles drawn around the weak category ranks on the owner's own board, and a trade's verdict written in marker next to the magnets that moved.

Unresolved: whether the hidden auction cards get a war-room board treatment now or when next season's draft starts (default: restyled in the same world, still hidden).

## Direction contract

THESIS: The page is the manager's locker-room tactics board. The model's numbers are printed on the board and on magnetic name strips; the coach's dry-erase marker does the judging: red circles around weak category ranks, blue ticks on strong ones, the weekly money written in green, a trade drawn as arrows between magnets. It refuses the category default: a dark sports-analytics dashboard of KPI tiles, neon accents and player headshots, and its opposite, a plain white spreadsheet.

OWN-WORLD: cool white melamine with faint erased-marker ghosting; aluminium frame rails with black corner caps and a marker tray; printed board-blue court lines and ruled grids; laminated label tape (white, mine yellow) for every name and heading; flat magnet strips for players and teams; small square magnet tiles for category ranks (blue strong, red weak); four marker inks only (black, blue, red, green); round magnets as toggles; a felt eraser for resets. Night: the black glass board with liquid-chalk inks. Printed text in Noto Sans TC with a condensed printed numeral face; marker hand only for digits, Latin, ticks, circles and arrows.

STORY: open → my board: rank, weekly W–L, money per week, the red-circled weak categories, the toughest opponent → the 14-strip league board, one tap opens any roster in place → a trade offer arrives: on the trade board tap magnets to send / get, read the marker verdict for both teams and all nine categories, apply it → coach's notes list suggested trades and pickups → the name-strip wall of players for search, filters and heat.

FIRST VIEWPORT: phone: thin aluminium top rail (back link, title tape, theme) → my board: yellow tape 創沒有未來, marker #1 circled with /14, 5.7–3.3 large, +$142/週 in green, season total small → the nine printed category cells with my ranks, red circles on weak, blue ticks on strong → toughest-opponent line → the league board's first strips. A sticky marker tray at the bottom holds 聯盟 / 交易 / 球員 and the compact readout; 交易 is the primary action. Desktop: my board and the league board side by side above the fold, the trade board directly below.

FORM: 戰術板 (coach's magnetic tactics whiteboard: melamine, aluminium frame and tray, label tape, magnet strips, dry-erase marks), position 3 of my ordered list (1 scorer's box score, 2 PTT NBA board, 3 tactics board, 4 arena scoreboard, 5 sports-paper front page, 6 card price guide, 7 draft war room), seed key 98ed6dcf (degraded roll: roll service unreachable, no challengers), chosen by the owner. Code-led (no image generation). Signature interaction: tapping a magnet lifts it onto the trade lane, the verdict's marker strokes draw themselves and the weekly delta is written in green or red; applying snaps the magnets onto the other team's rail. Motion is lifting, snapping and marker strokes only (150–250 ms); reduced motion places everything instantly.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
