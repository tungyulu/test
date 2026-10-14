#!/usr/bin/env python3
"""Fetch the daily portfolio of an active ETF managed by Uni-President (ezmoney.com.tw)
plus that day's closing prices, and keep them in one JSON file for etf-00981a.html.

Holdings come from the fund's PCF (creation/redemption basket) service, which accepts any
past date: querying business day D returns the portfolio as of the close of the business
day before D. Prices come from TWSE (MI_INDEX) and, for OTC stocks, TPEx. On an ex-dividend day TWSE prints
the change as "X 0.00"; the real change is measured from the ex-dividend reference price (TWT49U).

  python3 tools/etf-fetch.py                 # update: add every new trading day
  python3 tools/etf-fetch.py --since 2025-05-15   # backfill from a date (idempotent)
  python3 tools/etf-fetch.py --repair-exdiv       # re-price stored ex-dividend days

Standard library only, so it runs on a bare GitHub Actions runner.
"""
import argparse
import datetime as dt
import http.cookiejar
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

FUND = {
    'code': '49YTW',
    'ticker': '00981A',
    'name': '主動統一台股增長',
    'full': '統一台股增長主動式ETF基金',
    'listed': '2025-05-27',
}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'etf-00981a.json')
TZ = dt.timezone(dt.timedelta(hours=8))
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'

jar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))


def fetch(url, data=None, headers=None, tries=4):
    h = {'User-Agent': UA, 'Accept': 'application/json, text/plain, */*'}
    h.update(headers or {})
    for i in range(tries):
        try:
            req = urllib.request.Request(url, data=data, headers=h)
            with opener.open(req, timeout=40) as r:
                return r.read().decode('utf-8', 'replace')
        except Exception as e:  # network hiccups and rate limits: back off and retry
            if i == tries - 1:
                raise
            print(f'  retry {url[:60]}… ({e})', file=sys.stderr)
            time.sleep(5 * (i + 1))


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
    fetch(f'https://www.ezmoney.com.tw/ETF/Transaction/PCF', headers={'Accept': 'text/html'})


def pcf(query_day):
    body = json.dumps({'fundCode': FUND['code'], 'date': roc(query_day), 'specificDate': True}).encode()
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
    hold = sorted(([x['DetailCode'].strip(), x['DetailName'].strip(), int(x['Share']),
                    round(x['Amount']), x['NavRate']] for x in st), key=lambda r: -r[3])
    fut = [[x['DetailCode'].strip(), x['DetailName'].strip(), x['Position'].strip(), int(x['Share']),
            round(x['Amount']), x['NavRate'], (x.get('MTH') or '').strip()]
           for x in ((assets.get('GD') or {}).get('Details') or [])]
    return {
        'd': day.isoformat(),
        'nav': p.get('P_UNIT'), 'aum': p.get('NAV'), 'units': p.get('OUT_UNIT'),
        'dunits': p.get('DIFF_UNIT'), 'people': p.get('NAV_PEOPLE'),
        'h': hold, 'fut': fut,
    }


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


def tpex(day):
    raw = fetch('https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?'
               + urllib.parse.urlencode({'l': 'zh-tw', 'd': roc(day), 'se': 'EW', 'o': 'json'}))
    d = json.loads(raw)
    px = {}
    for t in d.get('tables') or []:
        for r in t.get('data') or []:
            c, diff = num(r[2]), num(r[3])
            if c is not None:
                px[r[0].strip()] = [c, diff]
    return px


def load():
    if os.path.exists(OUT):
        with open(OUT, encoding='utf-8') as f:
            return json.load(f)
    return {'fund': FUND, 'days': []}


def save(db):
    db['fund'] = FUND
    db['days'].sort(key=lambda x: x['d'])
    db['updated'] = dt.datetime.now(TZ).isoformat(timespec='seconds')
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    tmp = OUT + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        f.write('{"fund":' + json.dumps(db['fund'], ensure_ascii=False))
        f.write(',"updated":' + json.dumps(db['updated']))
        f.write(',"days":[\n')
        f.write(',\n'.join(json.dumps(x, ensure_ascii=False, separators=(',', ':')) for x in db['days']))
        f.write('\n]}\n')
    os.replace(tmp, OUT)


