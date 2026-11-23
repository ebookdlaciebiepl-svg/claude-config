# Karuzela „Co irytuje w agentach nieruchomości?” – 5 slajdów 1080x1350.
from PIL import Image, ImageDraw, ImageFont
import os
import sys

FD = '/tmp/claude-0/-home-user-claude-config/62174e4f-e878-5a2d-87d0-29fb4de8cbfa/scratchpad/fonty/'
SERIF = FD + 'cormorant-garamond-700.ttf'
M500 = FD + 'montserrat-500.ttf'
M700 = FD + 'montserrat-700.ttf'  # brak wagi 800 -> 700
LOGO = '/home/user/claude-config/assets/logo/logo-ciemne-tlo.webp'
OUT = '/home/user/claude-config/posty/2026-11-agenci-irytuje/'
PREVIEW = '/tmp/claude-0/-home-user-claude-config/62174e4f-e878-5a2d-87d0-29fb4de8cbfa/scratchpad/karuzela-podglad.jpg'

W, H, M = 1080, 1350, 80
WHITE, DARK, GOLD = (255, 255, 255), (20, 12, 12), (206, 168, 82)
BG = ['#D62839', '#2F5BEA', '#D9480F', '#9C1BB5', '#00855A']  # karmin, niebieski, pomarańcz, fiolet-magenta, szmaragd


def hexrgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lum(c):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(x) for x in c)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def F(path, size):
    return ImageFont.truetype(path, size)


def tw(font, s):
    return font.getlength(s)


def wrap(text, font, maxw):
    lines, cur = [], ''
    for w in text.split():
        t = (cur + ' ' + w).strip()
        if tw(font, t) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit(text, path, maxw, maxh, start, minimum, gap=1.12):
    """Największy rozmiar, przy którym tekst mieści się w ramce (żadne słowo nie wystaje)."""
    for size in range(start, minimum - 1, -2):
        f = F(path, size)
        lines = wrap(text, f, maxw)
        lh = int(size * gap)
        if all(tw(f, l) <= maxw for l in lines) and lh * len(lines) <= maxh:
            return f, lines, lh
    raise SystemExit(f'Tekst się nie mieści: {text!r}')


def block(d, x, y, lines, f, lh, fill, align='left', width=None):
    for i, l in enumerate(lines):
        lx = x
        if align == 'center':
            lx = x + (width - tw(f, l)) / 2
        d.text((lx, y + i * lh), l, font=f, fill=fill)
    return y + lh * len(lines)


_logo = None


def logo(size):
    global _logo
    if _logo is None:
        _logo = Image.open(LOGO).convert('RGB')
    im = _logo.resize((size, size), Image.LANCZOS)  # kwadrat -> kwadrat, proporcje zachowane
    mask = Image.new('L', (size * 4, size * 4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size * 4 - 1, size * 4 - 1), fill=255)
    return im, mask.resize((size, size), Image.LANCZOS)


def arrow(d, x, y, length, color, w=5):
    d.line((x, y, x + length, y), fill=color, width=w)
    d.polygon([(x + length + 4, y), (x + length - 14, y - 11), (x + length - 14, y + 11)], fill=color)


def base(n):
    bg = hexrgb(BG[n - 1])
    img = Image.new('RGB', (W, H), bg)
    d = ImageDraw.Draw(img)
    # numer slajdu + nazwa marki (lewy górny róg)
    d.text((M, M), f'{n}/5', font=F(M700, 40), fill=WHITE)
    d.text((M, M + 58), 'NIERUCHOMOŚCI BEZ STRESU', font=F(M700, 22), fill=WHITE)
    d.line((M, M + 96, M + 70, M + 96), fill=WHITE, width=4)
    # logo – zawsze prawy górny róg
    ls = 150
    li, lm = logo(ls)
    img.paste(li, (W - M - ls, M), lm)
    return img, d, bg


