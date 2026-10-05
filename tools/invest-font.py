#!/usr/bin/env python3
"""Re-subset and inline invest.html's two fonts from the page's current text.

  'Form Ming' — Noto Serif TC 700 (SIL OFL), the passbook's pre-printed form
                lettering: h1-h3, th, summary and the .lbl .folio .clause-k .k
                .seal .sqseal .tag classes.
  'Pin Dots'  — the passbook printer's dot-matrix entries (every .dm and
                .code): a font built here from GNU Unifont's 16-dot bitmaps
                (SIL OFL 1.1 / GPL2+ with font exception), one round pin dot
                per lit pixel, so entries read as impact-printed dots.

Run after any content edit (pip install fonttools brotli):
    python3 tools/invest-font.py            # rewrite the inlined @font-face block
    python3 tools/invest-font.py --check    # only report glyphs the fonts lack

Unifont comes from the system package (fonts-unifont); Noto Serif TC is fetched
once from Google Fonts into ~/.cache/invest-font/.
"""
import base64, importlib.util, io, math, pathlib, re, sys, urllib.request
from html.parser import HTMLParser
from fontTools.ttLib import TTFont
from fontTools.subset import Subsetter, Options
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE = ROOT / 'invest.html'
CACHE = pathlib.Path.home() / '.cache' / 'invest-font'
UNIFONT = pathlib.Path('/usr/share/fonts/opentype/unifont/unifont.otf')
MING_CSS = 'https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@700'

MING_TAGS = {'h1', 'h2', 'h3', 'th', 'summary'}
MING_CLASSES = {'ptitle', 'lbl', 'folio', 'clause-k', 'k', 'seal', 'sqseal', 'tag', 'kseal'}
DOT_CLASSES = {'dm', 'code'}
# text the script (and CSS content) writes at runtime
JS_MING = '今天下一筆以下未印'
JS_DOTS = '本頁已印滿'
ASCII = ''.join(chr(c) for c in range(0x20, 0x7f))


class Collect(HTMLParser):
    VOID = {'meta', 'link', 'br', 'img', 'input', 'hr', 'path', 'source'}

    def __init__(self):
        super().__init__()
        self.stack, self.ming, self.dots, self.skip = [], set(), set(), 0

    def handle_starttag(self, tag, attrs):
        if tag in ('style', 'script'):
            self.skip += 1
        if tag in self.VOID:
            return
        cls = set((dict(attrs).get('class') or '').split())
        self.stack.append((tag, cls))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in ('style', 'script'):
            self.skip -= 1
        if tag in self.VOID:
            return
        while self.stack:
            t, _ = self.stack.pop()
            if t == tag:
                break

    def handle_data(self, data):
        if self.skip:
            return
        chars = set(data) - set(' \n\t\r')
        if any(t in MING_TAGS or c & MING_CLASSES for t, c in self.stack):
            self.ming |= chars
        if any(c & DOT_CLASSES for _, c in self.stack):
            self.dots |= chars


def ming_source():
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / 'NotoSerifTC-700.ttf'
    if not path.exists():
        css = urllib.request.urlopen(urllib.request.Request(MING_CSS, headers={'User-Agent': 'curl/8'})).read().decode()
        url = re.search(r'url\((https://[^)]+)\)', css).group(1)
        path.write_bytes(urllib.request.urlopen(url).read())
    return path


def subset(src, text):
    font = TTFont(src)
    cmap = font.getBestCmap()
    missing = sorted(ch for ch in text if ord(ch) not in cmap)
    opts = Options()
    opts.flavor = 'woff2'
    opts.layout_features = ['kern', 'liga', 'palt', 'vert', 'vrt2']
    opts.name_IDs = ['*']
    opts.notdef_outline = True
    sub = Subsetter(opts)
    sub.populate(text=text)
    sub.subset(font)
    buf = io.BytesIO()
    font.flavor = 'woff2'
    font.save(buf)
    return buf.getvalue(), missing


