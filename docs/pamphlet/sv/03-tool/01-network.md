---
title: "Reputation-Based Social Network"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Anseendebaserat socialt nätverk

För att åstadkomma förändring behöver vi ett noggrant utformat verktyg. Först ska vi skissa det kortfattat; i senare kapitel ska vi undersöka varje del mer i detalj och lägga till mer. Föreställ dig ett ocensurerbart, globalt, decentraliserat socialt nätverk där du tryggt kan skapa och hantera din ombudsidentitet — en så kallad decentraliserad identitet (DID). En DID är en digital identitet som du själv skapar och kontrollerar, utan beroende av någon central auktoritet. Ingen kan ta den ifrån dig eller förfalska den, eftersom den är kryptografiskt signerad med din privata nyckel (eller nycklar, via multisig).

> [!note] Anmärkning
> En följd är att en sådan identitet gradvis skulle kunna ersätta statligt utfärdade identitetshandlingar — men mer om det i kapitlet om övergången.

![YOUR IDENTITY, YOUR KEYS, YOUR RULES](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

I ett sådant nätverk skulle du genom din identitet kunna rapportera att någon har orsakat dig skada (och senare, potentiellt, att de har avhjälpt den eller tvingats göra det). För att denna återkoppling — riktad mot upphovet till skadan — ska ha värde som en relevant källa måste det kosta tid, energi och pengar att föra in information i nätverket — och därutöver måste verifierbara bevis produceras för andra att detta inte är tomt prat.

Att läsa information skulle vara lätt och relativt billigt, men att skapa en enskild post skulle vara kostsamt och krävande. Att skriva skulle följa ett tydligt protokoll, där beräkning enligt den valda algoritmen strikt avgör vilken DID som ska ombes verifiera den inlämnade informationen och hur man går vidare så att den utvalda deltagaren bearbetar informationen å dina vägnar, publicerar den och blir dess verifierare.

> [!note] Algoritm kontra radikalism
> Algoritmiskt val av verifierare säkerställer att icke-radikala informationsutgivare med tiden håller en nästan neutral balans mellan kostnaderna för publicerad information och belöningar för verifiering.

![PUBLISHING COSTS TIME, ENERGY, AND MONEY](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Låt oss se på hur algoritmen väljer en verifierare.

> [!note] Algoritm
> Algoritmiskt val väljer icke-deterministiskt en annan verifierare (eller en uppsättning möjliga verifierare) för olika informationsdelar. En hash (en enkelriktad matematisk funktion som producerar ett unikt ”fingeravtryck” från vilken indata som helst — som ett fingeravtryck av ett dokument) av det fullständiga DID-dokumentet bestämmer positionen på en konsistent hash-ring och väljer ut verifierarkandidater.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> På ren svenska: algoritmen tar hela ditt DID-dokument, beräknar ett fingeravtryck utifrån det, och det fingeravtrycket bestämmer din verifierare.

![HOW THE ALGORITHM SELECTS YOUR VERIFIER](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Med den första verifierare som algoritmen väljer kanske du som utgivare inte lyckas — ditt anseende eller dina deklarerade inställningar kanske inte uppfyller deras krav. Du skulle algoritmiskt fortsätta sökandet efter nästa genom att utföra ännu en rekursiv iteration, som tilldelar dig ytterligare en verifierare. För varje steg växer ”avståndet” till målverifieraren, och därmed också de åtföljande metadata som måste publiceras. När data växer stiger kostnaderna naturligt (inte bara på grund av påståendets ursprungliga storlek, utan också på grund av de metadata som ackumuleras vid varje avslag). Trovärdig information passerar mycket lättare än nonsensartade infall. Det är upp till var och en hur högt pris de är villiga att bära och hur mycket posten betyder för dem — radikalism blir garanterat dyrt.

![HOW THE VERIFIER ANSWERS](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Vad verifieraren än beslutar som svar på din verifieringsbegäran är bollen tillbaka hos utgivaren: de kan acceptera verifierarens erbjudande om verifieringstjänster, foga in svaret i kronologin och försöka igen (dyrare), eller gå därifrån och svälja den redan nedlagda kostnaden.

![THE ISSUER'S CHOICE](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

För att ge din information större tyngd och en bättre chans att accepteras hos verifierare skulle du — som utgivare med en insats i att informationen utfärdas — kunna använda tjänsterna hos en **betrodd auktoritet**. Auktoriteten antingen avvisar den inlämnade informationen eller accepterar den och sätter sitt goda namn (anseende) på spel för den. Auktoriteten begär vanligtvis bevis från den verkliga världen, verifierar dem och klassificerar dem. Utfallet är ett protokoll över dess bedömning av det aktuella fallet vid den aktuella tidpunkten. Tänk på en auktoritet som en specialist på en viss typ av tjänst i både den verkliga och digitala världen — till exempel en utredare, en revisor, en försäkringsgivare, en leverantör av en viss klass av varor (i grunden vilken ekonomisk aktör som helst på marknaden).

![HOW A RECORD IS CREATED IN THE NETWORK](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

När du försöker publicera information i nätverket innehåller det sannolikt redan information om sina aktörer — dessa är anseendesignaler. Att navigera hur man läser anseendesignaler — vad de betyder för dig i olika situationer och vilka risker de bär — är kanske inte trivialt. Varje deltagare kan se på anseendeposter olika genom sin DID, beroende på den situation de hanterar gällande motparten. Är motparten en pålitlig betalare, eller behöver jag kräva pengar i förskott för en affärstransaktion? Bär den erbjudna produkten omdömen om dolt bedrägeri eller defekter? Försöker de slingra sig ur avtalsansvaret när något går fel? Ibland kommer en mer komplex bild av motpartens övergripande konsekvens väl till pass — det beror på preferenserna hos den som begär översikten. Marknaden skulle kunna erbjuda produkter och tjänster som förenklar, bearbetar och förtydligar läsningen av anseende i kontexten av den aktuella situationen. Olika auktoriteter och deras erbjudna tjänster kan tjäna detta syfte också.

![HOW TO READ REPUTATION](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Exempel
> Typisk information av intresse för utgivare — och värdefull för andra — rör händelser bortom vanlig mellanmänsklig kommunikation i den verkliga eller virtuella världen.
>
> Negativa exempel:
> - bevis på brottsliga handlingar (t.ex. reviderade av ett betrott utredande organ)
> - indirekta bevis (svaga var för sig, men statistiskt kumulativa) — t.ex. upprepad närvaro nära flera stölder under kort tid → fortfarande en tillfällighet?
> - avtalsbrott
>
> Positiva exempel:
> - avhjälpt skada (frivilligt eller under tryck från gemenskapen som straff)
> - accepterande och avtjänande av ett straff föreslaget av auktoritet X
> - auktoritet X återkallade erkännandet av gärningsmannens äganderätt i viss utsträckning
>
> Det är upp till var och en att samla tillgänglig information om motparten och bedöma riskerna efter sina preferenser.

![WHAT CAN YOU RECORD IN THE NETWORK?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Huruvida information om dig dyker upp i nätverket beror uteslutande på ditt eget beteende.
> Du behöver aldrig gå med i ett sådant nätverk, och ändå kan information om dig dyka upp i det. Det beror uteslutande på dina handlingar och den inverkan de har på andra.

![THE COMMUNITY CAN OPEN ONE FOR YOU](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Det jag just kort har skissat är hur ett socialt nätverk inspirerat av decentraliserad identitet (DID) skulle kunna fungera. Det primära syftet med DID-koncept är att stärka integritet och frihet genom principen att skriva under på de regler jag ska följa och leva efter — vilket ger användarna förmågan att avgöra vilken information de ska dela och under vilka villkor.

Jag föreslår att man vidare kopplar samman DID:er till ett kommunikationsnätverk där deras innehavare utbyter återkoppling även bortom situationer där något har hänt någon och gemenskapen eller en individ behöver reagera. En sådan förebyggande jämförelse av de regler vi har skrivit under på — med möjligheten att beräkna de ekonomiska och andra konsekvenserna av ömsesidiga avvikelser i förväntningar om hur den andra sidan borde agera — skulle kunna betraktas som en motivation för att finna konsensus. Istället för frihet skulle ett sådant system betona frivilligt beslutsfattande i förening med ansvar för beteende i den verkliga världen.

En individ kan inte bryta systemet ensam — en grupp människor har en större chans, och en grupp människor med förhandlad konsensus och drivkrafter att dra åt samma håll i många frågor har en ännu större chans att motstå auktoritära tendenser. Förutsättningen organisering från det första kapitlet uppfylls när två villkor är uppfyllda: DID-anseendenätverket täcker gemenskaper tillräckligt representativt för att dess användning upphör att vara exotisk. Och samtidigt blir detta gemenskapssegment en ekonomiskt betydande minoritet som kan förhandla självsäkert med resten av samhället.

> [!note] Frivillighet kontra frihet
> Frihet — i positiv mening — skulle vara en sekundär effekt av att balansera två faktorer: frivillighet och omgivningens tryck mot ansvar.

> [!note] AI-eran och anseendets värde
> I den artificiella intelligensens era automatiseras allt som är kopplat till kognitivt tänkande — och det kan gå ännu längre. Vad återstår då i mänsklig verksamhet som en konkurrensfördel? Svaret är svårt, och något kommer säkert att hittas, men en sak kan vi säga med säkerhet: anseendet kommer att avgöra. En verifierbar historik av ditt beteende, dina åtaganden och deras uppfyllande — det är något som AI inte kommer att bygga åt dig.

![AI CANNOT BUILD YOUR REPUTATION — ONLY YOU CAN](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![THE ECONOMICS OF TRUTH](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
