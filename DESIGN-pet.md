---
name: 電子雞飼養箱 · Pet-Shop Tank
description: A web virtual pet kept in a real glass tank on a dim pet-shop wall, cared for by acts done to the tank, with an orange price sticker on the glass and a yellow pencil index card taped under it.
colors:
  wall: "#162024"
  wall-2: "#1d2a2f"
  wall-3: "#273840"
  peg: "#0d1518"
  wall-dark: "#0c1215"
  ink: "#eaf2ef"
  ink-2: "#b3c7c1"
  ink-disabled: "#7d8f8a"
  rim: "#131618"
  rim-2: "#2a3034"
  rim-3: "#3b4348"
  shelf: "#3a4348"
  shelf-edge: "#20272b"
  tank-black: "#0b1114"
  glass: "#9fd6c9"
  lamp: "#f2fff7"
  lamp-off: "#2b3236"
  night-light: "#ffd98c"
  sticker: "#ff6a1a"
  sticker-ink: "#1b1006"
  card: "#fff2a8"
  card-rule: "#8eb3df"
  card-red: "#e2584d"
  pencil: "#2f2b28"
  act: "#ffe14d"
  poster: "#f5f7f4"
  poster-ink: "#1d282c"
  poster-ink-2: "#465559"
  lens-glass: "#f2f7f4"
  hidden-tint: "#fff6cf"
  reset-armed: "#5a2a24"
  land-band: "#ae1f5b"
  water-band: "#17599f"
  sky-band: "#6231a8"
  forest-band: "#0d6b5b"
  trop-band: "#9e470c"
  ice-band: "#1a6585"
  land-cell: "#e8508e"
  water-cell: "#2f86e0"
  sky-cell: "#9363da"
  forest-cell: "#1fa38b"
  trop-cell: "#ee7a2e"
  ice-cell: "#5db6de"
typography:
  bar-title:
    fontFamily: "'Chiron GoRound TC', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', system-ui, sans-serif"
    fontSize: "19px"
    fontWeight: 900
    letterSpacing: ".02em"
  section:
    fontFamily: "'Chiron GoRound TC', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', system-ui, sans-serif"
    fontSize: "22px"
    fontWeight: 900
  sticker-name:
    fontFamily: "'Chiron GoRound TC', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', system-ui, sans-serif"
    fontSize: "21px"
    fontWeight: 900
    lineHeight: 1.25
    letterSpacing: ".02em"
  sticker-age:
    fontFamily: "'Chiron GoRound TC', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', system-ui, sans-serif"
    fontSize: "30px"
    fontWeight: 900
    lineHeight: .9
    fontFeature: "'tnum'"
  sticker-small:
    fontFamily: "'Chiron GoRound TC', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 700
  title:
    fontFamily: "'Chiron GoRound TC', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 900
  body:
    fontFamily: "'Chiron GoRound TC', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.6
  tool-label:
    fontFamily: "'Chiron GoRound TC', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 700
  label:
    fontFamily: "'Chiron GoRound TC', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', system-ui, sans-serif"
    fontSize: "12.5px"
    fontWeight: 400
  card-head:
    fontFamily: "'Iansui', 'Chiron GoRound TC', 'PingFang TC', sans-serif"
    fontSize: "19px"
    fontWeight: 400
    lineHeight: "28px"
  card-row:
    fontFamily: "'Iansui', 'Chiron GoRound TC', 'PingFang TC', sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "28px"
  say:
    fontFamily: "'Iansui', 'Chiron GoRound TC', 'PingFang TC', sans-serif"
    fontSize: "15.5px"
    fontWeight: 400
    lineHeight: 1.6
rounded:
  card: "2px"
  sticker-flag: "3px"
  sticker: "4px"
  poster: "6px"
  lid: "8px 8px 2px 2px"
  base: "2px 2px 8px 8px"
  tile: "8px"
  key: "10px"
  pill: "999px"
  round: "50%"
