---
title: "Odpovede na zjavné pochybnosti"
chapter: 2
part: "Nástroj"
lang: en
version: v6
source: "v1 callouts extended in v4"
---

# Odpovede na zjavné pochybnosti

Opísaný systém prirodzene vyvoláva množstvo otázok. Poďme sa venovať tým najčastejším.

## Závislosť od technológie

Pravdepodobne si si už všimol, že na rozdiel od moderného štátu — ktorý je s nami asi 150 rokov — riešenie reputačnej siete tak, ako je tu opísané, silno závisí od technológie globálneho/lokálneho internetu. V prípade výpadku je fungovanie takej siete ohrozené.

Ak je výpadok dočasný, nedochádza k strate dát ani konzistentnosti tvrdení v sieti a ani dosiahnuté reputačné bilancie v rámci komunít by nemali byť narušené. Na rozdiel od porovnateľných platobných sietí táto sieť predpokladá veľmi nízke frekvencie procesov a dátových položiek. V tomto sa decentralizovaná reputačná sieť nelíši od dnešného štátu, ktorý je tiež už teraz silno závislý od technológie a zabudol pracovať s papierovými kartotékami (hoci v krízových plánoch by nemal na výber).

Evolučný nástupca štátu v podobe reputačnej siete môže v prípade trvalého výpadku (katastrofy nevídaného rozsahu) padnúť späť na primitívnejší centralizovaný systém — štát.

Technológia umožňuje ľudstvu dosiahnuť vyššie civilizačné formy vládnutia a prináša nám výhody, no aj riziká.

## Nehádžem zverejňovaním v sieti peniaze z okna?

Náklady na zverejnenie tvrdenia v reputačnej sieti sú z veľkej časti nie utopené. Užitočnosť správy, ktorú vydavateľ vloží do siete — informácie o skutočných krivdách, overené skúsenosti, relevantné varovania — sa štatisticky vracia v dlhšom časovom horizonte v podobe poplatkov za overovanie cudzích tvrdení z komunity. Komunita profituje, vydavateľ si buduje reputáciu a náklady na zverejnenie pravdivej informácie sa tak blížia vratnej zálohe, od ktorej treba odpočítať len menšiu časť skutočných nákladov na údržbu siete. Naopak, nepravdivé či triviálne záznamy sa nevracajú — ich náklady sú čistou stratou. Poctivosť teda nie je len morálnou voľbou, ale aj ekonomicky racionálnou stratégiou.

Po odpočítaní nákladov na údržbu siete by sa tento princíp dal nazvať princípom ekonomickej neutrality — nestrácam, keď som s komunitou, strácam, keď som proti nej.

Komunita má aj solidárne kanály na ocenenie poctivého prístupu svojich členov. Nerobme si však ilúzie: apely na solidaritu vznikajú väčšinou zo sociálneho tlaku komunity, takže nemusí ísť o solidaritu v dobrovoľnom zmysle slova.

## Čo ak si niekto vytvorí viacero identít?

Človek môže paralelne prevádzkovať viacero DID identít. Budovanie reputácie pre každú identitu si však vyžaduje samostatné úsilie — čas, energiu, peniaze.

Žiadne skratky: každá identita si musí nazbierať svoj track record[^trackrecord] cez skutočnú aktivitu. Udržiavanie paralelných identít je preto zámerne drahé.

V slobodných spoločnostiach náklady odrádzajú od zneužitia.

V diktatúrach sa však paralelné identity stávajú nástrojom prežitia: umožňujú organizovať podzemné siete, bezpečnejšie sa pohybovať na čiernom trhu a viesť kompartmentalizovaný[^compartmentalization] odboj, kde kompromitácia jednej identity neodhalí ostatné — a po páde režimu umožňujú plynulý návrat do verejného života a k tam vybudovanej reputácii, ba dokonca zlúčenie predtým oficiálnej a tajnej DID do jedinej kombinovanej množiny záznamov prostredníctvom tvrdenia.

![WHAT IF SOMEONE CREATES MULTIPLE IDENTITIES?](../../Info%20Graphics/v5/v5-04a-vice-identit.webp)

> [!note] Vnímanie obrátené naruby
> Na rozdiel od štátu princíp reputačnej siete postavenej na decentralizovanej identite obracia paradigmu vnímanej priority:
>
> - Dôležitá je reputácia — teda minulosť, ktorá sa používa na posúdenie rizík interakcie s protistranou — a osobné údaje ako mená, adresy atď. môžu byť vecou zdvorilostnej výmeny dát
> - Zatiaľ čo štát primárne vyžaduje osobné údaje, hromadí reputačné dáta a komunite ukáže len to, čo sa mu hodí

## Nemôže si bohatý človek jednoducho „kúpiť“ viac identít (alebo vytvoriť virtuálne komunity)?

Možnosť vytvárať paralelné decentralizované identity na prvý pohľad vyzerá ako nespravodlivá výhoda ľudí s väčšími ekonomickými prostriedkami oproti tým s menšími. Treba však zdôrazniť, že na rozdiel od centralizovaného systému, kde stačí skorumpovať pár bodov v pyramíde moci, aby určité previnenia zmizli, v decentralizovanom systéme by bolo treba skorumpovať celú komunitu.

Náhradné decentralizované identity by tomuto účelu mohli poslúžiť, ale ich reputácia musí byť budovaná v čase cez reálnu interakciu so skutočnými inými členmi komunity — nedá sa jednoducho kúpiť, pretože sieť robí overiteľným, ako si daná identita počína.

Navyše na trhu môžu existovať (a pravdepodobne aj budú) služby, ktoré ako autorita ponúkajú vyšetrovania produkujúce dôkaz, že niekoľko decentralizovaných identít je v skutočnosti tá istá osoba. Jediný záznam vložený do reputačnej siete tak môže za zlomok nákladov znehodnotiť celú investíciu času, energie a peňazí vynaloženú na budovanie paralelných identít.

