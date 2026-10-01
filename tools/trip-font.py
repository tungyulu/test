#!/usr/bin/env python3
"""Re-embed the Huninn (jf open 粉圓) subset in trip.html (or index.html) after its text changes.

trip.html ships offline-first: its display/body face is a subset of Huninn that
contains only the glyphs the page uses, inlined as a WOFF2 data URI. Any edit that
introduces a new character (a new shop name, a new place) must re-run this, or that
character falls back to the system font.

    pip install fonttools brotli
    python3 tools/trip-font.py            # re-subset from trip.html's current text
    python3 tools/trip-font.py --check    # only report characters missing from the subset
    python3 tools/trip-font.py --page index.html   # same, for the hub (any page with the 'Huninn Shiori' face)
    python3 tools/trip-font.py --page blackjack-game.html   # the blackjack table (counts every character in its script)

The full font (SIL OFL 1.1) is fetched from Google Fonts on first run and cached in
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
    # the blackjack table's script writes nearly all of its text, so every character in it counts
    writes_text = PAGE.name == 'trip.html'
    strings = ' '.join(a or b for a, b in re.findall(r"'([^'\n]*)'|`([^`\n]*)`", script)) if writes_text else ''
    if PAGE.name == 'blackjack-game.html':
        strings = script
    return {c for c in text + attrs + strings + (RUNTIME if writes_text else '') if not c.isspace()}


def font_path() -> Path:
    if CACHE.exists():
        return CACHE
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    css = urllib.request.urlopen(urllib.request.Request(CSS_URL, headers={'User-Agent': 'curl/8'})).read().decode()
    url = re.search(r'url\((https://[^)]+\.ttf)\)', css).group(1)
    CACHE.write_bytes(urllib.request.urlopen(url).read())
    return CACHE


def main() -> None:
    from fontTools import subset
    from fontTools.ttLib import TTFont

    src = PAGE.read_text(encoding='utf-8')
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
