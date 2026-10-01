---
name: 我的小工具 · 任意門空地
description: The site hub as a cel-flat empty lot under a blue sky, where every tool is a pink Anywhere Door standing on the grass.
colors:
  ink: "#1f3166"
  sky: "#6cc7f2"
  cloud: "#ffffff"
  cloud-shade: "#d6effb"
  horizon-light: "#9bd877"
  grass: "#8fd16a"
  grass-tuft: "#73b856"
  grass-deep: "#5e9c40"
  dirt: "#e3c38e"
  earth-shadow: "#8a6a3e"
  pink: "#f394c0"
  pink-deep: "#e2679f"
  plate: "#fffdf6"
  knob: "#f7d046"
  knob-shade: "#d9a91f"
  light: "#ffffff"
  wood: "#c98a4b"
  wood-edge: "#8a5a33"
  wood-ink: "#3a2414"
typography:
  display:
    fontFamily: "'Zen Maru Heavy', 'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', sans-serif"
    fontSize: "clamp(58px, 17vw, 132px)"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: ".02em"
  sign:
    fontFamily: "'Zen Maru Heavy', 'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', sans-serif"
    fontSize: "23px"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: ".08em"
  lede:
    fontFamily: "'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.7
  body:
    fontFamily: "'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.75
  nameplate:
    fontFamily: "'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.35
  ground-line:
    fontFamily: "'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "13.5px"
    fontWeight: 400
    lineHeight: 1.6
rounded:
  doorway: "3px 3px 0 0"
  frame: "9px 9px 3px 3px"
  moulding: "4px"
  plate: "5px"
  sign: "6px"
  round: "50%"
spacing:
  plate-gap: "5px"
  door-gap: "16px"
  sign-gap: "22px"
  gutter: "16px"
  gutter-wide: "40px"
  row-gap: "30px"
  row-gap-wide: "40px"
  stagger: "26px"
  stagger-wide: "34px"
components:
  door-frame:
    backgroundColor: "{colors.pink-deep}"
    rounded: "{rounded.frame}"
    width: "158px"
  door-panel:
    backgroundColor: "{colors.pink}"
    rounded: "{rounded.doorway}"
  doorway:
    backgroundColor: "{colors.light}"
    rounded: "{rounded.doorway}"
  nameplate:
    backgroundColor: "{colors.plate}"
    textColor: "{colors.ink}"
    typography: "{typography.nameplate}"
    rounded: "{rounded.plate}"
    padding: "9px 5px 10px"
  knob:
    backgroundColor: "{colors.knob}"
    rounded: "{rounded.round}"
    size: "15px"
  ground-line:
    textColor: "{colors.ink}"
    typography: "{typography.ground-line}"
  lot-sign:
    backgroundColor: "{colors.wood}"
    textColor: "{colors.wood-ink}"
    typography: "{typography.sign}"
    rounded: "{rounded.sign}"
    width: "172px"
    height: "92px"
  flash:
    backgroundColor: "{colors.light}"
---

# Design System: 我的小工具 · 任意門空地

> Scope: this system covers the **site hub** (`index.html`) only. `trip.html` has its own, unrelated system in root `DESIGN.md`; the tools behind the doors each keep their own look, and the hub never restyles them.

## Overview

**Creative North Star: "The Lot of Anywhere Doors"**

The hub is an empty lot (空地) on a cartoon afternoon. Flat blue sky with drawn clouds, a soft hill line, then flat grass with tufts and bare-dirt patches. Pink doors stand on the dirt, one per tool, each with a white nameplate, a gold knob and a contact shadow. Wooden stake signs (立て札) name the four lots, and a stack of concrete pipes sits in the first one. Open a door and you are somewhere else: the panel swings on its hinge, white light pours out of the doorway and fills the screen, and the tool loads.

The look is cel animation. Every field is a single flat colour, and every object is an authored inline SVG or CSS shape with one flat shade at most. The page reads top to bottom like a walk across the lot. The sky holds the title. Each lot is a sign, then a dirt patch with a two-up (phone) or auto-fit (desktop) row of doors, with alternate doors set back. The line printed on the ground under each door says what the tool does.

