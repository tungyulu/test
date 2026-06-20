# UI Contract: 快艇骰子遊戲

This document defines the user-facing interface contract for `yacht.html` — the screens, interactions, and observable behaviors the game must provide.

---

## Screens / Phases

### 1. Menu Screen (`phase === 'menu'`)

**Elements**:
- 標題：「快艇骰子」
- 副標題：遊戲簡介（一句話）
- 按鈕：「單人遊戲（對戰 CPU）」
- 按鈕：「雙人遊戲」

**Interactions**:
- Click「單人遊戲」→ `startGame('1p')`，轉換至 Playing Screen
- Click「雙人遊戲」→ `startGame('2p')`，轉換至 Playing Screen

---

### 2. Playing Screen (`phase === 'playing'`)

**Layout**（桌機版）:
```
[ 標題列：快艇骰子 | 回合 X/13 | 目前玩家：玩家一 ]
[ 骰子區：5 顆骰子（inline，點擊切換鎖定） ]
[ 控制列：[擲骰 (次數剩餘: N)] ]
[ 主體：左側計分板 | 右側（行動裝置：下方）計分板 ]
```

**骰子區**:
- 每顆骰子顯示 SVG 骰面（點數 1–6）
- 鎖定時：骰子加深背景色 + 顯示「🔒」或明顯邊框
- 未擲骰前骰子顯示問號或空白；擲骰後顯示點數
- 點擊骰子：`toggleHold(dieIndex)`（僅在 rollPhase && rollsLeft > 0 時有效）

**擲骰按鈕**:
- Label：「擲骰」+ 次數提示（`剩餘 ${rollsLeft} 次`）
- Disabled 條件：`rollsLeft === 0` 或 `!rollPhase && rollsLeft === 3` (已選完類別正等待下一回合開始，但此時 rollsLeft 已重置)
- Click → `rollDice()`

**計分板**（每位玩家一欄）:
- 行標：類別名稱（繁體中文）
- 欄標：玩家名稱（現任玩家欄有視覺高亮）
- 已填入的格：顯示數字，不可點擊
- 未填入的格（非現任玩家）：顯示「—」，不可點擊
- 未填入的格（現任玩家，已擲骰後）：顯示預覽分數（灰色斜體），可點擊 → `selectCategory(categoryId)`
- 未填入的格（現任玩家，尚未擲骰）：顯示「—」，不可點擊
- 分隔列：上區小計 | 上區獎勵（顯示進度：`N/63`，達標後顯示「+35」）| 下區合計 | 總計

**CPU 回合**:
- 顯示「CPU 思考中…」提示
- 骰子區與計分板的點擊事件均禁用
- CPU 動作透過 setTimeout 序列化（400ms 間隔），讓玩家看到骰子更新

---

### 3. Game Over Screen (`phase === 'gameover'`)

**Elements**:
- 標題：「遊戲結束」
- 完整計分板（同 Playing Screen，所有欄位已填滿）
- 勝者標示：勝者名稱欄高亮（黃色或綠色）；平局則兩欄均標示
- 按鈕：「再玩一次」→ `resetGame()`，轉換至 Menu Screen

---

## Interaction Contract

| 動作 | 前置條件 | 結果 |
|------|----------|------|
| `rollDice()` | `rollsLeft > 0` | 未鎖定骰子重新隨機；`rollsLeft--`；`rollPhase = true` |
| `toggleHold(i)` | `rollPhase && rollsLeft > 0` | `dice[i].held = !dice[i].held` |
| `selectCategory(id)` | `rollPhase && scorecard[id] === null` | 計算分數 → 填入 scorecard；重置骰子；切換玩家或回合；若最後一格 → gameover |
| `startGame(mode)` | `phase === 'menu'` | 初始化 GameState，`phase = 'playing'` |
| `resetGame()` | `phase === 'gameover'` | 清除所有狀態，`phase = 'menu'` |

---

## Responsive Breakpoints

| 寬度 | 計分板佈局 |
|------|-----------|
| ≥ 768px | 骰子區在上，計分板雙欄並排（左右） |
| < 768px | 骰子區在上，計分板雙欄仍並排但縮小字型；允許橫向捲動 |

---

## Visual Style Contract

- **Font**: Noto Sans TC（Google Fonts CDN）
- **CSS**: Tailwind CSS CDN（與 index.html、betting.html 相同版本）
- **Color palette**: Tailwind default（主色調：indigo-600 或 blue-600 按鈕；amber/yellow 骰子背景；green 勝者標示）
- **骰子 SVG**: 內嵌於 HTML（不外部引用）；白底黑點；圓角矩形邊框
