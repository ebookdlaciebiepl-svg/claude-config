# 5 karuzel FB o pracy agenta – po 5 slajdów 1080x1350 (4:5), nowy styl:
# gradient pionowy + ziarno, teksty na półprzezroczystych kartach, złote akcenty.
# Baza: posty/2026-11-niedziele-prezentacje/generuj_karuzele.py (hexrgb/lum/contrast, fit, logo, plansza końcowa).
# Uruchom: python3 posty/karuzele-agent/generuj_karuzele.py [ścieżka-siatki.jpg]
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy as np
import os
import re
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
FD = os.path.join(REPO, 'assets', 'fonty')
SERIF = os.path.join(FD, 'cormorant-garamond-700.ttf')
M500 = os.path.join(FD, 'montserrat-500.ttf')
M700 = os.path.join(FD, 'montserrat-700.ttf')
LOGO_CIEMNE = os.path.join(REPO, 'assets', 'logo', 'logo-ciemne-tlo.webp')
LOGO_JASNE = os.path.join(REPO, 'assets', 'logo', 'logo-jasne-tlo.webp')
BANER = os.path.join(REPO, 'assets', 'baner', 'baner-kontakt.webp')
PORTRET = os.path.join(REPO, 'assets', 'portret', 'maciej-portret.jpg')
OUT = os.path.dirname(os.path.abspath(__file__))

W, H, M = 1080, 1350, 80
PAD = 56                      # wewnętrzny margines karty
IW = W - 2 * M - 2 * PAD      # szerokość treści w karcie
CARD_ALPHA = 0.42             # czarna karta, alfa 42%
WHITE, DARK, GOLD = (255, 255, 255), (20, 12, 12), (206, 168, 82)
GOLD_D, GOLD_L = (174, 137, 54), (246, 219, 141)   # gradient złota #AE8936 -> #F6DB8D
GRAY_PILL, MYTH_TXT = (90, 90, 90), (205, 205, 205)   # MIT: szara pigułka z krzyżykiem, szary tekst
CHECKS = []                   # (kontrast, tekst) – do raportu


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


def lum_range(img, box):
    """Najciemniejszy i najjaśniejszy piksel (luminancja WCAG) w obszarze – tło z kartą, gradientem i ziarnem."""
    a = np.asarray(img.crop(tuple(int(v) for v in box)), dtype=float) / 255
    a = np.where(a <= 0.03928, a / 12.92, ((a + 0.055) / 1.055) ** 2.4)
    L = a @ np.array([0.2126, 0.7152, 0.0722])
    return L.min(), L.max()


def F(path, size):
    return ImageFont.truetype(path, size)


def tw(font, s):
    return font.getlength(s, features=feat(font))


def feat(f):
    # cyfry nautyczne Cormorant (opadające) -> cyfry wersalikowe
    return ['lnum'] if f.path == SERIF else None


def txt(img, d, xy, s, f, fill):
    txts(img, d, [(xy, s, f, fill)])


def txts(img, d, items):
    """Rysuje teksty po sprawdzeniu kontrastu (min. 4.5:1) względem najjaśniejszego i najciemniejszego
    miejsca pod nimi. Najpierw sprawdza wszystkie linie bloku, potem rysuje – żeby akcenty (Ę, Ń)
    z sąsiednich linii nie liczyły się jako tło."""
    for xy, s, f, fill in items:
        box = d.textbbox(xy, s, font=f, features=feat(f))
        lo, hi = lum_range(img, box)
        lf = lum(fill)
        c = min((max(lf, l) + 0.05) / (min(lf, l) + 0.05) for l in (lo, hi))
        assert c >= 4.5, f'za niski kontrast {c:.2f}:1 dla {s!r}'
        CHECKS.append((c, s))
    for xy, s, f, fill in items:
        d.text(xy, s, font=f, fill=fill, features=feat(f))


