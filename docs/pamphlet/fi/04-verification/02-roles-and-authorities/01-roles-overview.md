---
title: "Roolien yleiskatsaus"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Roolien yleiskatsaus

Kosketimme jo lyhyesti joitakin näistä rooleista verkostoa ja sen perusominaisuuksia käsittelevässä luvussa. Nyt on aika tarkastella niitä uudelleen yksityiskohtaisemmin ja lisätä ne lisäroolit, joita tarvitsemme tehdäksemme verkostosta vankemman. Jokaiseen varmennustapahtumaan liittyy useita rooleja — katsotaan, kuinka ne käyttäytyvät.

> [!note] Roolit varmennustapahtumassa
> Jokaiseen varmennukseen liittyy jopa kuusi erillistä roolia, jotka on koottu alla olevaan taulukkoon. Kaikilla niistä voi olla oma DID:nsä hajautetussa maineverkostossa.

| Rooli | Kuvaus |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Julkaisija** | Henkilö, joka julkaisee tietoa verkostoon — väittää, että jotain tapahtui (DID luotiin, muokattiin tai purettiin, väite, tietyn DID:n toimintalinja jne.) |
| **Kohde** | Henkilö, jota tieto koskee — väitteen vastaanottaja |
| **Auktoriteetti** | Luotettu taho, joka panttaa nimensä väitteen laatuun tutkimalla sitä ja joko tarkastelemalla esitettyjä todisteita tai aktiivisesti keräämällä niitä |
| **Tarkkailija** | Riippumaton kolmas osapuoli, joka pitää kirjaa siitä, kuinka varmentaja käsittelee väitteen — varmistaen, ettei varmentaja vaikene eikä poikkea julistamastaan toimintalinjasta |
| **Varmentaja** | Algoritmisesti valittu osallistuja, joka käsittelee tapahtuman |
| **Valtuutettu** | Henkilö, joka toimii toisen osallistujan puolesta |
