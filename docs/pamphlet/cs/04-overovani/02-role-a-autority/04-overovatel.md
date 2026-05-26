---
title: "Ověřovatel"
chapter: 3
part: "Jak funguje ověřování"
lang: cs
version: v6
---

# Ověřovatel

Každá DID může být ověřovatelem, a to napřímo nebo skrze delegovaná práva na třetí DID. Na to abych já nebo můj zástupce mohl být ověřovatelem, měl bych být v síti dostupný (online). Ne každému se bude chtít tuto podmínku splnit, proto je v definici jeho záznamu definována prioritní řada jeho zástupců, kteří danou funkci vykonávají za něj v době, kdy je offline.

Každá DID vystupující v síti má veřejně deklarovanou svoji politiku, skrze jejíchž definovaná pravidla bude v ověřovacím procesu nahlížet na reputaci protistrany a obsah a formu tvrzení označeného vydavatelem za určený k publikování do reputační sítě. Součástí politik jsou i kalkulační formule na výpočet poplatků za služby ověřování. Když mám toto zajištěno, pak v rámci statisticky velkého počtu tvrzení směřujících do sítě čekám, až mě algoritmus sítě vylosuje na straně vydavatele a určí k tomu, aby v jednotlivé iteraci provedl ověření jím vydávané informace. Vydavatel si může dopředu u sebe spočítat, jak se ověřovatel korektně zachová, avšak nemůže se vyhnout jeho kontaktování (nebo jeho zástupců) a danou iteraci musí vydavatel s vybraným ověřovatelem absolvovat, i když dopředu ví, že to nedopadne.

Jak víme, že vydavatel pouští algoritmus výběru ověřovatele nad správnou množinou DID potenciálních ověřovatelů? Každá DID spolu s deklarovanou veřejnou politikou publikuje i aktuální seznam identifikátorů své sociální sítě v rámci reputační sítě. Bude-li si sociální síť vydavatele pro sebe definovat jako sociální bublinu, která konvenuje a posiluje jen jeho názory, těžko publikované informace skrze ni budou šířeji přijímány mimo ni jinými komunitami. To že se mi podaří za draho radikální informaci v síti publikovat, neimplikuje, že při vyhodnocování reputace protistrany k ní budu přihlížet. K některým jsem tlačen komunitou, abych k nim přihlížel (vynesené tresty a omezení nad provinilci) a jiné jsou čistě na mě — ekonomický přínos zahrnutí/nezahrnutí dané informace si stanovuji sám.

![OVĚŘOVATEL — VYBRANÝ ALGORITMEM](../../../Info%20Graphics/v5-cz/v5-08e-role-verifier.webp)
