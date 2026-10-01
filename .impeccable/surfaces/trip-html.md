---
version: 1
slug: "trip-html"
primary_target: "trip.html"
related_targets: []
---

# trip.html · 關東秋季紅葉巡航 (station edition)

Scope: `trip.html`, third version of the trip itinerary, rebuilt in the station world of `livecam.html` (DESIGN-livecam.md) at the user's request (「改得跟 livecam.html 類似的風格，帥一點」). The previous booklet is `trip-v2.html` (its own world, root DESIGN.md) and the first version `trip-v1.html`; both stay reachable from the new page. Visitor mode: **Read** with Operate moments (glance at today, act on bookings, tick the checklist). Every piece of content and function of trip-v2 survives (PRODUCT.md › Trip itinerary): bookings and deadlines, eight days, lodging, transport, food, checklist with localStorage `trip-checklist-v1` ids (plus the new item 11/5 12:50 劃位・Visit Japan Web), 到著章 stamps (`shiori-stamps-v1`), today logic, deep links and old hash aliases, print, offline (no font / CSS / icon CDN: fonts, LED glyphs and pictograms are inlined).

## Direction contract

THESIS: The whole trip is one station, read from its concourse map. Eight days are eight platforms (1–8番線) on four island platforms; lodging, transport, food and the pre-trip checklist are the station's facilities (飯店口, みどりの窓口, 美食街, 改札口). The map is the contents; each platform below carries a 駅名標 for that day's place, its tickets for the hard commitments and 案内 boards for the rest. It refuses a stack of paper sections or a card timeline.

OWN-WORLD: livecam's world, unchanged: concrete ground, white enamel signs with line-colour bands (TK yellow-green Tokyo, YS sky blue Yokohama/Shonan, HF orange Hakone/Fuji), ringed number badges, black LED housing with amber / green / red Unifont dots, navy 案内 heads, yellow 出口 sign, filled JIS-style pictograms. Added for this surface: yellow 点字ブロック tactile edges on the island platforms, rails between them, pale green マルス tickets for bookings, red ink only for hard commitments.

STORY: open → the LED board says the trip, the dates and how many days are left (or which platform is today) → the concourse map shows all eight days and the facilities at once → tap a platform → its 駅名標, the day's tickets, then the plan → press the 駅スタンプ.

FIRST VIEWPORT: phone 390: exit sign + title strip (≤ 84 px), the LED departure board (trip name, dates, route, countdown / today in red), a row of keys (今天的頁 when travelling, 行前準備 n/16), then the top of the 構內圖 map: facility tiles and the first island platforms (1・2番線). Desktop: board and map side by side above the fold.

FORM: 車站構內圖, position 5 of my seven structural candidates, dealt by surface seed 3b0ffb80 (degraded roll) and chosen by the user. Signature interaction: the map's platforms are the navigation (today's platform lit, past platforms marked), and the LED board's countdown / today row; 駅スタンプ press keeps the old stamp mechanism. Motion: LED grammar only (whole-dot scroll, board wipe on load), the stamp press; signs never animate.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
