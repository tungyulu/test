#!/usr/bin/env python3
"""
golf-tracer.py — 在一般速度（30/60 fps）的高爾夫揮桿影片上畫出球的飛行軌跡（shot tracer）。

用法：
    python3 golf-tracer.py IMG_4086.mov --impact 101 --tee 905,1358
    python3 golf-tracer.py IMG_4086.mov --impact 101 --tee 905,1358 --out tracer.mp4 --no-replay

流程：
  1. 從擊球幀開始，用「與前一幀的正向亮度差」在預測位置附近找球的拖影（連通元件），逐幀追蹤，
     直到球被遮住／太小追不到為止（通常只有擊球後 0.1～0.3 秒）。
  2. 把實測點擬合成透視直線模型 p(t) = (A + B·t) / (1 + c·t)（3D 直線運動的影像投影），
     往後推估最多 1.2 秒，並加上隨時間線性增長的影像重力下垂修正。
  3. 用 ORB 特徵 + RANSAC 把每一幀對齊回擊球幀，讓軌跡跟著手持晃動一起移動。
  4. 疊上發光軌跡（實線＝實測、虛線＝推估）、球標記與說明面板，結尾附 0.25 倍速重播；
     以 libx264 輸出，保留原始音軌。

限制：後方／斜後方視角沒有深度資訊，只能畫方向與形狀，量不出球速；球速請用 golf.html 搭配正面慢動作影片。
相依：pip install opencv-python-headless numpy pillow imageio-ffmpeg
"""
import argparse, subprocess, sys
import cv2, numpy as np

# ---------------------------------------------------------------- args
ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('video')
ap.add_argument('--impact', type=int, required=True, help='擊球瞬間的幀號（0 起算，球剛離開球梯那一幀）')
ap.add_argument('--tee', required=True, help='擊球幀中球的像素座標 x,y')
ap.add_argument('--out', default=None, help='輸出 mp4 路徑（預設：<影片名>_tracer.mp4）')
ap.add_argument('--first-guess', default=None, help='擊球後第一幀球拖影的大約座標 x,y（不給則沿球梯上方大範圍搜尋）')
ap.add_argument('--thresh', type=int, default=22, help='亮度差門檻（預設 22）')
ap.add_argument('--max-track', type=int, default=40, help='最多追蹤幾幀')
ap.add_argument('--extrap', type=float, default=1.2, help='推估延伸秒數（預設 1.2）')
ap.add_argument('--droop', type=float, default=1.3, help='推估段每幀重力下垂像素（預設 1.3；0 = 純直線）')
ap.add_argument('--golfer-box', default='0,150,660,1500', help='排除球員的矩形 x0,y0,x1,y1（相機對齊時忽略此區域的特徵）')
ap.add_argument('--font', default='/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', help='中文字型檔')
ap.add_argument('--no-replay', action='store_true', help='不附慢動作重播')
ap.add_argument('--dry-run', action='store_true', help='只做追蹤與擬合，不輸出影片')
ap.add_argument('--stills', default=None, help='另存幾張靜態圖，逗號分隔幀號，例如 107,150,300')
args = ap.parse_args()

SRC = args.video; IMPACT = args.impact
TEE = tuple(float(v) for v in args.tee.split(','))
OUT = args.out or SRC.rsplit('.', 1)[0] + '_tracer.mp4'

# ---------------------------------------------------------------- load
cap = cv2.VideoCapture(SRC)
if not cap.isOpened(): sys.exit(f'無法開啟 {SRC}')
FPS = cap.get(cv2.CAP_PROP_FPS) or 30.0
frames = []
while True:
    ok, f = cap.read()
    if not ok: break
    frames.append(f)
N = len(frames); H, W = frames[0].shape[:2]
print(f'{SRC}: {N} frames, {W}x{H}, {FPS:.2f} fps')
if not (0 < IMPACT < N - 2): sys.exit('--impact 超出範圍')
gray = lambda n: cv2.cvtColor(frames[n], cv2.COLOR_BGR2GRAY)

