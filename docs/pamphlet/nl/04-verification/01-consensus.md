---
title: "Consensus and the Verification Process"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# Consensus en het verificatieproces

Om consensus op te bouwen over welke regels een samenleving gemiddeld zou moeten handhaven en afdwingen, kan het volgende mechanisme helpen. Als DID-deelnemer verklaar ik de regels waarop ik inteken en waarnaar ik zal leven, en ik publiceer ze. (Zie het als de statuten en reglementen die naar mijn mening mijn ideale wereld uitmaken — een wereld waarin ik me niet beperkt voel, maar veilig.)

Ik kan vooraf inschatten hoe mijn DID-contacten zouden reageren — en beoordelen hoe sterk, en door wie, ik zou worden gesanctioneerd in gewone sociale of zakelijke interacties, mochten die hypothetisch plaatsvinden.

De definitieve beoordeling gebeurt wanneer je informatie opvraagt bij een andere DID, of hem vraagt een claim te verifiëren (of een autoriteit om een dienst vraagt, enzovoort) die je in het reputatienetwerk wilt publiceren. Het zou hetzelfde moeten uitpakken als wanneer je de beoordeling zelf uitvoert, in een dry run, tegen het verklaarde beleid van de tegenpartij — en als dat niet zo is, is er iets mis aan de kant van de tegenpartij: die probeert een oneerlijk spel te spelen.

De uitkomst is ofwel aanvaarding, met een geciteerde prijs voor verificatie (in het geval van diensten van een verificateur of autoriteit), ofwel afwijzing. Zowel sancties als bonussen voor afwijking van het beleid van de beoordelaar zijn in de geciteerde prijs verwerkt. De aanvrager beslist vervolgens of hij de voorwaarden aanvaardt, of doorgaat naar de volgende ronde van verificatie in het toewijzingsalgoritme — waarbij hij het proces herhaalt tot hij tevreden is, of tot de economie het zinloos maakt om door te gaan.

> [!note] De sociale graaf
> Het reputatienetwerk is bovenal een sociaal netwerk. Je voegt contacten toe — mensen die instemmen met de verbinding. Zij hebben contacten, en die contacten hebben contacten. Het algoritme zoekt verificateurs binnen een instelbare diepte (bijv. drie niveaus: je directe contacten, hun contacten, en één niveau daarbuiten). Er is geen globale blockchain nodig — het netwerk vormt vanzelf gemeenschappen met overlappingen naar andere gemeenschappen.
>
> Het algoritme is niet-deterministisch: het hasht je claimdocument, mapt de hash op een positie op een ring van bekende identiteiten binnen deze kring, en selecteert de dichtstbijzijnde als kandidaat-verificateur. Je kunt niet voorspellen of beïnvloeden wie je claim zal verifiëren.

Elke afwijzing door een verificateur vergroot je document en verhoogt de verwerkingskosten ervan — dat is het eerste kostenkanaal (documentgroei). Elke nieuwe verificateur rekent een vergoeding op basis van gegevensvolume, je reputatie, en hoever de inhoud van je claim afwijkt van zijn verklaarde verificatiebeleid — dat is het tweede kostenkanaal (risicopremie). En elke iteratie kost tijd en energie — het derde kostenkanaal.

> [!note] Wat de verificateur controleert, in volgorde
> Eenmaal geselecteerd, beoordeelt een verificateur een claim in grofweg vier geordende stappen — goedkoopste filters eerst, dure inhoudscontroles laatst:
>
> 1. **Beleidsafscherming.** Valt dit soort claim überhaupt binnen wat de verificateur publiek verifieert? Zo niet, dan wordt het verzoek regelrecht afgewezen.
> 2. **Vertrouwen in de autoriteit.** Is de autoriteit die de claim heeft geruggensteund voldoende vertrouwd onder het eigen verklaarde beleid van de verificateur? Een autoriteit onder de vertrouwensdrempel van de verificateur is grond voor afwijzing, ongeacht de inhoud van de claim.
> 3. **Reputatie van de uitgever.** Voldoet de uitgever aan de reputatiedrempels die de verificateur voor dit type claim heeft verklaard? Een lage reputatie kan ofwel de vergoeding verhogen ofwel afwijzing uitlokken.
> 4. **Inhoudscontrole.** Pas wanneer de eerste drie poorten worden gepasseerd, beoordeelt de verificateur de claim zelf — handtekeningen, interne consistentie, formele correctheid, en hoever ze afwijkt van het beleid van de verificateur. De vergoeding voor deze laatste stap weerspiegelt het werkelijk genomen risico.
>
> De verificateur publiceert het beleid dat elk van deze poorten regeert, zodat de stappen niet aan zijn goeddunken zijn — hij is gebonden aan wat hij reeds heeft verklaard. Afwijking van het gepubliceerde beleid is zelf een publiceerbare claim tegen hem, en hij betaalt ervoor met zijn reputatie.

Het resultaat: een geloofwaardige en nuttige claim publiceren kost bijna niets. Een radicale claim publiceren kost meer. Een leugen publiceren wordt prohibitief duur — je moet verificateur na verificateur doorlopen, en iedereen die je afwijst voegt kosten toe. De markt beprijst je claim, en de prijs vertelt je waar je staat ten opzichte van de gemeenschappen waarin je je beweegt.

Het volstaat niet te verklaren dat je een regel naleeft terwijl je dat in werkelijkheid niet doet. In dat geval riskeert je DID de publicatie van een negatieve registratie die de hypocrisie blootlegt — wat je verandert in een risico voor iedereen. De uitkomst zou minder maar consistenter nageleefde regels moeten zijn, en een opschoning van die jungle van wetten en voorschriften waarin zelfs juridische professionals zich amper kunnen oriënteren.

![HYPOCRISIE IS HET DUURSTE GEDRAG](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Consensus vs. verantwoording
> Opdat het netwerk als waardevolle informatiebron dient, zou een DID niet te radicaal moeten zijn — anders wijzen de anderen hem af. Maatschappelijke druk zal evenwicht zoeken, en pogingen om het te destabiliseren zullen waarschijnlijk worden bestraft.

![VERKLAAR JE REGELS, BETAAL DE PRIJS](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Het aantal stemmen is niet hetzelfde als het gewicht van een stem
> Juraj Karpiš zegt dat "geld het geheugen van goede daden is." Ik zou daaraan toevoegen dat reputatie het geheugen van de slechte is.
>
> Daaruit volgt dat, meritocratisch, wie meer bijdraagt en geen slechte reputatie heeft een groter gewicht van stem in de gemeenschap verdient. Bekeken door de lens van bilaterale relaties: wanneer ik afweeg aan welke consensusdruk ik tegemoetkom, gaat het grootste gewicht naar de relaties waaruit ik het grootste economische voordeel haal. Tien mensen met wie ik geen actieve handel drijf, zullen mij veel minder beïnvloeden dan één vaste zakenpartner. Dit paradigma is niet beperkt tot handel — het strekt zich uit tot sociale, politieke en andere relaties.
