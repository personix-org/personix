---
title: "Roles Overview"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Overzicht van de rollen

We hebben sommige van deze rollen al kort aangeraakt in het hoofdstuk over het netwerk en zijn basiseigenschappen. Nu is het tijd ze opnieuw en gedetailleerder te bekijken en de bijkomende toe te voegen die we nodig hebben om het netwerk robuuster te maken. Bij elke verificatietransactie zijn verscheidene rollen betrokken — laten we zien hoe ze zich gedragen.

> [!note] Rollen in een verificatietransactie
> Bij elke verificatie zijn tot zes verschillende rollen betrokken, samengevat in de tabel hieronder. Ze kunnen allemaal hun eigen DID in het gedecentraliseerde reputatienetwerk hebben.

| Rol | Beschrijving |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Uitgever** | De persoon die informatie in het netwerk publiceert — beweert dat er iets is gebeurd (een DID is aangemaakt, bewerkt of ontbonden, een claim, het beleid van een gegeven DID enz.) |
| **Subject** | De persoon over wie de informatie gaat — de geadresseerde van de claim |
| **Autoriteit** | Een vertrouwde entiteit die haar naam inzet op de kwaliteit van de claim door die te onderzoeken en ofwel het overgelegde bewijs te toetsen ofwel het actief te verzamelen |
| **Waarnemer** | Een onafhankelijke derde die bijhoudt hoe de verificateur met de claim omgaat — die ervoor zorgt dat de verificateur niet zwijgt en niet afwijkt van het beleid dat hij heeft verklaard |
| **Verificateur** | Een algoritmisch geselecteerde deelnemer die de transactie verwerkt |
| **Gemachtigde** | Een persoon die handelt namens een andere deelnemer |
