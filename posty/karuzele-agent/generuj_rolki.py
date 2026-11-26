# 5 rolek 9:16 (1080x1920, 30 fps, H.264 + cisza AAC 48 kHz) z treści karuzel o pracy agenta.
# Styl i funkcje z generuj_karuzele.py (import; wysokość kadru podmieniana na 1920 – slajdy JPG nietknięte).
# Bez twarzy (CLAUDE.md, Rolki): bez portretu i podpisu; „przesuń” i numeracja n/5 pominięte.
# Sceny: hook 3,5 s, 3 x 4 s, pytanie + CTA 3 s, plansza końcowa 3,5 s; przenikanie 0,35 s,
# karty wjeżdżają kolejno (fade + slide), tło z wolnym zoomem pod nieruchomym tekstem.
# Muzykę dodaje się w CapCut / bibliotece Meta i TikTok (brak licencjonowanego utworu w repo).
# Uruchom: python3 posty/karuzele-agent/generuj_rolki.py [katalog-klatek-kontrolnych]
from PIL import Image, ImageDraw
from multiprocessing import Pool
import numpy as np
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generuj_karuzele as gk  # noqa: E402

W, H, FPS = 1080, 1920, 30
gk.H = H                                    # funkcje karuzel czytają W/H z modułu w chwili wywołania
SAFE_TOP, SAFE_BOT, SAFE_R = 250, 1500, 960   # strefa bezpieczna Reels/TikTok na ważny tekst
DUR = [3.5, 4.0, 4.0, 4.0, 3.0, 3.5]
XF, REVEAL, STEP, SLIDE = 0.35, 0.35, 0.45, 40   # przenikanie, wjazd karty, odstęp kart, przesunięcie px
ZOOM = 1.06                                  # zoom tła od 1.00 do 1.06 przez całą rolkę
# scena 5: (podpis pod pytaniem albo None, tekst złotej pigułki CTA)
CTA5 = {
    '01-zanim-pokaze': (None, 'Proszę napisać w komentarzu'),
    '02-pytania-do-agenta': (None, 'Proszę napisać w komentarzu'),
    '03-zdjecia-30-minut': (None, 'Proszę napisać „PORADNIK”'),
    '04-wylacznosc-mity': (None, 'Proszę napisać w komentarzu'),
    '05-dokumenty': ('Pomogę.', 'Proszę napisać wiadomość'),
}
_txts_checked = gk.txts


def _txts_plain(img, d, items):
    for xy, s, f, fill in items:
        d.text(xy, s, font=f, fill=fill, features=gk.feat(f))


def layer(draw, ref_bg):
    """Rysuje treść 3 razy: na prawdziwym tle (assert kontrastu 4.5:1), na czarnym i na białym –
    z różnicy wychodzi warstwa (kolor premultiplied + alfa), którą można kłaść na ruchome tło.
    Zwraca (P, A, pasy kart w pionie)."""
    boxes, card0 = [], gk.card

    def card_rec(img, box, *a, **kw):
        boxes.append((int(box[1]), int(box[3])))
        card0(img, box, *a, **kw)
    gk.card = card_rec
    real = ref_bg.copy()
    draw(real, ImageDraw.Draw(real))
    gk.card, gk.txts = card0, _txts_plain
    try:
        out = []
        for c in (0, 255):
            im = Image.new('RGB', (W, H), (c, c, c))
            draw(im, ImageDraw.Draw(im))
            out.append(np.asarray(im, np.float32))
    finally:
        gk.txts = _txts_checked
    s0, s1 = out
    A = np.clip(1 - (s1 - s0).mean(2) / 255, 0, 1)
    rec = s0 + np.asarray(ref_bg, np.float32) * (1 - A[..., None])
    assert np.abs(rec - np.asarray(real, np.float32)).max() <= 3, 'warstwa nie odtwarza kadru'
    return s0, A, [(max(0, a - 2), min(H, b + 2)) for a, b in boxes]