def wrap(text, font, maxw):
    # jednoliterowe spójniki/przyimki (w, i, z, o…) nie zostają na końcu linii
    words = re.sub(r'(?<!\S)(\w) ', '\\1\u00a0', text).split(' ')
    lines, cur = [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if tw(font, t) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return [l.replace('\u00a0', ' ') for l in lines]


def fit(text, path, maxw, maxh, start, minimum, gap=1.12):
    """Największy rozmiar, przy którym tekst mieści się w ramce (żadne słowo nie wystaje)."""
    for size in range(start, minimum - 1, -2):
        f = F(path, size)
        lines = wrap(text, f, maxw)
        lh = int(size * gap)
        if all(tw(f, l) <= maxw for l in lines) and lh * len(lines) <= maxh:
            return f, lines, lh
    raise SystemExit(f'Tekst się nie mieści: {text!r}')


def rmask(w, h, r, val=255, ss=3):
    """Maska zaokrąglonego prostokąta z wygładzonymi krawędziami (supersampling)."""
    m = Image.new('L', (w * ss, h * ss), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, w * ss - 1, h * ss - 1), radius=r * ss, fill=val)
    return m.resize((w, h), Image.LANCZOS)


def hgrad(w, h, c1, c2):
    t = np.linspace(0, 1, w)[None, :, None]
    g = np.array(c1) * (1 - t) + np.array(c2) * t
    return Image.fromarray(np.repeat(g, h, 0).astype('uint8'))


def card(img, box, alpha=CARD_ALPHA, r=36, color=(0, 0, 0)):
    x0, y0, x1, y1 = (int(v) for v in box)
    img.paste(color, (x0, y0, x1, y1), rmask(x1 - x0, y1 - y0, r, int(255 * alpha)))


