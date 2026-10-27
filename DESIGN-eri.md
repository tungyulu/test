---
name: 欸哩照顧手冊 · Grouped Care Notes
description: "A dog-sitting handbook built as native grouped-inset system UI in the Apple Reminders / Apple Health manner: notes and reminders only, cool grey ground, white rounded sections with inset hairlines, one warm caramel accent, red kept for 不舒服時."
colors:
  ground: "#F2F2F7"
  cell: "#FFFFFF"
  ink: "#111114"
  ink-2: "#4A4A52"
  separator: "#C6C6CB"
  bar: "rgba(249,249,251,.88)"
  accent: "#B85A0A"
  accent-ink: "#9C4A06"
  accent-soft: "#FBEBDC"
  food: "#B85A0A"
  food-ink: "#9C4A06"
  walk: "#2E7D32"
  habit: "#3557C4"
  habit-ink: "#3557C4"
  sos: "#C62828"
  sos-ink: "#B71C1C"
  sos-soft: "#FDECEC"
  doc: "#5E5E66"
  avatar-disc: "#EFE4D6"
  dark-ground: "#000000"
  dark-cell: "#1C1C1E"
  dark-ink: "#F2F2F7"
  dark-ink-2: "#C2C2C8"
  dark-separator: "#3A3A3E"
  dark-bar: "rgba(22,22,24,.88)"
  dark-accent: "#D9782A"
  dark-accent-ink: "#F2A35E"
  dark-accent-soft: "#3A2614"
  dark-food: "#C96A1C"
  dark-food-ink: "#F2A35E"
  dark-walk: "#2F8A3A"
  dark-habit: "#3E63D6"
  dark-habit-ink: "#93AAF7"
  dark-sos: "#D64040"
  dark-sos-ink: "#FF8A80"
  dark-sos-soft: "#3A1717"
  dark-doc: "#636369"
typography:
  large-title:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "34px"
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: "-.01em"
  section-title:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "24px"
    fontWeight: 700
    lineHeight: 1.25
  closing:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "22px"
    fontWeight: 700
    lineHeight: 1.55
  row-key:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "20px"
    fontWeight: 600
    lineHeight: 1.35
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "19px"
    fontWeight: 400
    lineHeight: 1.55
  detail:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: 1.55
  group-header:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "17px"
    fontWeight: 600
    lineHeight: 1.55
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif"
    fontSize: "15px"
    fontWeight: 600
    lineHeight: 1.55
rounded:
  section: "14px"
  tab: "12px"
  control: "10px"
  circle: "50%"
spacing:
  page-max: "600px"
  gutter: "16px"
  row-x: "16px"
  row-y: "14px"
  group-gap: "28px"
  header-inset: "4px"
components:
  section-list:
    backgroundColor: "{colors.cell}"
    rounded: "{rounded.section}"
  list-row:
    textColor: "{colors.ink}"
    typography: "{typography.row-key}"
    padding: "14px 16px"
  key-value-row:
    textColor: "{colors.ink}"
    typography: "{typography.detail}"
    padding: "14px 16px"
    height: "56px"
  sos-first-row:
    backgroundColor: "{colors.sos-soft}"
    textColor: "{colors.sos-ink}"
    typography: "{typography.section-title}"
    padding: "14px 16px"
  avatar:
    backgroundColor: "{colors.avatar-disc}"
    rounded: "{rounded.circle}"
    size: "64px"
  tab-bar:
    backgroundColor: "{colors.bar}"
    textColor: "{colors.ink-2}"
    typography: "{typography.caption}"
    height: "56px"
  tab-item:
    textColor: "{colors.ink-2}"
    typography: "{typography.caption}"
    rounded: "{rounded.tab}"
    height: "56px"
  tab-item-current:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.accent-ink}"
    rounded: "{rounded.tab}"
  tab-item-sos:
    textColor: "{colors.sos-ink}"
  tab-item-sos-current:
    backgroundColor: "{colors.sos-soft}"
    textColor: "{colors.sos-ink}"
    rounded: "{rounded.tab}"
