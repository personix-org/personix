# Šablona pro NWO Whitepaper (Tier 1)

Analýza stěžejních technických whitepaperů a doporučená šablona pro psaní whitepaperu projektu New World Order.

---

## Část 1: Analýza referenčních dokumentů

### 1.1 Bitcoin Whitepaper (Satoshi Nakamoto, 2008)

**Základní údaje:**
- Název: "Bitcoin: A Peer-to-Peer Electronic Cash System"
- Rozsah: 9 stran, 12 sekcí + abstrakt
- Citace: 8 referencí (extrémně málo pro akademický paper)
- Publikace: mimo tradiční akademické kanály (metzdowd.com mailing list)

**Struktura sekcí:**
1. Introduction
2. Transactions
3. Timestamp Server
4. Proof-of-Work
5. Network
6. Incentive
7. Reclaiming Disk Space
8. Simplified Payment Verification
9. Combining and Splitting Value
10. Privacy
11. Calculations
12. Conclusion

**Styl psaní:**
- Formální akademický tón, třetí osoba a pasivní konstrukce ("We propose...", "We define...")
- Používá "we" jako autorský plurál, nikoliv osobní hlas
- Stručný, věcný, bez zbytečných slov -- každá věta nese informaci
- Minimální sebeodkazování, žádné marketingové fráze
- Překvapivě málo žargonu -- srozumitelný i nespecialistům

**Abstrakt:** Jeden odstavec (~150 slov). Definuje problém (důvěra ve třetí strany), navrhuje řešení (peer-to-peer systém), popisuje mechanismus (proof-of-work řetěz). Žádné buzzwordy.

**Definice problému:** Sekce 1 (Introduction) -- stručně, cca 2 odstavce. Identifikuje konkrétní slabinu (nutnost důvěry ve finanční instituce) a proč je to problém.

**Technický model:** Sekce 2-9 -- každá sekce řeší jednu komponentu systému. Postupuje od základních primitiv (transakce) přes infrastrukturu (síť, PoW) k pokročilým vlastnostem (privacy, SPV).

**Bezpečnostní analýza:** Sekce 11 (Calculations) -- formální matematická analýza pravděpodobnosti útoku, Poissonovo rozdělení, numerické výpočty. Jediná sekce s intenzivní matematikou.

**Matematika/formální notace:** Umírněná. Matematika se objevuje hlavně v sekci 11 (výpočet pravděpodobnosti úspěšného útoku). Jinak se spoléhá na jasné verbální popisy a hashové řetězce.

**Diagramy:** Minimální, ale vysoce efektivní. Obsahuje ~3 schémata (řetěz bloků, transakce, Merkle strom). Jednoduché čárové diagramy bez barev.

**Citační styl:** Číslované reference [1]-[8] na konci dokumentu. Odkazuje na Hashcash, b-money, kryptografické časové razítko -- ukazuje genealogii myšlenky.

**Klíčové poučení pro NWO:**
- Extrémní stručnost je přednost, ne slabina
- Každá sekce řeší přesně jednu věc
- Problém definuj v jednom odstavci, řešení v jedné větě
- Matematiku používej jen tam, kde je nezbytná pro důvěryhodnost
- Diagramy jednoduché, ale přesné

---

### 1.2 Decentralized Society: Finding Web3's Soul (Weyl, Ohlhaver, Buterin, 2022)

**Základní údaje:**
- Název: "Decentralized Society: Finding Web3's Soul"
- Rozsah: ~37 stran
- Citace: Rozsáhlý seznam (60+ referencí)
- Publikace: SSRN preprint, Microsoft Research

