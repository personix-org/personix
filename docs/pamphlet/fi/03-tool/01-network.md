---
title: "Maineeseen perustuva sosiaalinen verkosto"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Maineeseen perustuva sosiaalinen verkosto

Muutoksen aikaansaamiseksi tarvitsemme huolellisesti suunnitellun työkalun. Ensin hahmottelemme sen lyhyesti; myöhemmissä luvuissa tarkastelemme kutakin osaa yksityiskohtaisemmin ja lisäämme lisää. Kuvittele sensuroimaton, globaali, hajautettu sosiaalinen verkosto, jossa voisit turvallisesti luoda ja hallita proxy-identiteettiäsi — niin sanottua hajautettua identiteettiä (DID). DID on digitaalinen identiteetti, jonka luot ja jota hallitset itse, ilman riippuvuutta mistään keskitetystä auktoriteetista. Kukaan ei voi ottaa sitä pois tai väärentää sitä, koska se on kryptografisesti allekirjoitettu yksityisellä avaimellasi (tai avaimillasi, multisigin kautta).

> [!note] Huomio
> Yksi seuraus on se, että tällainen identiteetti voisi vähitellen korvata valtion myöntämät henkilöllisyystodistukset — mutta tästä lisää siirtymää käsittelevässä luvussa.

![IDENTITEETTISI, AVAIMESI, SÄÄNTÖSI](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

Tällaisessa verkostossa voisit identiteettisi kautta ilmoittaa, että joku on aiheuttanut sinulle vahinkoa (ja myöhemmin mahdollisesti, että hän on korjannut sen tai hänet on pakotettu korjaamaan se). Jotta tällä palautteella — joka on suunnattu vahingon aiheuttajalle — olisi arvoa olennaisena lähteenä, tiedon syöttämisen verkostoon on maksettava aikaa, energiaa ja rahaa — ja lisäksi muille on tuotettava todennettava todiste siitä, ettei kyse ole joutavasta jaarittelusta.

Tiedon lukeminen olisi helppoa ja suhteellisen halpaa, mutta yksittäisen tietueen luominen olisi kallista ja vaativaa. Kirjoittaminen noudattaisi selkeää protokollaa, jossa valitun algoritmin mukainen laskenta määrää tiukasti, miltä DID:ltä pyydetään toimitetun tiedon varmennusta ja miten edetään niin, että valittu osallistuja käsittelee tiedon puolestasi, julkaisee sen ja tulee sen varmentajaksi.

> [!note] Algoritmi vs. radikaalius
> Varmentajien algoritminen valinta varmistaa, että ei-radikaalit tiedon julkaisijat säilyttävät ajan myötä lähes neutraalin tasapainon julkaistun tiedon kustannusten ja varmennuksesta saatavien palkkioiden välillä.

![JULKAISEMINEN MAKSAA AIKAA, ENERGIAA JA RAHAA](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Katsotaan, kuinka algoritmi valitsee varmentajan.

> [!note] Algoritmi
> Algoritminen valinta valitsee ei-deterministisesti eri varmentajan (tai joukon mahdollisia varmentajia) eri tietosisällöille. Täydellisen DID-dokumentin hash (yksisuuntainen matemaattinen funktio, joka tuottaa mistä tahansa syötteestä ainutkertaisen ”sormenjäljen” — kuin asiakirjan sormenjälki) määrää paikan konsistentilla hash-renkaalla ja valitsee varmentajaehdokkaat.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Selkokielellä: algoritmi ottaa koko DID-dokumenttisi, laskee siitä sormenjäljen, ja tuo sormenjälki määrää varmentajasi.

![KUINKA ALGORITMI VALITSEE VARMENTAJASI](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Ensimmäisen algoritmin valitseman varmentajan kanssa et julkaisijana välttämättä onnistu — maineesi tai julistamasi asetukset eivät ehkä täytä hänen vaatimuksiaan. Jatkaisit algoritmisesti seuraavan etsimistä suorittamalla uuden rekursiivisen iteraation, joka osoittaa sinulle uuden varmentajan. Joka askeleella ”etäisyys” kohdevarmentajaan kasvaa, ja niin kasvaa myös oheismetadata, joka on julkaistava. Datan kasvaessa kustannukset luonnollisesti nousevat (ei vain väitteen alkuperäisen koon vuoksi, vaan myös jokaisen hylkäyksen myötä kertyvän metadatan vuoksi). Uskottava tieto menee läpi paljon helpommin kuin järjettömät oikut. Kunkin on päätettävä, kuinka korkean hinnan hän on valmis kantamaan ja kuinka paljon tietue hänelle merkitsee — radikaalius menee taatusti kalliiksi.

![KUINKA VARMENTAJA VASTAA](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Riippumatta siitä, mitä varmentaja päättää vastauksena varmennuspyyntöösi, pallo on jälleen julkaisijan kentällä: hän voi hyväksyä varmentajan tarjouksen varmennuspalveluista, taittaa vastauksen aikajanaan ja yrittää uudelleen (kalliimmalla) tai kävellä pois ja niellä uponneet kustannukset.

![JULKAISIJAN VALINTA](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Antaaksesi tiedollesi enemmän painoarvoa ja paremman mahdollisuuden tulla hyväksytyksi varmentajien luona, voisit julkaisijana, jolla on intressi julkaistavan tiedon suhteen, käyttää **luotettavan auktoriteetin** palveluja. Auktoriteetti joko hylkää toimitetun tiedon tai hyväksyy sen ja panttaa siihen hyvän nimensä (maineensa). Auktoriteetti tyypillisesti pyytää tosielämän todisteita, todentaa ne ja luokittelee ne. Tuloksena on protokolla sen arviosta annetusta tapauksesta annettuna aikana. Ajattele auktoriteettia tietyn tyyppisen palvelun asiantuntijana sekä todellisessa että digitaalisessa maailmassa — esimerkiksi tutkijana, tilintarkastajana, vakuuttajana, tietyn tavaraluokan toimittajana (käytännössä minä tahansa markkinoiden taloudellisena toimijana).

![KUINKA TIETUE SYNTYY VERKOSTOON](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Siihen mennessä, kun yrität julkaista tietoa verkostoon, se sisältää todennäköisesti jo tietoa toimijoistaan — nämä ovat mainesignaaleja. Sen navigointi, kuinka mainesignaaleja luetaan — mitä ne merkitsevät sinulle eri tilanteissa ja mitä riskejä ne kantavat — ei välttämättä ole triviaalia. Kukin osallistuja voi katsoa mainetietueita eri tavoin DID:nsä kautta riippuen siitä tilanteesta, jota hän käsittelee vastapuolen suhteen. Onko vastapuoli luotettava maksaja, vai tarvitseeko minun vaatia rahaa etukäteen liiketoimesta? Kantaako tarjottu tuote arvioita piilotetusta petoksesta tai vioista? Yrittääkö hän luikerrella pois sopimusvastuusta, kun jokin menee pieleen? Joskus monimutkaisempi näkymä vastapuolen kokonaisjohdonmukaisuuteen tulee tarpeeseen — se riippuu siitä, kuka yhteenvedon pyytää, ja hänen mieltymyksistään. Markkinat voisivat tarjota tuotteita ja palveluja, jotka yksinkertaistavat, käsittelevät ja selkeyttävät maineen lukemista käsillä olevan tilanteen kontekstissa. Erilaiset auktoriteetit ja niiden tarjoamat palvelut voivat myös palvella tätä tarkoitusta.

![KUINKA MAINETTA LUETAAN](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Esimerkkejä
> Tyypillinen julkaisijoita kiinnostava — ja muille arvokas — tieto koskee tapahtumia, jotka ylittävät tavanomaisen ihmisten välisen viestinnän todellisessa tai virtuaalisessa maailmassa.
>
> Negatiivisia esimerkkejä:
> - todisteet rikollisista teoista (esim. luotettavan tutkintaelimen tarkastamat)
> - epäsuorat todisteet (yksinään heikkoja, mutta tilastollisesti kumuloituvia) — esim. toistuva läsnäolo useiden varkauksien lähellä lyhyessä ajassa → yhä sattumaa?
> - sopimusrikkomus
>
> Positiivisia esimerkkejä:
> - korjattu vahinko (vapaaehtoisesti tai yhteisön painostuksesta rangaistuksena)
> - auktoriteetin X ehdottaman rangaistuksen hyväksyminen ja kärsiminen
> - auktoriteetti X peruutti tietyssä määrin tunnustuksen tekijän omistusoikeuksille
>
> Kunkin on itse kerättävä saatavilla oleva tieto vastapuolesta ja arvioitava riskit mieltymystensä mukaan.

![MITÄ VERKOSTOON VOI KIRJATA?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Se, ilmestyykö sinusta tietoa verkostoon, riippuu yksinomaan omasta käyttäytymisestäsi.
> Sinun ei koskaan tarvitse liittyä tällaiseen verkostoon, ja silti sinusta voi ilmestyä siihen tietoa. Se riippuu yksinomaan teoistasi ja siitä vaikutuksesta, joka niillä on muihin.

![YHTEISÖ VOI AVATA SELLAISEN PUOLESTASI](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Se, mitä juuri hahmottelin lyhyesti, on se, kuinka hajautetusta identiteetistä (DID) inspiroitunut sosiaalinen verkosto voisi toimia. DID-käsitteiden ensisijainen tarkoitus on vahvistaa yksityisyyttä ja vapautta sen periaatteen kautta, että sitoudun sääntöihin, joita noudatan ja joiden mukaan elän — antaen käyttäjille kyvyn päättää, mitä tietoa jakaa ja millä ehdoin.

Ehdotan, että DID:t yhdistetään edelleen viestintäverkostoksi, jossa niiden haltijat vaihtavat palautetta myös niiden tilanteiden ulkopuolella, joissa jollekulle on tapahtunut jotain ja yhteisön tai yksilön on reagoitava. Tällaista niiden sääntöjen ennakoivaa vertailua, joihin olemme sitoutuneet — mahdollisuudella laskea keskinäisten poikkeamien taloudelliset ja muut seuraukset odotuksissa siitä, miten toisen osapuolen tulisi toimia — voitaisiin pitää motivaationa konsensuksen löytämiseen. Vapauden sijaan tällainen järjestelmä korostaisi vapaaehtoista päätöksentekoa yhdistettynä vastuuseen tosielämän käyttäytymisestä.

Yksilö ei voi murtaa järjestelmää yksin — ryhmällä ihmisiä on suurempi mahdollisuus, ja ryhmällä ihmisiä, joilla on neuvoteltu konsensus ja motivaatiot vetää yhtä köyttä monissa asioissa, on vielä suurempi mahdollisuus vastustaa autoritaarisia pyrkimyksiä. Ensimmäisen luvun järjestäytymisedellytys täyttyy, kun kaksi ehtoa toteutuu: DID-maineverkosto kattaa yhteisöt riittävän edustavasti, jotta sen käyttö lakkaa olemasta eksoottista. Ja samalla tästä yhteisösegmentistä tulee taloudellisesti merkittävä vähemmistö, joka voi neuvotella määrätietoisesti muun yhteiskunnan kanssa.

> [!note] Vapaaehtoisuus vs. vapaus
> Vapaus — positiivisessa mielessä — olisi toissijainen vaikutus kahden tekijän tasapainottamisesta: vapaaehtoisuuden ja ympäristön vastuuseen kohdistaman paineen.

> [!note] Tekoälyn aikakausi ja maineen arvo
> Tekoälyn aikakaudella kaikkea kognitiiviseen ajatteluun liittyvää automatisoidaan — ja se voi mennä vielä pidemmälle. Mitä sitten jää inhimilliseen toimintaan kilpailueduksi? Vastaus on vaikea, ja jotain varmasti löytyy, mutta yhden asian voimme sanoa varmuudella: maine ratkaisee. Todennettava historia käyttäytymisestäsi, sitoumuksistasi ja niiden täyttämisestä — se on jotain, jota tekoäly ei rakenna puolestasi.

![TEKOÄLY EI VOI RAKENTAA MAINETTASI — VAIN SINÄ VOIT](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![TOTUUDEN TALOUS](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