spacing:
  gutter: "16px"
  gutter-desktop: "24px"
  rule: "28px"
  tap: "44px"
  tile-h: "52px"
  tool-h: "64px"
  wall-top: "34px"
  wall-top-desktop: "44px"
  shelf-gap: "18px 12px"
  shelf-gap-desktop: "22px 18px"
components:
  sticker:
    backgroundColor: "{colors.sticker}"
    textColor: "{colors.sticker-ink}"
    rounded: "{rounded.sticker}"
    padding: "7px 10px 8px"
    width: "156px"
  index-card:
    backgroundColor: "{colors.card}"
    textColor: "{colors.pencil}"
    typography: "{typography.card-row}"
    rounded: "{rounded.card}"
    padding: "12px 16px"
  call-flag:
    backgroundColor: "{colors.sticker}"
    textColor: "{colors.sticker-ink}"
    rounded: "{rounded.sticker-flag}"
    padding: "6px 12px 6px 14px"
  tool:
    textColor: "{colors.ink}"
    typography: "{typography.tool-label}"
    height: "64px"
  tool-disabled:
    textColor: "{colors.ink-disabled}"
  tray:
    backgroundColor: "{colors.rim}"
    textColor: "{colors.ink}"
    padding: "12px 12px 10px"
  food-tile:
    backgroundColor: "{colors.rim-2}"
    textColor: "{colors.ink}"
    rounded: "{rounded.tile}"
    padding: "6px 8px"
    height: "52px"
  food-tile-hover:
    backgroundColor: "{colors.rim-3}"
  tank-pick:
    backgroundColor: "{colors.wall-3}"
    textColor: "{colors.ink}"
    rounded: "{rounded.tile}"
    height: "52px"
  close-key:
    textColor: "{colors.ink-2}"
    rounded: "{rounded.key}"
    size: "44px"
  close-key-hover:
    backgroundColor: "{colors.rim-2}"
    textColor: "{colors.ink}"
  guess-key:
    backgroundColor: "{colors.rim}"
    textColor: "#ffffff"
    rounded: "{rounded.pill}"
    padding: "10px 14px"
  lens:
    backgroundColor: "{colors.lens-glass}"
    textColor: "{colors.poster-ink}"
    rounded: "{rounded.round}"
    width: "min(92%, 430px)"
  poster:
    backgroundColor: "{colors.poster}"
    textColor: "{colors.poster-ink}"
    rounded: "{rounded.poster}"
    padding: "16px 14px 18px"
  shelf-tank-band:
    backgroundColor: "{colors.land-band}"
    textColor: "#ffffff"
    padding: "4px 8px 5px"
  reset-key:
    textColor: "{colors.ink-2}"
    rounded: "{rounded.tile}"
    height: "44px"
    padding: "0 14px"
  reset-key-armed:
    backgroundColor: "{colors.reset-armed}"
    textColor: "#ffffff"
---

# Design System: 電子雞飼養箱 · Pet-Shop Tank

> Scope: `pet-tank.html` (電子雞飼養箱) only. This world is separate from root `DESIGN.md` (trip booklet, `trip-v2.html`), `DESIGN-hub.md` (site hub), `DESIGN-livecam.md` (station: `livecam.html`, `trip.html`), `DESIGN-blackjack.md` (pocket LCD), `DESIGN-yacht.md` (regatta), `DESIGN-nba.md` (fantasy data app), `DESIGN-invest.md` (passbook) and `DESIGN-etf.md` (disclosure notice). Recorded from the shipped build on 2026-10-20.

## Overview

**Creative North Star: "The Tank on the Shop Shelf"**

The pet lives in a real glass tank on a dim pet-shop wall. The tank has a black plastic lid with a fluorescent tube in it, black side rims, a faint green glass edge, two slanted reflection streaks and a black base. Below it runs a grey shelf board. The six fields are six kinds of tank: a sand terrarium, an aquarium, a tall perch cage, a bamboo rainforest tank, a warm-lamp tropical tank and a frosted freezer case. Each tank's habitat is drawn in natural materials. The tank's lamp is the main light on the page: it spills a soft glow onto the wall behind the tank, and switching it off darkens the tank, the wall, the card, the tools and the top strip together, leaving a small amber night light in the corner.

