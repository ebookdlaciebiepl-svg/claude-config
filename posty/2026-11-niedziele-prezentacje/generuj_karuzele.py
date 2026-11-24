# Karuzela „Prezentacja w niedzielę? Standard czy wyjątek?” – 5 slajdów 1080x1350 (FB, 4:5).
# Wzór: posty/2026-11-agenci-irytuje/generuj_karuzele.py (te same helpery, fonty, rozmiar).
from PIL import Image, ImageDraw, ImageFont
import os
import sys

FD = '/tmp/claude-0/-home-user-claude-config/62174e4f-e878-5a2d-87d0-29fb4de8cbfa/scratchpad/fonty/'
SERIF = FD + 'cormorant-garamond-700.ttf'
M500 = FD + 'montserrat-500.ttf'
M700 = FD + 'montserrat-700.ttf'
REPO = '/home/user/claude-config/'
LOGO_CIEMNE = REPO + 'assets/logo/logo-ciemne-tlo.webp'
LOGO_JASNE = REPO + 'assets/logo/logo-jasne-tlo.webp'
BANER = REPO + 'assets/baner/baner-kontakt.webp'
OUT = REPO + 'posty/2026-11-niedziele-prezentacje/'
PREVIEW = '/tmp/claude-0/-home-user-claude-config/62174e4f-e878-5a2d-87d0-29fb4de8cbfa/scratchpad/karuzela-niedziele-podglad.jpg'

W, H, M = 1080, 1350, 80
WHITE, DARK, GOLD = (255, 255, 255), (20, 12, 12), (206, 168, 82)
BG = ['#2F5BEA', '#00855A', '#D62839', '#9C1BB5', '#C2410C']  # niebieski, szmaragd, karmin, fiolet, pomarańcz (ciemniejszy niż #D9480F – kontrast)


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
        # cyfry nautyczne Cormorant (opadające „7”) -> cyfry wersalikowe
        d.text((lx, y + i * lh), l, font=f, fill=fill, features=['lnum'] if f.path == SERIF else None)
    return y + lh * len(lines)


def logo(size, under):
    """Logo właściwe do jasności tła pod nim (CLAUDE.md); kwadrat -> kwadrat, proporcje zachowane."""
    path = LOGO_CIEMNE if lum(under) < 0.4 else LOGO_JASNE
    src = Image.open(path).convert('RGBA')
    im = src.resize((size, size), Image.LANCZOS)
    mask = Image.new('L', (size * 4, size * 4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size * 4 - 1, size * 4 - 1), fill=255)
    mask = mask.resize((size, size), Image.LANCZOS)
    alpha = Image.composite(im.getchannel('A'), Image.new('L', (size, size), 0), mask)
    return im.convert('RGB'), alpha


def arrow(d, x, y, length, color, w=5):
    d.line((x, y, x + length, y), fill=color, width=w)
    d.polygon([(x + length + 4, y), (x + length - 14, y - 11), (x + length - 14, y + 11)], fill=color)


def arrow_down(d, cx, y, length, color, w=6):
    """Zamiast emoji 👇 (Montserrat nie ma emoji)."""
    d.line((cx, y, cx, y + length), fill=color, width=w)
    d.polygon([(cx, y + length + 6), (cx - 14, y + length - 14), (cx + 14, y + length - 14)], fill=color)


def bubble(d, x, y, s, color):
    """Prosty dymek zamiast emoji 💬."""
    d.rounded_rectangle((x, y, x + s, y + s * 0.72), radius=s * 0.22, fill=color)
    d.polygon([(x + s * 0.2, y + s * 0.62), (x + s * 0.12, y + s * 0.95), (x + s * 0.45, y + s * 0.68)], fill=color)


def base(n, corner_logo=True):
    bg = hexrgb(BG[n - 1])
    img = Image.new('RGB', (W, H), bg)
    d = ImageDraw.Draw(img)
    d.text((M, M), f'{n}/5', font=F(M700, 40), fill=WHITE)
    d.text((M, M + 58), 'NIERUCHOMOŚCI BEZ STRESU', font=F(M700, 22), fill=WHITE)
    d.line((M, M + 96, M + 70, M + 96), fill=WHITE, width=4)
    if corner_logo:
        ls = 150
        li, lm = logo(ls, bg)
        img.paste(li, (W - M - ls, M), lm)
    return img, d, bg


