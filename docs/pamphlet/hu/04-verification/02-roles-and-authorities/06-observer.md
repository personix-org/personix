---
title: "Observer"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Megfigyelő

A megfigyelő szerep megszünteti az ellenőrző ösztönzését arra, hogy hajlítsa a szabályokat. Olyan helyzetekben, amikor egy ellenőrzőnek nem tetszik a kibocsátó vagy az autoritás kérése, egyszerűen hallgathatna — nem válaszol, és blokkolja az algoritmikus sorrendet. A megfigyelő — vagy megfigyelők egy halmaza — a reputációját teszi arra, hogy dokumentálja, hogyan kérdezték meg az ellenőrzőt. Ha az ellenőrző hallgat annak ellenére, hogy a deklarált elvei mást mondanak, elmarasztalható a protokoll megsértéséért.

![A MEGFIGYELŐ — NYILVÁNTARTÁST VEZET AZ ELLENŐRZŐRŐL](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## A mechanizmus: időbélyeg és kihíváskód

Mielőtt elküldenél egy állítást az ellenőrzőnek, átirányítod megfigyelőkön keresztül — embereken, akikben megbízol, vagy specializált megfigyelőszolgáltatókon, akik kis díjat számolnak fel. Minden megfigyelő megkapja a beadványodat, időbélyeggel látja el, aláírja, hogy látta kimenni, és kihíváskódot generál — a saját aláírásának kriptográfiai hashét. A kódok hozzáfűződnek a kéréshez. Az ellenőrző látja őket, de fogalma sincs, kik a megfigyelők, vagy hogy a kódok egyáltalán valósak-e. A megfigyelők így proxyként működnek a kibocsátó és az ellenőrző között, független nyilvántartást tartva arról, hogy az állítást benyújtották, és hogy mit tartalmazott. Zérótól N-ig terjedhet a számuk.

Amikor az ellenőrző becsületesen viselkedik — a deklarált elveivel összhangban fogad el vagy utasít el —, a kódok átlátszatlanok maradnak. Senki sem lepleződik le.

De ha az ellenőrző hallgat annak ellenére, hogy engedékeny elveket vall, vagy úgy válaszol, ami ellentmond annak, amit közzétett, nálad vannak az eredeti megfigyelői aláírások. Közzéteheted őket proxy-tanúságtételként, hogy az állítást benyújtották, és hogy az ellenőrző nem tartotta be a protokollt. Bárki ellenőrizheti, hogy az aláírások egyeznek-e a kihíváskódokkal.

## A csattanó: nincs szükséged valódi megfigyelőkre

És itt jön a legelegánsabb rész: **egyáltalán nincs szükséged valódi megfigyelőkre.** Generálhatsz véletlen számokat, amelyek pontosan úgy néznek ki, mint a kihíváskódok. Az ellenőrző nem tudja megkülönböztetni őket — kockáztatnia kell, hogy kockára tegye-e a reputációját. Minden kapott kérése mögött állhat egy tekintélyes megfigyelő, aki inkognitóban figyel — vagy lehet tiszta zaj is. Az ellenőrző nem tudja. És ez a bizonytalanság a mechanizmus.

A becsületes nyomás fenntartásának költsége: közel nulla (a véletlen számok ingyenesek). A becstelenség lehetséges költsége az ellenőrző számára: katasztrofális. A becsületes viselkedés akkor is ösztönzött, ha valójában senki sem figyel.

A rendszer azért működik, mert mindenki egy kicsit paranoiás. A bizonytalanság olcsóbb, mint a megfigyelés.

![A BLÖFF, AMELY BECSÜLETESEN TARTJA AZ ELLENŐRZŐT](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Több ellenőrző egyetlen iterációban
> Az ellenőrző elérhetőségének megerősítő kísérőszabálya lehet egy olyan algoritmikus kiterjesztés, amely egyetlen iterációban nem csak egyet, hanem ellenőrzőjelöltek egy halmazát adja vissza.
