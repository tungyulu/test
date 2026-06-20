---
name: update-betting-slip
description: >-
  Use when the user provides a World Cup betting slip / 運彩投注單 photo or asks to
  record or update a betting ticket — phrases like "更新投注單", "新增一張注單", "這張票/票根",
  "幫我加進去", or sending a sports-lottery slip image. Reads the slip photo, extracts
  the legs / odds / stakes / parlay combinations, and adds (or updates) the matching
  ticket inside betting.html's seedData(), keeping per-combo rounding and totals
  consistent. Also use when the user reports results ("X 過了、Y 沒過") to flip the
  result fields and recompute.
---

# 更新運彩投注單到 betting.html

This project tracks World Cup sports-lottery (運彩) bets in `betting.html`, a
single-file web app. When the user sends a **betting slip photo** or asks to
**update a ticket**, follow this skill.

## Where the data lives

- `betting.html` → `seedData()` returns the canonical array of `tickets[]`. **This
  is the source you edit.**
- The running app reads `localStorage` (key `wc-betting-tracker-v1`) first and only
  falls back to `seedData()` when storage is empty. So after you edit `seedData()`,
  the user sees the change on a fresh browser or after clicking **「重設為範例資料」**.
  Mention this if they ask why their browser still shows old data.

## Ticket data model

```js
{
  id: 't5',                       // unique, e.g. 't' + next number
  date: '2026-06-20',             // YYYY-MM-DD from the slip
  label: '今天 4 場複式（票根）',   // short note
  selections: [                   // one per leg; keys are A, B, C, … in order
    { key:'A', match:'南非 @ 捷克', pick:'總分大小 小2.5', odds:1.78, result:'pending' },
    // result: 'pending' | 'win' | 'lose' | 'void'
  ],
  groups: [                       // one per 關數 (parlay size) bought
    { size:1, stakePer:10 },      // size = legs per combo; stakePer = 每注金額
    { size:3, stakePer:10 },
    { size:4, stakePer:20, manualOdds:1.72 }, // manualOdds: optional, see below
  ],
}
```

## How to read a slip photo

Extract from the image:
1. **Date** of the bets.
2. **Each leg**: the match (隊伍/對戰), the pick (玩法 — e.g. 獨贏 / 不讓分 / 讓分 / 和局 /
   總分大小), and the **odds (賠率)**.
3. **Combination groups**: which 關數 were bought (串 1/2/3/4 關), the **組合數**
   (count) and the **每注金額** for each.
4. **Total stake** to cross-check.

Map each leg to a `selection` (assign keys A, B, C… in slip order) and each 關數 row
to a `group` (`size` = number of legs, `stakePer` = per-combo stake).

## Rules (must follow)

- **Per-combo payout rounds to the nearest integer**: return = `Math.round(stakePer ×
  Π odds)`, summed across combos. This matches the printed slip. (Already implemented
  in `computeTicket`; just don't reintroduce un-rounded math.)
- **`void` (賠率視為 1)** is ONLY for 讓分平退 (handicap push). A 獨贏 that ends in a
  draw is `lose`, never void.
- **`manualOdds`** on a group overrides the odds product — use it when individual leg
  odds are unknown but the slip prints a single total odds (e.g. a pure N-串-1 where
  only 總賠率 is given). For full-cover slips with per-leg odds, leave it out.
- A combo wins only if **all** its legs are `win` (or `void`); any `lose` → that combo
  pays 0; any `pending` → that combo is undecided.

## Steps

1. **Read the photo** with the Read tool.
2. **Decide add vs update**:
   - New slip → append a new ticket object to the array in `seedData()`.
   - User reporting results for an existing ticket → edit that ticket's
     `selections[].result` fields only.
3. **Edit** `betting.html` (`seedData()`), keeping keys A,B,C… and the schema above.
4. **Cross-check the total stake**: Σ over groups of `組合數 × stakePer` must equal the
   slip's total. C(n,k) for n legs gives the combo count per size.
5. **Verify** the payout math with a quick Node check before committing — reuse the
   engine logic (`combinations`, `comboStatus`, `comboOdds`, `Math.round`).
6. **Commit and push** to the development branch
   `claude/world-cup-betting-tracker-hvl24o` (per project branch rules; create it if
   needed, never push elsewhere without explicit permission). Do NOT open a PR unless
   asked.

## Verification snippet

```bash
node -e '
function combinations(a,k){const r=[];(function p(s,c){if(c.length===k){r.push(c.slice());return;}for(let i=s;i<a.length;i++){c.push(a[i]);p(i+1,c);c.pop();}})(0,[]);return r;}
function status(s){if(s.some(x=>x.result==="lose"))return"lose";if(s.some(x=>x.result==="pending"))return"pending";return"win";}
function odds(s){return s.reduce((p,x)=>p*(x.result==="void"?1:(+x.odds||0)),1);}
function compute(t){let staked=0,ret=0,pot=0;for(const g of t.groups){for(const c of combinations(t.selections,g.size)){const st=status(c);const o=g.manualOdds!=null?+g.manualOdds:odds(c);const r=Math.round(g.stakePer*o);staked+=g.stakePer;pot+=r;if(st==="win")ret+=r;}}return{staked,returned:ret,potential:pot,profit:ret-staked};}
// paste the ticket object as `t` and console.log(compute(t))
'
```

Confirm `staked` matches the slip total and report the settled profit (or max
potential if still pending) back to the user.
