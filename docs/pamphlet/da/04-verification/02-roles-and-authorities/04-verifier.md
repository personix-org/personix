---
title: "Verifier"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Verifikator

Enhver DID kan fungere som verifikator, enten direkte eller gennem verifikationsrettigheder delegeret til en tredje DID. For at jeg — eller min delegat — skal kunne verificere, bør jeg være tilgængelig på netværket (online). Ikke alle vil forpligte sig til det, og derfor kan en DID-registrering opliste, i prioriteret rækkefølge, de stedfortrædere, der vil udføre funktionen på dens vegne, mens den er offline.

Hver DID, der er aktiv i netværket, erklærer offentligt sin egen politik. Gennem de regler, der er defineret i den politik, bedømmer den under verifikationsprocessen modpartens omdømme samt indholdet og formen af den påstand, som udstederen har markeret til offentliggørelse i omdømmenetværket. En del af politikken er den beregningsformel, der bruges til at udregne gebyrer for verifikationstjenester. Når det er på plads, venter jeg — på tværs af et statistisk stort antal påstande, der strømmer gennem netværket — på, at netværkets algoritme trækker mig på udstederens side og tildeler mig, i en given iteration, at verificere den information, der udstedes. Udstederen kan på forhånd beregne, hvordan en korrekt opførende verifikator ville reagere, men kan ikke undgå faktisk at kontakte dem (eller deres stedfortrædere); iterationen med den udvalgte verifikator skal gennemføres af udstederen, selv når de på forhånd ved, at den ikke vil passere.

Hvordan ved vi, at udstederen kører verifikatorudvælgelses-algoritmen over det korrekte sæt af kandidat-verifikator-DID'er? Sammen med sin offentligt erklærede politik offentliggør hver DID også den aktuelle liste over identifikatorer for sit sociale netværk inden for omdømmenetværket. Hvis en udsteder definerer sit sociale netværk som en social boble, der blot genlyder og forstærker dens egne synspunkter, vil information offentliggjort gennem den næppe blive modtaget bredere af andre fællesskaber. Det faktum, at det lykkes mig, til høj pris, at skubbe en radikal påstand ind i netværket, indebærer ikke, at jeg, når jeg bedømmer modpartens omdømme, vil tillægge den nogen vægt. Nogle påstande bliver jeg af mit fællesskab skubbet til at tage i betragtning (domme og restriktioner pålagt lovovertrædere); andre er helt op til mig — jeg beslutter selv den økonomiske værdi af at inkludere eller ekskludere et givet informationsstykke.

![VERIFIKATOREN — UDVALGT AF ALGORITMEN](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
