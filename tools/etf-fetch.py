#!/usr/bin/env python3
"""Fetch the daily portfolios of the active ETFs managed by Uni-President (ezmoney.com.tw)
plus closing prices, and keep one JSON file per fund (data/etf-<ticker>.json) for etf-00981a.html.

Holdings come from each fund's PCF (creation/redemption basket) service, which accepts any
past date: querying business day D returns the portfolio as of the close of an earlier business
day (the day before D for the Taiwan funds, usually two days before for the global ones).

Taiwan funds ('tw'): prices come from TWSE (MI_INDEX) and, for OTC stocks, TPEx. On an
ex-dividend day TWSE prints the change as "X 0.00"; the real change is measured from the
ex-dividend reference price (TWT49U).

Global funds ('global'): holdings are priced in their own currency, so every price comes from
the basket itself (amount / shares, the fund's own valuation) and a day's change is measured
against the previous basket. Amounts are converted to NTD: USD at the basket's own USD_EXRATE,
other currencies at the rate implied by the basket (weight x fund NAV / amount), scaled by the
same factor that maps the implied USD rate onto USD_EXRATE (the implied rates run 0.2-0.6 %
high). The fund's own market quote comes from TWSE STOCK_DAY, or TPEx for an OTC-listed fund.

  python3 tools/etf-fetch.py                       # update every fund: add every new trading day
  python3 tools/etf-fetch.py --fund 00403A         # one fund only (repeatable)
  python3 tools/etf-fetch.py --fund 00403A --since 2026-04-28   # backfill from a date (idempotent)
  python3 tools/etf-fetch.py --repair-exdiv        # re-price stored ex-dividend days (Taiwan funds)

Standard library only, so it runs on a bare GitHub Actions runner.
"""
import argparse
import collections
import datetime as dt
import http.cookiejar
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

FUNDS = [
    {'code': '49YTW', 'ticker': '00981A', 'name': '主動統一台股增長', 'short': '台股增長',
     'full': '統一台股增長主動式ETF基金', 'listed': '2025-05-27', 'kind': 'tw'},
    {'code': '63YTW', 'ticker': '00403A', 'name': '主動統一升級50', 'short': '升級50',
     'full': '統一台股升級50主動式ETF基金', 'listed': '2026-04-28', 'kind': 'tw'},
    {'code': '61YTW', 'ticker': '00988A', 'name': '主動統一全球創新', 'short': '全球創新',
     'full': '統一全球創新主動式ETF基金', 'listed': '2025-10-21', 'kind': 'global'},
    {'code': '64YTW', 'ticker': '00411A', 'name': '主動統一前沿科技', 'short': '前沿科技',
     'full': '統一前沿科技主動式ETF基金', 'listed': '2026-08-11', 'kind': 'global', 'market': 'tpex'},
]
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
TZ = dt.timezone(dt.timedelta(hours=8))
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'

jar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
_last_twse = [0.0]


def fetch(url, data=None, headers=None, tries=4):
    h = {'User-Agent': UA, 'Accept': 'application/json, text/plain, */*'}
    h.update(headers or {})
    for i in range(tries):
        if 'twse.com.tw' in url:  # TWSE blocks clients that ask more than a few times in five seconds
            time.sleep(max(0.0, _last_twse[0] + 3 - time.time()))
            _last_twse[0] = time.time()
        try:
            req = urllib.request.Request(url, data=data, headers=h)
            with opener.open(req, timeout=40) as r:
                return r.read().decode('utf-8', 'replace')
        except Exception as e:  # network hiccups and rate limits: back off and retry
            if i == tries - 1:
                raise
            print(f'  retry {url[:60]}… ({e})', file=sys.stderr)
            time.sleep(5 * (i + 1))


def cached(fn):
    """Memoise a quote source, so funds sharing a day share one request."""
    memo = {}

    def wrap(*args):
        if args not in memo:
            memo[args] = fn(*args)
        return memo[args]
    return wrap


