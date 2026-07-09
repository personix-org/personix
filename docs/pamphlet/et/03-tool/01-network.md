---
title: "Reputatsioonipõhine suhtlusvõrk"
chapter: 2
part: "Tööriist"
lang: en
version: v6
source: v1
---

# Reputatsioonipõhine suhtlusvõrk

Muutuse esilekutsumiseks vajame hoolikalt kavandatud tööriista. Kõigepealt visandame selle põgusalt; hilisemates peatükkides vaatleme iga osa üksikasjalikumalt ja lisame veel. Kujuta ette tsenseerimatut, globaalset, detsentraliseeritud suhtlusvõrku, kus saaksid turvaliselt luua ja hallata oma proksi-identiteeti — nn detsentraliseeritud identiteeti (DID). DID on digitaalne identiteet, mille sa ise lood ja mille üle sul on kontroll, ilma sõltuvuseta ühestki keskvõimust. Keegi ei saa seda ära võtta ega võltsida, sest see on krüptograafiliselt allkirjastatud sinu privaatvõtmega (või võtmetega, multisig'i kaudu).

> [!note] Märkus
> Üks järeldus on, et selline identiteet võiks järk-järgult asendada riigi väljastatud isikut tõendavad dokumendid — kuid sellest lähemalt ülemineku peatükis.

![SINU IDENTITEET, SINU VÕTMED, SINU REEGLID](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

Sellises võrgus saaksid oma identiteedi kaudu teatada, et keegi on sulle kahju tekitanud (ja hiljem võimalusel, et ta on selle heastanud või sunnitud seda tegema). Selleks, et sellel tagasisidel — mis on suunatud kahju põhjustajale — oleks väärtust asjakohase allikana, peab informatsiooni võrku sisestamine maksma aega, energiat ja raha — ning lisaks tuleb toota kontrollitav tõend teistele, et tegemist ei ole tühja lobaga.

Informatsiooni lugemine oleks lihtne ja suhteliselt odav, kuid üksiku kirje loomine oleks kulukas ja nõudlik. Kirjutamine järgiks selget protokolli, milles arvutus valitud algoritmi järgi määrab rangelt, milliselt DID-lt küsida esitatud informatsiooni kontrollimist ja kuidas edasi toimida, et valitud osaleja töötleks informatsiooni sinu nimel, avaldaks selle ja saaks selle kontrollijaks.

> [!note] Algoritm vs radikalism
> Kontrollijate algoritmiline valik tagab, et mitteradikaalsed informatsiooni avaldajad säilitavad aja jooksul peaaegu neutraalse tasakaalu avaldatud informatsiooni kulude ja kontrollimise tasude vahel.

![AVALDAMINE MAKSAB AEGA, ENERGIAT JA RAHA](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Vaatame, kuidas algoritm kontrollija valib.

> [!note] Algoritm
> Algoritmiline valik valib mittedeterministlikult erineva kontrollija (või võimalike kontrollijate hulga) erinevate informatsioonitükkide jaoks. Tervikliku DID-dokumendi räsi (ühesuunaline matemaatiline funktsioon, mis toodab mis tahes sisendist ainulaadse „sõrmejälje" — nagu dokumendi sõrmejälg) määrab positsiooni järjepideval räsiringil ja valib kontrollijakandidaadid.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Lihtsalt öeldes: algoritm võtab kogu sinu DID-dokumendi, arvutab sellest sõrmejälje ja see sõrmejälg määrab sinu kontrollija.

![KUIDAS ALGORITM SINU KONTROLLIJA VALIB](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Esimese kontrollijaga, kelle algoritm valib, ei pruugi sul kui avaldajal õnnestuda — sinu reputatsioon või deklareeritud seaded ei pruugi vastata tema nõuetele. Sa jätkaksid algoritmiliselt järgmise otsimist, sooritades järgmise rekursiivse iteratsiooni, mis määrab sulle uue kontrollija. Iga sammuga kasvab „kaugus" sihtkontrollijani ja koos sellega ka avaldamisele kuuluvad kaasnevad metaandmed. Andmete kasvades tõusevad loomulikult ka kulud (mitte ainult väite algse suuruse tõttu, vaid ka iga tagasilükkamisega kuhjuvate metaandmete tõttu). Usaldusväärne informatsioon läbib palju kergemini kui mõttetud tujud. Igaühe otsustada on, kui kõrget hinda ta on valmis kandma ja kui palju see kirje talle korda läheb — radikalism läheb garanteeritult kalliks.

![KUIDAS KONTROLLIJA VASTAB](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Mida iganes kontrollija sinu kontrollimispäringule vastuseks otsustab, on pall tagasi avaldaja väljakupoolel: ta võib võtta vastu kontrollija pakkumise kontrollimisteenuste kohta, lülitada vastuse kronoloogiasse ja proovida uuesti (kallimalt) või lahkuda ja neelata alla uppunud kulu.

![VÄLJAANDJA VALIK](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Selleks et anda oma informatsioonile suuremat kaalu ja parem võimalus, et kontrollijad selle vastu võtaksid, saaksid sina — kui avaldaja, kellel on huvi väljastatava informatsiooni vastu — kasutada **usaldusväärse autoriteedi** teenuseid. Autoriteet kas lükkab esitatud informatsiooni tagasi või võtab selle vastu ja paneb selle peale mängu oma hea nime (reputatsiooni). Autoriteet nõuab tavaliselt reaalse maailma tõendeid, kontrollib neid ja klassifitseerib. Väljundiks on protokoll tema hinnangust antud juhtumile antud ajal. Kujutle autoriteeti kui teatava teenuseliigi spetsialisti nii reaalses kui digitaalses maailmas — näiteks uurija, audiitor, kindlustaja, teatava kaubaklassi tarnija (sisuliselt mis tahes majandustegutseja turul).

![KUIDAS KIRJE VÕRGUS TEKIB](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Selleks ajaks, kui sa üritad informatsiooni võrku avaldada, sisaldab see tõenäoliselt juba informatsiooni oma osaliste kohta — need on reputatsioonisignaalid. Orienteerumine selles, kuidas reputatsioonisignaale lugeda — mida need sulle erinevates olukordades tähendavad ja milliseid riske kannavad — ei pruugi olla triviaalne. Iga osaleja saab reputatsioonikirjeid oma DID kaudu vaadelda erinevalt, sõltuvalt olukorrast, millega ta vastaspoole suhtes tegeleb. Kas vastaspool on usaldusväärne maksja või pean nõudma äritehinguks raha ette? Kas pakutav toode kannab arvustusi varjatud pettuse või defektide kohta? Kas ta üritab lepingulisest vastutusest kõrvale hiilida, kui midagi läheb valesti? Mõnikord kulub ära keerukam vaade vastaspoole üldisele järjepidevusele — see sõltub selle eelistustest, kes ülevaadet küsib. Turg võiks pakkuda tooteid ja teenuseid, mis lihtsustavad, töötlevad ja selgitavad reputatsiooni lugemist antud olukorra kontekstis. Sel eesmärgil saavad teenida ka mitmesugused autoriteedid ja nende pakutavad teenused.

![KUIDAS REPUTATSIOONI LUGEDA](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Näited
> Tüüpiline informatsioon, mis pakub avaldajatele huvi — ja on teistele väärtuslik — puudutab sündmusi, mis jäävad väljapoole tavalist inimestevahelist suhtlust reaalses või virtuaalses maailmas.
>
> Negatiivsed näited:
> - tõendid kuritegude kohta (nt auditeeritud usaldusväärse uurimisorgani poolt)
> - kaudsed tõendid (üksinda nõrgad, kuid statistiliselt kuhjuvad) — nt korduv viibimine mitme varguse lähedal lühikese aja jooksul → ikka veel juhus?
> - lepingu rikkumine
>
> Positiivsed näited:
> - heastatud kahju (vabatahtlikult või kogukonna surve all karistusena)
> - autoriteedi X pakutud karistuse vastuvõtmine ja kandmine
> - autoriteet X tühistas teatavas ulatuses toimepanija omandiõiguste tunnustamise
>
> Igaühe otsustada on koguda kättesaadavat informatsiooni vastaspoole kohta ja hinnata riske oma eelistuste järgi.

![MIDA SAAD VÕRGUS KIRJENDADA?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Kas informatsioon sinu kohta võrgus ilmub, sõltub üksnes sinu enda käitumisest.
> Sa ei pea sellise võrguga kunagi liituma, ometi võib informatsioon sinu kohta selles siiski ilmuda. See sõltub üksnes sinu tegudest ja nende mõjust teistele.

![KOGUKOND VÕIB SELLE SINU EEST AVADA](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

See, mille ma just põgusalt visandasin, on see, kuidas võiks töötada detsentraliseeritud identiteedist (DID) inspireeritud suhtlusvõrk. DID-kontseptsioonide esmane eesmärk on tugevdada privaatsust ja vabadust põhimõtte kaudu, et tellin need reeglid, mida ma järgin ja mille järgi elan — andes kasutajatele võime otsustada, millist informatsiooni ja millistel tingimustel jagada.

Ma teen ettepaneku ühendada DID-d veel edasi suhtlusvõrguks, kus nende hoidjad vahetavad tagasisidet ka väljaspool olukordi, kus kellegagi on midagi juhtunud ja kogukond või üksikisik peab reageerima. Sellist ennetavat võrdlust reeglitest, millega oleme end sidunud — koos võimalusega arvutada välja majanduslikke ja muid tagajärgi vastastikustest kõrvalekalletest ootustes selle suhtes, kuidas teine pool peaks toimima — võiks pidada motivatsiooniks konsensuse leidmisel. Vabaduse asemel rõhutaks selline süsteem vabatahtlikku otsustamist koos vastutusega reaalse maailma käitumise eest.

Üksik indiviid ei suuda süsteemi üksi murda — grupil inimestest on suurem võimalus ning grupil inimestest, kellel on läbiräägitud konsensus ja motivatsioonid tõmmata paljudes küsimustes ühte köit, on veelgi suurem võimalus autoritaarsetele kalduvustele vastu seista. Esimese peatüki organiseerumise eeldus saab täidetud, kui täidetud on kaks tingimust: DID-reputatsioonivõrk katab kogukondi piisavalt esinduslikult, nii et selle kasutamine lakkab olemast eksootiline. Ning samal ajal muutub see kogukonnasegment majanduslikult oluliseks vähemuseks, mis suudab ülejäänud ühiskonnaga enesekindlalt läbi rääkida.

> [!note] Vabatahtlikkus vs vabadus
> Vabadus — positiivses tähenduses — oleks kahe teguri tasakaalustamise teisene mõju: vabatahtlikkuse ja ümbritseva keskkonna surve vastutuse poole.

> [!note] Tehisintellekti ajastu ja reputatsiooni väärtus
> Tehisintellekti ajastul automatiseeritakse kõik, mis on seotud kognitiivse mõtlemisega — ja see võib minna veelgi kaugemale. Mis siis jääb inimtegevusse konkurentsieeliseks? Vastus on raske ja midagi kindlasti leitakse, kuid ühte võime kindlalt öelda: otsustab reputatsioon. Sinu käitumise, sinu kohustuste ja nende täitmise kontrollitav ajalugu — seda tehisintellekt sinu eest üles ei ehita.

![TEHISINTELLEKT EI SUUDA SINU REPUTATSIOONI ÜLES EHITADA — SEDA SUUDAD AINULT SINA](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![TÕE MAJANDUS](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
