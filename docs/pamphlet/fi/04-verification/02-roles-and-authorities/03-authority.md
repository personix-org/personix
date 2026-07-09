---
title: "Auktoriteetti"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Auktoriteetti

Auktoriteetilla on kaksoisrooli: se voi olla **tilintarkastaja** (todistaen todisteiden laadun ennen väitteen julkaisemista) tai **takaaja** (pantaten maineensa väitteen totuudenmukaisuuteen). Kummassakin tapauksessa se vahvistaa julkaisijan väitettä. Nämä kaksi palvelua ovat eroteltavissa — auktoriteetti voi tarjota toisen, toisen tai molemmat kerralla. Työhypoteesi on, että useimmat auktoriteettien tarjoamat palvelut voidaan toimittaa vapaan markkinan pohjalta. Tämä pätee jopa aloilla, joita on vaikea kuvitella yksityistettäviksi, kuten oikeuslaitos, jossa erikoistuneet palvelut — tutkinta, todisteiden arviointi, aina niihin palveluihin asti, joita nykyään tarjoavat keskitetyt armeijat (strateginen suunnittelu, standardoitu koulutus, hankinta ja varastonhallinta jne.) — voidaan tehokkaasti toimittaa markkinatoimijoiden kautta. Tuskin on mitään, mitä uudelleenjärjestelyn jälkeen ei voitaisi tehdä tehokkaammaksi vapaan markkinan kannustimilla.

> [!warning] Auktoriteetti, julkaisija ja tarkkailija eivät saa koskaan olla oman tapauksensa varmentaja.
> Varmentajan algoritminen valinta takaa riippumattomuuden. Kukaan ei voi varmentaa omaa väitettään tai väitettä, jossa hänellä on suora intressi. Tämä on yksi perussäännöistä, joiden ylläpitämiseen koko DID-yhteisöllä on intressi.

Seuraavat grafiikat näyttävät toisiaan täydentäviä näkymiä auktoriteettien kattaman toiminnan laajuudesta (termin ”auktoriteetti” voi lukea vaihdellen ”palveluntarjoajana”).

![AUKTORITEETTI — KUKA PANTTAA NIMENSÄ](../../../Info%20Graphics/v5/v5-08d-role-authority.webp)

![AUKTORITEETIN KAKSI KASVOA](../../../Info%20Graphics/v5/v5-08a-autorita-auditor-garant.webp)

> [!note] Auktoriteetti inkognito-tarkkailijana
> Maineikas auktoriteetti — ajattele notaaria, jonka liiketoiminta riippuu yksinomaan track recordista — voi päätoimintojen (tilintarkastaja / takaaja) rinnalla tarjota kolmannen: inkognito-tarkkailijan roolin varmennuksen aikana. Hän pitää aikaleimattua kirjaa toimitetusta väitteestä niin, ettei varmentaja voi hiljaa pudottaa sitä. Tarkkailijaroolin mekanismi kuvataan tarkemmin Tarkkailija-roolia käsittelevässä osiossa.
