---
name: 21點實戰牌桌 · Pocket LCD
description: The blackjack table and the strategy trainer as one 1980s pocket LCD game, with a tomato-red shell, a charcoal faceplate, a grey-green glass with ghost segments, and rubber keys.
colors:
  shell: "#c4331f"
  shell-deep: "#a12815"
  shell-ink: "#a3291a"
  face: "#24221f"
  face-deep: "#171614"
  bezel: "#121110"
  print: "#f5f3ee"
  print-dim: "rgba(245,243,238,.72)"
  print-yellow: "#f2c230"
  key: "#3a3732"
  lcd: "#aab59c"
  ink: "#1d231c"
  ghost: "rgba(29,35,28,.085)"
  red-ink: "#8a2414"
  chip10: "#1f5fbf"
  chip50: "#d9621a"
  chip100: "#141311"
  chip500: "#6d2fa0"
  paper: "#ffffff"
  paper-ink: "#24221f"
typography:
  logo:
    fontFamily: "'Michroma', 'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', sans-serif"
    fontSize: "21px"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: ".16em"
  silkscreen:
    fontFamily: "'Michroma', 'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', sans-serif"
    fontSize: "11px"
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: ".04em"
  readout-lg:
    fontFamily: "'LCD', 'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "27px"
    fontWeight: 400
    lineHeight: 1.15
  readout:
    fontFamily: "'LCD', 'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "19px"
    fontWeight: 400
    lineHeight: 1.15
  seg14:
    fontFamily: "'LCD14', 'LCD', sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1
  prompt:
    fontFamily: "'LCD', 'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.45
  key-legend:
    fontFamily: "'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.2
  body:
    fontFamily: "'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.6
  manual:
    fontFamily: "'Huninn Shiori', 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "14.5px"
    fontWeight: 400
    lineHeight: 1.75
rounded:
  faceplate: "28px"
  bezel: "16px 16px 16px 34px"
  coach-plate: "14px"
  key: "12px"
  lcd: "8px"
  window: "7px"
  leaflet: "6px"
  card: "5px"
  segment: "4px"
  pill: "999px"
  round: "50%"
spacing:
  app-gutter: "12px"
  app-gutter-wide: "22px"
  faceplate-pad: "16px"
  faceplate-pad-wide: "20px"
  unit-gap: "16px"
  key-gap: "9px"
  chip-gap: "8px"
  panel-gap: "14px"
  column-gap: "22px"
  card-gap: "5px"
components:
  key:
    backgroundColor: "{colors.key}"
    textColor: "{colors.print}"
    typography: "{typography.key-legend}"
    rounded: "{rounded.key}"
    padding: "8px 4px 6px"
    height: "62px"
  key-primary:
    backgroundColor: "{colors.print-yellow}"
    textColor: "{colors.ink}"
    rounded: "{rounded.round}"
    size: "78px"
  chip-key-10:
    backgroundColor: "{colors.chip10}"
    textColor: "{colors.print}"
    rounded: "{rounded.round}"
    size: "52px"
  mode-key:
    backgroundColor: "{colors.face}"
    textColor: "{colors.print}"
    rounded: "{rounded.pill}"
    padding: "7px 13px"
    height: "38px"
  lcd-glass:
    backgroundColor: "{colors.lcd}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lcd}"
    padding: "10px 12px 8px"
  lcd-window:
    backgroundColor: "{colors.lcd}"
    textColor: "{colors.ink}"
    rounded: "{rounded.window}"
    padding: "9px 11px"
  card-slot:
    backgroundColor: "{colors.lcd}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    width: "38px"
    height: "54px"
  okng-lamp:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.lcd}"
    typography: "{typography.seg14}"
    rounded: "{rounded.segment}"
  coach-plate:
    backgroundColor: "{colors.face-deep}"
    textColor: "{colors.print}"
    rounded: "{rounded.coach-plate}"
    padding: "12px 14px"
  leaflet:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.paper-ink}"
    typography: "{typography.manual}"
    rounded: "{rounded.leaflet}"
  select:
    backgroundColor: "{colors.face}"
    textColor: "{colors.print}"
    rounded: "{rounded.pill}"
    padding: "6px 32px 6px 13px"
    height: "38px"
  summary-readout:
    backgroundColor: "{colors.lcd}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lcd}"
    padding: "10px 18px 8px"
---

# Design System: 21點實戰牌桌 · Pocket LCD

> Scope: `blackjack-game.html` (the table) and `blackjack.html` (the strategy trainer). Both pages share the rules, the strategy tables and this world. This world is separate from root `DESIGN.md` (trip booklet) and `DESIGN-hub.md` (site hub).

