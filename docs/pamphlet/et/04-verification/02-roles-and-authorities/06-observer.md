---
title: "Vaatleja"
chapter: 3
part: "Kuidas kontrollimine toimib"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Vaatleja

Vaatleja roll kõrvaldab kontrollija stiimuli reegleid painutada. Olukordades, kus kontrollijale ei meeldi väljaandja või autoriteedi päring, võiks ta lihtsalt vait jääda — mitte vastata ja blokeerida algoritmilise järgnevuse. Vaatleja — või vaatlejate hulk — paneb oma reputatsiooni mängu selle dokumenteerimise peale, kuidas kontrollijalt päriti. Kui kontrollija jääb vait vaatamata deklareeritud poliitikale, mis ütleb teisiti, saab teda protokolli rikkumises süüdi mõista.

![VAATLEJA — PEAB KONTROLLIJA ÜLE ARVESTUST](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Mehhanism: ajatempel ja väljakutsekood

Enne kui saadad väite kontrollijale, suunad selle läbi vaatlejate — inimeste, keda usaldad, või spetsialiseeritud vaatlusteenuse pakkujate, kes võtavad väikest tasu. Iga vaatleja saab sinu esildise, lööb sellele ajatempli, allkirjastab, et nägi selle väljaminemist, ja genereerib väljakutsekoodi — oma allkirja krüptograafilise räsi. Koodid lisatakse sinu päringule. Kontrollija näeb neid, kuid tal pole aimugi, kes vaatlejad on või kas koodid on üldse ehtsad. Vaatlejad tegutsevad seega proksidena väljaandja ja kontrollija vahel, hoides sõltumatut arvestust selle üle, et väide esitati ja mida see sisaldas. Neid võib olla null kuni N.

Kui kontrollija käitub ausalt — võttes vastu või lükates tagasi kooskõlas oma deklareeritud poliitikaga — jäävad koodid läbipaistmatuks. Keegi ei paljastu.

Kuid kui kontrollija jääb vait vaatamata vastutulevale poliitikale või vastab viisil, mis on vastuolus sellega, mille ta avaldas, on sul käes vaatlejate algsed allkirjad. Sa saad need avaldada kui proksitunnistuse, et väide esitati ja et kontrollija ei järginud protokolli. Igaüks saab kontrollida, et allkirjad vastavad väljakutsekoodidele.

## Puänt: sul ei ole vaja ehtsaid vaatlejaid

Ja siin on kõige elegantsem osa: **sul ei ole ehtsaid vaatlejaid üldse vaja.** Sa saad genereerida juhuslikke arve, mis näevad välja täpselt nagu väljakutsekoodid. Kontrollija ei suuda vahet teha — tal tuleb täringut veeretada, kas riskida oma reputatsiooniga. Iga päringu taga, mille ta saab, võib olla lugupeetud vaatleja, kes inkognito jälgib — või võib see olla puhas müra. Kontrollija ei tea. Ja see ebakindlus ongi mehhanism.

Ausa surve ülalhoidmise kulu: peaaegu null (juhuslikud arvud on tasuta). Ebaausa käitumise potentsiaalne kulu kontrollija jaoks: katastroofiline. Ausat käitumist stimuleeritakse ka siis, kui keegi tegelikult ei jälgi.

Süsteem toimib, sest kõik on veidi paranoilised. Ebakindlus on odavam kui jälgimine.

![BLÖFF, MIS HOIAB KONTROLLIJA AUSANA](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Mitu kontrollijat ühes iteratsioonis
> Tugevdav kaasnev reegel kontrollija kättesaadavuse jaoks võib olla algoritmiline laiendus, mis tagastab ühes iteratsioonis mitte ainult ühe, vaid kandideerivate kontrollijate hulga.
