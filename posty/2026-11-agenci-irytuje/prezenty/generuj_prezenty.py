"""Generuje poradnik „Jak przygotować mieszkanie do sprzedaży – 10 kroków” (JPG 1080x1350).

Użycie: python3 generuj_prezenty.py KATALOG_FONTOW [KATALOG_WYJSCIOWY]
Katalog fontów: cormorant-garamond-700.ttf, montserrat-500.ttf, montserrat-700.ttf.
Liczb rynkowych brak celowo (zasada danych z CLAUDE.md).
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H, M = 1080, 1350, 80
CZERN, ZLOTO, JASNY = "#140C0C", "#CEA852", "#EFE7DA"
KREM, ZLOTO_NA_KREMIE = "#F5EFE4", "#9E7A2C"  # ciemniejsze złoto: kontrast tekstu na kremowym tle

REPO = Path(__file__).resolve().parents[3]
LOGO = Image.open(REPO / "assets/logo/logo-ciemne-tlo.webp").convert("RGB")

CECHY = ["lnum"]  # cyfry wyrównane: Cormorant domyślnie ma nautyczne („1” jak „I”)
KONTAKT = ["Maciej Styczek, METROHOUSE Wrocław", "tel. 572 518 617", "mstyczek@metrohouse.pl"]
STRONA = "nieruchomoscibezstresu.netlify.app"

KROKI = [
    ("Dokumenty", "Warto zawczasu przygotować odpis księgi wieczystej, zaświadczenia ze spółdzielni lub wspólnoty oraz potwierdzenie braku zadłużenia. Komplet dokumentów budzi zaufanie kupujących."),
    ("Porządek", "Proszę usunąć zbędne rzeczy z blatów, szaf i przedpokoju. Mniej przedmiotów to optycznie więcej przestrzeni."),
    ("Depersonalizacja", "Zdjęcia rodzinne, kolekcje i pamiątki warto na czas sprzedaży schować. Kupujący powinni móc wyobrazić sobie w tym miejscu siebie."),
    ("Drobne naprawy", "Cieknący kran, luźna klamka, niedziałające gniazdko czy ciemne fugi psują odbiór całości. Warto je naprawić przed pierwszą prezentacją."),
    ("Odświeżone ściany", "Ślady i intensywne kolory warto pokryć neutralną, jasną farbą. Takie wnętrze wygląda czyściej i lepiej wychodzi na zdjęciach."),
    ("Światło", "Proszę odsłonić okna, wymienić przepalone żarówki i wybrać ciepłą barwę światła. Jasne mieszkanie wydaje się większe."),
    ("Zapach i świeże powietrze", "Przed każdą wizytą warto dobrze przewietrzyć mieszkanie. Zapach jedzenia, dymu czy zwierząt potrafi zniechęcić od progu."),
    ("Zdjęcia", "Zdjęcia najlepiej robić w dzień, przy naturalnym świetle, z prostym, wypoziomowanym kadrem. Proszę sfotografować każde pomieszczenie."),
    ("Przygotowanie do prezentacji", "Przed wizytą proszę zadbać o porządek i komfortową temperaturę. Warto mieć pod ręką informacje o czynszu i kosztach utrzymania."),
    ("Realistyczna cena", "Cenę warto ustalić na podstawie podobnych ofert i od początku jasno przedstawić wszystkie koszty. Przejrzystość ułatwia rozmowy z kupującymi."),
]
PODZIAL = [3, 3, 2, 2]  # kroki na kolejnych stronach treści


def fonty(katalog):
    k = Path(katalog)
    return lambda nazwa, r: ImageFont.truetype(str(k / f"{nazwa}.ttf"), r)


def lam(d, tekst, font, szer):
    """Łamie tekst na linie mieszczące się w szerokości szer."""
    linie, akt = [], ""
    for slowo in tekst.split():
        proba = f"{akt} {slowo}".strip()
        if d.textlength(proba, font=font, features=CECHY) <= szer or not akt:
            akt = proba
        else:
            linie.append(akt)
            akt = slowo
    linie.append(akt)
    for l in linie:
        assert d.textlength(l, font=font, features=CECHY) <= szer, f"za długie słowo: {l}"
    return linie


def pisz(d, x, y, tekst, font, kolor, szer, odstep=1.3, srodek=False):
    """Rysuje łamany tekst, zwraca y pod ostatnią linią."""
    for l in lam(d, tekst, font, szer):
        lx = x + (szer - d.textlength(l, font=font, features=CECHY)) / 2 if srodek else x
        d.text((lx, y), l, font=font, fill=kolor, features=CECHY)
        y += int(font.size * odstep)
    return y


def logo(img, x, y, rozm):
    mask = Image.new("L", (rozm, rozm), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, rozm - 1, rozm - 1), fill=255)
    img.paste(LOGO.resize((rozm, rozm), Image.LANCZOS), (x, y), mask)


def zapisz(img, d, y, sciezka):
    assert y <= H - M, f"{sciezka.name}: treść wychodzi poza margines (y={y})"
    img.save(sciezka, "JPEG", quality=92)
    print("zapisano", sciezka)


def okladka(F, out):
    img = Image.new("RGB", (W, H), CZERN)
    d = ImageDraw.Draw(img)
    d.rectangle((40, 40, W - 41, H - 41), outline=ZLOTO, width=3)
    logo(img, (W - 300) // 2, 130, 300)
    y = 490
    y = pisz(d, M, y, "PORADNIK", F("montserrat-700", 36), ZLOTO, W - 2 * M, srodek=True) + 30
    y = pisz(d, M, y, "JAK PRZYGOTOWAĆ MIESZKANIE DO SPRZEDAŻY", F("cormorant-garamond-700", 84), JASNY, W - 2 * M, 1.1, True) + 30
    d.line((W / 2 - 120, y, W / 2 + 120, y), fill=ZLOTO, width=3)
    y = pisz(d, M, y + 40, "10 KROKÓW", F("cormorant-garamond-700", 110), ZLOTO, W - 2 * M, 1.1, True) + 30
    y = pisz(d, M, y, "Praktyczna lista dla Państwa – krok po kroku, przed pierwszym ogłoszeniem.", F("montserrat-500", 36), JASNY, W - 2 * M, srodek=True)
    zapisz(img, d, y, out / "poradnik-1.jpg")


def strona_krokow(F, out, nr_strony, kroki, start):
    img = Image.new("RGB", (W, H), KREM)
    d = ImageDraw.Draw(img)
    rozm_logo = 130
    logo(img, W - M - rozm_logo, 60, rozm_logo)
    szer_naglowka = W - 2 * M - rozm_logo - 30
    y = pisz(d, M, 75, "JAK PRZYGOTOWAĆ MIESZKANIE DO SPRZEDAŻY", F("montserrat-700", 26), ZLOTO_NA_KREMIE, szer_naglowka)
    y = pisz(d, M, y + 5, f"Kroki {start + 1}–{start + len(kroki)} z 10", F("cormorant-garamond-700", 56), CZERN, szer_naglowka)
    y = max(y, 60 + rozm_logo) + 30
    d.line((M, y, W - M, y), fill=ZLOTO, width=3)
    y += 45
    kol = 170  # szerokość kolumny z numerem
    fnum, ftyt, ftek = F("cormorant-garamond-700", 130), F("montserrat-700", 40), F("montserrat-500", 34)
    def blok(d, y, ekstra):
        for i, (tytul, tekst) in enumerate(kroki):
            nr = str(start + i + 1)
            d.text((M + (kol - 30 - d.textlength(nr, font=fnum, features=CECHY)) / 2, y - 30), nr, font=fnum, fill=ZLOTO, features=CECHY)
            yt = pisz(d, M + kol, y, tytul, ftyt, CZERN, W - 2 * M - kol, 1.2) + 10
            yt = pisz(d, M + kol, yt, tekst, ftek, "#3A2E28", W - 2 * M - kol, 1.4)
            y = max(yt, y + 130) + 40
            if i < len(kroki) - 1:
                y += ekstra // 2
                d.line((M + kol, y - 20, W - M, y - 20), fill="#DCCBA8", width=2)
                y += 20 + ekstra // 2
        return y

    # przebieg próbny: wolne miejsce rozkładamy między kroki, by strony z 2 krokami nie miały pustego dołu
    koniec = blok(ImageDraw.Draw(Image.new("RGB", (W, H))), y, 0)
    ekstra = min(160, max(0, H - M - 40 - koniec) // len(kroki))
    y = blok(d, y + ekstra // 2, ekstra)
    zapisz(img, d, y, out / f"poradnik-{nr_strony}.jpg")


def kontakt(F, out, nr_strony):
    img = Image.new("RGB", (W, H), CZERN)
    d = ImageDraw.Draw(img)
    d.rectangle((40, 40, W - 41, H - 41), outline=ZLOTO, width=3)
    logo(img, (W - 240) // 2, 120, 240)
    y = 410
    y = pisz(d, M, y, "Chcą Państwo sprzedać mieszkanie bez stresu?", F("cormorant-garamond-700", 76), JASNY, W - 2 * M, 1.1, True) + 30
    y = pisz(d, M, y, "Zapraszamy do kontaktu. Chętnie pomożemy przejść przez wszystkie kroki.", F("montserrat-500", 36), JASNY, W - 2 * M, srodek=True) + 40
    d.line((W / 2 - 120, y, W / 2 + 120, y), fill=ZLOTO, width=3)
    y += 50
    y = pisz(d, M, y, KONTAKT[0], F("montserrat-700", 40), ZLOTO, W - 2 * M, srodek=True) + 10
    for l in KONTAKT[1:]:
        y = pisz(d, M, y, l, F("montserrat-500", 40), JASNY, W - 2 * M, srodek=True) + 6
    y = pisz(d, M, y + 30, STRONA, F("montserrat-700", 36), ZLOTO, W - 2 * M, srodek=True)
    zapisz(img, d, y, out / f"poradnik-{nr_strony}.jpg")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    F = fonty(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).resolve().parent
    out.mkdir(parents=True, exist_ok=True)
    assert sum(PODZIAL) == len(KROKI) == 10
    okladka(F, out)
    start = 0
    for i, n in enumerate(PODZIAL):
        strona_krokow(F, out, i + 2, KROKI[start:start + n], start)
        start += n
    kontakt(F, out, len(PODZIAL) + 2)


if __name__ == "__main__":
    main()