## Overview

**Creative North Star: "The Pocket LCD Casino"**

The page is a 1980s handheld blackjack game. A drenched tomato-red moulded shell fills the whole viewport, with the logo and six mode keys printed on it. One charcoal faceplate holds everything else: a bezel-framed grey-green LCD with fixed card slots, bet rings and segment readouts; rubber keys under the glass; a recessed coach plate; and a data unit of small LCD windows behind a silkscreen rule. The rules and the strategy chart are a printed two-colour leaflet that comes in the box.

Every number is a segment readout with its unlit ghost 8s showing. Cards are fixed LCD positions that light up, and the ghost outlines of the empty slots are always visible. Nothing slides or fades. Segments switch on and off in whole steps, and keys physically depress. Data is dense, as on a real device, but every window sits on the same faceplate rather than in floating cards.

Confirmed rejections: the green-felt casino skin and the dark "table plus card panels" dashboard this world replaced; real-money or casino-brand cues.

**Key Characteristics:**
- Three materials only: red plastic shell, charcoal printed faceplate, grey-green reflective LCD. A white leaflet stands in for the printed manual.
- Ghost segments always show: 8s behind readouts, empty card slots on the glass.
- All motion is `steps(1,end)`: blink, hold, switch. No easing on the glass.
- Rubber keys with a press travel. Yellow is spent on the one round primary key.
- Self-contained: inlined font subsets, inline SVG, no CDN, nothing saved.

## Colors

A toy's palette: one saturated plastic red, charcoal print surfaces, a dull grey-green glass printed in near-black, and one signal yellow.

### Primary
- **Tomato Shell** (`shell`): the page itself (html/body background), the split swatch, the leaflet's header rule, solid 分 cells. **Shell Deep** (`shell-deep`) is the scrollbar thumb. **Shell Ink** (`shell-ink`) is the darker red for leaflet headings, `b/strong`, links and 降 text, where `shell` would be too light on white.

### Secondary
- **Signal Yellow** (`print-yellow`): the round primary key, the selected chip ring, the 策略提示 ring and 建議 tag, the lit mode-key swatch, key sublegends, rule-spec terms, emphasis in faceplate prose, the bezel's "BJ 3:2" print, and the global focus ring.

### Tertiary
- **Chip mouldings** (`chip10` blue, `chip50` orange, `chip100` black, `chip500` purple): only the four chip keys. Each has a white dashed edge-spot ring.

### Neutral
- **Faceplate Charcoal** (`face`): the faceplate (`main.layout`) and the mode keys. **Recess** (`face-deep`) is the coach plate and the segmented control's well. **Bezel Black** (`bezel`) frames the LCD and fills the speaker grille.
- **Rubber Key** (`key`): every key and `kbd`.
- **Silkscreen White** (`print`): key legends and faceplate text. **Dim Print** (`print-dim`, 72 %) is secondary faceplate print: bezel spec line, prompt sub-line, notes, coach "why" line, segmented-control off state.
- **LCD Glass** (`lcd`): the main glass, data windows, card slots, the brandmark and the OK/NG badge on the coach plate.
- **Segment Ink** (`ink`): everything printed on the glass: digits, rules, card borders, filled bars, lit lamps (reversed `lcd` on `ink`).
- **Ghost** (`ghost`, `ink` at 8.5 %): unlit segments, empty slot outlines (inline SVG at `stroke-opacity .09`), unfilled bar ticks, idle hand borders.
- **Red Filter** (`red-ink`): hearts and diamonds, and the cut-card marker on the shoe gauge. Nothing else on the glass is red.
- **Leaflet Paper** (`paper`) with **Leaflet Charcoal** (`paper-ink`): the manual.

### Named Rules
**The Three Materials Rule.** Every surface is shell, faceplate or glass (plus the leaflet). A new element goes on one of them. It never floats in its own card, gradient or tint.

**The One Yellow Key Rule.** Exactly one key per stage is yellow and round: 發牌 DEAL, 同注再發, or 補充籌碼. Every other key is charcoal rubber. Yellow elsewhere is print (sublegends, terms, rings), not another primary.

**The Two Inks on Glass Rule.** The LCD prints in `ink` and its ghost only. Red suits and the cut card print through `red-ink`. Win, lose and push are told by reversal, solid border and dashed border, never by green or red.

## Typography

