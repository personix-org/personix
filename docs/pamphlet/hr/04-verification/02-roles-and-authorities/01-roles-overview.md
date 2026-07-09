---
title: "Pregled uloga"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Pregled uloga

Neke smo od tih uloga već ukratko dotaknuli u poglavlju o mreži i njezinim osnovnim svojstvima. Sada je vrijeme da ih ponovno pogledamo podrobnije i dodamo dodatne koje su nam potrebne da mrežu učinimo robusnijom. Svaka transakcija provjere uključuje nekoliko uloga — pogledajmo kako se ponašaju.

> [!note] Uloge u transakciji provjere
> Svaka provjera uključuje do šest različitih uloga, sažetih u tablici u nastavku. Sve one mogu imati vlastiti DID u decentraliziranoj reputacijskoj mreži.

| Uloga | Opis |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Izdavatelj** | Osoba koja objavljuje informacije u mrežu — tvrdi da se nešto dogodilo (DID je stvoren, izmijenjen ili raspušten, tvrdnja, politika danog DID-a itd.) |
| **Subjekt** | Osoba o kojoj je informacija — adresat tvrdnje |
| **Autoritet** | Pouzdan entitet koji ulaže svoje ime u kvalitetu tvrdnje istražujući je i bilo pregledavajući iznesene dokaze bilo ih aktivno prikupljajući |
| **Promatrač** | Neovisna treća strana koja vodi zapis o tome kako verifikator postupa s tvrdnjom — pazeći da verifikator niti šuti niti odstupa od politike koju je deklarirao |
| **Verifikator** | Algoritamski odabran sudionik koji obrađuje transakciju |
| **Delegat** | Osoba koja djeluje u ime drugog sudionika |
