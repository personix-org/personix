---
title: "Rejstřík pojmů"
part: "Příloha"
lang: cs
version: v6
---

# Rejstřík pojmů

| Pojem | Anglicky | Význam |
|-------|----------|--------|
| **Alokace daní** | Tax Allocation | Mechanismus, kterým daňový poplatník rozhoduje, kam putuje část jeho daní. Alokovatelné procento rok od roku roste. |
| **Autorita** | Authority | Důvěryhodná entita (osoba, organizace), která ověřuje informace a vsází na ně svou reputaci. Může být specializovaná (investigativní, právní, technická). |
| **Compartmentalizace** | Compartmentalization | Obecně: oddělení informací do izolovaných celků tak, aby prozrazení jednoho celku neohrozilo ostatní. Princip známý ze zpravodajských služeb. Zde: paralelní DID identity v diktaturách — kompromitace jedné z nich ostatní neodhalí. |
| **DID** | Decentralized Identity | Digitální identita, kterou si vytváříte a kontrolujete sami, bez centrální autority. Kryptograficky podepsaná vaším soukromým klíčem — nikdo vám ji nemůže odebrat ani zfalšovat. |
| **DID dokument** | DID Document | Veřejně dostupný datový soubor popisující vaši DID identitu — obsahuje veřejné klíče, síťové adresy a metadata. Slouží k ověření vaší totožnosti v síti. |
| **Due diligence** | Due Diligence | Obecně: hloubková prověrka protistrany před vstupem do obchodního nebo právního vztahu — ověření její historie, financí, reputace a rizik. Zde: v reputační síti probíhá rychleji a automatičtěji díky dostupnosti ověřených záznamů. |
| **Emergentní** | Emergent | Samovolně vznikající z interakcí jednodušších částí, aniž by to někdo navrhl nebo řídil. Hejno ptáků létá v útvaru bez plánu — útvar emerguje z jednoduchých pravidel, kterými se řídí každý jedinec. |
| **Emergentní společenská smlouva** | Emergent Social Contract | Pravidla chování, která nevznikají shora (zákon), ale zdola — z opakovaných interakcí a konsenzu v komunitě. |
| **ESR** | Electronic Spending Register | Navrhovaný systém transparentního sledování veřejných výdajů — každý realizovaný výdaj státu se páruje s plánovanou platbou. Inspirováno českou EET, ale obrácenou proti státu. |
| **Fenomenologický** | Phenomenological | Obecně: přístup zkoumající jevy tak, jak se ukazují v přímé zkušenosti, pozorováním toho, co z nich vyplývá, bez předem daných teorií. Zde: svoboda, společenská smlouva a normy chování jsou pozorované jevy — důsledky tisíců mikrointerakcí mezi lidmi, ne principy definované shora. |
| **Hash** | Hash (otisk) | Obecně: jednosměrná matematická funkce, která z libovolného vstupu vytvoří unikátní „otisk" pevné délky — jako otisk prstu dokumentu. Ze stejného vstupu vždy vznikne stejný výstup, ale z výstupu nelze zpětně odvodit vstup. Zde: slouží k určení pozice na hash ringu a k ověřování integrity dokumentů. |
| **Hash ring** | Consistent Hash Ring | Algoritmický mechanismus výběru ověřovatelů — pozici na kruhu určuje hash DID dokumentu v sociálním grafu. Zajišťuje nedeterministický, ale ověřitelný výběr. |
| **Just-in-time financování** | Just-in-Time Funding | Financování státu podmíněné transparentností — peníze tečou, až když stát přijme ESR a spáruje výdaje. Páka k vynucení spolupráce. |
| **Meritokracie** | Meritocracy | Obecně: systém, kde o postavení rozhodují skutečné zásluhy a prokázané schopnosti, ne formální tituly, konexe nebo zděděná privilegia. Zde: reputační síť přirozeně upřednostňuje ty, kdo prokazatelně přispívají komunitě — jejich hlas má větší váhu díky track recordu, ne díky funkci. |
| **Onion gateway** | Onion Gateway | Síťová adresa DID identity v onion síti. Oddělená od DID dokumentu — lze ji změnit bez ztráty identity (podobně jako změna IP adresy u domény). |
| **Onion routing** | Onion Routing (Tor) | Komunikační protokol zajišťující necenzurovatelnost sítě. Zprávy se šifrují ve vrstvách — každý uzel odstraní jednu vrstvu, ale nezná celou cestu. |
| **Oracle problém** | Oracle Problem | Obecně: jak zajistit, aby data vstupující do digitálního systému věrně odpovídala tomu, co se skutečně stalo ve fyzickém světě. Pojem pochází z oblasti blockchainů. Zde: řeší se přes autority, které do ověření vkládají svou reputaci jako záruku, že digitální záznam odpovídá fyzické skutečnosti. |
| **Ověřovatel** | Verifier | Účastník algoritmicky vybraný k ověření a zveřejnění záznamu. Sází své dobré jméno na pravdivost informace. |
| **Policy (politika)** | Policy | Obecně: soubor pravidel nebo zásad určujících chování v určitém kontextu. Zde: každý účastník DID sítě deklaruje svou politiku — jak reaguje na konkrétní chování ostatních, jaká pravidla dodržuje a jaké tresty považuje za přiměřené. Souhrn politik tvoří emergentní společenskou smlouvu. |
| **Princip ekonomické neutrality** | Economic Neutrality Principle | Poctivé chování v síti se ekonomicky blíží nule — náklady na publikaci se vracejí jako odměny za ověřování. Nepoctivé chování je čistá ztráta. |
| **Proxy** | Proxy | Obecně: zástupce nebo zprostředkovatel — systém nebo subjekt jednající jménem jiného. Zde se používá ve dvou kontextech: (1) ESR jako proxy párující veřejné výdaje s plánovanými platbami; (2) pozorovatelé jako proxy mezi vydavatelem a ověřovatelem v triku s pozorovateli. |
| **Reputační signál** | Reputation Signal | Jednotlivý záznam v síti — pozitivní (náprava škody, splnění závazku) nebo negativní (křivda, porušení smlouvy). Kumulativně tvoří reputační profil. |
| **Reputační síť** | Reputation-Based Social Network (RSN) | Decentralizovaná sociální síť, kde si účastníci vyměňují zpětnou vazbu o chování v reálném světě. Záznamy jsou nákladné na vytvoření, levné na čtení. |
| **Sociální graf** | Social Graph | Síť vašich kontaktů a kontaktů vašich kontaktů. Algoritmus hledá ověřovatele v konfigurovatelné hloubce (například 3 úrovně). Žádný globální blockchain — síť přirozeně vytváří komunity s přesahy. |
| **Track record** | Track Record | Obecně: historie dosavadních výsledků, úspěchů i neúspěchů osoby nebo organizace. Zde: souhrn všech dosavadních interakcí dané DID identity v síti — ověřených tvrzení, přijatých i odmítnutých záznamů — z něhož se její reputace odvozuje. |
| **Tvrzení** | Claim | Obecně: jakýkoli ověřitelný výrok. Zde: záznam publikovaný do reputační sítě — tvrzení o události, vlastnosti nebo vztahu, kryptograficky podepsané a ověřené. Např. „jsem rezident obce X" nebo „tato osoba porušila smlouvu". |
| **Vydavatel** | Publisher | Účastník sítě, který vytváří a publikuje záznam (tvrzení o křivdě, nápravě a podobně). Nese náklady na publikaci. |