def add_prices(db):
    """Fill 'px' (close, change) for the stocks held that day or the day before, the ETF itself
    ('etf') and the TAIEX ('ix'); a day whose quotes are not out yet is retried next run."""
    days = db['days']
    for i, x in enumerate(days):
        if 'px' in x:
            continue
        day = dt.date.fromisoformat(x['d'])
        codes = {r[0] for r in x['h']} | ({r[0] for r in days[i - 1]['h']} if i else set())
        px, ix, xs = twse(day)
        time.sleep(3)  # TWSE blocks clients that ask more than a few times in five seconds
        if px is None:
            print(f'  {x["d"]}: no TWSE quotes yet')
            continue
        if xs & (codes | {FUND['ticker']}):
            try:
                refs = exdiv_refs(day, day)
            except Exception as e:  # keep the day unpriced so the next run tries again
                print(f'  {x["d"]}: TWT49U failed ({e})', file=sys.stderr)
                continue
            time.sleep(3)
            for c in xs:
                if (x['d'], c) in refs:
                    px[c] = from_ref(px[c], refs[(x['d'], c)])
        if codes - px.keys():
            try:
                px.update({k: v for k, v in tpex(day).items() if k not in px})
            except Exception as e:
                print(f'  {x["d"]}: TPEx failed ({e})', file=sys.stderr)
                continue
            time.sleep(1)
        x['px'] = {c: px[c] for c in sorted(codes) if c in px}
        x['etf'] = px.get(FUND['ticker'])
        x['ix'] = ix
        print(f'  {x["d"]}: prices for {len(x["px"])}/{len(codes)}')
        save(db)


def repair_exdiv(db):
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
        if x.get('etf') and (x['d'], FUND['ticker']) in refs:
            new = from_ref(x['etf'], refs[(x['d'], FUND['ticker'])])
            if new != x['etf']:
                x['etf'] = new
                fixed += 1
    print(f'{len(refs)} ex-dividend records; {fixed} stored quote(s) re-priced')
    if fixed:
        save(db)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--since', help='backfill from this date (YYYY-MM-DD)')
    ap.add_argument('--no-prices', action='store_true')
    ap.add_argument('--repair-exdiv', action='store_true')
    a = ap.parse_args()

    db = load()
    if a.repair_exdiv:
        repair_exdiv(db)
        return
    have = {x['d'] for x in db['days']}
    today = dt.datetime.now(TZ).date()
    if a.since:
        start = dt.date.fromisoformat(a.since)
    elif db['days']:
        start = dt.date.fromisoformat(db['days'][-1]['d']) + dt.timedelta(days=1)
    else:
        start = dt.date.fromisoformat(FUND['listed'])

    warm_up()
    # Query each weekday up to a few days ahead: after ~16:30 the fund publishes the next
    # business day's basket, which carries today's closing portfolio.
    q, added = start, 0
    while q <= today + dt.timedelta(days=4):
        if q.weekday() < 5:
            try:
                x = pcf(q)
            except Exception as e:
                print(f'  {q}: PCF failed ({e})', file=sys.stderr)
                x = None
            if x and x['d'] not in have:
                db['days'].append(x)
                have.add(x['d'])
                added += 1
                print(f'+ {x["d"]}  {len(x["h"])} stocks  NAV {x["nav"]}')
                if added % 20 == 0:
                    save(db)
            time.sleep(0.4)
        q += dt.timedelta(days=1)
    if added:  # leave the file untouched when nothing is new, so the daily job commits nothing
        save(db)
    print(f'{added} new day(s); {len(db["days"])} in file')
    if not a.no_prices:
        add_prices(db)


if __name__ == '__main__':
    main()
