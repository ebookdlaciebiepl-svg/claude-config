# Okladka rolki MURARSKA (przed/po), 1080x1920. Uzycie: python3 -I okladka.py ZRODLA FONTY CENA OUT [SIATKA]
import sys
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageChops

SRC, FONTS, CENA, OUT = sys.argv[1:5]
W, H = 1080, 1920
GOLD, BLACK, LIGHT = (206, 168, 82), (20, 12, 12), (243, 235, 221)
LOGO = '/home/user/claude-config/assets/logo/logo-ciemne-tlo.webp'
F = lambda n, s: ImageFont.truetype(f'{FONTS}/{n}.ttf', s)
SERIF = lambda s: F('cormorant-garamond-700', s)
SANS = lambda s: F('montserrat-500', s)
SANSB = lambda s: F('montserrat-700', s)

def cover(name, fx=0.5):
    # cover-crop: skala jednolita, fx = poziomy punkt kadrowania (0 lewo, 1 prawo)
    im = Image.open(f'{SRC}/{name}').convert('RGB')
    s = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x0 = round((im.width - W) * fx); y0 = (im.height - H) // 2
    return im.crop((x0, y0, x0 + W, y0 + H))

przed = ImageEnhance.Color(cover('pokoj-1-przed.jpg', 1.0)).enhance(0.45)
przed = ImageEnhance.Brightness(przed).enhance(0.92)
przed = ImageChops.multiply(przed, Image.new('RGB', (W, H), (222, 232, 245)))  # chlodniej
po = ImageEnhance.Color(cover('pokoj-1-po.jpg')).enhance(0.95)

# ukosny podzial: x = XT u gory, XB u dolu
XT, XB = 760, 560
xs = lambda y: XT + (XB - XT) * y / H
m = Image.new('L', (W, H), 0)
ImageDraw.Draw(m).polygon([(XT, 0), (W, 0), (W, H), (XB, H)], fill=255)
img = Image.composite(po, przed, m)

# gradienty #140C0C u gory i dolu
ov = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(ov)
for y in range(H):
    a = 0
    if y < 900: u = max(0, (y - 230) / 670); a = 238 * (1 - u * u * (3 - 2 * u))  # gladko, bez skoku
    if y > 1180: a = max(a, 250 * ((y - 1180) / 740) ** 1.1)
    d.line((0, y, W, y), fill=BLACK + (round(a),))
img = img.convert('RGBA'); img.alpha_composite(ov)
d = ImageDraw.Draw(img)

# zlota linia podzialu (z cieniem)
d.line((XT + 4, 0, XB + 4, H), fill=(0, 0, 0, 255), width=4)
d.line((XT, 0, XB, H), fill=GOLD, width=7)

def pill(cx, cy, text, f, pad=22, fill=BLACK, outline=GOLD, color=GOLD, r=12, w=2):
    tw = d.textlength(text, font=f); hh = f.size * 0.8
    box = (cx - tw / 2 - pad, cy - hh / 2 - pad * 0.6, cx + tw / 2 + pad, cy + hh / 2 + pad * 0.6)
    d.rounded_rectangle(box, r, fill=fill, outline=outline, width=w)
    d.text((cx, cy), text, font=f, fill=color, anchor='mm'); return box

# HOOK
hf = SERIF(150)
d.text((W / 2, 370), 'Z TEGO…', font=hf, fill=GOLD, anchor='mm', stroke_width=2, stroke_fill=BLACK)
d.text((W / 2, 520), 'TAKI SALON?', font=hf, fill=GOLD, anchor='mm', stroke_width=2, stroke_fill=BLACK)
d.line((380, 618, 700, 618), fill=GOLD, width=2)
d.text((W / 2, 668), 'Wrocław · ul. Murarska · 42 m² · 2 pokoje', font=SANS(38), fill=LIGHT, anchor='mm')

# etykiety PRZED / PO (przy linii, srodek kadru)
yl = 800
pill(xs(yl) - 150, yl, 'PRZED', SANSB(34), fill=BLACK + (215,), color=LIGHT, outline=LIGHT)
pill(xs(yl) + 120, yl, 'PO', SANSB(34), fill=GOLD, color=BLACK, outline=GOLD)
vf = SANS(26); vw = d.textlength('wizualizacja aranżacji', font=vf)
pill(min(xs(yl) + 60 + vw / 2, W - vw / 2 - 40), yl + 70, 'wizualizacja aranżacji', vf, pad=14, fill=BLACK + (200,), outline=BLACK + (0,), color=LIGHT, w=0)

if CENA:
    pill(W / 2, 1385, CENA, SANSB(42), pad=26, fill=BLACK + (230,), r=40)

# CTA - przycisk
cf = SANSB(44); txt = 'PROSZĘ OBEJRZEĆ PRZEMIANĘ'
tw = d.textlength(txt, font=cf); bw = tw + 60 + 50; x0 = (W - bw) / 2; y0, y1 = 1470, 1574
d.rounded_rectangle((x0, y0, x0 + bw, y1), 52, fill=GOLD)
d.text((x0 + 50, (y0 + y1) / 2), txt, font=cf, fill=BLACK, anchor='lm')
tx = x0 + 50 + tw + 24; cy = (y0 + y1) / 2  # trojkat "play" rysowany (brak glifu w fontach)
d.polygon([(tx, cy - 17), (tx, cy + 17), (tx + 28, cy)], fill=BLACK)
d.text((W / 2, 1625), 'nieruchomosci-bez-stresu.org', font=SANS(30), fill=GOLD, anchor='mm')

# logo: kolo jak w rolce, prawy gorny rog
S = 130
L = Image.open(LOGO).convert('RGB').resize((S, S), Image.LANCZOS)
mk = Image.new('L', (S * 4, S * 4), 0); ImageDraw.Draw(mk).ellipse((4, 4, S * 4 - 4, S * 4 - 4), fill=255)
img.paste(L, (W - S - 40, 262), mk.resize((S, S), Image.LANCZOS))

img = img.convert('RGB'); img.save(OUT, quality=92)
if len(sys.argv) > 5:  # podglad siatki IG 3:4 (srodek 1080x1440) obok calosci
    g = img.crop((0, 240, W, 1680)); sh = Image.new('RGB', (W * 2 + 40, H), (90, 90, 90))
    sh.paste(img, (0, 0)); sh.paste(g, (W + 40, 240)); sh.save(sys.argv[5], quality=85)