Ekonomicky sa teda oplatí komunitu nepodvádzať — a keď treba, preskúmať svoje činy a usilovať sa o nápravu, aby sa reputácia vrátila na prijateľnú úroveň a jej nositeľ nestrádal ekonomicky ani inak pod hnevom komunity.

Ekonomicky mocná identita, ktorá stratila reputáciu vo vlastnej komunite, sa môže pokúsiť uniknúť hnevu komunity cez podpultové dohody s cielenými identitami — tie však potom tiež riskujú stratu vlastnej reputácie.

Stále ostáva únik do inej komunity s čerstvou identitou — to však znamená nechať za sebou všetky výdobytky a začať niekde od nuly s nulovou reputáciou. Niekedy to môže byť pochopiteľná cesta a jediné východisko.

![YOU CAN'T CORRUPT AN ENTIRE COMMUNITY](../../Info%20Graphics/v5/v5-04b-centralizace-vs-decentralizace.webp)

> [!note] Poznámka
> Podobne by komunity riešili útok, pri ktorom niekto venuje zdroje na vytvorenie virtuálnej identity: pre takú identitu je riskantné vstúpiť do interakcie s inou komunitou bez overenia — teda nekriticky prijímať informácie o identitách druhej komunity. Reputácie sa vždy budujú v rámci komunity, nie globálne.

## Čo s prispôsobivcami, ktorí chcú len čítať a komunite nedať nič?

Prístup k informáciám nie je od prvého dňa vytvorenia decentralizovanej identity neobmedzený. Noví účastníci — tí, čo si ešte nevybudovali reputáciu skutočnou aktivitou — čelia stupňovaným obmedzeniam: menej informácií, dlhšie čakacie doby, vyššie náklady na dotazy. Sieť odmeňuje účasť, nie pasívnu spotrebu a svojvoľné zberanie dát.

Decentralizovaná identita riskuje svoju reputáciu aj vtedy, keď ju za odplatu prepožičia inej osobe (ktorá ani nemusí byť v reputačnej sieti DID). Platí tu rovnaký princíp: taká zrada komunity (porušenie súkromia) sa môže odraziť na reputácii zradcu a čin sa nedá vymazať podpultovou dohodou tak, ako to funguje v centralizovanom systéme. Musí rátať s hnevom komunity vrátane straty výdobytkov — komunita je totiž v jeho očiach garantom napríklad výsady vlastniť hnuteľný a nehnuteľný majetok.

> [!note] Kotva k reálnemu svetu
> Pri posudzovaní rizika je rizikovejším subjektom prirodzene ten, kto nepožíva výsadu vlastníctva uznaného danou komunitou — má vo svojom počínaní menej čo stratiť (digitálne aktíva sa presúvajú ľahšie).
>
Môže to vyzerať ako drobnosť, no má to veľké dôsledky. Ak chceme, aby komunita mala páku na svojich členov, znamená to vlastníctvo ako výsadu — v najslobodnejších spoločnostiach takmer nedotknuteľnú, no stále nie právo ani základný princíp, ale výsadu, ktorá sa v krajných prípadoch môže odňať (viem si predstaviť napríklad odmietnutie služby v obrane komunity v ozbrojenom konflikte).
>
Podprahovo to zároveň odpovedá na to, ako bude komunita zaobchádzať so svojimi členmi a akú motiváciu má člen bojovať za komunitu — udržať si svoje výsady. Človek môže zlyhať vo svojej zodpovednosti voči komunite, ale morálne nemôže očakávať zhovievavosť, keď ide o udržanie ťažko získaných výsad.

![THE NETWORK REWARDS PARTICIPATION](../../Info%20Graphics/v5/v5-04c-prizivnici.webp)

## Finančná neutralita

Pri čítaní slov ako decentralizovaný, necenzurovateľný, neskorumpovateľný si ich človek nevyhnutne spája s najznámejšími kryptomenami — Bitcoin, Monero a povedzme Kaspa — ktoré sa dajú takto opísať. Intuícia tu však zavádza: poplatky za služby autorít, za overenie a zverejnenie a podobne sa dajú vyrovnať v ľubovoľnej mene alebo peniazoch. Pre prepojených účastníkov sociálnej siete v sieti DID (teda tvoju komunitu) a jej okolie je dôležité reputáciou podložené potvrdenie, že platba prebehla. Zverejnenie tvrdenia musí individuálne niesť rozumnú, overiteľnú cenu, aby aktér nemohol zverejniť koľkokoľvek a akékoľvek tvrdenia bez vynaloženia energie, peňazí a času — silno nežiaduci stav zodpovedajúci výsade elít v dnešných korupciou prežratých štátnych systémoch.

V tomto majú spomínané kryptomeny malú výhodu v tom, že ich siete pôsobia ako dôveryhodné autority na overenie, že daná platba prebehla, za cenu malej straty súkromia a odhalenia niektorých svojich adries.

[^trackrecord]: **Track record** — všeobecne: história minulých výsledkov, úspechov a zlyhaní osoby alebo organizácie. Tu: súhrn všetkých minulých interakcií danej DID identity v sieti — overené tvrdenia, prijaté a zamietnuté záznamy — z ktorých sa odvodzuje jej reputácia.

[^compartmentalization]: **Kompartmentalizácia** (z angl. *compartment*) znamená oddelenie informácií do izolovaných jednotiek tak, aby odhalenie jednej jednotky neohrozilo ostatné. Princíp známy zo spravodajských služieb: agent pozná len svoju časť operácie, takže ani pod nátlakom nemôže odhaliť celok.
