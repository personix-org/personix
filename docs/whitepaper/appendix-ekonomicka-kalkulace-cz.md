---
title: "Appendix: Demokratizace ekonomické kalkulace"
subtitle: "Odpověď na námitku, že v RSN ekonomická kalkulace neexistuje"
author: "Pavel Kudrna"
date: 2026-04-23
version: "v1"
lang: cs
navazuje_na: "whitepaper-draft-v1-cz.md (Decentralizovaná reputační síť: Rámec pro dobrovolnou organizaci společnosti)"
---

# Appendix: Demokratizace ekonomické kalkulace

*Tento text navazuje na whitepaper „Decentralizovaná reputační síť" a neaspiruje na revizi jeho obsahu. Slouží jako samostatná odpověď na předvídatelnou kritickou námitku z pozice rakouské ekonomické školy.*

## 1. Námitka, kterou tento text řeší

Každý návrh organizace společnosti, který odebírá kompetence státu, naráží na stejnou klasickou kritiku: **problém ekonomické kalkulace** formulovaný Ludwigem von Misesem (1920) a rozvinutý F. A. Hayekem (1945). V krátkosti:

> „Bez tržních cen výrobních faktorů, vzniklých směnou soukromého vlastnictví, nelze racionálně porovnat alternativní způsoby užití zdrojů. Utopické systémy, které odstraňují nebo deformují cenový systém, nevyhnutelně selžou na neschopnosti rozhodnout, co je hospodárné a co plýtvavé."

Kritik může namítnout: „Vaše reputační síť je další utopie. Nahrazujete tržní ceny reputačními body. Na tom krachli plánovači ve 20. století, zkrachujete i vy."

Tento appendix ukazuje, proč je námitka mylná — nikoli proto, že by Misesův argument byl špatný, ale proto, že **reputační síť (RSN) nedělá to, co Mises kritizoval**. Neodstraňuje trh ani ceny. Naopak, rozšiřuje dosah tržní kalkulace do oblasti, která dnes žádnou kvantifikovatelnou kalkulaci nemá — a to právě díky tomu, že ji dnes monopolizuje stát nebo platformy.

## 2. Co ekonomická kalkulace skutečně je

Ekonomická kalkulace je schopnost racionálně porovnat alternativní užití zdrojů. Má tři ireducibilní předpoklady:

1. **Společný jmenovatel** — heterogenní zdroje (práce, kapitál, půda, suroviny) musí být srovnatelné na jedné škále. Peníze jsou jediný historicky ověřený univerzální jmenovatel.
2. **Distribuovaná znalost** — informace o vzácnosti, preferencích a možnostech je rozptýlena mezi miliony aktérů. Žádný plánovač ji nemá celou [16].
3. **Signalizační mechanismus** — ceny vznikají ze směny a fungují jako informační systém, který přenáší znalost bez potřeby jejího explicitního sdělování.

Utopické systémy (centrální plánování, technokracie, ekonomika darů v měřítku společnosti) selhávají, protože **odstraňují jeden nebo více z těchto tří pilířů**. RSN nedělá nic z toho.

## 3. Co RSN ve skutečnosti dělá

RSN neruší peníze. Neruší tržní směnu. Neruší soukromé vlastnictví. Zavádí **druhý komplementární signál** vedle ceny — reputační signál rizika protistrany — a činí ho:

- **decentralizovaným** (nelze ho zcenzurovat ani zmanipulovat centrálně),
- **veřejně ověřitelným** (kryptograficky podepsaným, strojově čitelným),
- **ekonomicky drahým zfalšovat, levným ověřit** (princip drahého radikalismu).

Tento signál existuje i dnes, ale v podobách, které Misesovu i Hayekovu kritiku paradoxně potvrzují:

| Dnešní nositel signálu rizika | Problém z hlediska kalkulace |
|---|---|
| **Státní rejstříky, licence, soudní rozhodnutí** | Cenzurovatelné, politicky vychýlené, pomalé — signál je zkreslen centrálním aktérem |
| **Bankovní kreditní skóre** | Uzavřený monopol několika institucí, neprůhledná metodika, mimo dosah běžného jednotlivce |
| **Platformové reputace (eBay, Google, Uber)** | Soukromý monopol s možností cenzury a manipulace, bez přenositelnosti mezi platformami |
| **Intuice a ústní doporučení** | Neagregovatelné, neškálovatelné, neověřitelné |

Ve všech čtyřech případech existuje **informační asymetrie** — což je přesně situace, ve které podle Akerlofa [18] tržní mechanismus selhává nebo degeneruje (market for lemons). RSN tuto asymetrii odstraňuje tím, že činí reputační signál veřejným statkem, který lze zahrnout do tržní kalkulace jako plnohodnotný vstup.

## 4. Formální vyjádření: očekávaná cena rizika

