#!/usr/bin/env node
/**
 * usage-dashboard.js — 終端機即時 /usage 儀表板
 *
 * 顯示 Claude Code `/usage` 的方案額度(Current session / Current week …),
 * 自動定時刷新,不用一直手動打 /usage。
 *
 * 用法:
 *   node usage-dashboard.js            # 預設每 1 分鐘刷新
 *   node usage-dashboard.js 5          # 每 5 分鐘刷新
 *   node usage-dashboard.js --interval 2
 *   node usage-dashboard.js --once     # 只印一次就結束(適合排程/cron)
 *   node usage-dashboard.js --serve    # 起本機網頁儀表板 http://localhost:8787
 *   node usage-dashboard.js --serve 9000   # 指定埠號
 *
 * 資料來源:GET https://api.anthropic.com/api/oauth/usage
 *   憑證讀自 ~/.claude/.credentials.json(即 /usage 用的同一份 OAuth token)。
 *   每次刷新都重讀憑證檔,以搭配 Claude Code 的 token 自動更新。
 *
 * --serve 模式:
 *   GET /            → 回傳同目錄的 usage.html(瀏覽器儀表板)
 *   GET /api/usage   → 伺服器端讀本機憑證、代理 Anthropic API,回傳正規化 JSON
 *   只綁 127.0.0.1(憑證代理不對外)。
 */

'use strict';
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const http = require('node:http');