**Struktura sekcí (rekonstruovaná z analýz a shrnutí):**
1. Úvod -- problém Web3 hyperfinancializace
2. Soulbound Tokens (SBTs) -- definice konceptu
3. Community Recovery -- obnova peněženek přes sociální graf
4. Sybil-Resistant Governance -- odolnost vůči falešným identitám
5. Decentralization -- mechanismy skutečné decentralizace
6. Plural Property Rights -- rozložitelná vlastnická práva
7. Programmable Plural Privacy -- soukromí přes ZKP a MPC
8. Challenges and Risks -- výzvy a rizika
9. Conclusion -- budoucnost DeSoc

**Styl psaní:**
- Akademicko-vizionářský hybrid: formální struktura, ale s ambicióznějšími proklamacemi
- Používá "we" konzistentně, ale místy přechází do opisných narativů
- Bohatší jazyk než Bitcoin whitepaper -- pracuje se sociálními koncepty, ne jen technickými
- Definuje novou terminologii (Souls, SBTs, DeSoc) a důsledně ji používá
- Obsahuje jak technické popisy, tak společenskovědní argumentaci

**Abstrakt:** Delší než u BTC (~300 slov). Kontextualizuje problém (Web3 je příliš financializovaný), představuje SBTs jako řešení a vyjmenovává klíčové aplikace.

**Definice problému:** Rozsáhlá, zabírá celý úvod (~3 strany). Argumentuje, že Web3 postrádá primitiva pro sociální vztahy a důvěru.

**Technický model:** Progresivní budování -- každá sekce staví na předchozí. Od definice SBT přes konkrétní aplikace (recovery, governance) k abstraktnějším konceptům (property rights, privacy).

**Bezpečnostní analýza:** Integrovaná do sekcí (zejm. sybil resistance) + samostatná sekce Challenges and Risks. Méně formální než BTC, více kvalitativní.

**Matematika/formální notace:** Minimální explicitní matematika. Odkazuje na quadratic voting/funding formule, ale neuvádí je v plné formální notaci. Spoléhá na konceptuální popisy.

**Diagramy:** Minimum. Paper je primárně textový, koncepční -- nepotřebuje architektonické diagramy.

**Citační styl:** Akademický autor-rok styl. Rozsáhlé reference zahrnující ekonomii, politickou filosofii, informatiku a sociologii.

**Klíčové poučení pro NWO:**
- Interdisciplinární paper může být delší (30-40 stran) a stále fungovat
- Nová terminologie musí být definována brzy a používána konzistentně
- Společenskovědní argumentace legitimizuje technický návrh
- Aplikace (use cases) lze řadit od konkrétních po abstraktní
- Sekce risks/challenges přidává důvěryhodnost

---

### 1.3 Ceramic Network Specification

**Základní údaje:**
- Typ: Technická specifikace protokolu (ne whitepaper)
- Formát: GitHub Markdown (SPECIFICATION.md + CIP systém)
- Rozsah: Hlavní specifikace ~20-30 stran, CIPs stovky stran dohromady

**Struktura (Legacy Specification):**
1. Protocol Overview -- co je Ceramic
2. Streams -- append-only log commitů
3. Commits (Genesis, Signed, Anchor)
4. Stream Identifiers (StreamID)
5. Conflict Resolution
6. Document Types (3IDs, Account-links, Tiles)
7. Anchoring -- blockchain anchoring
8. Networking -- libp2p, syncing

**CIP systém (Ceramic Improvement Proposals):**
- Kategorie: Core, Networking, Interface, RFC
- Stavy: Draft -> Review -> Final -> Superseded/Withdrawn
- Inspirováno EIP (Ethereum Improvement Proposals) a BIP (Bitcoin Improvement Proposals)

**Styl psaní:**
- Striktně technický, specifikační jazyk
- Používá normativní klíčová slova RFC 2119 (MUST, SHOULD, MAY)
- Třetí osoba, pasivní konstrukce ("A stream is defined as...", "The genesis commit MUST contain...")
- Žádné narativy, žádné příběhy, žádné motivace -- čistě "co a jak"
- Extrémně strukturovaný s definicemi pojmů na začátku

