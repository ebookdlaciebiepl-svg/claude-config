# Analiza konkurencji – Nieruchomości bez stresu (Wrocław i dolnośląskie)

Data analizy: 11.11.2026
Dla: marka „Nieruchomości bez stresu” (social media, rynek średni, rodziny), współpraca z METROHOUSE Wrocław (Maciej Styczek).
Aktualizacja: 11.11.2026 (bezpośredni odczyt stron po odblokowaniu części hostów w sieci sesji).

---

## 0. Co zmieniło się w aktualizacji (11.11.2026)

- **Liczba ofert z Morizon (katalog biur Wrocławia, sortowanie „największa liczba ofert”)**: JOT-BE 470, WRE 403, Verso 167, KONCEPT 46, RE/MAX Sunix 9; **SDP Nieruchomości 1 291** (2. miejsce w katalogu). Freedom, Tecnocasa, homfi, Hamilton May, Iglica i Metrohouse **nie występują** w wrocławskim katalogu Morizon. Otodom blokuje pobieranie (błąd 403 CloudFront), więc liczb z Otodom nadal brak. Źródło: https://www.morizon.pl/biura-nieruchomosci/wroclaw/ (odczyt 2026-11-11).
- **Zmiana składu 10 biur**: do zestawienia wchodzi **SDP Nieruchomości** (duża liczba ofert, najsilniejszy TikTok wśród lokalnych biur), wypada **KONCEPT** (46 ofert, IG 122 obserwujących, ostatnie widoczne posty sprzed lat). Kolejność lokalnych biur ułożono według liczby ofert na Morizon.
- **Zmiana TOP 5**: wchodzą **Iglica** (IG 2 337 obserwujących i 691 postów, prawie same rolki; FB 2 623) oraz **SDP** (TikTok 1 945 obserwujących, 20 tys. polubień, 280 filmów). Wypadają **JOT-BE** i **Tecnocasa** (przeniesione do wyróżnień). Szczegóły w sekcji 3.
- **Aktualne liczby obserwujących** (odczyt bezpośredni, 2026-11-11), m.in.: homfi FB 17 435, IG 4 942; Iglica FB 2 623, IG 2 337; WRE FB 1 669, IG 789, TikTok 886; Freedom IG 3 734; JOT-BE FB 1 965, IG 1 076; SDP TikTok 1 945; Metrohouse Wrocław IG 88 (34 posty), FB 149. Pełna lista w sekcji 2.
- **Przykładowe ostatnie posty z datami i zaangażowaniem** dla WRE, Iglicy, homfi i Metrohouse Wrocław (IG) oraz homfi, JOT-BE i Iglicy (FB) – sekcje 2 i 3. Posty Freedom, SDP i Tecnocasa na IG nadal niedostępne. Funkcje stron www zebrano w nowej sekcji 3a.
- **Strony www**: Metrohouse ma wyceniarkę online („5 minut”), kalkulator raty, raporty Barometr z Credipass, blog, „Magazine” i kanał YouTube; Iglica ma profesjonalne zdjęcia i spacery 3D, ale jej blog nie działa (błąd bazy danych); Tecnocasa ma formularz wyceny bez bloga.
- **Nowe dane do treści**: Wrocław, III kw. 2026: średnia cena ofertowa na rynku pierwotnym 16 026 zł/m² (+4,7% kw./kw., największy wzrost wśród miast); w limicie Rodzinnego Kredytu Mieszkaniowego mieści się 55% ofert z rynku wtórnego we Wrocławiu (dane Metrohouse i Credipass).
- **Rekomendacje**: dodano pomysł #13 „Czy to mieszkanie mieści się w Rodzinnym Kredycie Mieszkaniowym?”, doprecyzowano #2, #3, #5, #11 i #12 (sekcja 5); dodano #13 do planu tygodniowego (sekcja 6) i dwa nowe wnioski: wysokie zasięgi bez zaangażowania oraz formalny ton „Państwo” jako wyróżnik (sekcja 4, pkt 8–9).

---

## 1. Metodologia i ograniczenia

**Jak zbierano dane – aktualizacja 11.11.2026**

- Po odblokowaniu hostów strony pobierano bezpośrednio (curl przez proxy sesji, w razie potrzeby Chromium/Playwright). Bez logowania, bez zakładania kont, bez obchodzenia zabezpieczeń. Odczytywano tylko publiczne dane (meta og:description profili, publiczne posty widoczne bez logowania).
- **Hosty, które zadziałały**: www.instagram.com (z limitem zapytań, część profili tylko co którąś próbę), www.facebook.com (część stron; pozostałe przekierowują na logowanie), www.tiktok.com (statystyki profilu; lista filmów niedostępna), www.morizon.pl, gratka.pl (strona główna), rankingpro.pl, iglica.pl, www.metrohouse.pl, www.tecnocasa.pl.
- **Hosty, które nie zadziałały**: www.otodom.pl (403 CloudFront, także w przeglądarce Chromium), m.facebook.com (błąd 400 i przekierowanie na www.facebook.com), homfi.pl (przekierowanie 301 na www.homfi.com, który jest zablokowany przez proxy), www.remax.pl (to strona innej firmy, „REMAX-G”, metalizacja i konstrukcje stalowe; strona sieci RE/MAX to remax-polska.pl, zablokowana przez proxy), tecnocasa.pl bez „www” (blokada proxy; działa tylko www.tecnocasa.pl). Katalog biur na Gratce (gratka.pl/biura-nieruchomosci/wroclaw) zwrócił błąd 401.
- Strony Freedom, WRE, JOT-BE, Verso, KONCEPT i Hamilton May nadal są zablokowane; nie próbowano ich obchodzić.

**Jak zbierano dane – pierwsza wersja raportu**

- Jedynym narzędziem, które działało w tej sesji, była wyszukiwarka internetowa (WebSearch, tryby „standard” i „extended”). Pokazuje ona fragmenty stron i zapisane w pamięci podręcznej podglądy profili FB/IG/TikTok.
- Bezpośrednie pobieranie stron (WebFetch, curl) było wtedy **zablokowane przez ustawienia sieci sesji**.
- Narzędzia vidIQ (`vidiq_ig_profile`, `vidiq_ig_profile_reels`) kosztują 5 kredytów za wywołanie. Konto ma 79 kredytów, więc zgodnie z poleceniem **nie użyto ich** (wydano 0 kredytów). Sprawdzono tylko saldo, co jest bezpłatne.
- Niczego nie kupiono, niczego nie opublikowano i z nikim się nie kontaktowano.

**Jak wybrano 10 biur**

Brak publicznego rankingu biur we Wrocławiu według wielkości (liczby ofert, transakcji czy oddziałów). Rankingi w sieci, np. rankingpro.pl, opierają się na ocenach klientów i mają charakter promocyjny. Wybrano więc biura i sieci, które łącznie spełniają te kryteria:
1. ogólnopolska sieć z kilkoma oddziałami we Wrocławiu (Freedom, Tecnocasa, homfi, RE/MAX);
2. duża liczba ofert lub transakcji w agregatorach (tabelaofert.pl, sonarhome.pl);
3. rozpoznawalność i obecność w zestawieniach lokalnych (Hamilton May, Iglica, JOT-BE, Verso, Koncept).

Kolejność w tabeli jest **szacunkowa**. Nie jest to ranking oparty na pełnych danych.

**Aktualizacja 11.11.2026 – jak urealniono listę.** Katalog Morizon dla Wrocławia (233 biura, sortowanie „największa liczba ofert”) pozwolił porównać biura lokalne. Uwaga: liczba przy biurze to **wszystkie oferty profilu na Morizon**, nie tylko wrocławskie. Np. WGN (1. miejsce, 3 786 ofert) ma w profilu oferty z Katowic, Poznania czy Tarnobrzega, a SDP ma też biura w Warszawie, Łodzi i innych miastach. Dlatego WGN nie trafił do zestawienia (oferty ogólnopolskiej sieci, brak lokalnej komunikacji w social media do sprawdzenia). Sieci ogólnopolskie (Freedom, Tecnocasa, homfi, RE/MAX) i Hamilton May, Iglica oraz Metrohouse nie mają w tym katalogu wrocławskich profili z ofertami (RE/MAX Sunix: 9 ofert), więc ich pozycja nadal opiera się na liczbie oddziałów i rozpoznawalności, a nie na liczbie ofert.

**Najważniejsze ograniczenia (czego nadal NIE dało się sprawdzić, stan 11.11.2026)**