---

# Design System: 欸哩照顧手冊 · Grouped Care Notes

## Overview

**Creative North Star: "The Phone's Own Notes"**

The handbook is the category standard played straight: it should read like notes and reminders the phone itself ships, at the craft level of Apple Reminders and Apple Health, without their branding. It is read, not operated: there is no checklist, no stored state and nothing to tick. A cool grey grouped ground carries white rounded sections; rows are a bold key over a quieter detail line, separated by inset hairlines; titles are large and bold. The readers are elderly parents opening a LINE link on a phone, so everything is set larger than the platform default (19px body, 20px row keys, 34px title) and nothing important is faint.

The page opens on the title and goes straight into the owner's three requests; there is no summary or status card. Each section is announced the Health way: a coloured line glyph beside a section title in the same colour (the three requests and the daily routine in caramel, food amber, walks green, habits blue, emergency red, the dog's profile a grey glyph under an ink title). Colour identifies a section's glyph and title and nothing else; rows stay white with ink text. Red belongs to 不舒服時 alone. Dark mode is the platform's true-black grouped scheme, not a tinted variant.

The single illustration is a small drawn avatar of the dog in a 64px circle beside the title, made of flat filled planes and following the owner's photo (chocolate tricolour long coat, white blaze and muzzle, tan brows and cheeks, yellow harness). The photo itself is not published. The page is still: apart from the browser's default anchor jump, nothing moves.

**Key Characteristics:**
- Grouped-inset system UI: grey ground, white 14px-radius sections, hairlines inset 16px from the leading edge.
- Notes, not tasks: key-over-detail rows, written-out rules, no checkboxes, counts, status cards or stored state.
- One warm caramel accent for the two leading sections, the current tab (tinted pill + 800 weight), inline times and focus.
- Section identity by coloured glyph + coloured title only (Health manner), never colour-square tiles.
- System sans at enlarged sizes; secondary text is a dark grey that keeps ≥7.8:1.
- A fixed translucent bottom tab bar with five destinations; emergency always reachable in one tap.
- No motion.

## Colors

A neutral platform palette with one warm accent and four section hues, each hue paired with a darker (light mode) or lighter (dark mode) "-ink" variant wherever it sets text.

### Primary
- **Caramel** (accent): the star glyph of 最重要的三件事, the clock glyph of 每天的作息, the focus outline and the caret.
- **Deep Caramel** (accent-ink): every piece of caramel text: the titles 最重要的三件事 and 每天的作息, the current tab label, inline times inside a row (晚上 10–11 點), links. 6.18:1 on white, 5.54:1 on the ground.
- **Caramel Wash** (accent-soft): the current tab's pill (accent-ink on it is 5.31:1 light, 6.94:1 dark) and text selection.

### Secondary
- **Food Amber** (food, food-ink): the 吃飯 glyph and title; deliberately the accent's hue in light mode, since feeding is the core of the handover.
- **Leash Green** (walk): glyph and title of 散步和上廁所.
- **Habit Blue** (habit, habit-ink): glyph and title of 欸哩的習慣; dark mode lifts the title to a pale blue.

### Tertiary
- **Alarm Red** (sos, sos-ink, sos-soft): the 不舒服時 glyph and title, its tab label, the first row (先 LINE 我) on a pale red wash, and the bullet markers of the go-to-the-vet list; the wash also backs the 不舒服 tab when it is current.

### Neutral
- **Grouped Grey** (ground): page ground.
- **Cell White** (cell): every section list.
- **Ink** (ink): primary text, and instruction lines that must not read as secondary.
- **Secondary Ink** (ink-2): detail lines, group headers, the subtitle, key-value values, inactive tabs (7.87:1 on the ground, 8.78:1 on white).
- **Hairline** (separator): inset row separators and the tab bar's top edge.
- **Frosted Bar** (bar): the translucent tab bar.
- **Doc Grey** (doc): the 欸哩的資料 glyph only; its title stays ink.
- **Avatar Cream** (avatar-disc): the avatar's backing disc, fixed in both themes on purpose so the chocolate coat reads against true black (checked in a dark-mode capture).

