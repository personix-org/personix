---
title: "Kontrollija"
chapter: 3
part: "Kuidas kontrollimine toimib"
lang: en
version: v6
---

# Kontrollija

Iga DID saab tegutseda kontrollijana, kas otse või kolmandale DID-le delegeeritud kontrollimisõiguste kaudu. Selleks et mina — või minu delegaat — saaksin kontrollida, peaksin olema võrgus kättesaadav (online). Mitte kõik ei taha selleks kohustuda, mistõttu DID-kirje saab loetleda tähtsuse järjekorras asendajad, kes täidavad seda funktsiooni tema nimel, kui ta on võrgust väljas.

Iga võrgus aktiivne DID deklareerib avalikult oma poliitika. Selles poliitikas määratletud reeglite kaudu hindab ta kontrollimisprotsessi ajal vastaspoole reputatsiooni ning väljaandja poolt reputatsioonivõrku avaldamiseks märgitud väite sisu ja vormi. Osa poliitikast on arvutusvalem, mida kasutatakse kontrollimisteenuste tasude arvutamiseks. Kui see on paigas, siis üle statistiliselt suure hulga võrgus liikuvate väidete ootan, et võrgu algoritm tõmbaks mind väljaandja poolele ja määraks mind antud iteratsioonis väljastatavat informatsiooni kontrollima. Väljaandja saab ette arvutada, kuidas õigesti käituv kontrollija reageeriks, kuid ei saa vältida temaga (või tema asendajatega) tegelikku ühenduse võtmist; iteratsiooni valitud kontrollijaga peab väljaandja läbi viima ka siis, kui ta teab ette, et see ei lähe läbi.

Kuidas me teame, et väljaandja jooksutab kontrollija valiku algoritmi õige kandideerivate kontrollija-DID-de hulga üle? Koos oma avalikult deklareeritud poliitikaga avaldab iga DID ka oma reputatsioonivõrgusisese suhtlusvõrgu identifikaatorite hetkenimekirja. Kui väljaandja määratleb oma suhtlusvõrgu kui sotsiaalse mulli, mis üksnes kajastab ja tugevdab tema enda vaateid, ei võta teised kogukonnad selle kaudu avaldatud informatsiooni vaevalt laiemalt vastu. See, et mul õnnestub kõrge kuluga suruda radikaalne väide võrku, ei tähenda, et vastaspoole reputatsiooni hinnates annaksin sellele mingit kaalu. Mõne väitega surub mu kogukond mind arvestama (toimepanijatele määratud karistused ja piirangud); teised on täielikult minu otsustada — ma otsustan ise antud informatsioonitüki kaasamise või väljajätmise majandusliku väärtuse.

![KONTROLLIJA — VALITUD ALGORITMI POOLT](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