**Matematika/formální notace:** CID hashe, IPLD datové struktury, JSON schémata. Formální, ale ne matematická -- spíše datově-strukturální.

**Diagramy:** Architektonické diagramy, sekvenční diagramy, datové flow. Technicky přesné.

**Klíčové poučení pro NWO:**
- Specifikace != whitepaper. NWO potřebuje obojí, ale v jiných dokumentech
- CIP/BIP systém je vynikající model pro budoucí governance technických změn
- Normativní jazyk (MUST/SHOULD/MAY) je vhodný pro technické sekce whitepaperu
- Specifikace je referenční dokument, whitepaper je přesvědčovací dokument

---

### 1.4 W3C DID Core Specification v1.0

**Základní údaje:**
- Název: "Decentralized Identifiers (DIDs) v1.0"
- Typ: W3C Recommendation (formální webový standard)
- Rozsah: Velmi obsáhlý (~100+ stran v HTML)
- Publikace: W3C, červenec 2022

**Struktura hlavních sekcí:**
1. Introduction
2. Terminology
3. Conformance
4. Architecture Overview (DID, DID Subject, DID Document, DID Method)
5. DID Syntax
6. Core Properties (verification methods, services, atd.)
   - 5.1 id
   - 5.2 controller
   - 5.3 Verification Methods
   - 5.4 Verification Relationships
   - 5.5 Services
   - 5.6 (další properties)
7. Core Representations (JSON, JSON-LD, CBOR)
8. Methods (DID Method Requirements)
9. Resolution (DID Resolution, DID URL Dereferencing)
10. Security Considerations
11. Privacy Considerations
12. Accessibility Considerations

**Styl psaní:**
- Formální specifikační jazyk, nejpřísnější ze všech analyzovaných dokumentů
- RFC 2119 normativní terminologie (MUST, MUST NOT, SHALL, SHOULD, MAY)
- Striktně třetí osoba, pasivní konstrukce
- Odlišuje normativní a informativní sekce (klíčový princip W3C specifikací)
- Každý pojem formálně definován v sekci Terminology

**Definice problému:** Minimální -- specifikace předpokládá, že čtenář ví proč DID potřebuje. Krátký úvod kontextualizuje.

**Technický model:** Hierarchický, od abstraktní architektury přes syntax k datovému modelu a operacím. Extrémně systematický.

**Bezpečnostní analýza:** Samostatné sekce Security Considerations a Privacy Considerations (~10+ stran dohromady). Strukturovaný seznam hrozeb s mitigacemi.

**Matematika/formální notace:** ABNF gramatika pro DID syntax. JSON schémata. Žádná matematika v tradičním smyslu.

**Diagramy:** Architektonické přehledy, vztahové diagramy mezi DID, DID Document, DID Subject, DID Method.

**Citační styl:** W3C styl -- normativní a informativní reference odděleny. Používá URL reference.

**Klíčové poučení pro NWO:**
- Oddělení normativních a informativních částí je silný vzor
- Security/Privacy Considerations jako samostatné sekce jsou standard
- Terminologie musí být definována formálně na jednom místě
- DID Core je reference pro technické sekce NWO whitepaperu o identitě

---

## Část 2: Srovnávací matice

| Aspekt | BTC Whitepaper | DeSoc Paper | Ceramic Spec | W3C DID Core |
|---|---|---|---|---|
| **Rozsah** | 9 stran | ~37 stran | ~25 stran + CIPs | ~100+ stran |
| **Účel** | Představit systém | Představit vizi + systém | Definovat protokol | Definovat standard |
| **Tón** | Formálně stručný | Akademicko-vizionářský | Technicky striktní | Formálně normativní |
| **Osoba** | 1. os. pl. (we) | 1. os. pl. (we) | 3. osoba pasiv | 3. osoba pasiv |
| **Abstrakt** | 150 slov | ~300 slov | Žádný | Krátký |
| **Problém** | 2 odstavce | 3 strany | Žádný | Minimální |
| **Matematika** | Umírněná (1 sekce) | Minimální | Žádná | ABNF gramatika |
| **Diagramy** | 3 jednoduché | Minimum | Architektonické | Vztahové |
| **Reference** | 8 | 60+ | Inline odkazy | W3C normativní |
| **Terminologie** | Implicitní | Definuje nové pojmy | Formální slovník | Formální sekce |
| **Security** | Matematická analýza | Kvalitativní sekce | Minimální | Rozsáhlé sekce |