// ---------- 解析參數 ----------
const argv = process.argv.slice(2);
let intervalMin = 1;
let once = false;
let serve = false;
let servePort = 8787;
for (let i = 0; i < argv.length; i++) {
  const a = argv[i];
  if (a === '--once') once = true;
  else if (a === '--interval') intervalMin = Number(argv[++i]) || intervalMin;
  else if (a === '--serve') {
    serve = true;
    if (/^\d+$/.test(argv[i + 1] || '')) servePort = Number(argv[++i]);
  } else if (a === '--port') servePort = Number(argv[++i]) || servePort;
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

// ---------- 時間格式 ----------
const TZ = Intl.DateTimeFormat().resolvedOptions().timeZone || 'local';
function lowerAmPm(s) { return s.replace(/\s?([AP])M/i, (_, g) => g.toLowerCase() + 'm'); }
function fmtReset(iso) {
  if (!iso) return '';
  const d = new Date(iso);
  const now = new Date();
  const timeOpts = { hour: 'numeric', minute: '2-digit', hour12: true };
  const sameDay = d.toDateString() === now.toDateString();
  const label = sameDay
    ? lowerAmPm(d.toLocaleTimeString('en-US', timeOpts))
    : lowerAmPm(d.toLocaleString('en-US', { month: 'short', day: 'numeric', ...timeOpts }));
  return `Resets ${label} (${TZ})`;
}
function fmtDuration(ms) {
  if (ms < 0) ms = 0;
  const totalMin = Math.floor(ms / 60000);
  const h = Math.floor(totalMin / 60), m = totalMin % 60, s = Math.floor(ms / 1000) % 60;
  if (h > 0) return `${h}h ${m}m`;
  if (m > 0) return `${m}m`;
  return `${s}s`;
}

// ---------- 抓 /usage 資料 ----------
const CRED = path.join(os.homedir(), '.claude', '.credentials.json');
let lastData = null;   // 解析後的 limits 陣列
let lastFetch = 0;
let lastError = null;
let lastOk = 0;

function severityColor(percent) {
  if (percent >= 95) return C.red;
  if (percent >= 80) return C.yellow;
  return C.blue;
}

// 讀本機憑證 + 呼叫 API,回傳正規化的 items 陣列;失敗時 throw(err.status 帶 HTTP 狀態)
async function fetchUsage() {
  const cred = JSON.parse(fs.readFileSync(CRED, 'utf8'));
  const oauth = cred.claudeAiOauth || {};
  const tok = oauth.accessToken;
  if (!tok) { const e = new Error('找不到 accessToken(請先在 Claude Code 登入)'); e.status = 401; throw e; }
  if (oauth.expiresAt && oauth.expiresAt < Date.now()) {
    const e = new Error('Token 已過期,請在 Claude Code 內用一次(會自動刷新)'); e.status = 401; throw e;
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
    const e = new Error(`授權失敗 (${res.status}),請在 Claude Code 內用一次以刷新 token`); e.status = res.status; throw e;
  }
  if (!res.ok) { const e = new Error(`API 回應 ${res.status}`); e.status = res.status; throw e; }
  const j = await res.json();

  // 優先用結構化的 limits 陣列;沒有就退回 five_hour / seven_day
  const items = [];
  if (Array.isArray(j.limits) && j.limits.length) {
    for (const l of j.limits) {
      let label;
      if (l.kind === 'session' || l.group === 'session') label = 'Current session';
      else if (l.kind === 'weekly_all') label = 'Current week (all models)';
      else if (l.kind === 'weekly_scoped') {
        const m = l.scope && l.scope.model && l.scope.model.display_name;
        label = `Current week (${m || 'scoped'})`;
      } else label = l.kind || l.group || 'limit';
      items.push({ label, percent: Number(l.percent) || 0, resetsAt: l.resets_at, active: !!l.is_active });
    }
  } else {
    if (j.five_hour) items.push({ label: 'Current session', percent: Number(j.five_hour.utilization) || 0, resetsAt: j.five_hour.resets_at });
    if (j.seven_day) items.push({ label: 'Current week (all models)', percent: Number(j.seven_day.utilization) || 0, resetsAt: j.seven_day.resets_at });
  }
  return items;
}

async function fetchData() {
  try {
    lastData = await fetchUsage();
    lastError = null;
    lastOk = Date.now();
  } catch (e) {
    lastError = (e && e.message) || String(e);
  }
  lastFetch = Date.now();
}

// ---------- 畫面 ----------
const W = 52;
const BAR_W = 34;
const line = (s = '') => `${C.gray}│${C.reset} ` + pad(s, W) + ` ${C.gray}│${C.reset}`;
const rule = (l, r) => `${C.gray}${l}${'─'.repeat(W + 2)}${r}${C.reset}`;

function usageBlock(item) {
  const p = Math.max(0, Math.min(100, item.percent));
  const filled = Math.round((p / 100) * BAR_W);
  const col = severityColor(p);
  const barStr = `${col}${'█'.repeat(filled)}${C.gray}${'█'.repeat(BAR_W - filled)}${C.reset}`;
  const out = [];
  out.push(line(`${C.bold}${C.white}${item.label}${C.reset}`));
  out.push(line(`${barStr}  ${col}${p}%${C.reset} ${C.grayText}used${C.reset}`));
  if (item.resetsAt) out.push(line(`${C.grayText}${fmtReset(item.resetsAt)}${C.reset}`));
  out.push(line(''));
  return out;
}

function render() {
  const now = Date.now();
  const lines = [];
  lines.push(rule('╭', '╮'));
  lines.push(line(`${C.bold}${C.cyan}📊 Claude Code Usage${C.reset}`));
  lines.push(rule('├', '┤'));
  lines.push(line(''));

  if (lastError && !lastData) {
    lines.push(line(`${C.red}⚠ ${lastError}${C.reset}`));
    lines.push(line(''));
  } else if (!lastData) {
    lines.push(line(`${C.dim}載入中…${C.reset}`));
    lines.push(line(''));
  } else {
    for (const item of lastData) usageBlock(item).forEach((l) => lines.push(l));
    if (lastError) lines.push(line(`${C.yellow}⚠ 更新失敗(顯示上次資料):${lastError}${C.reset}`));
  }

  lines.push(rule('├', '┤'));
  const updated = lastOk ? new Date(lastOk).toLocaleTimeString('en-GB') : '—';
  const nextIn = once ? '—' : fmtDuration(intervalMs - (now - lastFetch));
  if (once) {
    lines.push(line(`${C.grayText}更新於 ${updated}${C.reset}`));
  } else {
    lines.push(line(`${C.grayText}更新於 ${updated} · 每 ${intervalMin} 分刷新 · 下次 ${nextIn}${C.reset}`));
    lines.push(line(`${C.grayText}Ctrl+C 離開${C.reset}`));
  }
  lines.push(rule('╰', '╯'));

  const frame = lines.join('\n');
  if (once) process.stdout.write(frame + '\n');
  else process.stdout.write('\x1b[H' + frame + '\n\x1b[J');
}

// ---------- --serve:本機網頁儀表板 ----------
function startServer(port) {
  const htmlPath = path.join(__dirname, 'usage.html');
  const server = http.createServer(async (req, res) => {
    const url = (req.url || '/').split('?')[0];
    if (req.method !== 'GET') {
      res.writeHead(405, { 'Content-Type': 'application/json; charset=utf-8' });
      res.end(JSON.stringify({ error: 'method not allowed' }));
      return;
    }
    if (url === '/' || url === '/usage.html' || url === '/index.html') {
      try {
        const html = fs.readFileSync(htmlPath);
        res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store' });
        res.end(html);
      } catch {
        res.writeHead(500, { 'Content-Type': 'text/plain; charset=utf-8' });
        res.end('找不到 usage.html(請與 usage-dashboard.js 放在同一目錄)');
      }
      return;
    }
    if (url === '/api/usage') {
      try {
        const items = await fetchUsage();
        res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' });
        res.end(JSON.stringify({ items, fetchedAt: Date.now() }));
      } catch (e) {
        const status = (e && e.status) || 502;
        res.writeHead(status, { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' });
        res.end(JSON.stringify({ error: (e && e.message) || String(e) }));
      }
      return;
    }
    res.writeHead(404, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify({ error: 'not found' }));
  });
  server.listen(port, '127.0.0.1', () => {
    console.log(`${C.cyan}📊 Claude Code Usage 網頁儀表板${C.reset}`);
    console.log(`   打開  ${C.bold}http://localhost:${port}${C.reset}`);
    console.log(`${C.grayText}   (只綁 127.0.0.1,Ctrl+C 離開)${C.reset}`);
  });
  server.on('error', (e) => {
    console.error(`${C.red}無法啟動伺服器:${e.message}${C.reset}`);
    process.exit(1);
  });
}

// ---------- 主流程 ----------
(async () => {
  if (serve) { startServer(servePort); return; }

  await fetchData();
  if (once) { render(); return; }

  process.stdout.write('\x1b[?1049h\x1b[?25l'); // 進替代畫面 + 隱藏游標
  render();

  const tick = setInterval(async () => {
    if (Date.now() - lastFetch >= intervalMs) await fetchData();
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
