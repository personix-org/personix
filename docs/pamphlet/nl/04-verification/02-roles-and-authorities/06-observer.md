---
title: "Observer"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Waarnemer

De waarnemersrol neemt de prikkel voor de verificateur weg om de regels te buigen. In situaties waarin een verificateur het verzoek van de uitgever of de autoriteit niet zint, zou hij eenvoudig kunnen zwijgen — niet antwoorden en de algoritmische reeks blokkeren. De waarnemer — of een verzameling waarnemers — zet zijn reputatie in op het documenteren van hoe de verificateur werd bevraagd. Als de verificateur zwijgt ondanks een verklaard beleid dat anders zegt, kan hij worden veroordeeld voor het schenden van het protocol.

![DE WAARNEMER — HOUDT EEN REGISTRATIE VAN DE VERIFICATEUR BIJ](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Het mechanisme: tijdstempel en uitdagingscode

Voordat je een claim naar de verificateur stuurt, route je die via waarnemers — mensen die je vertrouwt, of gespecialiseerde aanbieders van waarnemersdiensten die een kleine vergoeding rekenen. Elke waarnemer ontvangt je inzending, voorziet die van een tijdstempel, ondertekent dat hij haar zag uitgaan, en genereert een uitdagingscode — een cryptografische hash van zijn handtekening. De codes worden aan je verzoek toegevoegd. De verificateur ziet ze, maar heeft geen idee wie de waarnemers zijn, of de codes zelfs echt zijn. Waarnemers treden zo op als proxy's tussen de uitgever en de verificateur, en houden een onafhankelijke registratie dat de claim werd ingediend en wat die bevatte. Er kunnen er nul tot N zijn.

Wanneer de verificateur zich eerlijk gedraagt — aanvaardt of afwijst in lijn met zijn verklaarde beleid — blijven de codes ondoorzichtig. Niemand wordt blootgesteld.

Maar als de verificateur zwijgt ondanks een meegaand beleid, of antwoordt op een manier die in tegenspraak is met wat hij heeft gepubliceerd, dan houd je de oorspronkelijke waarnemershandtekeningen. Je kunt ze publiceren als proxy-getuigenis dat de claim werd ingediend en dat de verificateur het protocol niet volgde. Iedereen kan verifiëren dat de handtekeningen overeenkomen met de uitdagingscodes.

## De clou: je hebt geen echte waarnemers nodig

En hier komt het meest elegante deel: **je hebt helemaal geen echte waarnemers nodig.** Je kunt willekeurige getallen genereren die er precies uitzien als uitdagingscodes. De verificateur kan het verschil niet zien — hij moet gokken of hij zijn reputatie riskeert. Achter elk verzoek dat hij ontvangt zou een gerespecteerde waarnemer incognito kunnen meekijken — of het zou puur ruis kunnen zijn. De verificateur weet het niet. En die onzekerheid is het mechanisme.

De kosten om eerlijke druk te handhaven: bijna nul (willekeurige getallen zijn gratis). De potentiële kosten van oneerlijkheid voor de verificateur: catastrofaal. Eerlijk gedrag wordt geprikkeld, zelfs wanneer niemand daadwerkelijk kijkt.

Het systeem werkt omdat iedereen een beetje paranoïde is. Onzekerheid is goedkoper dan toezicht.

![DE BLUF DIE DE VERIFICATEUR EERLIJK HOUDT](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Meerdere verificateurs in één iteratie
> Een versterkende begeleidende regel voor de beschikbaarheid van verificateurs kan een algoritmische uitbreiding zijn die, in één iteratie, een verzameling kandidaat-verificateurs teruggeeft in plaats van slechts één.
