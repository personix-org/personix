---
title: "Řešení zjevných pochybností"
chapter: 2
part: "Nástroj"
lang: cs
version: v6
source: "v1 callouts rozšířené ve v4"
---

# Řešení zjevných pochybností

Popsaný systém přirozeně vzbuzuje řadu otázek. Pojďme si ty nejčastější probrat.

## Závislost na technologii

Určitě vás již napadlo, že na rozdíl od moderního státu, který je s námi něco kolem 150 let, řešení reputační sítě, tak jak je zde popisována, závisí silně na technologii globálního/lokálního internetu. V případě jeho výpadku je fungování takové sítě ohroženo.

Jde-li o výpadek povahy dočasný, nedochází ke ztrátě dat, ani konzistence tvrzení v síti a nemělo by dojít, ani k narušení dosažených rovnováh reputací v komunitách. Na rozdíl od podobných platebních sítí se v této síti předpokládají velmi nízké četnosti procesů a údajů. V tomto se decentralizovaná reputační síť neliší od současného státu, který také nyní silně závisí na technologiích a odvykl si pracovat s papírovými kartotékami (v krizových plánech by ale neměl na vybranou).

Evoluční nástupce státu ve formě reputační sítě však může v případě trvalého výpadku (katastrofa nevídaného rozsahu) přejít zpět na primitivnější centralizovaný systém — stát.

Technologie nám umožňuje lidstvu dostat se na vyšší civilizační formy řízení a přináší nám benefity, ale i rizika.

## Nevyhodím publikováním v síti peníze oknem?

Náklady na publikaci tvrzení v reputační síti nejsou z valné části utopené. Užitečnost vydavatelova sdělení do sítě — informace o skutečných křivdách, ověřené zkušenosti, relevantní varování — se v delším časovém horizontu statisticky vrací zpět ve formě poplatků za ověřování tvrzení někoho jiného z komunity. Komunita z toho má prospěch, vydavatel buduje reputaci a náklady na publikaci pravdivých informací se tak blíží vratné záloze, od které je třeba odečíst jen menší část skutečných nákladů na údržbu sítě. Naopak nepravdivé nebo triviální záznamy se nevracejí — jejich náklady jsou čistá ztráta. Poctivost je tak nejen morální volba, ale i ekonomicky racionální strategie.

Po odečtení nákladů na údržbu sítě by se tento princip dal nazvat principem ekonomické neutrality — netratím, když jsem s komunitou, tratím, když jsem proti.

Komunita má i solidární kanály, jak ocenit čestný přístup svých členů. Nedělejme si ale iluze: apel na solidaritu většinou vychází ze společenského tlaku komunity, takže nemusí jít o solidaritu v dobrovolném slova smyslu.

## Co když si někdo založí víc identit?

Člověk může provozovat více DID identit paralelně. Budování reputace pro každou identitu však vyžaduje nezávislé úsilí — čas, energii, peníze.

Žádné zkratky: každá identita musí svůj track record[^trackrecord] nasbírat skutečnou aktivitou. Udržovat paralelní identity je proto záměrně drahé.

Ve svobodných společnostech náklady odrazují od zneužití.

V diktaturách se však paralelní identity stávají nástrojem přežití: umožňují organizování podzemních sítí, bezpečnější navigaci černým trhem a compartmentalizovaný[^compartmentalizace] odpor, kde kompromitování jedné identity neodhalí ostatní — a po svržení režimu umožňují plynule navázat na veřejný život a budovanou reputaci a klidně spojit předtím oficiální a tajnou DID tvrzením do jedné spojené množiny záznamů.

![CO KDYŽ SI NĚKDO ZALOŽÍ VÍC IDENTIT?](../../Info%20Graphics/v5-cz/v5-04a-vice-identit.webp)

> [!note] Vnímání naruby
> Na rozdíl od státu princip reputační sítě postavené na decentralizované identitě obrací paradigma vnímání pořadí důležitosti:
>
>- Důležitá je reputace, čili minulost pro hodnocení rizik interakce s protistranou a osobní údaje typu jména, adresy atp. mohou být předmětem zdvořilostní výměny dat
>- Kdežto stát požaduje primárně osobní data, shromažďuje reputační data a komunitě pouští jen to, co se mu zlíbí

## Nemůže si bohatý člověk prostě „koupit" víc identit (nebo vytvářet virtuální komunity)?

Možnost vytvářet paralelní decentralizované identity na první pohled vypadá jako nefér výhoda lidí s vyššími ekonomickými možnostmi oproti těm s nižšími. Je ale potřeba zdůraznit, že na rozdíl od centralizovaného systému, kde stačí zkorumpovat pár bodů v pyramidě moci, aby se zapomnělo na nějaké nekalosti, v decentralizovaném systému by dotyčný musel zkorumpovat celou komunitu.

K tomu by mu mohly sloužit náhradní decentralizované identity, jenže jejich reputaci je nutné budovat v čase reálnou interakcí se skutečnými dalšími členy komunity — nejde si ji prostě koupit, protože v síti je ověřitelné, jak si daná identita vede.

Navíc na trhu mohou (a patrně budou) existovat služby, které formou autority nabízejí investigaci důkazů, že několik decentralizovaných identit je ve skutečnosti tatáž osoba. Jediným záznamem do reputační sítě tak lze za zlomek ceny zmařit celou investici času, energie a peněz vloženou do budování paralelních identit.