def _glyph_bits():
    spec = importlib.util.spec_from_file_location('led_glyphs', ROOT / 'tools' / 'led-glyphs.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.glyph_bits


PITCH, DOT = 64, 0.5           # 16 dots per em; dot radius as a share of the pitch


def build_dots(text):
    """Pin-dot font: every lit Unifont pixel becomes one octagonal (round at
    text sizes) dot, like a 16-pin passbook printer."""
    bits = _glyph_bits()
    src = TTFont(UNIFONT)
    order, cmap, glyphs, metrics, missing = ['.notdef'], {}, {}, {}, []
    glyphs['.notdef'] = TTGlyphPen(None).glyph()
    metrics['.notdef'] = (8 * PITCH, 0)
    r = PITCH * DOT
    for ch in text:
        if ch == ' ':
            name = 'space'
            order.append(name); cmap[32] = name
            glyphs[name] = TTGlyphPen(None).glyph(); metrics[name] = (8 * PITCH, 0)
            continue
        g = bits(src, ch)
        if g is None:
            missing.append(ch)
            continue
        cols, rows = g
        pen, xmin = TTGlyphPen(None), cols * PITCH
        for ri, v in enumerate(rows):
            cy = (13.5 - ri) * PITCH          # row 14 sits on the baseline
            for c in range(cols):
                if v >> (cols - 1 - c) & 1:
                    cx = (c + .5) * PITCH
                    pts = [(round(cx + r * math.cos(math.radians(22.5 + 45 * k))),
                            round(cy + r * math.sin(math.radians(22.5 + 45 * k)))) for k in range(8)]
                    pen.moveTo(pts[0])
                    for q in pts[1:]:
                        pen.lineTo(q)
                    pen.closePath()
                    xmin = min(xmin, round(cx - r))
        name = 'uni%04X' % ord(ch)
        order.append(name); cmap[ord(ch)] = name
        glyphs[name] = pen.glyph(); metrics[name] = (cols * PITCH, xmin if xmin < cols * PITCH else 0)
    fb = FontBuilder(16 * PITCH, isTTF=True)
    fb.setupGlyphOrder(order)
    fb.setupCharacterMap(cmap)
    fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=14 * PITCH, descent=-2 * PITCH)
    fb.setupNameTable({'familyName': 'Pin Dots', 'styleName': 'Regular',
                       'copyright': 'Generated from GNU Unifont glyphs (SIL OFL 1.1)',
                       'licenseDescription': 'SIL Open Font License 1.1'})
    fb.setupOS2(sTypoAscender=14 * PITCH, sTypoDescender=-2 * PITCH, sTypoLineGap=0,
                usWinAscent=14 * PITCH, usWinDescent=2 * PITCH)
    fb.setupPost()
    buf = io.BytesIO()
    fb.font.flavor = 'woff2'
    fb.font.save(buf)
    return buf.getvalue(), missing


def face(family, data, weight):
    b64 = base64.b64encode(data).decode()
    return ("  @font-face { font-family: '%s'; font-weight: %d; font-style: normal; font-display: swap;\n"
            "    src: url(data:font/woff2;base64,%s) format('woff2'); }\n" % (family, weight, b64))


def main():
    html = PAGE.read_text(encoding='utf-8')
    c = Collect()
    c.feed(html)
    ming = ''.join(sorted(c.ming | set(JS_MING) | set(ASCII)))
    dots = ''.join(sorted(c.dots | set(JS_DOTS) | set(ASCII)))
    ming_data, ming_miss = subset(ming_source(), ming)
    dots_data, dots_miss = build_dots(dots)
    for name, miss in (('Form Ming', ming_miss), ('Pin Dots', dots_miss)):
        if miss:
            print('%s lacks: %s' % (name, ''.join(miss)))
    print('Form Ming: %d chars, %d KB · Pin Dots: %d chars, %d KB'
          % (len(ming), len(ming_data) // 1024, len(dots), len(dots_data) // 1024))
    if '--check' in sys.argv:
        return
    block = ('/*@FONTS-BEGIN@*/\n' + face('Form Ming', ming_data, 700)
             + face('Pin Dots', dots_data, 400) + '/*@FONTS-END@*/')
    if '/*@FONTS@*/' in html:
        html = html.replace('/*@FONTS@*/', block)
    else:
        html = re.sub(r'/\*@FONTS-BEGIN@\*/.*?/\*@FONTS-END@\*/', lambda m: block, html, flags=re.S)
    PAGE.write_text(html, encoding='utf-8')
    print('updated', PAGE.name)


if __name__ == '__main__':
    main()