Confirmed rejections: the dark grid of same-size icon cards with eyebrow labels that this hub replaced; gradients as fills, glass, glow; card containers; characters or logos from any franchise (the doors are our own drawing).

**Key Characteristics:**
- Cel-flat: one flat colour per field, one hard shade per object at most, no gradients, no glow.
- Navy ink prints every word on the field; only the painted lot signs carry their own brown lettering.
- Doors are the only interactive objects, and their motion is the hinge.
- Two inlined OFL faces: heavy rounded for the title and signs, soft round Huninn for everything else.
- Every picture is inline SVG; no rasters, no CDN, no state.

## Colors

Cartoon daylight: a sky blue, two grass greens and a sandy dirt, with one saturated pink for the doors. Navy is the only text ink.

### Primary
- **Door Pink** (`pink`): the door panel. Nothing else on the page is this pink, which is why a door reads as a door.
- **Frame Pink** (`pink-deep`): the door frame, the moulding strokes, and the 2px nameplate border.

### Secondary
- **Knob Gold** (`knob`) with **Knob Shade** (`knob-shade`): the round knob and its single inset cel shade. `knob` is also the text-selection colour.
- **Doorway Light** (`light`): the doorway behind every panel and the full-screen `#flash`. Flat white.

### Neutral
- **Navy Ink** (`ink`): all text, icon strokes and the focus ring. Contrast: 6.56:1 on `sky`, 6.8:1 on `grass`, 7.38:1 on `dirt`, 12.2:1 on `plate`.
- **Sky** (`sky`): the header field and `theme-color`. **Cloud** (`cloud`) with **Cloud Shade** (`cloud-shade`) as its flat underside band.
- **Horizon Light** (`horizon-light`): the far hill band of the horizon SVG; the near band is `grass`.
- **Grass** (`grass`): the field and the page background. **Tuft Green** (`grass-tuft`) draws the two offset tuft-pattern layers. **Deep Grass** (`grass-deep`) is the pipe stack's ground shadow and the scrollbar thumb.
- **Dirt** (`dirt`): the irregular bare-dirt patch every lot's doors stand on.
- **Earth Shadow** (`earth-shadow`): the door's contact ellipse, always at .35 opacity.
- **Nameplate White** (`plate`): the warm white of the nameplate.
- **Wood** (`wood`), **Wood Edge** (`wood-edge`, the stake and board outline) and **Wood Ink** (`wood-ink`, the sign lettering, 5.0:1 on wood). The pipe stack's concretes (`#c3c7cc`, `#a9aeb4`, `#6e747c`) are local to that one drawing and are not tokens.

### Named Rules
**The Cel-Flat Rule.** Every field is one flat colour. An object gets at most one hard-edged shade: the cloud's underside band, the knob's inset, the darker hill band. No gradients, no glow, no blur. The doorway light is flat white, and the contact shadow is a flat ellipse.

**The Navy Ink Rule.** Navy `ink` prints every word on sky, grass, dirt and nameplate, at ≥6.5:1. There is no grey or faded secondary text; hierarchy is size. The one exception is part of the world: the stake signs are painted boards lettered in `wood-ink`.

**The Pink Is a Door Rule.** `pink` / `pink-deep` belong to doors. Don't use them for headings, links or decoration elsewhere on the lot.

## Typography

**Display Font:** Zen Maru Heavy (Zen Maru Gothic Black, SIL OFL), falls back to Huninn Shiori
**Body Font:** Huninn Shiori (jf open 粉圓, SIL OFL), falls back to PingFang TC, Noto Sans TC and Microsoft JhengHei

**Character:** a heavy, rounded cartoon headline over a soft, round Taiwanese text face. Friendly, legible, and a bit hand-drawn.

Both faces are inlined WOFF2 subsets with `font-display: block`. Huninn is subset to the page's own text, so re-run `python3 tools/trip-font.py --page index.html` after any text change. Zen Maru Heavy is a fixed `unicode-range` subset of 我的小工具旅行遊戲運動理財與筆記, so a new lot name needs a newly fetched subset.

