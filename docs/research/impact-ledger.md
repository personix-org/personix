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

#### Indexace whitepaperu — stav k 1. 8. 2026

Audit všech agregátorů, které pro tenhle typ textu dávají smysl. Zenodo rozešle
záznam samo jen do části z nich, zbytek chce ruční krok.

| Kde | Stav | Poznámka |
|---|---|---|
| DataCite | je | automaticky přes Zenodo |
| OpenAIRE | je | dva záznamy, deduplikace ze dvou zdrojů, ne duplicita |
| OpenAlex | je | práce `W7162246792` |
| ORCID | doplněno ručně | profil byl do té doby úplně prázdný |
| Zenodo komunity | podáno | `dd4ed` a `pe`, čeká na kurátory |
| ScienceOpen | podáno | účet přes ORCID, request přes DOI |
| Semantic Scholar | draft emailu | jejich kontaktní stránka vrací 404, jede se na feedback@semanticscholar.org |
| CORE, BASE, IA Scholar | není | harvestují repozitáře samy, autorský submit nemají |
| Google Scholar | neověřeno | Google z domácí IP hází kontrolu na robota |
| Sci-Hub | nelze a nedává smysl | viz níže |

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
