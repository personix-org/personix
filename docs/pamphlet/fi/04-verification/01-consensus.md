---
title: "Konsensus ja varmennusprosessi"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# Konsensus ja varmennusprosessi

Konsensuksen rakentamisessa siitä, mitä sääntöjä yhteiskunnan tulisi keskimäärin ylläpitää ja panna täytäntöön, voi seuraava mekanismi auttaa. DID-osallistujana julistan säännöt, joihin sitoudun ja joiden mukaan elän, ja julkaisen ne. (Ajattele niitä sääntöinä ja ohjesääntöinä, jotka minun näkemykseni mukaan muodostavat ihanteellisen maailmani — maailman, jossa en tunne itseäni rajoitetuksi vaan turvalliseksi.)

Voin arvioida etukäteen, kuinka DID-kontaktini reagoisivat — ja arvioida, kuinka voimakkaasti ja kenen toimesta minua sanktioitaisiin tavanomaisissa sosiaalisissa tai liiketoiminnallisissa vuorovaikutuksissa, mikäli niitä hypoteettisesti tapahtuisi.

Lopullinen arviointi tapahtuu, kun pyydät tietoa toiselta DID:ltä tai pyydät häntä varmentamaan väitteen (tai pyydät auktoriteetilta palvelua ja niin edelleen), jonka haluat julkaista maineverkostoon. Sen pitäisi päättyä samalla tavalla kuin silloin, kun suoritat arvioinnin itse, kuivaharjoituksena, vastapuolen julistettua toimintalinjaa vasten — ja jos ei, jokin on vialla vastapuolen puolella: hän yrittää pelata epärehellistä peliä.

Lopputulos on joko hyväksyntä ja siihen liitetty varmennuksesta annettu hinta (varmentajan tai auktoriteetin palvelujen tapauksessa) tai hylkäys. Sekä sanktiot että bonukset arvioijan toimintalinjasta poikkeamisesta taitetaan annettuun hintaan. Pyytäjä päättää sitten, hyväksyykö hän ehdot vai siirtyykö allokointialgoritmin seuraavalle varmennuskierrokselle — toistaen prosessia, kunnes on tyytyväinen tai kunnes talous tekee jatkamisen turhaksi.

> [!note] Sosiaalinen graafi
> Maineverkosto on ennen kaikkea sosiaalinen verkosto. Lisäät kontakteja — ihmisiä, jotka suostuvat yhteyteen. Heillä on kontakteja, ja niillä kontakteilla on kontakteja. Algoritmi etsii varmentajia konfiguroitavan syvyyden sisällä (esim. kolme tasoa: suorat kontaktisi, heidän kontaktinsa ja yksi taso sen yli). Globaalia lohkoketjua ei tarvita — verkosto muodostaa luonnollisesti yhteisöjä, joilla on limittymiä toisiin yhteisöihin.
>
> Algoritmi on ei-deterministinen: se hashaa väitedokumenttisi, kuvaa hashin paikaksi tunnettujen identiteettien renkaalla tämän piirin sisällä ja valitsee lähimmän varmentajaehdokkaaksi. Et voi ennustaa etkä vaikuttaa siihen, kuka väitteesi varmentaa.

Jokainen varmentajan hylkäys suurentaa dokumenttiasi ja kasvattaa sen käsittelykustannusta — se on ensimmäinen kustannuskanava (dokumentin kasvu). Jokainen uusi varmentaja veloittaa maksun, joka perustuu datamäärään, maineeseesi ja siihen, kuinka kauas väitteesi sisältö poikkeaa hänen julistamastaan varmennusperiaatteesta — se on toinen kustannuskanava (riskilisä). Ja jokainen iteraatio maksaa aikaa ja energiaa — kolmas kustannuskanava.