def footer_cta(d, bg):
    """Wspólna stopka-CTA na slajdach 2–4: ciemna pigułka, złoty tekst + strzałka."""
    text = 'Proszę napisać w komentarzu, co Państwa irytuje'
    f, lines, lh = fit(text, M700, W - 2 * M - 88 - 100, 40, 32, 22)
    h = 96
    y0 = H - M - h
    d.rounded_rectangle((M, y0, W - M, H - M), radius=h // 2, fill=DARK)
    tx = M + 44 + (W - 2 * M - 88 - 100 - tw(f, lines[0])) / 2
    ty = y0 + (h - f.size) / 2 - f.size * 0.12
    d.text((tx, ty), lines[0], font=f, fill=GOLD)
    arrow(d, W - M - 44 - 60, y0 + h / 2, 56, GOLD)
    return y0


def heading_sub(d, title, sub, top, bottom, title_max=92):
    """Nagłówek (szeryf, biały) + podtytuł (Montserrat 500) dopasowane do pasa [top, bottom]."""
    maxw = W - 2 * M
    fs, sl, slh = fit(sub, M500, maxw, 150, 40, 28, 1.3)
    sub_h = slh * len(sl)
    fh, hl, hlh = fit(title, SERIF, maxw, bottom - top - sub_h - 36, title_max, 52, 1.05)
    y = block(d, M, top, hl, fh, hlh, WHITE)
    y += 30
    d.line((M, y, M + 90, y), fill=WHITE, width=5)
    block(d, M, y + 26, sl, fs, slh, WHITE)


# ---------- Slajd 1: hook + pigułka CTA ----------
def s1():
    img, d, bg = base(1)
    maxw = W - 2 * M
    fh, hl, hlh = fit('CO NAJBARDZIEJ IRYTUJE PAŃSTWA W AGENTACH NIERUCHOMOŚCI?', SERIF, maxw, 560, 130, 70, 1.0)
    y = block(d, M, 300, hl, fh, hlh, WHITE)
    # pigułka CTA – biała, ciemny tekst
    y += 60
    fp, pl, _ = fit('PROSZĘ NAPISAĆ W KOMENTARZU', M700, maxw - 100, 50, 40, 26)
    ph = 110
    d.rounded_rectangle((M, y, W - M, y + ph), radius=ph // 2, fill=WHITE)
    d.text((M + (maxw - tw(fp, pl[0])) / 2, y + (ph - fp.size) / 2 - fp.size * 0.12), pl[0], font=fp, fill=DARK)
    y += ph + 34
    f5, fb = F(M500, 36), F(M700, 36)
    d.text((M, y), 'i odebrać prezent:', font=f5, fill=WHITE)
    y += 50
    segs = [('KALKULATOR', fb), (' lub ', f5), ('PORADNIK', fb)]
    x = M
    for s, f in segs:
        d.text((x, y), s, font=f, fill=WHITE)
        x += tw(f, s)
    # przesuń →
    fs = F(M700, 30)
    t = 'przesuń'
    tx = W - M - 70 - tw(fs, t)
    d.text((tx, H - M - 36), t, font=fs, fill=WHITE)
    arrow(d, W - M - 56, H - M - 36 + 20, 52, WHITE)
    return img


# ---------- Slajd 2: telefon + dymek „...” ----------
def s2():
    img, d, bg = base(2)
    # telefon (kształty)
    px, py, pw, ph = M, 300, 230, 400
    d.rounded_rectangle((px, py, px + pw, py + ph), radius=36, fill=DARK)
    d.rounded_rectangle((px + 18, py + 46, px + pw - 18, py + ph - 56), radius=14, fill=bg)
    d.rounded_rectangle((px + pw / 2 - 30, py + 18, px + pw / 2 + 30, py + 28), radius=5, fill=(70, 60, 60))
    d.ellipse((px + pw / 2 - 16, py + ph - 46, px + pw / 2 + 16, py + ph - 14), outline=(90, 80, 80), width=3)
    # na ekranie: przekreślona słuchawka -> kółko „brak odpowiedzi”
    cx, cy = px + pw / 2, py + ph / 2 - 5
    d.ellipse((cx - 50, cy - 50, cx + 50, cy + 50), outline=WHITE, width=8)
    d.line((cx - 34, cy + 34, cx + 34, cy - 34), fill=WHITE, width=8)
    # dymek z trzema kropkami (cisza)
    bx0, by0, bx1, by1 = px + pw + 60, 340, W - M, 540
    d.rounded_rectangle((bx0, by0, bx1, by1), radius=60, fill=WHITE)
    d.polygon([(bx0 + 10, by1 - 60), (bx0 - 40, by1 + 20), (bx0 + 90, by1 - 6)], fill=WHITE)
    for i in range(3):
        cxx = (bx0 + bx1) / 2 + (i - 1) * 90
        d.ellipse((cxx - 22, (by0 + by1) / 2 - 22, cxx + 22, (by0 + by1) / 2 + 22), fill=(190, 200, 225))
    fl = F(M700, 26)
    lab = 'ODPOWIEDŹ AGENTA'
    d.text(((bx0 + bx1) / 2 - tw(fl, lab) / 2, by1 + 26), lab, font=fl, fill=WHITE)
    fy = footer_cta(d, bg)
    heading_sub(d, 'Cisza po pierwszym telefonie?', 'Dzwonią Państwo, a potem… nic.', 760, fy - 50)
    return img


# ---------- Slajd 3: okienka OGŁOSZENIE vs RZECZYWISTOŚĆ ----------
def house(d, x, y, s, wall, roof, win, door):
    d.polygon([(x, y + s * 0.45), (x + s / 2, y), (x + s, y + s * 0.45)], fill=roof)
    d.rectangle((x + s * 0.12, y + s * 0.45, x + s * 0.88, y + s), fill=wall)
    d.rectangle((x + s * 0.22, y + s * 0.55, x + s * 0.42, y + s * 0.72), fill=win)
    d.rectangle((x + s * 0.58, y + s * 0.62, x + s * 0.76, y + s), fill=door)


def s3():
    img, d, bg = base(3)
    gap = 40
    pw = (W - 2 * M - gap) / 2
    y0, ph = 290, 400
    fl = F(M700, 26)
    for i, (lab, panel) in enumerate([('OGŁOSZENIE', WHITE), ('RZECZYWISTOŚĆ', DARK)]):
        x0 = M + i * (pw + gap)
        d.rounded_rectangle((x0, y0, x0 + pw, y0 + ph), radius=24, fill=panel)
        s = 220
        hx, hy = x0 + (pw - s) / 2, y0 + 50
        if i == 0:
            # „pałac”: słońce, dom w kolorze slajdu, gwiazdki
            d.ellipse((x0 + pw - 110, y0 + 30, x0 + pw - 40, y0 + 100), fill=GOLD)
            house(d, hx, hy, s, bg, DARK, WHITE, GOLD)
            for sx, sy in [(x0 + 50, y0 + 70), (x0 + 70, y0 + 210)]:
                d.polygon([(sx, sy - 18), (sx + 6, sy - 6), (sx + 18, sy), (sx + 6, sy + 6), (sx, sy + 18),
                           (sx - 6, sy + 6), (sx - 18, sy), (sx - 6, sy - 6)], fill=GOLD)
        else:
            # „zaskoczenie”: szary dom, pęknięcie, znak zapytania
            house(d, hx, hy + 10, s, (95, 88, 88), (60, 54, 54), (40, 34, 34), (60, 54, 54))
            d.line([(hx + s * 0.5, hy + s * 0.5), (hx + s * 0.44, hy + s * 0.62), (hx + s * 0.52, hy + s * 0.72),
                    (hx + s * 0.46, hy + s * 0.84)], fill=DARK, width=5)
            fq = F(SERIF, 120)
            d.text((x0 + pw - 80, y0 + 10), '?', font=fq, fill=GOLD)
        # pasek z etykietą
        d.rounded_rectangle((x0, y0 + ph - 74, x0 + pw, y0 + ph), radius=24, fill=DARK if i == 0 else WHITE,
                            corners=(False, False, True, True))
        fl2, ll, _ = fit(lab, M700, pw - 30, 34, 28, 18)
        d.text((x0 + (pw - tw(fl2, ll[0])) / 2, y0 + ph - 74 + (74 - fl2.size) / 2 - 4), ll[0], font=fl2,
               fill=GOLD if i == 0 else DARK)
    fy = footer_cta(d, bg)
    heading_sub(d, 'Zdjęcia, które nie mają nic wspólnego z rzeczywistością?',
                'W ogłoszeniu pałac, na miejscu – zaskoczenie.', y0 + ph + 60, fy - 50, 84)
    return img


# ---------- Slajd 4: duży znak % ----------
def s4():
    img, d, bg = base(4)
    r = 230
    cx, cy = W / 2, 300 + r
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=DARK)
    d.ellipse((cx - r + 18, cy - r + 18, cx + r - 18, cy + r - 18), outline=GOLD, width=4)
    fp = F(SERIF, 360)
    bb = d.textbbox((0, 0), '%', font=fp)
    d.text((cx - (bb[0] + bb[2]) / 2, cy - (bb[1] + bb[3]) / 2), '%', font=fp, fill=GOLD)
    # mała metka „na końcu”
    tag = 'NA KOŃCU?'
    ft = F(M700, 28)
    tx0 = cx + r * 0.45
    d.rounded_rectangle((tx0, cy + r - 70, tx0 + tw(ft, tag) + 50, cy + r - 14), radius=28, fill=WHITE)
    d.text((tx0 + 25, cy + r - 70 + 12), tag, font=ft, fill=DARK)
    fy = footer_cta(d, bg)
    heading_sub(d, 'Prowizja, o której dowiadują się Państwo na końcu?',
                'Koszty powinny być jasne od pierwszej rozmowy.', cy + r + 50, fy - 50, 84)
    return img


# ---------- Slajd 5: prezenty + kontakt ----------
def gift(d, cx, y, s, box, ribbon):
    d.rectangle((cx - s / 2, y + s * 0.35, cx + s / 2, y + s), fill=box)
    d.rectangle((cx - s / 2 - 8, y + s * 0.22, cx + s / 2 + 8, y + s * 0.4), fill=box)
    d.rectangle((cx - s * 0.08, y + s * 0.22, cx + s * 0.08, y + s), fill=ribbon)
    b = y + s * 0.22  # kokarda: dwa trójkąty
    d.polygon([(cx, b), (cx - s * 0.36, y), (cx - s * 0.36, b)], fill=ribbon)
    d.polygon([(cx, b), (cx + s * 0.36, y), (cx + s * 0.36, b)], fill=ribbon)


def s5():
    img, d, bg = base(5)
    maxw = W - 2 * M
    fh, hl, hlh = fit('PREZENT ZA KOMENTARZ', SERIF, maxw - 200, 200, 96, 60, 1.0)
    y = block(d, M, 268, hl, fh, hlh, WHITE) + 30
    gap = 30
    cw = (maxw - gap) / 2
    ch = 430
    cards = [('KALKULATOR', 'sprawdzą Państwo, ile może być warta Państwa nieruchomość'),
             ('PORADNIK', 'jak przygotować mieszkanie do sprzedaży')]
    for i, (t, desc) in enumerate(cards):
        x0 = M + i * (cw + gap)
        d.rounded_rectangle((x0, y, x0 + cw, y + ch), radius=26, fill=WHITE)
        gift(d, x0 + cw / 2, y + 30, 110, bg, DARK)
        ft, tl, _ = fit(t, M700, cw - 50, 44, 36, 24)
        d.text((x0 + (cw - tw(ft, tl[0])) / 2, y + 162), tl[0], font=ft, fill=DARK)
        fd, dl, dlh = fit(desc, M500, cw - 50, ch - 230, 28, 20, 1.3)
        block(d, x0 + 25, y + 222, dl, fd, dlh, DARK, 'center', cw - 50)
        if i == 0:
            # adres kalkulatora w dwóch wierszach, wyrównany do dołu karty
            ul = ['nieruchomosci-bez-stresu.org', '/kalkulator']
            fu, _, ulh = fit(ul[0], M700, cw - 50, 40, 26, 18, 1.25)
            assert y + 222 + dlh * len(dl) + 12 <= y + ch - 28 - ulh * 2, 'adres koliduje z opisem'
            block(d, x0 + 25, y + ch - 28 - ulh * 2, ul, fu, ulh, bg, 'center', cw - 50)
    y += ch + 34
    fi, il, ilh = fit('Proszę dopisać w komentarzu: KALKULATOR lub PORADNIK – prześlemy w wiadomości prywatnej.',
                      M500, maxw, 120, 32, 22, 1.3)
    y = block(d, M, y, il, fi, ilh, WHITE) + 28
    # blok kontaktowy – ciemny, złoty
    bh = H - M - y
    d.rounded_rectangle((M, y, W - M, H - M), radius=24, fill=DARK)
    lines = [('Maciej Styczek, METROHOUSE Wrocław', M700, GOLD),
             ('tel. 572 518 617 · mstyczek@metrohouse.pl', M500, WHITE),
             ('nieruchomoscibezstresu.netlify.app', M700, GOLD)]
    inner = maxw - 60
    sizes = []
    for t, p, _ in lines:
        f, l, _ = fit(t, p, inner, 44, 34, 18)
        assert len(l) == 1, t
        sizes.append(f)
    fsz = min(f.size for f in sizes)
    lh = int(fsz * 1.45)
    ty = y + (bh - lh * 3) / 2 + 4
    for i, (t, p, c) in enumerate(lines):
        f = F(p, fsz)
        d.text((M + (maxw - tw(f, t)) / 2, ty + i * lh), t, font=f, fill=c)
    assert bh >= lh * 3 + 20, f'Za mało miejsca na kontakt: {bh}'
    return img


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for i, b in enumerate(BG, 1):
        print(f'slajd {i} {b}: biały {contrast(WHITE, hexrgb(b)):.2f}:1')
    print(f'złoto na czerni {contrast(GOLD, DARK):.2f}:1')
    # python3 generuj_karuzele.py 5  -> generuje tylko wskazane slajdy (bez podglądu)
    only = [int(a) for a in sys.argv[1:]]
    if only:
        for n in only:
            [s1, s2, s3, s4, s5][n - 1]().save(f'{OUT}slajd-{n}.jpg', quality=92)
        raise SystemExit('ok')
    slides = [s1(), s2(), s3(), s4(), s5()]
    for i, im in enumerate(slides, 1):
        im.save(f'{OUT}slajd-{i}.jpg', quality=92)
    tw_, th_ = 432, 540
    pad = 20
    prev = Image.new('RGB', (pad + 5 * (tw_ + pad), th_ + 2 * pad), (235, 235, 235))
    for i, im in enumerate(slides):
        prev.paste(im.resize((tw_, th_), Image.LANCZOS), (pad + i * (tw_ + pad), pad))
    prev.save(PREVIEW, quality=90)
    print('ok')
