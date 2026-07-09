---
title: "Verifier"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Verificateur

Elke DID kan optreden als verificateur, hetzij rechtstreeks, hetzij via verificatierechten die aan een derde DID zijn gedelegeerd. Om mij — of mijn gemachtigde — in staat te stellen te verifiëren, zou ik bereikbaar moeten zijn op het netwerk (online). Niet iedereen zal zich daaraan willen binden, en daarom kan een DID-registratie, in volgorde van prioriteit, de vervangers opsommen die de functie namens haar zullen vervullen terwijl ze offline is.

Elke DID die actief is in het netwerk verklaart publiek zijn eigen beleid. Via de in dat beleid gedefinieerde regels beoordeelt hij tijdens het verificatieproces de reputatie van de tegenpartij en de inhoud en vorm van de claim die de uitgever voor publicatie in het reputatienetwerk heeft aangemerkt. Deel van het beleid is de rekenformule die wordt gebruikt om vergoedingen voor verificatiediensten te berekenen. Zodra dat op zijn plaats is, wacht ik over een statistisch groot aantal claims dat door het netwerk stroomt tot het algoritme van het netwerk mij aan de kant van de uitgever trekt en mij, in een gegeven iteratie, toewijst om de uit te geven informatie te verifiëren. De uitgever kan vooraf berekenen hoe een correct handelende verificateur zou reageren, maar kan niet vermijden hem (of zijn vervangers) daadwerkelijk te contacteren; de iteratie met de geselecteerde verificateur moet door de uitgever worden uitgevoerd, ook wanneer hij vooraf weet dat ze niet zal slagen.

Hoe weten we dat de uitgever het verificateurselectie-algoritme uitvoert over de juiste verzameling kandidaat-verificateur-DID's? Samen met zijn publiek verklaarde beleid publiceert elke DID ook de actuele lijst van identifiers van zijn sociale netwerk binnen het reputatienetwerk. Als een uitgever zijn sociale netwerk definieert als een sociale bubbel die louter zijn eigen opvattingen weerkaatst en versterkt, zal informatie die er doorheen wordt gepubliceerd nauwelijks breder worden ontvangen door andere gemeenschappen. Het feit dat het mij lukt, tegen hoge kosten, een radicale claim in het netwerk te duwen, impliceert niet dat ik er, bij het beoordelen van de reputatie van de tegenpartij, enig gewicht aan zal geven. Sommige claims word ik door mijn gemeenschap gedwongen in aanmerking te nemen (straffen en beperkingen opgelegd aan overtreders); andere zijn geheel aan mij — ik beslis zelf de economische waarde van het opnemen of uitsluiten van een gegeven stuk informatie.

![DE VERIFICATEUR — GEKOZEN DOOR HET ALGORITME](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