### Hierarchy
- **Display** (900, clamp(58px, 17vw, 132px), 1, .02em, balanced): 「我的小工具」 in the sky, used once.
- **Sign** (900, 23px; 26px ≥760px, 1, .08em): lot names centred on the stake-sign board.
- **Lede** (400, 16px; 18px ≥760px, 1.7, max 22em): the one sentence under the title.
- **Nameplate** (400, 14px; 15px ≥760px, 13.5px ≤400px, 12.5px ≤340px, 1.35, centred): tool name under a 22px icon.
- **Ground line** (400, 13.5px; 12.5px ≤400px, 12px ≤340px, 1.6, max 17em, centred): the description printed under each door.

### Named Rules
**The Phrase Wrap Rule.** CJK lines break only between phrases. Every phrase is a `span.seg` (inline-block, max-width 100%).
- The ` · ` separator is glued to the end of its phrase with a no-break space (`湘南&nbsp;·`), followed by a normal space.
- Ground lines also split after 、，・／, and at hand-chosen phrase breaks (e.g. 隨機牌局 | 練基本策略).
- A Latin–CJK space goes between segs, outside the spans.
- Nameplates get a space only where Latin meets another phrase (`NBA` `拍賣選秀板`, `Usage` `Dashboard`); CJK-only nameplates have none.

**The Two Faces Rule.** The heavy face sets only the title and lot signs; its subset cannot set anything else. Everything else is Huninn at weight 400.

## Layout

Two bands, sky then field, both full-bleed. Content is capped at 1080px.

- **Sky:** min-height 40svh on phones (50vh ≥760px), padding `max(92px, safe-area-top) 22px 92px` (168px 40px 100px ≥760px). Below it, a 60px horizon SVG with two hill bands.
- **Clouds:** on phones they sit in the corners. From 760px they stay in a band above the title (top 26–72px) and never cross the words.
- **Lots:** stacked one per group: a sign (172×92, 196×105 ≥760px), then a dirt `.ground` with the door list. Lot padding is 24px 0 40px (34px 0 52px ≥760px). The field gutter is 16px (40px ≥760px, 10px ≤340px).
- **Doors:** a two-column grid of up to 168px columns, gap 30px 18px. Every even door drops 26px so the row reads as doors standing on uneven ground. From 760px the grid is `repeat(auto-fit, 188px)` with gap 40px 34px and a 34px drop, inside a ground of max 960px. Narrow phones tighten the column gap to 12px (≤400) and 8px (≤340).
- **First viewport (390px phone):** the title, the 旅行 sign, the pipes and both travel doors' nameplates are visible without scrolling.

## Elevation & Depth

Depth is drawn, not lit. Layering is by order and by flat contact shadows. There are no drop shadows and no glow.

