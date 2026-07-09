---
title: "Tarkkailija"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Tarkkailija

Tarkkailijarooli poistaa varmentajan kannustimen taivuttaa sääntöjä. Tilanteissa, joissa varmentaja ei pidä julkaisijan tai auktoriteetin pyynnöstä, hän voisi yksinkertaisesti vaieta — olla vastaamatta ja tukkia algoritmisen sarjan. Tarkkailija — tai tarkkailijoiden joukko — panttaa maineensa siihen, että dokumentoi, kuinka varmentajalta kysyttiin. Jos varmentaja vaikenee vastoin toimintalinjaa, joka sanoo toisin, hänet voidaan tuomita protokollan rikkomisesta.

![TARKKAILIJA — PITÄÄ KIRJAA VARMENTAJASTA](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Mekanismi: aikaleima ja haastekoodi

Ennen kuin lähetät väitteen varmentajalle, reitität sen tarkkailijoiden kautta — ihmisten, joihin luotat, tai erikoistuneiden tarkkailijapalvelujen tarjoajien, jotka veloittavat pienen maksun. Kukin tarkkailija vastaanottaa toimituksesi, aikaleimaa sen, allekirjoittaa, että näki sen lähtevän, ja generoi haastekoodin — kryptografisen hashin allekirjoituksestaan. Koodit liitetään pyyntöösi. Varmentaja näkee ne mutta ei tiedä, keitä tarkkailijat ovat, tai ovatko koodit edes aitoja. Tarkkailijat toimivat siten välittäjinä julkaisijan ja varmentajan välillä pitäen riippumatonta kirjaa siitä, että väite toimitettiin ja mitä se sisälsi. Niitä voi olla nollasta N:ään.

Kun varmentaja käyttäytyy rehellisesti — hyväksyen tai hyläten julistamansa toimintalinjan mukaisesti — koodit pysyvät läpinäkymättöminä. Ketään ei paljasteta.

Mutta jos varmentaja vaikenee vastoin mukautuvaa toimintalinjaa tai vastaa tavalla, joka on ristiriidassa hänen julkaisemansa kanssa, sinulla on hallussasi alkuperäiset tarkkailija-allekirjoitukset. Voit julkaista ne välitodistuksena siitä, että väite toimitettiin ja ettei varmentaja noudattanut protokollaa. Kuka tahansa voi todentaa, että allekirjoitukset täsmäävät haastekoodeihin.

## Iskurepliikki: et tarvitse aitoja tarkkailijoita

Ja tässä on kaikkein elegantein osa: **et tarvitse aitoja tarkkailijoita lainkaan.** Voit generoida satunnaislukuja, jotka näyttävät täsmälleen haastekoodeilta. Varmentaja ei voi erottaa eroa — hänen on heitettävä noppaa siitä, riskeeraako maineensa. Jokaisen saamansa pyynnön takana voisi olla arvostettu tarkkailija katsomassa inkognito — tai se voi olla pelkkää kohinaa. Varmentaja ei tiedä. Ja tuo epävarmuus on mekanismi.

Rehellisen paineen ylläpitämisen kustannus: lähes nolla (satunnaisluvut ovat ilmaisia). Epärehellisyyden mahdollinen kustannus varmentajalle: katastrofaalinen. Rehelliseen käyttäytymiseen kannustetaan silloinkin, kun kukaan ei todella katso.

Järjestelmä toimii, koska jokainen on hieman paranoidi. Epävarmuus on halvempaa kuin valvonta.

![BLUFFI, JOKA PITÄÄ VARMENTAJAN REHELLISENÄ](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Useita varmentajia yhdessä iteraatiossa
> Vahvistava kumppanisääntö varmentajan tavoitettavuudelle voi olla algoritminen laajennus, joka palauttaa yhdessä iteraatiossa joukon varmentajaehdokkaita vain yhden sijaan.
