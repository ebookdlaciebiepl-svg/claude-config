# CLAUDE.md

Ten plik zawiera instrukcje dla Claude Code dotyczące pracy w tym projekcie.

## Opis projektu

<!-- Krótko: czym jest projekt, dla kogo, jaki jest jego cel. -->

## Stos technologiczny

<!-- Np. język, framework, baza danych, narzędzia budowania. -->

## Struktura katalogów

<!-- Najważniejsze katalogi i co w nich jest, np.:
- `src/` – kod źródłowy
- `tests/` – testy
- `docs/` – dokumentacja
-->

## Polecenia

<!-- Uzupełnij właściwymi poleceniami projektu. -->

```bash
# instalacja zależności
# uruchomienie aplikacji
# testy
# lint / formatowanie
```

## Zasady i konwencje

- Odpowiadaj i pisz komentarze po polsku (chyba że kod wymaga inaczej).
- Trzymaj się istniejącego stylu kodu i nazewnictwa w projekcie.
- Przed zakończeniem zadania uruchom testy i linter.
- Nie commituj sekretów (kluczy API, haseł, plików `.env`).
- Wprowadzaj małe, przemyślane zmiany; większe refaktory najpierw omów.

## Praca z subagentami

- Nigdy nie wykonuj pracy samodzielnie – każde zadanie zlecaj subagentom (narzędzie Agent).
- Nie używaj domyślnie modelu Fable; wybieraj model odpowiedni do zadania.
- Do powtarzalnych, rutynowych zadań używaj modelu Opus 5.5 (`model: "opus"`).

## Uwagi

<!-- Wszystko, o czym Claude powinien pamiętać: znane problemy, pułapki, decyzje architektoniczne. -->
