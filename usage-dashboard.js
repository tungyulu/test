#!/usr/bin/env node
/**
 * usage-dashboard.js — 終端機即時 /usage 儀表板(增強版)
 *
 * 顯示 Claude Code `/usage` 的方案額度,並加上:
 *   • Reset 倒數 + 標出「目前最緊」的限制
 *   • 預估撞限時間(依 % 成長速率推算)
 *   • 今日花費 / 燃燒速率(接 ccusage,best-effort)
 *   • 各模型週用量 + severity 標籤
 *
 * 用法:
 *   node usage-dashboard.js            # 預設每 1 分鐘刷新
 *   node usage-dashboard.js 5          # 每 5 分鐘刷新
 *   node usage-dashboard.js --interval 2
 *   node usage-dashboard.js --once     # 只印一次就結束(適合排程/cron)
 *
 * 資料來源:GET https://api.anthropic.com/api/oauth/usage
 *   憑證讀自 ~/.claude/.credentials.json(即 /usage 用的同一份 OAuth token)。
 *   每次刷新都重讀憑證檔,以搭配 Claude Code 的 token 自動更新。
 */

'use strict';
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { execFileSync } = require('node:child_process');

// ---------- 解析參數 ----------
const argv = process.argv.slice(2);
let intervalMin = 1;
let once = false;
let selftest = false;
for (let i = 0; i < argv.length; i++) {
  const a = argv[i];
  if (a === '--once') once = true;
  else if (a === '--selftest') { selftest = true; once = true; }
  else if (a === '--interval') intervalMin = Number(argv[++i]) || intervalMin;
  else if (/^\d+(\.\d+)?$/.test(a)) intervalMin = Number(a);
}
const intervalMs = Math.max(10, intervalMin * 60) * 1000; // 最短 10 秒防呆

// ---------- 顏色 ----------
const C = {
  reset: '\x1b[0m', dim: '\x1b[2m', bold: '\x1b[1m',
  blue: '\x1b[38;5;39m', gray: '\x1b[38;5;240m', grayText: '\x1b[90m',
  green: '\x1b[38;5;42m', yellow: '\x1b[38;5;214m', red: '\x1b[38;5;203m',
  cyan: '\x1b[36m', white: '\x1b[97m',
};

