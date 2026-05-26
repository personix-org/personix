---
title: "Reputační sociální síť"
chapter: 2
part: "Nástroj"
lang: cs
version: v6
source: v1
---

# Reputační sociální síť (Reputation-Based Social Network)

Ke změně potřebujeme pečlivě připravený nástroj. Nejdříve ho stručně prolétneme a v pozdějších kapitolách probereme každou jednotlivost detailněji a doplníme další. Představte si necenzurovatelnou globální decentralizovanou sociální síť, kde byste mohli bezpečně vytvořit a spravovat svou zástupnou identitu — takzvanou decentralizovanou identitu (Decentralized Identity, DID). DID je digitální identita, kterou si vytváříte a kontrolujete sami, bez závislosti na jakékoliv centrální autoritě. Nikdo vám ji nemůže odebrat ani zfalšovat, protože je kryptograficky podepsaná vaším soukromým klíčem/klíči (multisig).

> [!note] Poznámka
> Jednou z implikací je, že taková identita může postupně nahradit státem vydávané průkazy totožnosti — ale o tom až v kapitole o přechodu.

![VAŠE IDENTITA, VAŠE KLÍČE, VAŠE PRAVIDLA](../../Info%20Graphics/v5-cz/v5-01b-co-je-did.webp)

V takové síti byste mohli nahlásit prostřednictvím své identity, že vám někdo způsobil křivdu/škodu (a později případně, že ji napravil nebo byl donucen ji napravit). Aby taková zpětná vazba směřovaná k původci křivdy měla hodnotu relevantního zdroje, vložení informace do sítě musí stát čas, energii a peníze — a navíc o tom musí vzniknout ověřitelný důkaz pro ostatní, že nejde o plané tlachání.

Čtení informací by bylo snadné a relativně levné, ale vytvoření jednotlivého informačního záznamu nákladné a náročné. Zápis by podléhal jasnému protokolu, v němž by výpočet podle zvoleného algoritmu přísně určoval, jakou DID požádat o ověření vkládané informace a jak postupovat, aby vybraný účastník informaci vaším jménem zprocesoval, zveřejnil a stal se jejím ověřovatelem.

> [!note] Algoritmus vs radikalismus
> Algoritmický výběr ověřovatelů zajistí, že neradikální vydavatelé informací časem udržují téměř neutrální rovnováhu mezi náklady na zveřejněné informace a odměnami za ověřování.

![ZVEŘEJNĚNÍ STOJÍ ČAS, ENERGII A PENÍZE](../../Info%20Graphics/v5-cz/v5-02g-cena-publikace.webp)

Pojďme se podívat, jak algoritmus vybírá ověřovatele.