def heading(d, text, top, maxh, start=110, minimum=60, maxw=W - 2 * M):
    fh, hl, hlh = fit(text, SERIF, maxw, maxh, start, minimum, 1.0)
    return block(d, M, top, hl, fh, hlh, WHITE)


def rule(d, y):
    d.line((M, y, M + 90, y), fill=WHITE, width=5)


# ---------- Slajd 1: pytanie + CTA na start ----------
def s1():
    img, d, bg = base(1)
    maxw = W - 2 * M
    y = heading(d, 'PREZENTACJA W NIEDZIELĘ?', 330, 380, 140, 80)
    y += 36
    rule(d, y)
    fs, sl, slh = fit('Standard czy wyjątek?', M700, maxw, 80, 60, 36)
    y = block(d, M, y + 36, sl, fs, slh, WHITE) + 70
    # pigułka CTA – ciemna, złoty tekst + strzałka w dół
    ph = 110
    fp, pl, _ = fit('Proszę napisać w komentarzu', M700, maxw - 160, 50, 40, 26)
    d.rounded_rectangle((M, y, W - M, y + ph), radius=ph // 2, fill=DARK)
    d.text((M + 50, y + (ph - fp.size) / 2 - fp.size * 0.12), pl[0], font=fp, fill=GOLD)
    arrow_down(d, W - M - 70, y + 28, 50, GOLD)
    fsw = F(M700, 30)
    t = 'przesuń'
    d.text((W - M - 70 - tw(fsw, t), H - M - 36), t, font=fsw, fill=WHITE)
    arrow(d, W - M - 56, H - M - 36 + 20, 52, WHITE)
    return img


# ---------- Slajd 2: elastyczność – lista z ptaszkami ----------
def s2():
    img, d, bg = base(2)
    maxw = W - 2 * M
    y = heading(d, 'ELASTYCZNOŚĆ – TAK', 330, 260, 120, 70)
    y += 60
    items = ['wieczory', 'soboty', 'terminy dopasowane do Państwa']
    rh, gap = 150, 34
    for it in items:
        d.rounded_rectangle((M, y, W - M, y + rh), radius=28, fill=WHITE)
        r = 40
        cx, cy = M + 40 + r, y + rh / 2
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=bg)
        d.line([(cx - 18, cy + 2), (cx - 5, cy + 16), (cx + 20, cy - 14)], fill=WHITE, width=8, joint='curve')
        fi, il, ilh = fit(it, M700, maxw - 190, rh - 30, 46, 26)
        block(d, M + 160, y + (rh - ilh * len(il)) / 2 - fi.size * 0.1, il, fi, ilh, DARK)
        y += rh + gap
    return img


# ---------- Slajd 3: 7 dni – niedziela wyróżniona ----------
def s3():
    img, d, bg = base(3)
    maxw = W - 2 * M
    y = heading(d, '7 DNI W TYGODNIU – NIE MUSI', 360, 300, 120, 70)
    y += 90
    days = ['PN', 'WT', 'ŚR', 'CZ', 'PT', 'SB', 'ND']
    gap = 14
    cw = (maxw - gap * 6) / 7
    fd = F(M700, 30)
    for i, dd in enumerate(days):
        x0 = M + i * (cw + gap)
        last = i == 6
        d.rounded_rectangle((x0, y, x0 + cw, y + 140), radius=20,
                            fill=DARK if last else WHITE, outline=GOLD if last else None, width=4)
        d.text((x0 + (cw - tw(fd, dd)) / 2, y + 22), dd, font=fd, fill=GOLD if last else DARK)
        cx, cy = x0 + cw / 2, y + 100
        if last:  # serce = czas dla rodziny
            s = 22
            d.ellipse((cx - s, cy - s * 0.9, cx, cy + s * 0.1), fill=GOLD)
            d.ellipse((cx, cy - s * 0.9, cx + s, cy + s * 0.1), fill=GOLD)
            d.polygon([(cx - s + 1, cy - s * 0.3), (cx + s - 1, cy - s * 0.3), (cx, cy + s)], fill=GOLD)
        else:
            d.ellipse((cx - 12, cy - 12, cx + 12, cy + 12), fill=bg)
    y += 140 + 100
    rule(d, y)
    ft, tl, tlh = fit('Prawie zawsze da się znaleźć termin dobry dla obu stron.', M500, maxw, 260, 62, 34, 1.3)
    block(d, M, y + 44, tl, ft, tlh, WHITE)
    return img


