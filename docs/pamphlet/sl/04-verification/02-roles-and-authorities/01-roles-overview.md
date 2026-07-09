---
title: "Roles Overview"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Pregled vlog

Nekaterih od teh vlog smo se že na kratko dotaknili v poglavju o omrežju in njegovih osnovnih lastnostih. Zdaj je čas, da si jih znova ogledamo podrobneje in dodamo dodatne, ki jih potrebujemo, da omrežje naredimo robustnejše. Vsaka transakcija preverjanja vključuje več vlog — poglejmo, kako se obnašajo.

> [!note] Vloge v transakciji preverjanja
> Vsako preverjanje vključuje do šest različnih vlog, povzetih v spodnji tabeli. Vse imajo lahko svoj DID v decentraliziranem reputacijskem omrežju.

| Vloga | Opis |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Izdajatelj** | Oseba, ki objavlja informacije v omrežje — trdi, da se je nekaj zgodilo (DID je bil ustvarjen, urejen ali razpuščen, trditev, politika danega DID itd.) |
| **Subjekt** | Oseba, o kateri je informacija — naslovnik trditve |
| **Avtoriteta** | Zaupanja vreden entitet, ki na kakovost trditve stavi svoje ime, tako da jo preišče in bodisi pregleda predložene dokaze bodisi jih aktivno zbira |
| **Opazovalec** | Neodvisna tretja stran, ki vodi zapis o tem, kako preveritelj ravna s trditvijo — pri čemer skrbi, da preveritelj niti ne molči niti ne odstopa od politike, ki jo je deklariral |
| **Preveritelj** | Algoritemsko izbran udeleženec, ki obdela transakcijo |
| **Delegat** | Oseba, ki deluje v imenu drugega udeleženca |