---

## Část 3: Doporučená šablona pro NWO Whitepaper

### 3.1 Poziční určení dokumentu

NWO whitepaper je **hybridem mezi Bitcoin whitepaperem a DeSoc paperem**:
- Jako BTC: představuje konkrétní technický systém s jasnými mechanismy
- Jako DeSoc: operuje na průsečíku technologie a společenských věd
- Na rozdíl od Ceramic/W3C: není specifikace -- detailní technické specifikace budou v samostatných dokumentech

**Cílový rozsah: 25-35 stran** (bez příloh a referencí)

**Cílové publikum:**
- Primární: technicky gramotní lidé se zájmem o decentralizaci, kryptografii, politickou filosofii
- Sekundární: akademici (politologie, ekonomie, informatika)
- Terciární: aktivní občané bez technického zázemí (pro ně slouží pamflet)

---

### 3.2 Navrhovaná struktura sekcí

```
Název: [pracovní] "Decentralized Reputation Network:
        A Framework for Voluntary Societal Organization"

0. Abstract                                    (~300 slov, 0.5 strany)
1. Introduction                                (~2 strany)
   1.1 The Problem of Centralized Trust
   1.2 Why Existing Solutions Fall Short
   1.3 Our Contribution
2. Design Principles                           (~2 strany)
   2.1 Continuity and Evolution (not Revolution)
   2.2 Voluntariness and Responsibility
   2.3 Diversity and Cultural Neutrality
   2.4 Resilience and Censorship Resistance
   2.5 Consensus and Enforcement
3. System Overview                             (~2 strany)
   3.1 Reputation Social Network
   3.2 Architectural Components
   3.3 Participant Roles
4. Decentralized Identity Model                (~4 strany)
   4.1 DID with Special Properties
   4.2 Four Roles of a DID (Holder, Executor, Authority, Verifier)
   4.3 Claim Lifecycle
   4.4 Relationship to W3C DID Core
5. Information Verification and Propagation    (~4 strany)
   5.1 Cost of Information Entry
   5.2 Algorithmic Verifier Selection
   5.3 Non-deterministic Onion Routing
   5.4 Expensive Radicalism Principle
6. Reputation and Risk Assessment              (~3 strany)
   6.1 Reputation Accumulation Model
   6.2 Reputable Authorities
   6.3 Individual Risk Evaluation
   6.4 Market for Reputation Services
7. Consensus and Dispute Resolution            (~3 strany)
   7.1 Decentralized Justice Model
   7.2 Satisfaction vs. Truth-seeking
   7.3 Punishment Calibration Mechanism
   7.4 Appeal and Correction
8. Economic Model                              (~3 strany)
   8.1 Incentive Structure
   8.2 Cost Dynamics (Writing vs. Reading)
   8.3 Parallel Fiscal System
   8.4 Transition Economics
9. Migration Path                              (~3 strany)
   9.1 Coexistence with Current Systems
   9.2 Institutional Onboarding
   9.3 Phases of Adoption
   9.4 Pressure Mechanisms (Monetary Policy Leverage)
10. Security Analysis                          (~3 strany)
    10.1 Threat Model
    10.2 Sybil Attack Resistance
    10.3 Collusion and Cartel Formation
    10.4 State-level Adversary
    10.5 Privacy vs. Accountability Tradeoff
11. Privacy Considerations                     (~2 strany)
    11.1 Pseudonymity Architecture
    11.2 Information Asymmetry by Design
    11.3 Right to Be Forgotten vs. Immutability
12. Related Work                               (~2 strany)
    12.1 Decentralized Identity (W3C DID, Ceramic, ION)
    12.2 Reputation Systems (Soulbound Tokens, EigenTrust)
    12.3 Decentralized Governance (DAOs, Quadratic Voting)
    12.4 Anarcho-capitalist and Minarchist Theory
13. Discussion and Limitations                 (~1.5 strany)
    13.1 Known Limitations
    13.2 Open Questions
    13.3 What This Paper Does Not Claim
14. Conclusion                                 (~1 strana)
15. References                                 (~2 strany)

Přílohy (volitelné, mimo hlavní počet stran):
A. Formální definice algoritmů
B. Matematický model reputačního výpočtu
C. Slovník pojmů (Glossary)
```