def safe_check(A, bands, name):
    # treść (alfa > 0) tylko w pasie bezpiecznym; karty mogą sięgać x=1000, tekst kończy się na x=944
    ys = np.where(A.max(1) > 0.01)[0]
    assert ys.min() >= SAFE_TOP - 30 and ys.max() <= SAFE_BOT, f'{name}: treść poza strefą y {ys.min()}–{ys.max()}'
    assert gk.M + gk.PAD + gk.IW <= SAFE_R, 'tekst poza strefą x'


def reel_header(img, d):
    """Małe logo w lewym górnym rogu + nazwa marki (bez numeracji n/5)."""
    ls, x, y = 110, 60, 140
    li, lm = gk.logo(ls, gk.DARK)
    img.paste(li, (x, y), lm)
    fb = gk.F(gk.M700, 22)
    s = 'NIERUCHOMOŚCI BEZ STRESU'
    bb = d.textbbox((0, 0), s, font=fb)
    gk.txt(img, d, (x + ls + 20, y + (ls - (bb[3] - bb[1])) / 2 - bb[1]), s, fb, gk.WHITE)


def endboard(img, d):
    """Plansza końcowa: logo-ciemne-tlo + baner kontaktowy (oryginalne proporcje) + adres strony, na środku strefy."""
    pad, ls, bw = 30, 260, 840
    ban = Image.open(gk.BANER).convert('RGB')
    bh = round(bw * ban.height / ban.width)
    fu = gk.F(gk.M700, 40)
    url = 'nieruchomosci-bez-stresu.org'
    ch = pad + ls + 30 + bh + 30 + 48 + pad
    y0 = round((SAFE_TOP + SAFE_BOT - ch) / 2)
    x0 = (W - bw) // 2 - pad
    gk.card(img, (x0, y0, W - x0, y0 + ch), alpha=1, r=28, color=gk.DARK)
    li, lm = gk.logo(ls, gk.DARK)   # lum(DARK) < 0.4 -> logo-ciemne-tlo.webp
    img.paste(li, ((W - ls) // 2, y0 + pad), lm)
    by = y0 + pad + ls + 30
    img.paste(ban.resize((bw, bh), Image.LANCZOS), ((W - bw) // 2, by))
    gk.txt(img, d, ((W - gk.tw(fu, url)) / 2, by + bh + 26), url, fu, gk.GOLD)


def scene_draw(k, spec):
    kind = spec[0]
    if kind == 'hook':
        _, head, sub, cta, icon = spec
        cards = [[gk.Hd(head, 112, 60, 460), gk.G(28), gk.R()],
                 [gk.T(sub, gk.M700, 58, 36)],
                 [gk.CTA(cta, icon)]]
    elif kind == 'end':
        _, q, _ = spec
        sub, cta = CTA5[k['dir']]
        first = [gk.Hd(q, 96, 56, 420)]
        if sub:
            first += [gk.G(28), gk.R(), gk.G(28), gk.T(sub, gk.M500, 52, 32)]
        cards = [first, [gk.CTA(cta, 'arrow')]]
    else:
        cards = spec[1]
    return lambda img, d: gk.stack(img, d, cards, SAFE_TOP + 20, SAFE_BOT - 20, gap=40)


def list_slide_reel(head, items):
    # nagłówek i lista jako osobne karty – lista wjeżdża po nagłówku
    return ('cards', [[gk.Hd(head, 104, 56), gk.G(30), gk.R()], [gk.L(items, 48)]])


def bg_big(k):
    # to samo tło co w karuzelach (gradient + ziarno), większe o ZOOM pod wolne zbliżenie
    gk.W, gk.H = round(W * ZOOM), round(H * ZOOM)
    try:
        return gk.background(*k['c'], k['seed'] * 10 + 1)
    finally:
        gk.W, gk.H = W, H


def bg_frame(big, t, total):
    z = 1 + (ZOOM - 1) * t / total
    cw, chh = big.width / z, big.height / z
    x0, y0 = (big.width - cw) / 2, (big.height - chh) / 2
    return big.resize((W, H), Image.BICUBIC, box=(x0, y0, x0 + cw, y0 + chh))


def ease(u):
    u = min(max(u, 0.0), 1.0)
    return 1 - (1 - u) ** 3


def build(k):
    gk.list_slide = list_slide_reel
    specs = k['slides']()
    total = sum(DUR)
    starts = np.concatenate([[0], np.cumsum(DUR)[:-1]])
    big = bg_big(k)
    scenes = []
    for s, spec in enumerate(specs + [('board',)]):
        ref = bg_frame(big, starts[s] + 1, total)
        dr = endboard if spec[0] == 'board' else scene_draw(k, spec)
        P, A, bands = layer(dr, ref)
        safe_check(A, bands, f"{k['dir']} scena {s + 1}")
        scenes.append((P, A, bands))
    hP, hA, _ = layer(reel_header, bg_frame(big, 0, total))
    return big, starts, total, scenes, (hP, hA)


def compose(t, big, starts, total, scenes, head):
    out = np.asarray(bg_frame(big, t, total), np.float32).copy()

    def put(P, A, y0, y1, o, dy=0):
        if o <= 0:
            return
        a = A[y0:y1, :, None] * o
        out[y0 + dy:y1 + dy] = out[y0 + dy:y1 + dy] * (1 - a) + P[y0:y1] * o
    last = len(scenes) - 1
    put(*head, 0, H, 1 - ease((t - starts[last]) / XF))
    for s, (P, A, bands) in enumerate(scenes):
        a, b = starts[s], starts[s] + DUR[s]
        if t < a or (s < last and t > b + XF):
            continue
        o_out = 1.0 if s == last else 1 - ease((t - b) / XF)
        for i, (y0, y1) in enumerate(bands):
            r = 1.0 if (s == 0 and i == 0) else ease((t - a - (i * STEP if s else (i - 1) * STEP + 0.4)) / REVEAL)
            dy = round(SLIDE * (1 - r))
            put(P, A, y0, min(y1, H - dy), r * o_out, dy)
    return np.clip(out + 0.5, 0, 255).astype(np.uint8)


def make(i):
    k = gk.KARUZELE[i]   # indeks, bo słowniki karuzel mają lambdy (nie da się ich przekazać do procesu)
    big, starts, total, scenes, head = build(k)
    out = os.path.join(gk.OUT, k['dir'])
    compose_args = (big, starts, total, scenes, head)
    Image.fromarray(compose(1.6, *compose_args)).save(os.path.join(out, 'okladka-rolki.jpg'), quality=92)
    cmd = ['ffmpeg', '-y', '-loglevel', 'error',
           '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
           '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo',
           '-map', '0:v', '-map', '1:a', '-shortest',
           '-vf', 'scale=out_color_matrix=bt709:out_range=tv,format=yuv420p',
           '-c:v', 'libx264', '-preset', 'slow', '-crf', '19', '-profile:v', 'high',
           '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
           '-c:a', 'aac', '-b:a', '128k', '-ar', '48000', '-ac', '2',
           '-movflags', '+faststart', os.path.join(out, 'rolka.mp4')]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for n in range(round(total * FPS)):
        p.stdin.write(compose(n / FPS, *compose_args).tobytes())
    p.stdin.close()
    assert p.wait() == 0, f"ffmpeg: {k['dir']}"
    return k['dir'], [float(round(a + min(d - 0.5, 2.2), 2)) for a, d in zip(starts, DUR)], len(gk.CHECKS)


if __name__ == '__main__':
    with Pool(min(5, os.cpu_count() or 1)) as pool:
        for name, times, n in pool.map(make, range(len(gk.KARUZELE))):
            print(name, 'ok; klatki kontrolne [s]:', times, '; sprawdzonych tekstów:', n)
