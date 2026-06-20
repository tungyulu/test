# Research: 快艇骰子遊戲

## Decision: 遊戲規則（Yacht vs Yahtzee）

- **Decision**: 使用標準 Yacht 規則（Yacht 骰子的原始版本，也是 Nintendo 51 Worldwide Games 所採用的規則）。
- **Rationale**: 51 Worldwide Games 使用 Yacht（ヤット）規則：沒有 Joker 規則、Yacht（五同）固定 50 分、Full House 固定 25 分、Small Straight 固定 30 分、Large Straight 固定 40 分。Yahtzee（Hasbro 商標版）有額外 Joker 規則讓 Yahtzee 可代替任何下區類別，但 51 Worldwide Games 沒有此規則。
- **Alternatives considered**: 使用 Yahtzee 規則 → 增加 Joker 邏輯複雜度，且與目標遊戲不符。

## Decision: 技術棧

- **Decision**: 純 HTML + 內嵌 CSS（Tailwind CDN）+ 內嵌 JavaScript（vanilla ES2022），單一 `yacht.html` 檔案。
- **Rationale**: 與 index.html 和 betting.html 架構完全一致；不需要打包工具或伺服器；GitHub Pages 直接提供靜態檔案。
- **Alternatives considered**: React/Vue 元件 → 需要構建步驟，與現有頁面模式不符。

## Decision: CPU 策略

- **Decision**: Greedy 策略 — 每次擲骰後計算所有可用類別的「即時分數」，保留對最高分類別最有貢獻的骰子；最終選分時選即時分數最高的類別。
- **Rationale**: 實作簡單，對休閒玩家已構成有趣挑戰，不需要複雜的機率計算（Monte Carlo 或 dp 表）。CPU 回合延遲 800ms 模擬思考，保持流暢 UX。
- **Alternatives considered**: Monte Carlo 期望值計算 → 高複雜度，且對單一 HTML 檔案不合適；Random 策略 → 太弱，無挑戰性。

## Decision: 骰子動畫

- **Decision**: CSS keyframe 動畫（抖動 + 翻轉）約 400ms，用 Unicode 骰子符號（⚀⚁⚂⚃⚄⚅）或 SVG 圖形呈現骰面。
- **Rationale**: 純 CSS 動畫不依賴外部資源；骰子符號在所有目標瀏覽器均支援。最終選擇 SVG 骰面（點陣圖案）以確保視覺清晰。
- **Alternatives considered**: Canvas 動畫 → 過複雜；`<img>` 引用外部圖片 → GitHub Pages CSP / 外部依賴問題。

## Decision: 計分板佈局

- **Decision**: 雙欄表格（玩家一 | 玩家二），垂直列為 13 個類別加小計列；行動裝置縮小字型並允許表格橫向捲動。
- **Rationale**: 51 Worldwide Games 採用相同的雙欄計分板佈局，直觀且玩家熟悉。
- **Alternatives considered**: 分頁顯示各玩家計分板 → 無法同時對比分數，降低競爭感。

## Decision: 骰子鎖定互動

- **Decision**: 點擊骰子切換鎖定/解鎖（locked dice 有明顯邊框和半透明遮罩）；第一次擲骰前不可點選；已使用完 3 次擲骰次數後不可解鎖/鎖定。
- **Rationale**: 符合 51 Worldwide Games 的互動方式。
- **Alternatives considered**: 拖曳到「保留區」→ 在行動裝置上手勢複雜；觸控不如點擊直觀。

## Decision: 狀態管理

- **Decision**: 單一 `state` 物件，每次狀態變更後呼叫 `render()` 重繪整個 UI（與 betting.html 相同模式）。
- **Rationale**: 無框架、邏輯集中、容易 debug。遊戲狀態簡單，不需要細粒度的差量更新。
- **Alternatives considered**: Pub/Sub 事件系統 → 過度工程化；多個全域變數 → 難以追蹤狀態。

## Resolved Clarifications

| 原始疑問 | 解決方案 |
|----------|----------|
| Yacht vs Yahtzee 規則？ | Yacht（仿 Nintendo 51）：無 Joker，固定分數 |
| CPU 策略複雜度？ | Greedy 即可，延遲 800ms 模擬思考 |
| 骰子呈現方式？ | SVG 點陣骰面（內嵌於 HTML）|
| 需要 localStorage？ | 否，不持久化 |
| 需要音效？ | 否（瀏覽器 Web Audio 沙盒限制，GitHub Pages 不適合） |
| 玩家名稱輸入？ | 否，固定名稱 |