Care is done to the tank, never through stat bars. Food drops through the lid, falls, bounces on the substrate and the pet walks over to eat it. A knuckle knocks on the glass to start play. A scoop comes down through the lid and sweeps out the poop. A spray bottle mists the pet. The lamp is a rocker switch. State is shown as marks and materials. On the yellow index card, pencil ticks fill four boxes for hunger and mood, and 正-stroke tallies count tornadoes, rice balls and suns. Dirt shows as darkened substrate. Illness shows as fogged glass, and a pet turned devil fogs the glass further and gets horns. Evolution fogs the glass, whites out the pet, and then slaps a new price sticker onto the glass.

Confirmed rejections (direction contract): the egg-shaped LCD device with three buttons, and the cartoon-room app with stat bars. The characters are original and drawn as flat colour planes without outlines. No Bandai names, sprites or logos.

**Key Characteristics:**
- One dim teal shop wall with a peg-board dot grid, lit by the tank's own lamp.
- A black-rimmed glass tank about 55 % of the phone screen tall, on a shelf board with a hard front edge.
- A fluorescent-orange price sticker on the glass (tank, stage, name, age) and a yellow ruled index card taped under the tank, written in pencil (Iansui).
- Seven drawn tools standing on the shelf edge: 餵食, 陪玩, 清理, 保養, the lamp switch, 吃藥 and 放大鏡.
- Field colours appear only as label bands (shelf tanks, binder sections) and, in the magnifier, as cell fills.
- Every care act has a physical animation, and every one has an instant path under reduced motion.

## Colors

A dark shop wall and black tank plastic, one warm lamp, and the stationery taped to the tank: an orange sticker, a yellow card in pencil and a white poster.

### Primary
- **Price-Sticker Orange** (`sticker`, ink `sticker-ink`): the price sticker on the glass, the call flag on the index card (在叫你：肚子餓 / 想玩 / 睡著了，燈還開著), the 現在 tag on the shelf tank in use, and `::selection`. It always means "this pet, now".

### Secondary
- **Index-Card Yellow** (`card`) with **Card Rule Blue** (`card-rule`, a 1px rule every 28px) and **Card Red** (`card-red`, the 2px header rule at 40px): the 飼育紀錄 card. The play game's score slip at the top of the tank uses the same yellow and pencil.
- **Pencil** (`pencil`): all writing and marks on the card and the score slip: ticked boxes, 正 tallies, ○ and ✕ guesses, all at .88 opacity with seeded jitter.
- **Switch Yellow** (`act`): the global focus ring (3px), the pressed tool's 3px underline, the hover ring on a shelf tank, the food-point dots in the feed tray, and the lamp switch's rocker.

### Tertiary
- **Field bands** (`land-band`, `water-band`, `sky-band`, `forest-band`, `trop-band`, `ice-band`): the label band under each shelf tank (white text, every pair ≥ 6.2:1) and the 6px rule on top of each binder section.
- **Field cells** (`land-cell` … `ice-cell`): the filled field-cell circles in the magnifier during the baby stage.
- **Habitat materials:** each tank's SVG habitat uses its own natural colours (sand, water, lilac sky with cage bars, deep green with bamboo, warm orange with palms, pale ice). These colours stay inside the glass.

### Neutral
- **Shop Wall** (`wall`): the page and `theme-color`, with a 24px grid of **Peg** (`peg`) dots. **Wall-3** (`wall-3`) is the tank-pick tiles and the hover fill of wall-level keys. With the lamp off the page turns **Wall Dark** (`wall-dark`).
- **Wall Ink** (`ink`) and **Wall Ink 2** (`ink-2`): text on the wall and inside the tank's dark overlays (14.6:1 and 9.4:1 on the wall). **Disabled Ink** (`ink-disabled`) is a tool that can't be used now (4.9:1).
- **Tank Plastic** (`rim`, `rim-2`, `rim-3`): the lid, side rims, base, feed tray, magnifier rim, food tiles and their hover, the lid hatch.
- **Shelf** (`shelf`, front edge `shelf-edge`): the shelf board under the tank, under the tools and under each shelf tank.
- **Glass** (`glass`): the tank's inner edge, as a 2px line at .45 and a 5px line at .12.
- **Lamp** (`lamp`) / **Lamp Off** (`lamp-off`): the tube in the lid. **Night Light** (`night-light`) is the small lamp left on in the dark.
- **Poster** (`poster`, inks `poster-ink` / `poster-ink-2`): the binder and the care sheet, the white paper pinned on the wall. **Hidden Tint** (`hidden-tint`) marks a hidden character's cell there. **Lens Glass** (`lens-glass`) is the magnifier's face.

