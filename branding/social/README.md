---
title: "Bannery pro sociální sítě"
created: 2026-07-22
status: active
tags: [personix, branding, linkedin, youtube, banner]
---

# Bannery pro sociální sítě

| soubor | rozměr | kam |
|---|---|---|
| `linkedin-banner-4200x700.png` | 4200 × 700 (6:1) | firemní stránka LinkedIn |
| `youtube-banner-2560x1440.png` | 2560 × 1440 (16:9) | kanál YouTube |

Generátor LinkedIn verze: `generator-linkedin.py`.

## Proč zrovna tyhle rozměry

**Nahrávat ve 4200 × 700, ne v 1128 × 191.** To druhé je jen velikost, ve které se
banner vykresluje. Na retina displeji má kontejner 804 bodů na šířku, tedy 1608 pixelů —
obrázek o šířce 1128 se natahuje a je rozmazaný. Zdroje to jmenují jako typickou chybu.

Poměr **přesně 6:1**. Kontejner má `background-size: cover`, takže cokoli jiného se ořezává.

## Změřená geometrie LinkedInu (22. 7. 2026, z `getBoundingClientRect()`)

Tentýž obrázek se zobrazuje ve třech pohledech a každý z něj ukazuje něco jiného:

| pohled | kontejner | poměr | co vidí | avatar |
|---|---|---|---|---|
| veřejná stránka | 804 × 134 | 6,00:1 | plnou šířku | 3,0–18,9 % šířky, od 52,2 % výšky |
| admin, postranní karta | 225 × 62 | **3,63:1** | jen **prostředních 60,5 % šířky** | 24,0–43,4 % originálu, od 25,8 % výšky |
| admin, formulář | 735 × 72 | **10,21:1** | jen **prostředních 58 % výšky** | žádný |

⚠️ Ta postranní karta je past. Má úplně jiný poměr než obrázek, takže **uřízne
zhruba pětinu z každé strany**. Text, který na veřejné stránce sedí perfektně,
je v ní useknutý — a není to vinou avatara.

**Bezpečná zóna, viditelná ve všech třech pohledech:** `x 43,5–80,0 %`, `y 21–79 %`.
Uvnitř ní ještě vnitřní okraj o šířce jednoho písmene nadpisu.

## YouTube

Avatar sedí **pod** bannerem a nepřekrývá ho (změřeno na kanálu: banner 1560 × 251).
Platí jen bezpečná zóna **1546 × 423 na střed** — vejde se do ní i mobilní ořez 3,65:1
i televizní 16:9.

## Texty

```
UNCENSORABLE  ·  INCORRUPTIBLE
Decentralized Reputation Network
Take your authority back.
personix.org
```

Písmo Baskerville, pozadí `#16161A` s jemným svislým přechodem, zlatá `#C6A45C`.
