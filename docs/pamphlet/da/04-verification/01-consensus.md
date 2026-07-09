---
title: "Consensus and the Verification Process"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# Konsensus og verifikationsprocessen

For at opbygge konsensus om, hvilke regler et samfund i gennemsnit bør opretholde og håndhæve, kan følgende mekanisme hjælpe. Som DID-deltager erklærer jeg de regler, jeg tilslutter mig og vil leve efter, og jeg offentliggør dem. (Tænk på det som de vedtægter og statutter, der efter min mening udgør min ideelle verden — en verden, hvor jeg ikke føler mig begrænset, men tryg.)

Jeg kan på forhånd anslå, hvordan mine DID-kontakter ville reagere — og vurdere, hvor stærkt og af hvem jeg ville blive sanktioneret i almindelige sociale eller forretningsmæssige interaktioner, hvis de hypotetisk skulle finde sted.

Den endelige evaluering sker, når du anmoder om information fra en anden DID, eller beder dem verificere en påstand (eller beder en autoritet om en tjeneste osv.), som du vil offentliggøre til omdømmenetværket. Det bør falde ud på samme måde, som det gør, når du selv kører evalueringen i tør-kørsel mod modpartens erklærede politik — og hvis det ikke gør, er der noget galt på modpartens side: de forsøger at spille et uærligt spil.

Udfaldet er enten accept, med en oplyst pris for verifikation (i tilfælde af verifikator- eller autoritetstjenester), eller afvisning. Både sanktioner og bonusser for afvigelse fra evaluatorens politik foldes ind i den oplyste pris. Anmoderen beslutter derefter, om de vil acceptere vilkårene eller gå videre til næste runde af verifikation i tildelingsalgoritmen — idet processen gentages, indtil de er tilfredse, eller indtil økonomien gør det meningsløst at fortsætte.

> [!note] Den sociale graf
> Omdømmenetværket er først og fremmest et socialt netværk. Du tilføjer kontakter — folk, der samtykker til forbindelsen. De har kontakter, og de kontakter har kontakter. Algoritmen søger efter verifikatorer inden for en konfigurerbar dybde (f.eks. tre niveauer: dine direkte kontakter, deres kontakter og ét niveau derudover). Ingen global blockchain er nødvendig — netværket danner naturligt fællesskaber med overlap ind i andre fællesskaber.
>
> Algoritmen er ikke-deterministisk: den hasher dit påstandsdokument, mapper hashen til en position på en ring af kendte identiteter inden for denne kreds og udvælger den nærmeste som kandidatverifikator. Du kan ikke forudsige eller påvirke, hvem der vil verificere din påstand.

Hver verifikators afvisning forstørrer dit dokument og øger dets behandlingsomkostning — det er den første omkostningskanal (dokumentvækst). Hver ny verifikator opkræver et gebyr baseret på datamængde, dit omdømme, og hvor langt indholdet af din påstand afviger fra deres erklærede verifikationspolitik — det er den anden omkostningskanal (risikopræmie). Og hver iteration koster tid og energi — den tredje omkostningskanal.

> [!note] Hvad verifikatoren tjekker, i rækkefølge
> Når først en verifikator er udvalgt, evaluerer den en påstand i groft sagt fire ordnede trin — de billigste filtre først, de dyre indholdstjek sidst:
>
> 1. **Politik-gating.** Falder denne slags påstand overhovedet inden for det, verifikatoren offentligt verificerer? Hvis ikke, afvises anmodningen direkte.
> 2. **Autoritetstillid.** Er den autoritet, der har godkendt påstanden, tilstrækkeligt betroet under verifikatorens egen erklærede politik? En autoritet under verifikatorens tillidstærskel er grund til afvisning uanset påstandens indhold.
> 3. **Udstederens omdømme.** Opfylder udstederen de omdømmetærskler, verifikatoren har erklæret for denne type påstand? Lavt omdømme kan enten hæve gebyret eller udløse afvisning.
> 4. **Indholdstjek.** Kun når de tre første porte passeres, evaluerer verifikatoren selve påstanden — signaturer, intern konsistens, formel korrekthed, og hvor langt den afviger fra verifikatorens politik. Gebyret, der opkræves for dette sidste trin, afspejler den faktiske risiko, der tages.
>
> Verifikatoren offentliggør den politik, der styrer hver af disse porte, så trinnene ligger ikke op til deres skøn — de er bundet af det, de allerede har erklæret. Afvigelse fra den offentliggjorte politik er i sig selv en påstand, der kan offentliggøres imod dem, og de betaler for den med deres omdømme.

Resultatet: at offentliggøre en troværdig og nyttig påstand koster næsten intet. At offentliggøre en radikal påstand koster mere. At offentliggøre en løgn bliver uoverkommeligt dyrt — du må iterere gennem verifikator efter verifikator, og hver eneste, der afviser dig, lægger omkostninger til. Markedet prissætter din påstand, og prisen fortæller dig, hvor du står i forhold til de fællesskaber, du færdes i.

Det er ikke nok at erklære, at du overholder en regel, når du i virkeligheden ikke gør. I det tilfælde risikerer din DID offentliggørelsen af en negativ registrering, der afslører hykleriet — hvilket gør dig til en risiko for alle andre. Udfaldet bør være færre, men mere konsekvent fulgte regler, og en udrensning af den jungle af love og forordninger, som selv juridiske fagfolk knap kan navigere i.

![HYKLERI ER DEN DYRESTE ADFÆRD](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Konsensus vs. ansvarlighed
> For at netværket kan tjene som en værdifuld informationskilde, bør en DID ikke være for radikal — ellers vil de andre afvise den. Socialt pres vil søge ligevægt, og forsøg på at destabilisere den vil sandsynligvis blive straffet.

![ERKLÆR DINE REGLER, BETAL PRISEN](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Antallet af stemmer er ikke det samme som en stemmes vægt
> Juraj Karpiš siger, at "penge er erindringen om gode gerninger." Jeg vil tilføje, at omdømme er erindringen om de dårlige.
>
> Deraf følger, at meritokratisk fortjener den, der bidrager mere og ikke har noget dårligt omdømme, en større vægt af stemme i fællesskabet. Set gennem de bilaterale relationers linse: når jeg vejer, hvilke konsensuspres jeg skal imødekomme, går den største vægt til de relationer, hvorfra jeg henter den største økonomiske fordel. Ti mennesker, som jeg ikke har nogen aktiv handel med, vil påvirke mig langt mindre end én permanent forretningspartner. Dette paradigme er ikke begrænset til handel — det strækker sig til sociale, politiske og andre relationer.