def num(s):
    """'1,234.50' -> 1234.5; '--' / '' / 'X' -> None."""
    s = re.sub(r'<[^>]*>', '', str(s)).replace(',', '').strip()
    try:
        return float(s)
    except ValueError:
        return None


def roc(d):
    return f'{d.year - 1911}/{d.month:02d}/{d.day:02d}'


def ms_date(s):
    """'/Date(1791820800000)/' or '2026-10-13T00:00:00' (the service sends either) -> Taiwan date."""
    m = re.match(r'/Date\((-?\d+)\)/', s)
    if m:
        return dt.datetime.fromtimestamp(int(m.group(1)) / 1000, TZ).date()
    return dt.date.fromisoformat(s[:10])


def warm_up():
    # The site answers the first request with a cookie and a redirect to itself.
    fetch('https://www.ezmoney.com.tw/ETF/Transaction/PCF', headers={'Accept': 'text/html'})


def pcf(fund, query_day):
    body = json.dumps({'fundCode': fund['code'], 'date': roc(query_day), 'specificDate': True}).encode()
    raw = fetch('https://www.ezmoney.com.tw/ETF/Transaction/GetPCF', data=body,
                headers={'Content-Type': 'application/json; charset=utf-8',
                         'X-Requested-With': 'XMLHttpRequest',
                         'Referer': 'https://www.ezmoney.com.tw/ETF/Transaction/PCF'})
    d = json.loads(raw)
    assets = {a['AssetCode']: a for a in (d.get('asset') or [])}
    st = (assets.get('ST') or {}).get('Details') or []
    if not st:
        return None
    day = ms_date(st[0]['TranDate'])
    p = {x['PCFCode']: x['Amount'] for x in (d.get('pcf') or [])}
    fut = [[x['DetailCode'].strip(), x['DetailName'].strip(), x['Position'].strip(), int(x['Share']),
            round(x['Amount']), x['NavRate'], (x.get('MTH') or '').strip()]
           for x in ((assets.get('GD') or {}).get('Details') or [])]
    out = {
        'd': day.isoformat(),
        'nav': p.get('P_UNIT'), 'aum': p.get('NAV'), 'units': p.get('OUT_UNIT'),
        'dunits': p.get('DIFF_UNIT'), 'people': p.get('NAV_PEOPLE'),
    }
    if fund['kind'] == 'tw':
        out['h'] = sorted(([x['DetailCode'].strip(), x['DetailName'].strip(), int(x['Share']),
                            round(x['Amount']), x['NavRate']] for x in st), key=lambda r: -r[3])
        out['fut'] = fut
        return out

    # Global fund: amounts are in each holding's own currency.
    aum = p.get('NAV') or 0
    by_cur = collections.defaultdict(lambda: [0.0, 0.0])
    for x in st:
        c = (x.get('MoneyType') or 'NTD').strip()
        by_cur[c][0] += x['NavRate'] / 100 * aum
        by_cur[c][1] += x['Amount']
    implied = {c: v / a for c, (v, a) in by_cur.items() if c != 'NTD' and v > 0 and a > 0}
    usd = next((x.get('USD_EXRATE') for x in st if (x.get('USD_EXRATE') or 1) != 1), None)
    k = usd / implied['USD'] if usd and implied.get('USD') else 1
    fx = {c: round(r * k, 6) for c, r in implied.items()}
    if usd and 'USD' in by_cur:
        fx['USD'] = usd
    hold, cur, px = [], {}, {}
    for x in st:
        code, c = x['DetailCode'].strip(), (x.get('MoneyType') or 'NTD').strip()
        rate = 1 if c == 'NTD' else fx.get(c)
        amt = x['Amount'] * rate if rate else x['NavRate'] / 100 * aum
        hold.append([code, x['DetailName'].strip(), int(x['Share']), round(amt), x['NavRate']])
        if c != 'NTD':
            cur[code] = c
        if x['Share'] > 0:
            px[code] = [round(x['Amount'] / x['Share'], 4), None]
    out['h'] = sorted(hold, key=lambda r: -r[3])
    out['fut'] = fut
    out['cur'], out['fx'], out['px'] = cur, fx, px
    return out


