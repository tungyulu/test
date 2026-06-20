# Quickstart & Validation Guide: 快艇骰子遊戲

## Prerequisites

- 現代瀏覽器（Chrome 100+、Edge 100+、Safari 15+）
- 網路連線（首次載入 Tailwind CDN + Google Fonts）
- 或離線後可從快取讀取

## Running the Game

```bash
# 直接以瀏覽器開啟（本機驗證）
open yacht.html          # macOS
start yacht.html         # Windows
xdg-open yacht.html      # Linux

# 或透過本機伺服器（避免 file:// 限制）
npx serve .              # 任何機器，訪問 http://localhost:3000/yacht.html

# GitHub Pages（部署後）
# https://tungyulu.github.io/yacht.html
```

---

## Validation Scenarios

### V-01：核心遊戲流程（P1）

**目標**：驗證一局 13 回合能完整跑完。

步驟：
1. 開啟 `yacht.html`，確認顯示選單畫面（兩個模式按鈕）。
2. 點「單人遊戲」，確認進入遊戲畫面，顯示「回合 1/13 | 玩家」。
3. 點「擲骰」，確認 5 顆骰子顯示 1–6 的隨機點數，按鈕顯示「剩餘 2 次」。
4. 點選 2 顆骰子鎖定，確認這 2 顆有視覺鎖定標示。
5. 再點「擲骰」，確認鎖定骰子點數未改變，其餘 3 顆重新隨機。
6. 點計分板中一個類別（灰色預覽分數），確認分數填入、骰子重置、CPU 開始動作。
7. 等 CPU 完成，確認 CPU 計分板也填入一格，回合計數更新。
8. 重複直至回合 13 結束，確認顯示遊戲結束畫面。

**Expected**：計分板所有格填滿，顯示「遊戲結束」與勝者。

---

### V-02：計分規則正確性

**目標**：手動驗證幾個關鍵類別的得分計算。

| 測試骰子 | 選擇類別 | 預期得分 |
|---------|---------|---------|
| 1,1,1,1,1 | 快艇（Yacht） | 50 |
| 1,1,1,1,1 | 一點（Aces） | 5 |
| 2,3,4,5,6 | 大順（Large Straight） | 40 |
| 1,2,3,4,6 | 小順（Small Straight） | 30 |
| 3,3,3,5,5 | 葫蘆（Full House） | 25 |
| 4,4,4,2,3 | 三同（Three of a Kind） | 17 |
| 1,2,3,4,5 | 機會（Chance） | 15 |
| 1,2,3,4,5 | 三同（Three of a Kind） | 0（不符合條件）|

步驟：
1. 進入遊戲，手動操控擲骰直到出現目標骰子組合（可透過不鎖任何骰子多次擲骰等待）。
2. 對照計分板預覽分數（灰色數字）是否與上表一致。
3. 點選類別，確認正式填入的分數與預覽相同。

---

### V-03：上區獎勵

**目標**：上區合計 ≥ 63 時顯示 +35 獎勵。

步驟：
1. 在計分板依序填入上區 6 類，使合計 ≥ 63（例如 Sixes 全填滿 = 30 分，搭配其他類各填滿即達）。
2. 觀察計分板「上區獎勵」欄，確認顯示「+35」。
3. 確認總計 = 上區合計 + 35 + 下區合計。

---

### V-04：CPU 自動回合

**目標**：CPU 能在 2 秒內完成一個回合。

步驟：
1. 選「單人遊戲」。
2. 玩家完成第一回合後，觀察 CPU 回合。
3. 確認 CPU 出現「思考中…」提示，骰子自動更新 1–2 次，最終自動選分類。
4. 整個過程不超過 3 秒（含 UI 更新）。

---

### V-05：行動裝置響應式

**目標**：375px 寬度下畫面正常，不溢出。

步驟：
1. 開啟 DevTools → 切換至 iPhone SE 模擬（375px）。
2. 進入遊戲，確認骰子與計分板不橫向溢出視窗。
3. 計分板雙欄可正常顯示（字型縮小但可讀）。

---

### V-06：禁用狀態正確性

- 擲骰 3 次後，「擲骰」按鈕應 disabled（灰色，不可點）。
- 已填入的計分格不可再次點選（cursor: default，無 hover 效果）。
- 遊戲結束後骰子和計分格均不可互動。

---

## Links to Design Artifacts

- Data Model: [`data-model.md`](./data-model.md)
- UI Contract: [`contracts/ui-contract.md`](./contracts/ui-contract.md)
- Research: [`research.md`](./research.md)
