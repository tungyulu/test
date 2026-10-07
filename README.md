# test

我的小工具 — 純靜態網頁集合，直接用瀏覽器開即可。

🔗 **線上版：https://tungyulu.github.io/test/index.html**

## 頁面

| 頁面 | 說明 |
| --- | --- |
| [index.html](https://tungyulu.github.io/test/index.html) | 小工具首頁導覽 |
| [trip.html](https://tungyulu.github.io/test/trip.html) | 關東秋季紅葉巡航 · 8 天 7 夜自駕行程 |
| [betting.html](https://tungyulu.github.io/test/betting.html) | 世界盃運彩投注紀錄 · 複式串關盈虧計算 |
| [yacht.html](https://tungyulu.github.io/test/yacht.html) | 快艇骰子 · 5 顆骰子 13 類別計分 |
| [usage.html](https://tungyulu.github.io/test/usage.html) | Claude Code 方案額度儀表板 |
| [dyson.html](https://tungyulu.github.io/test/dyson.html) | Dyson 選購 · 四家 AI 交叉比對報告 |
| [invest.html](https://tungyulu.github.io/test/invest.html) | 投資作戰表 · 2026 年 9～12 月 |
| [congress-trades.html](https://tungyulu.github.io/test/congress-trades.html) | 國會交易日報 · 美國國會議員的股票交易申報（資料來自 Kadoa 整理的眾議院／參議院公開申報，每天更新）：依公布日排列、標出上次打開之後的新申報、追蹤議員和股票代號、近 30 天最多議員買賣的股票 |
| [golf.html](https://tungyulu.github.io/test/golf.html) | 高爾夫揮桿分析 · 丟入手機影片自動找擊球瞬間、量下桿節奏推估桿頭速度與飛行距離，能追到球時疊上 tracer；另有正面慢動作手動量測 |
| [blackjack.html](https://tungyulu.github.io/test/blackjack.html) | 21點機率決策挑戰 · 隨機牌局練基本策略，對照策略表計分 |
| [blackjack-game.html](https://tungyulu.github.io/test/blackjack-game.html) | 21點實戰牌桌 · 同一套規則實際開打：虛擬籌碼下注（主注＋完美對子／21+3 副注）、可加 1–4 位照基本策略打的電腦玩家、6 副牌靴、策略教練、即時機率與 Hi-Lo 算牌，數據面板可開關 |
| [nba-auction.html](https://tungyulu.github.io/test/nba-auction.html) | NBA Fantasy 拍賣選秀板（2026-27）· 乾淨的 fantasy 數據 app 版面（淺色／深色）· 傳統 9 項、14 隊每隊 $200、11 先發＋3 板凳：約 240 位球員的建議價與推薦指數、九項熱度圖、punt 重算；選秀後改成聯盟模式：我的戰力與弱項、14 隊戰力（每週贏幾類、每週輸贏 $）、交易試算、推薦的一換一與自由球員（存本機） |
| [yotei.html](https://tungyulu.github.io/test/yotei.html) | 羊蹄山戰鬼（Ghost of Yōtei）收集清單 · 依類別／地區逐項打勾（存本機），未完成的點名稱開對應攻略頁（繁中／簡中／英文可切換）；iPhone 建議 Safari「分享 → 加入主畫面」，進度才不會被 Safari 7 天清除 |
| [tamagotchi.html](https://tungyulu.github.io/test/tamagotchi.html) | 塔麻可吉樂園（Tamagotchi Paradise）攻略 · 照機台旋鈕的四個視角排：選機台、行星等級、每月活動日曆、尋蛋、照顧與龍捲風、結婚與隱藏角色，加上六個場地的完整進化表（可搜尋角色）、實驗室碼與商店碼 |

## golf-tracer.py

在一般速度（30/60 fps）揮桿影片上畫出球的飛行軌跡（shot tracer）並輸出 mp4；適合後方／斜後方視角、球一兩幀就飛遠的影片。需要 Python 3 與 `pip install opencv-python-headless numpy pillow imageio-ffmpeg`。

```bash
python3 golf-tracer.py IMG_4086.mov --impact 101 --tee 905,1358          # 擊球幀號、該幀球的像素座標
python3 golf-tracer.py IMG_4086.mov --impact 101 --tee 905,1358 --dry-run # 只看追蹤與擬合結果
```

只能畫方向與軌跡，量不出球速；要量球速請用 `golf.html` 搭配正面 240 fps 慢動作影片。

## usage-dashboard.js

終端機版的額度儀表板（Node 18+，零相依）：

```bash
node usage-dashboard.js            # 持續更新
node usage-dashboard.js --once     # 只跑一次
node usage-dashboard.js --interval 5
```