- **Otodom**: brak liczby ofert dla wszystkich biur. Powód: serwis zwraca 403 (CloudFront „Request blocked”) zarówno dla curl, jak i dla przeglądarki Chromium.
- **Gratka**: brak liczby ofert. Powód: katalog biur zwraca błąd 401; strona główna działa, ale nie ma na niej danych o biurach. Morizon i Gratka należą do tej samej grupy (Morizon-Gratka), więc liczby z Morizon są najlepszym dostępnym przybliżeniem.
- **Facebook**: aktualne liczby dla homfi, Iglicy, WRE, JOT-BE, Metrohouse Wrocław i Tecnocasa Grabiszyn (część dopiero w 3. próbie). Strony FreeDOM Wrocław, oddziałów Freedom Krzyki/Centrum, pozostałych oddziałów Tecnocasa i SDP przekierowywały na logowanie (FreeDOM Wrocław: 3 rundy prób). Dla nich zostały liczby z pierwszej wersji raportu (podgląd wyszukiwarki, nieznana data). Z publicznego HTML-a stron FB widać tylko 1 najnowszy post, więc częstotliwości na FB nie da się ustalić.
- **Instagram**: Instagram ogranicza zapytania bez logowania (przekierowanie na stronę logowania). Nie udało się odczytać profili @tecnocasa_krzyki, @tecnocasa_grabiszyn i @verso__nieruchomosci (3 rundy prób; @homfi_com, @freedom_nieruchomosci_ i @jotbe_nieruchomosci_wroclaw udało się odczytać dopiero w kolejnych próbach); dla nich zostały stare liczby. Liczba polubień i komentarzy pochodzi z meta opisu pojedynczych postów; zasięgów i wyświetleń rolek nie widać.
- **TikTok**: widać statystyki profilu (obserwujący, polubienia, liczba filmów), ale lista filmów ładuje się dopiero w przeglądarce i w trybie bez logowania była pusta. Brak dat i wyników pojedynczych filmów. Profili TikTok Freedom, Tecnocasa, Iglicy, Verso i Metrohouse Wrocław nie znaleziono pod sprawdzonymi nazwami (@freedom_nieruchomosci, @tecnocasa_polska, @iglica_nieruchomosci, @verso_nieruchomosci, @metrohouse_wroclaw); konto @metrohouse ma 2 obserwujących i 0 filmów.
- **Strony www**: homfi (www.homfi.com) i RE/MAX (remax-polska.pl) zablokowane przez proxy; www.remax.pl to strona innej firmy. Dla homfi zostały dane z pierwszej wersji (wyszukiwarka). Blog Iglicy zwraca błąd 500 („Error establishing a database connection”). Lista ofert na metrohouse.pl i lista biur na tecnocasa.pl renderują się przez JavaScript i w Chromium były puste, więc liczby ofert Metrohouse i Tecnocasa we Wrocławiu nie ustalono.
- **Posty Freedom i JOT-BE na IG oraz Instagram SDP**: nie odczytano (Instagram przekierowywał na logowanie przy kolejnych próbach).
- **Częstotliwość postów** jest szacunkiem z dat kilku ostatnich postów na IG (4–5 postów na konto), nie pełną statystyką.
- vidIQ: nie użyto (0 kredytów wydanych).

**Rekomendacja na przyszłość:** pełną częstotliwość i zaangażowanie na FB, liczby z Otodom oraz brakujące profile IG da się uzupełnić tylko ręcznie, po zalogowaniu na własne konto w przeglądarce, albo przez płatne narzędzie (vidIQ: ok. 5 kredytów za wywołanie, decyzja należy do Państwa).

---

## 2. Tabela 10 biur (zaktualizowana 11.11.2026)