def fit_model(pts):
    """pts: list of (frame,x,y,area) → perspective-linear fit p(t)=(A+B t)/(1+c t) through the tee. returns (c, ax, ay, err)"""
    T = np.array([0.0] + [n - IMPACT for n, _, _, _ in pts]); X = np.array([TEE[0]] + [x for _, x, _, _ in pts]); Y = np.array([TEE[1]] + [y for _, _, y, _ in pts])
    best = None
    for c in np.linspace(0.005, 1.5, 600):
        D = 1 + c * T; M = np.stack([1 / D, T / D], 1)
        ax = np.linalg.lstsq(M, X, rcond=None)[0]; ay = np.linalg.lstsq(M, Y, rcond=None)[0]
        err = np.sum((M @ ax - X) ** 2) + np.sum((M @ ay - Y) ** 2)
        if best is None or err < best[0]: best = (err, c, ax, ay)
    err, c, ax, ay = best
    return c, ax, ay, np.sqrt(err / len(T) / 2)
def model_pt(c, ax, ay, t):
    D = 1 + c * t; return ((ax[0] + ax[1] * t) / D, (ay[0] + ay[1] * t) / D)

# ---------------------------------------------------------------- 1. track the ball streak
track = []            # (frame, x, y, area)
if args.first_guess:
    pred = tuple(float(v) for v in args.first_guess.split(',')); R = 170
else:
    pred = (TEE[0], TEE[1] - 220); R = 320       # somewhere above the tee
vel = None; prev = None
for n in range(IMPACT + 1, min(N, IMPACT + 1 + args.max_track)):
    d = cv2.GaussianBlur(cv2.subtract(gray(n), gray(n - 1)), (3, 3), 0)
    _, m = cv2.threshold(d, args.thresh, 255, cv2.THRESH_BINARY)
    x0, x1 = int(max(0, pred[0] - R)), int(min(W, pred[0] + R)); y0, y1 = int(max(0, pred[1] - R)), int(min(H, pred[1] + R))
    win = np.zeros_like(m); win[y0:y1, x0:x1] = m[y0:y1, x0:x1]
    k, lab, st, cen = cv2.connectedComponentsWithStats(win, connectivity=8)
    best = None
    for i in range(1, k):
        a = st[i][4]
        if a < 15 or a > 4000: continue
        cx, cy = cen[i]; md = d[lab == i].mean()
        score = np.hypot(cx - pred[0], cy - pred[1]) + (0 if md > 28 else 60)
        if best is None or score < best[0]: best = (score, cx, cy, int(a))
    if best is None:
        print(f'  frame {n}: 找不到球，追蹤結束'); break
    _, cx, cy, a = best
    if vel is not None:
        step = np.hypot(cx - prev[0], cy - prev[1]); vprev = np.hypot(*vel)
        if step > vprev * 1.6 + 15:
            print(f'  frame {n}: 候選位移不合理，追蹤結束'); break
    if len(track) >= 6 and np.hypot(cx - pred[0], cy - pred[1]) > 40:
        print(f'  frame {n}: 候選點偏離透視模型預測 {np.hypot(cx - pred[0], cy - pred[1]):.0f} px（可能黏到身體），追蹤結束'); break
    if len(track) >= 4 and a > 500 and a > 1.3 * max(t[3] for t in track[-4:-1]):
        print(f'  frame {n}: 拖影面積 {a} 反而變大（遠離的球只會變小，可能黏到身體），追蹤結束'); break
    track.append((n, float(cx), float(cy), a))
    print(f'  frame {n}: ball streak at ({cx:.0f},{cy:.0f}) area {a}')
    vel = (cx - (prev[0] if prev else TEE[0]), cy - (prev[1] if prev else TEE[1])); prev = (cx, cy)
    if len(track) >= 6:   # once the model is constrained, predict from it (a receding ball only slows down)
        good_now = [t for t in track if t[3] >= 250] or track
        c_, ax_, ay_, _ = fit_model(good_now); pred = model_pt(c_, ax_, ay_, n + 1 - IMPACT); R = 60
    else:
        pred = (cx + vel[0] * 0.8, cy + vel[1] * 0.8); R = max(60, np.hypot(*vel) * 0.7 + 40)
