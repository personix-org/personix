---
title: "Roles Overview"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Översikt över rollerna

Vi berörde redan kort några av dessa roller i kapitlet om nätverket och dess grundläggande egenskaper. Nu är det dags att se på dem igen mer i detalj och lägga till de ytterligare som vi behöver för att göra nätverket mer robust. Varje verifieringstransaktion involverar flera roller — låt oss se hur de beter sig.

> [!note] Roller i en verifieringstransaktion
> Varje verifiering involverar upp till sex distinkta roller, sammanfattade i tabellen nedan. Alla kan ha sin egen DID i det decentraliserade anseendenätverket.

| Roll | Beskrivning |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Utfärdare** | Den person som publicerar information till nätverket — påstår att något hände (en DID skapades, redigerades eller upplöstes, ett påstående, en given DID:s policy osv.) |
| **Subjekt** | Den person informationen handlar om — påståendets adressat |
| **Auktoritet** | En betrodd entitet som sätter sitt namn på spel för påståendets kvalitet genom att utreda det och antingen granska de framlagda bevisen eller aktivt samla in dem |
| **Observatör** | En oberoende tredje part som för en anteckning om hur verifieraren hanterar påståendet — och ser till att verifieraren varken tiger eller avviker från den policy de deklarerat |
| **Verifierare** | En algoritmiskt utvald deltagare som bearbetar transaktionen |
| **Delegat** | En person som agerar å en annan deltagares vägnar |