---

### 3.3 Pokyny ke stylu (Style Guide)

#### Tón a hlas

**Základní tón: Formálně sebevědomý, ale intelektuálně pokorný.**

- Používej **1. osobu plurálu** ("We propose...", "We define...") -- stejně jako BTC a DeSoc
- **Žádný marketingový jazyk.** Srovnej:
  - Špatně: "Our revolutionary platform will transform the world"
  - Správně: "We propose a mechanism that reduces reliance on centralized trust"
- **Žádné emotivní apely.** Srovnej:
  - Špatně: "The corrupt state steals your money through inflation"
  - Správně: "Sustained inflation represents an implicit tax on holders of the currency, reducing individual purchasing power without explicit consent"
- **Přiznávej limity.** BTC whitepaper říká "We need a way..." -- přiznává problém. DeSoc říká "This raises challenges..." -- přiznává nejistotu.
- **Buď konkrétní.** Místo "many people are unhappy" piš "citizens lack a mechanism to withdraw delegated authority between election cycles"

#### Jazyk dokumentu

**Whitepaper bude v angličtině.** Důvody:
- Cílí na globální publikum
- Akademické reference jsou anglické
- Technická terminologie je anglická
- Český pamflet slouží jako národní verze

#### Citační formát

**Číslované reference [1]-[N]** (styl BTC whitepaperu, nikoliv autor-rok).

Důvody:
- Kratší inline odkazy = plynulejší čtení
- Technická komunita je na tento styl zvyklá
- BTC, Ethereum a většina crypto whitepaperů tento styl používá

Příklad:
```
Previous approaches to decentralized identity [3, 7] focus primarily
on privacy preservation, while our model extends the DID framework [12]
to serve as a foundation for reputation-based social organization.
```

**Doporučený minimální počet referencí: 25-40.**

Klíčové reference musí zahrnovat:
- BTC whitepaper (Nakamoto 2008)
- DeSoc paper (Weyl, Ohlhaver, Buterin 2022)
- W3C DID Core v1.0
- Ceramic Network specification
- EigenTrust (Kamvar, Schlosser, Garcia-Molina 2003)
- Quadratic Voting/Funding (Buterin, Hitzig, Weyl 2019)
- Anarcho-kapitalistická teorie (Rothbard, Hoppe)
- Teorie her a mechanismů (relevantní foundational papers)

#### Terminologie

**Definuj vlastní pojmy v sekci 3 (System Overview) a používej je konzistentně.**

Příklad klíčových pojmů k formální definici:
- **Reputation Social Network (RSN)** -- celý systém
- **Claim** -- jednotka informace v síti (tvrzení o události)
- **Authority** -- DID s ověřovacími pravomocemi
- **Verifier** -- algoritmicky vybraný ověřovatel claimu
- **Reputation Score** -- agregovaná metrika důvěryhodnosti DID
- **Expensive Radicalism** -- princip rostoucích nákladů radikálních tvrzení

**Pravidlo:** Jednou definovaný pojem piš vždy stejně (velké písmeno na začátku). Nepoužívej synonyma -- "Claim" je vždy "Claim", nikdy "statement" nebo "assertion" v technickém kontextu.

