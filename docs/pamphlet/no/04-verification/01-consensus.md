---
title: "Consensus and the Verification Process"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# Konsensus og verifiseringsprosessen

For å bygge konsensus om hvilke regler et samfunn i gjennomsnitt bør opprettholde og håndheve, kan følgende mekanisme hjelpe. Som DID-deltaker erklærer jeg de reglene jeg slutter meg til og vil leve etter, og jeg publiserer dem. (Tenk på det som vedtektene og statuttene som, slik jeg ser det, utgjør min ideelle verden — en verden der jeg ikke føler meg begrenset, men trygg.)

Jeg kan på forhånd anslå hvordan DID-kontaktene mine ville reagere — og vurdere hvor sterkt, og av hvem, jeg ville bli sanksjonert i vanlige sosiale eller forretningsmessige interaksjoner, skulle de hypotetisk inntreffe.

Den endelige vurderingen skjer når du ber om informasjon fra en annen DID, eller ber dem verifisere en påstand (eller ber en autoritet om en tjeneste, og så videre) som du vil publisere til omdømmenettverket. Det bør vise seg å gå på samme måte som når du kjører vurderingen selv, i tørrkjøring, mot motpartens erklærte politikk — og gjør det ikke det, er noe galt på motpartens side: de prøver å spille et uærlig spill.

Utfallet er enten aksept, med en tilbudt pris for verifisering (i tilfelle verifikator- eller autoritetstjenester), eller avslag. Både sanksjoner og bonuser for avvik fra vurdererens politikk er innbakt i den tilbudte prisen. Forespørreren avgjør deretter om de skal godta vilkårene, eller gå videre til neste runde av verifisering i tildelingsalgoritmen — og gjenta prosessen til de er fornøyd, eller til økonomien gjør det poengløst å fortsette.

> [!note] Den sosiale grafen
> Omdømmenettverket er først og fremst et sosialt nettverk. Du legger til kontakter — folk som samtykker til forbindelsen. De har kontakter, og de kontaktene har kontakter. Algoritmen leter etter verifikatorer innenfor en konfigurerbar dybde (f.eks. tre nivåer: dine direkte kontakter, deres kontakter, og ett nivå til). Ingen global blokkjede trengs — nettverket danner naturlig fellesskap med overlapp inn i andre fellesskap.
>
> Algoritmen er ikke-deterministisk: den hasher påstandsdokumentet ditt, kobler hashen til en posisjon på en ring av kjente identiteter innenfor denne kretsen, og velger den nærmeste som kandidatverifikator. Du kan ikke forutsi eller påvirke hvem som vil verifisere påstanden din.

Hvert avslag fra en verifikator forstørrer dokumentet ditt og øker behandlingskostnaden — det er den første kostnadskanalen (dokumentvekst). Hver ny verifikator tar et gebyr basert på datamengde, omdømmet ditt og hvor langt innholdet i påstanden din avviker fra deres erklærte verifiseringspolitikk — det er den andre kostnadskanalen (risikopåslag). Og hver iterasjon koster tid og energi — den tredje kostnadskanalen.

> [!note] Hva verifikatoren sjekker, i rekkefølge
> Når den først er valgt, vurderer en verifikator en påstand i omtrent fire ordnede steg — de billigste filtrene først, de dyre innholdssjekkene sist:
>
> 1. **Politikk-portvakt.** Faller denne typen påstand i det hele tatt innenfor det verifikatoren offentlig verifiserer? Hvis ikke, avvises forespørselen umiddelbart.
> 2. **Autoritetstillit.** Er autoriteten som støttet påstanden, betrodd nok under verifikatorens egen erklærte politikk? En autoritet under verifikatorens tillitsterskel er grunn til avslag uansett påstandens innhold.
> 3. **Utstederens omdømme.** Oppfyller utstederen de omdømmeterskler verifikatoren har erklært for denne typen påstand? Lavt omdømme kan enten heve gebyret eller utløse avslag.
> 4. **Innholdssjekk.** Bare når de tre første portene passeres, vurderer verifikatoren selve påstanden — signaturer, intern konsistens, formell korrekthet, og hvor langt den avviker fra verifikatorens politikk. Gebyret som tas for dette siste steget, gjenspeiler den faktiske risikoen som tas.
>
> Verifikatoren publiserer politikken som styrer hver av disse portene, så stegene er ikke etter deres eget forgodtbefinnende — de er bundet av det de allerede har erklært. Avvik fra den publiserte politikken er i seg selv en publiserbar påstand mot dem, og de betaler for det med omdømmet sitt.

Resultatet: å publisere en troverdig og nyttig påstand koster nesten ingenting. Å publisere en radikal påstand koster mer. Å publisere en løgn blir uoverkommelig dyrt — du må iterere gjennom verifikator etter verifikator, og hver eneste som avviser deg, legger til kostnader. Markedet priser påstanden din, og prisen forteller deg hvor du står i forhold til fellesskapene du ferdes i.

Det holder ikke å erklære at du følger en regel når du i virkeligheten ikke gjør det. I så fall risikerer DID-en din publisering av en negativ oppføring som avslører hykleriet — noe som gjør deg til en risiko for alle andre. Utfallet bør bli færre, men mer konsekvent fulgte regler, og en oppklaring av den jungelen av lover og forskrifter som selv juridiske fagfolk knapt kan navigere i.

![HYPOCRISY IS THE MOST EXPENSIVE BEHAVIOR](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Konsensus vs. ansvarlighet
> For at nettverket skal tjene som en verdifull informasjonskilde, bør en DID ikke være for radikal — ellers vil de andre avvise den. Det sosiale presset vil søke likevekt, og forsøk på å destabilisere den vil trolig bli straffet.

![DECLARE YOUR RULES, PAY THE PRICE](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Antall stemmer er ikke det samme som en stemmes vekt
> Juraj Karpiš sier at «penger er minnet om gode gjerninger». Jeg vil legge til at omdømme er minnet om de dårlige.
>
> Det følger at, meritokratisk, den som bidrar mer og ikke har noe dårlig omdømme, fortjener større stemmevekt i fellesskapet. Sett gjennom linsen av bilaterale relasjoner: når jeg veier hvilke konsensuspress jeg skal imøtekomme, går den største vekten til de relasjonene jeg henter størst økonomisk utbytte fra. Ti personer jeg ikke har noen aktiv handel med, vil påvirke meg langt mindre enn én fast forretningspartner. Dette paradigmet er ikke begrenset til handel — det strekker seg til sosiale, politiske og andre relasjoner.