// ---------- 顯示寬度(ANSI 0 寬,全形/emoji 2 寬) ----------
const ANSI = /\x1b\[[0-9;]*m/g;
function displayWidth(s) {
  const plain = String(s).replace(ANSI, '');
  let w = 0;
  for (const ch of plain) {
    const cp = ch.codePointAt(0);
    const wide =
      (cp >= 0x1100 && cp <= 0x115f) || (cp >= 0x2e80 && cp <= 0xa4cf) ||
      (cp >= 0xac00 && cp <= 0xd7a3) || (cp >= 0xf900 && cp <= 0xfaff) ||
      (cp >= 0xfe30 && cp <= 0xfe4f) || (cp >= 0xff00 && cp <= 0xff60) ||
      (cp >= 0xffe0 && cp <= 0xffe6) || (cp >= 0x1f300 && cp <= 0x1faff) ||
      (cp >= 0x2600 && cp <= 0x27bf);
    w += wide ? 2 : 1;
  }
  return w;
}
const pad = (s, w) => String(s) + ' '.repeat(Math.max(0, w - displayWidth(s)));
// 右對齊:左內容 + 右內容,中間補滿到寬度 w
function padBetween(left, right, w) {
  const gap = Math.max(1, w - displayWidth(left) - displayWidth(right));
  return left + ' '.repeat(gap) + right;
}

// ---------- 時間格式 ----------
const TZ = Intl.DateTimeFormat().resolvedOptions().timeZone || 'local';
function lowerAmPm(s) { return s.replace(/\s?([AP])M/i, (_, g) => g.toLowerCase() + 'm'); }
function fmtClock(iso) {
  const d = new Date(iso);
  const now = new Date();
  const timeOpts = { hour: 'numeric', minute: '2-digit', hour12: true };
  const sameDay = d.toDateString() === now.toDateString();
  return sameDay
    ? lowerAmPm(d.toLocaleTimeString('en-US', timeOpts))
    : lowerAmPm(d.toLocaleString('en-US', { month: 'short', day: 'numeric', ...timeOpts }));
}
function fmtDuration(ms) {
  if (ms < 0) ms = 0;
  const totalMin = Math.floor(ms / 60000);
  const d = Math.floor(totalMin / 1440);
  const h = Math.floor((totalMin % 1440) / 60);
  const m = totalMin % 60;
  const s = Math.floor(ms / 1000) % 60;
  if (d > 0) return `${d}d ${h}h`;
  if (h > 0) return `${h}h ${m}m`;
  if (m > 0) return `${m}m`;
  return `${s}s`;
}

// ---------- 抓 /usage 資料 ----------
const CRED = path.join(os.homedir(), '.claude', '.credentials.json');
let lastData = null;   // 解析後的 limits 陣列
let lastCost = null;   // ccusage 花費資訊
let lastFetch = 0;
let lastError = null;
let lastOk = 0;

// 預估撞限:記錄每條 limit 的 (時間, %) 樣本
const history = new Map(); // kind -> [{t, p}]
const HIST_MAX = 60;

function severityColor(percent, severity) {
  if (severity === 'critical' || percent >= 95) return C.red;
  if (severity === 'warning' || percent >= 80) return C.yellow;
  return C.blue;
}
function severityTag(sev) {
  if (sev === 'critical') return `${C.red}⛔ critical${C.reset}`;
  if (sev === 'warning') return `${C.yellow}⚠ warning${C.reset}`;
  return '';
}

// 依 kind 的歷史樣本推估撞到 100% 的時間;回 fmtDuration 字串或 null
function projectETA(kind, currentPercent) {
  const arr = history.get(kind);
  if (!arr || arr.length < 2) return null;
  const first = arr[0], last = arr[arr.length - 1];
  const dt = last.t - first.t;
  if (dt < 30000) return null;              // 樣本間隔太短,不可靠
  const rate = (last.p - first.p) / dt;     // %/ms
  if (rate <= 0) return null;               // 沒在成長(或剛重置)
  const eta = (100 - currentPercent) / rate;
  if (!isFinite(eta) || eta <= 0) return null;
  return fmtDuration(eta);
}

async function fetchData() {
  try {
    const cred = JSON.parse(fs.readFileSync(CRED, 'utf8'));
    const oauth = cred.claudeAiOauth || {};
    const tok = oauth.accessToken;
    if (!tok) throw new Error('找不到 accessToken(請先在 Claude Code 登入)');
    if (oauth.expiresAt && oauth.expiresAt < Date.now()) {
      throw new Error('Token 已過期,請在 Claude Code 內用一次(會自動刷新)');
    }
    const res = await fetch('https://api.anthropic.com/api/oauth/usage', {
      headers: {
        Authorization: 'Bearer ' + tok,
        Accept: 'application/json',
        'Content-Type': 'application/json',
        'anthropic-beta': 'oauth-2025-04-20',
      },
      signal: AbortSignal.timeout(8000),
    });
    if (res.status === 401 || res.status === 403) {
      throw new Error(`授權失敗 (${res.status}),請在 Claude Code 內用一次以刷新 token`);
    }
    if (res.status === 429) {
      throw new Error('API 限流,稍後自動重試(顯示上次資料)');
    }
    if (!res.ok) throw new Error(`API 回應 ${res.status}`);
    const j = await res.json();
    if (j && j.error && j.error.type === 'rate_limit_error') {
      throw new Error('API 限流,稍後自動重試(顯示上次資料)');
    }

    // 優先用結構化的 limits 陣列;沒有就退回 five_hour / seven_day
    let items = [];
    if (Array.isArray(j.limits) && j.limits.length) {
      for (const l of j.limits) {
        let label;
        if (l.kind === 'session' || l.group === 'session') label = 'Current session';
        else if (l.kind === 'weekly_all') label = 'Current week (all models)';
        else if (l.kind === 'weekly_scoped') {
          const m = l.scope && l.scope.model && l.scope.model.display_name;
          label = `Current week (${m || 'scoped'})`;
        } else label = l.kind || l.group || 'limit';
        items.push({
          label, percent: Number(l.percent) || 0, resetsAt: l.resets_at,
          active: !!l.is_active, severity: l.severity || 'normal',
          kind: l.kind || l.group || label,
        });
      }
    } else {
      if (j.five_hour) items.push({ label: 'Current session', percent: Number(j.five_hour.utilization) || 0, resetsAt: j.five_hour.resets_at, kind: 'session', severity: 'normal', active: true });
      if (j.seven_day) items.push({ label: 'Current week (all models)', percent: Number(j.seven_day.utilization) || 0, resetsAt: j.seven_day.resets_at, kind: 'weekly_all', severity: 'normal', active: false });
    }
    lastData = items;
    lastError = null;
    lastOk = Date.now();

    // 記錄歷史樣本供預估撞限使用
    for (const it of items) {
      if (!history.has(it.kind)) history.set(it.kind, []);
      const arr = history.get(it.kind);
      // 若 % 下降(視窗重置),清掉舊樣本重新起算
      if (arr.length && it.percent < arr[arr.length - 1].p) arr.length = 0;
      arr.push({ t: lastOk, p: it.percent });
      if (arr.length > HIST_MAX) arr.shift();
    }
  } catch (e) {
    lastError = (e && e.message) || String(e);
  }
  lastFetch = Date.now();
}

// ---------- 抓 ccusage 花費(best-effort) ----------
function ccusageJSON(args) {
  const out = execFileSync('ccusage', args, { encoding: 'utf8', timeout: 8000, maxBuffer: 32 * 1024 * 1024 });
  return JSON.parse(out);
}
function fetchCost() {
  try {
    const daily = ccusageJSON(['daily', '-j']);
    const today = (daily.daily || []).slice(-1)[0] || null;
    let burnHr = null;
    try {
      const blocks = ccusageJSON(['blocks', '--active', '--json']);
      const b = (blocks.blocks || []).find((x) => x.isActive);
      if (b && b.burnRate) burnHr = b.burnRate.costPerHour;
    } catch { /* 區塊拿不到就算了 */ }
    if (!today) { lastCost = null; return; }

    // 今日各模型(降冪、取前 3、金額 >= 0.01)
    const breakdown = (today.modelBreakdowns || [])
      .map((b) => ({ m: shortModel(b.modelName), c: b.cost || 0 }))
      .filter((x) => x.c >= 0.01)
      .sort((a, b) => b.c - a.c)
      .slice(0, 3);
    // 近 7 日花費(sparkline)
    const spark7 = (daily.daily || []).slice(-7).map((d) => d.totalCost || 0);
    // 本週 / 本月(各自 best-effort)
    let weekCost = null, monthCost = null;
    try { const w = (ccusageJSON(['weekly', '-j']).weekly || []).slice(-1)[0]; if (w) weekCost = w.totalCost; } catch {}
    try { const m = (ccusageJSON(['monthly', '-j']).monthly || []).slice(-1)[0]; if (m) monthCost = m.totalCost; } catch {}

    lastCost = { cost: today.totalCost, tokens: today.totalTokens, burnHr, breakdown, spark7, weekCost, monthCost };
  } catch {
    lastCost = null; // ccusage 未安裝或失敗 → 整區省略
  }
}

// ---------- 畫面 ----------
const W = 40;          // 版面寬度基準(橫線長度、標題列靠右)
const BAR_W = 34;
const line = (s = '') => s;                                   // 去框:內容直接靠左
const hr = () => `${C.gray}${'─'.repeat(W)}${C.reset}`;       // 分區橫線

function money(n) { return '$' + Number(n || 0).toFixed(2); }
function money2(n) { // 緊湊金額:>=10 無小數,<10 一位
  n = Number(n || 0);
  return '$' + (n >= 10 ? Math.round(n).toString() : n.toFixed(1));
}
function fmtTokens(n) {
  n = Number(n || 0);
  if (n >= 1e6) return (n / 1e6).toFixed(1) + 'M';
  if (n >= 1e3) return (n / 1e3).toFixed(1) + 'K';
  return String(n);
}
function shortModel(name) {
  if (/opus/i.test(name)) return 'Opus';
  if (/sonnet/i.test(name)) return 'Sonnet';
  if (/haiku/i.test(name)) return 'Haiku';
  if (/fable/i.test(name)) return 'Fable';
  return name;
}
function sparkline(vals) {
  const blocks = '▁▂▃▄▅▆▇█';
  const max = Math.max(1, ...vals);
  return vals.map((v) => blocks[Math.min(7, Math.floor((v / max) * 7))]).join('');
}

// ---------- 大字時鐘(tty-clock 風格,用 █ 拼 LED 數字)----------
// 字型仍以 5 列點陣定義,bigClock() 再用半形方塊(▀▄█)壓成 3 列,避免上下被拉長
const DIGITS = {
  '0': ['███', '█ █', '█ █', '█ █', '███'],
  '1': ['  █', '  █', '  █', '  █', '  █'],
  '2': ['███', '  █', '███', '█  ', '███'],
  '3': ['███', '  █', '███', '  █', '███'],
  '4': ['█ █', '█ █', '███', '  █', '  █'],
  '5': ['███', '█  ', '███', '  █', '███'],
  '6': ['███', '█  ', '███', '█ █', '███'],
  '7': ['███', '  █', '  █', '  █', '  █'],
  '8': ['███', '█ █', '███', '█ █', '███'],
  '9': ['███', '█ █', '███', '  █', '███'],
  ':': [' ', '█', ' ', '█', ' '],
};
// 把每個字元的 5 列點陣,兩列一組壓成半形方塊 → 3 列(高度減半,比例正常)
function bigClock(str) {
  const half = (t, b) => (t && b ? '█' : t ? '▀' : b ? '▄' : ' ');
  const pairs = [[0, 1], [2, 3], [4, -1]]; // 5 列 → 3 半列((4,無))
  const out = ['', '', ''];
  [...str].forEach((ch, ci) => {
    const g = DIGITS[ch] || ['   ', '   ', '   ', '   ', '   '];
    const w = g[0].length;
    const sub = g.map((s) => s.padEnd(w));
    for (let hr = 0; hr < 3; hr++) {
      const [ti, bi] = pairs[hr];
      let seg = '';
      for (let x = 0; x < w; x++) {
        const t = sub[ti][x] === '█';
        const b = bi < 0 ? false : sub[bi][x] === '█';
        seg += half(t, b);
      }
      out[hr] += (ci ? ' ' : '') + seg;
    }
  });
  return out.map((r) => '  ' + C.white + r + C.reset);
}

// ---------- 進度條 + 系統資源 ----------
function bar(pct, width, col) {
  const p = Math.max(0, Math.min(100, Number(pct) || 0));
  const filled = Math.round((p / 100) * width);
  return `${col}${'█'.repeat(filled)}${C.gray}${'░'.repeat(Math.max(0, width - filled))}${C.reset}`;
}
function sysColor(p) {
  if (p >= 90) return C.red;
  if (p >= 70) return C.yellow;
  return C.blue;
}
let prevCpu = null;
function sampleCPU() {
  const cpus = os.cpus();
  let idle = 0, total = 0;
  for (const c of cpus) {
    for (const k in c.times) total += c.times[k];
    idle += c.times.idle;
  }
  if (!prevCpu) { prevCpu = { idle, total }; return null; }
  const di = idle - prevCpu.idle, dt = total - prevCpu.total;
  prevCpu = { idle, total };
  if (dt <= 0) return null;
  return Math.round(100 * (1 - di / dt));
}
function readMem() {
  let total = null, avail = null;
  try {
    const mi = fs.readFileSync('/proc/meminfo', 'utf8');
    const mt = mi.match(/MemTotal:\s+(\d+)/);
    const ma = mi.match(/MemAvailable:\s+(\d+)/);
    if (mt) total = Number(mt[1]) * 1024;
    if (ma) avail = Number(ma[1]) * 1024;
  } catch { /* 非 Linux 或讀不到 → 退回 os */ }
  if (total == null) total = os.totalmem();
  if (avail == null) avail = os.freemem();
  const used = total - avail;
  const g = (n) => { const v = n / 1073741824; return v >= 10 ? String(Math.round(v)) : v.toFixed(1); };
  return { usedG: g(used), totalG: g(total), pct: Math.round((used / total) * 100) };
}
let sys = { cpu: null, mem: null };
function updateSys() {
  const c = sampleCPU();
  if (c != null) sys.cpu = c;
  sys.mem = readMem();
}
function syncSleep(ms) { // --once 用:取兩次 CPU 樣本間的短暫等待
  Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, ms);
}

