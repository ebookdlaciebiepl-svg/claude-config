# Render rolki MURARSKA 20 s, 1080x1920, 30 fps -> surowe klatki RGB na stdout (do ffmpeg).
# Uzycie: python3 -I render_rolka.py ZRODLA_DIR FONTY_DIR CENA > raw   (CENA="" = bez ceny)
import sys
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageOps, ImageFilter

SRC, FONTS, CENA = sys.argv[1], sys.argv[2], sys.argv[3]
W, H, FPS, DUR = 1080, 1920, 30, 20.0
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
    s = H * ZMAX / im.height
    im = im.resize((round(im.width * s), round(H * ZMAX)), Image.LANCZOS)  # proporcje zachowane
    cw = round(W * ZMAX)
    x0 = (im.width - cw) // 2
    return im.crop((x0, 0, x0 + cw, im.height))

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

# (start, koniec, plik, tytul, podtytul) - twarde ciecia miedzy ujeciami jak we wzorcu
SHOTS = [
    (0.0, 2.5, 'img0.webp', ['42 M² DO URZĄDZENIA', 'PO SWOJEMU'], ['Wrocław, ul. Murarska']),
    (2.5, 4.6, 'img3.webp', ['WYGODNY UKŁAD'], ['wiele możliwości aranżacji']),
    (4.6, 6.7, 'img1.webp', ['DWA NIEZALEŻNE POKOJE'], ['dobrze doświetlone']),
    (6.7, 8.8, 'img2.webp', ['NOWA INSTALACJA GAZOWA'], ['komfort i ekonomiczne użytkowanie']),
    (8.8, 10.9, 'img4.webp', ['USTAWNA KUCHNIA'], ['symetryczna, łatwa do zabudowy']),
    (10.9, 13.0, 'img6.webp', ['DOBRA LOKALIZACJA'], ['zieleń, sklepy, placówki oświatowe', 'wygodny dojazd do centrum']),
]
DATA = (13.0, 17.0, 'img0.webp')
bases = {f: load_cover(f) for f in {s[2] for s in SHOTS} | {DATA[2]}}

out = sys.stdout.buffer
for i in range(N):
    t = i / FPS
    if t >= 17.0:
        frame = end_board(t - 17.0)
    elif t >= DATA[0]:
        p = (t - DATA[0]) / (DATA[1] - DATA[0])
        frame = data_board(kenburns(bases[DATA[2]], p), t - DATA[0])
    else:
        s0, s1, f, ti, su = next(s for s in SHOTS if s[0] <= t < s[1])
        frame = reveal(kenburns(bases[f], (t - s0) / (s1 - s0)), t - s0).convert('RGBA')
        caption(frame, ti, su, t - s0 - (0.4 if s0 else 0.2))
        frame = frame.convert('RGB')
    if t < 17.0:
        frame.paste(LOGO_S, (W - 150 - 48, 110), LOGO_M)
    out.write(frame.tobytes())
assert i == N - 1
