---
title: "Observer"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Observatør

Observatørrollen fjerner verifikatorens incitament til at bøje reglerne. I situationer, hvor en verifikator ikke bryder sig om udstederens eller autoritetens anmodning, kunne de simpelthen forblive tavse — undlade at svare og blokere den algoritmiske sekvens. Observatøren — eller et sæt observatører — sætter sit omdømme på spil for at dokumentere, hvordan verifikatoren blev forespurgt. Hvis verifikatoren forbliver tavs på trods af en erklæret politik, der siger det modsatte, kan de dømmes for at overtræde protokollen.

![OBSERVATØREN — FØRER OPTEGNELSE OVER VERIFIKATOREN](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Mekanismen: tidsstempel og challenge-kode

Før du sender en påstand til verifikatoren, dirigerer du den gennem observatører — folk, du stoler på, eller specialiserede observatør-tjenesteudbydere, der opkræver et lille gebyr. Hver observatør modtager din indsendelse, tidsstempler den, signerer, at de så den gå ud, og genererer en challenge-kode — en kryptografisk hash af deres signatur. Koderne føjes til din anmodning. Verifikatoren ser dem, men aner ikke, hvem observatørerne er, eller om koderne overhovedet er ægte. Observatører fungerer således som mellemled mellem udstederen og verifikatoren og holder en uafhængig optegnelse over, at påstanden blev indsendt, og hvad den indeholdt. Der kan være nul til N af dem.

Når verifikatoren opfører sig ærligt — accepterer eller afviser i overensstemmelse med sin erklærede politik — forbliver koderne uigennemsigtige. Ingen bliver eksponeret.

Men hvis verifikatoren forbliver tavs på trods af en imødekommende politik, eller svarer på en måde, der modsiger det, de offentliggjorde, holder du de oprindelige observatør-signaturer. Du kan offentliggøre dem som stedfortrædende vidnesbyrd om, at påstanden blev indsendt, og at verifikatoren ikke fulgte protokollen. Enhver kan verificere, at signaturerne matcher challenge-koderne.

## Pointen: du behøver ikke rigtige observatører

Og her er den mest elegante del: **du behøver slet ikke rigtige observatører.** Du kan generere tilfældige tal, der ligner challenge-koder til forveksling. Verifikatoren kan ikke se forskel — de er nødt til at kaste terningerne om, hvorvidt de vil risikere deres omdømme. Bag hver anmodning, de modtager, kunne der være en respekteret observatør, der ser med inkognito — eller det kunne være ren støj. Verifikatoren ved det ikke. Og den usikkerhed er mekanismen.

Omkostningen ved at opretholde ærligt pres: næsten nul (tilfældige tal er gratis). Den potentielle omkostning ved uærlighed for verifikatoren: katastrofal. Ærlig adfærd tilskyndes, selv når ingen faktisk holder øje.

Systemet fungerer, fordi alle er en smule paranoide. Usikkerhed er billigere end overvågning.

![BLUFFET, DER HOLDER VERIFIKATOREN ÆRLIG](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Flere verifikatorer i en enkelt iteration
> En forstærkende ledsageregel for verifikator-tilgængelighed kan være en algoritmisk udvidelse, der i en enkelt iteration returnerer et sæt kandidat-verifikatorer i stedet for blot én.
