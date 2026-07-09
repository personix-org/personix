---
title: "Observer"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Observer

Observatørrollen fjerner verifikatorens insentiv til å bøye reglene. I situasjoner der en verifikator ikke liker utstederens eller autoritetens forespørsel, kunne de rett og slett tie stille — ikke svare, og blokkere den algoritmiske sekvensen. Observatøren — eller et sett av observatører — setter sitt omdømme på spill for å dokumentere hvordan verifikatoren ble forespurt. Tier verifikatoren stille til tross for en erklært politikk som sier noe annet, kan de bli felt for brudd på protokollen.

![THE OBSERVER — KEEPS A RECORD OF THE VERIFIER](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Mekanismen: tidsstempel og utfordringskode

Før du sender en påstand til verifikatoren, ruter du den gjennom observatører — folk du stoler på, eller spesialiserte observatørtjenesteleverandører som tar et lite gebyr. Hver observatør mottar innsendingen din, tidsstempler den, signerer på at de så den gå ut, og genererer en utfordringskode — en kryptografisk hash av signaturen deres. Kodene legges til forespørselen din. Verifikatoren ser dem, men aner ikke hvem observatørene er, eller om kodene i det hele tatt er ekte. Observatører opptrer dermed som stedfortredere mellom utstederen og verifikatoren, og holder en uavhengig oppføring om at påstanden ble innsendt og hva den inneholdt. Det kan være fra null til N av dem.

Når verifikatoren opptrer ærlig — godtar eller avviser i tråd med sin erklærte politikk — forblir kodene ugjennomsiktige. Ingen blir eksponert.

Men tier verifikatoren stille til tross for en imøtekommende politikk, eller svarer på en måte som motsier det de publiserte, holder du de opprinnelige observatørsignaturene. Du kan publisere dem som stedfortredervitnesbyrd om at påstanden ble innsendt, og at verifikatoren ikke fulgte protokollen. Hvem som helst kan verifisere at signaturene stemmer med utfordringskodene.

## Poenget: du trenger ikke ekte observatører

Og her er det mest elegante: **du trenger ikke ekte observatører i det hele tatt.** Du kan generere tilfeldige tall som ser nøyaktig ut som utfordringskoder. Verifikatoren kan ikke se forskjell — de må terne om de skal risikere omdømmet sitt. Bak hver forespørsel de mottar, kunne det stå en aktet observatør og se på inkognito — eller det kunne være ren støy. Verifikatoren vet ikke. Og den usikkerheten er mekanismen.

Kostnaden ved å opprettholde ærlig press: nesten null (tilfeldige tall er gratis). Den potensielle kostnaden ved uærlighet for verifikatoren: katastrofal. Ærlig atferd blir incentivert selv når ingen faktisk ser på.

Systemet fungerer fordi alle er en smule paranoide. Usikkerhet er billigere enn overvåkning.

![THE BLUFF THAT KEEPS THE VERIFIER HONEST](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Flere verifikatorer i én iterasjon
> En forsterkende følgeregel for verifikatortilgjengelighet kan være en algoritmisk utvidelse som returnerer, i én iterasjon, et sett av kandidatverifikatorer i stedet for bare én.
