---
title: "Varmentaja"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Varmentaja

Mikä tahansa DID voi toimia varmentajana, joko suoraan tai kolmannelle DID:lle delegoitujen varmennusoikeuksien kautta. Jotta minä — tai valtuutettuni — voisin varmentaa, minun tulisi olla tavoitettavissa verkostossa (online). Kaikki eivät halua sitoutua siihen, minkä vuoksi DID-tietue voi luetella prioriteettijärjestyksessä ne sijaiset, jotka hoitavat tehtävää sen puolesta sen ollessa offline.

Jokainen verkostossa aktiivinen DID julistaa julkisesti oman toimintalinjansa. Tuossa toimintalinjassa määriteltyjen sääntöjen kautta se arvioi varmennusprosessin aikana vastapuolen maineen sekä sen väitteen sisällön ja muodon, jonka julkaisija on merkinnyt julkaistavaksi maineverkostoon. Osa toimintalinjaa on laskentakaava, jota käytetään varmennuspalvelujen maksujen laskemiseen. Kun se on paikallaan, odotan tilastollisesti suuren verkoston läpi virtaavan väitemäärän yli, että verkoston algoritmi vetää minut julkaisijan puolelle ja osoittaa minut tietyssä iteraatiossa varmentamaan julkaistavaa tietoa. Julkaisija voi laskea etukäteen, kuinka oikein käyttäytyvä varmentaja reagoisi, mutta hän ei voi välttää tosiasiallista yhteydenottoa häneen (tai hänen sijaisiinsa); iteraatio valitun varmentajan kanssa on julkaisijan suoritettava silloinkin, kun hän tietää etukäteen, ettei se mene läpi.

Mistä tiedämme, että julkaisija ajaa varmentajanvalinta-algoritmin oikean varmentajaehdokas-DID:iden joukon yli? Julkisesti julistetun toimintalinjansa ohella jokainen DID julkaisee myös nykyisen listan sosiaalisen verkostonsa tunnisteista maineverkoston sisällä. Jos julkaisija määrittelee sosiaalisen verkostonsa sosiaaliseksi kuplaksi, joka vain kaikuu ja vahvistaa omia näkemyksiään, sen kautta julkaistua tietoa tuskin vastaanotetaan laajemmin muissa yhteisöissä. Se, että onnistun korkein kustannuksin työntämään radikaalin väitteen verkostoon, ei tarkoita, että vastapuolen mainetta arvioidessani antaisin sille mitään painoa. Jotkin väitteet yhteisöni painostaa minut ottamaan huomioon (rikkojille määrätyt tuomiot ja rajoitukset); toiset ovat täysin minun päätettävissäni — päätän itse tietyn tiedon sisällyttämisen tai poissulkemisen taloudellisen arvon.

![VARMENTAJA — ALGORITMIN VALITSEMA](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
