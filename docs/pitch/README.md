> ⚠️ **!!! TENTO REPOZITÁŘ MUSÍ ZŮSTAT PRIVATE !!!** ⚠️
>
> Obsahuje PII třetích stran (`src/Web/reviewers.json`), interní pitch materiály a strategické dokumenty.
>
> **Před jakýmkoli `git push` na public remote PROVEĎ:**
> 1. `git-filter-repo` audit (odstranit reviewers.json z celé historie, ne jen z HEAD)
> 2. Server-side rotaci všech review tokenů
> 3. Mailmap rewrite ALL-CAPS author emailů
> 4. Anonymizaci / odstranění `docs/pitch/` (investor materiály nepatří do public open-source)
>
> **Public flip = nevratná akce** — jména třetích osob v git history nelze vzít zpět.

---

# Personix — investor pitch deck

Pitch deck pro mainstream české investory. **Není** určen anarcho-kapitalistické komunitě — záměrně mírný akademický tón, žádné krypto-libertariánské signály.

## Soubory

| Soubor | Velikost | Účel |
|---|---|---|
| [`pitch-deck.html`](./pitch-deck.html) | ~40 KB | Slide deck (7 slidů, samostatný HTML — IM Fell English + Palatino, otevři v Brave/Chrome) |
| [`speaker-notes.html`](./speaker-notes.html) | ~50 KB | Mluvený scénář pro každý slide + Q&A appendix |

HTML deck je funkční bez závislostí díky CDN fallback (Google Fonts) — stažený HTML soubor stačí otevřít v browseru.

## Struktura decku (7 slidů)

| # | Slide | Pointa |
|---|---|---|
| **i** | The product — _PERSONIX_ | _„An uncensorable, incorruptible, decentralized reputation network — an evolutionary successor to the state."_ Headline product, žádná historická vata. |
| **ii** | Why now | Eyebrow `WESTPHALIA 1648 · BISMARCK 1871` — dva historické anchory. Tři důvody proč zrovna teď: Bitcoin (2009+), kolaps důvěry v instituce (2020+), AI eats jobs. |
| **iii** | The architecture | Pět protokol-primitiv: DID layer · Claims · Verifiers · Aggregation · **Declared policy** (2×2 grid + full-width row pro 5. primitiv). Matematika drží protokol, sociální incentivy ho udrží poctivý. |
| **iv** | Incorruptibility | Čtyři síly: unpredictable target, reputational leverage (slow up, fast down), public promise, mesh attack-cost asymmetry. „Two walls of the same room." |
| **v** | Roadmap | _„Five phases — four mine, the fifth open."_ Phase 4 = **THE HEART · MAIN GOAL** (široký sienna-tinted box): „A controlled simulation under adversarial pressure. The question we measure: do honest incentives keep the network stable — and free?" Phase 5 (red-clay přerušovaný kruh) = _„Open. State, city, region — whoever takes it and builds the real institution."_ |
| **vi** | The deal | Dvě sekce: **THE AUTHOR** + **THE FOUNDATION** (3 bullets — recurring pledges, donor-elected board s váhou hlasu = trailing 12 months, audits+reports). Coda: _„The only return I offer: a hand in changing the world. (No tokens, no tricks. No monetization path that wouldn't corrupt the protocol.)"_ |
| **vii** | Thank you | _„Here is a tool. It can carry civilization past the age of excuses. Do we have the courage?"_ + contact (Pavel Kudrna · personix@personix.org · personix.org · github.com/personix-org). |

## Brand kit

| Element | Hodnota |
|---|---|
| Paper background | `#f6e7c5` (cream) |
| Title font | IM Fell English (woff2 v `fonts/`, fallback Google Fonts CDN) |
| Body font | Palatino |
| Eyebrow font | mono, tracked 0.3em, all-caps |
| Sienna accent | `#b56a1d` (highlights, italic emphasis, dot 1) |
| Dusty blue | (dot 2) |
| Red-clay | (dot 3, dashed circle for „open" phase) |
| Ink | (default body color, dot 4) |
| Warm ochre | `#a78240` (5. accent, dot 5) |
| Two-rules motif | Krátký hairline pod každým section title |

## Q&A appendix (speaker-notes.html)

Záložní odpovědi na potenciální otázky:

1. **I want to help, but I cannot make a financial pledge right now** — pomoc s knihou, outreach, intros, personix@personix.org
2. **How does this sustain itself long-term — without equity, tokens, or fees on the protocol?** — donations now, paid integration support later (downstream service business, nenarušuje neutralitu)
3. **What exactly do you simulate?** — capture attempts, collusion rings, sybil attacks, signal poisoning, reputation laundering. Test: stays equilibrium-stable & free
4. Další záložní entries pokrývají technický stack (.NET), governance bylaws, a typické dotazy investorů.

## Jak otevřít

```bash
open docs/pitch/pitch-deck.html
open docs/pitch/speaker-notes.html
```

Pitch deck používá custom element `<deck-stage>` — bez JS deck zobrazí všechny slidy under-sebou (scrollable). Pro present mode (one-slide-at-a-time, šipky) je nutné mít `deck-stage.js`.

---

_Deck dokončen 2026-05-20._
