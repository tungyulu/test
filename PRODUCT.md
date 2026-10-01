# Product

<!-- impeccable:product-schema 1 -->

> Scope: this record covers two surfaces of the personal site **我的小工具** (GitHub Pages, `https://tungyulu.github.io/test/`): the **site hub** (`index.html`, section directly below) and the **Japan autumn road-trip itinerary** (`trip.html`, every section after the hub section). The other pages (betting tracker, yacht dice, usage dashboard, golf analyzer, blackjack pages, investment notes, Yōtei checklist, NBA draft board, etc.) are independent personal tools with their own looks and are not described here beyond their one-line entry in the hub.

## Site hub · 我的小工具 (`index.html`)

**Users.** The owner (Traditional Chinese, Taiwan), on phone and desktop about equally, opening the hub to jump into one of their tools. The hub link is also shared with friends, who should understand what each tool is from its entry alone.

**Purpose.** The front door to twelve single-file tools. Success: the owner finds and opens any tool in a couple of seconds, and a friend can tell what each one does and pick one that interests them.

**Content (confirmed grouping, in this order).**
- 旅行: 關東秋季紅葉巡航 (`trip.html`), 東京近郊即時影像 (`livecam.html`)
- 遊戲: 快艇骰子 (`yacht.html`), 21點實戰牌桌 (`blackjack-game.html`), 21點機率決策挑戰 (`blackjack.html`), 羊蹄山戰鬼 收集清單 (`yotei.html`)
- 運動: NBA 拍賣選秀板 (`nba-auction.html`), 高爾夫球軌跡追蹤 (`golf.html`), 運彩投注紀錄 (`betting.html`)
- 理財與筆記: 投資作戰表 (`invest.html`), Dyson 選購比對 (`dyson.html`), Usage Dashboard (`usage.html`)

**Constraints.** Static single HTML file at the Pages root, no build step. The name 「我的小工具」 is kept. The hub never restyles the tools themselves; each keeps its own look. Every tool must stay reachable; adding a tool later must be a small, obvious edit. No tracking, accounts or invented usage numbers: the hub does not know how often a tool is used.

**Evidence on hand.** The tool names, file names and one-line descriptions from the existing hub and CLAUDE.md. No screenshots, logos or usage data exist; none may be invented.

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