Jakmile je reputační signál veřejně dostupný a kvantifikovatelný, riziko transakce přestává být subjektivní tušení a stává se **kalkulovatelnou veličinou** standardního risk managementu.

Základní vzorec očekávané ztráty (v odborné literatuře *Annualized Loss Expectancy*, v pojišťovnictví *Pure Premium*):

$$
E[L] = P(\text{událost} \mid \tau) \times S
$$

kde:
- $E[L]$ je **očekávaná ztráta** za dané období nebo daný počet transakcí,
- $P(\text{událost} \mid \tau)$ je **pravděpodobnost** výskytu rizikové události v intervalu $\tau$ (časovém nebo transakčním),
- $S$ je **závažnost** — náklady na likvidaci následků události, pokud nastane.

Pravděpodobnost $P$ je přímou funkcí reputačního profilu protistrany. Čím delší a konzistentnější behaviorální historie, tím užší interval nejistoty. Závažnost $S$ je dána povahou transakce (výše smluvní expozice, nahraditelnost protistrany, časová kritičnost).

**Tento výraz jsou skutečné peníze, se kterými musí podnikatel, spotřebitel nebo věřitel počítat.** Jsou to peníze, které buď zaplatí předem formou mitigace (pojistka, záloha, escrow, diverzifikace protistran), nebo je v dlouhodobém průměru ztratí ve formě realizovaných škod. Nejsou to „teoretické" peníze. Jsou to peníze, které dnes platí každý, jen je nevidí, protože jsou rozmazané v režijních nákladech, marže pojistitelů a pokrytectví regulace.

## 5. Co z toho konkrétně plyne pro tržní kalkulaci

RSN umožňuje to, co dnes systematicky dělají pouze banky a pojišťovny: **cenovat riziko**. A dělá to dostupné komukoli. Tři praktické důsledky:

**5.1 Nižší rozptyl, nižší pojistné.** Transakce s prověřenou protistranou má užší interval možných ztrát. V pojistně-matematické logice to znamená nižší pojistné pro obě strany — riziko se přesouvá z tail distribuce do měřitelného středu. Totéž platí pro úvěrovou prémii, záruky, zálohy. Rozdíl mezi dnešními pojistnými sazbami (kalkulovanými bez přístupu k reputačním datům) a sazbami budoucími (s plným přístupem) je přímá a kvantifikovatelná úspora pro účastníky sítě.

**5.2 Vyčíslitelná cena důvěry.** Dnes se „důvěra" v ekonomických modelech objevuje jako reziduální proměnná nebo kulturní konstanta. V RSN má důvěra konkrétní tržní cenu — rozdíl mezi náklady transakce s anonymní protistranou a náklady transakce s reputačně silnou protistranou. Tato cena je pozorovatelná, porovnatelná a obchodovatelná.

**5.3 Demokratizace hodnocení rizika.** Nástroje systematického hodnocení protistrany dnes patří profesionálům — bankovním rizikovým oddělením, pojišťovnám, firemním due diligence týmům. Běžný občan je postrádá a nahrazuje je intuicí nebo drahou expertní službou. RSN činí tyto nástroje dostupnými v marginálních nákladech, přičemž zachovává možnost trhu konkurenčních interpretačních služeb (kapitola 6.4 whitepaperu).

## 6. Limity: kde naše tvrzení končí

Poctivost vyžaduje uvést, kam tento argument nesahá.

**6.1 Knightovo rozlišení risk vs. uncertainty.** Frank Knight (1921) odlišil *riziko* (známá distribuce pravděpodobnosti) od *nejistoty* (neznámá distribuce). Reputační síť posouvá významnou část jevů z kategorie nejistoty do kategorie rizika — právě tím, že generuje statisticky zpracovatelnou historii. Ale ne vše. „Černé labutě" podle Taleba [22] zůstávají nekvantifikovatelné a žádný reputační systém je neodstraní.

**6.2 Očekávaná hodnota není deterministická cena.** $E[L]$ platí jako průměr přes mnoho opakování. U jedné konkrétní transakce zaplatíte nulu nebo plnou škodu. Pro malé subjekty s malým počtem transakcí zůstává riziko diskrétní a agregovaný průměr je zavádějící. Řešením je sdružování rizika (pojistný trh, vzájemná podpora), kde RSN opět přináší přesnější oceňování.

**6.3 Risk aversion zvyšuje skutečný výdaj.** Racionální aktéři nejsou risk-neutrální. Pojistné v praxi = očekávaná ztráta + přirážka za averzi + kapitálové náklady + zisk pojistitele. Skutečný výdaj na mitigaci rizika je proto vyšší než matematická očekávaná hodnota. Rozdíl je cena, kterou aktér platí za psychologický klid — legitimní položka kalkulace, nikoli iracionalita.

