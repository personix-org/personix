---
title: "Verifier"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Ellenőrző

Bármely DID eljárhat ellenőrzőként, akár közvetlenül, akár egy harmadik DID-re delegált ellenőrzési jogokon keresztül. Ahhoz, hogy én — vagy a megbízottam — ellenőrizni tudjak, elérhetőnek kell lennem a hálózaton (online). Nem mindenki akar erre kötelezettséget vállalni, ezért egy DID-bejegyzés prioritási sorrendben felsorolhatja azokat a helyetteseket, akik a funkciót a nevében ellátják, amíg offline van.

Minden, a hálózatban aktív DID nyilvánosan deklarálja a saját elveit. Az azokban az elvekben meghatározott szabályok révén ítéli meg az ellenőrzési folyamat során az ellenfél reputációját, valamint annak az állításnak a tartalmát és formáját, amelyet a kibocsátó a reputációs hálózatba való közzétételre jelölt. Az elvek részét képezi az a számítási képlet, amellyel az ellenőrzési szolgáltatásokért járó díjakat számolják. Ha ez megvan, akkor a hálózaton átáramló, statisztikailag nagyszámú állítás közül várom, hogy a hálózat algoritmusa a kibocsátó oldalán engem húzzon, és egy adott iterációban engem rendeljen a kibocsátott információ ellenőrzésére. A kibocsátó előre kiszámíthatja, hogyan reagálna egy helyesen viselkedő ellenőrző, de nem kerülheti el, hogy ténylegesen felvegye vele (vagy a helyetteseivel) a kapcsolatot; a kiválasztott ellenőrzővel folytatott iterációt a kibocsátónak akkor is végre kell hajtania, ha előre tudja, hogy nem fog átmenni.

Honnan tudjuk, hogy a kibocsátó az ellenőrző-kiválasztási algoritmust a helyes ellenőrzőjelölt-DID-halmazon futtatja? A nyilvánosan deklarált elveivel együtt minden DID közzéteszi a reputációs hálózaton belüli közösségi hálózata azonosítóinak aktuális listáját is. Ha egy kibocsátó a közösségi hálózatát olyan társadalmi buborékként határozza meg, amely csupán visszhangozza és megerősíti a saját nézeteit, akkor a rajta keresztül közzétett információt más közösségek aligha fogadják majd szélesebb körben. Az a tény, hogy nagy költséggel sikerül egy radikális állítást a hálózatba nyomnom, nem jelenti azt, hogy az ellenfél reputációjának megítélésekor bármilyen súlyt adok neki. Bizonyos állításokat a közösségem nyom rám, hogy figyelembe vegyem (elkövetőkre kiszabott büntetések és korlátozások); mások teljes mértékben rajtam múlnak — magam döntöm el egy adott információdarab beszámításának vagy kizárásának gazdasági értékét.

![AZ ELLENŐRZŐ — AKIT AZ ALGORITMUS VÁLASZT](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
