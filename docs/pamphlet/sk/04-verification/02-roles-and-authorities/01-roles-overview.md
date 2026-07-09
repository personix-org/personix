---
title: "Prehľad rolí"
chapter: 3
part: "Ako funguje overovanie"
lang: en
version: v6
---

# Prehľad rolí

Niektorých z týchto rolí sme sa už krátko dotkli v kapitole o sieti a jej základných vlastnostiach. Teraz je čas pozrieť sa na ne opäť podrobnejšie a doplniť ďalšie, ktoré potrebujeme, aby sme sieť spravili robustnejšou. Každá overovacia transakcia zahŕňa niekoľko rolí — pozrime sa, ako sa správajú.

> [!note] Roly v overovacej transakcii
> Každé overenie zahŕňa až šesť odlišných rolí, zhrnutých v tabuľke nižšie. Všetky môžu mať svoj vlastný DID v decentralizovanej reputačnej sieti.

| Rola | Opis |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Vydavateľ** | Osoba, ktorá zverejňuje informáciu do siete — tvrdí, že sa niečo stalo (DID bol vytvorený, upravený alebo zrušený, tvrdenie, politika daného DID atď.) |
| **Subjekt** | Osoba, ktorej sa informácia týka — adresát tvrdenia |
| **Autorita** | Dôveryhodný subjekt, ktorý vsádza svoje meno na kvalitu tvrdenia tým, že ho vyšetrí a buď preskúma predložené dôkazy, alebo ich aktívne zhromaždí |
| **Pozorovateľ** | Nezávislá tretia strana, ktorá vedie záznam o tom, ako overovateľ s tvrdením naloží — dbá na to, aby overovateľ ani nemlčal, ani sa neodchýlil od deklarovanej politiky |
| **Overovateľ** | Algoritmicky vybraný účastník, ktorý spracuje transakciu |
| **Delegát** | Osoba konajúca v mene iného účastníka |