@cached
def twse(day):
    raw = fetch('https://www.twse.com.tw/exchangeReport/MI_INDEX?' + urllib.parse.urlencode(
        {'response': 'json', 'date': day.strftime('%Y%m%d'), 'type': 'ALLBUT0999'}))
    d = json.loads(raw)
    if d.get('stat') != 'OK':
        return None, None, set()
    px, taiex, xs = {}, None, set()
    for t in d.get('tables') or []:
        f = t.get('fields') or []
        if '證券代號' in f and '收盤價' in f:
            ic, ip, isg, idf = f.index('證券代號'), f.index('收盤價'), f.index('漲跌(+/-)'), f.index('漲跌價差')
            for r in t['data']:
                c, diff = num(r[ip]), num(r[idf])
                sign = re.sub(r'<[^>]*>', '', r[isg]).strip()
                if c is None:
                    continue
                if sign == 'X':  # not compared with the previous close (ex-dividend and the like)
                    xs.add(r[ic].strip())
                    diff = None
                elif diff is not None and sign == '-':
                    diff = -diff
                elif sign != '+':
                    diff = 0.0 if diff is not None else None
                px[r[ic].strip()] = [c, diff]
        elif '指數' in f and taiex is None:
            for r in t['data']:
                if r[0].strip() == '發行量加權股價指數':
                    sign = re.sub(r'<[^>]*>', '', r[2]).strip()
                    pts = num(r[3])
                    taiex = [num(r[1]), -pts if sign == '-' else pts]
    return px, taiex, xs


@cached
def month_quotes(ticker, market, year, month):
    """{ISO date: [close, change]} for one listed security over one month (change None on an
    'X' day), from TWSE STOCK_DAY or, for an OTC security, TPEx tradingStock."""
    if market == 'tpex':
        raw = fetch('https://www.tpex.org.tw/www/zh-tw/afterTrading/tradingStock?' + urllib.parse.urlencode(
            {'code': ticker, 'date': f'{year}/{month:02d}/01', 'response': 'json'}))
        time.sleep(1)
        rows, idd, ic, idf = (json.loads(raw).get('tables') or [{}])[0].get('data') or [], 0, 6, 7
    else:
        raw = fetch('https://www.twse.com.tw/exchangeReport/STOCK_DAY?' + urllib.parse.urlencode(
            {'response': 'json', 'date': f'{year}{month:02d}01', 'stockNo': ticker}))
        d = json.loads(raw)
        if d.get('stat') != 'OK':
            return {}
        f = d.get('fields') or []
        rows, idd, ic, idf = d.get('data') or [], f.index('日期'), f.index('收盤價'), f.index('漲跌價差')
    out = {}
    for r in rows:
        m = re.match(r'(\d+)/(\d+)/(\d+)', r[idd].strip())
        c = num(r[ic])
        if not m or c is None:
            continue
        s = re.sub(r'<[^>]*>', '', r[idf]).strip()
        out[dt.date(int(m.group(1)) + 1911, int(m.group(2)), int(m.group(3))).isoformat()] = \
            [c, None if s.startswith('X') else num(s)]
    return out


@cached
def exdiv_refs(start, end):
    """{(ISO date, code): ex-dividend reference price} for TWSE stocks between two dates."""
    raw = fetch('https://www.twse.com.tw/exchangeReport/TWT49U?' + urllib.parse.urlencode(
        {'response': 'json', 'startDate': start.strftime('%Y%m%d'), 'endDate': end.strftime('%Y%m%d')}))
    d = json.loads(raw)
    refs = {}
    if d.get('stat') != 'OK':
        return refs
    f = d.get('fields') or []
    idd, ic, iref = f.index('資料日期'), f.index('股票代號'), f.index('除權息參考價')
    for r in d.get('data') or []:
        m = re.match(r'(\d+)年(\d+)月(\d+)日', r[idd])
        ref = num(r[iref])
        if m and ref:
            day = dt.date(int(m.group(1)) + 1911, int(m.group(2)), int(m.group(3)))
            refs[(day.isoformat(), r[ic].strip())] = ref
    return refs


