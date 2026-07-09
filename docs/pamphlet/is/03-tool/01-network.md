---
title: "Samfélagsnet byggt á orðspori"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Samfélagsnet byggt á orðspori

Til að koma á breytingu þurfum við vandlega hannað verkfæri. Fyrst bregðum við upp stuttri mynd af því. Í síðari köflum skoðum við hvern hluta nánar og bætum fleirum við. Ímyndaðu þér óritskoðanlegt, hnattrænt, dreifstýrt samfélagsnet þar sem þú gætir á öruggan hátt búið til og haldið utan um staðgengilsauðkenni þitt — svokallað dreifstýrt auðkenni (DID). DID er stafrænt auðkenni sem þú býrð til og stýrir sjálfur, án þess að reiða þig á nokkurt miðlægt vald. Enginn getur tekið það af þér eða falsað það, því það er dulritað undirritað með einkalyklinum þínum (eða lyklum, í gegnum multisig).

> [!note] Athugasemd
> Ein afleiðing er sú að slíkt auðkenni gæti smám saman komið í stað opinberra skilríkja sem ríkið gefur út — en meira um það í kaflanum um umbreytinguna.

![AUÐKENNI ÞITT, LYKLAR ÞÍNIR, REGLUR ÞÍNAR](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

Í slíku neti gætir þú, í gegnum auðkenni þitt, tilkynnt að einhver hafi valdið þér tjóni (og síðar, hugsanlega, að hann hafi bætt úr því eða verið þvingaður til þess). Til að þessi endurgjöf — sem beinist að þeim sem olli tjóninu — hafi gildi sem áreiðanleg heimild, verður innsláttur upplýsinga í netið að kosta tíma, orku og peninga — og þar að auki verður að leggja fram staðfestanlega sönnun fyrir aðra um að þetta sé ekki innantómt hjal.

Að lesa upplýsingar væri auðvelt og tiltölulega ódýrt, en að búa til staka færslu væri kostnaðarsamt og krefjandi. Ritun fylgdi skýrri samskiptareglu, þar sem útreikningur samkvæmt völdu algrími ræður nákvæmlega hvaða DID skuli beðið um staðfestingu á innsendum upplýsingum og hvernig haldið skuli áfram þannig að valinn þátttakandi vinni úr upplýsingunum fyrir þína hönd, birti þær og verði staðfestingaraðili þeirra.

> [!note] Algrím gegn öfgum
> Algrímsval á staðfestingaraðilum tryggir að útgefendur upplýsinga sem eru ekki öfgakenndir haldi, með tímanum, nánast hlutlausu jafnvægi milli kostnaðar við birtar upplýsingar og umbunar fyrir staðfestingu.

![BIRTING KOSTAR TÍMA, ORKU OG PENINGA](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Lítum á hvernig algrímið velur staðfestingaraðila.

> [!note] Algrím
> Algrímsval velur, á ófyrirsjáanlegan hátt, mismunandi staðfestingaraðila (eða mengi mögulegra staðfestingaraðila) fyrir mismunandi upplýsingar. Hash (einstefnu-stærðfræðifall sem framleiðir einstakt „fingrafar" úr hvaða inntaki sem er — líkt og fingrafar af skjali) af öllu DID-skjalinu ræður staðsetningunni á samkvæmum hash-hring og velur staðfestingaraðila til greina.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Á mannamáli: algrímið tekur allt DID-skjalið þitt, reiknar út fingrafar af því, og það fingrafar ræður staðfestingaraðila þínum.

![HVERNIG ALGRÍMIÐ VELUR STAÐFESTINGARAÐILA ÞINN](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Með fyrsta staðfestingaraðilanum sem algrímið velur er ekki víst að þú, sem útgefandi, hafir árangur — orðspor þitt eða yfirlýstar stillingar uppfylla kannski ekki kröfur hans. Þú myndir halda leitinni áfram með algríminu að þeim næsta með því að framkvæma aðra endurkvæma ítrun, sem úthlutar þér enn öðrum staðfestingaraðila. Með hverju skrefi vex „fjarlægðin" að markstaðfestingaraðilanum, og sömuleiðis þau lýsigögn sem verður að birta. Eftir því sem gögnin vaxa hækkar kostnaðurinn eðlilega (ekki aðeins vegna upphaflegrar stærðar fullyrðingarinnar, heldur einnig vegna lýsigagnanna sem safnast upp við hverja höfnun). Trúverðugar upplýsingar komast miklu auðveldar í gegn en vitlausir duttlungar. Það er undir hverjum og einum komið hversu hátt verð hann er tilbúinn að bera og hversu miklu færslan skiptir hann — öfgar eiga tryggt með að verða dýrar.

![HVERNIG STAÐFESTINGARAÐILINN SVARAR](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Hvað sem staðfestingaraðilinn ákveður að svara staðfestingarbeiðni þinni, þá er boltinn aftur hjá útgefandanum: hann getur samþykkt tilboð staðfestingaraðilans um staðfestingarþjónustu, fellt svarið inn í tímaröðina og reynt aftur (dýrar), eða gengið burt og kyngt hinum töpuðu kostnaði.

![VAL ÚTGEFANDANS](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Til að gefa upplýsingum þínum meira vægi og betri líkur á að þær verði samþykktar hjá staðfestingaraðilum gætir þú — sem útgefandi með hagsmuni af upplýsingunum sem gefnar eru út — nýtt þér þjónustu **trausts álitsaðila**. Álitsaðilinn annaðhvort hafnar innsendum upplýsingum eða samþykkir þær og leggur gott nafn sitt (orðspor) að veði fyrir þeim. Álitsaðilinn óskar að jafnaði eftir gögnum úr raunheiminum, sannreynir þau og flokkar þau. Útkoman er bókun um mat hans á tilteknu máli á tilteknum tíma. Hugsaðu um álitsaðila sem sérfræðing í tiltekinni tegund þjónustu, bæði í raunheimi og stafrænum heimi — til dæmis rannsakanda, endurskoðanda, tryggingafélag, birgi tiltekins vöruflokks (í raun hvaða efnahagslegan geranda á markaði sem er).

![HVERNIG FÆRSLA VERÐUR TIL Í NETINU](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Þegar þú reynir að birta upplýsingar í netinu inniheldur það líklega þegar upplýsingar um gerendur sína — það eru orðsporsmerki. Að rata um hvernig lesa skuli orðsporsmerki — hvað þau þýða fyrir þig í mismunandi aðstæðum og hvaða áhættu þau bera — er ekki endilega einfalt. Hver þátttakandi getur horft á orðsporsfærslur á mismunandi hátt í gegnum DID sitt, eftir þeim aðstæðum sem hann er að fást við gagnvart mótaðilanum. Er mótaðilinn áreiðanlegur greiðandi, eða þarf ég að krefjast greiðslu fyrirfram fyrir viðskipti? Bera vörurnar sem boðnar eru umsagnir um falin svik eða galla? Er verið að reyna að smjúga undan samningsbundinni ábyrgð þegar eitthvað fer úrskeiðis? Stundum kemur flóknari sýn á heildarsamkvæmni mótaðilans að góðum notum — það veltur á óskum þess sem biður um yfirlitið. Markaðurinn gæti boðið vörur og þjónustu sem einfalda, vinna úr og skýra lestur orðspors í samhengi þeirra aðstæðna sem við á. Ýmsir álitsaðilar og sú þjónusta sem þeir bjóða geta líka þjónað þessum tilgangi.

![HVERNIG LESA Á ORÐSPOR](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Dæmi
> Dæmigerðar upplýsingar sem útgefendur hafa áhuga á — og eru verðmætar öðrum — varða atburði umfram venjuleg mannleg samskipti í raunheimi eða sýndarheimi.
>
> Neikvæð dæmi:
> - sönnun um refsiverð brot (t.d. yfirfarin af traustum rannsóknaraðila)
> - óbein sönnun (veik ein og sér, en tölfræðilega uppsöfnuð) — t.d. endurtekin nærvera nálægt mörgum þjófnuðum á stuttum tíma → enn tilviljun?
> - samningsbrot
>
> Jákvæð dæmi:
> - bætt tjón (sjálfviljugt eða undir þrýstingi frá samfélaginu sem refsing)
> - samþykki og afplánun refsingar sem álitsaðili X lagði til
> - álitsaðili X afturkallaði viðurkenningu á eignarrétti brotamannsins að vissu marki
>
> Það er undir hverjum og einum komið að safna tiltækum upplýsingum um mótaðilann og meta áhættuna eftir eigin óskum.

![HVAÐ GETUR ÞÚ SKRÁÐ Í NETIÐ?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Hvort upplýsingar um þig birtast í netinu veltur eingöngu á þinni eigin hegðun.
> Þú þarft aldrei að ganga í slíkt net, en samt geta upplýsingar um þig birst í því. Það veltur eingöngu á gjörðum þínum og þeim áhrifum sem þær hafa á aðra.

![SAMFÉLAGIÐ GETUR OPNAÐ EITT FYRIR ÞIG](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Það sem ég hef nú brugðið stuttlega upp mynd af er hvernig samfélagsnet innblásið af dreifstýrðu auðkenni (DID) gæti virkað. Megintilgangur DID-hugmyndanna er að styrkja friðhelgi einkalífs og frelsi með þeirri meginreglu að gerast áskrifandi að þeim reglum sem ég mun fylgja og lifa eftir — með því að gefa notendum getuna til að ákveða hvaða upplýsingum þeir deila og við hvaða skilyrði.

Ég legg til að tengja DID enn frekar saman í samskiptanet þar sem handhafar þeirra skiptast á endurgjöf, jafnvel umfram þær aðstæður þar sem eitthvað hefur hent einhvern og samfélagið eða einstaklingur þarf að bregðast við. Slíkur fyrirbyggjandi samanburður á þeim reglum sem við höfum skráð okkur fyrir — með þeim möguleika að reikna út efnahagslegar og aðrar afleiðingar gagnkvæmra frávika í væntingum um hvernig hinn aðilinn eigi að starfa — mætti telja hvatningu til að finna samstöðu. Í stað frelsis myndi slíkt kerfi leggja áherslu á sjálfviljuga ákvarðanatöku ásamt ábyrgð á hegðun í raunheimi.

Einstaklingur getur ekki brotið kerfið einn — hópur fólks á meiri möguleika, og hópur fólks með umsamda samstöðu og hvata til að draga saman á mörgum málum á enn meiri möguleika á að standast forræðishneigðir. Forsendan um samtök úr fyrsta kaflanum verður uppfyllt þegar tvö skilyrði eru til staðar: DID-orðsporsnetið nær yfir samfélög nægilega vel til að notkun þess hætti að vera framandi. Og á sama tíma verður þessi samfélagshluti efnahagslega mikilvægur minnihluti sem getur samið af festu við afganginn af samfélaginu.

> [!note] Sjálfviljugheit gegn frelsi
> Frelsi — í jákvæðri merkingu — væri aukaáhrif þess að vega saman tvo þætti: sjálfviljugheit og þrýsting umhverfisins í átt til ábyrgðar.

> [!note] Tímabil gervigreindar og gildi orðspors
> Á tímabili gervigreindar er allt sem tengist hugrænni hugsun sjálfvirknivætt — og það gæti gengið enn lengra. Hvað stendur þá eftir í mannlegri starfsemi sem samkeppnisforskot? Svarið er erfitt, og eitthvað mun áreiðanlega finnast, en eitt getum við sagt með vissu: orðspor mun ráða úrslitum. Staðfestanleg saga um hegðun þína, skuldbindingar þínar og efndir þeirra — það er eitthvað sem gervigreind mun ekki byggja upp fyrir þig.

![GERVIGREIND GETUR EKKI BYGGT UPP ORÐSPOR ÞITT — AÐEINS ÞÚ GETUR ÞAÐ](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![HAGFRÆÐI SANNLEIKANS](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