### Named Rules
**The One Warm Accent Rule.** Caramel is the only accent. It marks what leads (the three requests, the routine), where you are (the current tab's pill) and focus; no second accent is introduced.

**The Red Is Unwell Rule.** Red appears only in the 不舒服時 section and its tab. It never marks a meal, a request or a forbidden food (the 不能給他吃 bullets are grey).

**The Title-Not-Tile Rule.** A section's colour lives in its line glyph and its title text. Never put the glyph on a filled colour square; that reads as Settings, which the owner rejected.

## Typography

**Display Font:** the platform system sans (-apple-system / PingFang TC, then Noto Sans TC, Microsoft JhengHei)
**Body Font:** the same stack
**Label/Mono Font:** none; the Japan clock in the emergency row uses `font-variant-numeric: tabular-nums`

**Character:** The phone's own face, the material of this world, set one size step larger than the platform default throughout for older readers. Hierarchy comes from size and weight (800 / 700 / 600 / 400) and from ink versus secondary ink.

### Hierarchy
- **Large title** (800, 34px, 1.15, -.01em): the dog's name 欸哩, once.
- **Section title** (700, 24px, 1.25): each section heading in its colour; the 先 LINE 我 row raises it to 800.
- **Closing** (700, 22px): the 謝謝爸媽！ line at the end.
- **Row key** (600, 20px, 1.35): the first line of every row; key-value keys drop to 500.
- **Body** (400, 19px, 1.55): base size and bulleted lists.
- **Detail** (400, 18px): the second line of a row and key-value values, in secondary ink; in ink when it is the instruction itself (the evening-meal rules, the emergency steps).
- **Group header** (600, 17px, secondary ink): 早上 / 晚上 / 需要的話 / 零食 and the other in-section labels; the subtitle beside the title is 17px at 400.
- **Caption** (600, 15px; 800 on the current tab): tab labels; the smallest size on the page.

### Named Rules
**The Nothing Small Rule.** No text below 15px, row content at 18px or larger, and no faint tint for content a parent must read; secondary text is a dark grey, never a lowered opacity.

**The Phrase Break Rule.** Chinese lines break between phrases: running text is wrapped in inline-block phrase spans (`.seg`) so a line never splits mid-phrase.

**The Bold Lead-In Rule.** When one row carries alternative rules, each rule is its own detail line in ink, opened by a bold condition word and a full-width space (**有吃完**　… / **沒吃**　…). The cases are written out; the reader never has to answer a control to see them.

## Layout

One centred column, max 600px, 16px side gutter, bottom padding of 104px plus the safe-area inset so the last content clears the tab bar. Order: title with avatar, then 最重要的三件事 directly below (8px top margin instead of the usual 28px), 每天的作息 (早上 / 晚上 / 需要的話), 吃飯, 散步和上廁所, 欸哩的習慣, 不舒服時, 欸哩的資料 (breed, sex, age, weight, microchip, vaccines, last vet visit), and a centred closing line. Later groups are separated by 28px; section headers and group headers sit inset 4px from the list edge, group headers with 18px above and 8px below. Rows are 14px × 16px; key-value rows are at least 56px tall with the value right-aligned. A detail line that starts a new rule inside a row gets 8px above it.

The bottom tab bar is fixed, full width, with its five items constrained to the same 600px column. Scroll padding (12px top, 96px bottom) keeps anchored sections clear of the bar. Print hides the tab bar, prints on white and keeps groups unbroken.

## Elevation & Depth

Flat, by tonal layering: white sections on a grey ground (true black and #1C1C1E in dark). No shadows anywhere. The one platform material is the tab bar.

### Shadow Vocabulary
- **Frosted bar** (`backdrop-filter: saturate(180%) blur(20px)` over the translucent bar colour, 1px hairline top): the tab bar only.

### Named Rules
**The Flat Sections Rule.** Sections never float. Depth is the grey/white step; nothing on the page casts a shadow.

## Shapes

Gently rounded containers (14px, clipped) for every section list; 12px for tab items; 10px for the focus outline. The avatar is a full circle (64px). Icons are a seven-symbol inline SVG sprite on a 24-unit grid, one 2px round-capped stroke (2.2 at the 28px section size, 26px in the tab bar): star, clock, bowl, paw, heart, cross, document.

## Components

### Section Lists / Rows
- **Corner Style:** 14px, clipped.
- **Background:** cell white on the grouped ground.
- **Shadow Strategy:** none (see Elevation).
- **Border:** none; rows are divided by a 1px separator inset 16px.
- **Internal Padding:** 14px 16px; a row key over a detail line. Key-value rows (欸哩的資料) put the value right-aligned in secondary ink.
- **Bullets:** disc markers inside a row, red in the go-to-the-vet list, secondary ink in the forbidden-food list, each list closed by a detail line saying where the list comes from.

### Section Header
A 28px line glyph in the section's colour, then the 24px title in the same colour (or its "-ink" variant). Group headers (17px, secondary ink) subdivide inside a section.

### Evening Meal Row (signature)
The routine's evening meal: a row key that names the condition (吃飯：看早上那份有沒有吃完) followed by two ink detail lines, each opened by a bold lead-in (**有吃完** / **沒吃**), so both portions are always visible.

### Emergency First Row
The first row of 不舒服時 on the pale red wash: 先 LINE 我 in 800 24px red, then in ink the time difference with a live tabular Japan clock (refreshed every 30 s; the page's only clock) and when to take him straight to the vet.

### Navigation (tab bar)
Fixed bottom, frosted, 1px hairline top. Five items (作息 / 吃飯 / 散步 / 習慣 / 不舒服), each a 26px line glyph over a 600 15px label, at least 56px tall, 12px radius, 2px side margin. Inactive items are secondary ink. The item for the section in view (the last section whose top has passed 35% of the viewport, marked `aria-current`) becomes a caramel-wash pill with accent-ink text at 800, so the current place is shown by fill and weight, not colour alone. The 不舒服 item is always sos-ink and takes the red wash when current. Tapping jumps with the browser's default anchor scroll; no smooth-scroll or transition is added.

### Avatar
A 64px circle on the fixed avatar-cream disc holding a flat-plane SVG of the dog drawn from the owner's photo. It is decorative (`aria-hidden`) and appears once, beside the large title.

## Do's and Don'ts

### Do:
- **Do** put every new block of content in a white 14px-radius section on the grouped ground, with inset hairline separators between rows.
- **Do** announce a new section with a line glyph from the sprite (24-unit grid, 2px round stroke) and a title in the same colour.
- **Do** write alternative rules out in full as ink detail lines with a bold lead-in, rather than hiding one behind a control.
- **Do** use the accent for what leads, where you are and focus, and accent-ink whenever caramel sets text; mark the current place with fill and weight as well as colour.
- **Do** keep body text at 19px, details at 18px and nothing below 15px; secondary text in ink-2, never by opacity.
- **Do** wrap Chinese phrases in `.seg` spans so lines break between phrases.
- **Do** define every new colour in both the light and the true-black dark set, and keep text pairs at 4.5:1 or better.

### Don't:
- **Don't** place a section glyph on a filled colour square or build Settings-style rows (the owner rejected anything settings-like).
- **Don't** use red outside 不舒服時 and its tab.
- **Don't** add checkboxes, progress counts, a summary or status card, or saved state; the owner asked for notes and reminders only.
- **Don't** add decorated pet-app cuteness (stickers, paw-print patterns, cartoon type) or dashboard stat cards; the owner named childish, sticker-like, busy and cold-app-like as wrong.
- **Don't** add shadows, gradients or motion; the page is still.
- **Don't** publish the owner's photo of the dog; the drawn avatar stands in for it.
