---
title: "Reputation-Based Social Network"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Omdømmebaseret socialt netværk

For at skabe forandring har vi brug for et omhyggeligt designet værktøj. Først vil vi skitsere det kort. I senere kapitler vil vi undersøge hver enkelt del mere detaljeret og tilføje mere. Forestil dig et ucensurerbart, globalt, decentraliseret socialt netværk, hvor du sikkert kunne oprette og administrere din stedfortræder-identitet — en såkaldt decentraliseret identitet (DID). En DID er en digital identitet, som du selv skaber og kontrollerer, uden afhængighed af nogen central autoritet. Ingen kan tage den fra dig eller forfalske den, fordi den er kryptografisk signeret med din private nøgle (eller nøgler, via multisig).

> [!note] Bemærkning
> En implikation er, at en sådan identitet gradvist kunne erstatte statsudstedte identifikationsdokumenter — men mere om det i kapitlet om overgang.

![DIN IDENTITET, DINE NØGLER, DINE REGLER](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

I et sådant netværk kunne du gennem din identitet rapportere, at nogen har forvoldt dig skade (og senere, potentielt, at de har rettet op på det eller er blevet tvunget til det). For at denne feedback — rettet mod ophavsmanden til skaden — skal have værdi som en relevant kilde, må det koste tid, energi og penge at indføre information i netværket — og oven i det skal der frembringes verificerbart bevis over for andre om, at dette ikke er tomt snak.

At læse information ville være let og relativt billigt, men at skabe en enkelt registrering ville være kostbart og krævende. Skrivning ville følge en klar protokol, hvor beregning efter den valgte algoritme strengt afgør, hvilken DID der skal bedes om verifikation af den indsendte information, og hvordan man går frem, så den udvalgte deltager behandler informationen på dine vegne, offentliggør den og bliver dens verifikator.

> [!note] Algoritme vs. radikalisme
> Algoritmisk udvælgelse af verifikatorer sikrer, at ikke-radikale informationsudgivere over tid vil opretholde en næsten neutral balance mellem omkostningerne ved offentliggjort information og belønninger for verifikation.

![OFFENTLIGGØRELSE KOSTER TID, ENERGI OG PENGE](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Lad os se på, hvordan algoritmen udvælger en verifikator.

> [!note] Algoritme
> Algoritmisk udvælgelse vælger ikke-deterministisk en anden verifikator (eller et sæt mulige verifikatorer) for forskellige informationsstykker. En hash (en envejs matematisk funktion, der frembringer et unikt “fingeraftryk” fra ethvert input — som et fingeraftryk af et dokument) af det komplette DID-dokument bestemmer positionen på en konsistent hash-ring og udvælger verifikatorkandidater.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> På almindeligt sprog: algoritmen tager hele dit DID-dokument, beregner et fingeraftryk fra det, og det fingeraftryk bestemmer din verifikator.

![HVORDAN ALGORITMEN UDVÆLGER DIN VERIFIKATOR](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Med den første verifikator, algoritmen udvælger, lykkes det måske ikke for dig som udgiver — dit omdømme eller dine erklærede indstillinger opfylder måske ikke deres krav. Du ville algoritmisk fortsætte søgningen efter den næste ved at udføre endnu en rekursiv iteration, som tildeler dig en yderligere verifikator. Med hvert skridt vokser “afstanden” til målverifikatoren, og det samme gør de ledsagende metadata, der skal offentliggøres. Efterhånden som dataene vokser, stiger omkostningerne naturligt (ikke kun på grund af påstandens oprindelige størrelse, men også på grund af de metadata, der ophobes ved hver afvisning). Troværdig information passerer langt lettere end meningsløse luner. Det er op til den enkelte, hvor høj en pris de er villige til at bære, og hvor meget registreringen betyder for dem — radikalisme bliver garanteret dyr.

![HVORDAN VERIFIKATOREN SVARER](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Uanset hvad verifikatoren beslutter som svar på din verifikationsanmodning, er bolden tilbage på udgiverens banehalvdel: de kan acceptere verifikatorens tilbud om verifikationstjenester, folde svaret ind i kronologien og prøve igen (dyrere) eller gå væk og sluge den tabte omkostning.

![UDSTEDERENS VALG](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

For at give din information større vægt og en bedre chance for accept hos verifikatorer kunne du — som en udgiver med en interesse i, at informationen udstedes — bruge en **betroet autoritets** tjenester. Autoriteten afviser enten den indsendte information eller accepterer den og sætter sit gode navn (omdømme) på spil for den. Autoriteten anmoder typisk om beviser fra den virkelige verden, verificerer dem og klassificerer dem. Resultatet er en protokol over dens vurdering af den givne sag på det givne tidspunkt. Tænk på en autoritet som en specialist i en bestemt type tjeneste i både den virkelige og den digitale verden — for eksempel en efterforsker, en revisor, et forsikringsselskab, en leverandør af en bestemt klasse varer (i bund og grund enhver økonomisk aktør på markedet).

![HVORDAN EN REGISTRERING OPSTÅR I NETVÆRKET](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

På det tidspunkt, hvor du forsøger at offentliggøre information i netværket, vil det sandsynligvis allerede indeholde information om dets aktører — disse er omdømmesignaler. At navigere i, hvordan man læser omdømmesignaler — hvad de betyder for dig i forskellige situationer, og hvilke risici de bærer — er måske ikke trivielt. Hver deltager kan se på omdømmeregistreringer forskelligt gennem sin DID, afhængigt af den situation, de har med modparten. Er modparten en pålidelig betaler, eller er jeg nødt til at kræve penge på forhånd for en handelstransaktion? Bærer det tilbudte produkt anmeldelser om skjult svindel eller defekter? Forsøger de at vride sig ud af kontraktligt ansvar, når noget går galt? Nogle gange kommer et mere komplekst blik på modpartens overordnede konsistens til nytte — det afhænger af præferencerne hos den, der anmoder om oversigten. Markedet kunne tilbyde produkter og tjenester, der forenkler, behandler og tydeliggør læsningen af omdømme i konteksten af den aktuelle situation. Forskellige autoriteter og deres tilbudte tjenester kan også tjene dette formål.

![HVORDAN MAN LÆSER OMDØMME](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Eksempler
> Typisk information af interesse for udgivere — og værdifuld for andre — vedrører hændelser ud over almindelig mellemmenneskelig kommunikation i den virkelige eller virtuelle verden.
>
> Negative eksempler:
> - bevis for kriminelle handlinger (f.eks. revideret af et betroet efterforskningsorgan)
> - indirekte bevis (svagt i sig selv, men statistisk kumulativt) — f.eks. gentagen tilstedeværelse nær flere tyverier på kort tid → stadig et tilfælde?
> - kontraktbrud
>
> Positive eksempler:
> - udbedret skade (frivilligt eller under pres fra fællesskabet som straf)
> - accept og afsoning af en straf foreslået af autoritet X
> - autoritet X tilbagekaldte anerkendelsen af gerningsmandens ejendomsret i et vist omfang
>
> Det er op til den enkelte at indsamle tilgængelig information om modparten og vurdere risiciene efter sine præferencer.

![HVAD KAN DU REGISTRERE I NETVÆRKET?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Hvorvidt information om dig optræder i netværket, afhænger udelukkende af din egen adfærd.
> Du behøver aldrig at tilslutte dig et sådant netværk, men information om dig kan alligevel optræde i det. Det afhænger udelukkende af dine handlinger og den virkning, de har på andre.

![FÆLLESSKABET KAN ÅBNE EN FOR DIG](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Det, jeg netop kort har skitseret, er, hvordan et socialt netværk inspireret af decentraliseret identitet (DID) kunne fungere. Det primære formål med DID-koncepter er at styrke privatliv og frihed gennem princippet om at tilslutte sig de regler, jeg vil følge og leve efter — og give brugerne mulighed for at beslutte, hvilken information de vil dele, og under hvilke betingelser.

Jeg foreslår yderligere at forbinde DID'er i et kommunikationsnetværk, hvor deres indehavere udveksler feedback selv ud over situationer, hvor der er sket noget for nogen, og fællesskabet eller en enkeltperson må reagere. En sådan forebyggende sammenligning af de regler, vi har tilsluttet os — med mulighed for at beregne de økonomiske og andre konsekvenser af gensidige afvigelser i forventninger om, hvordan den anden side bør operere — kunne betragtes som en motivation for at finde konsensus. I stedet for frihed ville et sådant system fremhæve frivillig beslutningstagen kombineret med ansvar for adfærd i den virkelige verden.

Et individ kan ikke bryde systemet alene — en gruppe mennesker har en større chance, og en gruppe mennesker med forhandlet konsensus og motivationer til at trække sammen på mange spørgsmål har en endnu større chance for at modstå autoritære tendenser. Forudsætningen om organisering fra det første kapitel vil være opfyldt, når to betingelser er mødt: DID-omdømmenetværket dækker fællesskaber repræsentativt nok til, at brugen af det ophører med at være eksotisk. Og samtidig bliver dette fællesskabssegment et økonomisk betydeligt mindretal, der assertivt kan forhandle med resten af samfundet.

> [!note] Frivillighed vs. frihed
> Frihed — i den positive betydning — ville være en sekundær virkning af at afbalancere to faktorer: frivillighed og presset fra ens omgivelser mod ansvar.

> [!note] AI-æraen og omdømmets værdi
> I den kunstige intelligens' æra bliver alt forbundet med kognitiv tænkning automatiseret — og det kan gå endnu videre. Hvad bliver der så tilbage i menneskelig aktivitet som en konkurrencemæssig fordel? Svaret er svært, og noget vil sikkert blive fundet, men én ting kan vi sige med sikkerhed: omdømme vil afgøre det. En verificerbar historik over din adfærd, dine forpligtelser og deres opfyldelse — det er noget, AI ikke vil bygge for dig.

![AI KAN IKKE BYGGE DIT OMDØMME — DET KAN KUN DU](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![SANDHEDENS ØKONOMI](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
