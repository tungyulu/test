# Product

<!-- impeccable:product-schema 1 -->

> Scope: this record covers three surfaces of the personal site **我的小工具** (GitHub Pages, `https://tungyulu.github.io/test/`): the **site hub** (`index.html`), the **blackjack table** (`blackjack-game.html`) and its strategy trainer (`blackjack.html`), which share one look, the trip's **live-camera page** (`livecam.html`), the **Yacht dice game** (`yacht.html`), the **NBA fantasy board** (`nba-auction.html`) and the **investment plan** (`invest.html`), each in its own section directly below, and the **Japan autumn road-trip itinerary** (`trip.html`, every section after them). The other pages (betting tracker, usage dashboard, golf analyzer, Yōtei checklist, Tamagotchi guide, etc.) are independent personal tools with their own looks and are not described here beyond their one-line entry in the hub.

## Site hub · 我的小工具 (`index.html`)

**Users.** The owner (Traditional Chinese, Taiwan), on phone and desktop about equally, opening the hub to jump into one of their tools. The hub link is also shared with friends, who should understand what each tool is from its entry alone.

**Purpose.** The front door to thirteen single-file tools. Success: the owner finds and opens any tool in a couple of seconds, and a friend can tell what each one does and pick one that interests them.

**Content (confirmed grouping, in this order).**
- 旅行: 關東秋季紅葉巡航 (`trip.html`), 東京近郊即時影像 (`livecam.html`)
- 遊戲: 快艇骰子 (`yacht.html`), 21點實戰牌桌 (`blackjack-game.html`), 21點機率決策挑戰 (`blackjack.html`), 羊蹄山戰鬼 收集清單 (`yotei.html`), 塔麻可吉樂園攻略 (`tamagotchi.html`)
- 運動: NBA 拍賣選秀板 (`nba-auction.html`), 高爾夫球軌跡追蹤 (`golf.html`), 運彩投注紀錄 (`betting.html`)
- 理財與筆記: 投資作戰表 (`invest.html`), Dyson 選購比對 (`dyson.html`), Usage Dashboard (`usage.html`)

**Constraints.** Static single HTML file at the Pages root, no build step. The name 「我的小工具」 is kept. The hub never restyles the tools themselves; each keeps its own look. Every tool must stay reachable; adding a tool later must be a small, obvious edit. No tracking, accounts or invented usage numbers: the hub does not know how often a tool is used.

**Evidence on hand.** The tool names, file names and one-line descriptions from the existing hub and CLAUDE.md. No screenshots, logos or usage data exist; none may be invented.

## Blackjack table · 21點實戰牌桌 (`blackjack-game.html`)

**Users.** The owner, on phone and desktop about equally (one-handed phone sessions matter as much as a desk session with the data panels open). Linked from the hub, so friends open it too.

**Purpose.** A playable blackjack table with virtual chips that doubles as a basic-strategy gym. Playing feel and learning matter equally: the table is the lead, and the coaching and odds stay one glance away, never buried. Success: a round deals, plays and settles with real table feel, and after any decision the player can see whether the chart agrees and why.

**Capabilities that must survive any redesign.**
- The rule set, shared with `blackjack.html`: 6 decks, S17, DAS, late surrender, dealer peek, blackjack 3:2, split to 4 hands, split aces one card, insurance / even money 2:1. Every two-card hand must give the same chart answer on both pages.
- Casino-style betting: pick a chip (10 / 50 / 100 / 500), tap a bet circle. Main bet 10–2,000 (required); side bets 完美對子 Perfect Pairs and 21+3, each ≤ 500. Undo, clear, last bet, double the bet, deal; deal-same-bet after a round; a 1,000 refill when broke.
- A real shuffled 6-deck shoe with a 72–78 % cut card; 0–4 computer players seated before the user who play perfect basic strategy.
- Actions hit / stand / double / split / surrender, with insurance and even money when the dealer shows an A.
- The strategy coach grading every decision, an optional 策略提示 that marks the recommended action, the full 繁體中文 strategy chart and the rules-and-probability explainer.
- Live odds (next-card bust, dealer final distribution, stand outcome, dealer up-card strength, dealer blackjack chance during insurance), the side-bet paytable with exact odds and house edge, shoe penetration and the Hi-Lo running / true count (hidden until shown), stats and recent-round history.
- An always-visible 本次輸贏 (session net); the data panels can be hidden as a whole and collapsed one by one; keyboard shortcuts (1–4, Backspace, C, Space/Enter, H S D P R, Y/N, B, Esc).
- Nothing is saved, by request: a refresh restarts at 1,000 chips with empty stats and default switches.
- Static single self-contained HTML file (no CDN), Traditional Chinese.

