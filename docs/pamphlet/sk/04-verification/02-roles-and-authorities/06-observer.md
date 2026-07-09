---
title: "Pozorovateľ"
chapter: 3
part: "Ako funguje overovanie"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Pozorovateľ

Rola pozorovateľa odstraňuje overovateľovi stimul ohýbať pravidlá. V situáciách, keď sa overovateľovi žiadosť vydavateľa alebo autority nepáči, mohol by jednoducho mlčať — neodpovedať a zablokovať algoritmickú postupnosť. Pozorovateľ — alebo množina pozorovateľov — vsádza svoju reputáciu na zdokumentovanie toho, ako bol overovateľ oslovený. Ak overovateľ napriek deklarovanej politike, ktorá hovorí opak, mlčí, možno ho usvedčiť z porušenia protokolu.

![THE OBSERVER — KEEPS A RECORD OF THE VERIFIER](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Mechanizmus: časová pečiatka a výzvový kód

Predtým, než pošleš tvrdenie overovateľovi, presmeruješ ho cez pozorovateľov — ľudí, ktorým dôveruješ, alebo špecializovaných poskytovateľov pozorovateľských služieb, ktorí si účtujú malý poplatok. Každý pozorovateľ dostane tvoje podanie, opečiatkuje ho časom, podpíše, že videl, ako odchádza, a vygeneruje výzvový kód — kryptografický hash svojho podpisu. Kódy sa pripoja k tvojej žiadosti. Overovateľ ich vidí, ale nemá tušenia, kto sú pozorovatelia, ani či sú kódy vôbec reálne. Pozorovatelia tak pôsobia ako sprostredkovatelia medzi vydavateľom a overovateľom, ktorí držia nezávislý záznam o tom, že tvrdenie bolo podané a čo obsahovalo. Môže ich byť nula až N.

Keď sa overovateľ správa poctivo — prijíma alebo zamieta v súlade so svojou deklarovanou politikou — kódy ostávajú nepriehľadné. Nikto nie je odhalený.

Ale ak overovateľ napriek ústretovej politike mlčí, alebo odpovie spôsobom, ktorý protirečí tomu, čo zverejnil, držíš pôvodné podpisy pozorovateľov. Môžeš ich zverejniť ako sprostredkované svedectvo, že tvrdenie bolo podané a že overovateľ nedodržal protokol. Ktokoľvek si môže overiť, že podpisy sedia s výzvovými kódmi.

## Pointa: nepotrebuješ skutočných pozorovateľov

A tu je tá najelegantnejšia časť: **vôbec nepotrebuješ skutočných pozorovateľov.** Môžeš vygenerovať náhodné čísla, ktoré vyzerajú presne ako výzvové kódy. Overovateľ nerozozná rozdiel — musí hádzať kockou, či riskovať svoju reputáciu. Za každou žiadosťou, ktorú dostane, by mohol byť rešpektovaný pozorovateľ sledujúci inkognito — alebo to môže byť čistý šum. Overovateľ to nevie. A tá neistota je ten mechanizmus.

Náklady na udržanie poctivého tlaku: takmer nulové (náhodné čísla sú zadarmo). Potenciálne náklady nepoctivosti pre overovateľa: katastrofálne. Poctivé správanie je stimulované aj vtedy, keď v skutočnosti nikto nesleduje.

Systém funguje, pretože každý je trochu paranoidný. Neistota je lacnejšia než dohľad.

![THE BLUFF THAT KEEPS THE VERIFIER HONEST](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Viacero overovateľov v jednej iterácii
> Posilňujúcim doplnkovým pravidlom pre dostupnosť overovateľa môže byť algoritmické rozšírenie, ktoré v jednej iterácii vráti množinu kandidátskych overovateľov namiesto jediného.