if len(track) < 3: sys.exit('追蹤到的幀太少（<3），請用 --first-guess 指定第一幀球的位置，或調低 --thresh')
good = [t for t in track if t[3] >= 250] or track          # drop partial (tiny) streaks for the fit
print('用於擬合的幀:', [t[0] for t in good])

# ---------------------------------------------------------------- 2. perspective-linear fit + extrapolation
c, ax, ay, rms = fit_model(good)
T_MEAS = track[-1][0] - IMPACT; T_END = T_MEAS + int(FPS * args.extrap)
def P(t):
    t = np.asarray(t, dtype=float); D = 1 + c * t
    q = np.stack([(ax[0] + ax[1] * t) / D, (ay[0] + ay[1] * t) / D], -1)
    q[..., 1] += args.droop * np.clip(t - T_MEAS, 0, None)
    return q
print(f'fit: c={c:.4f} rms={rms:.1f}px  measured {T_MEAS} frames ({T_MEAS / FPS:.2f}s), extrapolate to {T_END} frames')
if args.dry_run: sys.exit(0)

# ---------------------------------------------------------------- 3. camera alignment (ORB + RANSAC similarity to impact frame)
gx0, gy0, gx1, gy1 = (int(v) for v in args.golfer_box.split(','))
mask = np.full((H, W), 255, np.uint8); mask[gy0:gy1, gx0:gx1] = 0
orb = cv2.ORB_create(3000); bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
kref, dref = orb.detectAndCompute(gray(IMPACT), mask)
Mx = [np.eye(2, 3) for _ in range(N)]; last = np.eye(2, 3)
for n in range(IMPACT + 1, N):
    k, d = orb.detectAndCompute(gray(n), mask)
    if d is not None and len(k) > 20:
        m = bf.match(dref, d)
        if len(m) >= 20:
            src = np.float32([kref[x.queryIdx].pt for x in m]); dst = np.float32([k[x.trainIdx].pt for x in m])
            A, inl = cv2.estimateAffinePartial2D(src, dst, method=cv2.RANSAC, ransacReprojThreshold=4.0)
            if A is not None and inl is not None and inl.sum() >= 12: last = A
    Mx[n] = last
def warp(pts, n):
    pts = np.asarray(pts, dtype=np.float64).reshape(-1, 2); A = Mx[n]
    return pts @ A[:, :2].T + A[:, 2]

# ---------------------------------------------------------------- 4. render
try:
    from PIL import Image, ImageDraw, ImageFont
    FONT_B = ImageFont.truetype(args.font, 46); FONT_S = ImageFont.truetype(args.font, 30)
except Exception as e:
    print('字型載入失敗，改用無面板模式:', e); FONT_B = None
COL = (40, 215, 255)   # BGR warm yellow
def draw_trail(img, t_now, n):
    if t_now <= 0: return img
    layer = np.zeros_like(img)
    tm = min(t_now, T_MEAS)
    pts = warp(P(np.arange(0, tm + 1e-9, 0.25)), n).astype(np.int32).reshape(-1, 1, 2)
    cv2.polylines(layer, [pts], False, COL, 7, cv2.LINE_AA)
    if t_now > T_MEAS:
        ps = warp(P(np.arange(T_MEAS, min(t_now, T_END) + 1e-9, 0.25)), n)
        for i in range(0, len(ps) - 1, 12):
            seg = ps[i:i + 7].astype(np.int32).reshape(-1, 1, 2)
            if len(seg) > 1: cv2.polylines(layer, [seg], False, (120, 230, 255), 4, cv2.LINE_AA)
    out = cv2.addWeighted(img, 1.0, cv2.GaussianBlur(layer, (0, 0), 9), 0.9, 0)
    out = np.clip(out.astype(np.int16) + layer, 0, 255).astype(np.uint8)
    if t_now <= T_END:
        p = tuple(warp(P(t_now), n)[0].astype(int))
        if t_now <= T_MEAS: cv2.circle(out, p, 11, (255, 255, 255), -1, cv2.LINE_AA); cv2.circle(out, p, 14, COL, 3, cv2.LINE_AA)
        else: cv2.circle(out, p, 12, (255, 255, 255), 2, cv2.LINE_AA)
    return out