**Segment Fonts:** `'LCD'` is a single family split by `unicode-range`: DSEG7 covers space, `-` `.` `0-9` `:` `—` `−`, and DSEG14 covers `+` `%` `±`. `'LCD14'` (DSEG14) sets card ranks, OK/NG and the badge. All are inlined WOFF2 with `font-display: block`.
**Silkscreen Font:** Michroma (inlined), for Latin printed on the device: logo, bezel spec line, `CREDIT/DEALER/PLAYER`, key sublegends, chip values, strategy coordinates, `kbd`.
**Text Font:** Huninn (`'Huninn Shiori'`, jf open 粉圓, an inlined subset), for all Chinese, including Chinese inside LCD-font runs via fallback.

**Character:** segment digits that read as hardware, a wide technical Latin silkscreen, and a soft round Chinese face that keeps a dense device friendly.

Everything is weight 400; `b/strong` are reset to 400 and get emphasis from size (1.08em on glass) or yellow (on the faceplate). Huninn is subset to each page's text: run `python3 tools/trip-font.py --page blackjack-game.html` (or `blackjack.html`) after any text change.

### Hierarchy
- **Logo** (Michroma 21px, 24px ≥1080, .16em): `BLACKJACK` on the shell, beside the `21` brandmark (a small LCD with ghost `88`).
- **Readout large** (LCD 27px; 25 ≤599, 23 ≤370): 籌碼 CREDIT and 本次輸贏. **Readout** (19px, 18 ≤599): the other status readouts. Window values run 15–26px.
- **Prompt** (16px, 18 ≥600): the message line on the glass.
- **Key legend** (Huninn 17px) over **Silkscreen** sublegend (Michroma 11px, .04em, yellow).
- **Labels on glass** (11–12.5px): zone labels, stat keys, window row names.
- **Bezel print** (Michroma 9px, .16em; 7.5px ≤599).
- **Manual** (14.5px / 1.75): leaflet text; headings 15–18px in `shell-ink`.

### Named Rules
**The Plain Digits Rule.** Readouts print plain digits through `lcdNum` / `lcdSigned` (no thousands separators, `±0` for zero), right-aligned, so each digit lands on its ghost 8. Each `.ro` carries `data-g` with one 8 per position.

**The Three Voices Rule.** Segment faces set digits, Michroma sets Latin silkscreen, Huninn sets Chinese. Don't use a segment face for words or Michroma for Chinese.

## Layout

The shell is the page. `.app` is capped at 1340px with padding `max(14px, safe-area) 12px 32px` (20px 22px 40px ≥600, 8px sides ≤370). The top band holds the logo and mode keys: a three-column grid on phones, wrapping flex ≥600.

- **Faceplate:** one `main.layout`, padding 16px (20px ≥1080, 12px ≤599, 10px ≤370), radius 28px (24px ≤599).
  - Below 1080px it is a single column: the LCD unit, then the windows.
  - At 1080px and up it is unit plus a 360px side, behind a 1px silkscreen rule (`rgba(245,243,238,.2)`, padding-left 24px).
  - At 1280px and up the side is 590px and runs as two CSS columns (gap 22px), with `#pnl-side` `break-before: column` and panels `break-inside: avoid`.
  - Hidden data panels (`.no-side`) give a single column capped at 960px.
- **Sticky unit:** at ≥1080px wide and ≥760px tall, the LCD unit is `position: sticky; top: 20px`.
- **Inside the unit:** the stack is bezel/LCD, then the key deck, the coach plate and the foot (note, keymap, grille), with a 16px gap. On phones the chip keys and DEAL sit directly under the glass.
- **Card slots** scale with breakpoints (`--cw/--ch/--cg`): 38×54/5 base, 52×74/8 ≥600, 58×83/9 ≥1080, 36×51/5 ≤370. Split hands and computer seats use smaller sets. Each slot set redraws the ghost tile at its own size.
- **Action keys:** six-column grid on phones (HIT/STAND/DOUBLE two-up, SPLIT/SURRENDER three-up), five equal keys ≥600, gap 9px.
- **Panels** are separated by a 1px silkscreen top rule with 12px padding and a 14px stack gap. They are not cards.
- **Trainer:** at ≥1280px the side is a single 400px column (`.layout.lab`). On phones its shell band is a 4-column grid, and the restart key spans columns 2–4 beside the 練習題數 select.

## Elevation & Depth

Depth is moulded plastic. The shell is flat. The faceplate sits on it with one soft drop. Keys stand proud and travel down. Glass and windows are recessed with inset shadows. Nothing glows.

