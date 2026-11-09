# CLAUDE.md

Przewodnik marki [NAZWA MARKI] dla Claude Code: zasady tworzenia rolek, muzyki, zdjęć i grafik w spójnym stylu.

## Opis projektu

- [NAZWA MARKI] to marka w mediach społecznościowych z branży nieruchomości ([MIASTO]).
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

- `assets/logo/` – pliki logo (do dodania).
- `assets/fonty/` – czcionki marki.
- `assets/szablony-canva/` – linki do szablonów w Canva.
- `muzyka/` – lista wybranych utworów z Epidemic Sound.
- `scenariusze/` – scenariusze rolek.
- `zdjecia/` – zdjęcia referencyjne i wzorcowe ujęcia.

## Identyfikacja wizualna

### Kolory

- Paleta czarno-złota: ciemne tło, złote akcenty.
- Czerń (tło): `[HEX czerni]`.
- Złoto (akcenty, wyróżnienia): `[HEX złota]`.
- Uwaga: kody HEX trzeba uzupełnić. Do tego czasu nie zgaduj wartości; używaj kolorów z szablonów Canva.

### Logo

- Plik logo zostanie dodany później do `assets/logo/`.
- Zawsze używaj tej samej wersji logo.
- Logo zawsze w tym samym miejscu rolki: w rogu kadru oraz na planszy końcowej.
- Nie rozciągaj i nie zniekształcaj logo (zachowuj proporcje).
- Nie zmieniaj kolorów logo i nie nakładaj na nie efektów.

### Czcionki

- Nagłówki: `[czcionka nagłówków]`.
- Tekst i napisy: `[czcionka tekstu]`.
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
  5. Plansza końcowa z logo.
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

- [ ] `[NAZWA MARKI]` – nazwa marki.
- [ ] `[MIASTO]` – miasto działania.
- [ ] `[HEX czerni]` – kod koloru czerni.
- [ ] `[HEX złota]` – kod koloru złota.
- [ ] `[czcionka nagłówków]` – wybrana czcionka szeryfowa.
- [ ] `[czcionka tekstu]` – wybrana czcionka bezszeryfowa.
- [ ] Plik logo w `assets/logo/`.
- [ ] Katalogi z sekcji „Struktura katalogów” (`assets/fonty/`, `assets/szablony-canva/`, `muzyka/`, `scenariusze/`, `zdjecia/`).
