---
title: "Sõnastik"
part: "Lisa"
lang: en
version: v6
---

# Sõnastik

| Mõiste | Eesti keel | Tähendus |
|------|-------|---------|
| **Authority** | Autoriteet | Usaldusväärne üksus (inimene, organisatsioon), mis kontrollib informatsiooni ja paneb selle peale mängu oma reputatsiooni. Võib olla spetsialiseeritud (uuriv, õiguslik, tehniline). |
| **Claim** | Väide | Üldiselt: mis tahes kontrollitav väide. Siin: reputatsioonivõrku avaldatud kirje — väide sündmuse, omaduse või suhte kohta, mis on krüptograafiliselt allkirjastatud ja kontrollitud. Nt „ma olen omavalitsuse X elanik" või „see inimene rikkus lepingut". |
| **Compartmentalization** | Kompartmentaliseerimine | Üldiselt: informatsiooni eraldamine isoleeritud üksusteks nii, et ühe üksuse paljastamine ei kompromiteeri teisi. Luureteenistustest tuntud põhimõte. Siin: paralleelsed DID-identiteedid diktatuurides — ühe kompromiteerimine ei paljasta teisi. |
| **Consistent Hash Ring** | Järjepidev räsiring | Algoritmiline mehhanism kontrollijate valimiseks — positsiooni ringil määrab DID-dokumendi räsi sotsiaalse graafi sees. Tagab mittedeterministliku, ent kontrollitava valiku. |
| **DID** | DID (detsentraliseeritud identiteet) | Digitaalne identiteet, mille sa ise lood ja mille üle sul on kontroll, ilma keskvõimuta. Krüptograafiliselt allkirjastatud sinu privaatvõtmega — keegi ei saa seda tühistada ega võltsida. |
| **DID Document** | DID-dokument | Avalikult kättesaadav andmefail, mis kirjeldab sinu DID-identiteeti — sisaldab avalikke võtmeid, võrguaadresse ja metaandmeid. Kasutatakse sinu identiteedi kontrollimiseks võrgus. |
| **Due Diligence** | Due diligence | Üldiselt: vastaspoole põhjalik kontroll enne äri- või õigussuhtesse astumist — tema ajaloo, rahanduse, reputatsiooni ja riskide kontroll. Siin: reputatsioonivõrgus toimub see kontrollitud kirjete kättesaadavuse tõttu kiiremini ja automaatsemalt. |
| **Economic Neutrality Principle** | Majandusliku neutraalsuse põhimõte | Aus käitumine võrgus on majanduslikult nulli lähedal — avaldamiskulud tulevad tagasi kontrollimistasudena. Ebaaus käitumine on puhas kahjum. |
| **Emergent** | Emergentne | Spontaanselt lihtsamate osade interaktsioonidest tekkiv, ilma et keegi seda kavandaks või juhiks. Linnuparv lendab formatsioonis ilma plaanita — formatsioon kerkib esile iga isendi järgitavatest lihtsatest reeglitest. |
| **Emergent Social Contract** | Emergentne ühiskondlik leping | Käitumisreeglid, mis ei teki mitte ülevalt (seadus), vaid altpoolt — kogukonna korduvatest interaktsioonidest ja konsensusest. |
| **ESR** | Elektrooniline kuluregister | Pakutud süsteem avaliku sektori kulutuste läbipaistvaks jälgimiseks — iga teostatud riigi kulutus sobitatakse plaanitud maksega. Inspireeritud Tšehhi EET-st, kuid pööratud riigi vastu. |
| **Hash** | Räsi (sõrmejälg) | Üldiselt: ühesuunaline matemaatiline funktsioon, mis toodab mis tahes sisendist ainulaadse fikseeritud pikkusega „sõrmejälje" — nagu dokumendi sõrmejälg. Sama sisend annab alati sama väljundi, kuid sisendit ei saa väljundist tuletada. Siin: kasutatakse positsiooni määramiseks räsiringil ja dokumendi terviklikkuse kontrollimiseks. |
| **Just-in-Time Funding** | Just-in-time-rahastamine | Riigi rahastamine, mis on tingimuslik läbipaistvusest — raha liigub üksnes siis, kui riik võtab ESR-i vastu ja sobitab oma kulutused. Kang koostöö sundimiseks. |
| **Meritocracy** | Meritokraatia | Üldiselt: süsteem, kus positsiooni määrab tegelik teene ja tõestatud võimekus, mitte formaalsed tiitlid, sidemed või päritud privileegid. Siin: reputatsioonivõrk soosib loomulikult neid, kes tõestatavalt panustavad kogukonda — nende hääl kannab suuremat kaalu tegevusajaloo, mitte ameti tõttu. |
| **Onion Gateway** | Sibulalüüs | DID-identiteedi võrguaadress sibulvõrgus. Eraldi DID-dokumendist — seda saab muuta identiteeti kaotamata (sarnaselt domeeni taga oleva IP-aadressi muutmisega). |
| **Onion Routing** | Sibulmarsruutimine (Tor) | Sideprotokoll, mis tagab võrgu tsenseerimatuse. Sõnumid krüpteeritakse kihtidena — iga sõlm koorib maha ühe kihi, kuid ei tea kogu teed. |
| **Oracle Problem** | Oraakli probleem | Üldiselt: kuidas tagada, et digitaalsesse süsteemi sisenevad andmed vastaksid täpselt sellele, mis tegelikult füüsilises maailmas toimus. Termin pärineb plokiahela valdkonnast. Siin: lahendatud autoriteetide kaudu, kes panevad oma reputatsiooni mängu tagatiseks, et digitaalne kirje vastab füüsilisele tegelikkusele. |
| **Phenomenological** | Fenomenoloogiline | Üldiselt: lähenemine, mis uurib nähtusi nii, nagu need vahetus kogemuses avalduvad, jälgides seda, mis neist järeldub, ilma eelnevalt antud teooriateta. Siin: vabadus, ühiskondlik leping ja käitumisnormid on vaadeldud nähtused — tagajärjed tuhandetest mikrointeraktsioonidest inimeste vahel, mitte ülevalt defineeritud põhimõtted. |
| **Policy** | Policy (poliitika) | Üldiselt: reeglite või põhimõtete kogum, mis reguleerib käitumist antud kontekstis. Siin: iga DID-võrgu osaleja deklareerib oma poliitika — kuidas ta reageerib teiste konkreetsele käitumisele, milliseid reegleid ta järgib ja milliseid karistusi ta peab proportsionaalseks. Poliitikate kogum moodustab emergentse ühiskondliku lepingu. |
| **Proxy** | Proksi | Üldiselt: asendaja või vahendaja — süsteem või üksus, mis tegutseb teise nimel. Kasutatud siin kahes kontekstis: (1) ESR kui proksi, mis sobitab avaliku sektori kulutused plaanitud maksetega; (2) vaatlejad kui proksi avaldaja ja kontrollija vahel vaatleja trikis. |
| **Publisher** | Avaldaja | Võrgu osaleja, kes loob ja avaldab kirje (väite ülekohtu, heastamise jne kohta). Kannab avaldamise kulu. |
| **Reputation-Based Social Network (RSN)** | Reputatsioonivõrk | Detsentraliseeritud suhtlusvõrk, kus osalejad vahetavad tagasisidet reaalse maailma käitumise kohta. Kirjete loomine on kulukas, lugemine odav. |
| **Reputation Signal** | Reputatsioonisignaal | Üksik kirje võrgus — positiivne (kahju heastamine, kohustuse täitmine) või negatiivne (ülekohus, lepingurikkumine). Kumulatiivselt moodustavad signaalid reputatsiooniprofiili. |
| **Social Graph** | Sotsiaalne graaf | Sinu kontaktide ja sinu kontaktide kontaktide võrk. Algoritm otsib kontrollijaid seadistatava sügavuse piires (näiteks 3 taset). Globaalset plokiahelat ei ole — võrk moodustab loomulikult kogukondi kattumistega. |
| **Tax Allocation** | Maksude jaotamine | Mehhanism, mille abil maksumaksja otsustab, kuhu osa tema maksudest läheb. Jaotatav protsent kasvab aasta-aastalt. |
| **Track Record** | Tegevusajalugu | Üldiselt: inimese või organisatsiooni mineviku tulemuste, edude ja ebaõnnestumiste ajalugu. Siin: antud DID-identiteedi kõigi mineviku interaktsioonide summa võrgus — kontrollitud väited, vastu võetud ja tagasi lükatud kirjed —, millest tuletatakse tema reputatsioon. |
| **Verifier** | Kontrollija | Osaleja, kes on algoritmiliselt valitud kirjet kontrollima ja avaldama. Paneb oma hea nime mängu informatsiooni tõesuse peale. |
