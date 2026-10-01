#!/usr/bin/env python3
"""Rebuild the dot-matrix LED glyph table inlined in livecam.html.

The departure board, clocks and weather ticker on livecam.html are drawn dot by
dot on <canvas> from 16-dot bitmaps.  The bitmaps come from GNU Unifont (SIL OFL
1.1 / GPL-2.0+ with font exception), read from the system font:

    apt-get install fonts-unifont      # /usr/share/fonts/opentype/unifont/unifont.otf

The page keeps only the glyphs it uses: every character inside its <script>
blocks plus printable ASCII.  Run this after editing any text the LED draws
(TRIP, area names, weather words, board messages); a character missing from the
table is still drawn, but from the browser's own font at 16px, which looks rougher.

    python3 tools/led-glyphs.py              # rewrite livecam.html in place
    python3 tools/led-glyphs.py --check      # only report missing glyphs
"""
import argparse
import base64
import re
import sys
from pathlib import Path

from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
FONT = Path('/usr/share/fonts/opentype/unifont/unifont.otf')
BLOCK_RE = re.compile(r'/\*LED-GLYPHS-BEGIN\*/.*?/\*LED-GLYPHS-END\*/', re.S)


def page_chars(src):
    body = BLOCK_RE.sub('', src)
    text = ''.join(re.findall(r'<script>(.*?)</script>', body, re.S))
    chars = set(chr(c) for c in range(0x21, 0x7f))
    chars |= {c for c in text if ord(c) > 0x7f and ord(c) <= 0xffff and not c.isspace()}
    return sorted(chars)


def glyph_bits(font, ch):
    cmap = font.getBestCmap()
    name = cmap.get(ord(ch))
    if name is None:
        return None
    gs = font.getGlyphSet()
    pen = DecomposingRecordingPen(gs)
    gs[name].draw(pen)
    upp = font['head'].unitsPerEm / 16            # Unifont: 4 units per dot
    cols = round(gs[name].width / upp)
    if cols not in (8, 16):
        return None
    polys, cur = [], []
    for op, args in pen.value:
        if op == 'moveTo':
            cur = [args[0]]
        elif op == 'lineTo':
            cur.append(args[0])
        elif op in ('closePath', 'endPath'):
            if cur:
                polys.append(cur)
            cur = []
        else:                                       # Unifont outlines are rectilinear
            return None
    asc = font['hhea'].ascent / upp                 # baseline sits 14 dots down
    rows = []
    for r in range(16):
        y = (asc - r - 0.5) * upp
        v = 0
        for c in range(cols):
            x = (c + 0.5) * upp
            wn = 0
            for p in polys:
                for i in range(len(p)):
                    (x1, y1), (x2, y2) = p[i], p[(i + 1) % len(p)]
                    side = (x2 - x1) * (y - y1) - (x - x1) * (y2 - y1)
                    if y1 <= y < y2 and side > 0:
                        wn += 1
                    elif y2 <= y < y1 and side < 0:
                        wn -= 1
            v = (v << 1) | (1 if wn else 0)
        rows.append(v)
    return cols, rows


def build(chars, font):
    half, full, blob, missing = [], [], bytearray(), []
    for ch in chars:
        g = glyph_bits(font, ch)
        if g is None:
            missing.append(ch)
            continue
        cols, rows = g
        (half if cols == 8 else full).append((ch, rows, cols))
    for ch, rows, cols in half + full:
        for v in rows:
            blob += v.to_bytes(cols // 8, 'big')
    h = ''.join(c for c, _, _ in half)
    f = ''.join(c for c, _, _ in full)
    esc = lambda s: s.replace('\\', '\\\\').replace('"', '\\"')
    js = ('/*LED-GLYPHS-BEGIN*/const LEDG={h:"%s",f:"%s",b:"%s"};/*LED-GLYPHS-END*/'
          % (esc(h), esc(f), base64.b64encode(bytes(blob)).decode()))
    return js, missing


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--page', default='livecam.html')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    if not FONT.exists():
        sys.exit(f'{FONT} not found: apt-get install fonts-unifont')
    page = ROOT / a.page
    src = page.read_text(encoding='utf-8')
    if not BLOCK_RE.search(src):
        sys.exit(f'{a.page}: no /*LED-GLYPHS-BEGIN*/ block')
    font = TTFont(str(FONT))
    chars = page_chars(src)
    js, missing = build(chars, font)
    have = re.search(r'const LEDG=\{h:"(.*?)",f:"(.*?)"', BLOCK_RE.search(src).group(0), re.S)
    old = set((have.group(1) + have.group(2)).replace('\\"', '"').replace('\\\\', '\\')) if have else set()
    new = [c for c in chars if c not in old and c not in missing]
    print(f'{len(chars)} characters, {len(chars) - len(missing)} in Unifont'
          + (f', not in Unifont: {"".join(missing)}' if missing else ''))
    if a.check:
        print('missing from the table: ' + (''.join(new) if new else 'none'))
        sys.exit(1 if new else 0)
    page.write_text(BLOCK_RE.sub(lambda m: js, src), encoding='utf-8')
    print(f'wrote {a.page} ({len(js) // 1024} KB glyph table)')


if __name__ == '__main__':
    main()