**6.4 Reputace nenahrazuje ceny výrobních faktorů.** Misesův původní argument o cenách výrobních faktorů zůstává platný a RSN si nenárokuje jeho vyvrácení. Reputace není substitut ceny kapitálu, práce ani surovin. Je komplementárním signálem pro dimenzi, kterou cena sama neposkytuje — spolehlivost protistrany.

## 7. Historické precedenty: reputační sítě skutečně fungovaly

Tvrzení, že decentralizovaná reputace může nést ekonomicky významnou funkci, není spekulativní. Historie poskytuje empirické případy.

**Maghribští obchodníci 11. století** (Greif [21]) provozovali dálkový obchod Středomořím bez vymahatelné státní jurisdikce. Reputační síť obchodníků — psaná korespondence s ověřitelnou historií chování — fungovala jako substitut státního soudu. Odchýlení se od norem znamenalo vyloučení z obchodní sítě a ekonomickou likvidaci. Empiricky doložená úspěšnost tohoto uspořádání trvala několik generací.

**Elinor Ostrom** (Nobelova cena 2009, [20]) empiricky zdokumentovala desítky případů governance commons — společných zdrojů spravovaných komunitami bez státu i bez klasického trhu, s reputačními a normativními mechanismy. Její práce vyvrací předpoklad, že jediné dvě alternativy jsou stát a ziskový trh.

**Spence — signaling theory** (Nobelova cena 2001, [19]) formalizovala, jak nákladné, ale ověřitelné signály (vzdělání, certifikace) překonávají informační asymetrii. Reputační záznam v RSN je přímou aplikací této teorie: kryptograficky ověřitelný, ekonomicky nákladný signál chování.

**Hurwicz — mechanism design** (Nobelova cena 2007, [23]) ukázal, že kooperativní výsledky lze dosáhnout decentralizovaně, jestliže mechanismus správně strukturuje motivace (incentive compatibility). Algoritmický výběr ověřovatelů v RSN je takovým mechanismem.

Ekonomická profese tedy již přibližně půl století ukazuje, že prostor mezi čistým státem a čistou anonymní tržní směnou je obsaditelný funkčními institucemi. RSN není vynálezem této možnosti — je její současnou technologickou implementací.

## 8. Závěr

RSN neruší ekonomickou kalkulaci. **Předpokládá ji, potřebuje ji a rozšiřuje oblast, kde ji lze provádět.**

Přesná formulace pro diskusi s kritiky:

> *Ekonomickou kalkulaci neodstraňujeme. Odebíráme monopol na infrastrukturu, která ji umožňuje v oblasti rizika protistrany. Dnes tento monopol drží stát (regulace, soudy, rejstříky) a několik globálních platforem (kreditní skóre, tržní recenze). Reputační síť vrací tento signál do rukou účastníků trhu jako veřejný, ověřitelný a neztratitelný vstup standardní peněžní kalkulace.*

Pokud kritik tvrdí, že decentralizovaná reputace ekonomickou kalkulaci ničí, zatěžuje důkazní břemeno na stranu, která musí vysvětlit, proč by demokratizace kalkulačního vstupu byla horší než jeho současná monopolizace. Historická data ani teorie tento směr argumentace nepodporují.

RSN činí tržní mechanismus úplnějším, ne marginálnějším.

---

## Reference

[1] P. Kudrna, „Decentralizovaná reputační síť: Rámec pro dobrovolnou organizaci společnosti," whitepaper, Praha, 2026.

[15] L. von Mises, „Die Wirtschaftsrechnung im sozialistischen Gemeinwesen," *Archiv für Sozialwissenschaften*, vol. 47, 1920. Anglický překlad: „Economic Calculation in the Socialist Commonwealth," Ludwig von Mises Institute, 1990.

[16] F. A. Hayek, „The Use of Knowledge in Society," *American Economic Review*, vol. 35, no. 4, pp. 519–530, 1945.

[17] F. H. Knight, „Risk, Uncertainty and Profit," Hart, Schaffner & Marx, Boston, 1921.

[18] G. A. Akerlof, „The Market for 'Lemons': Quality Uncertainty and the Market Mechanism," *Quarterly Journal of Economics*, vol. 84, no. 3, pp. 488–500, 1970.

[19] M. Spence, „Job Market Signaling," *Quarterly Journal of Economics*, vol. 87, no. 3, pp. 355–374, 1973.

[20] E. Ostrom, „Governing the Commons: The Evolution of Institutions for Collective Action," Cambridge University Press, 1990.

[21] A. Greif, „Institutions and the Path to the Modern Economy: Lessons from Medieval Trade," Cambridge University Press, 2006.

[22] N. N. Taleb, „The Black Swan: The Impact of the Highly Improbable," Random House, 2007.

[23] L. Hurwicz, „The Design of Mechanisms for Resource Allocation," *American Economic Review*, vol. 63, no. 2, pp. 1–30, 1973.