function usageBlock(item, now) {
  const p = Math.max(0, Math.min(100, item.percent));
  const filled = Math.round((p / 100) * BAR_W);
  const col = severityColor(p, item.severity);
  const barStr = `${col}${'█'.repeat(filled)}${C.gray}${'█'.repeat(BAR_W - filled)}${C.reset}`;
  const out = [];

  // 標題行:▶ + label(active 高亮)+ severity 標籤 / ← 目前最緊
  const labelCol = item.active ? `${C.bold}${C.white}` : `${C.bold}${C.grayText}`;
  const marker = item.active ? `${C.cyan}▶ ${C.reset}` : '  ';
  const right = severityTag(item.severity);
  const left = `${marker}${labelCol}${item.label}${C.reset}`;
  out.push(line(right ? padBetween(left, right, W) : left));

  // 進度條
  out.push(line(`${barStr}  ${col}${p}%${C.reset} ${C.grayText}used${C.reset}`));

  // reset + 倒數
  if (item.resetsAt) {
    const remain = fmtDuration(new Date(item.resetsAt).getTime() - now);
    out.push(line(`${C.grayText}Resets ${fmtClock(item.resetsAt)} · 還剩 ${remain}${C.reset}`));
  }

  // 預估撞限(僅 session / weekly_all 顯示,避免雜亂)
  if (item.kind === 'session' || item.kind === 'weekly_all') {
    const eta = projectETA(item.kind, p);
    if (eta) {
      const etaCol = /^(\d+)m$|^\d+s$/.test(eta) ? C.red : C.yellow;
      out.push(line(`${etaCol}⏳ 依目前速度,約 ${eta} 用完${C.reset}`));
    }
  }

  out.push(line(''));
  return out;
}