> [!note] Mitä varmentaja tarkistaa, järjestyksessä
> Kun varmentaja on valittu, hän arvioi väitteen suunnilleen neljässä järjestetyssä vaiheessa — halvimmat suodattimet ensin, kalliit sisältötarkistukset viimeisenä:
>
> 1. **Toimintalinjan portti.** Kuuluuko tämänkaltainen väite ylipäätään siihen, mitä varmentaja julkisesti varmentaa? Jos ei, pyyntö hylätään suoralta kädeltä.
> 2. **Auktoriteetin luottamus.** Onko väitettä tukenut auktoriteetti riittävän luotettu varmentajan oman julistetun toimintalinjan mukaan? Varmentajan luottamuskynnyksen alapuolella oleva auktoriteetti on peruste hylkäykseen väitteen sisällöstä riippumatta.
> 3. **Julkaisijan maine.** Täyttääkö julkaisija ne mainekynnykset, jotka varmentaja on julistanut tämäntyyppiselle väitteelle? Matala maine voi joko nostaa maksua tai laukaista hylkäyksen.
> 4. **Sisältötarkistus.** Vasta kun kolme ensimmäistä porttia menevät läpi, varmentaja arvioi itse väitettä — allekirjoitukset, sisäisen johdonmukaisuuden, muodollisen oikeellisuuden ja sen, kuinka kauas se poikkeaa varmentajan toimintalinjasta. Tästä viimeisestä vaiheesta veloitettu maksu heijastaa todella otettua riskiä.
>
> Varmentaja julkaisee toimintalinjan, joka ohjaa kutakin näistä porteista, joten vaiheet eivät ole hänen harkintansa varassa — häntä sitoo se, minkä hän on jo julistanut. Julkaistusta toimintalinjasta poikkeaminen on itsessään julkaistavissa oleva väite häntä vastaan, ja hän maksaa siitä maineellaan.

Lopputulos: uskottavan ja hyödyllisen väitteen julkaiseminen maksaa lähes tyhjää. Radikaalin väitteen julkaiseminen maksaa enemmän. Valheen julkaisemisesta tulee kohtuuttoman kallista — sinun on iteroitava varmentajasta varmentajaan, ja jokainen sinut hylkäävä lisää kustannuksia. Markkinat hinnoittelevat väitteesi, ja hinta kertoo, missä seisot suhteessa niihin yhteisöihin, joissa liikut.

Ei riitä julistaa noudattavansa sääntöä, kun tosiasiassa ei noudata. Siinä tapauksessa DID:si riskeeraa tekopyhyyden paljastavan negatiivisen tietueen julkaisemisen — mikä tekee sinusta riskin kaikille muille. Lopputuloksen pitäisi olla vähemmän mutta johdonmukaisemmin noudatettuja sääntöjä ja sen lakien ja säädösten viidakon raivaaminen, jossa jopa juristit tuskin osaavat navigoida.

![TEKOPYHYYS ON KALLEIN KÄYTTÄYTYMINEN](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Konsensus vs. vastuullisuus
> Jotta verkosto palvelisi arvokkaana tiedon lähteenä, DID ei saisi olla liian radikaali — muuten muut hylkäävät sen. Sosiaalinen paine etsii tasapainoa, ja yrityksiä horjuttaa sitä todennäköisesti rangaistaan.

![JULISTA SÄÄNTÖSI, MAKSA HINTA](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Äänten määrä ei ole sama asia kuin äänen paino
> Juraj Karpiš sanoo, että ”raha on hyvien tekojen muisti”. Lisäisin, että maine on huonojen tekojen muisti.
>
> Tästä seuraa, että meritokraattisesti se, joka panostaa enemmän eikä omaa huonoa mainetta, ansaitsee suuremman äänen painon yhteisössä. Kahdenvälisten suhteiden linssin läpi katsottuna: kun punnitsen, mihin konsensuspaineisiin mukaudun, suurin paino menee niille suhteille, joista saan suurimman taloudellisen hyödyn. Kymmenen ihmistä, joiden kanssa minulla ei ole aktiivista kauppaa, vaikuttaa minuun paljon vähemmän kuin yksi pysyvä liikekumppani. Tämä paradigma ei rajoitu kaupankäyntiin — se ulottuu sosiaalisiin, poliittisiin ja muihin suhteisiin.