---

### 3.4 Pokyny pro matematiku a formální notace

**Přístup: Minimální, ale přesný** (vzor: BTC whitepaper)

Matematiku používej POUZE v těchto sekcích:
1. **Sekce 5.3** -- formální definice algoritmického výběru ověřovatele (onion address funkce)
2. **Sekce 6.1** -- model akumulace reputace (agregační funkce)
3. **Sekce 8** -- ekonomický model (nákladové funkce, rovnováha)
4. **Sekce 10** -- bezpečnostní analýza (pravděpodobnostní model útoku)

Všude jinde preferuj **jasný slovní popis** nad formální notací. Pokud musíš použít vzorec, doprovoď ho vysvětlujícím odstavcem.

Příklad vzoru z BTC whitepaperu:
```
The probability that an attacker catches up from z blocks behind
can be approximated as:

    P = 1 - sum_{k=0}^{z} (lambda^k * e^{-lambda}) / k! * (1 - (q/p)^{z-k})

where p is the probability of an honest node finding the next block,
q is the probability the attacker finds the next block, and
lambda = z * (q/p).
```

---

### 3.5 Pokyny pro diagramy a obrázky

**Přístup: Málo, ale vysoce informativních** (vzor: BTC whitepaper)

Doporučený počet: **5-8 diagramů** v celém dokumentu.

| Sekce | Typ diagramu | Popis |
|---|---|---|
| 3.2 | Architektonický přehled | Celkový systém -- DID, síť, claim flow |
| 4.2 | Vztahový diagram | 4 role DID a jejich interakce |
| 5.2-5.3 | Sekvenční diagram | Životní cyklus claimu od podání po ověření |
| 5.4 | Graf/křivka | Náklady vs. radikalismus (exponenciální růst) |
| 6.1 | Datový flow | Jak se reputace akumuluje a propaguje |
| 9.3 | Fázový diagram | Přechod od současného systému k novému |
| 10.1 | Threat model diagram | Hlavní vektory útoku a mitigace |

**Styl diagramů:**
- Černobílé nebo monochromatické (jako BTC whitepaper)
- Jednoduché, bez stínů a gradientů
- Každý diagram musí být srozumitelný i bez okolního textu
- Pod každým diagramem krátký popisek (Figure 1: ...)
- Formát: SVG preferovaný (vektorový, škálovatelný)

---

### 3.6 Co zahrnout vs. vynechat

#### ZAHRNOUT v whitepaperu:

- Jasnou definici problému (proč centralizovaná důvěra selhává)
- Popis mechanismu (jak systém funguje)
- Ekonomické incentivy (proč se lidé budou účastnit)
- Bezpečnostní model (jak systém odolává útokům)
- Migrační cestu (jak přejít od současného stavu)
- Omezení a otevřené otázky (intelektuální poctivost)
- Vztah k existující práci (DID, SBTs, DAOs)

#### VYNECHAT z whitepaperu (přesunout jinam):

- Emocionální příběhy a osobní motivaci autora -> pamflet
- Detailní technickou specifikaci DID -> samostatný spec dokument
- Implementační detaily (programovací jazyky, databáze) -> technická dokumentace
- Roadmap s daty a milníky -> projektový plán
- Informace o týmu a poradcích -> webové stránky
- Tokenomics / token sale detaily -> pokud relevantní, samostatný dokument
- Právní analýzu jurisdikcí -> právní posudek
- Příklady použití v narativní formě (živnostník vs. dlužník) -> pamflet / blog posty

---

### 3.7 Rozdíl mezi NWO whitepaperem a pamfletem

