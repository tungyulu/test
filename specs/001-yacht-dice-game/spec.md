# Feature Specification: 快艇骰子遊戲（Yacht Dice）

**Feature Branch**: `001-yacht-dice-game`

**Created**: 2026-06-21

**Status**: Draft

**Input**: 開發一個快艇骰子遊戲，遊戲方式跟 Nintendo Switch 上的遊戲一樣（世界遊戲大全51），可以跟另外兩個 HTML 檔案一樣在 https://tungyulu.github.io/ 打開

## User Scenarios & Testing *(mandatory)*

### User Story 1 - 完成一局完整遊戲 (Priority: P1)

玩家開啟 `yacht.html`，選擇單人（對戰 CPU）或雙人模式，依序輪流擲骰、鎖定骰子、再擲，最多 3 次，然後選擇一個計分類別登記分數。13 回合後計算總分，高分者獲勝。

**Why this priority**: 核心遊戲體驗，其他功能都圍繞此流程。

**Independent Test**: 直接開啟 `yacht.html`，選人數，打完 13 回合，看到最終計分板即視為可用的 MVP。

**Acceptance Scenarios**:

1. **Given** 遊戲開始，**When** 玩家按「擲骰」，**Then** 5 顆骰子顯示隨機點數（1–6），且最多可再擲 2 次。
2. **Given** 第一次擲骰後，**When** 玩家點選某顆骰子，**Then** 該骰子顯示鎖定狀態；再按「擲骰」時鎖定的骰子不重擲。
3. **Given** 已選好骰子，**When** 玩家點選計分類別（尚未使用），**Then** 分數依規則計算並登記，輪到下一位玩家。
4. **Given** 13 個類別全部填滿，**When** 最後一回合結束，**Then** 顯示最終計分板，標示勝負。

---

### User Story 2 - CPU 自動出牌 (Priority: P2)

在單人模式中，CPU 能自動選擇保留哪些骰子、決定再擲或停止，並選出最佳計分類別。

**Why this priority**: 提供單人對戰的可玩性，不需要找另一位玩家。

**Independent Test**: 選單人模式並讓 CPU 自動完成一局，觀察 CPU 每回合皆正常行動。

**Acceptance Scenarios**:

1. **Given** 輪到 CPU，**When** CPU 的回合開始，**Then** 稍作延遲後自動擲骰、選擇保留並再擲（最多 2 次），然後自動選分類。
2. **Given** CPU 選分類，**When** 多個類別有相近期望值，**Then** CPU 選擇能得分最高的可用類別（使用簡單 greedy 策略）。

---

### User Story 3 - 上區獎勵與最終計分板 (Priority: P2)

上區（Aces–Sixes）合計 ≥ 63 分時自動加 35 分獎勵，最終顯示完整計分板含上區小計、獎勵、下區合計、總分，並標示勝負。

**Why this priority**: 遊戲規則的完整性；影響策略判斷。

**Independent Test**: 刻意讓上區總分達到 63，確認計分板顯示 +35 獎勵。

**Acceptance Scenarios**:

1. **Given** 上區已填完，**When** 合計 ≥ 63，**Then** 計分板上區獎勵欄顯示「+35」。
2. **Given** 遊戲結束，**When** 計分板呈現，**Then** 包含：上區小計、獎勵、下區合計、總分，並以顏色或標記標示勝者。

---

### User Story 4 - 新遊戲 / 重新開始 (Priority: P3)

遊戲結束後，玩家可按「再玩一次」回到模式選擇，或直接重新開始相同模式。

**Why this priority**: 基本 UX 流暢度，非核心功能。

**Independent Test**: 遊戲結束後點「再玩一次」，確認所有計分歸零、骰子重置。

**Acceptance Scenarios**:

1. **Given** 遊戲結束，**When** 點「再玩一次」，**Then** 回到模式選擇畫面，所有狀態清除。

---

### Edge Cases

- 已使用的計分類別不可再次點選。
- 第 3 次擲骰後「擲骰」按鈕應被停用。
- 若玩家不符合任何類別（例如 Yacht 沒有五同），點選後該格記為 0 分。
- 遊戲進行中重新整理頁面不需要保留狀態（無需 localStorage 持久化）。

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: 遊戲 MUST 支援 5 顆骰子，每回合最多擲 3 次（含第一次）。
- **FR-002**: 玩家 MUST 能在每次擲骰後點選骰子鎖定（保留），再擲時已鎖定骰子不動。
- **FR-003**: 遊戲 MUST 包含 13 個標準計分類別（上區 6 項 + 下區 7 項，詳見 data-model）。
- **FR-004**: 上區合計 ≥ 63 時 MUST 自動加 35 分獎勵。
- **FR-005**: 遊戲 MUST 支援雙人模式（兩人輪流）及單人對 CPU 模式。
- **FR-006**: CPU MUST 使用自動策略（greedy）完成回合，包含保留骰子與選分類別。
- **FR-007**: 遊戲 MUST 在 13 回合後自動結算並顯示計分板與勝負。
- **FR-008**: 單一 HTML 檔案，無伺服器、無構建步驟，直接以瀏覽器開啟或透過 GitHub Pages 提供。
- **FR-009**: UI 語言為繁體中文，視覺風格與 index.html / betting.html 一致（Tailwind CSS + Noto Sans TC）。

### Key Entities

- **GameState**: 目前回合、現任玩家、每位玩家的計分板、骰子狀態、剩餘擲骰次數。
- **Die**: 點數（1–6）、是否鎖定。
- **Scorecard**: 玩家的 13 個分類得分（null = 未使用，number = 已填入）。
- **Player**: 名稱（玩家一／玩家二 or CPU）、計分板、是否為 CPU。

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 一局 13 回合能完整跑完，計分板數字與手算一致（Yacht 50 分、Full House 25 分、大順 40 分、小順 30 分）。
- **SC-002**: 頁面在 Chrome / Edge / Safari 現代瀏覽器直接開啟可正常遊戲，無 console error。
- **SC-003**: CPU 回合在 2 秒內完成，不阻塞主執行緒（setTimeout 模擬思考延遲 ≤ 800ms）。
- **SC-004**: 在 375px 寬度的行動裝置上計分板與骰子可正常顯示，不溢出。

## Assumptions

- 純前端靜態 HTML，與 index.html / betting.html 同風格（Tailwind CDN + Noto Sans TC）。
- 不需要 localStorage 持久化（重整清空）。
- CPU 使用 greedy 策略即可，無需 Monte Carlo 模擬。
- 使用標準 Yacht 規則（非 Yahtzee）：Yacht = 5 同骰 50 分，無 Joker 規則。
- 玩家名稱固定為「玩家一」、「玩家二」（單人模式為「玩家」vs「CPU」），不需輸入。
- 目標瀏覽器：Chrome 100+、Edge 100+、Safari 15+（ES2022 原生特性可用）。