def panel(img, lines):
    if FONT_B is None: return img
    y0 = H - 90 - (70 + len(lines) * 42)          # bottom of frame, so it never covers the far end of the trail
    pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)); d = ImageDraw.Draw(pil, 'RGBA')
    d.rounded_rectangle((40, y0, W - 40, y0 + 70 + len(lines) * 42), radius=18, fill=(8, 12, 20, 185))
    d.text((64, y0 + 14), 'Ball Tracer', font=FONT_B, fill=(34, 211, 238, 255))
    for i, (s, fill) in enumerate(lines): d.text((64, y0 + 76 + i * 42), s, font=FONT_S, fill=fill)
    return cv2.cvtColor(np.array(pil), cv2.COLOR_RGB2BGR)
def render(n, slow=False):
    img = frames[n].copy(); t = n - IMPACT
    if -30 <= t < 0: cv2.circle(img, (int(TEE[0]), int(TEE[1]) - 6), 22, COL, 2, cv2.LINE_AA)
    if t >= 0: img = draw_trail(img, t, n)
    if t < 0: lines = [('等待擊球…', (203, 213, 225, 255))]
    elif t <= T_MEAS: lines = [(f'擊球後 {t / FPS * 1000:4.0f} ms · 影片逐幀追蹤中（第 {t} 幀）', (255, 215, 40, 255))]
    elif t <= T_END: lines = [(f'擊球後 {t / FPS * 1000:4.0f} ms · 球已追不到，虛線為推估（透視直線＋重力修正）', (150, 220, 255, 255))]
    else: lines = [(f'實線＝影片實測 {T_MEAS} 幀（{T_MEAS / FPS:.2f} s）· 虛線＝推估延伸', (203, 213, 225, 255))]
    lines.append((f'一般速度 {FPS:.0f} fps 影片：可畫出方向與軌跡，無法量出球速', (150, 160, 180, 255)))
    if slow: lines.append(('SLOW-MO REPLAY ×0.25', (34, 211, 238, 255)))
    return panel(img, lines)

try:
    import imageio_ffmpeg; ff = imageio_ffmpeg.get_ffmpeg_exe()
except Exception: ff = 'ffmpeg'
REPLAY = [] if args.no_replay else list(range(max(0, IMPACT - 8), min(N, IMPACT + T_MEAS + 40))); HOLD = 0 if args.no_replay else 20
total = N + HOLD + 4 * len(REPLAY); dur = total / FPS
cmd = [ff, '-y', '-hide_banner', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', f'{FPS:.3f}', '-i', 'pipe:0',
       '-i', SRC, '-map', '0:v', '-map', '1:a?', '-af', f'apad=whole_dur={dur:.3f}', '-c:v', 'libx264', '-preset', 'medium', '-crf', '19',
       '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', OUT]
p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
for n in range(N): p.stdin.write(render(n).tobytes())
for _ in range(HOLD): p.stdin.write(render(N - 1).tobytes())
for n in REPLAY:
    f = render(n, slow=True)
    for _ in range(4): p.stdin.write(f.tobytes())
p.stdin.close(); p.wait()
print('寫出', OUT, f'({total} frames, {dur:.1f}s)', 'ffmpeg exit', p.returncode)
if args.stills:
    for k in (int(v) for v in args.stills.split(',')):
        path = OUT.rsplit('.', 1)[0] + f'_f{k}.jpg'; cv2.imwrite(path, render(k), [cv2.IMWRITE_JPEG_QUALITY, 90]); print('靜態圖', path)
