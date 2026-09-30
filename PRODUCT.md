# Product

<!-- impeccable:product-schema 1 -->

> Scope: this record covers the **Japan autumn road-trip itinerary** (`trip.html` and its redesign). The other pages in this repository (betting tracker, yacht dice, usage dashboard, golf analyzer, blackjack trainer, investment notes, etc.) are unrelated personal tools and are not described here.

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