function render() {
  const now = Date.now();
  const d = new Date();
  const lines = [];

  // 標題列(左:標題,右:日期)
  const date = d.toLocaleDateString('en-CA'); // YYYY-MM-DD
  lines.push(padBetween(`${C.bold}${C.cyan}📊 Claude Code Usage${C.reset}`, `${C.grayText}${date}${C.reset}`, W));
  // 大字時鐘 HH:MM:SS
  lines.push(line(''));
  bigClock(d.toLocaleTimeString('en-GB')).forEach((l) => lines.push(l));
  lines.push(hr());

  if (lastError && !lastData) {
    lines.push(line(`${C.red}⚠ ${lastError}${C.reset}`));
  } else if (!lastData) {
    lines.push(line(`${C.dim}載入中…${C.reset}`));
  } else {
    for (const item of lastData) usageBlock(item, now).forEach((l) => lines.push(l));
    while (lines.length && lines[lines.length - 1] === '') lines.pop(); // 去掉最後多餘空行
    if (lastError) lines.push(line(`${C.yellow}⚠ ${lastError}${C.reset}`));
  }

  // 花費區(ccusage,best-effort)
  if (lastCost) {
    lines.push(hr());
    const burn = lastCost.burnHr != null ? ` · ${C.yellow}🔥 ${money(lastCost.burnHr)}/hr${C.reset}` : '';
    lines.push(line(`${C.green}💰 今日 ${money(lastCost.cost)}${C.reset}${burn} ${C.grayText}· ${fmtTokens(lastCost.tokens)} tok${C.reset}`));
    // 本週 / 本月
    if (lastCost.weekCost != null || lastCost.monthCost != null) {
      const wk = lastCost.weekCost != null ? `本週 ${money2(lastCost.weekCost)}` : '';
      const mo = lastCost.monthCost != null ? `本月 ${money2(lastCost.monthCost)}` : '';
      lines.push(line(`${C.grayText}📅 ${[wk, mo].filter(Boolean).join(' · ')}${C.reset}`));
    }
    // 今日各模型
    if (lastCost.breakdown && lastCost.breakdown.length) {
      const seg = lastCost.breakdown.map((x) => `${x.m} ${money2(x.c)}`).join(' · ');
      lines.push(line(`${C.grayText}🧩 ${seg}${C.reset}`));
    }
    // 近 7 日 sparkline
    if (lastCost.spark7 && lastCost.spark7.length) {
      lines.push(line(`${C.grayText}📈 近7日 ${C.cyan}${sparkline(lastCost.spark7)}${C.reset}`));
    }
  }

  // 系統資源(CPU / RAM 各一條 bar)
  lines.push(hr());
  const cpu = sys.cpu;
  const cpuCol = cpu == null ? C.gray : sysColor(cpu);
  const cpuTxt = cpu == null ? ' --' : `${cpu}`.padStart(3);
  lines.push(line(`${C.green}💻 CPU${C.reset}  ${bar(cpu == null ? 0 : cpu, 20, cpuCol)}  ${cpuCol}${cpuTxt}%${C.reset}`));
  if (sys.mem) {
    const m = sys.mem;
    const memCol = sysColor(m.pct);
    lines.push(line(`${C.green}💾 RAM${C.reset}  ${bar(m.pct, 20, memCol)}  ${memCol}${`${m.pct}`.padStart(3)}%${C.reset} ${C.grayText}${m.usedG}/${m.totalG}G${C.reset}`));
  }

  // 頁尾(壓成一行省高度)
  lines.push(hr());
  const updated = lastOk ? new Date(lastOk).toLocaleTimeString('en-GB') : '—';
  if (once) {
    lines.push(line(`${C.grayText}更新於 ${updated}${C.reset}`));
  } else {
    const nextIn = fmtDuration(intervalMs - (now - lastFetch));
    lines.push(line(`${C.grayText}更新於 ${updated} · 每 ${intervalMin} 分刷新 · 下次 ${nextIn}${C.reset}`));
    lines.push(line(`${C.grayText}Ctrl+C 離開${C.reset}`));
  }

  if (once) {
    process.stdout.write(lines.join('\n') + '\n');
  } else {
    // 每行清到行尾(\x1b[K)避免右側殘影;回頂重繪;結尾不多印換行以免多捲一行;
    // 最後 \x1b[J 清掉下方(上一張較高時的殘留)
    const frame = lines.map((l) => l + '\x1b[K').join('\n');
    process.stdout.write('\x1b[H' + frame + '\x1b[J');
  }
}

