---
title: "Roles Overview"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Panoramica dei ruoli

Abbiamo già toccato brevemente alcuni di questi ruoli nel capitolo sulla rete e sulle sue proprietà di base. Ora è il momento di riguardarli in maggior dettaglio e di aggiungere quelli ulteriori che ci servono per rendere la rete più robusta. Ogni transazione di verifica coinvolge diversi ruoli — vediamo come si comportano.

> [!note] I ruoli in una transazione di verifica
> Ogni verifica coinvolge fino a sei ruoli distinti, riassunti nella tabella qui sotto. Tutti possono avere una propria DID nella rete di reputazione decentralizzata.

| Ruolo | Descrizione |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Emittente** | La persona che pubblica informazioni nella rete — afferma che qualcosa è accaduto (una DID è stata creata, modificata o dissolta, un reclamo, la policy di una data DID, ecc.) |
| **Soggetto** | La persona a cui l'informazione si riferisce — il destinatario del reclamo |
| **Autorità** | Un'entità di fiducia che mette in gioco il proprio nome sulla qualità del reclamo indagandolo e o esaminando le prove presentate o raccogliendole attivamente |
| **Osservatore** | Un terzo indipendente che tiene traccia di come il verificatore gestisce il reclamo — assicurandosi che il verificatore né taccia né si scosti dalla policy che ha dichiarato |
| **Verificatore** | Un partecipante selezionato algoritmicamente che elabora la transazione |
| **Delegato** | Una persona che agisce per conto di un altro partecipante |
