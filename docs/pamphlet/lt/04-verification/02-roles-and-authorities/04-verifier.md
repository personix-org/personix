---
title: "Verifier"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Tikrintojas

Bet kuri DID gali veikti kaip tikrintojas, tiesiogiai arba per patikros teises, deleguotas trečiajai DID. Kad aš — ar mano įgaliotinis — galėtume tikrinti, turėčiau būti pasiekiamas tinkle (prisijungęs). Ne kiekvienas norės tam įsipareigoti, todėl DID įraše prioriteto tvarka gali būti išvardyti pavaduojantieji, kurie atliks funkciją jos vardu, kol ji atsijungusi.

Kiekviena tinkle aktyvi DID viešai deklaruoja savo pačios politiką. Per toje politikoje apibrėžtas taisykles ji patikros proceso metu vertina kitos šalies reputaciją bei teiginio, kurį išdavėjas pažymėjo skelbimui į reputacijos tinklą, turinį ir formą. Politikos dalis yra skaičiavimo formulė, naudojama mokesčiams už patikros paslaugas apskaičiuoti. Kai tai vietoje, tuomet per statistiškai didelį per tinklą tekančių teiginių skaičių laukiu, kol tinklo algoritmas ištrauks mane išdavėjo pusėje ir priskirs mane duotojoje iteracijoje patikrinti išleidžiamą informaciją. Išdavėjas gali iš anksto apskaičiuoti, kaip reaguotų teisingai besielgiantis tikrintojas, bet negali išvengti realaus susisiekimo su juo (ar jo pavaduojančiaisiais); iteraciją su parinktu tikrintoju išdavėjas turi atlikti net tada, kai iš anksto žino, kad ji nepraeis.

Iš kur žinome, kad išdavėjas paleidžia tikrintojų atrankos algoritmą per teisingą kandidatų tikrintojų DID aibę? Kartu su savo viešai deklaruota politika kiekviena DID taip pat paskelbia esamą savo socialinio tinklo identifikatorių sąrašą reputacijos tinkle. Jei išdavėjas apibrėžia savo socialinį tinklą kaip socialinį burbulą, kuris tik atkartoja ir sustiprina jo paties pažiūras, per jį paskelbta informacija vargu ar bus plačiau priimta kitų bendruomenių. Tai, kad man pavyksta dideliais kaštais įstumti radikalų teiginį į tinklą, nereiškia, kad, vertindamas kitos šalies reputaciją, suteiksiu jam kokį nors svorį. Kai kuriuos teiginius mane spaudžia atsižvelgti mano bendruomenė (nusikaltėliams paskirti nuosprendžiai ir apribojimai); kiti visiškai priklauso nuo manęs — pats sprendžiu duotosios informacijos įtraukimo ar neįtraukimo ekonominę vertę.

![TIKRINTOJAS — PARINKTAS ALGORITMO](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
