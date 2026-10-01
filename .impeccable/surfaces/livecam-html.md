---
version: 1
slug: "livecam-html"
primary_target: "livecam.html"
related_targets: []
---

# livecam.html · 東京近郊即時影像

Scope: the live-camera / weather companion page of the trip. Visitor mode: **Operate**. Phone and desktop equally; used equally before the trip (at home, browsing the places) and during it (on the road in Kanto, checking today). The owner asked that the page open on **today's itinerary and weather**, cameras second. Full redesign: new world, every function kept (cameras + thumbnails + favourites + filters, weather ticker/grid, clothing advice, pack list, Fuji visibility, road reading + 30 km/h law note, recommendations, 8-day trip panel mirroring trip.html, theme toggle, legal/credits).

## Direction contract

THESIS: The page is a Japanese railway station. Today's plan is a dot-matrix departure board, the weather and Fuji are the 運行情報 status display, and every camera area is a white 駅名標 standing on the trip's route, with its cameras hung below like platform ITV monitors. It refuses the category default: a dark CCTV wall of same-size thumbnail cards under a hero.

OWN-WORLD: platform concrete ground; white enamel signs with a line-colour band (TK yellow-green, YS sky blue, HF orange, IZ teal, my own codes); station numbering badges (colour-ringed square, letters + number); black LED housing with amber / green / red 16-dot LEDs drawn dot by dot from GNU Unifont bitmaps, unlit dots visible; yellow 出口 exit sign for the way home; navy 案内 poster heads; filled JIS-style pictograms; Noto Sans TC for Chinese, Hind for romaji.

STORY: open → see what today is (or D1 before the trip), what is booked at what time, the weather and what to wear there, whether Fuji is out → pick a place → walk the line to its sign → tap a monitor to watch live on YouTube.

FIRST VIEWPORT: phone: exit sign + title strip (≤ 84px), then the LED departure board full width: header (day, countdown / 今天, LED clock JP + TW), the day title, one row per route step (time green, step amber, long rows scroll dot by dot), the note row in red; D1–D8 track plates under it; then the white "這天" panel: weather rows with wear pictograms and the day's camera list. Desktop: board + day panel on the left, 運行情報 (Fuji lamps, weather ticker, law sign, picks) on the right.

FORM: 車站告示系統 (発車標 + 駅名標 + 運行情報), position 7 of my ordered list, seed key 2a86da37 (degraded roll, no challengers). Signature interaction: choosing a day wipes the board column by column and redraws it; long rows scroll in whole-dot steps; prev / next on each 駅名標 walks the line. Motion is LED grammar only (whole-dot steps); signs never animate.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