def from_ref(quote, ref):
    return [quote[0], round(quote[0] - ref, 2)]


@cached
def tpex(day):
    raw = fetch('https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?'
                + urllib.parse.urlencode({'l': 'zh-tw', 'd': roc(day), 'se': 'EW', 'o': 'json'}))
    time.sleep(1)
    d = json.loads(raw)
    px = {}
    for t in d.get('tables') or []:
        for r in t.get('data') or []:
            c, diff = num(r[2]), num(r[3])
            if c is not None:
                px[r[0].strip()] = [c, diff]
    return px


def out_path(fund):
    return os.path.join(DATA, f'etf-{fund["ticker"].lower()}.json')


def load(fund):
    if os.path.exists(out_path(fund)):
        with open(out_path(fund), encoding='utf-8') as f:
            return json.load(f)
    return {'fund': fund, 'days': []}


def save(fund, db):
    db['fund'] = fund
    db['days'].sort(key=lambda x: x['d'])
    db['updated'] = dt.datetime.now(TZ).isoformat(timespec='seconds')
    os.makedirs(DATA, exist_ok=True)
    out = out_path(fund)
    tmp = out + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        f.write('{"fund":' + json.dumps(db['fund'], ensure_ascii=False))
        f.write(',"updated":' + json.dumps(db['updated']))
        f.write(',"days":[\n')
        f.write(',\n'.join(json.dumps(x, ensure_ascii=False, separators=(',', ':')) for x in db['days']))
        f.write('\n]}\n')
    os.replace(tmp, out)


def add_prices_tw(fund, db):
    """Fill 'px' (close, change) for the stocks held that day or the day before, the ETF itself
    ('etf') and the TAIEX ('ix'); a day whose quotes are not out yet is retried next run."""
    days = db['days']
    for i, x in enumerate(days):
        if 'px' in x:
            continue
        day = dt.date.fromisoformat(x['d'])
        codes = {r[0] for r in x['h']} | ({r[0] for r in days[i - 1]['h']} if i else set())
        px, ix, xs = twse(day)
        if px is None:
            print(f'  {x["d"]}: no TWSE quotes yet')
            continue
        px = dict(px)
        if xs & (codes | {fund['ticker']}):
            try:
                refs = exdiv_refs(day, day)
            except Exception as e:  # keep the day unpriced so the next run tries again
                print(f'  {x["d"]}: TWT49U failed ({e})', file=sys.stderr)
                continue
            for c in xs:
                if (x['d'], c) in refs:
                    px[c] = from_ref(px[c], refs[(x['d'], c)])
        if codes - px.keys():
            try:
                px.update({k: v for k, v in tpex(day).items() if k not in px})
            except Exception as e:
                print(f'  {x["d"]}: TPEx failed ({e})', file=sys.stderr)
                continue
        x['px'] = {c: px[c] for c in sorted(codes) if c in px}
        x['etf'] = px.get(fund['ticker'])
        x['ix'] = ix
        print(f'  {x["d"]}: prices for {len(x["px"])}/{len(codes)}')
        save(fund, db)


def foreign(code):
    return ' ' in code.strip()


def split_ratio(s0, s1, p0, p1):
    """k when a holding went from s0 to s1 shares while its price went from p0 to p1 the way a
    k-for-1 split (or a 1-for-k reverse split, k < 1) does; None otherwise."""
    if not (s0 and s1 and p0 and p1):
        return None
    sr, pr = s1 / s0, p0 / p1
    if sr >= 1.5:
        k = round(sr)
    elif sr <= 0.67:
        k = 1 / round(1 / sr)
    else:
        return None
    return k if abs(sr / k - 1) < 0.05 and abs(pr / k - 1) < 0.12 else None