### Named Rules
**The One Lamp Rule.** The tank's lamp is the light source. Turning it off dims everything that sits in its light (wall, card, tools, top strip, sticker) and turns on the amber night light; nothing on the page stays lit on its own.

**The Field Band Rule.** A field colour labels a tank or a binder section. It never fills a panel, a button or text.

**The Orange Means Now Rule.** Sticker orange marks the current pet and what it is asking for. Don't use it for decoration or for a second meaning.

## Typography

**UI face:** Chiron GoRound TC 400 / 700 / 900 (`--sans`, falling back to PingFang TC, Noto Sans TC, Microsoft JhengHei), a rounded sans for everything printed: the top strip, the sticker, tools, trays, the binder and the care sheet.
**Pencil face:** Iansui (`--hand`), for everything handwritten: the index card, the play score slip, the 說話 line under the tools and the sleeping z.

**Character:** a soft round print face for the shop's labels and a plain handwriting for the keeper's notes. Both come from Google Fonts, the page's only external request.

### Hierarchy
- **Sticker age** (900, 30px, line-height .9, tabular): the day number on the sticker.
- **Section** (900, 22px): the wall headings 架上的六個箱子 / 圖鑑 / 飼養須知, and the tank-pick heading.
- **Sticker name** (900, 21px; 19px ≤ 360px): the pet's name on the sticker.
- **Bar title** (900, 19px; 22px ≥ 900px): 電子雞飼養箱.
- **Title** (900, 16–17px): tray, magnifier and poster headings.
- **Body** (400, 16px / 1.6): page text; the care sheet runs 15px / 1.7 in a 48em measure.
- **Card** (Iansui 400, 19px head and 16px rows, every line on the 28px card rule): 飼育紀錄 and its rows.
- **Say line** (Iansui 400, 15.5px; 17px ≥ 900px): what just happened, a polite live region.
- **Tool label** (700, 13px; 12px ≤ 360px) under each drawn tool.
- **Label** (12–13px): sticker kind line (700), tray notes, food sub-lines, binder descriptions (11.5px), the shop clock (700, 15px, tabular).

### Named Rules
**The Print and Pencil Rule.** What the shop prints (labels, keys, posters) is Chiron GoRound TC. What the keeper writes (the card, the game slip, the say line) is Iansui. Don't mix them on one surface.

**The Card Rule Rule.** Every line on the index card sits on the 28px ruling: headings, rows and notes all use a 28px line height.

## Layout

- **Phone (default):** one column, 16px gutters, max width 1040px. A thin strip (首頁 exit, 電子雞飼養箱, the shop clock) → the tank, full width, `clamp(300px, 54svh, 560px)` tall → the index card overlapping the base by 14px, inset 8px and tilted −0.6° → the seven tools on one row (seven equal columns, 64px tall) standing on the shelf board → the say line. Below the fold, three wall sections 34px apart: the shelf of six tanks (two columns), the binder poster, the care-sheet poster, then the footer with 全部重來.
- **≥ 900px:** the stage is max 960px with 24px gutters, a grid of `1fr 400px` with 28px between. The tank spans both columns, `min(60vh, 520px)` tall. The card sits in the right column, raised 40px over the base and tilted +1.2°. The say line takes the left column beside it at 17px. The tools span the full width under both. The pet grows from 104px to 136px; the sticker from 156px to 178px wide. The shelf becomes three columns with 150px tanks.
- **≤ 360px:** tool labels 12px, sticker 140px wide.
- **Inside the tank:** the substrate line `--ground` (360px into a 600×500 habitat drawn with `xMidYMax slice`) is where the pet stands and food lands. Overlays (tank pick, feed tray, play game, magnifier) open inside the glass, never as page modals.
- **Tap targets:** every key is at least 44px; tank picks and food tiles 52px; tools 64px.

