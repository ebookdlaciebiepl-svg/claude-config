# Render rolki MURARSKA 'pojawia sie' (przed/po), 1080x1920, 30 fps -> surowe klatki RGB na stdout (do ffmpeg).
# Uzycie: python3 -I render_rolka.py ZRODLA_DIR FONTY_DIR CENA > raw   (CENA="" = bez ceny)
import sys
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageOps, ImageFilter

SRC, FONTS, CENA = sys.argv[1], sys.argv[2], sys.argv[3]
W, H, FPS, DUR = 1080, 1920, 30, 27.5
N = int(DUR * FPS)
GOLD, BLACK, LIGHT = (206, 168, 82), (20, 12, 12), (243, 235, 221)
LOGO = '/home/user/claude-config/assets/logo/logo-ciemne-tlo.webp'
BANER = '/home/user/claude-config/assets/baner/baner-kontakt.webp'

def font(name, size): return ImageFont.truetype(f'{FONTS}/{name}.ttf', size)
SERIF = lambda s: font('cormorant-garamond-700', s)
SANS = lambda s: font('montserrat-500', s)
SANSB = lambda s: font('montserrat-700', s)

ZMAX = 1.10
def load_cover(name):
    im = ImageEnhance.Color(Image.open(f'{SRC}/{name}').convert('RGB')).enhance(0.9)  # cieplo, bez przesycenia
    s = max(H * ZMAX / im.height, W * ZMAX / im.width)  # cover: wypelnia kadr, proporcje zachowane
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    cw, ch = round(W * ZMAX), round(H * ZMAX)
    x0, y0 = (im.width - cw) // 2, (im.height - ch) // 2
    return im.crop((x0, y0, x0 + cw, y0 + ch))

def kenburns(base, p):
    # p 0..1: najazd 1.00 -> 1.10, subpikselowo (EXTENT) -> brak drgan
    z = 1 + (ZMAX - 1) * p
    bw, bh = base.width / z, base.height / z
    x0, y0 = (base.width - bw) / 2, (base.height - bh) / 2
    return base.transform((W, H), Image.EXTENT, (x0, y0, x0 + bw, y0 + bh), Image.BICUBIC)

def reveal(img, t):
    # "pojawia sie": pierwsze 0,7 s ujecia z szarosci/ciemnosci do koloru
    a = min(1, t / 0.7)
    if a >= 1: return img
    g = ImageEnhance.Brightness(ImageOps.grayscale(img).convert('RGB')).enhance(0.75)
    return Image.blend(g, img, a * a * (3 - 2 * a))

# logo w rogu: maska kola (logo jest okragle), bez zmian kolorow i proporcji
logo_src = Image.open(LOGO).convert('RGB')
def logo_round(size):
    l = logo_src.resize((size, size), Image.LANCZOS)
    m = Image.new('L', (size * 4, size * 4), 0)
    ImageDraw.Draw(m).ellipse((4, 4, size * 4 - 4, size * 4 - 4), fill=255)
    return l, m.resize((size, size), Image.LANCZOS)
LOGO_S, LOGO_M = logo_round(150)

def text_w(d, s, f): return d.textlength(s, font=f)

def caption(img, title, sub, t):
    # skrzynka napisu jak we wzorcu (srodek, ~2/3 wysokosci), w barwach marki
    a = max(0, min(1, t / 0.3))
    ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    fs, size = SANS(40), 78
    while True:  # zmniejsz tytul, az skrzynka zmiesci sie w kadrze (max 1000 px)
        ft = SERIF(size)
        if max(text_w(d, l, ft) for l in title) + 100 <= 1000: break
        size -= 2
    lines = [(l, ft, GOLD) for l in title] + [(l, fs, LIGHT) for l in sub]
    hs = [ (86 if f is ft else 54) for _, f, _ in lines ]
    bw = max(text_w(d, l, f) for l, f, _ in lines) + 100
    bh = sum(hs) + 60
    y = 1240 + round((1 - a) * 20)
    x0 = (W - bw) / 2
    d.rounded_rectangle((x0, y, x0 + bw, y + bh), 18, fill=BLACK + (round(215 * a),), outline=GOLD + (round(255 * a),), width=3)
    yy = y + 30
    for (l, f, c), h in zip(lines, hs):
        d.text((W / 2, yy + h / 2), l, font=f, fill=c + (round(255 * a),), anchor='mm'); yy += h
    img.paste(ov, (0, 0), ov)

def data_board(img, t):
    img = ImageEnhance.Brightness(img.filter(ImageFilter.GaussianBlur(6))).enhance(0.35)
    ov = Image.new('RGBA', (W, H), BLACK + (120,)); d = ImageDraw.Draw(ov)
    def fade(t0): return round(255 * max(0, min(1, (t - t0) / 0.35)))
    y = 330
    d.text((W / 2, y), 'MIESZKANIE WŁASNOŚCIOWE', font=SANSB(38), fill=LIGHT + (fade(0),), anchor='mm')
    d.text((W / 2, y + 90), 'UL. MURARSKA', font=SERIF(104), fill=GOLD + (fade(0),), anchor='mm')
    d.text((W / 2, y + 180), 'Wrocław, Fabryczna', font=SANS(44), fill=LIGHT + (fade(0),), anchor='mm')
    d.line((340, y + 250, 740, y + 250), fill=GOLD + (fade(0),), width=3)
    rows = [('Powierzchnia', '42 m²'), ('Pokoje', '2'), ('Piętro', '3. (bez windy)'), ('Stan', 'do remontu'), ('Dostępne', 'od zaraz')]
    yy = y + 330
    for i, (k, v) in enumerate(rows):
        a = fade(0.2 + 0.15 * i)
        d.text((150, yy), k, font=SANS(46), fill=LIGHT + (a,), anchor='lm')
        d.text((930, yy), v, font=SANSB(50), fill=GOLD + (a,), anchor='rm')
        yy += 92
    if CENA:
        a = fade(1.0)
        d.text((W / 2, yy + 70), 'CENA', font=SANSB(36), fill=LIGHT + (a,), anchor='mm')
        d.text((W / 2, yy + 150), CENA, font=SANSB(96), fill=GOLD + (a,), anchor='mm')
        yy += 230
    a = fade(2.0)
    d.text((W / 2, yy + 80), 'Zapraszamy na prezentację –', font=SANSB(44), fill=LIGHT + (a,), anchor='mm')
    d.text((W / 2, yy + 140), 'proszę zadzwonić lub napisać.', font=SANSB(44), fill=LIGHT + (a,), anchor='mm')
    img = img.convert('RGBA'); img.alpha_composite(ov); return img.convert('RGB')