### Shadow Vocabulary
- **Contact shadow** (flat `earth-shadow` ellipse, 16px tall, 120% of the door width, 8px below, opacity .35, `z-index: -1` inside the door body's `isolation: isolate`): grounds each door on the dirt.
- **Knob shade** (`box-shadow: inset -2px -2px 0 var(--knob-shade)`): the one hard cel shade on the knob. It is not a drop shadow.
- **Pipe ground shadow** (flat `grass-deep` ellipse at .55 opacity in the SVG): grounds the pipe stack.

### Named Rules
**The Drawn Depth Rule.** If something needs to sit on the ground, draw it a flat contact ellipse. Never use `box-shadow` blur, `filter: drop-shadow` or a glow. Tonal change on interaction is `filter: brightness()` on the panel only.

## Shapes

Toy-like rectangles with soft corners. The frame has 9px top corners and 3px bottom corners. The doorway and panel are 3px at the top and square at the threshold. Mouldings are 3px `pink-deep` strokes at 4px radius, the nameplate is 5px with a 2px frame-pink border, and the sign board is 6px with a 4px wood-edge outline. The knob, clouds and shadows are round. Door proportions are fixed at 158 / 262. The door is 158px wide on phones (176px ≥760px) and shrinks with its column.

## Components

### Anywhere Door (signature)
The only interactive object. Each door is a whole `a.door`, with the description on the ground below it (gap 16px).
- **Build:**
  - `door-body` holds `door-frame` (`pink-deep`, `perspective: 820px`).
  - The frame holds `door-way` (flat `light`, inset 8px 8px 0) and `door-panel` (`pink`, hinged `transform-origin: left`).
  - The panel carries two mouldings, the knob (right 7%, top 49%) and the nameplate (top 11%, inset 16% each side; 10% ≤400px, 7% ≤340px).
  - `door-shadow` sits behind it all.
- **Hover (fine pointer) / keyboard focus:** the panel opens a crack (`rotateY(-26deg)`, brightness .95), showing a sliver of light. Hover also underlines the name (offset 3px). Focus adds a 3px navy outline 5px off the frame.
- **Open (plain left click or tap):**
  - The panel swings to `rotateY(-84deg)` (brightness .82) over .45s `cubic-bezier(.2,.75,.25,1)`.
  - At 300 ms, `#flash` grows its `clip-path` circle from the doorway centre to 150vmax (.36s `cubic-bezier(.2,.8,.2,1)`).
  - Navigation happens at 720 ms.
- **Bypass:** modified clicks, non-left buttons and `prefers-reduced-motion` navigate immediately. Reduced motion also kills every transition.
- **Return:** a `pageshow` handler removes `.is-opening` and the flash, so a bfcache restore shows the doors closed.

### Nameplate
A warm-white plate with a 2px frame-pink border at 5px radius, padding 9px 5px 10px, gap 5px. A 22px icon sits above the tool name, both in navy. The icons come from the inline sprite (24-unit grid, 1.8 stroke, round caps), one `<symbol>` per tool.

### Ground Line
The tool's one-line description, printed in navy on the dirt, centred, max 17em. It follows the Phrase Wrap Rule.

### Lot Sign
An inline SVG stake sign: a wood board with a wood-edge outline and grain strokes on a stake. An `h2` is laid over the board area in the heavy face, lettered in `wood-ink`. This is the lot's heading, and its `id` labels the section.

### Scenery
Clouds (white with a `cloud-shade` underside band), the two-band horizon, the dirt patch (one irregular SVG path stretched per lot), the grass tuft patterns (two offset tiled SVG layers) and the pipe stack (first lot only, hidden in print). All of it is `aria-hidden` inline SVG.

### Adding a 13th door
1. Copy one `li.spot` into the right lot and set `href`.
2. Split the name into `span.seg` phrases, following the Phrase Wrap Rule.
3. For the icon: `<use href="#i-…">`, adding a 24-grid, 1.8-stroke `<symbol>` if the tool needs a new one.
4. Write the ground line.
5. Update the door count in the lede and the meta description.
6. Run `python3 tools/trip-font.py --page index.html`.
7. A new lot also needs a new sign and a new Zen Maru subset.

## Do's and Don'ts

### Do:
- **Do** fill every field with one flat token colour and give an object at most one hard shade.
- **Do** print every word in navy `ink` (≥6.5:1 on sky, grass, dirt), with hierarchy by size alone; sign lettering stays `wood-ink` on wood.
- **Do** wrap every CJK phrase in `span.seg`, glue ` · ` to its phrase with a no-break space, and put Latin–CJK spaces between segs.
- **Do** keep clouds in the band above the title on ≥760px.
- **Do** ground new objects with a flat contact ellipse, and keep the door shadow inside `isolation: isolate`.
- **Do** keep the open sequence intact: −26° crack on hover/focus, −84° swing, flash at 300 ms, navigate at 720 ms, immediate for reduced motion and modified clicks, `pageshow` reset.
- **Do** draw every picture as authored inline SVG, and re-subset the font after text changes.

### Don't:
- **Don't** add gradients, glow shadows, blur, glass or card containers; the doorway light stays flat white.
- **Don't** tint or fade secondary text grey.
- **Don't** use door pink outside doors.
- **Don't** set anything but the title and lot signs in Zen Maru Heavy.
- **Don't** add franchise characters, logos, raster images, CDN assets, localStorage or any other state.
- **Don't** restyle the tools behind the doors.