Punkt odniesienia (nie liczony do 10): **Metrohouse Wrocław**.
- IG @metrohouse_wroclaw: **88 obserwujących, 34 posty** (odczyt 2026-11-11, https://www.instagram.com/metrohouse_wroclaw/; w pierwszej wersji: ok. 47 i 12 postów). Wśród 12 najnowszych pozycji na profilu: 9 postów (zdjęcia/karuzele) i 3 rolki.
- Ostatnie posty: seria „🔑 Klucze jeszcze w tym roku” – zapowiedź 8.11.2026 (9 polubień, 0 komentarzy, https://www.instagram.com/p/Dfer4QGCDFP/), część 2/7 z 10.11.2026 (4 polubienia, https://www.instagram.com/p/DfjspC-lV4k/), część 3/7 z 11.11.2026 (5 polubień, https://www.instagram.com/p/DfmRa6NG6Rj/); wcześniej post z 11.10.2026 „Poniedziałek, kawa, raporty…” (17 polubień, 1 komentarz, https://www.instagram.com/p/DeYh1ihCKZz/). Częstotliwość: nieregularna (seria codzienna od 8.11, wcześniej przerwy kilkutygodniowe – szacunek z dat 5 postów).
- FB „Metrohouse Wrocław”: **149 obserwujących** (https://www.facebook.com/metrohouseWroclaw/, 2026-11-11; w pierwszej wersji ok. 146). Jedyny post widoczny bez logowania pochodzi z 1.08.2016, więc aktualnej aktywności na FB nie da się ocenić. TikTok: brak profilu wrocławskiego; konto @metrohouse ma 2 obserwujących i 0 filmów (https://www.tiktok.com/@metrohouse, 2026-11-11).
- Strona sieci (https://www.metrohouse.pl/, 2026-11-11): wyceniarka online, kalkulator raty, raporty Barometr z Credipass, blog, „Magazine”, YouTube – szczegóły w sekcji 3a.
- Wniosek bez zmian, a nawet mocniejszy: **lokalne profile Metrohouse we Wrocławiu są bardzo małe** (posty z kilkoma polubieniami). To szansa dla marki „Nieruchomości bez stresu”, która może zostać głównym kanałem social media dla tej współpracy.

Oznaczenia: **(11.11)** = odczyt bezpośredni 2026-11-11; **(stare)** = podgląd wyszukiwarki z pierwszej wersji, data nieznana. „Morizon” = liczba wszystkich ofert profilu biura w katalogu https://www.morizon.pl/biura-nieruchomosci/wroclaw/ (2026-11-11); „brak w katalogu” = biuro nie ma wrocławskiego profilu z ofertami na Morizon.

| # | Biuro / sieć | Obecność we Wrocławiu i liczba ofert | Strona www (potwierdzone elementy) | Facebook | Instagram | TikTok / YouTube | Częstotliwość / formaty / zaangażowanie |
|---|---|---|---|---|---|---|---|
| 1 | **Freedom Nieruchomości** | Co najmniej 2–3 oddziały: Krzyki (Haukego-Bosaka 17/1), Centrum (Stabłowicka 24). Sieć: „ponad 65 oddziałów, blisko 500 agentów” (wg freedom.pl). Morizon: brak w katalogu. Otodom: nie odczytano | Blog z poradnikami (wycena, sprzedaż); strona „Zleć sprzedaż” dla biura Centrum (stare – strona nadal zablokowana) | FreeDOM Wrocław ok. 416, Krzyki ok. 1,2 tys., Centrum ok. 197 (stare; w 11.11 przekierowanie na logowanie) | Konto ogólnopolskie @freedom_nieruchomosci_: **3 734 obserwujących, 1 923 posty (11.11)**. Konta wrocławskiego nie znaleziono | TikTok: nie znaleziono (@freedom_nieruchomosci nie istnieje). YouTube, podcasty „Pewny Wybór” i „Rób swoje” (stare) | IG: wśród 12 najnowszych pozycji 9 postów i 3 rolki; pojedynczych postów (daty, polubienia) nie odczytano – limit zapytań Instagrama |
| 2 | **Tecnocasa** | Co najmniej 4 oddziały: I Krzyki (Hallera 29A), II Grabiszyn (Grabiszyńska 92A), III Nadodrze (Łokietka 2/1B), IV Przedmieście Oławskie (Kościuszki 134). Morizon: brak w katalogu. Otodom: nie odczytano | www.tecnocasa.pl (11.11): formularz „Sprzedaj nieruchomość” („szybko i rzetelnie wycenimy Twoją nieruchomość”), wyszukiwarka agencji; bloga w menu brak | Grabiszyn (https://www.facebook.com/TecnocasaWroclaw/): **328 obserwujących (11.11)**, najnowszy post widoczny bez logowania z 16.06.2025 (oferta 82 m², Grabiszyn, 0 reakcji); Krzyki ok. 73, Oławskie ok. 62, Nadodrze ok. 42 (stare) | @tecnocasa_krzyki ok. 445 (stare; w 11.11 limit zapytań IG); ogólnopolskie @tecnocasa_polska (link na www) | Nie znaleziono | Nie ustalono (profile IG niedostępne w 11.11) |
| 3 | **homfi** (dawniej Nowodworski Estates) | Duży oddział we Wrocławiu, biura w 12 największych miastach. Ok. 2 374 ofert w tabelaofert.pl (cała sieć, stare). Morizon: brak w katalogu | **Blog** z raportami (Barometr homfi), **wyceniarka online**, poradniki (stare – www.homfi.com zablokowany przez proxy, homfi.pl tylko przekierowuje) | **17 435 obserwujących, „615 osób mówi o tym” (11.11)** | @homfi_com: **4 942 obserwujących, 985 postów (11.11)** | TikTok @homfi_com: **236 obserwujących, 2 642 polubienia, 98 filmów (11.11)**; YouTube (stare) | IG: 12 najnowszych pozycji – 7 postów, 5 rolek; posty z 30.10 i 3.11.2026: 15 i 6 polubień. FB: najnowszy post 9.11.2026 – komentarz agentki homfi o rynku jesienią 2026, 2 reakcje, 0 komentarzy. Przy 17 tys. obserwujących to bardzo niskie zaangażowanie |
| 4 | **RE/MAX** (biura franczyzowe) | RE/MAX Speedway II (Na Ostatnim Groszu 3), RE/MAX Sunix (Grabiszyńska 204D). Morizon: **RE/MAX Sunix 9 ofert (11.11)** | Profile agentów na remax-polska.pl (stare; strona zablokowana przez proxy, www.remax.pl to inna firma) | REMAX Speedway II (liczby nie ustalono) | Konta wrocławskiego nie znaleziono | Nie ustalono | Nie sprawdzono |
| 5 | **Hamilton May** | Oddział wrocławski (premium, ekspaci). Morizon: brak w katalogu. W rankingu rankingpro.pl na 1. miejscu (zestawienie autorskie, z zastrzeżeniem, że pozycje mogą być odpłatne) | Blog, raport „Z wyższej półki”, filmy i spacery 3D (stare – strona zablokowana) | Wrocławskiej strony nie znaleziono | Nie ustalono | Nie ustalono | Nie sprawdzono (segment premium, poza grupą docelową) |
| 6 | **Iglica Nieruchomości** | Od 1998 r.; silna na rynku pierwotnym (inwestycje deweloperskie we Wrocławiu i okolicach: Siechnice, Czernica, Środa Śląska). Morizon: brak w katalogu | iglica.pl (11.11): **profesjonalny fotograf architektury i wnętrz**, **spacery 3D** (dla ofert na wyłączność), lista inwestycji; **blog nie działa** (błąd 500 bazy danych); wyceny online ani lead magnetu na stronie nie znaleziono | **2 623 obserwujących, „71 osób mówi o tym” (11.11)** | @witajwiglica: **2 337 obserwujących, 691 postów (11.11)** | YouTube @IglicaNieruchomosciWRO (link na stronie, nie otwierano). TikTok: nie znaleziono | IG: 11 z 12 najnowszych pozycji to rolki; ok. 4–5 publikacji tygodniowo (6–10.11.2026); 6–19 polubień i 1–7 komentarzy na post |
| 7 | **SDP Nieruchomości** (NOWE w zestawieniu) | 2 biura we Wrocławiu (Legnicka 50, Kościuszki 16), też Warszawa i Łódź. **Morizon: 1 291 ofert (11.11)** – 2. miejsce w katalogu Wrocławia (cały profil, nie tylko Wrocław). Dni otwarte mieszkań w opisach ofert | Nie sprawdzano (domena nie była na liście odblokowanych) | Nie odczytano (przekierowanie na logowanie) | Nie ustalono | TikTok @sdp.nieruchomosci: **1 945 obserwujących, 20 000 polubień, 280 filmów (11.11)**; opis: „Wnętrza, które inspirują” | TikTok: najwięcej filmów i polubień wśród sprawdzonych biur lokalnych; dat i wyników pojedynczych filmów nie odczytano |
| 8 | **JOT-BE Nieruchomości** | Piłsudskiego 8a; „najstarsze biuro we Wrocławiu”; ok. 19 agentów. **Morizon: 470 ofert (11.11)** – 3. miejsce w katalogu; tabelaofert: 448 (stare) | Prezentacja zespołu, „Dlaczego warto?” (własny dział prawny) (stare – strona zablokowana) | **1 965 obserwujących, „48 osób mówi o tym” (11.11)**, https://www.facebook.com/biurojotbe/; druga strona ok. 1,4 tys. (stare) | @jotbe_nieruchomosci_wroclaw: **1 076 obserwujących, 473 posty (11.11)** | TikTok @jotbe_nieruchomosci: **9 obserwujących, 70 polubień, 9 filmów (11.11)**. Wideo na FB (stare) | FB: post 10.11.2026 o nowej inwestycji „Ptasia 23” na Nadodrzu – 2 reakcje, 1 komentarz. Posty IG nie odczytane |
| 9 | **WRE Nieruchomości** | Piłsudskiego 91a; **Morizon: 403 oferty (11.11)**; sonarhome: 105 aktywnych ofert, 36 transakcji w 12 mies. (stare) | Strony z ofertami; bloga ani wyceny online nie znaleziono (stare – strona zablokowana) | **1 669 obserwujących, „105 osób mówi o tym” (11.11)** | @wre_nieruchomosci: **789 obserwujących, 245 postów (11.11)** (wcześniej ok. 377 i 158) | TikTok @wre_nieruchomosci: **886 obserwujących, 18 700 polubień, 108 filmów (11.11)**; opis: „Najlepiej oceniane biuro nieruchomości we Wrocławiu!” | IG: 10 z 12 najnowszych pozycji to rolki z ofertami („📍 Wrocław, dzielnica | ulica”); ok. 4 publikacje tygodniowo (5–11.11.2026); zwykle 10–58 polubień, jedna rolka 1 449 polubień i 80 komentarzy |
| 10 | **Verso Nieruchomości** | Grabiszyńska 208, od 2011 r. **Morizon: 167 ofert (11.11)** | Residential / commercial (stare – strona zablokowana) | ok. 823 polubień (stare) | @verso__nieruchomosci ok. 245, 241 postów (stare; w 11.11 limit zapytań IG) | Nie znaleziono | Nie ustalono |

**Wypadło z zestawienia: KONCEPT Nieruchomości** (Rynek 50/11). Morizon: 46 ofert (2026-11-11). IG @konceptnieruchomosci: 122 obserwujących, 25 postów (https://www.instagram.com/konceptnieruchomosci/, 2026-11-11); najnowsze widoczne pozycje na profilu mają stare identyfikatory postów (prawdopodobnie 2024–2025, daty nie odczytano). FB ok. 469 polubień (stare). Mała liczba ofert i niska aktywność, więc zastąpione przez SDP.

**Dlaczego taka kolejność (aktualizacja):** sieci ogólnopolskie (1–4) i Hamilton May (5) zostały na swoich miejscach, bo dla nich nadal brak liczby ofert (Otodom zablokowany, brak w katalogu Morizon). Biura lokalne (6–10) ułożono według liczby ofert na Morizon; Iglica (brak na Morizon) zostaje na 6. miejscu ze względu na skalę rynku pierwotnego i największe lokalne zasięgi w social media.

\* Liczby oznaczone „(stare)” pochodzą z podglądów wyszukiwarki o nieznanej dacie. Traktować jako orientacyjne.

**Mniejsze konta lokalne, ważne jako inspiracja (spoza TOP 10):**
- **Realsy Management** (TikTok @realsy_management): film „Najgorsze dzielnice Wrocławia?” ma ok. 2 275 polubień i 163 komentarze (stare). Profil: **656 obserwujących, 15 600 polubień, 67 filmów** (https://www.tiktok.com/@realsy_management, 2026-11-11). Duża liczba polubień przy małej liczbie obserwujących potwierdza, że **treści o dzielnicach Wrocławia** angażują bardziej niż prezentacje ofert.
- **SDP Nieruchomości** – od tej aktualizacji w zestawieniu 10 biur (poz. 7).
- **Agentki z Wrocławia** (TikTok @nieruchomosci.wroclaw): filmy o dzielnicach (Ołtaszyn, Wojnowice); **173 obserwujących, 376 polubień, 32 filmy** (https://www.tiktok.com/@nieruchomosci.wroclaw, 2026-11-11).
- **@agentstumostow** („Wrocławski agent nieruchomości”, IG): ok. 1 665 obserwujących.

---

## 3. TOP 5 – szczegóły (zaktualizowane 11.11.2026)

Kryterium: jakość i różnorodność treści oraz widoczne zasięgi i zaangażowanie. W aktualizacji dołożono bezpośrednio odczytane liczby obserwujących, liczbę postów/filmów oraz polubienia i komentarze pod kilkoma ostatnimi postami IG (z meta opisu postów). Zasięgów i wyświetleń nadal nie widać.

**Zmiana składu TOP 5 i uzasadnienie**
- **Wchodzi Iglica** (wcześniej wyróżnienie): IG @witajwiglica ma 2 337 obserwujących i 691 postów, prawie wyłącznie rolki, publikowane ok. 4–5 razy w tygodniu, z komentarzami pod większością postów; FB 2 623. To największe zasięgi IG i FB wśród biur lokalnych (niesieciowych).
- **Wchodzi SDP Nieruchomości** (nowe w zestawieniu): 1 291 ofert na Morizon i najsilniejszy TikTok wśród biur lokalnych (1 945 obserwujących, 20 tys. polubień, 280 filmów). To jedyne biuro z dużą liczbą ofert, które systematycznie robi wideo na TikToku.
- **Wypada Tecnocasa**: aktualnie odczytany największy profil (FB Grabiszyn) ma 328 obserwujących; IG niedostępny; brak bloga na www.tecnocasa.pl. Model „dzielnica = oddział” zostaje jako wyróżnienie.
- **Wypada JOT-BE**: IG 1 076 i 473 posty to dobry wynik, ale TikTok ma 9 obserwujących, a postów IG nie dało się odczytać. Przy aktualnych danych Iglica i SDP mają większe zasięgi i bardziej różnorodne formaty wideo. JOT-BE zostaje jako wyróżnienie (2. biuro lokalne pod względem liczby ofert na Morizon: 470).
- homfi, Freedom i WRE zostają; WRE wyraźnie urosło na IG (789 vs ok. 377 w pierwszej wersji).

### 1) homfi – lider treści eksperckich i lead magnetów

**Co robią dobrze**
- **Wyceniarka online jako lead magnet**: formularz zajmuje ok. 1 minuty, a raport zawiera wartość ofertową i transakcyjną, porównywalne oferty i czynniki ceny. Kończy się propozycją darmowej rozmowy z agentem. Źródło: https://www.homfi.com/mozliwosci (stare – w 11.11 strona zablokowana przez proxy)
- **Cykliczny raport rynkowy „Barometr nieruchomości homfi”** z danymi dla Wrocławia, np. maj 2026: ceny ofertowe na rynku pierwotnym −4% m/m, do 13,6 tys. zł/m². Źródło: https://www.homfi.com/blog/barometr-nieruchomosci-maj-2026 (stare)
- **Poradniki krok po kroku**, np. zakup z rynku wtórnego: inspekcja techniczna, księga wieczysta, checklista. Źródło: https://www.homfi.com/blog/zakup-mieszkania-z-rynku-wtornego (stare)
- **Największy zasięg w zestawieniu** (odczyt 2026-11-11): FB **17 435 obserwujących, 615 osób mówi o tym** (https://www.facebook.com/homficom/), IG **4 942 obserwujących, 985 postów** (https://www.instagram.com/homfi_com/), TikTok **236 obserwujących, 2 642 polubienia, 98 filmów** (https://www.tiktok.com/@homfi_com).
- Przykładowy ostatni post FB (9.11.2026): komentarz agentki homfi do sytuacji na rynku jesienią 2026 – format „ekspert komentuje rynek”. 2 reakcje, 0 komentarzy, 0 udostępnień (https://www.facebook.com/homficom/, 2026-11-11).
- Ostatnie posty IG (2026-11-11): wśród 12 najnowszych pozycji 7 postów i 5 rolek. 3.11.2026 „Gdziekolwiek jesteś, jesteśmy blisko.” – 6 polubień, 1 komentarz (https://www.instagram.com/p/DfRrZBfCDiD/); 30.10.2026 „🚀 Listingmaxxing? Podkręcamy oferty do maksimum!” – 15 polubień, 1 komentarz (https://www.instagram.com/p/DfH2nAbjDIb/). Na początku profilu (prawdopodobnie przypięte) posty wizerunkowe z maja 2026 o „ekosystemie homfi” i programie „Better homfi” dla agentów – 26 i 35 polubień (https://www.instagram.com/p/DYWvxvNiB1D/, https://www.instagram.com/p/DYRu9meCC6C/). Tematy: marka i rekrutacja agentów, nie kupujący. Częstotliwość: ok. 1 post tygodniowo w ostatnich 2 tygodniach (szacunek z dat 2 postów).

**Słabe strony / luki**
- Komunikacja ogólnopolska („360°”). Treści są przekrojowe, nie skupiają się na Wrocławiu ani na rodzinach.
- **Bardzo niskie zaangażowanie mimo dużego zasięgu**: 2 reakcje pod postem na profilu z ponad 17 tys. obserwujących. TikTok jest mały (236 obserwujących przy 98 filmach).
- Brak widocznego, osobnego wrocławskiego profilu marki. Agenci prowadzą własne konta (np. Jacek Drewicz, homfi Wrocław), więc przekaz się rozprasza.

### 2) Freedom Nieruchomości – edukacja w formie audio i wideo

**Co robią dobrze**
- **Podcast „Pewny Wybór”** (Spotify, Spreaker, YouTube) tłumaczy trudne tematy i komentuje zmiany na rynku, np. odcinek 35 o wycenie. Źródła: https://open.spotify.com/show/6yIbjpZEU85GDvJ7wA3uPH, https://freedom.pl/blog/pewny-wybor-35-wycena-nieruchomosci-czyli-za-ile-naprawde-mozna-sprzedac-nieruchomosc/ (stare)
- **Blog z praktycznymi poradnikami**, m.in. o różnicy między ceną ofertową a transakcyjną i o kosztach operatu (300–1000 zł). Źródło: https://freedom.pl/blog/ (stare – strona nadal zablokowana)
- **Duży, regularnie prowadzony IG ogólnopolski**: **3 734 obserwujących, 1 923 posty** (https://www.instagram.com/freedom_nieruchomosci_/, 2026-11-11; w pierwszej wersji ok. 3,5 tys. i 1 732 posty, czyli ok. 190 nowych postów od tamtego podglądu). Wśród 12 najnowszych pozycji: 9 postów (grafiki/karuzele) i 3 rolki.
- Pojedynczych postów Freedom nie odczytano: przy kolejnych próbach Instagram przekierowywał na logowanie (limit zapytań). Częstotliwości nie ustalono.
- **Lokalne strony oddziałów na FB**, np. Krzyki ok. 1,2 tys. (stare): https://www.facebook.com/p/Freedom-Nieruchomo%C5%9Bci-Oddzia%C5%82-Wroc%C5%82aw-Krzyki-61554148066377/

**Słabe strony / luki**
- Część artykułów jest bardzo stara (ok. 8–10 lat), a dane w nich dotyczą np. Trójmiasta, nie Wrocławia.
- Rozproszenie: trzy wrocławskie strony FB, brak wrocławskiego IG i brak TikToka. Treści podcastu są często skierowane do agentów („Kariera w nieruchomościach”, „Rób swoje”), a nie do kupujących.

### 3) WRE Nieruchomości – dowód społeczny i rolki z ofertami

**Co robią dobrze**
- **Opinie klientów jako główny argument**: w bio IG „ponad 800 opinii 5★ w Google”, na sonarhome 5/5 ze 124 opinii i 36 transakcji w 12 miesięcy (stare). Opis TikToka (2026-11-11): „Najlepiej oceniane biuro nieruchomości we Wrocławiu!”. Źródła: https://www.instagram.com/wre_nieruchomosci/, https://www.tiktok.com/@wre_nieruchomosci, https://sonarhome.pl/agencje-nieruchomosci/wroclaw
- **Rosnące konta** (2026-11-11): FB **1 669 obserwujących, 105 osób mówi o tym** (https://www.facebook.com/wrenieruch/); IG **789 obserwujących, 245 postów** (wcześniej ok. 377 i 158); TikTok **886 obserwujących, 18 700 polubień, 108 filmów**. Morizon: 403 oferty.
- **Stały szablon rolek z ofertą**: każdy opis zaczyna się od „📍 Wrocław, [dzielnica] | [ulica]”. 10 z 12 najnowszych pozycji na IG to rolki. Ostatnie publikacje (IG, 2026-11-11):
  - 11.11.2026, rolka „Wrocław, Borek | Inwestycja SUDEA” – 11 polubień, 2 komentarze (https://www.instagram.com/reel/Dfm96gPuJ-Y/)
  - 8.11.2026, rolka „Wrocław, Nadodrze | ul. Władysława Łokietka” – 58 polubień, 0 komentarzy (https://www.instagram.com/reel/DffhZtnxVSQ/)
  - 5.11.2026, rolka „Wrocław, Żerniki | ul. Onufrego Zagłoby” – 22 polubienia (https://www.instagram.com/reel/DfXlev_ReU-/)
  - 5.11.2026, post „Wrocław, Nadodrze | ul. Józefa Rostafińskiego” – 10 polubień (https://www.instagram.com/p/DfXhWI7gnCh/)
  - 27.07.2026, rolka „Wrocław | Ul. Długa” – **1 449 polubień, 80 komentarzy** (pierwsza pozycja na profilu, prawdopodobnie przypięta) (https://www.instagram.com/reel/DbTbf7BsQcI/)
- Częstotliwość: ok. 4 publikacje tygodniowo na IG (4 w dniach 5–11.11.2026).

**Słabe strony / luki**
- Typowa rolka z ofertą zbiera 10–60 polubień i prawie bez komentarzy; pojedyncze hity (1 449 polubień) są wyjątkiem.
- Na stronie nie znaleziono treści eksperckich (blog, wycena online). Opierają się na ofertach i opiniach.

### 4) Iglica Nieruchomości – rolki, dane z dzielnic i współpraca z deweloperami (NOWE w TOP 5)

**Co robią dobrze**
- **Największe lokalne zasięgi** (2026-11-11): IG **2 337 obserwujących, 691 postów** (https://www.instagram.com/witajwiglica/), FB **2 623 obserwujących, 71 osób mówi o tym** (https://www.facebook.com/witajwiglica/).
- **Rolki jako główny format**: 11 z 12 najnowszych pozycji na IG to rolki; ok. 4–5 publikacji tygodniowo. Ostatnie publikacje:
  - 10.11.2026, rolka „Lokal handlowo-usługowy w centrum Wrocławia” – 6 polubień, 3 komentarze (https://www.instagram.com/reel/DfkO0VbSTR7/); ten sam materiał na FB 10.11.2026 – 0 reakcji
  - 9.11.2026, rolka „Wiesz, co jest najpiękniejsze w tym mieszkaniu? Widok z 8. piętra.” – 19 polubień, 7 komentarzy (https://www.instagram.com/reel/DfhqCqFyEAb/) – hook pytaniem o emocję, nie o parametry
  - 9.11.2026, post z danymi: „Na Psim Polu ubyło 42% nowych mieszkań w cenie do 12 tys. zł/m²…” – 8 polubień, 1 komentarz (https://www.instagram.com/p/Dfg8vgGigwD/) – **dane rynkowe dla konkretnej dzielnicy**
  - 6.11.2026, rolka „Wyślij nam zrzut ekranu w wiadomości, a prześlemy Ci listę mieszkań na Nowej Pabianickiej z rabatem nawet do 15%.” – 8 polubień, 4 komentarze (https://www.instagram.com/reel/DfZ30n3KDWJ/) – **lead magnet przez wiadomość prywatną**
  - 6.11.2026, rolka we współpracy z deweloperem PCG (Osiedle BO), opublikowana na koncie dewelopera – 27 polubień, 5 komentarzy (https://www.instagram.com/reel/DfZXEGeiDRE/)
- **Jakość materiałów na www** (https://iglica.pl/, 2026-11-11): zdjęcia robi zatrudniony fotograf architektury i wnętrz („Agenci Iglica Nieruchomości nie wykonują zdjęć samodzielnie”), spacery 3D dla ofert na wyłączność, osobna sekcja „Oferty z wizytą 3D”, kanał YouTube @IglicaNieruchomosciWRO.

**Słabe strony / luki**
- **Blog nie działa** (https://iglica.pl/blog/ – błąd 500 „Error establishing a database connection”, 2026-11-11), brak wyceny online.
- Mocny nacisk na inwestycje deweloperskie, premium i nieruchomości komercyjne; mało treści dla rodzin kupujących z rynku wtórnego.
- Zwracają się do odbiorców na „Ty” („Wiesz…”, „Wyślij nam…”). Nasz formalny ton („Państwo”) wyróżni się na tym tle.

### 5) SDP Nieruchomości – skala ofert i TikTok (NOWE w TOP 5)

**Co robią dobrze**
- **Duża liczba ofert**: 1 291 na Morizon (2. miejsce w katalogu Wrocławia, cały profil, także Warszawa i Łódź) (https://www.morizon.pl/biuro-nieruchomosci/sdp-nieruchomosci-21445, 2026-11-11). Dwa biura we Wrocławiu (Legnicka 50, Kościuszki 16).
- **Najsilniejszy TikTok wśród biur lokalnych**: **1 945 obserwujących, 20 000 polubień, 280 filmów**, opis „Wnętrza, które inspirują” (https://www.tiktok.com/@sdp.nieruchomosci, 2026-11-11).
- **Wydarzenia jako treść**: w opisach ofert na Morizon „dni otwarte” mieszkań (np. 18 i 19 listopada) z promocją cenową – naturalny temat na krótkie wideo.
- Instagram SDP: nie ustalono (pod @sdp.nieruchomosci Instagram przekierowywał na logowanie; konto @sdpnieruchomosci istnieje, ale ma 0 postów i 0 obserwujących, więc nie jest profilem biura).

**Słabe strony / luki**
- Nie ustalono FB (przekierowanie na logowanie) ani dat i wyników pojedynczych filmów TikTok.
- Komunikacja skupiona na wnętrzach i ofertach; nie znaleziono treści edukacyjnych dla rodzin.

*Wyróżnienia poza TOP 5:*
- **JOT-BE** – 470 ofert na Morizon, IG 1 076 obserwujących i 473 posty (https://www.instagram.com/jotbe_nieruchomosci_wroclaw/, 2026-11-11), wideo o historii biura na FB i argument „własny dział prawny”; TikTok @jotbe_nieruchomosci tylko 9 obserwujących i 9 filmów (https://www.tiktok.com/@jotbe_nieruchomosci, 2026-11-11).
- **Tecnocasa** – model hiperlokalny („dzielnica = oddział”), formularz wyceny „znamy lokalny rynek” (https://www.tecnocasa.pl/sprzedaj-nieruchomosc.html?contract=sprzedaz, 2026-11-11), ale małe profile (FB Grabiszyn 328, https://www.facebook.com/TecnocasaWroclaw/, 2026-11-11). W opiniach zarzuty o niejasną prowizję („3%”, a w praktyce „3,7% z VAT”, stare) – dowód, jak ważna jest przejrzystość kosztów.
- **Hamilton May** – filmy i spacery 3D w standardzie, 1. miejsce w autorskim zestawieniu rankingpro.pl (https://rankingpro.pl/ranking-biur-nieruchomosci-wroclaw/, 2026-11-11; serwis zastrzega, że pozycje mogą być odpłatne), ale segment premium, nie rodziny.

### 3a. Strony www sieci i biur – blog, wycena, lead magnety, wideo (odczyt 2026-11-11)

| Strona | Blog / poradniki | Wycena online | Lead magnety / narzędzia | Wideo |
|---|---|---|---|---|
| **metrohouse.pl** (partner) | Tak: blog (np. „Jak przygotować mieszkanie do sprzedaży, jeśli nadal w nim mieszkasz”), „Magazine”, aktualności, raporty | **Tak: wyceniarka** („Wystarczy tylko 5 minut!”, formularz → raport z wyceną, bezpłatnie) – https://www.metrohouse.pl/wycen | Kalkulator raty kredytu (/oblicz-rate-kredytu), raport **Barometr Metrohouse i Credipass** (30. wydanie, III kw. 2026), analizy np. Rodzinny Kredyt Mieszkaniowy w 18 miastach, strony „Dla kupujących” i „Dla sprzedających” | Kanał YouTube @metrohouse (link na stronie); IG ogólnopolski @okiem_metrohouse (nie sprawdzano liczb) |
| **iglica.pl** | Link „Blog” jest, ale strona zwraca błąd 500 | Nie znaleziono | Brak; lead przez wiadomość na IG (rolka z 6.11.2026) | Spacery 3D, kanał YouTube @IglicaNieruchomosciWRO |
| **www.tecnocasa.pl** | Brak w menu | Formularz kontaktowy „szybko i rzetelnie wycenimy Twoją nieruchomość” (nie automatyczna wyceniarka) | Brak | Nie znaleziono |
| **homfi** (www.homfi.com) | Zablokowane przez proxy; dane z pierwszej wersji: blog, Barometr homfi, poradniki | Wyceniarka (stare) | Wyceniarka (stare) | YouTube, TikTok |
| **RE/MAX** (www.remax.pl) | Nie dotyczy: www.remax.pl to strona innej firmy (REMAX-G, metalizacja); sieć RE/MAX to remax-polska.pl, zablokowana przez proxy | – | – | – |

**Dane z metrohouse.pl przydatne w treściach (cytować ze źródłem, bez zaokrągleń):**
- III kw. 2026: największy kwartalny wzrost średniej ceny ofertowej na rynku pierwotnym odnotowano we Wrocławiu – o 4,7%, do 16 026 zł/m² (dane BIG DATA RynekPierwotny.pl w raporcie Barometr Metrohouse i Credipass). Źródło: https://www.metrohouse.pl/ceny-mieszkan-w-iii-kwartale-2026 (2026-11-11).
- Indeks Cen Mieszkań Metrohouse w III kw. 2026: 218,3 pkt (+5,4% r/r); negocjacje obniżały cenę o 1,2–3,2%. Źródło: jw.
- Rodzinny Kredyt Mieszkaniowy, limity na IV kw. 2026: **we Wrocławiu w limicie mieści się 55% ofert z rynku wtórnego**; limit we Wrocławiu jest drugi najwyższy po Warszawie (dokładnej kwoty w tekście nie podano). Źródło: https://www.metrohouse.pl/rodzinny-kredyt-mieszkaniowy-gdzie-na-rynku-wtornym-najlatwiej-o-mieszkanie-w-limicie (2026-11-11).

---

## 4. Wnioski: czego brakuje na rynku

1. **Nikt z dużych graczy nie ma silnego, wrocławskiego profilu social media skierowanego do rodzin.** Największe zasięgi (homfi, Freedom) są ogólnopolskie, a lokalne profile mają setki, nie tysiące obserwujących.
2. **Brak spójnej estetyki premium na rynku średnim.** Premium (Hamilton May) celuje w ekspatów, a sieci (Tecnocasa, RE/MAX) mają rozproszone profile agentów i oddziałów. Czarno-złota, elegancka i spójna identyfikacja to wolne miejsce na rynku.
3. **Treści o dzielnicach i osiedlach Wrocławia angażują** (Realsy: ok. 2,3 tys. polubień i 163 komentarze pod jednym filmem; 15 600 polubień przy 656 obserwujących), ale robią je małe konta. Z większych biur tylko Iglica zaczęła publikować dane dla dzielnic (post o Psim Polu, 9.11.2026), ale w formie zwykłego posta, bez serii i bez perspektywy rodzin.
4. **Edukacja dla kupujących rodzin** (kredyt, koszty transakcji, odbiór mieszkania, szkoły i przedszkola w okolicy) jest rozproszona po blogach. Brak jej w formie krótkich rolek z napisami.
5. **Przejrzystość kosztów** (prowizja, PCC, notariusz) budzi emocje (opinie o Tecnocasa), a mało kto robi z niej treść.
6. **Dane rynkowe dla Wrocławia** publikuje homfi (Barometr), a Iglica pojedyncze posty o dzielnicach. Metrohouse z Credipass ma własne, świeże dane (np. III kw. 2026: Wrocław z największym kwartalnym wzrostem cen ofertowych na rynku pierwotnym, +4,7% do 16 026 zł/m²; 55% ofert z rynku wtórnego we Wrocławiu w limicie Rodzinnego Kredytu Mieszkaniowego), ale profil @metrohouse_wroclaw ich nie wykorzystuje (ostatnie posty: seria „Klucze jeszcze w tym roku”, 4–9 polubień).
7. **TikTok jest prawie niezagospodarowany przez duże sieci.** Freedom, Tecnocasa i Metrohouse Wrocław nie mają tam profili, homfi ma tylko 236 obserwujących. Najsilniejsze są biura lokalne: SDP (1 945 obserwujących, 20 tys. polubień), WRE (886, 18 700 polubień) i małe konta tematyczne (Realsy). Nikt nie łączy TikToka z edukacją dla rodzin.
8. **Wysokie zasięgi nie dają zaangażowania.** homfi przy 17 435 obserwujących na FB zbiera 2 reakcje pod postem; typowa rolka z ofertą WRE czy Iglicy ma 6–60 polubień. Wyjątki (rolka WRE z 1 449 polubieniami, rolka Iglicy z 7 komentarzami) mają mocny hook lub emocję („Widok z 8. piętra”), a nie same parametry.
9. **Wszyscy lokalni gracze mówią do odbiorców na „Ty”** (np. Iglica: „Wiesz…”, „Wyślij nam…”). Formalny, elegancki ton „Państwo” jest wyróżnikiem, a nie przeszkodą.

---

## 5. Rekomendacje („jak oni, ale lepiej”)

Wszystkie pomysły zgodne z przewodnikiem: format 9:16, bez twarzy (lektor lub napisy), ton formalny („Państwo”), czarno-złota paleta, muzyka pianino/chill z Epidemic Sound, plansza końcowa z logo i banerem Metrohouse.

| # | Pomysł | Format | Przykładowy temat / hook | Częstotliwość | Czym przebijamy konkurencję |
|---|---|---|---|---|---|
| 1 | **„Wrocław dla rodzin – dzielnica w 30 sekund”** | Rolka (lektor + napisy, ujęcia ulic, parków, szkół), potem karuzela z podsumowaniem | „Szukają Państwo mieszkania z dziećmi? Oto 3 powody, dla których rodziny wybierają Ołtaszyn.” | 1×/tydz. (seria) | Realsy robi „najgorsze dzielnice” z negatywnym nastawieniem. My robimy pozytywny, rzetelny przewodnik dla rodzin: szkoły, przedszkola, zieleń, dojazd. |
| 2 | **„Wrocławski barometr cen” co miesiąc** | Karuzela (6–8 slajdów, złote wykresy) i rolka 20 s z najważniejszą liczbą | „Wrocław z największym wzrostem cen nowych mieszkań w III kwartale. Co to oznacza dla Państwa?” (dane: +4,7% kw./kw., 16 026 zł/m², Barometr Metrohouse i Credipass) | 1×/mies. | homfi pokazuje dane ogólnopolskie, a Iglica pojedyncze posty. My dajemy serię tylko dla Wrocławia i dolnośląskiego, na danych partnera (Metrohouse/Credipass), z cytowanym źródłem i bez zaokrągleń. Każdą liczbę sprawdzić w aktualnym raporcie przed publikacją. |
| 3 | **Prezentacja oferty w stałej strukturze 5 kroków** | Rolka 30–45 s | „Trzy pokoje, balkon i szkoła za rogiem – [lokalizacja do uzupełnienia].” | 2×/tydz. (zależnie od ofert) | WRE ma stały szablon opisu („📍 Wrocław, dzielnica | ulica”), ale typowa rolka zbiera 10–60 polubień: hook to sam adres. U nas hook mówi o korzyści dla rodziny (jak u Iglicy „Widok z 8. piętra”, która zebrała najwięcej komentarzy), a cała rolka ma stałą oprawę: hook, ujęcia, karta danych, CTA, plansza końcowa. Marka rozpoznawalna po 1 sekundzie. |
| 4 | **„Koszty bez niespodzianek”** | Karuzela i rolka z napisami | „Kupują Państwo mieszkanie za [cena]. Ile wyniosą koszty dodatkowe? Wyliczamy krok po kroku.” | 2×/mies. | Konkurencja unika tematu prowizji i kosztów. Pełna przejrzystość pasuje do nazwy „bez stresu” i odpowiada na zarzuty widoczne w opiniach o innych biurach. |
| 5 | **„Checklista przed zakupem” – lead magnet** | PDF w Canva (czarno-złoty) i rolka zapowiadająca; CTA: „Proszę napisać CHECKLISTA w wiadomości” | „5 rzeczy, które należy sprawdzić w księdze wieczystej przed podpisaniem umowy.” | Rolka 1×/mies.; PDF stale w bio | homfi i Metrohouse mają wyceniarki dla sprzedających (dla sprzedających kierujemy do wyceniarki Metrohouse: https://www.metrohouse.pl/wycen). Iglica testuje lead przez wiadomość prywatną, ale tylko z rabatem dewelopera (rolka z 6.11.2026: 4 komentarze). Nikt nie ma prostego lead magnetu **dla kupujących rodzin**. |
| 6 | **„Pytanie od Państwa” – odpowiedzi eksperckie** | Rolka z napisami (pytanie na planszy, odpowiedź lektora) | „Czy mieszkanie z rynku wtórnego wymaga inspekcji technicznej?” | 1×/tydz. | Freedom robi długie podcasty. My dajemy odpowiedzi w 30 sekund, bez twarzy, z napisami, łatwe do zapisania. |
| 7 | **„Sprzedali Państwo z nami” – opinie klientów bez twarzy** | Rolka: ujęcie kluczy, drzwi, pudeł; cytat opinii na planszy (za zgodą klienta) | „Sprzedaż w [liczba dni do uzupełnienia] dni. Oto, co powiedzieli nasi klienci.” | 2×/mies. | WRE pokazuje liczbę opinii. My pokazujemy historie z emocjami, w spójnej oprawie premium. |
| 8 | **„Za kulisami – jak przygotowujemy mieszkanie do sprzedaży”** | Rolka przed/po (porządek, światło, kadr) | „To samo mieszkanie, dwa zdjęcia. Która wersja sprzeda się szybciej?” | 2×/mies. | Hamilton May ma home staging tylko dla premium. My pokazujemy to na rynku średnim jako dowód jakości pracy. |
| 9 | **„Słownik bez stresu”** | Karuzela lub krótka rolka (1 pojęcie, 15 s) | „Co to jest umowa przedwstępna i czym różni się od rezerwacyjnej?” | 1×/tydz. | Blogi konkurencji są długie i stare. My stawiamy na krótki, aktualny, łatwy do zapisania format. |
| 10 | **„Dolnośląskie poza miastem”** – domy dla rodzin pod Wrocławiem | Rolka (dojazd, okolica, przyroda) | „Dom z ogrodem, 25 minut od Rynku. Gdzie szukać pod Wrocławiem?” | 2×/mies. | Konkurencja skupia się na mieście. Strefa podmiejska (Kąty Wrocławskie, Siechnice, Długołęka) to naturalny temat dla rodzin, a Metrohouse ma oddział w Kątach Wrocławskich. |
| 11 | **Seria TikTok „1 minuta o rynku”** | TikTok i Shorts (te same rolki 9:16) | „Czy w listopadzie warto negocjować cenę? Trzy argumenty.” (dane: negocjacje obniżały cenę o 1,2–3,2%, Barometr Metrohouse i Credipass, III kw. 2026) | 3×/tydz. (recykling rolek) | Duże sieci nie mają aktywnego TikToka; lokalne SDP i WRE pokazują tam głównie wnętrza i oferty. Wchodzimy jako pierwszy elegancki profil z edukacją dla rodzin. Punkt odniesienia na start: ok. 900–2 000 obserwujących (WRE, SDP). |
| 12 | **Jeden profil, jedna marka** | Zasada organizacyjna | – | Stale | Konkurenci rozpraszają się na profile oddziałów i agentów. My prowadzimy jeden spójny profil na każdej platformie, z jednym stylem i jednym CTA. Lokalny profil Metrohouse Wrocław ma 88 obserwujących na IG, więc to „Nieruchomości bez stresu” może być głównym kanałem tej współpracy. |
| 13 | **NOWE: „Czy to mieszkanie mieści się w Rodzinnym Kredycie Mieszkaniowym?”** | Rolka z napisami (lektor) i karuzela; przy ofercie dodatkowa plansza „w limicie RKM: tak/nie” | „Ponad połowa mieszkań z rynku wtórnego we Wrocławiu mieści się w limicie Rodzinnego Kredytu Mieszkaniowego. Jak sprawdzić, czy Państwa wybór także?” (dane: 55% ofert, Metrohouse i Credipass, limity na IV kw. 2026) | 2×/mies. + przy ofertach w limicie | Temat wprost dla rodzin; w odczytanych postach biur z zestawienia go nie znaleziono (sprawdzono tylko kilka ostatnich postów na konto). Dane od partnera (Metrohouse/Credipass). Limit i kwalifikowalność każdej oferty sprawdzić w aktualnym komunikacie BGK przed publikacją; ceny i metraże dokładnie według oferty. |

---

## 6. Plan tygodniowy (FB + IG + TikTok)

Założenie: ok. 4 nowe rolki tygodniowo, publikowane równolegle na IG Reels, FB Reels i TikToku, plus 2 karuzele lub posty statyczne.

| Dzień | Instagram | Facebook | TikTok |
|---|---|---|---|
| **Poniedziałek** | Rolka: „Pytanie od Państwa” (#6) | Ta sama rolka + krótki opis | Ta sama rolka |
| **Wtorek** | Karuzela: „Słownik bez stresu” (#9) | Ta sama karuzela (album zdjęć) | Wersja w trybie zdjęć (Photo Mode) |
| **Środa** | Rolka: prezentacja oferty (#3) | Rolka + post z linkiem do oferty | Ta sama rolka |
| **Czwartek** | Rolka: „Wrocław dla rodzin – dzielnica” (#1) | Ta sama rolka; pytanie do społeczności („Jaką dzielnicę pokazać następną?”) | Ta sama rolka |
| **Piątek** | Rolka: prezentacja oferty (#3) lub „Za kulisami” (#8) | Ta sama rolka | Ta sama rolka |
| **Sobota** | Karuzela: „Koszty bez niespodzianek” (#4) lub opinia klienta (#7) | Ta sama treść | „1 minuta o rynku” (#11) – recykling |
| **Niedziela** | Relacje (Stories): przypomnienie oferty tygodnia + ankieta | Brak publikacji / odpowiedzi na komentarze | Brak publikacji |

Raz w miesiącu: „Wrocławski barometr cen” (#2), zamiast karuzeli wtorkowej w pierwszym tygodniu. Do tego rolka z lead magnetem (#5) i „Dolnośląskie poza miastem” (#10) w miejsce rolki czwartkowej w co drugim tygodniu. Nowy temat „Rodzinny Kredyt Mieszkaniowy” (#13) 2× w miesiącu w miejsce sobotniej karuzeli (na zmianę z #4 i #7).

Punkt odniesienia z aktualizacji: najaktywniejsze lokalne konta (WRE, Iglica) publikują ok. 4–5 razy w tygodniu na IG, głównie rolki. Zaplanowane ok. 4 rolki + 2 karuzele tygodniowo to ten sam poziom, ale z większym udziałem treści edukacyjnych.

Godziny publikacji ustalić po pierwszych 4 tygodniach na podstawie statystyk kont. Nie da się ich wiarygodnie ustalić z danych konkurencji.

---

## 7. Trzy pomysły na rolki (struktura 5 kroków z CLAUDE.md)

### Rolka A – Prezentacja oferty dla rodziny

1. **Hook (0–3 s):** napis złotymi wersalikami na ciemnym tle: „Mieszkanie dla rodziny w [dzielnica – do uzupełnienia]?”. Lektor: „Szukają Państwo przestrzeni dla całej rodziny? Proszę zobaczyć to mieszkanie.”
2. **Prezentacja (3–20 s):** płynne, wypoziomowane ujęcia w naturalnym świetle: wejście, salon, kuchnia, pokój dziecięcy, balkon. Napisy z wyróżnieniem kluczowego atutu: [do uzupełnienia, np. „zielone podwórko”].
3. **Kluczowe dane (20–27 s):** karta z Canva: metraż [do uzupełnienia] · liczba pokoi [do uzupełnienia] · lokalizacja [do uzupełnienia] · cena [do uzupełnienia]. Bez zaokrągleń, dokładnie według oferty.
4. **CTA (27–32 s):** lektor: „Zapraszamy na prezentację. Proszę zadzwonić lub napisać wiadomość.”
5. **Plansza końcowa (32–36 s):** logo „Nieruchomości bez stresu” i baner kontaktowy: Maciej Styczek, METROHOUSE Wrocław, tel. 572 518 617, mstyczek@metrohouse.pl.

Muzyka: spokojne pianino (Epidemic Sound), wyraźnie pod lektorem.

### Rolka B – „Wrocław dla rodzin: dzielnica w 30 sekund”

1. **Hook (0–3 s):** napis: „Trzy powody, dla których rodziny wybierają [dzielnica – do uzupełnienia]”. Lektor wypowiada to samo.
2. **Prezentacja (3–20 s):** ujęcia dzielnicy: park lub plac zabaw, okolice szkoły i przedszkola, przystanek tramwajowy, osiedle. Każdy powód to osobna plansza z numerem 1/2/3 (złote cyfry). Fakty o dzielnicy sprawdzić przed publikacją.
3. **Kluczowe dane (20–26 s):** plansza „Na co zwrócić uwagę w tej dzielnicy”: przykładowy przedział cen z aktualnej oferty [do uzupełnienia, tylko na podstawie realnych ofert], typowy metraż w ofercie [do uzupełnienia], czas dojazdu do centrum [do uzupełnienia, po sprawdzeniu].
4. **CTA (26–31 s):** lektor: „Chcą Państwo zobaczyć oferty w tej dzielnicy? Proszę napisać do nas wiadomość.”
5. **Plansza końcowa (31–35 s):** logo i baner kontaktowy Metrohouse.

### Rolka C – „Koszty bez niespodzianek” (edukacyjna)

1. **Hook (0–3 s):** napis: „Cena mieszkania to nie wszystko. Ile naprawdę Państwo zapłacą?”
2. **Prezentacja (3–20 s):** spokojne ujęcia: dokumenty na stole, klucze, długopis. Kolejne plansze z napisami: podatek PCC (rynek wtórny), taksa notarialna i opłaty sądowe, prowizja biura, koszty kredytu (jeśli dotyczy). Bez twarzy, tylko lektor i napisy.
3. **Kluczowe dane (20–27 s):** przykład liczbowy na konkretnej ofercie: cena [do uzupełnienia], metraż [do uzupełnienia], liczba pokoi [do uzupełnienia], lokalizacja [do uzupełnienia], koszty dodatkowe [do wyliczenia według obowiązujących stawek, sprawdzonych przed publikacją].
4. **CTA (27–32 s):** lektor: „Przygotujemy dla Państwa pełne wyliczenie kosztów dla wybranej oferty. Zapraszamy do kontaktu.”
5. **Plansza końcowa (32–36 s):** logo i baner kontaktowy Metrohouse.

---

## 8. Źródła

**Źródła odczytane bezpośrednio w aktualizacji (data odczytu: 2026-11-11)**
- Morizon, katalog biur Wrocławia (233 biura, sortowanie wg liczby ofert, strony 1–12): https://www.morizon.pl/biura-nieruchomosci/wroclaw/
- Morizon, profile: https://www.morizon.pl/biuro-nieruchomosci/sdp-nieruchomosci-21445, https://www.morizon.pl/biuro-nieruchomosci/wgn-nieruchomosci-22440, https://www.morizon.pl/biuro-nieruchomosci/jot-be-nieruchomosci-sp-z-o-o-4224
- RankingPRO (zestawienie 2026): https://rankingpro.pl/ranking-biur-nieruchomosci-wroclaw/
- Metrohouse: https://www.metrohouse.pl/, https://www.metrohouse.pl/wycen, https://www.metrohouse.pl/ceny-mieszkan-w-iii-kwartale-2026, https://www.metrohouse.pl/rodzinny-kredyt-mieszkaniowy-gdzie-na-rynku-wtornym-najlatwiej-o-mieszkanie-w-limicie, https://www.instagram.com/metrohouse_wroclaw/, https://www.facebook.com/metrohouseWroclaw/, https://www.tiktok.com/@metrohouse
- Iglica: https://iglica.pl/, https://iglica.pl/blog/ (błąd 500), https://www.instagram.com/witajwiglica/, https://www.facebook.com/witajwiglica/
- Tecnocasa: https://www.tecnocasa.pl/, https://www.tecnocasa.pl/sprzedaj-nieruchomosc.html?contract=sprzedaz, https://www.facebook.com/TecnocasaWroclaw/
- homfi: https://www.facebook.com/homficom/, https://www.instagram.com/homfi_com/, https://www.tiktok.com/@homfi_com
- Freedom: https://www.instagram.com/freedom_nieruchomosci_/
- WRE: https://www.facebook.com/wrenieruch/, https://www.instagram.com/wre_nieruchomosci/, https://www.tiktok.com/@wre_nieruchomosci
- JOT-BE: https://www.facebook.com/biurojotbe/, https://www.instagram.com/jotbe_nieruchomosci_wroclaw/, https://www.tiktok.com/@jotbe_nieruchomosci
- SDP: https://www.tiktok.com/@sdp.nieruchomosci
- KONCEPT: https://www.instagram.com/konceptnieruchomosci/
- Konta inspiracyjne: https://www.tiktok.com/@realsy_management, https://www.tiktok.com/@nieruchomosci.wroclaw
- Pojedyncze posty IG: adresy podane przy postach w sekcjach 2 i 3.
- Hosty niedostępne: www.otodom.pl (403 CloudFront), gratka.pl/biura-nieruchomosci/wroclaw (401), www.homfi.com, remax-polska.pl i tecnocasa.pl bez „www” (blokada proxy), www.remax.pl (inna firma).

**Źródła z pierwszej wersji raportu**

Te źródła odczytano za pomocą wyszukiwarki (podglądy i fragmenty stron). Nie otwierano ich wtedy bezpośrednio, bo sieć sesji była zablokowana.

**Rankingi i agregatory**
- https://rankingpro.pl/ranking-biur-nieruchomosci-wroclaw/
- https://sonarhome.pl/agencje-nieruchomosci/wroclaw
- https://tabelaofert.pl/katalog-firm/agencje-nieruchomosci/homfi
- https://tabelaofert.pl/katalog-firm/agencje-nieruchomosci/jot-be
- https://tabelaofert.pl/katalog-firm/agencje-nieruchomosci/wrenieruchomosci
- https://www.nieruchomosci-online.pl/biura-nieruchomosci/

**Metrohouse (punkt odniesienia)**
- https://www.instagram.com/metrohouse_wroclaw/
- https://www.facebook.com/metrohouseWroclaw/
- https://www.facebook.com/metrohousewroclawcentrum/
- https://www.facebook.com/metrohousekatywroclawskie/
- https://www.otodom.pl/pl/firmy/biura-nieruchomosci/metrohouse-ID5125668

**Freedom**
- https://freedom.pl/biuro/wroclaw/
- https://freedom.pl/biuro/oddzial-wroclaw-krzyki/
- https://sprzedaj.freedom.pl/biuro/biuro-nieruchomosci-wroclaw-centrum
- https://www.facebook.com/FreeDOMwroclaw/
- https://www.facebook.com/p/Freedom-Nieruchomo%C5%9Bci-Oddzia%C5%82-Wroc%C5%82aw-Krzyki-61554148066377/
- https://www.facebook.com/people/Freedom-Nieruchomo%C5%9Bci-Oddzia%C5%82-Wroc%C5%82aw-Centrum/100083322341500/
- https://www.instagram.com/freedom_nieruchomosci_/
- https://freedom.pl/blog/
- https://freedom.pl/blog/jak-wycenic-nieruchomosc/
- https://freedom.pl/blog/wycena-nieruchomosci-jak-to-zrobic/
- https://open.spotify.com/show/6yIbjpZEU85GDvJ7wA3uPH
- https://www.youtube.com/channel/UCrWYnP275flZyxOl_90lQ6Q

**Tecnocasa**
- https://tecnocasa.pl/biura/tecnocasa-krzyki-wroclaw/
- https://tecnocasa.pl/darmowa-wycena/
- https://www.facebook.com/TecnocasaWroclaw/
- https://www.facebook.com/people/Tecnocasa-Oddzia%C5%82-I-Wroc%C5%82aw-Studio-Krzyki/100084239918003/
- https://www.facebook.com/profile.php?id=100094481276157
- https://www.facebook.com/TecnocasaPrzedmiescieOlawskie
- https://www.instagram.com/tecnocasa_krzyki/
- https://ratingcaptain.com/pl/opinie/198201/tecnocasa-pl

**homfi**
- https://www.homfi.com/en/about-us/who-we-are
- https://www.homfi.com/blog
- https://www.homfi.com/mozliwosci
- https://www.homfi.com/blog/barometr-nieruchomosci-maj-2026
- https://www.homfi.com/blog/zakup-mieszkania-z-rynku-wtornego
- https://www.facebook.com/homficom/
- https://www.instagram.com/homfi_com/
- https://www.youtube.com/channel/UCyOplDf7SPNoSEXwZguGO0g
- https://www.facebook.com/people/Jacek-Drewicz-agent-nieruchomo%C5%9Bci-homfi-Wroc%C5%82aw/100078775453532/

**RE/MAX**
- https://www.remax-polska.pl/en/offices/dolnoslaskie/wroclaw/remax-speedway-ii/80018
- https://www.remax-polska.pl/pl-pl/biura/dolnoslaskie/wroclaw/remax-sunix/47034
- https://www.facebook.com/remax.speedway.wroclaw/
- https://www.remax-polska.pl/kinga_szostek

**Hamilton May**
- https://www.hamiltonmay.pl/wroclaw
- https://www.hamiltonmay.pl/blog
- https://www.hamiltonmay.pl/post/hamilton-may-partnerem-raportu-z-wyszej-polki
- https://www.otodom.pl/wiadomosci/profesjonalisci/posrednicy/hamilton-may-eksperci-od-wymagajacych-rynkow
- https://pl.linkedin.com/company/hamilton-may-real-estate-company

**Iglica**
- https://iglica.pl/
- https://www.facebook.com/witajwiglica/
- https://tabelaofert.pl/iglica
- https://rynekpierwotny.pl/deweloperzy/iglica-nieruchomosci-3749/

**WRE Nieruchomości**
- https://wrenieruchomosci.pl/mieszkania
- https://www.facebook.com/wrenieruch/
- https://www.instagram.com/wre_nieruchomosci/
- https://wrenieruchomosci.oferteo.pl/
- https://www.aplikuj.pl/pracodawca/386663/wre-biuro-nieruchomosci-sp-z-o-o/opinie

**JOT-BE**
- https://jot-be.pl/
- https://jot-be.pl/agenci/
- http://jot-be.pl/zespol/
- http://jot-be.pl/o-nas/dlaczego-warto/
- https://web.facebook.com/biurojotbe/
- https://www.facebook.com/people/JotBeEstateKW/100066631639463/
- https://www.facebook.com/biurojotbe/videos/jot-be-historia-biura/2858259951071774/
- https://www.facebook.com/biurojotbe/videos/kup-z-jot-be-nieruchomo%C5%9Bci/343131590286138/

**Verso**
- https://www.verso.com.pl/
- https://www.instagram.com/verso__nieruchomosci/
- https://www.facebook.com/people/Verso-Nieruchomo%C5%9Bci/100051473456988/

**KONCEPT**
- https://www.konceptnieruchomosci.pl/
- https://www.instagram.com/konceptnieruchomosci/
- https://www.facebook.com/profile.php?id=100063738332262

**Konta lokalne (inspiracje)**
- https://www.tiktok.com/@realsy_management/video/7494324772868836630
- https://www.tiktok.com/@sdp.nieruchomosci
- https://www.tiktok.com/@nieruchomosci.wroclaw
- https://www.instagram.com/agentstumostow/

**Dane rynkowe (do barometru)**
- https://nskup.pl/raport-cen-mieszkan-wroclaw/2026-10/
- https://wroclife.pl/amp/artykul/8700/ceny-mieszkan-we-wroclawiu-w-gore-w-innych-miastach-przegrywaja-z-inflacja
- https://sonarhome.pl/ceny-mieszkan/wroclaw
- https://ceo.com.pl/ceny-na-rynku-wtornym-mieszkan-w-ii-kw-2026
