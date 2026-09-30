---
version: 1
slug: "trip-html"
primary_target: "trip.html"
related_targets: []
---

## Scope

`trip.html`: a full redesign of the trip itinerary. The pre-redesign page was renamed `trip-v1.html` and stays reachable from the new page (tab strip 「舊版」 and the back cover). Visitor mode: **Operate** (glance at today, act on bookings), with long-form reading before the trip.

Audience and job: the two travellers, on their own phones, before and during the trip (PRODUCT.md). Must carry every piece of content and function from `trip-v1.html` (see PRODUCT.md › Capabilities and Constraints), share the checklist localStorage key `trip-checklist-v1` and its `data-ck` ids so existing ticks carry over, and render fully styled offline (no CSS or icon CDN; system fonts only).

## Direction contract

THESIS: The trip as the hand-made 旅のしおり two friends staple together before leaving: cover, contents, one page per day, a 持ち物 checklist, lodging and transport pages, and a memo page at the back. It refuses the category default (an app shell with a timeline of cards) and last version's cream + terracotta.

OWN-WORLD: Two-ink risograph on paper stocks. Every line of text and every rule is Federal Blue ink on white stock. The only second ink is riso red, and it belongs to hard commitments (booking times, deadlines, 予約済 hanko). Cover, chapter dividers and index tabs are printed on 色上質紙 stocks (レモン, 若草, 水色, 桃, 藤). Visible details: slight ink misregistration, halftone fills, double rules, 切り取り線 dashed cuts, staples on the cover spine, ticket stubs with perforated edges for bookings, hand-ruled checkboxes. No cream, no gradients, no glass, no card shadows.

STORY: Open it and see the cover: the name, the dates, and a red stamp that says how many days are left, or which day it is today. The contents take you to any page. On each day page the red stubs are the things that cannot slip. Everything optional is a folded 付録 slip you can open. The checklist is ticked with a red check.

FIRST VIEWPORT: A phone at 390 px shows the cover on レモン stock. The title 關東秋季紅葉巡航 is set vertically (writing-mode vertical-rl) in heavy blue on the right, about 60 % of the viewport height. On the left: 2026 秋 · 旅のしおり, 11.7（土）→ 11.14（土）, the route in small blue, two staples on the left edge, and a large red circular riso stamp (countdown, or today). The primary action "今日のページ／もくじ" sits at the bottom edge of the viewport. A sticky index-tab strip of coloured stocks appears once you scroll past the cover.

FORM: 旅のしおり, position 1 on the ordered list (the user chose IMPECCABLE'S PICK over the assigned #7, 週間天気予報). Seed key 411927ed (degraded roll: no challengers, no QUALITY BAR boards). Code-led (no image generation). Signature interaction: the per-day 到着スタンプ box. Tap it and a red station-stamp lands with a small press motion; it persists per device, so the booklet fills with stamps as the trip goes. Motion grammar: ink press (scale 1.15 to 1 with slight rotation, 180 ms), nothing else moves.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
