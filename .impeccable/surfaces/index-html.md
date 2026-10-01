---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: []
---

## Scope

`index.html`, the 我的小工具 site hub: a full redesign, replacing the dark navy card grid. Visitor mode: **Operate** (find a tool and open it). Friends who receive the link must be able to read what each tool is. Twelve tools in four confirmed groups (旅行 / 遊戲 / 運動 / 理財與筆記; see PRODUCT.md › Site hub). Phone and desktop count equally. A self-contained single file: no CSS, JS or font CDN. The hub never restyles the tools.

## Direction contract

THESIS: The hub is an empty lot (空地) under a blue sky where twelve pink Anywhere Doors (任意門) stand on the grass, one per tool. Open a door and you are somewhere else. It refuses the category default it replaces: a dark grid of same-size icon cards with eyebrow labels.

OWN-WORLD:
- Cel-flat cartoon daylight. A flat sky-blue field with authored white SVG clouds, and flat grass green with authored tufts and bare-dirt patches.
- Pink panel doors with a deeper-pink frame, a gold round knob, a white nameplate, and a soft contact shadow on the grass.
- Wooden stake signs (立て札) name the four lots; a stack of concrete pipes sits in the first lot.
- Navy ink for all text. No gradients as fills, no glass, no glow, no card containers. No characters or logos from any franchise; the doors are our own drawing.

STORY: Land under the sky and read 「我的小工具」. Walk down past four lots, reading each door's nameplate and the line on the ground beneath it. Tap a door: it swings open, white light pours out and fills the screen, and you arrive in the tool.

FIRST VIEWPORT:
- Phone (390): sky across the top 45% with the title 「我的小工具」 in heavy rounded navy, plus clouds. The grass horizon starts below. The first lot's sign 「旅行」 and its two doors (關東秋季紅葉巡航, 東京近郊即時影像) stand on the grass with their nameplates readable without scrolling.
- Desktop: the sky band holds the title, and the first lots are visible below it.

FORM: user-pinned 「多拉A夢任意門」. The user overrode the rolls: seed key 7e4e162f assigned #4 五金行零件櫃, the user asked for bolder, and re-roll 1 (bolder unavailable, degraded) assigned #6 街機選角畫面. The user named this form instead, so it is not on my ordered list. Code-led, no image generation. Signature interaction: tap a door → the panel swings open on its hinge (rotateY, about 450 ms, ease-out) → white light grows from the doorway to fill the screen (about 250 ms) → navigate. Desktop hover/focus opens the door a crack with a sliver of light. Reduced motion navigates immediately; bfcache restores the doors closed.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
