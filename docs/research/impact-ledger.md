---
title: Impact ledger — ruční sledování dopadu Personixu
created: 2026-07-24
status: active
tags: [research, marketing, mereni, dopad, altmetric, zenodo]
relevance_to_personix: high
related: [clanek-osnova-palladium, stadni-moralka-a-personix]
review_cadence: týdně, pondělí
---

# Impact ledger

Ruční deník dopadu. Existuje proto, že standardní marketingové nástroje měří
u ideového projektu špatné věci, a ty správné neměří vůbec.

## Proč ne běžný stack

Google Analytics, Meta Pixel a marketingová automatizace jsou pro Personix
**vyloučené**, ne z technických, ale z věcných důvodů. Projekt provozuje
cibulové zrcadlo, drží kanárka pro státní nátlak a staví pseudonymitu jako
designový princip. Posílat návštěvníky do Googlu by byl doložitelný rozpor mezi
tím, co říkáme, a co děláme. První člověk, který si otevře zdrojový kód
stránky, z toho udělá screenshot.

Z nutnosti se dá udělat argument: měřit tak, jak tvrdíme, že se to má dělat,
a napsat o tom veřejně.

## Tři vrstvy měření

### Vrstva 1 — web, bez osobních údajů

- **Nástroj:** Plausible nebo Umami, **self-hostované** na vlastním serveru
- **Vlastnosti:** bez cookies, bez osobních údajů, open-source, data zůstávají u nás
- **Co dává:** návštěvy, zdroje, nejčtenější stránky, stažení
- **UTM parametry** fungují normálně, jen se nikam neodesílají
- **Transparence:** odkaz v zápatí webu na stránku „jak měříme a proč"

Konvence UTM pro každé umístění článku:

```
?utm_source=palladium&utm_medium=article&utm_campaign=herd-morality
```

### Vrstva 2 — akademická, tady máme náskok