Ekonomicky se tedy vyplatí komunitu nepodvádět — případně své činy zpytovat a hledat nápravu, aby se reputace dostala zpět na přijatelnou úroveň a její nositel hněvem komunity ekonomicky či jinak netrpěl.

Ekonomicky silná identita po ztrátě reputace ve vlastní komunitě může z hněvu komunity unikat pokoutnými obchody s vytipovanými identitami — jenže ty pak také riskují ztrátu své reputace.

Zbývá ještě únik k jiné komunitě s čerstvou identitou — to ale znamená nechat za sebou veškeré výdobytky a začít někde od nuly s nulovou reputací. Někdy to může být pochopitelná cesta a jediné východisko.

![CELOU KOMUNITU NEZKORUMPUJEŠ](../../Info%20Graphics/v5-cz/v5-04b-centralizace-vs-decentralizace.webp)

> [!note] Poznámka
> Obdobně by se komunity vypořádaly s útokem, kdy někdo věnuje prostředky na vytvoření virtuální identity: pro ni je rizikové vstupovat do interakce s jinou komunitou bez ověřování — tedy nekriticky přijímat informace o identitách druhé komunity. Reputace se vždy budují v rámci komunity, ne globálně.

## Co příživníci, kteří chtějí jen číst a nic komunitě nedávat?

Přístup k informacím není od prvního dne založení decentralizované identity neomezený. Noví účastníci — ti, kteří si dosud nevybudovali reputaci skutečnou aktivitou — narážejí na stupňovaná omezení: méně informací, delší čekání, vyšší náklady na dotazy. Síť odměňuje účast, ne pasivní konzumaci a vysávání dat jen tak na potkanou.

Decentralizovaná identita riskuje svoji reputaci i tehdy, když ji za úplatu propůjčí jiné osobě (která ani v DID reputační síti být nemusí). I tady platí: takové zrazení komunity (narušování soukromí) se může odrazit na reputaci zrádce, a ten si svůj čin nemůže nechat zahladit pokoutnou dohodou, jak je zvykem v centralizovaném systému. Musí počítat s hněvem komunity včetně ztráty výdobytků — komunita je v jeho očích například garantem privilegia vlastnit movité a nemovité věci.

> [!note] Kotva do reálného světa
> Při vyhodnocování rizik je přirozeně rizikovější ten subjekt, který nepožívá privilegia vlastnictví uznávaného danou komunitou — má totiž při svých jednáních méně co ztratit (digitální vlastnictví se přesouvá snáze). 
>
Vypadá to jako drobnost, ale má to velké důsledky. Chtít mít páku komunity na její členy implikuje vlastnictví jako privilegium — v nejsvobodnějších společnostech téměř nedotknutelné, ale stále ne právo ani základní princip, nýbrž privilegium, které v krajních případech může být odejmuto (dovedu si představit např. při odepření služby při obraně komunity v ozbrojeném konfliktu).
>
Podprahově to také odpovídá na to, jak se komunita zachová ke svým členům a jakou má člen motivaci za komunitu bojovat — aby si svá privilegia udržel. Člověk může ve své odpovědnosti vůči komunitě selhat, ale morálně nemůže očekávat shovívavost, pokud jde o udržení vydobytých privilegií.

![SÍŤ ODMĚŇUJE ÚČAST](../../Info%20Graphics/v5-cz/v5-04c-prizivnici.webp)

## Finanční neutralita
Při čtení slov jako decentralizovaný, nezcenzurovatelný, nezkorumpovatelný se člověk nemůže ubránit asociacím s nejznámějšími kryptoměnami Bitcoinem, Monerem a třeba Kaspou, které lze za takové označit. Intuice však klame a poplatky za platby služeb autorit, ověřování a publikování atp. však může být realizována v jakékoliv měně nebo penězích. Důležité pro navázané účastníky sociální sítě v DID síti (tj. vaší komunity) a jejího okolí je důležité reputačně podložené potvrzení o realizaci platby. Publikace tvrzení musí být jednotlivě přiměřeně ověřitelně nákladná, aby nedocházelo situaci, kdy si může aktér bez vynaložené energie, peněz a času publikovat kolik a jakých tvrzení chce — to je silně nežádoucí stav, který odpovídá privilegiu elit v současném státním zřízení plném korupce.

V tomto mají zmíněné kryptoměny malou výhodu, že jejich sítě plní role důvěryhodných autorit pro ověření, že k dané platbě došlo, za cenu malé ztráty soukromí a odhalení části svých adres.

[^trackrecord]: **Track record** (angl. *záznam výkonů*) — obecně: historie dosavadních výsledků, úspěchů i neúspěchů osoby nebo organizace. Zde: souhrn všech dosavadních interakcí dané DID identity v síti — ověřených tvrzení, přijatých i odmítnutých záznamů — z něhož se odvozuje její reputace.

[^compartmentalizace]: **Compartmentalizace** (z angl. *compartment* — oddíl, přihrádka) znamená oddělení informací do izolovaných celků tak, aby prozrazení jednoho celku neohrozilo ostatní. Princip známý ze zpravodajských služeb: agent zná jen svou část operace, takže i pod nátlakem nemůže prozradit celek.
