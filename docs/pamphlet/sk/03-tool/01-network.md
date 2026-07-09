---
title: "Reputačná sociálna sieť"
chapter: 2
part: "Nástroj"
lang: en
version: v6
source: v1
---

# Reputačná sociálna sieť

Na dosiahnutie zmeny potrebujeme starostlivo navrhnutý nástroj. Najprv ho stručne načrtneme; v neskorších kapitolách si každú časť rozoberieme podrobnejšie a niečo pridáme. Predstav si necenzurovateľnú, globálnu, decentralizovanú sociálnu sieť, kde by si mohol bezpečne vytvárať a spravovať svoju zastupiteľskú identitu — takzvanú decentralizovanú identitu (DID). DID je digitálna identita, ktorú si vytváraš a ovládaš sám, bez závislosti od akejkoľvek centrálnej autority. Nikto ti ju nemôže vziať ani sfalšovať, pretože je kryptograficky podpísaná tvojím súkromným kľúčom (alebo kľúčmi, cez multisig).

> [!note] Poznámka
> Jedným z dôsledkov je, že taká identita by mohla postupne nahradiť štátom vydávané doklady totožnosti — ale o tom viac v kapitole o prechode.

![YOUR IDENTITY, YOUR KEYS, YOUR RULES](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

V takej sieti by si mohol prostredníctvom svojej identity nahlásiť, že ti niekto spôsobil ujmu (a neskôr prípadne, že ju napravil alebo bol k tomu donútený). Aby táto spätná väzba — namierená na pôvodcu ujmy — mala hodnotu ako relevantný zdroj, musí vkladanie informácie do siete stáť čas, energiu a peniaze — a navyše sa pre ostatných musí vyprodukovať overiteľný dôkaz, že nejde o prázdne táranie.

Čítanie informácií by bolo ľahké a pomerne lacné, ale vytvorenie jednotlivého záznamu by bolo nákladné a náročné. Zápis by sa riadil jasným protokolom, v ktorom výpočet podľa zvoleného algoritmu striktne určuje, ktorý DID požiadať o overenie predloženej informácie a ako postupovať tak, aby vybraný účastník spracoval informáciu v tvojom mene, zverejnil ju a stal sa jej overovateľom.

> [!note] Algoritmus vs radikalizmus
> Algoritmický výber overovateľov zabezpečuje, že neradikálni vydavatelia informácií si v čase udržia takmer neutrálnu rovnováhu medzi nákladmi na zverejnené informácie a odmenami za overovanie.

![PUBLISHING COSTS TIME, ENERGY, AND MONEY](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Pozrime sa, ako algoritmus vyberá overovateľa.

> [!note] Algoritmus
> Algoritmický výber nedeterministicky volí pre rôzne informácie iného overovateľa (alebo množinu možných overovateľov). Hash (jednosmerná matematická funkcia, ktorá z ľubovoľného vstupu vyrobí jedinečný „odtlačok“ — ako odtlačok prsta dokumentu) kompletného DID dokumentu určuje pozíciu na konzistentnom hash ringu a vyberá kandidátov na overovateľa.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Jednoducho povedané: algoritmus vezme celý tvoj DID dokument, vypočíta z neho odtlačok a ten odtlačok určí tvojho overovateľa.

![HOW THE ALGORITHM SELECTS YOUR VERIFIER](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Pri prvom overovateľovi, ktorého algoritmus vyberie, nemusíš ako vydavateľ uspieť — tvoja reputácia alebo deklarované nastavenia nemusia spĺňať jeho požiadavky. Algoritmicky by si pokračoval v hľadaní ďalšieho vykonaním ďalšej rekurzívnej iterácie, ktorá ti priradí ďalšieho overovateľa. S každým krokom rastie „vzdialenosť“ k cieľovému overovateľovi a spolu s ňou aj sprievodné metadáta, ktoré treba zverejniť. Ako dáta rastú, prirodzene stúpajú náklady (nielen pre počiatočnú veľkosť tvrdenia, ale aj pre metadáta hromadiace sa pri každom zamietnutí). Dôveryhodná informácia prejde oveľa ľahšie ako nezmyselné rozmary. Je na každom, akú vysokú cenu je ochotný niesť a nakoľko mu na zázname záleží — radikalizmus sa zaručene predraží.

![HOW THE VERIFIER ANSWERS](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Nech overovateľ rozhodne v odpovedi na tvoju žiadosť o overenie akokoľvek, lopta je späť na strane vydavateľa: môže prijať overovateľovu ponuku overovacích služieb, zapracovať odpoveď do chronológie a skúsiť to znovu (drahšie), alebo odísť a preglgnúť utopené náklady.

![THE ISSUER'S CHOICE](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Aby si svojej informácii dodal väčšiu váhu a lepšiu šancu na prijatie u overovateľov, mohol by si ako vydavateľ so záujmom o vydávanú informáciu využiť služby **dôveryhodnej autority**. Autorita predloženú informáciu buď zamietne, alebo prijme a vsadí na ňu svoje dobré meno (reputáciu). Autorita si typicky vyžiada dôkazy z reálneho sveta, overí ich a klasifikuje. Výstupom je protokol jej posúdenia daného prípadu v danom čase. Predstav si autoritu ako špecialistu na určitý druh služby v reálnom aj digitálnom svete — napríklad vyšetrovateľa, audítora, poisťovateľa, dodávateľa určitej triedy tovaru (v podstate ktoréhokoľvek ekonomického aktéra na trhu).

![HOW A RECORD IS CREATED IN THE NETWORK](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Kým sa pokúsiš zverejniť informáciu do siete, tá už pravdepodobne bude obsahovať informácie o svojich aktéroch — to sú reputačné signály. Zorientovať sa v tom, ako čítať reputačné signály — čo pre teba znamenajú v rôznych situáciách a aké riziká nesú — nemusí byť triviálne. Každý účastník sa môže na reputačné záznamy pozerať cez svoj DID inak, podľa situácie, ktorú rieši voči protistrane. Je protistrana spoľahlivý platca, alebo si mám pri obchode vypýtať peniaze vopred? Nesie ponúkaný produkt recenzie o skrytom podvode alebo vadách? Snaží sa vykrútiť zo zmluvnej zodpovednosti, keď sa niečo pokazí? Niekedy sa hodí zložitejší pohľad na celkovú konzistentnosť protistrany — závisí to od preferencií toho, kto si prehľad vyžiada. Trh by mohol ponúkať produkty a služby, ktoré zjednodušujú, spracúvajú a sprehľadňujú čítanie reputácie v kontexte danej situácie. Tomuto účelu môžu slúžiť aj rôzne autority a nimi ponúkané služby.

![HOW TO READ REPUTATION](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Príklady
> Typické informácie zaujímavé pre vydavateľov — a cenné pre ostatných — sa týkajú udalostí presahujúcich bežnú medziľudskú komunikáciu v reálnom alebo virtuálnom svete.
>
> Negatívne príklady:
> - dôkaz o trestných činoch (napr. auditovaný dôveryhodným vyšetrovacím orgánom)
> - nepriamy dôkaz (sám o sebe slabý, ale štatisticky kumulatívny) — napr. opakovaná prítomnosť v blízkosti viacerých krádeží v krátkom čase → ešte stále náhoda?
> - porušenie zmluvy
>
> Pozitívne príklady:
> - napravená ujma (dobrovoľne alebo pod tlakom komunity ako trest)
> - prijatie a odpykanie trestu navrhnutého autoritou X
> - autorita X do určitej miery odňala uznanie majetkových práv previnilca
>
> Je na každom, aby si o protistrane pozháňal dostupné informácie a posúdil riziká podľa svojich preferencií.

![WHAT CAN YOU RECORD IN THE NETWORK?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Či sa o tebe v sieti objaví informácia, závisí výlučne od tvojho vlastného správania.
> Do takej siete nikdy nemusíš vstúpiť, a napriek tomu sa v nej informácia o tebe môže objaviť. Závisí to výlučne od tvojich činov a dopadu, ktorý majú na iných.

![THE COMMUNITY CAN OPEN ONE FOR YOU](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

To, čo som práve stručne načrtol, je spôsob, ako by mohla fungovať sociálna sieť inšpirovaná decentralizovanou identitou (DID). Prvotným účelom konceptov DID je posilniť súkromie a slobodu cez princíp prihlásenia sa k pravidlám, ktoré budem dodržiavať a podľa ktorých budem žiť — dáva užívateľom možnosť rozhodnúť, aké informácie zdieľať a za akých podmienok.

Navrhujem DID ďalej prepojiť do komunikačnej siete, kde si ich držitelia vymieňajú spätnú väzbu aj mimo situácií, keď sa niekomu niečo stalo a komunita alebo jednotlivec potrebuje zareagovať. Také preventívne porovnanie pravidiel, ku ktorým sme sa prihlásili — s možnosťou vypočítať ekonomické a iné dôsledky vzájomných odchýlok v očakávaniach o tom, ako by mala druhá strana fungovať — by sa dalo považovať za motiváciu k hľadaniu konsenzu. Namiesto slobody by taký systém zdôrazňoval dobrovoľné rozhodovanie spojené so zodpovednosťou za správanie v reálnom svete.

Jednotlivec systém sám nerozbije — skupina ľudí má väčšiu šancu a skupina ľudí s vyjednaným konsenzom a motiváciami ťahať za jeden povraz v mnohých otázkach má ešte väčšiu šancu odolávať autoritárskym tendenciám. Predpoklad organizácie z prvej kapitoly bude splnený, keď nastanú dve podmienky: reputačná sieť DID pokrýva komunity dostatočne reprezentatívne na to, aby jej používanie prestalo byť exotikou. A zároveň sa tento komunitný segment stane ekonomicky významnou menšinou, ktorá dokáže asertívne vyjednávať so zvyškom spoločnosti.

> [!note] Dobrovoľnosť vs sloboda
> Sloboda — v pozitívnom zmysle — by bola druhotným efektom vyvažovania dvoch faktorov: dobrovoľnosti a tlaku okolia smerom k zodpovednosti.

> [!note] Éra AI a hodnota reputácie
> V ére umelej inteligencie sa automatizuje všetko, čo súvisí s kognitívnym myslením — a môže to zájsť ešte ďalej. Čo potom ostáva v ľudskej činnosti ako konkurenčná výhoda? Odpoveď je ťažká a niečo sa určite nájde, ale jedno môžeme povedať s istotou: rozhodne reputácia. Overiteľná história tvojho správania, tvojich záväzkov a ich plnenia — to je niečo, čo za teba AI nevybuduje.

![AI CANNOT BUILD YOUR REPUTATION — ONLY YOU CAN](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![THE ECONOMICS OF TRUTH](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
