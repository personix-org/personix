---
title: "Roles Overview"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Lomu pārskats

Dažas no šīm lomām mēs jau īsi skārām nodaļā par tīklu un tā pamatīpašībām. Tagad ir īstais laiks tās aplūkot vēlreiz sīkāk un pievienot papildu lomas, kas mums vajadzīgas, lai padarītu tīklu robustāku. Katrs verifikācijas darījums iesaista vairākas lomas — paskatīsimies, kā tās uzvedas.

> [!note] Lomas verifikācijas darījumā
> Katra verifikācija iesaista līdz sešām atšķirīgām lomām, kas apkopotas zemāk esošajā tabulā. Visām no tām var būt savs DID decentralizētajā reputācijas tīklā.

| Loma | Apraksts |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Izdevējs** | Cilvēks, kurš publicē informāciju tīklā — apgalvo, ka kaut kas noticis (izveidots, rediģēts vai izbeigts DID, apgalvojums, attiecīgā DID politika utt.) |
| **Subjekts** | Cilvēks, par kuru ir informācija — apgalvojuma adresāts |
| **Autoritāte** | Uzticams subjekts, kas liek uz spēles savu vārdu par apgalvojuma kvalitāti, to izmeklējot un vai nu izskatot iesniegtos pierādījumus, vai aktīvi tos vācot |
| **Novērotājs** | Neatkarīga trešā puse, kas uztur ierakstu par to, kā verificētājs apstrādā apgalvojumu — pārliecinoties, ka verificētājs ne klusē, ne novirzās no deklarētās politikas |
| **Verificētājs** | Algoritmiski izvēlēts dalībnieks, kas apstrādā darījumu |
| **Deleģāts** | Cilvēks, kas rīkojas cita dalībnieka vārdā |