def tw_ref(fund, x, c):
    """TWSE / TPEx reference price (close - change) of a Taiwan stock on day x, or None."""
    q = (x.get('px') or {}).get(c) if fund['kind'] == 'tw' else None
    if q is None or q[1] is None:
        day = dt.date.fromisoformat(x['d'])
        try:
            px, _, xs = twse(day)
            q = (px or {}).get(c) or tpex(day).get(c)
            if q and q[1] is None and c in xs:  # ex-rights day: TWSE prints "X", use TWT49U
                ref = exdiv_refs(day, day).get((x['d'], c))
                q = from_ref(q, ref) if ref else q
        except Exception as e:
            print(f'  {x["d"]}: quote for split of {c} failed ({e})', file=sys.stderr)
            return None
    return q[0] - q[1] if q and q[1] is not None and q[0] - q[1] > 0 else None


def mark_splits(fund, db):
    """Record stock splits per day as 'sp' = {code: k}, so the page does not read the new share
    count as a trade. Foreign splits are whole ratios; a Taiwan split need not be (6669 went
    1 -> 2.98279 on 2026-09-02), so its k is the previous close over the exchange's reference
    price. Recomputed on every run (idempotent); returns True if anything changed."""
    days, changed = db['days'], False
    for i in range(1, len(days)):
        x, y = days[i], days[i - 1]
        s0, s1 = {r[0]: r[2] for r in y['h']}, {r[0]: r[2] for r in x['h']}
        px, px0 = x.get('px') or {}, y.get('px') or {}
        sp = {}
        for c in s0.keys() & s1.keys():
            p0 = (px0.get(c) or [None])[0]
            k = split_ratio(s0[c], s1[c], p0, (px.get(c) or [None])[0])
            if k and not foreign(c):
                old = (x.get('sp') or {}).get(c)
                if old and old != round(old) and abs(old / k - 1) < 0.05:  # already measured; skip the quote request
                    k = old
                else:
                    ref = tw_ref(fund, x, c)
                    if ref and abs(p0 / ref / k - 1) < 0.05:
                        k = round(p0 / ref, 6)
                        sr = s1[c] / s0[c]
                        if abs(sr / k - 1) < 0.001:  # no trade that day: take the exact share ratio
                            k = round(sr, 9)
            if k:
                sp[c] = k
        if sp != x.get('sp', {}):
            if sp:
                x['sp'] = sp
            else:
                x.pop('sp', None)
            changed = True
    return changed


def link_global(db):
    """Give each global-fund day the change of every holding against the previous basket, and
    carry the previous price, currency and rate for stocks sold out that day. Returns True if
    anything changed (it is recomputed from the baskets on every run, so it is idempotent)."""
    days, changed = db['days'], False
    for i in range(1, len(days)):
        x, y = days[i], days[i - 1]
        held, held0 = {r[0] for r in x['h']}, {r[0] for r in y['h']}
        px, px0 = x.setdefault('px', {}), y.get('px') or {}
        for c in held0:
            p0 = px0.get(c)
            if not p0:
                continue
            if c in held and c in px:
                k = (x.get('sp') or {}).get(c, 1)  # after a k-for-1 split, compare with p0 / k
                new = [px[c][0], round(px[c][0] - p0[0] / k, 4)]
            elif c not in held:
                new = [p0[0], None]
                cur = (y.get('cur') or {}).get(c)
                if cur:
                    x.setdefault('cur', {})[c] = cur
                    if cur not in x.setdefault('fx', {}) and cur in (y.get('fx') or {}):
                        x['fx'][cur] = y['fx'][cur]
            else:
                continue
            if px.get(c) != new:
                px[c] = new
                changed = True
    return changed


def add_quotes_global(fund, db):
    """The fund's own TWSE close for each day that has none yet (one request per month)."""
    changed = False
    for x in db['days']:
        if x.get('etf') or not x.get('nav'):  # pre-listing baskets (NAV 0) have no quote
            continue
        day = dt.date.fromisoformat(x['d'])
        try:
            q = month_quotes(fund['ticker'], fund.get('market', 'twse'), day.year, day.month).get(x['d'])
        except Exception as e:
            print(f'  {x["d"]}: market quotes failed ({e})', file=sys.stderr)
            continue
        if q:
            x['etf'] = q
            changed = True
    return changed


