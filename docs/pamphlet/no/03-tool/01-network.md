---
title: "Reputation-Based Social Network"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Omdømmebasert sosialt nettverk

For å få til endring trenger vi et omhyggelig utformet verktøy. Først skisserer vi det kort; i senere kapitler går vi grundigere inn på hver enkelt del og legger til mer. Se for deg et sensurfritt, globalt, desentralisert sosialt nettverk der du trygt kunne skape og forvalte din stedfortredende identitet — en såkalt desentralisert identitet (DID). En DID er en digital identitet som du selv skaper og kontrollerer, uten avhengighet av noen sentral autoritet. Ingen kan ta den fra deg eller forfalske den, fordi den er kryptografisk signert med din private nøkkel (eller nøkler, via multisig).

> [!note] Merknad
> En følge av dette er at en slik identitet gradvis kunne erstatte statlig utstedte identitetsdokumenter — men mer om det i kapittelet om overgangen.

![YOUR IDENTITY, YOUR KEYS, YOUR RULES](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

I et slikt nettverk kunne du gjennom identiteten din melde fra om at noen har påført deg skade (og senere eventuelt at de har rettet den opp eller blitt tvunget til det). For at denne tilbakemeldingen — rettet mot den som forårsaket skaden — skal ha verdi som en relevant kilde, må det å legge informasjon inn i nettverket koste tid, energi og penger — og i tillegg må det produseres etterprøvbart bevis for andre om at dette ikke er tomprat.

Å lese informasjon ville være lett og relativt billig, men å opprette en enkeltoppføring ville være kostbart og krevende. Skriving følger en klar protokoll, der beregning etter den valgte algoritmen strengt bestemmer hvilken DID som skal spørres om å verifisere den innsendte informasjonen, og hvordan man går frem slik at den valgte deltakeren behandler informasjonen på dine vegne, publiserer den og blir dens verifikator.

> [!note] Algoritme vs. radikalisme
> Algoritmisk valg av verifikatorer sikrer at ikke-radikale informasjonsutgivere over tid vil opprettholde en nesten nøytral balanse mellom kostnadene ved publisert informasjon og belønningene for verifisering.

![PUBLISHING COSTS TIME, ENERGY, AND MONEY](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

La oss se på hvordan algoritmen velger en verifikator.

> [!note] Algoritme
> Algoritmisk valg plukker ikke-deterministisk ut en annen verifikator (eller et sett av mulige verifikatorer) for ulike informasjonsbiter. En hash (en enveis matematisk funksjon som lager et unikt «avtrykk» av en hvilken som helst inndata — som et fingeravtrykk av et dokument) av det komplette DID-dokumentet bestemmer posisjonen på en konsistent hash-ring og velger ut verifikatorkandidater.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> På enkelt språk: algoritmen tar hele DID-dokumentet ditt, beregner et avtrykk av det, og det avtrykket bestemmer verifikatoren din.

![HOW THE ALGORITHM SELECTS YOUR VERIFIER](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Hos den første verifikatoren algoritmen velger, lykkes du kanskje ikke som utgiver — omdømmet ditt eller de erklærte innstillingene dine oppfyller kanskje ikke kravene deres. Du ville algoritmisk fortsette letingen etter den neste ved å utføre nok en rekursiv iterasjon, som tildeler deg enda en verifikator. For hvert steg vokser «avstanden» til målverifikatoren, og det gjør også de tilhørende metadataene som må publiseres. Etter hvert som dataene vokser, stiger kostnadene naturlig (ikke bare på grunn av påstandens opprinnelige størrelse, men også på grunn av metadataene som hoper seg opp for hvert avslag). Troverdig informasjon passerer langt lettere enn tåpelige innfall. Det er opp til hver enkelt hvor høy pris de er villige til å bære, og hvor mye oppføringen betyr for dem — radikalisme blir garantert dyrt.

![HOW THE VERIFIER ANSWERS](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Uansett hva verifikatoren bestemmer som svar på din verifiseringsforespørsel, ligger ballen igjen hos utgiveren: de kan godta verifikatorens tilbud om verifiseringstjenester, føre svaret inn i kronologien og prøve igjen (dyrere), eller trekke seg og svelge den tapte kostnaden.

![THE ISSUER'S CHOICE](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

For å gi informasjonen din større vekt og en bedre sjanse til å bli godtatt hos verifikatorene, kunne du — som utgiver med interesse i at informasjonen blir utstedt — bruke tjenestene til en **betrodd autoritet**. Autoriteten enten avviser den innsendte informasjonen eller godtar den og setter sitt gode navn (omdømme) på spill for den. Autoriteten ber typisk om bevis fra den virkelige verden, verifiserer det og klassifiserer det. Resultatet er en protokoll over dens vurdering av den gitte saken på det gitte tidspunktet. Tenk på en autoritet som en spesialist i en bestemt type tjeneste i både den virkelige og den digitale verden — for eksempel en etterforsker, en revisor, et forsikringsselskap, en leverandør av en bestemt vareklasse (i bunn og grunn en hvilken som helst økonomisk aktør i markedet).

![HOW A RECORD IS CREATED IN THE NETWORK](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Innen du forsøker å publisere informasjon i nettverket, vil det trolig allerede inneholde informasjon om aktørene sine — dette er omdømmesignaler. Å navigere i hvordan man leser omdømmesignaler — hva de betyr for deg i ulike situasjoner og hvilke risikoer de bærer med seg — er kanskje ikke trivielt. Hver deltaker kan se på omdømmeoppføringer på ulikt vis gjennom sin DID, avhengig av situasjonen de står i overfor motparten. Er motparten en pålitelig betaler, eller må jeg kreve penger på forskudd for en handel? Bærer det tilbudte produktet omtaler om skjult svindel eller mangler? Prøver de å vri seg unna kontraktsmessig ansvar når noe går galt? Iblant kommer et mer sammensatt bilde av motpartens samlede konsistens godt med — det avhenger av preferansene til den som ber om oversikten. Markedet kunne tilby produkter og tjenester som forenkler, bearbeider og klargjør lesingen av omdømme i lys av den aktuelle situasjonen. Ulike autoriteter og tjenestene de tilbyr, kan også tjene dette formålet.

![HOW TO READ REPUTATION](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Eksempler
> Typisk informasjon som er av interesse for utgivere — og verdifull for andre — gjelder hendelser utover vanlig mellommenneskelig kommunikasjon i den virkelige eller virtuelle verden.
>
> Negative eksempler:
> - bevis på kriminelle handlinger (f.eks. revidert av et betrodd etterforskningsorgan)
> - indirekte bevis (svakt alene, men statistisk kumulativt) — f.eks. gjentatt tilstedeværelse i nærheten av flere tyverier på kort tid → fortsatt tilfeldig?
> - kontraktsbrudd
>
> Positive eksempler:
> - utbedret skade (frivillig eller under press fra fellesskapet som straff)
> - aksept og soning av en straff foreslått av autoritet X
> - autoritet X tilbakekalte anerkjennelsen av overtrederens eiendomsrett i et visst omfang
>
> Det er opp til hver enkelt å samle tilgjengelig informasjon om motparten og vurdere risikoene etter egne preferanser.

![WHAT CAN YOU RECORD IN THE NETWORK?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Hvorvidt informasjon om deg dukker opp i nettverket, avhenger utelukkende av din egen atferd.
> Du behøver aldri å melde deg inn i et slikt nettverk, og likevel kan informasjon om deg dukke opp i det. Det avhenger utelukkende av dine handlinger og den virkningen de har på andre.

![THE COMMUNITY CAN OPEN ONE FOR YOU](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Det jeg nettopp har skissert kort, er hvordan et sosialt nettverk inspirert av desentralisert identitet (DID) kunne fungere. Hovedformålet med DID-konsepter er å styrke personvern og frihet gjennom prinsippet om å slutte seg til de reglene jeg vil følge og leve etter — ved å gi brukerne muligheten til å bestemme hvilken informasjon de deler og på hvilke vilkår.

Jeg foreslår å knytte DID-er videre sammen til et kommunikasjonsnettverk der innehaverne deres utveksler tilbakemeldinger også utover situasjoner der noe har hendt noen og fellesskapet eller et enkeltindivid må reagere. En slik forebyggende sammenligning av reglene vi har sluttet oss til — med muligheten til å beregne de økonomiske og andre følgene av gjensidige avvik i forventningene om hvordan den andre siden bør operere — kunne betraktes som en motivasjon for å finne konsensus. I stedet for frihet ville et slikt system legge vekt på frivillig beslutningstaking kombinert med ansvar for atferd i den virkelige verden.

Et individ kan ikke bryte systemet alene — en gruppe mennesker står bedre til, og en gruppe mennesker med fremforhandlet konsensus og motivasjoner til å dra i lag i mange saker står enda bedre til for å stå imot autoritære tendenser. Forutsetningen om organisering fra det første kapittelet vil være oppfylt når to betingelser er innfridd: DID-omdømmenettverket dekker fellesskapene representativt nok til at bruken av det slutter å være eksotisk. Og samtidig blir dette fellesskapssegmentet et økonomisk betydelig mindretall som selvsikkert kan forhandle med resten av samfunnet.

> [!note] Frivillighet vs. frihet
> Frihet — i positiv forstand — ville være en sekundær virkning av å balansere to faktorer: frivillighet og presset fra ens omgivelser mot ansvar.

> [!note] KI-æraen og omdømmets verdi
> I den kunstige intelligensens tidsalder blir alt knyttet til kognitiv tenkning automatisert — og det kan gå enda lenger. Hva står da igjen i menneskelig virksomhet som et konkurransefortrinn? Svaret er vanskelig, og noe vil sikkert bli funnet, men én ting kan vi si med sikkerhet: omdømmet vil avgjøre. En etterprøvbar historikk over din atferd, dine forpliktelser og innfrielsen av dem — det er noe KI ikke vil bygge for deg.

![AI CANNOT BUILD YOUR REPUTATION — ONLY YOU CAN](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![THE ECONOMICS OF TRUTH](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