### Shadow Vocabulary
- **Faceplate** (`inset 0 1px 0 rgba(255,255,255,.07), 0 12px 26px rgba(90,14,4,.38)`): the one plate on the shell.
- **Key up** (`--key-depth: inset 0 1px 0 rgba(255,255,255,.16), inset 0 -3px 0 rgba(0,0,0,.32), 0 3px 5px rgba(0,0,0,.42)`): every key at rest.
- **Key down** (`--key-down: inset 0 1px 0 rgba(255,255,255,.1), inset 0 -1px 0 rgba(0,0,0,.3), 0 1px 2px rgba(0,0,0,.42)`) plus `translateY(2px)`: `:active`, and the selected chip.
- **Glass recess** (`inset 0 3px 8px rgba(0,0,0,.4), inset 0 -1px 0 rgba(255,255,255,.22)`): main LCD. Windows use `inset 0 2px 6px rgba(0,0,0,.38)`; the brandmark adds a 3px `bezel` ring.
- **Leaflet** (`0 22px 48px rgba(0,0,0,.45)`) over a `rgba(36,10,4,.66)` scrim: the manual lying on the device.

### Named Rules
**The Key Travel Rule.** A key's press is `translateY(2px)` plus the down shadow over .06s ease-out. This is the only eased motion in the world. Disabled keys drop to .38 opacity with no depth.

## Shapes