// ---------- 自我測試(注入假資料,不打 API)----------
function runSelfTest() {
  const nowT = Date.now();
  lastOk = nowT;
  lastFetch = nowT;
  lastData = [
    { label: 'Current session', percent: 78, resetsAt: new Date(nowT + 90 * 60000).toISOString(), active: true, severity: 'warning', kind: 'session' },
    { label: 'Current week (all models)', percent: 37, resetsAt: new Date(nowT + 42 * 3600000).toISOString(), active: false, severity: 'normal', kind: 'weekly_all' },
    { label: 'Current week (Fable)', percent: 16, resetsAt: new Date(nowT + 42 * 3600000).toISOString(), active: false, severity: 'normal', kind: 'weekly_scoped' },
  ];
  // 種入兩筆歷史(60s 前 70% → 現在 78%)以觸發用量預估
  history.set('session', [{ t: nowT - 60000, p: 70 }, { t: nowT, p: 78 }]);
  history.set('weekly_all', [{ t: nowT - 60000, p: 36.9 }, { t: nowT, p: 37 }]);
  lastCost = {
    cost: 54.3, tokens: 27246553, burnHr: 7.4,
    weekCost: 33.69, monthCost: 176.84,
    breakdown: [{ m: 'Opus', c: 27.05 }, { m: 'Fable', c: 6.14 }, { m: 'Sonnet', c: 0.47 }],
    spark7: [12, 28, 40, 19, 54, 31, 22],
  };
  sys = { cpu: 34, mem: { usedG: '12', totalG: '31', pct: 39 } };
  render();
}

// ---------- 主流程 ----------
(async () => {
  if (selftest) { runSelfTest(); return; }
  await fetchData();
  fetchCost();
  if (once) {
    updateSys(); syncSleep(250); updateSys(); // 取兩次樣本才有 CPU%
    render();
    return;
  }

  process.stdout.write('\x1b[?1049h\x1b[?25l'); // 進替代畫面 + 隱藏游標
  updateSys();
  render();

  const tick = setInterval(async () => {
    if (Date.now() - lastFetch >= intervalMs) { await fetchData(); fetchCost(); }
    updateSys();
    render();
  }, 1000);

  const cleanup = () => {
    clearInterval(tick);
    process.stdout.write('\x1b[?25h\x1b[?1049l' + C.reset); // 還原終端
    process.exit(0);
  };
  process.on('SIGINT', cleanup);
  process.on('SIGTERM', cleanup);
})();
