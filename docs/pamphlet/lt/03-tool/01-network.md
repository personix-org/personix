---
title: "Reputation-Based Social Network"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Reputacija grįstas socialinis tinklas

Kad įvyktų pokytis, mums reikia kruopščiai suprojektuoto įrankio. Pirmiausia jį trumpai apibrėšime, o vėlesniuose skyriuose kiekvieną dalį panagrinėsime išsamiau ir pridėsime daugiau. Įsivaizduok necenzūruojamą, globalų, decentralizuotą socialinį tinklą, kuriame galėtum saugiai susikurti ir valdyti savo tarpininkaujančią tapatybę — vadinamąją decentralizuotą tapatybę (DID). DID yra skaitmeninė tapatybė, kurią susikuri ir valdai pats, nepriklausydamas nuo jokio centrinio autoriteto. Niekas negali jos atimti ar suklastoti, nes ji kriptografiškai pasirašyta tavo privačiuoju raktu (arba raktais, per multisig).

> [!note] Pastaba
> Viena iš pasekmių — tokia tapatybė palaipsniui galėtų pakeisti valstybės išduodamus tapatybės dokumentus. Bet apie tai daugiau skyriuje apie perėjimą.

![TAVO TAPATYBĖ, TAVO RAKTAI, TAVO TAISYKLĖS](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

Tokiame tinkle per savo tapatybę galėtum pranešti, kad kas nors padarė tau žalą (o vėliau, galbūt, kad ją atlygino ar buvo priverstas atlyginti). Kad šis grįžtamasis ryšys — nukreiptas į žalos sukėlėją — turėtų vertę kaip aktualus šaltinis, informacijos įvedimas į tinklą turi kainuoti laiką, energiją ir pinigus — o be to, kitiems turi būti pateiktas patikrinamas įrodymas, kad tai nėra tuščios plepalos.

Informacijos skaitymas būtų lengvas ir palyginti pigus, o atskiro įrašo sukūrimas — brangus ir reiklus. Rašymas vyktų pagal aiškų protokolą, kuriame skaičiavimas pagal pasirinktą algoritmą griežtai nustato, kurio DID prašyti pateiktos informacijos patikros ir kaip veikti toliau, kad pasirinktas dalyvis apdorotų informaciją tavo vardu, ją paskelbtų ir taptų jos tikrintoju.

> [!note] Algoritmas prieš radikalizmą
> Algoritminė tikrintojų atranka užtikrina, kad neradikalūs informacijos skelbėjai laikui bėgant išlaikys beveik neutralią pusiausvyrą tarp paskelbtos informacijos kaštų ir atlygio už patikrą.

![SKELBIMAS KAINUOJA LAIKĄ, ENERGIJĄ IR PINIGUS](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Pažiūrėkime, kaip algoritmas atrenka tikrintoją.

> [!note] Algoritmas
> Algoritminė atranka nedeterministiškai parenka skirtingą tikrintoją (arba galimų tikrintojų aibę) skirtingiems informacijos vienetams. Viso DID dokumento hash'as (vienakryptė matematinė funkcija, iš bet kokio įvesties duomens sukurianti unikalų „atspaudą“ — tarsi dokumento pirštų atspaudą) nustato poziciją nuosekliame hash žiede ir parenka tikrintojų kandidatus.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Paprastai tariant: algoritmas paima visą tavo DID dokumentą, apskaičiuoja iš jo atspaudą, ir tas atspaudas nustato tavo tikrintoją.

![KAIP ALGORITMAS ATRENKA TAVO TIKRINTOJĄ](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Su pirmuoju tikrintoju, kurį algoritmas parenka, tau kaip skelbėjui gali ir nepavykti — tavo reputacija ar deklaruotos nuostatos gali neatitikti jo reikalavimų. Algoritmiškai tęstum kito paiešką atlikdamas dar vieną rekursyvią iteraciją, kuri priskiria tau tolesnį tikrintoją. Su kiekvienu žingsniu „atstumas“ iki tikslinio tikrintojo auga, o kartu auga ir lydintys metaduomenys, kuriuos reikia paskelbti. Duomenims augant, kaštai natūraliai kyla (ne tik dėl pradinio teiginio dydžio, bet ir dėl metaduomenų, kaupiančių su kiekvienu atmetimu). Patikima informacija praeina kur kas lengviau nei beprasmiškos užgaidos. Kiekvienas žmogus pats sprendžia, kokią kainą pasirengęs pakelti ir kiek jam svarbus įrašas — radikalizmas garantuotai brangs.

![KAIP TIKRINTOJAS ATSAKO](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Kad ir ką tikrintojas nuspręstų atsakydamas į tavo patikros užklausą, kamuolys grįžta į skelbėjo pusę: jis gali priimti tikrintojo pasiūlymą dėl patikros paslaugų, įtraukti atsakymą į chronologiją ir bandyti dar kartą (brangiau) arba pasitraukti ir nuryti prarastus kaštus.

![IŠDAVĖJO PASIRINKIMAS](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Kad savo informacijai suteiktum didesnį svorį ir geresnę priėmimo pas tikrintojus galimybę, tu — kaip skelbėjas, suinteresuotas skelbiama informacija — galėtum pasinaudoti **patikimo autoriteto** paslaugomis. Autoritetas arba atmeta pateiktą informaciją, arba ją priima ir stato ant jos savo gerą vardą (reputaciją). Autoritetas paprastai prašo realaus pasaulio įrodymų, juos patikrina ir suklasifikuoja. Rezultatas yra jo atlikto duotojo atvejo vertinimo duotuoju metu protokolas. Įsivaizduok autoritetą kaip tam tikros rūšies paslaugos specialistą tiek realiame, tiek skaitmeniniame pasaulyje — pavyzdžiui, tyrėją, auditorių, draudiką, tam tikros klasės prekių tiekėją (iš esmės bet kurį ekonominį veikėją rinkoje).

![KAIP TINKLE ATSIRANDA ĮRAŠAS](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Iki to laiko, kai bandysi paskelbti informaciją tinkle, jis greičiausiai jau turės informacijos apie savo veikėjus — tai reputacijos signalai. Susigaudyti, kaip skaityti reputacijos signalus — ką jie tau reiškia skirtingose situacijose ir kokią riziką neša — gali būti nelengva. Kiekvienas dalyvis per savo DID gali į reputacijos įrašus žiūrėti kitaip, priklausomai nuo situacijos, kurią sprendžia dėl kitos šalies. Ar kita šalis yra patikimas mokėtojas, ar man verslo sandoriui reikia reikalauti pinigų iš anksto? Ar siūlomas produktas turi atsiliepimų apie paslėptą sukčiavimą ar defektus? Ar jie mėgina išsisukti nuo sutartinės atsakomybės, kai kas nors nutinka blogai? Kartais praverčia sudėtingesnis žvilgsnis į bendrą kitos šalies nuoseklumą — tai priklauso nuo to, kas prašo apžvalgos, nuostatų. Rinka galėtų pasiūlyti produktų ir paslaugų, kurie supaprastina, apdoroja ir paaiškina reputacijos skaitymą konkrečios situacijos kontekste. Šiam tikslui gali pasitarnauti ir įvairūs autoritetai bei jų siūlomos paslaugos.

![KAIP SKAITYTI REPUTACIJĄ](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Pavyzdžiai
> Tipiška skelbėjus dominanti — ir kitiems vertinga — informacija susijusi su įvykiais, peržengiančiais įprastą tarpasmeninę komunikaciją realiame ar virtualiame pasaulyje.
>
> Neigiami pavyzdžiai:
> - nusikalstamų veikų įrodymai (pvz., patikrinti patikimo tiriamojo organo)
> - netiesioginiai įrodymai (patys savaime silpni, bet statistiškai kaupiami) — pvz., pakartotinis buvimas šalia kelių vagysčių per trumpą laiką → vis dar sutapimas?
> - sutarties pažeidimas
>
> Teigiami pavyzdžiai:
> - atlyginta žala (savanoriškai arba bendruomenei spaudžiant kaip bausmė)
> - autoriteto X pasiūlytos bausmės priėmimas ir atlikimas
> - autoritetas X tam tikru mastu atšaukė nusikaltėlio nuosavybės teisių pripažinimą
>
> Kiekvienas pats sprendžia, kaip surinkti prieinamą informaciją apie kitą šalį ir įvertinti riziką pagal savo nuostatas.

![KĄ GALI ĮRAŠYTI TINKLE?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Ar informacija apie tave atsiras tinkle, priklauso išimtinai nuo tavo paties elgesio.
> Tau niekada nebūtina prisijungti prie tokio tinklo, tačiau informacija apie tave jame vis tiek gali atsirasti. Tai priklauso išimtinai nuo tavo veiksmų ir jų poveikio kitiems.

![BENDRUOMENĖ GALI JĮ ATVERTI UŽ TAVE](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Tai, ką ką tik trumpai apibrėžiau, yra tai, kaip galėtų veikti decentralizuotos tapatybės (DID) įkvėptas socialinis tinklas. Pirminis DID koncepcijų tikslas yra stiprinti privatumą ir laisvę per principą prenumeruoti taisykles, kurių laikysiuosi ir pagal kurias gyvensiu — suteikiant vartotojams galimybę spręsti, kokią informaciją dalytis ir kokiomis sąlygomis.

Siūlau DID toliau sujungti į komunikacijos tinklą, kuriame jų turėtojai keičiasi grįžtamuoju ryšiu net už situacijų, kai kam nors kas nors nutiko ir bendruomenė ar asmuo turi sureaguoti, ribų. Toks prevencinis taisyklių, prie kurių prisirašėme, palyginimas — su galimybe apskaičiuoti ekonomines ir kitas abipusių nuokrypių nuo lūkesčių dėl to, kaip kita pusė turėtų veikti, pasekmes — galėtų būti laikomas paskata ieškoti konsensuso. Vietoj laisvės tokia sistema pabrėžtų savanorišką sprendimų priėmimą kartu su atsakomybe už elgesį realiame pasaulyje.

Pavienis asmuo negali sulaužyti sistemos vienas — grupė žmonių turi didesnę galimybę, o grupė žmonių su suderintu konsensusu ir paskatomis daugeliu klausimų traukti išvien turi dar didesnę galimybę atsispirti autoritariniams polinkiams. Organizacijos prielaida iš pirmojo skyriaus bus įvykdyta, kai bus patenkintos dvi sąlygos: DID reputacijos tinklas pakankamai reprezentatyviai aprėps bendruomenes, kad jo naudojimas nustotų būti egzotiškas. Ir tuo pat metu šis bendruomenės segmentas taps ekonomiškai reikšminga mažuma, galinčia atkakliai derėtis su likusia visuomene.

> [!note] Savanoriškumas prieš laisvę
> Laisvė — teigiama prasme — būtų antrinis dviejų veiksnių balansavimo padarinys: savanoriškumo ir aplinkos spaudimo link atsakomybės.

> [!note] DI era ir reputacijos vertė
> Dirbtinio intelekto eroje viskas, kas susiję su kognityviniu mąstymu, yra automatizuojama — ir tai gali nueiti dar toliau. Kas tuomet lieka žmogaus veikloje kaip konkurencinis pranašumas? Atsakymas sunkus, ir kažkas tikrai bus rasta, bet vieną dalyką galime pasakyti tvirtai: reputacija nulems. Patikrinama tavo elgesio, tavo įsipareigojimų ir jų vykdymo istorija — to DI už tave nesukurs.

![DI NEGALI SUKURTI TAVO REPUTACIJOS — TIK TU PATS GALI](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![TIESOS EKONOMIKA](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