def repair_exdiv(fund, db):
    """Re-price every stored ex-dividend day from its reference price (one TWT49U request)."""
    days = [x for x in db['days'] if 'px' in x]
    if not days:
        return
    refs = exdiv_refs(dt.date.fromisoformat(days[0]['d']), dt.date.fromisoformat(days[-1]['d']))
    fixed = 0
    for x in days:
        for c, q in list(x['px'].items()):
            if (x['d'], c) in refs and q[1] != from_ref(q, refs[(x['d'], c)])[1]:
                x['px'][c] = from_ref(q, refs[(x['d'], c)])
                fixed += 1
        if x.get('etf') and (x['d'], fund['ticker']) in refs:
            new = from_ref(x['etf'], refs[(x['d'], fund['ticker'])])
            if new != x['etf']:
                x['etf'] = new
                fixed += 1
    print(f'{fund["ticker"]}: {len(refs)} ex-dividend records; {fixed} stored quote(s) re-priced')
    if fixed:
        save(fund, db)


def update(fund, since, prices):
    db = load(fund)
    have = {x['d'] for x in db['days']}
    today = dt.datetime.now(TZ).date()
    if since:
        start = dt.date.fromisoformat(since)
    elif db['days']:
        start = dt.date.fromisoformat(db['days'][-1]['d']) + dt.timedelta(days=1)
    else:
        start = dt.date.fromisoformat(fund['listed'])

    # Query each weekday up to a few days ahead: after ~16:30 the fund publishes the next
    # business day's basket, which carries the latest closing portfolio.
    q, added = start, 0
    while q <= today + dt.timedelta(days=4):
        if q.weekday() < 5:
            try:
                x = pcf(fund, q)
            except Exception as e:
                print(f'  {q}: PCF failed ({e})', file=sys.stderr)
                x = None
            if x and x['d'] not in have:
                db['days'].append(x)
                have.add(x['d'])
                added += 1
                print(f'+ {fund["ticker"]} {x["d"]}  {len(x["h"])} stocks  NAV {x["nav"]}')
                if added % 20 == 0:
                    save(fund, db)
            time.sleep(0.4)
        q += dt.timedelta(days=1)
    db['days'].sort(key=lambda x: x['d'])
    dirty = added > 0
    if fund['kind'] == 'global':
        dirty = mark_splits(fund, db) or dirty
        dirty = link_global(db) or dirty
        if prices:
            dirty = add_quotes_global(fund, db) or dirty
    if dirty:  # leave the file untouched when nothing is new, so the daily job commits nothing
        save(fund, db)
    print(f'{fund["ticker"]}: {added} new day(s); {len(db["days"])} in file')
    if prices and fund['kind'] == 'tw':
        add_prices_tw(fund, db)
        if mark_splits(fund, db):
            save(fund, db)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--fund', action='append', choices=[f['ticker'] for f in FUNDS],
                    help='only this fund (repeatable; default: every fund)')
    ap.add_argument('--since', help='backfill from this date (YYYY-MM-DD)')
    ap.add_argument('--no-prices', action='store_true')
    ap.add_argument('--repair-exdiv', action='store_true')
    a = ap.parse_args()

    funds = [f for f in FUNDS if not a.fund or f['ticker'] in a.fund]
    if a.repair_exdiv:
        for f in funds:
            if f['kind'] == 'tw':
                repair_exdiv(f, load(f))
        return
    warm_up()
    failed = []
    for f in funds:
        try:
            update(f, a.since, not a.no_prices)
        except Exception as e:  # one fund's failure must not keep the others from being saved
            failed.append(f['ticker'])
            print(f'::warning::{f["ticker"]} failed: {e}')
    if failed and len(failed) == len(funds):
        sys.exit(1)


if __name__ == '__main__':
    main()