> [!note] Algoritmus
> Algoritmický výběr pro různé informace nedeterministicky volí jiného ověřovatele (nebo sadu možných ověřovatelů). Hash (jednosměrná matematická funkce, která z libovolného vstupu vytvoří unikátní „otisk" — jako otisk prstu dokumentu) kompletního DID dokumentu určuje pozici na konzistentním hash ringu a vybírá kandidáty na ověřovatele.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Lidsky řečeno: algoritmus vezme celý váš DID dokument, spočítá z něj otisk a ten určí vašeho ověřovatele.

![JAK ALGORITMUS VYBÍRÁ VÁŠHO OVĚŘOVATELE](../../Info%20Graphics/v5-cz/v5-02e-hash-ring.webp)

U prvního ověřovatele, kterého algoritmus vybere, jako vydavatel informace nemusíte uspět — vaše reputace nebo deklarovaná nastavení mu nemusí vyhovovat. Algoritmicky byste pokračovali v hledání dalšího tak, že rekurzivně provedete další iteraci a ten vám přidělí dalšího ověřovatele. S každým krokem se „vzdálenost" k cílovému ověřovateli zvyšuje, a tím rostou i doprovodná metadata, která se musí zveřejnit. S růstem dat přirozeně rostou i náklady (nejen kvůli výchozí velikosti tvrzení, ale i kvůli nabalujícím se metadatům z každého odmítnutí k ověření). Věrohodná informace projde mnohem snáze než nesmyslné rozmary. Záleží na každém, jak vysokou cenu je ochoten nést a jak moc mu na záznamu záleží — radikalismus se jisto-jistě prodraží.

![JAK OVĚŘOVATEL ODPOVÍDÁ](../../Info%20Graphics/v5-cz/v5-02e2-odpoved-verifikatora.webp)

Ať už se ověřovatel rozhodne v odpovědi na vaši žádost o ověření jakkoliv, míček se vrací zpět k vydavateli: ten může nabídku ověřovatele za ověřovací služby přijmout, založit odpověď do chronologie a zkusit to znovu (dráž), nebo odejít a smířit se s utopenými náklady.

![ROZHODNUTÍ ISSUERA](../../Info%20Graphics/v5-cz/v5-02e3-rozhodnuti-issuera.webp)

Abyste své informaci jako vydavatel, který má zájem na vydání informace, dodali větší váhu a lepší šanci na přijetí u ověřovatelů, mohli byste využít služeb **důvěryhodné autority**. Ta předloženou informaci buď odmítne, nebo přijme a vsadí na ni své dobré jméno (reputaci). Autorita obvykle požádá o předložení důkazů z reálného světa, ověří je a klasifikuje. Výstupem je protokol o jejím zhodnocení daného případu v daném čase. Autoritu si představte jako specialistu na jistý typ služeb v reálném i digitálním světě — např. vyšetřovatele, auditora, pojišťovnu, dodavatele jistého typu zboží (v podstatě každý ekonomický aktér na trhu).

![JAK VZNIKÁ ZÁZNAM V SÍTI](../../Info%20Graphics/v5-cz/v5-02a-jak-vznika-zaznam.webp)

V době, kdy se budete snažit publikovat informaci v síti, už patrně bude obsahovat informace o jejích aktérech — to jsou reputační signály. Orientovat se v tom, jak reputační signály číst — co pro vás v různých situacích znamenají a jaká rizika nesou — nemusí být triviální. Každý účastník se může přes svou DID na reputační záznamy dívat různě, podle situace, kterou s protistranou řeší. Je protistrana spolehlivý plátce, nebo musím chtít peníze předem při obchodním styku? Nemá v nabízeném produktu recenze na skryté podvody a vady? Nesnaží se zbavit smluvní odpovědnosti, když se něco nepovede? Někdy se hodí i komplexnější pohled na celkovou konzistenci protistrany — záleží na preferencích toho, kdo si náhled vyžádá. Trh by mohl nabízet produkty a služby, které čtení reputace v kontextu řešené situace zjednodušují, zpracovávají a vysvětlují. I k tomu mohou sloužit rozličné autority a jejich nabízené služby.

![JAK SE ČTE REPUTACE](../../Info%20Graphics/v5-cz/v5-02b-jak-se-cte-reputace.webp)

> [!example] Příklady
> Typické informace zajímavé pro vydavatele — a hodnotné pro ostatní — se týkají událostí mimo běžnou mezilidskou komunikaci v reálném nebo virtuálním světě.
>
> Negativní příklady:
> - důkazy o trestných činech (např. auditované důvěryhodným vyšetřovacím orgánem)
> - nepřímé důkazy (samy o sobě slabé, ale statisticky kumulativní) — např. opakovaná přítomnost v blízkosti více krádeží v krátkém čase → stále náhoda?
> - porušení smlouvy
>
> Pozitivní příklady:
> - napravená škoda (dobrovolně nebo z nátlaku komunity jako trest)
> - přijetí a odpykání trestu navrženého autoritou XY
> - autorita XY odejmula uznání vlastnických práv pachatele v určitém rozsahu
>
> Je na každém, aby si dostupné informace o protistraně sehnal a vyhodnotil rizika dle jeho preferencí

![CO MŮŽETE ZAZNAMENAT V SÍTI?](../../Info%20Graphics/v5-cz/v5-02d-priklady-zaznamu.webp)

> [!note] Zda se informace o vás v síti objeví, závisí výhradně na vašem vlastním chování.
> Do takové sítě se nikdy nemusíte připojit, a přesto se v ní mohou informace o vás objevit. Záleží výhradně na vašich činech a na tom, jaký mají dopad na ostatní.

![KOMUNITA VÁM JI MŮŽE OTEVŘÍT](../../Info%20Graphics/v5-cz/v5-01b2-komunitni-did.webp)

Právě jsem ve zkratce navenek popsal, jak by mohla fungovat sociální síť inspirovaná decentralizovanou identitou (DID). Primárním účelem konceptů DID je posílit soukromí a svobodu principem přihlášení se k pravidlům, která budu dodržovat a dle kterých budu žít — dát uživatelům možnost rozhodovat, jaké informace sdílet a za jakých podmínek. 

Navrhuji dále propojit DID do komunikační sítě, kde si jejich nositelé vyměňují zpětnou vazbu i mimo situace, kdy se někomu něco přihodilo a je třeba reagovat komunitně nebo jednotlivě. Takové preventivní porovnání pravidel, ke kterým jsme se přihlásili s možností si spočítat ekonomické a jiné dopady vzájemných odchylek představ o tom, jak by měl ten druhý fungovat, by se dalo považovat za motivaci k nacházení konsenzu. Namísto svobody by takový systém kladl důraz na dobrovolné rozhodování spojené s odpovědností za chování v reálném světě.

Jednotlivec systém sám nerozbije — skupina lidí má větší šanci a skupina lidí s vyjednaným konsenzem a motivacemi táhnout v mnoha věcech za jeden provaz ještě větší šanci bojovat s autoritářskými tendencemi. Předpoklad organizace z první kapitoly bude splněn, až se naplní dvě podmínky: DID reputační síť pokryje komunity natolik reprezentativně, že její používání přestane být exotické. A zároveň se tato komunitní část stane ekonomicky signifikantní menšinou, která může asertivně vyjednávat se zbytkem společnosti.

> [!note] Dobrovolnost vs svoboda
> Svoboda — v pozitivním smyslu — by byla sekundárním efektem vyvažování dvou faktorů: dobrovolnosti a tlaku okolí na odpovědnost.

> [!note] Éra AI a hodnota reputace
> V éře umělé inteligence se automatizuje vše, co souvisí s kognitivním myšlením — a možná to půjde ještě dál. Co potom v mezilidské činnosti zbude jako konkurenční výhoda? Odpověď je těžká a něco se jistě najde, ale jednu věc můžeme říct s jistotou: rozhodne reputace. Ověřitelná historie vašeho chování, vašich závazků a jejich plnění — to je něco, co za vás AI nepostaví.

![AI VÁM REPUTACI NEPOSTAVÍ — JEN VY SAMI](../../Info%20Graphics/v5-cz/v5-02f-ai-era-reputace.webp)

![EKONOMIKA PRAVDY](../../Info%20Graphics/v5-cz/v5-02c-ekonomika-pravdy.webp)
