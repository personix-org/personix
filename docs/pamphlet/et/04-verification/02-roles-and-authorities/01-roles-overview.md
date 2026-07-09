---
title: "Rollide ülevaade"
chapter: 3
part: "Kuidas kontrollimine toimib"
lang: en
version: v6
---

# Rollide ülevaade

Mõnda neist rollidest puudutasime juba põgusalt võrku ja selle põhiomadusi käsitlevas peatükis. Nüüd on aeg neid uuesti üksikasjalikumalt vaadelda ja lisada täiendavad, mida vajame võrgu robustsemaks muutmiseks. Iga kontrollimistehing hõlmab mitut rolli — vaatame, kuidas need käituvad.

> [!note] Rollid kontrollimistehingus
> Iga kontrollimine hõlmab kuni kuut eristuvat rolli, mis on kokku võetud alltoodud tabelis. Kõigil neist võib olla oma DID detsentraliseeritud reputatsioonivõrgus.

| Roll | Kirjeldus |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Väljaandja** | Inimene, kes avaldab informatsiooni võrku — väidab, et midagi juhtus (DID loodi, muudeti või lõpetati, väide, antud DID poliitika jne) |
| **Subjekt** | Inimene, kellest informatsioon räägib — väite adressaat |
| **Autoriteet** | Usaldusväärne üksus, mis paneb oma nime mängu väite kvaliteedi peale, uurides seda ja kas vaadates üle esitatud tõendid või kogudes neid aktiivselt |
| **Vaatleja** | Sõltumatu kolmas osapool, kes peab arvestust selle üle, kuidas kontrollija väitega ümber käib — tehes kindlaks, et kontrollija ei jää vait ega kaldu kõrvale oma deklareeritud poliitikast |
| **Kontrollija** | Algoritmiliselt valitud osaleja, kes tehingut töötleb |
| **Delegaat** | Inimene, kes tegutseb teise osaleja nimel |
