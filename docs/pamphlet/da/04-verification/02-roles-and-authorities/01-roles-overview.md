---
title: "Roles Overview"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Oversigt over roller

Vi berørte allerede kort nogle af disse roller i kapitlet om netværket og dets grundlæggende egenskaber. Nu er tiden inde til at se på dem igen mere detaljeret og tilføje de yderligere, vi har brug for, for at gøre netværket mere robust. Hver verifikationstransaktion involverer flere roller — lad os se, hvordan de opfører sig.

> [!note] Roller i en verifikationstransaktion
> Hver verifikation involverer op til seks særskilte roller, opsummeret i tabellen nedenfor. De kan alle have deres egen DID i det decentraliserede omdømmenetværk.

| Rolle | Beskrivelse |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Udsteder** | Den person, der offentliggør information til netværket — påstår, at noget skete (en DID blev skabt, redigeret eller opløst, en påstand, en given DID's politik osv.) |
| **Subjekt** | Den person, informationen handler om — påstandens adressat |
| **Autoritet** | En betroet enhed, der sætter sit navn på spil for påstandens kvalitet ved at undersøge den og enten gennemgå det fremlagte bevis eller aktivt indsamle det |
| **Observatør** | En uafhængig tredjepart, der fører optegnelse over, hvordan verifikatoren håndterer påstanden — og sikrer, at verifikatoren hverken forbliver tavs eller afviger fra den politik, de erklærede |
| **Verifikator** | En algoritmisk udvalgt deltager, der behandler transaktionen |
| **Delegat** | En person, der handler på vegne af en anden deltager |