**The trainer (`blackjack.html`, 21點機率決策挑戰).** The same device, as a drill page: a 10 / 20 / 50 / 100-question challenge of random hands (including insurance questions) graded against the same strategy tables, with score, streak and accuracy, a four-part explanation after each answer, next-card bust odds, a per-situation Monte Carlo EV comparison (1,000 / 4,000 / 10,000 runs), the strategy chart and rules leaflet, and an end-of-round summary. Nothing is saved.

**Evidence on hand.** The rule texts, paytables and strategy tables already in the two pages. Chips are virtual; nothing may suggest real-money play, a real casino brand or invented odds.

## Live cameras · 東京近郊即時影像 (`livecam.html`)

**Users.** The two travellers of the trip, on phone and desktop about equally, and equally before the trip (at home, looking at the places) and during it (on the road in Kanto). Linked from the hub and from `trip.html`.

**Purpose.** Show what the trip's places look like right now and whether now is the time to go. Opening the page answers today's plan and the weather there first (before the trip: day 1), cameras second. Success: in a few seconds either traveller knows what is booked today, what to wear where they are going, whether Fuji is out, and can open a live camera of any stop.

**Capabilities that must survive any redesign.** About a hundred verified YouTube live cameras grouped by region and area with Chinese names, live frame thumbnails refreshed every minute (only while on screen), 載入中 / LIVE / 夜間 / 停格 / 無畫面 states from frame loading, the network and the sun position (a YouTube placeholder is 無畫面), the last good weather kept for offline use, favourites, region and mode filters (收藏, 自駕・路面, 富士山); TW and JP clocks; Open-Meteo weather per area with clothing advice, a ticker and a comparison table, a pack list, Fuji visibility from cloud / code / visibility, a road reading (not official road status) and the 2026-09-01 30 km/h residential-road law note with official links; three automatic picks with their reason; the 8-day trip panel that mirrors `trip.html` (route, note, that day's weather or forecast, that day's cameras); light / dark / system theme; the credits and legal notes (no images stored or rebroadcast; weather CC BY 4.0).

**Evidence on hand.** The camera list, routes and notes already in the page and `trip.html`. Readings (rec, Fuji, road) are derived estimates and must say so; nothing may suggest official status.

## Yacht dice · 快艇骰子 (`yacht.html`)

**Users.** The owner, on phone and desktop about equally, alone against the CPU or with a friend passing one device. Linked from the hub's 遊戲 lot.

**Purpose.** A quick game of Yacht that is fun to watch: the race between the two scores should be visible at a glance, not read off a table. Success: a turn is roll → keep → roll → pick a row with no explanation needed, and either player can tell who is ahead and by how much from across the table.

**Capabilities that must survive any redesign.** Five dice, up to three rolls a turn, holding any dice between rolls; thirteen categories (一點–六點, 三同, 四同, 葫蘆 25, 小順 30, 大順 40, 快艇 50, 機會) with the upper bonus of 35 at 63; 1P vs CPU (the greedy CPU: best-scoring open row, holds for it, rerolls twice) and 2P on one device; a preview of every open row's score for the current roll; the final board with the winner or a tie; a way back to the hub. Nothing is saved (by design: a refresh starts a new game). No new rules or features without the owner asking.

## NBA fantasy board · NBA 拍賣選秀板 (`nba-auction.html`)

**Users.** The owner, manager of the team 創沒有未來 in a 14-team 2026-27 fantasy league on Yahoo, on phone and desktop about equally, all season long. Linked from the hub's 運動 lot.

**Purpose.** Built as an auction board for the 2026-09-29 draft; since the draft it is the owner's season tool. Opening the page answers "where does my team stand and what is weak" first (rank, average categories won per week, the weekly money at the league's bet, weak categories), then the 14-team table, the trade calculator, suggested trades and free agents. Success: in a few seconds the owner knows their standing and what to fix, and can price any trade offer from a league-mate in a few taps.

**Capabilities that must survive any redesign.**
- The league's rules: traditional 9-cat (PTS, REB, AST, STL, BLK, 3PM, FG%, FT%, TO), head-to-head with every category its own win or loss, daily lineups, 14 teams of 14 (11 starters + 3 bench), 4 IL slots, $200 auction; the bet is $60 × (categories won − lost) per week over a 20-week regular season.
- About 240 hand-made 2026-27 projections and the valuation built on them: per-game z-scores, suggested price, the 0–100 recommendation index with S/A/B/C/D grades, the tags (值得搶, 易溢價, 適合 punt, rookie classes), each player's nine-category heatmap, punt toggles that re-price everything.
- League mode: the 聯盟戰力 table (14 teams by weekly W–L and $/week, nine category ranks, each roster with draft price against value, strengths and weaknesses); my team's rank, weekly record, $/week and season estimate, category ranks and weekly margin against every team; the 交易試算 calculator (any players with any team or the free-agent pool, before → after for both teams and the nine category win rates, apply and undo); 1-for-1 trade suggestions that do not hurt the partner and pass the draft-price check, and free-agent pickups; changing any player's owner; the two-step 還原成選秀名單.
- The auction tracker (budget, max bid, inflation, tiers, $200 plans, tips) stays in the page for next season's draft and is hidden in league mode.
- Search, sort, position / rookie-class / 值得搶 / free-agent filters; tooltips on heat cells and tiers.
- Rosters, applied trades and settings persist per device (localStorage `nba-auction-2026-v1`); a new embedded draft list (`DRAFT_ID`) replaces local edits on every device.
- The league numbers come from the analytic engine (no sampling noise); the 14 fantasy team names show exactly as the managers named them.
- Static single HTML file on GitHub Pages, Traditional Chinese.

