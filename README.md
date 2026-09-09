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
| [golf.html](https://tungyulu.github.io/test/golf.html) | 高爾夫球軌跡追蹤 · 慢動作影片逐幀追蹤球／桿頭，物理模型模擬飛行 |

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
