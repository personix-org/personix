---
title: "Slovníček pojmov"
part: "Príloha"
lang: en
version: v6
---

# Slovníček pojmov

| Pojem | Slovensky | Význam |
|------|-------|---------|
| **Authority** | Autorita | Dôveryhodný subjekt (osoba, organizácia), ktorý overuje informácie a vsádza na ne svoju reputáciu. Môže byť špecializovaný (vyšetrovací, právny, technický). |
| **Claim** | Tvrdenie | Všeobecne: akýkoľvek overiteľný výrok. Tu: záznam zverejnený do reputačnej siete — tvrdenie o udalosti, vlastnosti alebo vzťahu, ktoré je kryptograficky podpísané a overené. Napr. „som obyvateľom obce X“ alebo „táto osoba porušila zmluvu“. |
| **Compartmentalization** | Kompartmentalizácia | Všeobecne: oddelenie informácií do izolovaných jednotiek tak, aby odhalenie jednej jednotky neohrozilo ostatné. Princíp známy zo spravodajských služieb. Tu: paralelné identity DID v diktatúrach — kompromitácia jednej neodhalí ostatné. |
| **Consistent Hash Ring** | Hash ring | Algoritmický mechanizmus na výber overovateľov — pozíciu na ringu určuje hash DID dokumentu v rámci sociálneho grafu. Zabezpečuje nedeterministický, no overiteľný výber. |
| **DID** | DID (Decentralizovaná identita) | Digitálna identita, ktorú si vytváraš a ovládaš sám, bez centrálnej autority. Kryptograficky podpísaná tvojím súkromným kľúčom — nikto ju nemôže zrušiť ani sfalšovať. |
| **DID Document** | DID dokument | Verejne dostupný dátový súbor opisujúci tvoju identitu DID — obsahuje verejné kľúče, sieťové adresy a metadáta. Používa sa na overenie tvojej identity v sieti. |
| **Due Diligence** | Due diligence | Všeobecne: dôkladné preverenie protistrany pred vstupom do obchodného alebo právneho vzťahu — kontrola jej histórie, financií, reputácie a rizík. Tu: v reputačnej sieti prebieha rýchlejšie a automatickejšie vďaka dostupnosti overených záznamov. |
| **Economic Neutrality Principle** | Princíp ekonomickej neutrality | Poctivé správanie v sieti je ekonomicky blízke nule — náklady na zverejnenie sa vracajú ako odmeny za overovanie. Nepoctivé správanie je čistá strata. |
| **Emergent** | Emergentný | Spontánne vznikajúci z interakcií jednoduchších častí, bez toho, aby to niekto navrhol alebo riadil. Kŕdeľ vtákov letí vo formácii bez plánu — formácia emerguje z jednoduchých pravidiel, ktoré dodržiava každý jednotlivec. |
| **Emergent Social Contract** | Emergentná spoločenská zmluva | Pravidlá správania, ktoré nevznikajú zhora (zákon), ale zdola — z opakovaných interakcií a konsenzu v rámci komunity. |
| **ESR** | Electronic Spending Register | Navrhovaný systém priehľadného sledovania verejných výdavkov — každý zrealizovaný výdavok štátu sa páruje s plánovanou platbou. Inšpirovaný českým EET, ale obrátený proti štátu. |
| **Hash** | Hash (odtlačok) | Všeobecne: jednosmerná matematická funkcia, ktorá z ľubovoľného vstupu vyrobí jedinečný „odtlačok“ pevnej dĺžky — ako odtlačok prsta dokumentu. Rovnaký vstup vždy dá rovnaký výstup, ale zo vstupu sa nedá odvodiť výstup naspäť. Tu: používa sa na určenie pozície na hash ringu a na overenie integrity dokumentu. |
| **Just-in-Time Funding** | Just-in-time financovanie | Financovanie štátu podmienené transparentnosťou — peniaze plynú len vtedy, keď štát prijme ESR a spáruje svoje výdavky. Páka na vynútenie spolupráce. |
| **Meritocracy** | Meritokracia | Všeobecne: systém, kde postavenie určujú skutočné zásluhy a preukázaná schopnosť, nie formálne tituly, konexie či zdedená výsada. Tu: reputačná sieť prirodzene zvýhodňuje tých, ktorí preukázateľne prispievajú komunite — ich hlas má väčšiu váhu vďaka track recordu, nie vďaka úradu. |
| **Onion Gateway** | Onion gateway | Sieťová adresa identity DID v onion sieti. Oddelená od DID dokumentu — dá sa zmeniť bez straty identity (podobne ako zmena IP adresy za doménou). |
| **Onion Routing** | Onion routing (Tor) | Komunikačný protokol, ktorý zabezpečuje necenzurovateľnosť siete. Správy sú šifrované vo vrstvách — každý uzol odlúpne jednu vrstvu, ale nepozná celú cestu. |
| **Oracle Problem** | Problém orákula | Všeobecne: ako zabezpečiť, aby dáta vstupujúce do digitálneho systému verne zodpovedali tomu, čo sa naozaj stalo vo fyzickom svete. Pojem pochádza z oblasti blockchainu. Tu: rieši sa cez autority, ktoré vsádzajú svoju reputáciu ako záruku, že digitálny záznam zodpovedá fyzickej realite. |
| **Phenomenological** | Fenomenologický | Všeobecne: prístup, ktorý skúma javy tak, ako sa prejavujú v priamej skúsenosti, pozorovaním toho, čo z nich vyplýva, bez vopred daných teórií. Tu: sloboda, spoločenská zmluva a normy správania sú pozorované javy — dôsledky tisícov mikrointerakcií medzi ľuďmi, nie princípy definované zhora. |
| **Policy** | Policy (politika) | Všeobecne: súbor pravidiel alebo princípov riadiacich správanie v danom kontexte. Tu: každý účastník siete DID deklaruje svoju policy — ako reaguje na konkrétne správanie iných, ktoré pravidlá dodržiava a ktoré tresty považuje za primerané. Súhrn politík tvorí emergentnú spoločenskú zmluvu. |
| **Proxy** | Proxy | Všeobecne: zástupca alebo sprostredkovateľ — systém alebo subjekt konajúci v mene iného. Tu použité v dvoch kontextoch: (1) ESR ako proxy párujúce verejné výdavky s plánovanými platbami; (2) pozorovatelia ako proxy medzi vydavateľom a overovateľom v triku s pozorovateľmi. |
| **Publisher** | Vydavateľ | Účastník siete, ktorý vytvára a zverejňuje záznam (tvrdenie o krivde, náprave a podobne). Nesie náklady na zverejnenie. |
| **Reputation-Based Social Network (RSN)** | Reputačná sieť | Decentralizovaná sociálna sieť, kde si účastníci vymieňajú spätnú väzbu o správaní v reálnom svete. Záznamy sú nákladné na vytvorenie, lacné na čítanie. |
| **Reputation Signal** | Reputačný signál | Jednotlivý záznam v sieti — pozitívny (náprava ujmy, splnenie záväzku) alebo negatívny (krivda, porušenie zmluvy). Kumulatívne signály tvoria reputačný profil. |
| **Social Graph** | Sociálny graf | Sieť tvojich kontaktov a kontaktov tvojich kontaktov. Algoritmus hľadá overovateľov do konfigurovateľnej hĺbky (napríklad 3 úrovne). Žiadny globálny blockchain — sieť prirodzene tvorí komunity s presahmi. |
| **Tax Allocation** | Alokácia daní | Mechanizmus, ktorým daňovník rozhoduje, kam ide časť jeho daní. Alokovateľné percento z roka na rok rastie. |
| **Track Record** | Track record | Všeobecne: história minulých výsledkov, úspechov a zlyhaní osoby alebo organizácie. Tu: súhrn všetkých minulých interakcií danej identity DID v sieti — overené tvrdenia, prijaté a zamietnuté záznamy — z ktorých sa odvodzuje jej reputácia. |
| **Verifier** | Overovateľ | Účastník algoritmicky vybraný na overenie a zverejnenie záznamu. Vsádza svoje dobré meno na pravdivosť informácie. |