**Binding preferences (2026-10-02).** Numbers stay easy to compare: league, roster and player data stay in aligned rows and columns, never split into separate cards. Nothing the owner checks often (standing, category ranks, trade results) hides behind extra taps or nested panels.

**Brand commitment (2026-10-02, after the critique).** The owner retired the tactics-board look (it read as cheap: hardware chrome, magnets and tape on every element, a handwriting face for numbers). The page is the category standard played straight: a clean fantasy-sports data app at the craft level of Yahoo Fantasy, Sleeper, ESPN Fantasy and Basketball Monster. Those products set the bar for finish, not a template to copy: none of their branding, colours-as-identity, logos or layouts. No metaphor costume of any kind. The player table keeps all of its information; only explanation that repeats what is already on screen goes.

**Evidence on hand.** The projections (estimates compiled 2026-09-28 from ESPN's rankings, team news and 2025-26 stats, with camp-news adjustments), the official 196 draft picks, the league's rosters as re-pasted on 2026-10-05 (every trade and pickup since the draft, 200 players including IL) and the team names exactly as the league shows them. The projections are estimates and the page says so. No NBA, team or Yahoo logos and no player photos are on hand; none may be added or imitated, and nothing may look like an official NBA or Yahoo product.

## Investment plan · 投資作戰表 (`invest.html`)

**Users.** The owner (Traditional Chinese, Taiwan), a small retail investor in Taiwan stocks and ETFs, on phone and desktop. Linked from the hub's 理財與筆記 lot; the page is public on GitHub Pages, so it never shows account numbers or the owner's name.

**Purpose.** The owner's own forward plan for the portfolio: what happens next and how far the plan has come. Opening the page answers "where is the plan now" first (the next dated action, the cash buffer against its floor, the open short-term position and its exit date), then the standing rules, the price conditions, the current allocation against its targets and the short-term ETF choice. Success: in a few seconds the owner knows the next thing to do and whether any rule applies today.

**Content that must survive any redesign.**
- The monthly DCA: 0050 NT$15,000 + 00878 NT$5,000 (the whole NT$20,000), never paused; 0050 is not sold to rebalance.
- The cash buffer: floor NT$10,000, at NT$3,168 after the 2026-09-29 sale; it fills from selling one MediaTek share when the price is ≥ 5,000, 00878 dividends and extra income; kept outside the settlement account.
- The rules: individual stocks and theme / active ETFs only with extra money, at most 20 % together and 6 % per stock; known large expenses saved ahead by lowering that month's DCA; the emergency sell order buffer → satellites → 00878 → 0050; sale proceeds are not reinvested before their purpose is done; no buying after a +5 % gap.
- The October short-term plan (decided 2026-10-05): with about NT$40,000 of extra money, top the buffer up first (~6,832), then at most ~33,000 into one active ETF — 00981A, or 00985A for lower volatility — with a −8 % stop and a full exit before 11/4 so cash settles 11/6, before the 11/7 trip.
- The price conditions: MediaTek (sell 1 at ≥ 5,000, buy back < 4,500, re-check < 3,900), GUC (1 share at 5,600–5,800, 1 more at 5,200–5,400, cap 2, no chase > 6,300, re-check < 4,900), Shin Zu Shing (wait for October revenue), Macronix (no buy-back), 00757 (hold).
- Current holdings in brief (value, share, role) and the allocation targets: 0050 70–80 %, 00878 15–25 %, satellites ≤ 20 %.
- Past material (the 9/29 trades, the September review, the version log and every source) stays reachable but folded away at the end, by the owner's choice on 2026-10-05.
- Static single self-contained HTML file, Traditional Chinese; gains and losses are never coloured red/green (Taiwan broker apps use red = up).

**Evidence on hand.** The holdings snapshot from the 2026-09-29 broker screenshot, the 9/29 trade records, prices and fund facts from 10/1–10/2 search results (cited on the page). Everything is the owner's personal note, not investment advice, and the page says so. No bank, broker or fund logos; nothing may look like a real bank's or broker's document.

---

# Trip itinerary (`trip.html`)

## Platform

web

## Users

Two travellers, the owner and one travel companion, each opening the page on their own phone (Traditional Chinese, Taiwan). The same two people use it in two equally important moments:

- **Before the trip, at home:** reading the plan, comparing optional stops, ticking off the pre-trip checklist, recording bookings as they land.
- **During the trip, on the road in Japan:** a quick glance at today — where we go, what is booked and at what time, which restaurant, one tap to Google Maps — often from a passenger seat, a train platform or a shop, frequently with poor or no mobile data.

## Product Purpose

A single personal itinerary for an 8-day, 7-night trip, 2026-11-07 (Sat) to 11-14 (Sat): three self-drive days (Hakone → Kawaguchiko → Enoshima/Kamakura → Yokohama) followed by four days based in Tokyo. It holds the day-by-day plan, every confirmed booking, lodging, food candidates, transport details and a pre-trip checklist in one place.

Success: either traveller can answer "what are we doing today, and what can't we miss?" in a few seconds on a phone, offline, and the plan reads as a relaxed trip rather than a schedule to keep up with.

## Positioning

Not a travel app or a template. It is this one trip, written by the people taking it: real booking numbers, real deadlines, and opinions about which stops are optional. Its job is to separate the few hard commitments (flights, car return, reservations) from the large pool of nice-to-have options, and to know what day it is.

## Operating Context

- Phones first (≈390 px wide); desktop is occasional.
- Poor or absent connectivity is the normal case on the road; the page must render fully styled with no network.
- Navigation happens through Google Maps links; Suica/trains in Tokyo; a rental car (Toyota GR Yaris) on days 2–4.
- A companion live-camera/weather page, `livecam.html`, is linked from the itinerary and mirrors its eight days.

## Capabilities and Constraints

Must be preserved in any redesign:

- All content: flights (CX450 / CX451), eight day plans, lodging for every night, food candidates by area, transport (rental car booking, N'EX, drive routes, Tokyo rail routes from the hotel), pre-trip checklist, rain/alternate plans, shopping and ACG lists.
- Confirmed bookings and their hard facts: Toyota Rent-a-Car 関内店 (reservation 98119828100, pick-up 11/08 10:30, return **11/10 20:00**, shop closes at 20:00); Hotel BUSTEL (D1), Super Hotel 富士河口湖 (D2), Enoshima Hotel (D3), APA Yokohama Bay Tower (D4), Minn 日本橋水天宮前 (D5–D7); 焼肉 あぶる。池袋店 11/11 **19:30**, 2 people, Tabelog GYSPCX8TK7 (10 minutes late without calling counts as a no-show).
- Open deadlines still to act on: Nissan HQ Gallery FAIRLADY Z test drive booking opens **10/28** (and whether a Taiwan licence + Japanese translation is accepted must be confirmed first).
- Pre-trip checklist state persists per device (localStorage `trip-checklist-v1`, keyed by stable item ids).
- Knows the date: countdown before departure; during the trip, opens on today's day and marks it.
- Deep links to a day or section; Google Maps link per place; printable.
- Static single HTML file on GitHub Pages, no build step, no runtime CSS framework (offline).
- The earlier versions stay reachable from the current page: `trip-v2.html` (the 旅のしおり booklet) and `trip-v1.html` (the first tabbed page).
- Optional material (timelines, alternates, shopping lists, sightseeing notes) stays available but out of the way.

User-stated preferences that bind:

- A visible hour-by-hour timeline on the plan "feels like pressure" — time estimates may exist only on request.
- Nothing may waste horizontal space on a phone (a decorative left rail was explicitly rejected).
- The page name "Autumn Road Trip / 關東秋季紅葉巡航" is open to change in the redesign.

## Evidence on Hand

Real content only: the bookings, addresses, phone numbers and links already in `trip.html`. There are no trip photos, logos or illustrations; none may be presented as the travellers' own. The companion is referred to only as "同行的人"; their name is not recorded. Eri is the travellers' chihuahua (pet-shop picks mention her).

## Product Principles

1. **Hard commitments first, options second.** A booking time or a deadline must never be as easy to overlook as a suggestion.
2. **Today, at a glance.** The page should answer "what now?" before it answers "what else?".
3. **Relaxed, not scheduled.** Frame days as a plan with slack, not a minute-by-minute programme.
4. **Works in the field.** Offline, one-handed, sunlight, patchy data.
5. **Everything is kept, not everything is shown.** Optional detail is one tap away, never deleted.

## Accessibility & Inclusion

Readable outdoors on a phone: body text meets WCAG AA contrast; tap targets comfortable for one-handed use; respects reduced-motion.
