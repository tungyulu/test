---
version: 1
slug: "yacht-html"
primary_target: "yacht.html"
related_targets: []
---

# yacht.html · 快艇骰子

Scope: the Yacht dice game (5 dice, up to 3 rolls, 13 categories). Visitor mode: **Experience** (the visitor is inside the game). Phone and desktop equally, alone against the CPU or two people passing one device. Full redesign: new world. Rules, scoring, the 1P-vs-CPU and 2P modes and the greedy CPU stay exactly as they are; no new features. The owner chose the regatta direction and asked for it bolder.

## Direction contract

THESIS: A game of Yacht is a yacht race. The page is the sea seen from above: both boats sail one course, and every category you score moves your boat forward by those points, so the lead is a distance you can see. Dice you hold are hoisted as International Code of Signals numeral pennants on a halyard. It refuses the category default: a green felt tray, a dice cup and a white scorecard table under a header.

OWN-WORLD: the page is drenched in deep chart blue with lighter depth contours, scattered soundings and a magenta compass rose; buff sand islands. Flag colours only, flat and full strength: signal red, yellow, blue, black, white. Numeral pennants 1–6 and letter flags drawn to the ICS patterns; Y (Yankee) is 快艇. The scorecard is the race committee's white results board, ruled black, previews written in grease pencil and scored cells stamped. Archivo (condensed heavy, sail-number lettering) for numerals, Noto Sans TC 900 / 500 for Chinese. No rope, anchors or wheels.

STORY: start → read the flag hoist that spells YACHT and pick 對 CPU or 雙人 → roll, hoist the dice to keep, roll again → tap a row on the board → watch your boat surge along the course while the other sails beside it → at round 13 the finish gun and the results.

FIRST VIEWPORT: phone: a thin strip (back, title, round n/13) → the course chart, full width, about 40 % of the height, both boats on the line with 50-point distance ticks → the halyard of held pennants over five large dice (~64px) → the yellow 擲骰 key with three roll pennants → the board starts below. Desktop: course chart and dice on the left two thirds, the results board as a tall white panel on the right.

FORM: 帆船賽 (regatta: chart + signal flags + committee results board), position 7 of my ordered list, seed key ac0120dd (degraded roll, no challengers), pushed bolder at the owner's request. Signature interaction: scoring a row stamps the board cell and sails your boat along the course to its new total, its wake drawing behind it; a held die flies up to the halyard as its pennant. Yacht (50) sets a full spinnaker across the chart. Motion is sailing and hoisting only; reduced motion places everything instantly.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
