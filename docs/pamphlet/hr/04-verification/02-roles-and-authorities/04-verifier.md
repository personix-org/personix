---
title: "Verifikator"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Verifikator

Bilo koji DID može djelovati kao verifikator, izravno ili preko prava provjere delegiranih trećem DID-u. Da bih ja — ili moj delegat — mogao provjeravati, trebao bih biti dostupan na mreži (online). Neće se svatko htjeti na to obvezati, zbog čega DID zapis može navesti, prema prioritetu, zamjene koje će funkciju obavljati u njegovo ime dok je izvan mreže.

Svaki DID aktivan u mreži javno deklarira svoju vlastitu politiku. Kroz pravila definirana u toj politici procjenjuje, tijekom procesa provjere, reputaciju druge strane te sadržaj i oblik tvrdnje koju je izdavatelj označio za objavu u reputacijsku mrežu. Dio politike jest formula izračuna kojom se računaju naknade za usluge provjere. Kad je to na mjestu, tada kroz statistički velik broj tvrdnji koje teku mrežom čekam da me mrežni algoritam izvuče na izdavateljevu stranu i dodijeli mi, u danoj iteraciji, provjeru informacije koja se izdaje. Izdavatelj može unaprijed izračunati kako bi ispravno postupajući verifikator reagirao, ali ne može izbjeći stvarno kontaktiranje s njim (ili njegovim zamjenama); iteraciju s odabranim verifikatorom izdavatelj mora provesti čak i kad unaprijed zna da neće proći.

Kako znamo da izdavatelj pokreće algoritam odabira verifikatora nad ispravnim skupom kandidata za verifikatora — DID-ova? Zajedno sa svojom javno deklariranom politikom, svaki DID objavljuje i aktualni popis identifikatora svoje društvene mreže unutar reputacijske mreže. Ako izdavatelj svoju društvenu mrežu definira kao društveni mjehur koji tek odzvanja i pojačava njegove vlastite stavove, informacije objavljene kroz nju druge će zajednice teško šire primiti. Činjenica da uspijem, uz visok trošak, gurnuti radikalnu tvrdnju u mrežu ne znači da ću joj, kad procjenjujem reputaciju druge strane, dati ikakvu težinu. Neke me tvrdnje moja zajednica gura da uzmem u obzir (kazne i ograničenja izrečena počiniteljima); druge su posve na meni — sam odlučujem o ekonomskoj vrijednosti uključivanja ili isključivanja dane informacije.

![THE VERIFIER — CHOSEN BY THE ALGORITHM](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
