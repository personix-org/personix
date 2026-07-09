---
title: "Verifier"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Verifier

Enhver DID kan opptre som verifikator, enten direkte eller gjennom verifiseringsrettigheter delegert til en tredje DID. For at jeg — eller min delegat — skal kunne verifisere, bør jeg være tilgjengelig på nettverket (på nett). Ikke alle vil binde seg til det, og derfor kan en DID-oppføring liste opp, i prioritert rekkefølge, de stedfortrederne som skal utføre funksjonen på dens vegne mens den er frakoblet.

Hver DID som er aktiv i nettverket, erklærer offentlig sin egen politikk. Gjennom reglene definert i den politikken vurderer den, under verifiseringsprosessen, omdømmet til motparten og innholdet i og formen på den påstanden utstederen har flagget for publisering til omdømmenettverket. En del av politikken er beregningsformelen som brukes til å beregne gebyrer for verifiseringstjenester. Når det er på plass, venter jeg — på tvers av et statistisk stort antall påstander som strømmer gjennom nettverket — på at nettverkets algoritme skal trekke meg inn på utstederens side og tildele meg, i en gitt iterasjon, å verifisere informasjonen som utstedes. Utstederen kan på forhånd beregne hvordan en korrekt oppførende verifikator ville reagere, men kan ikke unngå faktisk å kontakte dem (eller stedfortrederne deres); iterasjonen med den valgte verifikatoren må gjennomføres av utstederen selv når de på forhånd vet at den ikke vil passere.

Hvordan vet vi at utstederen kjører verifikator-valgalgoritmen over det korrekte settet av kandidat-verifikator-DID-er? Sammen med sin offentlig erklærte politikk publiserer hver DID også den gjeldende listen over identifikatorer for sitt sosiale nettverk innenfor omdømmenettverket. Definerer en utsteder sitt sosiale nettverk som en sosial boble som bare gjenlyder og forsterker sine egne synspunkter, vil informasjon publisert gjennom det knapt bli mottatt bredere av andre fellesskap. At jeg klarer, til høy kostnad, å presse en radikal påstand inn i nettverket, betyr ikke at jeg, når jeg bedømmer motpartens omdømme, vil gi den noen vekt. Enkelte påstander presses jeg av mitt fellesskap til å ta i betraktning (dommer og begrensninger pålagt overtredere); andre er helt opp til meg — jeg avgjør selv den økonomiske verdien av å inkludere eller ekskludere en gitt informasjonsbit.

![THE VERIFIER — CHOSEN BY THE ALGORITHM](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
