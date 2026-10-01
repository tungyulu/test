#!/usr/bin/env python3
"""Re-embed the inlined font subsets of a page after its text changes.

Pages here ship offline-first: their faces are subsets that contain only the glyphs
the page uses, inlined as WOFF2 data URIs. Any edit that introduces a new character
(a new shop name, a new place) must re-run this, or that character falls back to
the system font.

trip.html (the station edition) carries the station faces: 'Eki TC' = Noto Sans TC
400 / 700 (every character on the page) and 900 (headings and station names only),
'Eki JP' = Noto Sans JP 400 / 700 for the Japanese kanji forms Noto Sans TC lacks
(営, 峠, 焼 …), and 'Eki Latin' = Hind 600 / 700 (Latin). Every other page carries 'Huninn Shiori'
(jf open 粉圓).

    pip install fonttools brotli
    python3 tools/trip-font.py            # re-subset trip.html from its current text
    python3 tools/trip-font.py --check    # only report characters missing from the subsets
    python3 tools/trip-font.py --page trip-v2.html  # the booklet edition (Huninn)
    python3 tools/trip-font.py --page index.html   # same, for the hub (any page with the 'Huninn Shiori' face)
    python3 tools/trip-font.py --page blackjack-game.html   # the blackjack table (counts every character in its script)
    python3 tools/trip-font.py --page blackjack.html        # the strategy trainer (same)

The full fonts (SIL OFL 1.1) are fetched from Google Fonts on first run and cached in
~/.cache/trip-font/. Nothing else in the page is touched.
"""
import base64, html, io, re, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / (sys.argv[sys.argv.index('--page') + 1] if '--page' in sys.argv else 'trip.html')
CACHE = Path.home() / '.cache' / 'trip-font' / 'Huninn-Regular.ttf'
CSS_URL = 'https://fonts.googleapis.com/css2?family=Huninn&display=swap'
FACE_RE = re.compile(r"(@font-face\{font-family:'Huninn Shiori';src:url\(data:font/woff2;base64,)([A-Za-z0-9+/=]+)(\))")
# Glyphs the page's script writes at runtime (cover stamp states, buttons) that may not be in the markup yet.
RUNTIME = '0123456789:/.-–—()（）· ／、，。！？「」天還有第今日目旅程完成平安回家出發結束的頁把行前準備勾選全部清掉'


def page_chars(src: str) -> set:
    body = re.sub(r'<style>.*?</style>', ' ', src, flags=re.S)
    body = re.sub(r'<svg class="ic.*?</svg>', ' ', body, flags=re.S)
    script = ''.join(re.findall(r'<script>(.*?)</script>', body, flags=re.S))
    body = re.sub(r'<script>.*?</script>', ' ', body, flags=re.S)
    text = html.unescape(re.sub(r'<[^>]+>', ' ', body))
    attrs = ' '.join(re.findall(r'(?:aria-label|title|data-ink)="([^"]*)"', src))
    # trip.html's script writes visible text (cover stamp, buttons); the hub's script writes none;
    # the blackjack table's and trainer's scripts write nearly all of their text, so every character in them counts
    writes_text = PAGE.name in ('trip.html', 'trip-v2.html')
    strings = ' '.join(a or b for a, b in re.findall(r"'([^'\n]*)'|`([^`\n]*)`", script)) if writes_text else ''
    if PAGE.name in ('blackjack-game.html', 'blackjack.html') or EKI_RE.search(src):
        strings = script
    css = ' '.join(re.findall(r'content:"([^"]*)"', src))
    text += css
    return {c for c in text + attrs + strings + (RUNTIME if writes_text else '') if not c.isspace()}


def font_path(cache: Path = CACHE, css_url: str = CSS_URL) -> Path:
    if cache.exists():
        return cache
    cache.parent.mkdir(parents=True, exist_ok=True)
    css = urllib.request.urlopen(urllib.request.Request(css_url, headers={'User-Agent': 'curl/8'})).read().decode()
    url = re.search(r'url\((https://[^)]+\.ttf)\)', css).group(1)
    cache.write_bytes(urllib.request.urlopen(url).read())
    return cache


# The station faces of trip.html: (family, weight, cached file, Google Fonts family spec, which characters)
EKI = [('Eki TC', 400, 'NotoSansTC-400.ttf', 'Noto+Sans+TC:wght@400', 'all'),
       ('Eki TC', 700, 'NotoSansTC-700.ttf', 'Noto+Sans+TC:wght@700', 'all'),
       ('Eki TC', 900, 'NotoSansTC-900.ttf', 'Noto+Sans+TC:wght@900', 'display'),
       ('Eki JP', 400, 'NotoSansJP-400.ttf', 'Noto+Sans+JP:wght@400', 'jp'),
       ('Eki JP', 700, 'NotoSansJP-700.ttf', 'Noto+Sans+JP:wght@700', 'jp'),
       ('Eki Latin', 600, 'Hind-600.ttf', 'Hind:wght@600', 'latin'),
       ('Eki Latin', 700, 'Hind-700.ttf', 'Hind:wght@700', 'latin')]