## Elevation & Depth

Depth is physical. The tank casts one soft drop shadow onto the wall. Paper taped to it (sticker, card, call flag, game slip) casts a small contact shadow. Shelf boards show their thickness as a hard front edge. Glass is shown by its inner edge lines and reflection streaks, the lamp by a soft glow on the wall and a light band under the lid.

### Shadow Vocabulary
- **Tank on the wall** (`filter: drop-shadow(0 18px 22px rgba(0,0,0,.45))`): the whole tank, lid to base.
- **Shelf board edge** (`box-shadow: 0 7px 0 #20272b, 0 14px 14px rgba(0,0,0,.35)` under the tools; `0 6px 0` under the tank; `0 5px 0` under each shelf tank): the board's front face, then its shadow. This is the shelf's own thickness, not a card shadow.
- **Taped paper** (`0 2px 4px rgba(0,0,0,.25)`): sticker, call flag, game score slip. The index card sits higher (`0 6px 12px rgba(0,0,0,.35)`) with two clear tape strips (`rgba(255,255,255,.42)`).
- **Overlays in the tank** (`0 10px 18px rgba(0,0,0,.4)`): the feed tray dropping from the lid. The magnifier is ringed by two rim lines (9px `rim`, 12px `rim-3`) over `0 18px 28px rgba(0,0,0,.45)`.
- **Posters on the wall** (`0 10px 22px rgba(0,0,0,.35)`): binder and care sheet.

### Named Rules
**The Real Objects Rule.** Only things that exist in the shop cast shadows: the tank, the shelf, the taped paper, the trays and posters. Text and icons never get glows or shadows.

## Shapes

- The tank is a box: lid with 8px top corners, straight black side rims (6px), base with 8px bottom corners; the shelf tanks repeat it at 4px rims and an 8px lid.
- Paper is nearly square: card 2px, sticker 4px, call flag 3px with its right edge running off the card. Paper is always tilted (sticker −3°, card −0.6° / +1.2°, flag 4°, tape strips −6° / 5°).
- Wall-level tiles (food, tank picks, the reset key) are 8px; the close key 10px; posters 6px.
- Round things are round: the magnifier lens, the cell slots and dots, the guess keys in the play game (pills).
- **Characters** are built by `spr()` on a 64-unit grid from flat colour planes: one body shape (`o` oval, `r` rounded box, `d` drop, `p` pear, `bell`, `cloud`, `egg`, `snow`, `gem`) plus ears, sprouts, tails and marks in the character's two or three colours, with a darker shade for the far side. No outlines. Eyes blink; sleeping and sad states change the eyes and mouth.
- Tools and food icons are small flat drawings on a 32- or 30-unit grid, in their own object colours.

## Components

### The tank
Lid (tube + a hatch that tips up 24° when something comes through the lid) → glass (habitat SVG, dirt, poop and food, the pet, the night overlay, the fog, the reflection streaks, the sticker) → base. Habitats move a little: water plants sway, bubbles rise in the aquarium, the perch swings; all of it pauses with the lamp off.
- **Lamp off:** the tube goes `lamp-off`, a navy overlay (`rgba(6,10,28,.78)`) fades in over .9s, the night light comes on with its glow, the pet dims and stops wandering, the wall glow and lid light band go out.
- **Lamp on:** the tube and the overlay flicker in `steps(1,end)` over .7s, the fluorescent start-up.
- **Dirty:** the substrate darkens with a brown wash from the ground up. Poop older than 2 hours turns dark.
- **Sick / devil:** fog over the glass at .62 / .8, the pet desaturated (devil also darkened, with horns).
- **Evolving:** fog .9 and the pet whited out for 1.3s, then the new sticker slaps on.

