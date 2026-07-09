---
title: "Konsensus ja kontrollimisprotsess"
chapter: 3
part: "Kuidas kontrollimine toimib"
lang: en
version: v6
source: v1
---

# Konsensus ja kontrollimisprotsess

Konsensuse ülesehitamiseks selle üle, milliseid reegleid ühiskond peaks keskmiselt üleval hoidma ja jõustama, saab aidata järgmine mehhanism. DID-osalejana deklareerin reeglid, millega end seon ja mille järgi elan, ning avaldan need. (Kujutle seda kui põhikirja ja statuute, mis minu arvates moodustavad minu ideaalse maailma — maailma, kus ma ei tunne end piiratuna, vaid turvaliselt.)

Ma saan ette hinnata, kuidas minu DID-kontaktid reageeriksid — ja hinnata, kui tugevalt ja kelle poolt mind tavalistes ühiskondlikes või ärialastes interaktsioonides sanktsioneeritaks, kui need hüpoteetiliselt aset leiaksid.

Lõplik hindamine toimub siis, kui sa küsid informatsiooni teiselt DID-lt või palud tal kontrollida väidet (või palud autoriteedilt teenust jne), mille soovid avaldada reputatsioonivõrku. See peaks kujunema samamoodi, nagu see kujuneb siis, kui sa jooksutad hindamise ise, kuivkatsena, vastaspoole deklareeritud poliitika vastu — ja kui ei kujune, on midagi vastaspoole poolel valesti: ta üritab mängida ebaausat mängu.

Tulemuseks on kas vastuvõtmine koos noteeritud hinnaga kontrollimise eest (kontrollija või autoriteedi teenuste puhul) või tagasilükkamine. Nii sanktsioonid kui boonused hindaja poliitikast kõrvalekaldumise eest on kokku pandud noteeritud hinda. Taotleja otsustab siis, kas võtta tingimused vastu või liikuda edasi jaotusalgoritmi järgmisse kontrollimisvooru — korrates protsessi, kuni ta on rahul või kuni majandus muudab jätkamise mõttetuks.

> [!note] Sotsiaalne graaf
> Reputatsioonivõrk on ennekõike suhtlusvõrk. Sa lisad kontakte — inimesi, kes ühendusega nõustuvad. Neil on kontaktid ja neil kontaktidel on kontaktid. Algoritm otsib kontrollijaid seadistatava sügavuse piires (nt kolm taset: sinu otsekontaktid, nende kontaktid ja üks tase kaugemal). Globaalset plokiahelat pole vaja — võrk moodustab loomulikult kogukondi, mis kattuvad teiste kogukondadega.
>
> Algoritm on mittedeterministlik: see räsib sinu väitedokumendi, kaardistab räsi positsiooni selle ringi tuntud identiteetide ringil ja valib lähima kandideerivaks kontrollijaks. Sa ei saa ennustada ega mõjutada, kes sinu väidet kontrollib.

Iga kontrollija tagasilükkamine suurendab sinu dokumenti ja tõstab selle töötlemiskulu — see on esimene kulukanal (dokumendi kasv). Iga uus kontrollija võtab tasu andmemahu, sinu reputatsiooni ja selle põhjal, kui kaugele sinu väite sisu kaldub tema deklareeritud kontrollimispoliitikast — see on teine kulukanal (riskipreemia). Ja iga iteratsioon maksab aega ja energiat — kolmas kulukanal.

> [!note] Mida kontrollija järjekorras kontrollib
> Kui kontrollija on valitud, hindab ta väidet umbes neljas järjestatud sammus — kõigepealt kõige odavamad filtrid, kalleimad sisukontrollid viimasena:
>
> 1. **Poliitika värav.** Kas seda liiki väide kuulub üldse selle hulka, mida kontrollija avalikult kontrollib? Kui ei, lükatakse päring otsekohe tagasi.
> 2. **Autoriteedi usaldus.** Kas väidet toetanud autoriteet on kontrollija enda deklareeritud poliitika kohaselt piisavalt usaldusväärne? Kontrollija usalduslävest allpool olev autoriteet on tagasilükkamise alus sõltumata väite sisust.
> 3. **Väljaandja reputatsioon.** Kas väljaandja vastab reputatsiooniläveedele, mille kontrollija on seda liiki väite jaoks deklareerinud? Madal reputatsioon võib kas tõsta tasu või vallandada tagasilükkamise.
> 4. **Sisukontroll.** Alles siis, kui esimesed kolm väravat läbitakse, hindab kontrollija väidet ennast — allkirju, sisemist järjepidevust, formaalset korrektsust ja seda, kui kaugele see kontrollija poliitikast kaldub. Selle viimase sammu eest võetud tasu peegeldab tegelikult võetud riski.
>
> Kontrollija avaldab poliitika, mis reguleerib igat neist väravatest, nii et sammud ei ole tema äranägemisel — teda seob see, mida ta on juba deklareerinud. Avaldatud poliitikast kõrvalekaldumine on ise avaldatav väide tema vastu ja ta maksab selle eest oma reputatsiooniga.

Tulemus: usaldusväärse ja kasuliku väite avaldamine ei maksa peaaegu midagi. Radikaalse väite avaldamine maksab rohkem. Vale avaldamine muutub keelavalt kalliks — sul tuleb itereerida läbi kontrollija kontrollija järel ja igaüks, kes su tagasi lükkab, lisab kulusid. Turg hinnastab su väite ja hind ütleb sulle, kus sa asud nende kogukondade suhtes, milles sa liigud.

Ei piisa deklareerimisest, et sa järgid reeglit, kui tegelikult sa ei järgi. Sellisel juhul riskib su DID negatiivse kirje avaldamisega, mis paljastab silmakirjalikkuse — mis muudab su riskiks kõigi teiste jaoks. Tulemuseks peaks olema vähem, kuid järjekindlamalt järgitud reegleid ja selle seaduste ja määruste džungli väljaraiumine, milles isegi õigusspetsialistid vaevu orienteeruvad.

![SILMAKIRJALIKKUS ON KÕIGE KALLIM KÄITUMINE](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Konsensus vs aruandekohustus
> Selleks et võrk toimiks väärtusliku informatsiooniallikana, ei tohiks DID olla liiga radikaalne — muidu lükkavad teised ta tagasi. Ühiskondlik surve otsib tasakaalu ja katsed seda destabiliseerida saavad tõenäoliselt karistatud.

![DEKLAREERI OMA REEGLID, MAKSA HIND](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Häälte arv ei ole sama mis hääle kaal
> Juraj Karpiš ütleb, et „raha on heade tegude mälu". Mina lisaksin, et reputatsioon on halbade tegude mälu.
>
> Sellest järeldub, et meritokraatlikult väärib see, kes panustab rohkem ja kellel ei ole halba reputatsiooni, kogukonnas suuremat hääle kaalu. Kui vaadata kahepoolsete suhete prisma kaudu: kui ma kaalun, milliste konsensusesurvetega arvestada, läheb suurim kaal suhetele, millest ma saan suurima majandusliku kasu. Kümme inimest, kellega mul ei ole aktiivset kaubandust, mõjutavad mind palju vähem kui üks püsiv äripartner. See paradigma ei piirdu kaubandusega — see laieneb ühiskondlikele, poliitilistele ja muudele suhetele.
