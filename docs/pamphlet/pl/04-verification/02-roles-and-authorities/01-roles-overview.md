---
title: "Przegląd ról"
chapter: 3
part: "Jak działa weryfikacja"
lang: pl
version: v6
---

# Przegląd ról

O niektórych z tych ról wspomnieliśmy już pokrótce w rozdziale o sieci i jej podstawowych właściwościach. Teraz jest czas, by przyjrzeć się im ponownie, dokładniej, i dodać kolejne, których potrzebujemy, by uczynić sieć bardziej odporną. Każda transakcja weryfikacyjna angażuje kilka ról — zobaczmy, jak się zachowują.

> [!note] Role w transakcji weryfikacyjnej
> Każda weryfikacja angażuje do sześciu odrębnych ról, podsumowanych w poniższej tabeli. Wszystkie mogą mieć własny DID w zdecentralizowanej sieci reputacji.

| Rola | Opis |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Wystawca** | Osoba, która publikuje informację w sieci — twierdzi, że coś się wydarzyło (utworzono, zmodyfikowano lub rozwiązano DID, teza, polityka danego DID itd.) |
| **Podmiot** | Osoba, której informacja dotyczy — adresat tezy |
| **Autorytet** | Zaufany podmiot, który stawia swoje imię na jakości tezy, badając ją i albo przeglądając przedstawione dowody, albo aktywnie je zbierając |
| **Obserwator** | Niezależna strona trzecia, która prowadzi zapis tego, jak weryfikator obchodzi się z tezą — pilnując, by weryfikator ani nie milczał, ani nie odchodził od zadeklarowanej polityki |
| **Weryfikator** | Wybrany algorytmicznie uczestnik, który przetwarza transakcję |
| **Delegat** | Osoba działająca w imieniu innego uczestnika |