Whitepaper má trvalý identifikátor **[10.5281/zenodo.20366216](https://doi.org/10.5281/zenodo.20366216)**,
což je nejlepší měřicí infrastruktura v tomhle prostoru a je zdarma.

| Nástroj | Co měří | Poznámka |
|---|---|---|
| **Zenodo statistiky** | zobrazení, stažení | Přímo u záznamu, nic se nemusí nastavovat |
| **Altmetric Attention Score** | vážený součet zmínek | Tweet = váha 1, novinový článek = 8, **dokument o veřejné politice = 3** |
| **Dimensions** | citace, open-access status | Propojené s Altmetricem |
| **Google Scholar alert** | kdo cituje | Nastavit alert na jméno autora i na název |
| **Semantic Scholar** | citační graf | Doplňkově |

Ta váha 3 u dokumentů o veřejné politice je pro nás nejdůležitější číslo
v celém Altmetricu, protože policy je cílový terén projektu.

#### Indexace whitepaperu — stav k 9. 8. 2026

Audit všech agregátorů, které pro tenhle typ textu dávají smysl. Zenodo rozešle
záznam samo jen do části z nich, zbytek chce ruční krok.

| Kde | Stav | Poznámka |
|---|---|---|
| DataCite | je | automaticky přes Zenodo |
| OpenAIRE | je | dva záznamy, deduplikace ze dvou zdrojů, ne duplicita |
| OpenAlex | je | práce `W7162246792` |
| ORCID | doplněno ručně | profil byl do té doby úplně prázdný |
| Zenodo komunity | částečně | `pe` schválena 4. 8., `dd4ed` stále čeká na kurátory |
| ScienceOpen | podáno | účet přes ORCID, request přes DOI |
| Semantic Scholar | draft emailu | jejich kontaktní stránka vrací 404, jede se na feedback@semanticscholar.org |
| SocArXiv | zamítnuto | `bx3ud` neprošel moderací 5. 8., Crossref DOI odtud nebude |
| CORE, BASE, IA Scholar | není | harvestují repozitáře samy, autorský submit nemají |
| Google Scholar | je, ale pod názvem | Záznam existuje i s abstraktem, zdroj personix.org. Pod slovem Personix nevyskočí, k tomu viz deník 15. 9. |
| Sci-Hub | nelze a nedává smysl | viz níže |

**Systémové řešení: druhý depozit s Crossref DOI.** Mechanika je pořád platná.
Když text dostane identifikátor od Crossrefu, propadne se do Unpaywallu a odtud
si ho Semantic Scholar, CORE i další natáhnou samy. Vznikají dvě DOI pro tentýž
text, což je u preprintů běžné, a vazbu stačí doplnit do Zenodo záznamu jako
související identifikátor.

První pokus přes SocArXiv ale nevyšel. Prefix `10.31235` u Crossrefu
registrovaný je, jenže moderace preprint 5. 8. zamítla s tím, že text nesplňuje
kritéria odborného společenskovědního výzkumu, protože navrhuje nový rámec, aniž
by se opíral o literaturu v oboru.

Ověřeno proti zdroji, doslova vzato to neplatí. Whitepaper má 25 citací
v textu, sekci Related Work a v úvodu vymezení vůči existujícím systémům, a
všech 18 položek seznamu je někde použitých. Skutečná námitka bude oborová.
Text debatuje s kryptografickou a libertariánskou literaturou, kdežto ze
společenskovědní klasiky bere Durkheima, Rawlse, Haidta a Younga jen jako
opěrné body. Pro sociologický repozitář to čte jako rozhovor vedený jinde.

Z toho plyne, že resubmit na SocArXiv by znamenal přepsat text do jiného žánru,
ne doplnit chybějící část. To se nevyplatí, protože Crossref DOI jde získat
jinde beze změny textu.

**Celá platforma OSF je mimo hru, ne jen SocArXiv.** Obecný server OSF
Preprints, prefix `10.31219`, nová podání vůbec nepřijímá, a všech čtrnáct
otevřených oborových serverů pod OSF jede na předběžné moderaci téhož typu,
na které text neprošel. Ověřeno přes `api.osf.io/v2/providers/preprints/`.

Zbylé alternativy, oba prefixy u Crossrefu registrované:

| Server | Prefix | Registrátor | Screening | Riziko |
|---|---|---|---|---|
| SSRN | `10.2139` | Elsevier | Rozsah, formát, integrita. Věcnou správnost výslovně neposuzuje, autory bez afiliace bere | Nízké |
| Preprints.org | `10.20944` | MDPI | Do 24 hodin, kontroluje angličtinu, etiku, pravost autorů a přiznané AI | Střední, podmínky vylučují obsah označený jako provokativní nebo kontroverzní |

První volba je SSRN, protože jako jediný explicitně netvrdí, že hodnotí obsah.

**Nejdůležitější zjištění: DataCite versus Crossref.** Zenodo přiděluje DOI přes
DataCite, ne přes Crossref. Řada agregátorů ale bere open-access obsah přes
Unpaywall, a ten čerpá z Crossrefu. Proto whitepaper nedorazil do Semantic
Scholaru sám a proto ho ScienceOpen nemusí přijmout, ten v podmínkách chce
Crossref DOI, PMC nebo arXiv ID. Pro každý další text platí, že Zenodo samo
o sobě viditelnost v citačních službách nezajistí.

**Sci-Hub je slepá ulička, ne opomenutí.** Nemá žádné rozhraní pro autory.
Obsah získává obcházením paywallů u vydavatelů, typicky přes darované
institucionální přístupy, a ukládá to, co si někdo vyžádá a co je jinak placené.
Otevřený text pod licencí CC BY nemá co obcházet, takže tam nemá jak ani proč
být. Od prosince 2020 navíc kvůli soudnímu sporu v Indii pozastavil přidávání
nového obsahu a jeho databáze zůstává hlavně na článcích do roku 2021. Pro nás
je to bez užitku i bez rizika, prostě mimo hru.

### Vrstva 3 — to, co žádný nástroj neumí

Tady leží skutečný dopad. Vede se ručně v tabulce níže.

## Marnivé metriky vs. signál

| Marnivá metrika | Co sledovat místo toho |
|---|---|
| Počet návštěv | **Kdo** napsal email. Deset zpráv od správných lidí je víc než 50 000 zobrazení. |
| Počet stažení PDF | Citace ve zdroji, který není náš |
| Sdílení na sítích | **Adopce jazyka** — použije někdo cizí naše pojmy? |
| Kladné ohlasy | **Kvalita odporu** — kdo argumentuje proti a jak tvrdě |

Poslední řádek stojí za vysvětlení. Podle Stennerové je odpor signál, že věc
byla vnímána jako reálná, ne ignorována. Kvalifikovaný kritik je lepší zpráva
než tisíc lajků.

## Sledované fráze

Na tyhle výrazy nastavit alerty (Google Alerts, Scholar alert, ruční hledání
jednou týdně). Jejich výskyt mimo naše zdroje je nejtvrdší důkaz dopadu.

- `Personix`
- `Reputation Social Network` / `RSN`
- `Expensive Radicalism` / `drahý radikalismus`
- `Reputable Authority`
- `uncorruptible` ve spojení s reputačním systémem
- `10.5281/zenodo.20366216`

## Deník událostí

Jeden řádek na událost. Doplňovat průběžně, revidovat v pondělí.

| Datum | Typ | Popis | Zdroj / odkaz | Signál (1–3) | Poznámka |
|---|---|---|---|---|---|
| 2026-07-24 | založení | Ledger vznikl | — | — | Výchozí stav |
| 2026-07-24 | publikace | Pitch odeslán redakci Palladia | editors@palladiummag.com | 1 | Čeká odpověď. Kontrola naplánována na 2026-08-07. Bez odpovědi jeden follow-up, pak jinam. |
| 2026-07-25 | kontakt | Palladium má zájem, chce draft 2000–3000 slov do 8. 8. | editors@palladiummag.com | 3 | ⚠️ Redakce NEPUBLIKUJE AI text ani AI editaci. Chce autorskou bio (1–2 věty). Kontrolní task na 7. 8. zrušen. |
| 2026-08-01 | indexace | Audit agregátorů, whitepaper byl jen v DataCite, OpenAIRE a OpenAlex | — | 2 | Zenodo hlásilo 40 zobrazení a 16 stažení. Podrobný stav v tabulce výše. |
| 2026-08-01 | indexace | Whitepaper doplněn do ORCID profilu jako preprint, veřejný, vytažený jako Featured | [ORCID 0009-0004-9179-8261](https://orcid.org/0009-0004-9179-8261) | 2 | Profil neměl do té doby ani jednu práci. ORCID feeduje další služby, takže to byla největší mezera. |
| 2026-08-01 | indexace | Podány žádosti do dvou Zenodo komunit | `dd4ed`, `pe` | 1 | Čeká na kurátory. Komunity jsou malé, přínos spíš marginální. |
| 2026-08-01 | indexace | Založen účet na ScienceOpen přes ORCID, podán request přes DOI | scienceopen.com | 1 | Jejich server během registrace spadl na chybu 524, registrace přesto prošla. Výsledek requestu přijde mailem. |
| 2026-08-01 | indexace | Připraven draft pro Semantic Scholar | feedback@semanticscholar.org | 1 | Čeká na odeslání. Vysvětluje, proč je DataCite DOI minulo přes Unpaywall. |
| 2026-08-04 | indexace | Zenodo komunita `pe` (political economy) žádost schválila, záznam je v jejím výpisu | [zenodo.org/communities/pe](https://zenodo.org/communities/pe/) | 1 | Komunita má 38 záznamů, přínos je spíš symbolický. Žádost do `dd4ed` pořád leží u kurátorů. |
| 2026-08-04 | indexace | Whitepaper podán na SocArXiv jako preprint | [osf.io/preprints/socarxiv/bx3ud_v1](https://osf.io/preprints/socarxiv/bx3ud_v1) | 2 | Moderace 4–5 pracovních dnů. Po schválení Crossref DOI, což otevírá cestu do Unpaywallu. Abstrakt bez věty o projektu, střet zájmů přiznán. |
| 2026-08-05 | indexace | SocArXiv preprint `bx3ud` neprošel moderací | [socopen.org/moderation-policy](https://socopen.org/moderation-policy/) | 2 | Moderace napsala, že text nesplňuje kritéria odborného společenskovědního výzkumu, protože navrhuje nový rámec bez opory v literatuře oboru. Doslova to neplatí, whitepaper má 25 citací a sekci Related Work. Námitka je oborová, text debatuje s kryptografií a libertariánskou teorií, ne se sociologií. Zjištěno až 9. 8. z digest mailu, protože API u zamítnutých hlásí totéž co u čekajících. Crossref DOI tudy nevede, alternativy v tabulce výše. |
| 2026-08-08 | publikace | Draft článku „Irresponsibility Is Free of Charge" (~2900 slov) odeslán redakci Palladia | Google Doc (komentování) + .md příloha | 3 | Reaguje na výzvu editora z 25.7., odesláno v termínu. Text psal Pavel (redakce zakázala AI text i editaci). Čeká na editorial review. Finální text zařazen v [[palladium-clanek-final-en]]. |
| 2026-09-15 | indexace | Diagnóza po 49 dnech marného denního hlídání Scholaru | — | 3 | Scholar paper zná a má ho i s abstraktem, indexace nikdy nebyla problém. Pod slovem Personix nevyskočí proto, že slovo bylo v dokumentu jen jednou, a to v afiliaci na titulní straně. Tu Scholar parsuje jako metadata o autorovi, ne jako tělo textu, a pdfkeywords z metadat souboru do fulltextu nebere vůbec. Oprava z 28. 7. tedy mířila do dvou míst, která se do fulltextu nepromítají. |
| 2026-09-15 | indexace | Whitepaper přebuildován na Draft v3, jméno projektu v abstraktu a závěru | `docs(whitepaper)` v repu personix | 2 | Osm výskytů místo jednoho, z toho dva v abstraktu, který Scholar zobrazuje i indexuje. Obsah návrhu beze změny, otimestampovaná v1 nedotčena. Čeká se na recrawl. |
| 2026-09-15 | indexace | Rešerše ochranné známky PERSONIX v rejstřících | USPTO TSDR, TMview | 1 | V EU stojí jediná živá známka, Sodexo pro stravovací služby, překryv nulový. V USA Fiserv pro ražbu platebních karet, což je zápis z roku 1997, kdy třída 42 byla zbytková, a michiganská firma pro platformu ke komunikaci s pacienty. Jediná citlivá zóna je reputační skóre ve zdravotnictví na americkém trhu. Evropské třídy 9 a 42 jsou pro jméno volné. |

### Legenda typů

| Typ | Význam |
|---|---|
| `publikace` | Náš text vyšel někde |
| `citace` | Někdo cituje whitepaper nebo pamflet |
| `jazyk` | Cizí zdroj použil náš pojem |
| `kontakt` | Někdo relevantní napsal |
| `odpor` | Kvalifikovaná kritika |
| `policy` | Zmínka v dokumentu o veřejné politice — nejvyšší hodnota |
| `média` | Novinový nebo magazínový článek |
| `indexace` | Záznam přibyl do agregátoru nebo katalogu, případně tam byla podána žádost |

### Stupnice signálu

- **1** — zaznamenáno, žádná akce
- **2** — stojí za odpověď nebo navázání
- **3** — mění plán, řešit hned

## Týdenní rytmus

Pondělí, zhruba pět minut:

1. Zkontrolovat statistiky na Zenodu
2. Projít alerty na sledované fráze
3. Zkontrolovat schránku personix@personix.org na kvalifikované kontakty
4. Zkontrolovat, jestli se pohnuly podané žádosti o zařazení (Zenodo komunity,
   ScienceOpen, Semantic Scholar) a doplnit stav do tabulky indexace
5. Doplnit nové řádky do deníku
6. Cokoli se signálem 3 přesunout do úkolů

## Cílový funnel

Nejde o obchodní trychtýř. Odpovídá tomu, co naměřil Fromm — nezajímá nás 75 %
procházejících, zajímá nás konverze do těch 15 %, kteří jsou ochotni něco
udělat. Podrobněji v [[stadni-moralka-a-personix]].

| Fáze | Co znamená | Jak poznat |
|---|---|---|
| Dosah | Text si někdo přečetl | Statistiky, marnivé |
| Porozumění | Někdo to správně převyprávěl | Citace, shrnutí jinde |
| **Adopce jazyka** | Někdo používá naše pojmy jako svoje | Alerty na fráze |
| **Účast** | Někdo přispěl, napsal, oponoval kvalifikovaně | Deník, typ `kontakt` |

Třetí a čtvrtá fáze jsou jediné, na kterých záleží.