Toy-moulded rounds. The faceplate has 28px corners. The bezel is 16px with a larger 34px bottom-left corner (the device's asymmetric cut). The glass is 8px and the windows are 7px. Keys are 12px oblongs; the primary key, chips and the close key are circles; mode keys and the segmented control are pills. On the glass: card slots are 5px with a 2px `ink` border, lamps and result tags are 3–4px, and bet rings are dashed segment circles drawn as inline SVG (a second inner ring when a bet is placed). The leaflet is 6px.

## Components

### Rubber keys
- **Action keys** (要牌 / 停牌 / 加倍 / 分牌 / 投降, plus 保險 keys): charcoal `key`, 62px tall (68px ≥600). They carry a white Huninn legend, a yellow Michroma sublegend with the keyboard letter (`.kb`, hidden ≤599), and an 11px swatch top-left in the manual's code: HIT white, STAND solid charcoal, DOUBLE hatched, SPLIT solid red, SURRENDER charcoal with a red rule.
- **Primary key:** a round yellow 78px key (88 ≥600, 70 ≤370) with an `ink` legend and a Michroma sublegend. Exactly one per stage.
- **Secondary keys** (撤回 / 清除 / 上局 / 下注 ×2 / 調整下注): charcoal, min 44px tall, 14px text.
- **Hint state:** 策略提示 marks the recommended key with a 3px yellow outline (offset 3px) and a yellow 建議 pill tab on its top edge.
- **Focus:** a global 3px yellow outline, offset 3px. Bet rings use a 2px dashed `ink` outline on the glass.
- **Trainer round keys:** 下一題 / 看成績 on the coach plate and 再挑戰 in the summary leaflet are the round yellow key of their stage.

### Chip keys
52px circles (58 ≥600, 44 ≤370), moulded in the chip colour, with a white inset ring, a dashed edge ring and a white Michroma value. The selected chip is pressed down and ringed in `face` plus 3px yellow.

### Mode keys
Charcoal pills on the shell (38px, 34 ≤599). Toggles carry a 9px lamp swatch: dark red when off, yellow when `aria-pressed="true"`. `.brand small` uses balanced wrapping (`text-wrap: balance`).

### Selects
A charcoal `face` pill (min 38px) with a white chevron, used for the trainer's 練習題數 on the shell and the Monte Carlo sample count on the faceplate. The trainer's restart key (開始 N 題挑戰) is a charcoal mode key beside it.

### LCD glass
The unit's screen holds the status readouts, a 2px `ink` rule, the dealer slots, a dashed divider that carries the toast, computer seats, player hands and bet rings, then the message line with the OK / NG lamp.
- **Cards:** a lit slot (`lcd` with an `ink` border), with the rank in `LCD14` and a small and a large SVG suit. Red suits use `red-ink`. The hole card is a 7px diagonal hatch.
- **Active hand:** a 2px `ink` border. Idle split hands use a `ghost` border.
- **Message line:** `.msg` wraps. A long prompt keeps whole words, and the OK / NG lamp drops below it, right-aligned.
- **Trainer status row:** four readouts (題數 / 策略分數 / 連續答對 / 答對率), two-up on phones and four-up at ≥600, where each label is right-aligned over its value.

### Data windows
Each panel has a white Huninn title, an optional `sm` key and a round collapse key. The body is an `lcdw` window. Bars are segmented with masks (5px on, 2px off) over ghost ticks, the dealer distribution uses stacked 4/2px segments, and paytable values use the LCD face. The rules panel prints straight on the faceplate, with yellow terms. The faceplate legend repeats the chart code; its 降 swatch keeps its red rule.
- **Monte Carlo (trainer):** a select plus a charcoal pill key (開始模擬), with results in an LCD window: a table with a 2px `ink` header rule, dashed row rules and LCD-face values. The best row is reverse video (`lcd` on `ink`), never a colour. Each row carries a segmented `.evbar` (4px on, 2px off), reversed inside the best row.

### Coach
After each decision, the OK / NG lamp lights on the glass (reversed `ink`). NG blinks three times with `lamp-blink`, returning to its ghost colour between blinks rather than vanishing. Below the keys, the reason prints on the recessed `face-deep` coach plate: an LCD `okw` badge, the verdict (yellow when wrong), a Michroma strategy coordinate, and the body with yellow emphasis.
- **Trainer explanation:** four parts (`.explain-grid`, two columns ≥600). Each `.explain-box` sits under a silkscreen rule with a white heading over `print-dim` text and no numbering. The EV formula prints in a small LCD window (`lcd` glass, 6px, LCD face). The stage ends in the round yellow 下一題 key.

### Manual (modals)
A white two-colour leaflet in `paper-ink` and red, with a 4px `shell` rule under its header. Strategy cells:
- 要: white with an ink rule.
- 停: solid charcoal.
- 倍: hatched (135°, with a white plate behind the letter).
- 分: solid red.
- 降: white with a red rule and red text.

The graded cell (`.cur`) gets a 3px charcoal outline. Row labels and the corner header are sticky, and opening the chart scrolls the graded cell beside its labels (`showCell()`). Rule cards are separated by 3px charcoal top rules.
- **Summary leaflet (trainer):** the score is a ghost-8 `.ro` (`#summaryScore`, `data-g="888%"`, min four cells) on a 56px LCD inset ringed in `bezel`. 再挑戰 is the round yellow key.

### Motion (the LCD grammar)
All glass motion uses `steps(1,end)`:
- `lcd-blink` (.42s): a dealt or flipped card and a dropped bet tick blink twice, then hold.
- `lcd-blink3` (1s): result words and a positive prompt blink three times.
- `lamp-blink` (1s): the NG lamp blinks three times back to its ghost.
- `lcd-on` (.12–.16s): split slides, the toast and the coach plate switch on.
- `lcd-peek` (.6s, infinite): the hole card flickers its hatch while the dealer peeks.

`prefers-reduced-motion` removes every animation and transition. Async card pacing (`wait`) shortens to ≤60 ms.

### The trainer in the world (`blackjack.html`)
The trainer is the same device in drill mode. The same shell, faceplate, glass, keys and leaflet carry it. One scenario is a dealer slot and player slots over the same action keys, with the tally on the glass, explanations on the coach plate and Monte Carlo in a data window. Its chart uses the same strategy-cell code.

## Do's and Don'ts

### Do:
- **Do** put every new element on the shell, the faceplate, the glass or the leaflet, and separate faceplate panels with silkscreen rules.
- **Do** give every segment readout a `data-g` ghost of 8s and print it through `lcdNum` / `lcdSigned`.
- **Do** animate the glass only with `steps(1,end)` blinks and switches: two blinks for a dealt card, three for a result.
- **Do** keep exactly one round yellow primary key per stage, and keep the five action swatches in the manual's two-ink code.
- **Do** set digits in the segment faces, Latin silkscreen in Michroma and Chinese in Huninn, then run `python3 tools/trip-font.py --page <page>` for the page you edited.
- **Do** keep the file single and self-contained (inlined fonts, inline SVG, no CDN), with nothing saved.
- **Do** change the tables and rules on both pages together, and make any change to shared components on both pages.
- **Do** mark a best or chosen row by reverse video, not colour.

### Don't:
- **Don't** fade, slide or ease anything on the glass; only key travel is eased.
- **Don't** add green felt, gold, glow, gradients as fills, or floating cards.
- **Don't** colour win/lose in green/red on the glass; use reversal and borders. Red on the glass is for suits and the cut card only.
- **Don't** add a second yellow key, or use chip colours outside the chip keys.
- **Don't** add thousands separators or extra characters to readouts; the digits would fall off their ghosts.
- **Don't** suggest real money or a real casino brand.