# ---------- Slajd 4: trzy wyróżnione słowa ----------
def s4():
    img, d, bg = base(4)
    maxw = W - 2 * M
    y = heading(d, 'O JAKOŚCI OBSŁUGI DECYDUJE', 330, 240, 100, 60)
    y += 60
    words = ['PRZYGOTOWANIE', 'UWAŻNOŚĆ', 'ZAANGAŻOWANIE']
    ph, gap = 130, 30
    fw = min((fit(w, M700, maxw - 120, 70, 56, 30)[0] for w in words), key=lambda f: f.size)
    for w in words:
        d.rounded_rectangle((M, y, W - M, y + ph), radius=ph // 2, fill=DARK)
        d.text((M + (maxw - tw(fw, w)) / 2, y + (ph - fw.size) / 2 - fw.size * 0.12), w, font=fw, fill=GOLD)
        y += ph + gap
    y += 30
    fs, sl, slh = fit('…a nie godzina czy dzień tygodnia.', M500, maxw, 120, 44, 28, 1.3)
    block(d, M, y, sl, fs, slh, WHITE)
    return img


# ---------- Slajd 5: pytanie + plansza końcowa (logo + baner) ----------
def s5():
    img, d, bg = base(5, corner_logo=False)
    maxw = W - 2 * M
    # plansza końcowa – ciemny blok od dołu
    pad = 24
    ban = Image.open(BANER).convert('RGB')
    bw = maxw - 2 * pad
    bh = round(bw * ban.height / ban.width)  # proporcje banera zachowane
    ls = 170
    fu = F(M700, 34)
    url = 'nieruchomosci-bez-stresu.org'
    card_h = pad + ls + 24 + bh + 26 + 44 + pad
    cy0 = H - M - card_h
    d.rounded_rectangle((M, cy0, W - M, H - M), radius=28, fill=DARK)
    li, lm = logo(ls, DARK)
    img.paste(li, (int((W - ls) / 2), cy0 + pad), lm)
    by = cy0 + pad + ls + 24
    img.paste(ban.resize((bw, bh), Image.LANCZOS), (M + pad, by))
    d.text(((W - tw(fu, url)) / 2, by + bh + 22), url, font=fu, fill=GOLD)
    # treść nad planszą
    y = heading(d, 'A JAK UWAŻAJĄ PAŃSTWO?', 230, 220, 100, 60)
    y += 26
    rule(d, y)
    fq, ql, qlh = fit('Niedziela i święta: standard czy wyjątek?', M700, maxw, 120, 46, 28, 1.2)
    y = block(d, M, y + 30, ql, fq, qlh, WHITE) + 24
    fc = F(M500, 38)
    t = 'Czekam na Państwa komentarze'
    d.text((M, y), t, font=fc, fill=WHITE)
    bubble(d, M + tw(fc, t) + 18, y + 4, 44, WHITE)
    assert y + 60 <= cy0 - 20, f'treść nachodzi na planszę: {y + 60} > {cy0 - 20}'
    return img


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for i, b in enumerate(BG, 1):
        c = contrast(WHITE, hexrgb(b))
        print(f'slajd {i} {b}: biały {c:.2f}:1')
        assert c >= 4.5, f'za niski kontrast na slajdzie {i}'
    print(f'złoto na czerni {contrast(GOLD, DARK):.2f}:1')
    print(f'ciemny tekst na bieli {contrast(DARK, WHITE):.2f}:1')
    only = [int(a) for a in sys.argv[1:]]
    fns = [s1, s2, s3, s4, s5]
    if only:
        for n in only:
            fns[n - 1]().save(f'{OUT}slajd-{n}.jpg', quality=92)
        raise SystemExit('ok')
    slides = [f() for f in fns]
    for i, im in enumerate(slides, 1):
        im.save(f'{OUT}slajd-{i}.jpg', quality=92)
    tw_, th_ = 432, 540
    pad = 20
    prev = Image.new('RGB', (pad + 5 * (tw_ + pad), th_ + 2 * pad), (235, 235, 235))
    for i, im in enumerate(slides):
        prev.paste(im.resize((tw_, th_), Image.LANCZOS), (pad + i * (tw_ + pad), pad))
    prev.save(PREVIEW, quality=90)
    print('ok')
