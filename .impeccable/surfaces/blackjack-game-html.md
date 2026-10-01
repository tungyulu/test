---
version: 1
slug: "blackjack-game-html"
primary_target: "blackjack-game.html"
related_targets: []
---

## Scope

`blackjack-game.html`, the 21點實戰牌桌: a full redesign that replaces the green-felt-and-gold casino skin. Every rule, flow, number and keyboard shortcut stays (see PRODUCT.md › Blackjack table). Visitor mode: **Operate** (play rounds and learn basic strategy). Playing feel and learning carry equal weight, and phone and desktop count equally. A self-contained single file with no CDN; nothing is saved. `blackjack.html` (the trainer) adopts this world later, so the system must also carry a drill page.

## Direction contract

THESIS: The table is a 1980s pocket LCD blackjack game. Numbers are segment readouts with their ghost 8s showing. Cards are fixed LCD slots that light up. Every action is a rubber key, and the coach is an OK / NG segment lighting up on the glass. It refuses the green-felt casino skin and the dark "table plus card panels" dashboard.

OWN-WORLD:
- Moulded shell: a drenched tomato-red plastic shell owns the whole page.
- Faceplate: charcoal, printed with white and signal-yellow silkscreen.
- LCD: a recessed grey-green reflective panel. Segment ink is near-black; unlit segments ghost at about 7%. Red suits print through a red filter.
- Rubber keys: charcoal oblong keys, a round yellow key for the primary action, and chip keys moulded in the chip colours.
- Type: DSEG 7/14-segment numerals, Michroma for Latin silkscreen, Huninn for Chinese.
- Data unit: small LCD windows set into the faceplate.
- Manual: the rules and strategy chart are a two-colour printed leaflet, charcoal and red on white.

STORY: A toy game machine that is obviously blackjack. Press chip keys, then DEAL; the cards light up and you press HIT or STAND. After each decision the glass lights OK or NG, and the faceplate prints the reason. The odds and the count live in their own windows.

FIRST VIEWPORT:
- Phone: silkscreen logo and six small mode keys; the LCD nearly full-width (credit / bet / session readouts, dealer slots, bet rings); the chip keys and DEAL directly under the glass, within thumb reach.
- Desktop: the device centred; LCD plus key deck on the left, the data unit's windows on the right.

FORM: handheld LCD casino game, #4 on my re-rolled list. Seed 73dec062: the first roll assigned the Thorp paperback; the user asked for bolder; re-roll 1 (bolder register unavailable, degraded) assigned this, and the user chose it. Code-led.

Signature interaction (the LCD grammar): nothing slides or fades. Segments switch on and off. A dealt card's slot blinks twice, then holds. A result word blinks. Keys physically depress. Ghost segments are always visible.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
