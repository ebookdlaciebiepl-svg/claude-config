# CLAUDE.md

Przewodnik marki Nieruchomości bez stresu dla Claude Code: zasady tworzenia rolek, muzyki, zdjęć i grafik w spójnym stylu.

## Opis projektu

- Nieruchomości bez stresu to marka w mediach społecznościowych z branży nieruchomości (Wrocław, województwo dolnośląskie).
- Segment: rynek średni, czyli mieszkania i domy dla rodzin.
- Odbiorcy: rodziny szukające mieszkania lub domu; zwracamy się do nich per „Państwo”.
- To repozytorium nie zawiera kodu. Przechowuje konfigurację i zasoby marki.
- Cel repo: spójność wszystkich treści (rolki, muzyka, zdjęcia, logo), niezależnie od tego, kto i kiedy je przygotowuje.

## Stos technologiczny (narzędzia)

- **Canva** – grafiki, okładki rolek, szablony (plansza końcowa, karty z danymi oferty).
- **CapCut** – montaż rolek, napisy, filtr/preset kolorystyczny, miks muzyki z lektorem.
- **Epidemic Sound** – jedyne źródło muzyki (licencjonowanej).
- **Telefon** – zdjęcia i nagrania nieruchomości.
- Platformy publikacji: Instagram, TikTok, Facebook (rolki pionowe 9:16).

## Struktura katalogów

Układ planowany; katalogi będą tworzone w miarę dodawania zasobów.

- `assets/logo/` – pliki logo (jest): `logo-jasne-tlo.webp`, `logo-ciemne-tlo.webp`.
- `assets/baner/` – baner kontaktowy (jest): `baner-kontakt.webp`, `baner-kontakt-maly.png`.
- `assets/fonty/` – czcionki marki.
- `assets/szablony-canva/` – linki do szablonów w Canva.
- `muzyka/` – lista wybranych utworów z Epidemic Sound.
- `scenariusze/` – scenariusze rolek.
- `zdjecia/` – zdjęcia referencyjne i wzorcowe ujęcia.

## Identyfikacja wizualna

### Kolory

- Paleta czarno-złota: ciemne tło, złote akcenty.
- Czerń (tło): `#140C0C` (ciepła, lekko brązowa czerń pierścienia logo).
- Złoto (akcenty, wyróżnienia): `#CEA852` (napisy i obwódka „sznur” w logo).
- Złoto jasne / gradient (napisy na banerze): średnio `#DEB654`, gradient od `#AE8936` (ciemny) do `#F6DB8D` (jasny).
- Uwaga: kody HEX zostały odczytane programowo z plików logo i banera (`assets/`). Mogą zostać doprecyzowane na podstawie oryginałów z Canva; w razie rozbieżności pierwszeństwo mają wartości z Canva.

### Logo

- Opis: logo okrągłe, złota obwódka „sznur”, czarny pierścień z napisem NIERUCHOMOŚCI BEZ STRESU złotymi wersalikami szeryfowymi, w środku ornamentalny wazon.
- Pliki w `assets/logo/`:
  - `logo-ciemne-tlo.webp` – na ciemne tła (rolki, ciemne kadry).
  - `logo-jasne-tlo.webp` – na jasne tła.
- Zawsze używaj tej samej wersji logo (właściwej dla jasności tła).
- Logo zawsze w tym samym miejscu rolki: w rogu kadru oraz na planszy końcowej.
- Nie rozciągaj i nie zniekształcaj logo (zachowuj proporcje).
- Nie zmieniaj kolorów logo i nie nakładaj na nie efektów.

### Baner kontaktowy i współpraca z Metrohouse

- Pliki w `assets/baner/`: `baner-kontakt.webp` (wersja duża), `baner-kontakt-maly.png` (wersja mała).
- Dane kontaktowe (zawsze dokładnie w tej formie):
  - Maciej Styczek, METROHOUSE Wrocław
  - tel. 572 518 617
  - mstyczek@metrohouse.pl
