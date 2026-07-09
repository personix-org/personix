---
title: "Sanasto"
part: "Appendix"
lang: en
version: v6
---

# Sanasto

| Termi | Suomi | Merkitys |
|------|-------|---------|
| **Authority** | Auktoriteetti | Luotettu taho (henkilö, organisaatio), joka todentaa tietoa ja panttaa maineensa siihen. Voi olla erikoistunut (tutkinta, oikeus, tekniikka). |
| **Claim** | Väite | Yleisesti: mikä tahansa todennettava lausunto. Tässä: maineverkostoon julkaistu tietue — väittämä tapahtumasta, ominaisuudesta tai suhteesta, joka on kryptografisesti allekirjoitettu ja todennettu. Esim. ”olen kunnan X asukas” tai ”tämä henkilö rikkoi sopimusta”. |
| **Compartmentalization** | Lokerointi | Yleisesti: tiedon erottaminen eristettyihin yksiköihin niin, ettei yhden yksikön paljastuminen vaaranna muita. Tiedustelupalveluista tunnettu periaate. Tässä: rinnakkaiset DID-identiteetit diktatuureissa — yhden paljastuminen ei paljasta muita. |
| **Consistent Hash Ring** | Hash-rengas | Algoritminen mekanismi varmentajien valintaan — paikka renkaalla määräytyy DID-dokumentin hashista sosiaalisen graafin sisällä. Takaa ei-deterministisen mutta silti todennettavan valinnan. |
| **DID** | DID (hajautettu identiteetti) | Digitaalinen identiteetti, jonka luot ja jota hallitset itse, ilman keskitettyä auktoriteettia. Kryptografisesti allekirjoitettu yksityisellä avaimellasi — kukaan ei voi peruuttaa sitä eikä väärentää sitä. |
| **DID Document** | DID-dokumentti | Julkisesti saatavilla oleva datatiedosto, joka kuvaa DID-identiteettisi — sisältää julkiset avaimet, verkko-osoitteet ja metadataa. Käytetään identiteettisi todentamiseen verkostossa. |
| **Due Diligence** | Due diligence | Yleisesti: vastapuolen perusteellinen todentaminen ennen liiketoiminta- tai oikeussuhteeseen ryhtymistä — hänen historiansa, taloutensa, maineensa ja riskiensä tarkistaminen. Tässä: maineverkostossa se tapahtuu nopeammin ja automaattisemmin todennettujen tietueiden saatavuuden ansiosta. |
| **Economic Neutrality Principle** | Taloudellisen neutraaliuden periaate | Rehellinen käyttäytyminen verkostossa on taloudellisesti lähellä nollaa — julkaisukustannukset palautuvat varmennuspalkkioina. Epärehellinen käyttäytyminen on nettotappio. |
| **Emergent** | Emergentti | Yksinkertaisempien osien vuorovaikutuksista spontaanisti syntyvä, ilman että kukaan sitä suunnittelee tai ohjaa. Lintuparvi lentää muodostelmassa ilman suunnitelmaa — muodostelma emergoituu kunkin yksilön noudattamista yksinkertaisista säännöistä. |
| **Emergent Social Contract** | Emergentti yhteiskuntasopimus | Käyttäytymissäännöt, jotka syntyvät ei ylhäältä (laki) vaan alhaalta — toistuvista vuorovaikutuksista ja konsensuksesta yhteisön sisällä. |
| **ESR** | Sähköinen menorekisteri | Ehdotettu järjestelmä julkisten menojen läpinäkyvään jäljittämiseen — jokainen valtion toteutunut meno täsmätään suunniteltuun maksuun. Inspiroitunut tšekkiläisestä EET:stä, mutta käännetty valtiota vastaan. |
| **Hash** | Hash (tiiviste) | Yleisesti: yksisuuntainen matemaattinen funktio, joka tuottaa mistä tahansa syötteestä ainutkertaisen kiinteänmittaisen ”sormenjäljen” — kuin asiakirjan sormenjälki. Sama syöte tuottaa aina saman tuloksen, mutta syötettä ei voi johtaa tuloksesta. Tässä: käytetään paikan määrittämiseen hash-renkaalla ja dokumentin eheyden todentamiseen. |
| **Just-in-Time Funding** | Just-in-time-rahoitus | Läpinäkyvyyteen ehdollistettu valtion rahoitus — raha virtaa vain, kun valtio hyväksyy ESR:n ja täsmää menonsa. Vipu yhteistyöhön pakottamiseen. |
| **Meritocracy** | Meritokratia | Yleisesti: järjestelmä, jossa asema määräytyy todellisten ansioiden ja todistetun kyvyn, ei muodollisten titteleiden, suhteiden tai perityn etuoikeuden mukaan. Tässä: maineverkosto suosii luonnollisesti niitä, jotka todistettavasti panostavat yhteisöön — heidän äänellään on enemmän painoa track recordin, ei viran vuoksi. |
| **Onion Gateway** | Onion gateway | DID-identiteetin verkko-osoite onion-verkossa. Erillinen DID-dokumentista — sitä voidaan muuttaa menettämättä identiteettiä (kuten IP-osoitteen vaihtaminen verkkotunnuksen takana). |
| **Onion Routing** | Onion routing (Tor) | Viestintäprotokolla, joka takaa verkoston sensuroimattomuuden. Viestit salataan kerroksittain — kukin solmu kuorii yhden kerroksen mutta ei tunne koko reittiä. |
| **Oracle Problem** | Oraakkeliongelma | Yleisesti: kuinka varmistetaan, että digitaaliseen järjestelmään syötettävä data vastaa uskollisesti sitä, mitä fyysisessä maailmassa todella tapahtui. Termi on peräisin lohkoketjujen alueelta. Tässä: käsitellään auktoriteettien kautta, jotka panevat maineensa peliin takuuna siitä, että digitaalinen tietue vastaa fyysistä todellisuutta. |
| **Phenomenological** | Fenomenologinen | Yleisesti: lähestymistapa, joka tutkii ilmiöitä sellaisina kuin ne ilmenevät välittömässä kokemuksessa, havainnoimalla mitä niistä seuraa, ilman ennalta annettuja teorioita. Tässä: vapaus, yhteiskuntasopimus ja käyttäytymisnormit ovat havaittuja ilmiöitä — seurauksia tuhansista mikrovuorovaikutuksista ihmisten välillä, ei ylhäältä määriteltyjä periaatteita. |
| **Policy** | Toimintalinja (policy) | Yleisesti: joukko sääntöjä tai periaatteita, jotka ohjaavat käyttäytymistä tietyssä kontekstissa. Tässä: jokainen DID-verkoston osallistuja julistaa toimintalinjansa — kuinka hän reagoi muiden tiettyyn käyttäytymiseen, mitä sääntöjä hän noudattaa ja mitä rangaistuksia hän pitää suhteellisina. Toimintalinjojen aggregaatti muodostaa emergentin yhteiskuntasopimuksen. |
| **Proxy** | Proxy | Yleisesti: sijainen tai välittäjä — järjestelmä tai taho, joka toimii toisen puolesta. Käytetään tässä kahdessa kontekstissa: (1) ESR proxyna, joka täsmää julkiset menot suunniteltuihin maksuihin; (2) tarkkailijat proxyna julkaisijan ja varmentajan välillä tarkkailijatempussa. |
| **Publisher** | Julkaisija | Verkoston osallistuja, joka luo ja julkaisee tietueen (väite vääryydestä, korjauksesta ja niin edelleen). Kantaa julkaisemisen kustannuksen. |
| **Reputation-Based Social Network (RSN)** | Maineeseen perustuva sosiaalinen verkosto | Hajautettu sosiaalinen verkosto, jossa osallistujat vaihtavat palautetta tosielämän käyttäytymisestä. Tietueiden luominen on kallista, lukeminen halpaa. |
| **Reputation Signal** | Mainesignaali | Yksittäinen tietue verkostossa — positiivinen (vahingon korjaus, velvoitteen täyttäminen) tai negatiivinen (vääryys, sopimusrikkomus). Kumulatiivisesti signaalit muodostavat maineprofiilin. |
| **Social Graph** | Sosiaalinen graafi | Kontaktiesi ja kontaktiesi kontaktien verkko. Algoritmi etsii varmentajia konfiguroitavalla syvyydellä (esimerkiksi 3 tasoa). Ei globaalia lohkoketjua — verkosto muodostaa luonnollisesti yhteisöjä, joilla on limittymiä. |
| **Tax Allocation** | Verojen allokointi | Mekanismi, jolla veronmaksaja päättää, mihin osa hänen veroistaan menee. Allokoitava prosenttiosuus kasvaa vuosi vuodelta. |
| **Track Record** | Track record | Yleisesti: historia henkilön tai organisaation menneistä tuloksista, onnistumisista ja epäonnistumisista. Tässä: tietyn DID-identiteetin kaikkien menneiden vuorovaikutusten summa verkostossa — todennetut väitteet, hyväksytyt ja hylätyt tietueet — joista sen maine johdetaan. |
| **Verifier** | Varmentaja | Algoritmisesti valittu osallistuja, joka todentaa ja julkaisee tietueen. Panttaa hyvän nimensä tiedon totuudenmukaisuuteen. |
