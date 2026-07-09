---
title: "Słownik pojęć"
part: "Dodatek"
lang: pl
version: v6
---

# Słownik pojęć

| Pojęcie | Polski | Znaczenie |
|------|-------|---------|
| **Authority** | Autorytet | Zaufany podmiot (osoba, organizacja), który weryfikuje informacje i stawia na nie swoją reputację. Może być wyspecjalizowany (śledczy, prawny, techniczny). |
| **Claim** | Teza | Ogólnie: dowolne weryfikowalne stwierdzenie. Tutaj: zapis opublikowany w sieci reputacji — twierdzenie o zdarzeniu, właściwości lub relacji, kryptograficznie podpisane i zweryfikowane. Np. „jestem mieszkańcem gminy X” albo „ta osoba naruszyła umowę”. |
| **Compartmentalization** | Kompartmentalizacja | Ogólnie: oddzielanie informacji na izolowane jednostki tak, by ujawnienie jednej jednostki nie skompromitowało pozostałych. Zasada znana ze służb wywiadowczych. Tutaj: równoległe tożsamości DID w dyktaturach — skompromitowanie jednej nie ujawnia pozostałych. |
| **Consistent Hash Ring** | Pierścień haszujący | Algorytmiczny mechanizm wyboru weryfikatorów — pozycję na pierścieniu wyznacza hash dokumentu DID w obrębie grafu społecznego. Zapewnia niedeterministyczny, a zarazem weryfikowalny wybór. |
| **DID** | DID (Tożsamość zdecentralizowana) | Cyfrowa tożsamość, którą tworzysz i kontrolujesz sam, bez centralnej władzy. Kryptograficznie podpisana twoim kluczem prywatnym — nikt nie może jej cofnąć ani podrobić. |
| **DID Document** | Dokument DID | Publicznie dostępny plik danych opisujący twoją tożsamość DID — zawiera klucze publiczne, adresy sieciowe i metadane. Służy do weryfikacji twojej tożsamości w sieci. |
| **Due Diligence** | Due diligence | Ogólnie: dogłębna weryfikacja drugiej strony przed wejściem w relację biznesową lub prawną — sprawdzenie jej historii, finansów, reputacji i ryzyk. Tutaj: w sieci reputacji odbywa się szybciej i bardziej automatycznie dzięki dostępności zweryfikowanych zapisów. |
| **Economic Neutrality Principle** | Zasada neutralności ekonomicznej | Uczciwe zachowanie w sieci jest ekonomicznie bliskie zeru — koszty publikacji zwracają się jako nagrody za weryfikację. Nieuczciwe zachowanie jest czystą stratą. |
| **Emergent** | Emergentny | Spontanicznie powstający z interakcji prostszych części, bez niczyjego projektu ani sterowania. Klucz ptaków leci w formacji bez planu — formacja wyłania się z prostych reguł, których przestrzega każdy osobnik. |
| **Emergent Social Contract** | Emergentna umowa społeczna | Reguły zachowania powstające nie z góry (prawo), lecz z dołu — z powtarzanych interakcji i konsensusu wewnątrz wspólnoty. |
| **ESR** | Elektroniczny rejestr wydatków | Proponowany system przejrzystego śledzenia wydatków publicznych — każdy zrealizowany wydatek państwa jest dopasowany do planowanej płatności. Zainspirowany czeskim EET, ale odwrócony przeciw państwu. |
| **Hash** | Hash (odcisk) | Ogólnie: jednokierunkowa funkcja matematyczna, która z dowolnego wejścia wytwarza unikalny „odcisk” o stałej długości — jak odcisk palca dokumentu. To samo wejście zawsze daje to samo wyjście, ale z wyjścia nie da się wyprowadzić wejścia. Tutaj: używany do wyznaczenia pozycji na pierścieniu haszującym i do weryfikacji integralności dokumentu. |
| **Just-in-Time Funding** | Finansowanie just-in-time | Finansowanie państwa uwarunkowane przejrzystością — pieniądze płyną tylko wtedy, gdy państwo przyjmuje ESR i dopasowuje swoje wydatki. Dźwignia zmuszająca do współpracy. |
| **Meritocracy** | Merytokracja | Ogólnie: system, w którym pozycję wyznaczają faktyczne zasługi i udowodnione umiejętności, a nie formalne tytuły, koneksje czy odziedziczony przywilej. Tutaj: sieć reputacji naturalnie faworyzuje tych, którzy w dowodliwy sposób wnoszą wkład do wspólnoty — ich głos ma większą wagę dzięki track recordowi, a nie urzędowi. |
| **Onion Gateway** | Onion gateway | Adres sieciowy tożsamości DID w sieci onion. Oddzielny od dokumentu DID — można go zmienić bez utraty tożsamości (podobnie jak zmiana adresu IP za domeną). |
| **Onion Routing** | Onion routing (Tor) | Protokół komunikacyjny zapewniający niecenzurowalność sieci. Wiadomości są szyfrowane warstwami — każdy węzeł zdejmuje jedną warstwę, ale nie zna pełnej trasy. |
| **Oracle Problem** | Problem wyroczni | Ogólnie: jak zapewnić, by dane wchodzące do systemu cyfrowego wiernie odpowiadały temu, co faktycznie wydarzyło się w świecie fizycznym. Termin pochodzi z domeny blockchaina. Tutaj: rozwiązywany poprzez autorytety, które stawiają swoją reputację jako gwarancję, że zapis cyfrowy odpowiada rzeczywistości fizycznej. |
| **Phenomenological** | Fenomenologiczny | Ogólnie: podejście badające zjawiska tak, jak przejawiają się w bezpośrednim doświadczeniu, poprzez obserwację tego, co z nich wynika, bez z góry danych teorii. Tutaj: wolność, umowa społeczna i normy zachowania są obserwowanymi zjawiskami — konsekwencjami tysięcy mikrointerakcji między ludźmi, a nie zasadami definiowanymi z góry. |
| **Policy** | Policy (polityka) | Ogólnie: zbiór reguł lub zasad rządzących zachowaniem w danym kontekście. Tutaj: każdy uczestnik sieci DID deklaruje swoją politykę — jak reaguje na konkretne zachowania innych, których reguł przestrzega i które kary uznaje za proporcjonalne. Suma polityk tworzy emergentną umowę społeczną. |
| **Proxy** | Proxy | Ogólnie: zastępca lub pośrednik — system lub podmiot działający w imieniu innego. Używane tu w dwóch kontekstach: (1) ESR jako proxy dopasowujące wydatki publiczne do planowanych płatności; (2) obserwatorzy jako proxy między wydawcą a weryfikatorem w triku z obserwatorem. |
| **Publisher** | Wydawca | Uczestnik sieci, który tworzy i publikuje zapis (tezę o niesprawiedliwości, naprawie itd.). Ponosi koszt publikacji. |
| **Reputation-Based Social Network (RSN)** | Sieć reputacji | Zdecentralizowana sieć społecznościowa, w której uczestnicy wymieniają informację zwrotną o zachowaniu w świecie rzeczywistym. Zapisy są kosztowne do utworzenia, tanie do przeczytania. |
| **Reputation Signal** | Sygnał reputacyjny | Pojedynczy zapis w sieci — pozytywny (naprawa krzywdy, wypełnienie zobowiązania) lub negatywny (niesprawiedliwość, naruszenie umowy). Kumulatywnie sygnały tworzą profil reputacyjny. |
| **Social Graph** | Graf społeczny | Sieć twoich kontaktów i kontaktów twoich kontaktów. Algorytm szuka weryfikatorów na konfigurowalnej głębokości (na przykład 3 poziomy). Brak globalnego blockchaina — sieć naturalnie tworzy wspólnoty z zazębieniami. |
| **Tax Allocation** | Alokacja podatków | Mechanizm, dzięki któremu podatnik decyduje, dokąd trafia część jego podatków. Procent możliwy do zaalokowania rośnie rok do roku. |
| **Track Record** | Track record | Ogólnie: historia dotychczasowych wyników, sukcesów i porażek osoby lub organizacji. Tutaj: suma wszystkich dotychczasowych interakcji danej tożsamości DID w sieci — zweryfikowanych tez, przyjętych i odrzuconych zapisów — z których wywodzi się jej reputacja. |
| **Verifier** | Weryfikator | Uczestnik wybrany algorytmicznie do zweryfikowania i opublikowania zapisu. Stawia swoje dobre imię na prawdziwości informacji. |
