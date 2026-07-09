---
title: "Reputation-Based Social Network"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Sociaal netwerk op basis van reputatie

Om verandering tot stand te brengen hebben we een zorgvuldig ontworpen instrument nodig. Eerst schetsen we het kort; in latere hoofdstukken bekijken we elk onderdeel in meer detail en voegen we er meer aan toe. Stel je een oncensureerbaar, globaal, gedecentraliseerd sociaal netwerk voor waarin je veilig je proxy-identiteit — een zogeheten Decentralized Identity (DID) — zou kunnen aanmaken en beheren. Een DID is een digitale identiteit die je zelf aanmaakt en beheert, zonder afhankelijkheid van enige centrale autoriteit. Niemand kan die afnemen of vervalsen, omdat ze cryptografisch is ondertekend met je privésleutel (of sleutels, via multisig).

> [!note] Opmerking
> Eén implicatie is dat zo'n identiteit geleidelijk de door de staat uitgegeven identiteitsdocumenten zou kunnen vervangen — maar daarover meer in het hoofdstuk over de overgang.

![JOUW IDENTITEIT, JOUW SLEUTELS, JOUW REGELS](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

In zo'n netwerk zou je via je identiteit kunnen melden dat iemand je schade heeft berokkend (en later mogelijk dat hij die heeft hersteld of daartoe is gedwongen). Opdat deze feedback — gericht aan de veroorzaker van de schade — waarde heeft als relevante bron, moet het invoeren van informatie in het netwerk tijd, energie en geld kosten — en bovenop dat moet er verifieerbaar bewijs voor anderen worden geproduceerd dat dit geen loze praat is.

Informatie lezen zou gemakkelijk en relatief goedkoop zijn, maar het aanmaken van een individuele registratie zou kostbaar en veeleisend zijn. Schrijven zou een duidelijk protocol volgen, waarin berekening volgens het gekozen algoritme strikt bepaalt welke DID om verificatie van de ingediende informatie moet worden gevraagd en hoe te werk te gaan zodat de geselecteerde deelnemer de informatie namens jou verwerkt, publiceert, en er de verificateur van wordt.

> [!note] Algoritme vs. radicalisme
> Algoritmische selectie van verificateurs zorgt ervoor dat niet-radicale informatie-uitgevers na verloop van tijd een bijna neutraal evenwicht behouden tussen de kosten van gepubliceerde informatie en de beloningen voor verificatie.

![PUBLICEREN KOST TIJD, ENERGIE EN GELD](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Laten we kijken hoe het algoritme een verificateur selecteert.

> [!note] Algoritme
> Algoritmische selectie kiest niet-deterministisch een andere verificateur (of een verzameling mogelijke verificateurs) voor verschillende stukjes informatie. Een hash (een eenrichtings-wiskundige functie die uit elke invoer een unieke “vingerafdruk” produceert — als een vingerafdruk van een document) van het volledige DID-document bepaalt de positie op een consistente hashring en selecteert kandidaat-verificateurs.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> In gewone taal: het algoritme neemt je hele DID-document, berekent er een vingerafdruk van, en die vingerafdruk bepaalt je verificateur.

![HOE HET ALGORITME JOUW VERIFICATEUR SELECTEERT](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Bij de eerste verificateur die het algoritme selecteert, slaag je als uitgever mogelijk niet — je reputatie of je verklaarde instellingen voldoen wellicht niet aan hun eisen. Je zou algoritmisch verder zoeken naar de volgende door nog een recursieve iteratie uit te voeren, die je een verdere verificateur toewijst. Bij elke stap groeit de “afstand” tot de doelverificateur, en daarmee ook de bijkomende metadata die moet worden gepubliceerd. Naarmate de gegevens groeien, stijgen de kosten vanzelf (niet alleen door de aanvankelijke omvang van de claim, maar ook door de metadata die zich bij elke afwijzing opstapelen). Geloofwaardige informatie gaat er veel makkelijker doorheen dan onzinnige grillen. Het is aan ieder hoe hoge prijs hij bereid is te dragen en hoeveel de registratie hem waard is — radicalisme wordt gegarandeerd duur.

![HOE DE VERIFICATEUR ANTWOORDT](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Wat de verificateur ook beslist in antwoord op je verificatieverzoek, de bal ligt weer bij de uitgever: hij kan het aanbod van de verificateur voor verificatiediensten aanvaarden, het antwoord in de chronologie opnemen en het (duurder) opnieuw proberen, of ermee stoppen en de verzonken kosten slikken.

![DE KEUZE VAN DE ISSUER](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Om je informatie meer gewicht te geven en een betere kans op aanvaarding bij verificateurs, zou je — als uitgever met een belang in het uit te geven bericht — de diensten van een **vertrouwde autoriteit** kunnen gebruiken. De autoriteit wijst de ingediende informatie ofwel af, ofwel aanvaardt ze die en zet er haar goede naam (reputatie) op in. De autoriteit vraagt doorgaans om bewijs uit de echte wereld, verifieert het en classificeert het. De output is een protocol van haar beoordeling van de gegeven zaak op het gegeven moment. Denk aan een autoriteit als een specialist in een bepaald type dienst in zowel de echte als de digitale wereld — bijvoorbeeld een onderzoeker, een auditor, een verzekeraar, een leverancier van een bepaalde klasse goederen (in wezen elke economische actor op de markt).

![HOE EEN REGISTRATIE IN HET NETWERK ONTSTAAT](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Tegen de tijd dat je informatie in het netwerk probeert te publiceren, bevat het waarschijnlijk al informatie over zijn actoren — dat zijn reputatiesignalen. Uitvogelen hoe je reputatiesignalen moet lezen — wat ze in verschillende situaties voor jou betekenen en welke risico's ze dragen — is misschien niet triviaal. Elke deelnemer kan reputatieregistraties anders bekijken via zijn DID, afhankelijk van de situatie waarmee hij ten aanzien van de tegenpartij te maken heeft. Is de tegenpartij een betrouwbare betaler, of moet ik geld vooraf eisen voor een zakelijke transactie? Draagt het aangeboden product beoordelingen over verborgen fraude of gebreken? Proberen ze zich onder contractuele verantwoordelijkheid uit te wurmen wanneer er iets misgaat? Soms komt een complexere blik op de algehele consistentie van de tegenpartij van pas — het hangt af van de voorkeuren van wie het overzicht opvraagt. De markt zou producten en diensten kunnen aanbieden die het lezen van reputatie vereenvoudigen, verwerken en verhelderen in de context van de situatie die voorligt. Diverse autoriteiten en hun aangeboden diensten kunnen daar eveneens toe dienen.

![HOE JE REPUTATIE LEEST](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Voorbeelden
> Typische informatie die van belang is voor uitgevers — en waardevol voor anderen — betreft gebeurtenissen voorbij de gewone tussenmenselijke communicatie in de echte of virtuele wereld.
>
> Negatieve voorbeelden:
> - bewijs van strafbare feiten (bijv. geaudit door een vertrouwd onderzoeksorgaan)
> - indirect bewijs (op zichzelf zwak, maar statistisch cumulatief) — bijv. herhaalde aanwezigheid nabij meerdere diefstallen in korte tijd → nog steeds toeval?
> - contractbreuk
>
> Positieve voorbeelden:
> - herstelde schade (vrijwillig of onder druk van de gemeenschap als straf)
> - aanvaarding en uitzitten van een door autoriteit X voorgestelde straf
> - autoriteit X heeft de erkenning van de eigendomsrechten van de dader in zekere mate ingetrokken
>
> Het is aan ieder om beschikbare informatie over de tegenpartij te verzamelen en de risico's naar eigen voorkeur in te schatten.

![WAT KUN JE IN HET NETWERK REGISTREREN?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Of er informatie over jou in het netwerk verschijnt, hangt uitsluitend af van je eigen gedrag.
> Je hoeft nooit lid te worden van zo'n netwerk, en toch kan er informatie over jou in verschijnen. Het hangt uitsluitend af van je handelen en de impact ervan op anderen.

![DE GEMEENSCHAP KAN ER EEN VOOR JE OPENEN](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Wat ik zojuist kort heb geschetst, is hoe een sociaal netwerk geïnspireerd op Decentralized Identity (DID) zou kunnen werken. Het primaire doel van DID-concepten is het versterken van privacy en vrijheid via het principe van intekenen op de regels die ik zal volgen en waarnaar ik zal leven — waarbij gebruikers de mogelijkheid krijgen te beslissen welke informatie ze delen en onder welke voorwaarden.

Ik stel voor DID's verder te verbinden tot een communicatienetwerk waarin de houders ervan feedback uitwisselen, ook voorbij situaties waarin iemand iets is overkomen en de gemeenschap of een individu moet reageren. Zulke preventieve vergelijking van de regels waarop we hebben ingetekend — met de mogelijkheid om de economische en andere gevolgen van wederzijdse afwijkingen in de verwachtingen over hoe de andere kant zou moeten opereren te berekenen — zou als een motivatie voor het vinden van consensus kunnen worden beschouwd. In plaats van vrijheid zou zo'n systeem de nadruk leggen op vrijwillige besluitvorming gecombineerd met verantwoordelijkheid voor gedrag in de echte wereld.

Een individu kan het systeem niet alleen breken — een groep mensen maakt meer kans, en een groep mensen met onderhandelde consensus en motivaties om aan veel kwesties samen te trekken, maakt nog meer kans om autoritaire tendensen te weerstaan. Aan de voorwaarde van organisatie uit het eerste hoofdstuk zal worden voldaan zodra aan twee voorwaarden is voldaan: het DID-reputatienetwerk dekt gemeenschappen representatief genoeg af zodat het gebruik ervan ophoudt exotisch te zijn. En tegelijk wordt dit gemeenschapssegment een economisch significante minderheid die assertief kan onderhandelen met de rest van de samenleving.

> [!note] Vrijwilligheid vs. vrijheid
> Vrijheid — in positieve zin — zou een secundair effect zijn van het balanceren van twee factoren: vrijwilligheid en de druk van de omgeving richting verantwoordelijkheid.

> [!note] Het AI-tijdperk en de waarde van reputatie
> In het tijdperk van kunstmatige intelligentie wordt alles wat met cognitief denken verbonden is geautomatiseerd — en het kan nog verder gaan. Wat blijft er dan in menselijke activiteit over als concurrentievoordeel? Het antwoord is moeilijk, en er zal ongetwijfeld iets worden gevonden, maar één ding kunnen we met zekerheid zeggen: reputatie zal beslissen. Een verifieerbare geschiedenis van je gedrag, je verbintenissen en de nakoming ervan — dat is iets wat AI niet voor je zal opbouwen.

![AI KAN JOUW REPUTATIE NIET OPBOUWEN — ALLEEN JIJ](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![DE ECONOMIE VAN DE WAARHEID](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
