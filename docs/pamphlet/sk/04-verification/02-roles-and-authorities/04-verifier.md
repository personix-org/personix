---
title: "Overovateľ"
chapter: 3
part: "Ako funguje overovanie"
lang: en
version: v6
---

# Overovateľ

Ako overovateľ môže vystupovať ktorýkoľvek DID, buď priamo, alebo cez overovacie práva delegované na tretí DID. Aby som ja — alebo môj delegát — mohol overovať, mal by som byť dosiahnuteľný v sieti (online). Nie každý sa k tomu bude chcieť zaviazať, a preto môže záznam DID uvádzať v poradí priority náhradníkov, ktorí budú funkciu vykonávať v jeho mene, kým je offline.

Každý DID aktívny v sieti verejne deklaruje svoju vlastnú politiku. Cez pravidlá definované v tejto politike posudzuje počas procesu overovania reputáciu protistrany a obsah a formu tvrdenia, ktoré vydavateľ označil na zverejnenie do reputačnej siete. Súčasťou politiky je výpočtový vzorec používaný na výpočet poplatkov za overovacie služby. Keď je to na mieste, tak naprieč štatisticky veľkým počtom tvrdení prúdiacich sieťou čakám, kým ma algoritmus siete potiahne na stranu vydavateľa a priradí ma v danej iterácii na overenie vydávanej informácie. Vydavateľ si vopred vie vypočítať, ako by sa správne konajúci overovateľ zachoval, ale nemôže sa vyhnúť tomu, aby ho (alebo jeho náhradníkov) skutočne kontaktoval; iteráciu s vybraným overovateľom musí vydavateľ vykonať aj vtedy, keď vopred vie, že neprejde.

Ako vieme, že vydavateľ spúšťa algoritmus výberu overovateľa nad správnou množinou kandidátskych DID overovateľov? Spolu so svojou verejne deklarovanou politikou každý DID zverejňuje aj aktuálny zoznam identifikátorov svojej sociálnej siete v rámci reputačnej siete. Ak vydavateľ definuje svoju sociálnu sieť ako sociálnu bublinu, ktorá len prizvukuje a posilňuje jeho vlastné názory, informácia zverejnená cez ňu bude len ťažko širšie prijatá inými komunitami. To, že sa mi za vysokú cenu podarí pretlačiť radikálne tvrdenie do siete, neznamená, že mu pri posudzovaní reputácie protistrany dám nejakú váhu. Niektoré tvrdenia som svojou komunitou tlačený brať do úvahy (tresty a obmedzenia uložené previnilcom); iné sú úplne na mne — sám rozhodujem o ekonomickej hodnote zahrnutia alebo vylúčenia danej informácie.

![THE VERIFIER — CHOSEN BY THE ALGORITHM](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