| Aspekt | Whitepaper | Pamflet |
|---|---|---|
| **Jazyk** | Angličtina | Čeština (+ anglický překlad) |
| **Tón** | Formální akademický | Osobní, provokativní |
| **Publikum** | Odborníci, vývojáři, akademici | Běžní občané |
| **Účel** | Definovat systém | Přesvědčit a motivovat |
| **Emoce** | Minimální | Záměrné (hněv, naděje) |
| **Příklady** | Abstraktní, formální | Konkrétní, životní |
| **Délka** | 25-35 stran | 10-15 stran |
| **Citace** | Akademické reference | Žádné nebo minimální |

---

### 3.8 Kontrolní seznam před publikací

- [ ] Abstrakt je srozumitelný i bez čtení zbytku dokumentu
- [ ] Každý nový pojem je formálně definován před prvním použitím
- [ ] Žádná sekce nepřesahuje 4 strany
- [ ] Všechny diagramy mají popisky a jsou odkazovány v textu
- [ ] Bezpečnostní analýza pokrývá minimálně 5 vektorů útoku
- [ ] Sekce Limitations přiznává minimálně 3 významná omezení
- [ ] Related Work nezesměšňuje konkurenční přístupy
- [ ] Závěr neslibuje víc, než co dokument prokázal
- [ ] Všechny matematické vzorce jsou doprovázeny slovním vysvětlením
- [ ] Reference pokrývají minimálně 25 zdrojů z různých disciplín
- [ ] Dokument prošel review od minimálně 2 nezávislých čtenářů
- [ ] Anglický jazyk prošel nativním korektorem

---

## Část 4: Doporučený pracovní postup psaní

### Fáze 1: Kostra (1 týden)
Napsat jednoodstavcové shrnutí každé sekce. Celý dokument na 3-4 stranách.

### Fáze 2: Technické jádro (2-3 týdny)
Rozpracovat sekce 4-8 (DID model, verifikace, reputace, konsensus, ekonomika). Toto je srdce dokumentu.

### Fáze 3: Kontext a analýza (1-2 týdny)
Dopsat sekce 1-3 (úvod, principy, přehled), 10-11 (security, privacy), 12 (related work).

### Fáze 4: Leštění (1-2 týdny)
Napsat abstrakt (vždy nakonec). Dopsat conclusion. Sjednotit terminologii. Přidat diagramy. Zkontrolovat reference.

### Fáze 5: Review (2-4 týdny)
Minimálně 2 kola review od různých typů čtenářů:
- Technický reviewer (kryptograf / distributed systems)
- Doménový reviewer (politolog / ekonom)
- Jazykový korektor (native English speaker)

---

## Zdroje použité pro tuto analýzu

- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) -- Satoshi Nakamoto, 2008
- [Decentralized Society: Finding Web3's Soul](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763) -- Weyl, Ohlhaver, Buterin, 2022
- [Ceramic Network Legacy Specification](https://github.com/ceramicnetwork/.github/blob/main/LEGACY_SPECIFICATION.md)
- [Ceramic Improvement Proposals](https://cips.ceramic.network/CIPs/cip-1)
- [W3C DID Core v1.0](https://www.w3.org/TR/did-1.0/)
- [The Bitcoin White Paper References](https://medium.com/@nelsonmrosario/the-bitcoin-white-paper-references-857f001f4878) -- Nelson M. Rosario
- [Reading the DeSoc Paper Thoroughly](https://projeteam.medium.com/reading-the-desoc-paper-thoroughly-8f9bab9b8ce9) -- Seungchul Seo
- [Bitcoin Whitepaper Explained](https://www.bitpanda.com/academy/en/lessons/the-bitcoin-whitepaper-simply-explained) -- Bitpanda Academy
- [Bitcoin's White Paper: A 9-Page Revolution](https://www.ccn.com/education/crypto/bitcoin-white-paper-9-page-revolution/) -- CCN
- [Satoshi Nakamoto's Bitcoin Whitepaper: A Walk-through](https://www.freecodecamp.org/news/satoshi-nakamotos-bitcoin-whitepaper-a-walk-through-3e9e1dee71ce/) -- freeCodeCamp
