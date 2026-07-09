---
title: "Roles Overview"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Oversikt over rollene

Vi berørte allerede noen av disse rollene kort i kapittelet om nettverket og dets grunnleggende egenskaper. Nå er tiden inne for å se på dem igjen mer i detalj og legge til de ekstra vi trenger for å gjøre nettverket mer robust. Hver verifiseringstransaksjon involverer flere roller — la oss se hvordan de oppfører seg.

> [!note] Roller i en verifiseringstransaksjon
> Hver verifisering involverer opptil seks distinkte roller, oppsummert i tabellen nedenfor. Alle sammen kan ha sin egen DID i det desentraliserte omdømmenettverket.

| Rolle | Beskrivelse |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Issuer** | Personen som publiserer informasjon til nettverket — påstår at noe har skjedd (en DID ble opprettet, redigert eller oppløst, en påstand, politikken til en gitt DID osv.) |
| **Subject** | Personen informasjonen handler om — påstandens adressat |
| **Authority** | En betrodd enhet som setter sitt navn på spill for påstandens kvalitet ved å etterforske den og enten gjennomgå de fremlagte bevisene eller aktivt samle dem inn |
| **Observer** | En uavhengig tredjepart som fører oppføring over hvordan verifikatoren håndterer påstanden — og passer på at verifikatoren verken forblir taus eller avviker fra politikken de erklærte |
| **Verifier** | En algoritmisk valgt deltaker som behandler transaksjonen |
| **Delegate** | En person som handler på vegne av en annen deltaker |