EKI_RE = re.compile(r"@font-face\{font-family:'Eki TC'")


def eki_face_re(fam: str, w: int):
    return re.compile(r"(@font-face\{font-family:'" + fam + r"';font-weight:" + str(w) +
                      r";font-display:swap;src:url\(data:font/woff2;base64,)([A-Za-z0-9+/=]*)(\))")


def display_chars(src: str) -> set:
    # weight 900 sets headings, station names and the page title only
    body = re.sub(r'<(style|script)>.*?</\1>', ' ', src, flags=re.S)
    parts = re.findall(r'<(h1|h2|h3)\b[^>]*>(.*?)</\1>', body, flags=re.S)
    parts = [p[1] for p in parts] + re.findall(r'<span class="eki-k">(.*?)</span>', body)
    text = html.unescape(re.sub(r'<[^>]+>', ' ', ' '.join(parts))) + '注意'
    return {c for c in text if not c.isspace()}


def eki(src: str) -> None:
    from fontTools import subset
    from fontTools.ttLib import TTFont
    allc = page_chars(src)
    tc = TTFont(font_path(CACHE.parent / 'NotoSansTC-400.ttf', 'https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400')).getBestCmap()
    sets = {'jp': {c for c in allc if ord(c) not in tc and ord(c) > 0x2e7f},'all': allc, 'display': display_chars(src) | set('0123456789'),
            'latin': {c for c in allc if ord(c) < 0x2000} | {chr(c) for c in range(0x20, 0x7f)} | set('·–—°¥×')}
    out, report, missing_all = src, [], []
    for fam, w, file, spec, which in EKI:
        rx = eki_face_re(fam, w)
        m = rx.search(out)
        if not m:
            continue
        want = sets[which]
        have = set(chr(u) for u in TTFont(io.BytesIO(base64.b64decode(m.group(2)))).getBestCmap()) if m.group(2) else set()
        missing = sorted(c for c in want - have if ord(c) > 0x20)
        if '--check' in sys.argv:
            if which in ('all', 'jp'):
                missing_all += [c for c in missing if c not in missing_all and (which == 'jp' or ord(c) in tc)]
            continue
        full = TTFont(font_path(CACHE.parent / file, 'https://fonts.googleapis.com/css2?family=' + spec))
        cmap = full.getBestCmap()
        opts = subset.Options()
        opts.flavor = 'woff2'
        opts.layout_features = ['palt', 'kern', 'liga', 'locl', 'vert']
        opts.hinting = False
        opts.desubroutinize = True
        sub = subset.Subsetter(opts)
        sub.populate(text=''.join(c for c in want if ord(c) in cmap))
        sub.subset(full)
        buf = io.BytesIO()
        full.flavor = 'woff2'
        full.save(buf)
        out = out[:m.start(2)] + base64.b64encode(buf.getvalue()).decode() + out[m.end(2):]
        report.append(f"{fam} {w}: {len(buf.getvalue()) // 1024} KB, {len(want)} chars")
    if '--check' in sys.argv:
        print('missing from subsets:', ''.join(missing_all) or '(none)')
        sys.exit(1 if missing_all else 0)
    PAGE.write_text(out, encoding='utf-8')
    print(f'{PAGE.name}: ' + '; '.join(report))


def main() -> None:
    from fontTools import subset
    from fontTools.ttLib import TTFont

    src = PAGE.read_text(encoding='utf-8')
    if EKI_RE.search(src):
        return eki(src)
    m = FACE_RE.search(src)
    if not m:
        sys.exit(f"{PAGE.name} has no inlined 'Huninn Shiori' @font-face — nothing to update")
    want = page_chars(src)
    have = set(chr(u) for u in TTFont(io.BytesIO(base64.b64decode(m.group(2)))).getBestCmap())
    missing = sorted(c for c in want - have if ord(c) > 0x20)
    if '--check' in sys.argv:
        print('missing from subset:', ''.join(missing) or '(none)')
        sys.exit(1 if missing else 0)

    full = TTFont(font_path())
    cmap = full.getBestCmap()
    unsupported = sorted(c for c in want if ord(c) not in cmap and ord(c) > 0x7f)
    opts = subset.Options()
    opts.flavor = 'woff2'
    opts.layout_features = ['*']
    opts.hinting = False
    opts.desubroutinize = True
    sub = subset.Subsetter(opts)
    sub.populate(text=''.join(want))
    sub.subset(full)
    buf = io.BytesIO()
    full.flavor = 'woff2'
    full.save(buf)
    b64 = base64.b64encode(buf.getvalue()).decode()
    PAGE.write_text(src[:m.start(2)] + b64 + src[m.end(2):], encoding='utf-8')
    print(f'{PAGE.name}: font subset {len(buf.getvalue()) // 1024} KB, {len(want)} chars'
          f' ({len(missing)} newly added{", not in Huninn: " + "".join(unsupported) if unsupported else ""})')


if __name__ == '__main__':
    main()