def end_board(t):
    img = Image.new('RGB', (W, H), BLACK); d = ImageDraw.Draw(img)
    L, M = logo_round(600); img.paste(L, ((W - 600) // 2, 330), M)
    b = Image.open(BANER).convert('RGB')
    bw = 1000; b = b.resize((bw, round(b.height * bw / b.width)), Image.LANCZOS)  # proporcje zachowane
    img.paste(b, ((W - bw) // 2, 1080))
    d.text((W / 2, 1380), 'nieruchomosci-bez-stresu.org', font=SANS(40), fill=GOLD, anchor='mm')
    a = min(1, t / 0.4)
    return Image.blend(Image.new('RGB', (W, H), BLACK), img, a)


def viz_label(img):
    # wymog uczciwosci oferty: stale oznaczenie na kazdym ujeciu "po"
    d = ImageDraw.Draw(img); f = SANSB(30); s = 'WIZUALIZACJA ARANŻACJI'
    w = text_w(d, s, f)
    d.rounded_rectangle((48, 140, 48 + w + 44, 140 + 64), 12, fill=BLACK, outline=GOLD, width=2)
    d.text((48 + 22 + w / 2, 172), s, font=f, fill=GOLD, anchor='mm')

def ease(x): x = max(0, min(1, x)); return x * x * (3 - 2 * x)

def wipe(a, b, p):
    # "pojawia sie": odsloniecie od lewej z miekka krawedzia i zlota linia
    if p <= 0: return a
    if p >= 1: return b
    x = ease(p) * (W + 120) - 60
    m = Image.new('L', (W, 1), 0)
    m.putdata([round(255 * max(0, min(1, (x - i) / 60 + 0.5))) for i in range(W)])
    out = Image.composite(b, a, m.resize((W, H)))
    ImageDraw.Draw(out).rectangle((x - 2, 0, x + 2, H), fill=GOLD)
    return out

A = ''  # pliki wzgledem SRC (argv[1])
WIPE = 0.8
# (start, koniec, przed, po, czas przejscia od startu, [(od, tytul, podpis)])
SEGS = [
    (0.0, 6.0, 'pokoj-1-przed.jpg', 'pokoj-1-po.jpg', 2.5,
     [(0.0, ['42 M² – POTENCJAŁ,', 'KTÓRY WIDAĆ'], ['Proszę zobaczyć, jak może wyglądać']),
      (2.5, ['SALON'], ['dobrze doświetlony pokój'])]),
    (6.0, 10.5, 'pokoj-2-przed.jpg', 'pokoj-2-po.jpg', 1.5, [(0.0, ['SYPIALNIA'], ['drugi niezależny, jasny pokój'])]),
    (10.5, 15.0, 'kuchnia-przed.jpg', 'kuchnia-po.jpg', 1.5, [(0.0, ['KUCHNIA'], ['ustawna, symetryczna', 'łatwa do zabudowy'])]),
    (15.0, 19.5, 'lazienka-przed.jpg', 'lazienka-po.jpg', 1.5, [(0.0, ['ŁAZIENKA'], ['nowa instalacja gazowa'])]),
]
DATA = (19.5, 24.5, 'pokoj-1-przed.jpg')
END = 24.5
bases = {}
for f in {x for s in SEGS for x in s[2:4]} | {DATA[2]}:
    bases[f] = load_cover(A + f)

out = sys.stdout.buffer
for i in range(N):
    t = i / FPS
    if t >= END:
        frame = end_board(t - END)
    elif t >= DATA[0]:
        frame = data_board(kenburns(bases[DATA[2]], (t - DATA[0]) / (DATA[1] - DATA[0])), t - DATA[0])
    else:
        s0, s1, fa, fb, tw, caps = next(s for s in SEGS if s[0] <= t < s[1])
        lt, p = t - s0, (t - s0) / (s1 - s0)
        a = kenburns(bases[fa], p)
        if s0 == 0: a = reveal(a, lt)
        pw = (lt - tw) / WIPE
        frame = wipe(a, kenburns(bases[fb], p), pw)
        if pw > 0: viz_label(frame)  # od pierwszej klatki, na ktorej widac "po"
        c0, ti, su = [c for c in caps if c[0] <= lt][-1]
        frame = frame.convert('RGBA')
        caption(frame, ti, su, lt - c0 - (0.2 if s0 == 0 and c0 == 0 else 0.1))
        frame = frame.convert('RGB')
    if t < END:
        frame.paste(LOGO_S, (W - 150 - 48, 110), LOGO_M)
    out.write(frame.tobytes())
assert i == N - 1