def gold_shape(img, box, r=None):
    """Kształt (pigułka/pasek/koło) wypełniony złotym gradientem marki."""
    x0, y0, x1, y1 = (int(v) for v in box)
    w, h = x1 - x0, y1 - y0
    img.paste(hgrad(w, h, GOLD_D, GOLD_L), (x0, y0), rmask(w, h, h // 2 if r is None else r))


def background(c1, c2, seed):
    """Pionowy gradient (ciemniej u góry -> jaśniej u dołu) + delikatne monochromatyczne ziarno, stały seed."""
    t = np.linspace(0, 1, H)[:, None, None]
    g = np.array(hexrgb(c1), float) * (1 - t) + np.array(hexrgb(c2), float) * t
    g = np.repeat(g, W, 1)
    g += np.random.default_rng(seed).normal(0, 4.5, (H, W, 1))
    return Image.fromarray(np.clip(g, 0, 255).astype('uint8'))


def logo(size, under):
    """Logo właściwe do jasności tła pod nim (CLAUDE.md); kwadrat -> kwadrat, proporcje zachowane."""
    path = LOGO_CIEMNE if lum(under) < 0.4 else LOGO_JASNE
    src = Image.open(path).convert('RGBA')
    assert src.width == src.height, 'logo nie jest kwadratowe – skalowanie by je zniekształciło'
    im = src.resize((size, size), Image.LANCZOS)
    mask = Image.new('L', (size * 4, size * 4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size * 4 - 1, size * 4 - 1), fill=255)
    mask = mask.resize((size, size), Image.LANCZOS)
    alpha = Image.composite(im.getchannel('A'), Image.new('L', (size, size), 0), mask)
    return im.convert('RGB'), alpha


def portrait(img, cx, cy, dia, ring=7):
    """Okrągły portret w złotej obwódce (gradient marki) z delikatnym cieniem; zwraca bbox."""
    x0, y0 = int(cx - dia / 2), int(cy - dia / 2)
    sh = Image.new('L', (W, H), 0)
    ImageDraw.Draw(sh).ellipse((x0, y0 + 8, x0 + dia, y0 + dia + 8), fill=150)
    img.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(12)))
    gold_shape(img, (x0, y0, x0 + dia, y0 + dia))
    src = Image.open(PORTRET).convert('RGB')
    di = dia - 2 * ring
    assert di <= src.width * 1.3, 'portret powiększony ponad 1,3x'
    ph = src.resize((di, di), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1, 30, 2))
    img.paste(ph, (x0 + ring, y0 + ring), rmask(di, di, di // 2))
    return x0, y0, x0 + dia, y0 + dia


def signature(img, d, x, cy, card_x0, card_x1=None):
    """Podpis „Maciej Styczek / agent nieruchomości · Wrocław” na ciemnej karcie (kontrast na jasnym gradiencie)."""
    fn, fs = F(SERIF, 50), F(M700, 23)
    name, role = 'Maciej Styczek', 'agent nieruchomości · Wrocław'
    hn, hs, gap = 50, 26, 12
    top = cy - (hn + gap + hs) / 2
    x1 = card_x1 if card_x1 is not None else x + max(tw(fn, name), tw(fs, role)) + 32
    card(img, (card_x0, top - 26, x1, top + hn + gap + hs + 26), r=34)
    bn, bs = d.textbbox((0, 0), name, font=fn, features=feat(fn)), d.textbbox((0, 0), role, font=fs)
    txts(img, d, [((x, top - bn[1]), name, fn, WHITE), ((x, top + hn + gap - bs[1]), role, fs, GOLD_L)])
    return x1


# ---------- ikony zamiast emoji (font nie ma emoji) ----------
def arrow_down(d, cx, y, length, color, w=6):
    d.line((cx, y, cx, y + length - 10), fill=color, width=w)
    d.polygon([(cx, y + length + 4), (cx - 15, y + length - 16), (cx + 15, y + length - 16)], fill=color)


def arrow_right(d, x, y, length, color, w=5):
    d.line((x, y, x + length - 10, y), fill=color, width=w)
    d.polygon([(x + length + 4, y), (x + length - 14, y - 11), (x + length - 14, y + 11)], fill=color)


def bookmark(d, cx, y, h, color):
    w = h * 0.68
    x0, x1 = cx - w / 2, cx + w / 2
    d.polygon([(x0, y), (x1, y), (x1, y + h), (cx, y + h * 0.72), (x0, y + h)], fill=color)


def check(d, cx, cy, s, color, w=6):
    d.line([(cx - s, cy), (cx - s * 0.3, cy + s * 0.7), (cx + s, cy - s * 0.7)], fill=color, width=w, joint='curve')


def cross(d, cx, cy, s, color, w=6):
    d.line((cx - s, cy - s, cx + s, cy + s), fill=color, width=w)
    d.line((cx - s, cy + s, cx + s, cy - s), fill=color, width=w)


# ---------- bloki treści: każdy zwraca (wysokość, rysuj(img, d, x, y)) ----------
def G(h):
    return h, lambda img, d, x, y: None


def Hd(text, start=108, minimum=56, maxh=420):
    """Nagłówek – Cormorant Garamond, biały."""
    f, lines, lh = fit(text, SERIF, IW, maxh, start, minimum, 1.02)

    def dr(img, d, x, y):
        txts(img, d, [((x, y + i * lh), l, f, WHITE) for i, l in enumerate(lines)])
    return lh * len(lines), dr


def T(text, path=M700, start=50, minimum=30, color=WHITE, gap=1.3, maxh=400):
    f, lines, lh = fit(text, path, IW, maxh, start, minimum, gap)

    def dr(img, d, x, y):
        txts(img, d, [((x, y + i * lh), l, f, color) for i, l in enumerate(lines)])
    return lh * len(lines), dr


def R():
    """Złote podkreślenie (gradient)."""
    return 7, lambda img, d, x, y: gold_shape(img, (x, y, x + 130, y + 7))


def L(items, size=46):
    """Lista z ptaszkami w złotych kółkach."""
    f = F(M500, size)
    lh = int(size * 1.3)
    rows = [wrap(it, f, IW - 86) for it in items]
    assert all(tw(f, l) <= IW - 86 for r in rows for l in r)
    gap = 38
    h = sum(lh * len(r) for r in rows) + gap * (len(rows) - 1)

    def dr(img, d, x, y):
        for r in rows:
            cy = y + lh / 2
            gold_shape(img, (x, cy - 25, x + 50, cy + 25))
            check(d, x + 25, cy + 1, 11, DARK, 5)
            txts(img, d, [((x + 86, y + i * lh), l, f, WHITE) for i, l in enumerate(r)])
            y += lh * len(r) + gap
    return h, dr


def Q(n, text):
    """Pytanie z numerem w złotym kole."""
    d_ = 96
    f, lines, lh = fit(text, M700, IW - d_ - 36, 300, 52, 34, 1.25)
    th = lh * len(lines)
    h = max(d_, th)
    fn = F(SERIF, 64)

    def dr(img, d, x, y):
        gold_shape(img, (x, y + (h - d_) / 2, x + d_, y + (h - d_) / 2 + d_))
        s = str(n)
        bb = d.textbbox((0, 0), s, font=fn, features=feat(fn))
        txt(img, d, (x + (d_ - (bb[2] - bb[0])) / 2 - bb[0], y + (h - d_) / 2 + (d_ - (bb[3] - bb[1])) / 2 - bb[1]), s, fn, DARK)
        ty = y + (h - th) / 2 - f.size * 0.08
        txts(img, d, [((x + d_ + 36, ty + i * lh), l, f, WHITE) for i, l in enumerate(lines)])
    return h, dr


def P(label, kind):
    """Pigułka MIT (szara, krzyżyk) / FAKT (złota, ptaszek)."""
    f = F(M700, 32)
    ph = 64
    pw = int(tw(f, label)) + 2 * 30 + 44

    def dr(img, d, x, y):
        if kind == 'fakt':
            gold_shape(img, (x, y, x + pw, y + ph))
            fg = DARK
            check(d, x + 40, y + ph / 2 + 1, 11, fg, 5)
        else:
            img.paste(GRAY_PILL, (int(x), int(y), int(x) + pw, int(y) + ph), rmask(pw, ph, ph // 2))
            fg = WHITE
            cross(d, x + 40, y + ph / 2, 9, fg, 5)
        bb = d.textbbox((0, 0), label, font=f)
        txt(img, d, (x + 70, y + (ph - (bb[3] - bb[1])) / 2 - bb[1]), label, f, fg)
    return ph, dr


def CTA(text, icon):
    """Złota pigułka z wezwaniem do komentarza + ikona (strzałka w dół / zakładka)."""
    ph = 108
    f, lines, _ = fit(text, M700, IW - 150, 60, 40, 26)
    assert len(lines) == 1, f'CTA w jednej linii: {text!r}'

    def dr(img, d, x, y):
        gold_shape(img, (x, y, x + IW, y + ph))
        bb = d.textbbox((0, 0), lines[0], font=f)
        txt(img, d, (x + 46, y + (ph - (bb[3] - bb[1])) / 2 - bb[1]), lines[0], f, DARK)
        cx = x + IW - 64
        if icon == 'bookmark':
            bookmark(d, cx, y + 28, 52, DARK)
        else:
            arrow_down(d, cx, y + 24, 56, DARK)
    return ph, dr


# ---------- układ slajdu ----------
def header(img, d, n, k, corner_logo=True):
    """Numeracja n/5 w złotej pigułce + nazwa marki (lewy górny róg), małe logo (prawy górny)."""
    f = F(M700, 30)
    s = f'{n}/5'
    pw, ph = int(tw(f, s)) + 52, 56
    gold_shape(img, (M, M, M + pw, M + ph))
    bb = d.textbbox((0, 0), s, font=f)
    txt(img, d, (M + (pw - (bb[2] - bb[0])) / 2 - bb[0], M + (ph - (bb[3] - bb[1])) / 2 - bb[1]), s, f, DARK)
    fb = F(M700, 22)
    bb = d.textbbox((0, 0), 'NIERUCHOMOŚCI BEZ STRESU', font=fb)
    txt(img, d, (M + pw + 22, M + (ph - (bb[3] - bb[1])) / 2 - bb[1]), 'NIERUCHOMOŚCI BEZ STRESU', fb, WHITE)
    if corner_logo:
        ls = 150
        li, lm = logo(ls, hexrgb(k['c'][0]))
        img.paste(li, (W - M - ls, M), lm)
        return M + ls          # dół strefy nagłówka
    return M + ph


def stack(img, d, cards, top, bottom, gap=36):
    """Karty jedna pod drugą, wyśrodkowane w pionie między top a bottom."""
    hs = [sum(b[0] for b in c) + 2 * PAD for c in cards]
    total = sum(hs) + gap * (len(cards) - 1)
    assert total <= bottom - top, f'treść za wysoka: {total} > {bottom - top}'
    y = top + (bottom - top - total) / 2
    for c, ch in zip(cards, hs):
        card(img, (M, y, W - M, y + ch))
        by = y + PAD
        for h, dr in c:
            dr(img, d, M + PAD, by)
            by += h
        y += ch + gap


def endboard(img, d):
    """Plansza końcowa: ciemny blok, logo + baner kontaktowy (oryginalne proporcje) + adres strony złotem."""
    pad = 24
    ban = Image.open(BANER).convert('RGB')
    bw = W - 2 * M - 2 * pad
    bh = round(bw * ban.height / ban.width)  # proporcje banera zachowane
    ls = 170
    fu = F(M700, 34)
    url = 'nieruchomosci-bez-stresu.org'
    card_h = pad + ls + 24 + bh + 26 + 44 + pad
    cy0 = H - M - card_h
    card(img, (M, cy0, W - M, H - M), alpha=1, r=28, color=DARK)
    li, lm = logo(ls, DARK)
    img.paste(li, (int((W - ls) / 2), cy0 + pad), lm)
    by = cy0 + pad + ls + 24
    img.paste(ban.resize((bw, bh), Image.LANCZOS), (M + pad, by))
    txt(img, d, ((W - tw(fu, url)) / 2, by + bh + 22), url, fu, GOLD)
    return cy0


def render(k, n, spec):
    img = background(*k['c'], k['seed'] * 10 + n)
    d = ImageDraw.Draw(img)
    kind = spec[0]
    if kind == 'hook':
        _, head, sub, cta, icon = spec
        top = header(img, d, n, k) + 40
        # „przesuń” w ciemnej pigułce, prawy dolny róg
        fs = F(M700, 28)
        pw, ph = int(tw(fs, 'przesuń')) + 120, 58
        x0, y0 = W - M - pw, H - M - ph
        card(img, (x0, y0, x0 + pw, y0 + ph), r=ph // 2)
        bb = d.textbbox((0, 0), 'przesuń', font=fs)
        txt(img, d, (x0 + 28, y0 + (ph - (bb[3] - bb[1])) / 2 - bb[1]), 'przesuń', fs, WHITE)
        arrow_right(d, x0 + pw - 76, y0 + ph / 2, 46, WHITE)
        dia = 214
        pcx, pcy = M + dia / 2, H - M - dia / 2
        sx1 = signature(img, d, M + dia + 24, pcy, pcx)
        assert sx1 <= x0 - 20, 'podpis nachodzi na „przesuń”'
        portrait(img, pcx, pcy, dia)
        bottom = H - M - dia - 36
        rest = [G(30), R(), G(32), T(sub, M700, 54, 36), G(40), CTA(cta, icon)]
        stack(img, d, [[Hd(head, 108, 60, min(330, bottom - top - 2 * PAD - sum(b[0] for b in rest)))] + rest],
              top, bottom)
    elif kind == 'end':
        _, q, sub = spec
        header(img, d, n, k, corner_logo=False)
        dia = 232
        pcx, pcy = W - M - dia / 2, M + dia / 2
        signature(img, d, M + 36, pcy + 34, M, pcx)
        portrait(img, pcx, pcy, dia)
        top = M + dia + 36
        cy0 = endboard(img, d)
        rest = [G(30), R(), G(32), T(sub, M500, 46, 30)] if sub else []
        # nagłówek dostaje tyle miejsca, ile zostaje między portretem a planszą końcową
        blocks = [Hd(q, 84, 50, min(260, cy0 - 40 - top - 2 * PAD - sum(b[0] for b in rest)))] + rest
        stack(img, d, [blocks], top, cy0 - 40)
    else:
        top = header(img, d, n, k) + 60
        stack(img, d, spec[1], top, H - M)
    return img


def list_slide(head, items):
    return ('cards', [[Hd(head, 96, 56), G(30), R(), G(48), L(items)]])


def mit_fakt(mit, fakt):
    return ('cards', [[P('MIT', 'mit'), G(30), T(mit, M500, 50, 32, MYTH_TXT)],
                      [P('FAKT', 'fakt'), G(30), T(fakt, M700, 50, 32)]])


BASE_TAGS = '#nieruchomoscibezstresu #nieruchomosciwroclaw #agentnieruchomosci #metrohouse #sprzedazmieszkania #kupnomieszkania #wroclaw'
STOPKA = '''Maciej Styczek | METROHOUSE Wrocław
📞 572 518 617 | ✉️ mstyczek@metrohouse.pl
🌐 https://nieruchomosci-bez-stresu.org'''

KARUZELE = [
    dict(dir='01-zanim-pokaze', seed=1, c=('#0F4C5C', '#1A8A8A'),
         tytul='Co robi agent, zanim pokaże Państwa mieszkanie?',
         slides=lambda: [
             ('hook', 'ZANIM ZADZWONI PIERWSZY KUPUJĄCY…', 'Ile pracy jest przed ogłoszeniem?',
              'Proszę zgadnąć w komentarzu', 'arrow'),
             list_slide('ANALIZA', ['ceny podobnych mieszkań w okolicy', 'stan prawny', 'mocne strony nieruchomości']),
             list_slide('PRZYGOTOWANIE', ['porządek i aranżacja', 'zdjęcia w dziennym świetle', 'rolka i opis']),
             ('cards', [[Hd('SELEKCJA', 96, 56), G(30), R(), G(44),
                         T('Rozmowa z każdym zainteresowanym przed prezentacją – oglądają tylko poważni kupujący.',
                           M500, 52, 34, gap=1.35)]]),
             ('end', 'Co Państwa najbardziej zaskoczyło?', 'Proszę napisać w komentarzu.'),
         ],
         opis='Ogłoszenie to tylko wierzchołek. Pokazuję, co dzieje się wcześniej – i dlaczego to wpływa na cenę i czas sprzedaży.',
         pytanie='Ile pracy jest przed ogłoszeniem? Proszę zgadnąć w komentarzu 👇',
         tagi='#wycenanieruchomosci #ofertasprzedazy'),
    dict(dir='02-pytania-do-agenta', seed=2, c=('#3B1F6B', '#6D3FB5'),
         tytul='5 pytań do agenta przed podpisaniem umowy',
         slides=lambda: [
             ('hook', 'ZANIM PODPISZĄ PAŃSTWO UMOWĘ Z AGENTEM', '5 pytań, które warto zadać',
              'Które zadaliby Państwo jako pierwsze?', 'arrow'),
             ('cards', [[Q(1, 'Jak ustalił Pan cenę?')], [Q(2, 'Gdzie i jak będzie promowana oferta?')]]),
             ('cards', [[Q(3, 'Jak często dostanę informację o postępach?')], [Q(4, 'Kto prowadzi prezentacje?')]]),
             ('cards', [[Q(5, 'Co dokładnie obejmuje wynagrodzenie?')],
                        [R(), G(34), T('Dobry agent odpowie konkretnie – bez ogólników.', SERIF, 66, 44, GOLD_L, 1.1)]]),
             ('end', 'Jakie pytanie Państwo by dodali?', None),
         ],
         opis='Wybór agenta to decyzja o pieniądzach i czasie. Te pytania pomogą ją podjąć spokojnie.',
         pytanie='5 pytań, które warto zadać. Które zadaliby Państwo jako pierwsze? 👇',
         tagi='#wyboragenta #umowaposrednictwa'),
    dict(dir='03-zdjecia-30-minut', seed=3, c=('#7A2E1D', '#C2552D'),
         tytul='Mieszkanie do zdjęć w 30 minut',
         slides=lambda: [
             ('hook', '30 MINUT, KTÓRE ZMIENIAJĄ ZDJĘCIA OFERTY', 'Chcą Państwo pełną listę?',
              'Proszę napisać „PORADNIK”', 'arrow'),
             list_slide('ŚWIATŁO', ['odsłonięte okna', 'zdjęcia w dzień', 'włączone lampy']),
             list_slide('MNIEJ ZNACZY WIĘCEJ', ['puste blaty', 'schowane drobiazgi', 'zamknięta deska sedesu']),
             list_slide('SZCZEGÓŁY', ['pościelone łóżko', 'świeże ręczniki', 'kwiat lub owoce na stole']),
             ('end', 'Pełna lista w darmowym poradniku.', 'Wystarczy komentarz „PORADNIK”.'),
         ],
         opis='Pierwsze wrażenie kupujący mają ze zdjęć. Krótka lista, którą można zrobić jeszcze dziś. '
              'Poradnik PDF wyślę każdemu, kto napisze komentarz „PORADNIK”.',
         pytanie='Chcą Państwo pełną listę? Proszę napisać „PORADNIK” 👇',
         tagi='#homestaging #zdjecianieruchomosci'),
    dict(dir='04-wylacznosc-mity', seed=4, c=('#123D2E', '#1F7A55'),
         tytul='Umowa na wyłączność – mity i fakty',
         slides=lambda: [
             ('hook', 'UMOWA NA WYŁĄCZNOŚĆ', 'Pułapka czy korzyść?', 'Jakie mają Państwo zdanie?', 'arrow'),
             mit_fakt('„Tracę kontrolę nad sprzedażą”', 'To Państwo akceptują cenę, termin i kupującego.'),
             mit_fakt('„Więcej agentów = szybsza sprzedaż”',
                      'Ta sama oferta w kilku cenach i wersjach budzi nieufność kupujących.'),
             ('cards', [[P('FAKT', 'fakt'), G(36), Hd('Jedna osoba odpowiada za wynik.', 86, 56), G(30), R(), G(36),
                         T('Jeden plan, jedna cena, jeden kontakt dla Państwa.', M500, 48, 32)]]),
             ('end', 'Mieli Państwo doświadczenie z taką umową?', None),
         ],
         opis='Wokół umowy na wyłączność narosło wiele mitów. Krótko o tym, jak to wygląda w praktyce.',
         pytanie='Umowa na wyłączność: pułapka czy korzyść? Jakie mają Państwo zdanie? 👇',
         tagi='#umowanawylacznosc #mityifakty'),
    dict(dir='05-dokumenty', seed=5, c=('#14234B', '#2D4FA0'),
         tytul='Jakie dokumenty przygotować do sprzedaży mieszkania?',
         slides=lambda: [
             ('hook', 'SPRZEDAJĄ PAŃSTWO MIESZKANIE?', 'Te dokumenty warto mieć wcześniej.',
              'Proszę zapisać na później', 'bookmark'),
             list_slide('PODSTAWA', ['akt notarialny lub inny dokument nabycia',
                                     'numer księgi wieczystej (jeśli jest założona)']),
             list_slide('ZAŚWIADCZENIA', ['o braku zaległości (spółdzielnia lub zarządca)', 'o osobach zameldowanych']),
             list_slide('DODATKOWO', ['rzut mieszkania', 'świadectwo charakterystyki energetycznej',
                                      'dokumenty remontów']),
             ('end', 'Nie wiedzą Państwo, od czego zacząć?', 'Pomogę.'),
         ],
         opis='Komplet dokumentów to szybsza sprzedaż i mniej stresu u notariusza. Lista do zapisania – szczegóły '
              'zależą od rodzaju własności, chętnie sprawdzę je indywidualnie.',
         pytanie='Te dokumenty warto mieć wcześniej. Proszę zapisać na później 🔖',
         tagi='#dokumentydosprzedazy #ksiegawieczysta'),
]


if __name__ == '__main__':
    all_slides = []
    for k in KARUZELE:
        out = os.path.join(OUT, k['dir'])
        os.makedirs(out, exist_ok=True)
        for n, spec in enumerate(k['slides'](), 1):
            im = render(k, n, spec)
            assert im.size == (W, H)
            im.save(os.path.join(out, f'slajd-{n}.jpg'), quality=92)
            all_slides.append(im)
        with open(os.path.join(out, 'opis-posta.md'), 'w', encoding='utf-8') as fh:
            fh.write(f"{k['opis']}\n\n{k['pytanie']}\n\n{STOPKA}\n\n{BASE_TAGS} {k['tagi']}\n")
        print(k['dir'], 'ok')
    worst = min(CHECKS)
    print(f'sprawdzonych tekstów: {len(CHECKS)}, najniższy kontrast {worst[0]:.2f}:1 ({worst[1]!r})')
    if len(sys.argv) > 1:  # siatka miniatur 5x5
        tw_, th_, gp = 216, 270, 12
        grid = Image.new('RGB', (gp + 5 * (tw_ + gp), gp + 5 * (th_ + gp)), (235, 235, 235))
        for i, im in enumerate(all_slides):
            grid.paste(im.resize((tw_, th_), Image.LANCZOS), (gp + (i % 5) * (tw_ + gp), gp + (i // 5) * (th_ + gp)))
        grid.save(sys.argv[1], quality=88)
        print('siatka:', sys.argv[1])