- Baner służy jako plansza końcowa / CTA każdej rolki (razem z krokiem 5 struktury rolki).
- Żółty `#FFCC00` to kolor marki Metrohouse – używaj go tylko w obrębie logo/bloku Metrohouse, nie jako koloru marki „Nieruchomości bez stresu”.
- Logo Metrohouse nie modyfikuj (kolory, proporcje, układ bez zmian).

### Czcionki

- Nagłówki: szeryfowa, wersaliki jak w logo – nazwa do potwierdzenia.
- Tekst i napisy: bezszeryfowa geometryczna jak na banerze (wygląda na Montserrat – do potwierdzenia).
- Zalecenie: wybierz jedną elegancką czcionkę szeryfową (nagłówki) i jedną czystą bezszeryfową (tekst, napisy), a następnie używaj ich zawsze, bez wyjątków.

## Rolki

- Format: pionowy 9:16.
- Bez twarzy: narracja lektora lub same napisy.
- Napisy zawsze, w spójnym stylu: kolory marki (jasny tekst na ciemnym tle, złote wyróżnienia), czcionka marki.
- Ton: formalny i profesjonalny, zwracamy się do widzów per „Państwo”.
- Stała struktura rolki:
  1. Hook w pierwszych sekundach.
  2. Prezentacja nieruchomości.
  3. Kluczowe dane: metraż, liczba pokoi, lokalizacja, cena.
  4. CTA (wezwanie do działania, np. kontakt lub wiadomość).
  5. Plansza końcowa: logo + baner kontaktowy.
- Scenariusze rolek zapisuj w katalogu `scenariusze/` według tej struktury.

## Muzyka

- Styl: elegancki, pianino / chill.
- Źródło: wyłącznie Epidemic Sound (muzyka licencjonowana). Żadnych innych źródeł.
- Głośność: spokojna, wyraźnie pod lektorem; głos musi być dobrze słyszalny.
- Prowadź listę używanych utworów w `muzyka/` (tytuł, wykonawca, w której rolce użyty), aby zachować spójne brzmienie.

## Zdjęcia i nagrania

- Sprzęt: telefon.
- Kadr wypoziomowany (proste linie ścian, drzwi, okien).
- Naturalne światło; nagrywaj w dzień, z odsłoniętymi oknami.
- Porządek we wnętrzach przed nagraniem (usuń zbędne przedmioty).
- Ten sam filtr/preset w CapCut i Canva dla wszystkich materiałów.
- Spójna kolorystyka: ciepła, nieprzesycona.
- Do rolek nagrywaj ujęcia pionowe.

## Zasady i konwencje

- Wszystkie treści i komentarze pisz po polsku.
- Każdą treść przed publikacją sprawdzaj z tym przewodnikiem.
- Dane ofert (cena, metraż i inne parametry) zawsze zgodne z ofertą; nie zaokrąglaj i nie zgaduj.
- Nie commituj sekretów (haseł, kluczy API).

## Praca z subagentami

- Nigdy nie wykonuj pracy samodzielnie – każde zadanie zlecaj subagentom (narzędzie Agent).
- Nie używaj domyślnie modelu Fable; wybieraj model odpowiedni do zadania.
- Do powtarzalnych, rutynowych zadań używaj modelu Opus 5.5 (`model: "opus"`).

## Do uzupełnienia

- [x] Nazwa marki: Nieruchomości bez stresu.
- [x] Miasto: Wrocław, województwo dolnośląskie.
- [x] Kod koloru czerni: `#140C0C` (odczytany z logo; ewentualnie doprecyzować z Canva).
- [x] Kod koloru złota: `#CEA852` (odczytany z logo; ewentualnie doprecyzować z Canva).
- [ ] Potwierdzić czcionkę nagłówków (szeryfowa, wersaliki jak w logo).
- [ ] Potwierdzić czcionkę tekstu i napisów (bezszeryfowa geometryczna, prawdopodobnie Montserrat).
- [x] Pliki logo w `assets/logo/` i baner kontaktowy w `assets/baner/`.
- [ ] Katalogi z sekcji „Struktura katalogów” (`assets/fonty/`, `assets/szablony-canva/`, `muzyka/`, `scenariusze/`, `zdjecia/`).
