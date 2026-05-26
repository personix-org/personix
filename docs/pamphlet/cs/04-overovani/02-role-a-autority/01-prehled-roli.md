---
title: "Přehled rolí"
chapter: 3
part: "Jak funguje ověřování"
lang: cs
version: v6
---

# Přehled rolí

Některé role jsme krátce naťukli už v kapitole o síti a jejích základních vlastnostech. Nyní nastal čas podívat se podrobněji znova na tyto role a přidat další nezbytné, abychom zajistili větší robustnost sítě. V každé ověřovací transakci vystupuje několik rolí, pojďme se podívat, jak se chovají.

> [!note] Role v ověřovací transakci
> Každá ověřovací transakce má až šest různých rolí, shrnutých v tabulce níže. Všechny mohou mít v decentralizované reputační síti svůj DID.

| Role | Popis |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Vydavatel (Issuer)** | Osoba, která zveřejňuje informaci do sítě — tvrdí, že se něco stalo (DID vznikla, byla editována nebo zanikla, publikované tvrzení, policy dané DID atd.) |
| **Subjekt/Nositel (Subject)** | Osoba, o které informace hovoří — adresát tvrzení |
| **Autorita (Authority)** | Důvěryhodný subjekt, který svým jménem ručí za kvalitu tvrzení jeho prošetřením a necháním si předložení důkazů nebo jejich aktivním dohledáním |
| **Pozorovatel (Observer)** | Nezávislá třetí strana, která vede záznam o tom, jak ověřovatel zpracovává tvrzení — dohlíží, aby ověřovatel výsledek nevymlčel ani se neodchýlil od deklarované politiky |
| **Ověřovatel (Verifier)** | Algoritmicky vybraný účastník, který transakci zpracuje |
| **Delegát (Delegate)** | Osoba jednající jménem jiného účastníka |
