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

### Stupnice signálu

- **1** — zaznamenáno, žádná akce
- **2** — stojí za odpověď nebo navázání
- **3** — mění plán, řešit hned

## Týdenní rytmus

Pondělí, zhruba pět minut:

1. Zkontrolovat statistiky na Zenodu
2. Projít alerty na sledované fráze
3. Zkontrolovat schránku personix@personix.org na kvalifikované kontakty
4. Doplnit nové řádky do deníku
5. Cokoli se signálem 3 přesunout do úkolů

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