### Price sticker
Orange, 156px, top left of the glass at −3°: kind line (tank name and stage, 12px 700), the pet's name (21px 900), 出生第 **N** 天 (the number 30px). New stickers land with a slap (from −14° and ×1.5, .5s overshoot). It fades out while the game or magnifier covers the glass and dims with the lamp.

### Index card (飼育紀錄)
Yellow ruled card with a red header rule, two clear tape strips, pencil text. Rows: 肚子 and 心情 as four pencil boxes ticked per 25 %, 龍捲風 as a 正 tally (in the young stage the stage's count, otherwise the total with （全部）), and in the young stage 飯糰 and 太陽 tallies. Every mark has a screen-reader twin. The note line says what is happening next; its actions (孵一顆新蛋, 再養一隻) are underlined pencil text. When the pet calls, the orange **call flag** sticks out of the card's right edge and sways.

### Tools on the shelf
Seven buttons, each a drawn object (food box, ball, scoop, spray bottle, rocker switch, medicine bottle, magnifier) over a 13px label. Hover lifts the object 3px; an open tool (`aria-pressed`) lifts it 5px, tilts it −6° and underlines the tool in switch yellow. Disabled tools turn grey. The lamp switch's rocker moves down and greys with the lamp off.

### Care acts on the glass
- **Feed:** the tray drops from the lid (rim black, scaleY .28s) with food tiles: icon, name, the cell and its +1/+2/+4 as yellow dots, the remaining stock for +4 foods. A chosen food falls through the open hatch (900ms, rotating, one bounce), the pet walks over at speed and eats (chomp), then hops.
- **Play:** a knuckle knock on the glass (a smudge and five strike lines, 650ms), a yellow pencil score slip at the top (round, ○ / ✕ marks) and two dark pill keys on the left and right halves of the tank.
- **Clean:** the scoop comes down through the lid and sweeps left to right (1.1s); each poop flicks away as the scoop passes.
- **Groom:** the spray bottle appears at the glass edge and 14 mist dots drift onto the pet.
- **Magnifier:** a round light lens with a black rim opens in the glass (scale from .5, .32s) showing field cells (baby) or food-cell dots (kid) in the field and food colours.

### Pet motion
Walking hops in two steps; sleeping breathes with a drifting pencil z; calling bounces; eating chomps; a happy pet jumps three times; a refusal shakes; the egg wobbles. Eyes blink every 5.2s.

### Wall sections
- **Shelf of six tanks:** miniature tanks with their habitat, retired residents standing in them (the current pet larger), a field band (field and tank name, residents n/4), and a 現在 sticker or a black 搬過來 tag.
- **Binder and care sheet:** white posters. Binder sections are `details` with a field-colour top rule, a 48px header and a chevron; characters in 62px cells, unseen ones as a 16 % silhouette, hidden ones on `hidden-tint`. The care sheet holds the numbered rules and a 24-hour sleep band with its legend.

### Reduced motion
All animations and transitions collapse; food lands at once, the scoop, spray, knock, flicker and slap are skipped, and walking, calling and breathing stop.

## Do's and Don'ts

### Do:
- **Do** keep every care verb a physical act on the tank (through the lid, on the glass, at the switch), with an instant reduced-motion path.
- **Do** show the pet's state as pencil marks on the card and as material changes in the tank (fog, dark substrate, dark poop), not as bars or warning icons.
- **Do** let the lamp switch darken the tank and everything in its light together, and flicker on in `steps()`.
- **Do** draw new characters with `spr()` as flat colour planes without outlines, in two or three colours.
- **Do** keep field colours to label bands and cell fills, with white text on bands.
- **Do** keep handwriting (Iansui) on the keeper's paper and Chiron GoRound TC on everything printed.
- **Do** open every overlay inside the glass and keep keys at 44px or larger.

### Don't:
- **Don't** add stat bars, percentages on screen, or an egg-shaped LCD device.
- **Don't** use sticker orange for anything but the current pet and its call.
- **Don't** give text or icons glows or shadows; shadows belong to the tank, the shelf, taped paper, trays and posters.
- **Don't** use Bandai names, sprites or logos for any character.
