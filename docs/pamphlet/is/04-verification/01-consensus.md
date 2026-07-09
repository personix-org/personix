---
title: "Samstaða og staðfestingarferlið"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# Samstaða og staðfestingarferlið

Til að byggja upp samstöðu um það hvaða reglur samfélag ætti, að meðaltali, að halda uppi og framfylgja, getur eftirfarandi ferli hjálpað. Sem DID-þátttakandi lýsi ég yfir þeim reglum sem ég gerist áskrifandi að og mun lifa eftir, og ég birti þær. (Hugsaðu um það sem samþykktir og lög sem, að mínu mati, mynda minn fullkomna heim — heim þar sem mér finnst ég ekki heftur, heldur öruggur.)

Ég get áætlað fyrirfram hvernig DID-tengiliðir mínir myndu bregðast við — og metið hversu harkalega, og af hverjum, ég yrði beittur viðurlögum í venjulegum félagslegum eða viðskiptalegum samskiptum, ef þau ættu sér stað í hugsanlegu tilviki.

Endanlega matið á sér stað þegar þú biður annað DID um upplýsingar, eða biður það að staðfesta fullyrðingu (eða biður álitsaðila um þjónustu, og svo framvegis) sem þú vilt birta í orðsporsnetinu. Það ætti að koma eins út og þegar þú keyrir matið sjálfur, í þurrkeyrslu, á móti yfirlýstri stefnu mótaðilans — og ef ekki, þá er eitthvað að hjá mótaðilanum: hann er að reyna að spila óheiðarlegan leik.

Niðurstaðan er annaðhvort samþykki, með uppgefnu verði fyrir staðfestingu (í tilviki þjónustu staðfestingaraðila eða álitsaðila), eða höfnun. Bæði viðurlög og umbun fyrir frávik frá stefnu matsaðilans eru felld inn í uppgefna verðið. Beiðandinn ákveður þá hvort hann samþykki skilmálana, eða haldi áfram í næstu umferð staðfestingar í úthlutunaralgríminu — og endurtaki ferlið þar til hann er sáttur, eða þar til efnahagurinn gerir tilgangslaust að halda áfram.

> [!note] Félagsgrafinn
> Orðsporsnetið er fyrst og fremst samfélagsnet. Þú bætir við tengiliðum — fólki sem samþykkir tenginguna. Það á tengiliði, og þeir tengiliðir eiga tengiliði. Algrímið leitar að staðfestingaraðilum innan stillanlegs dýptar (t.d. þriggja stiga: beinir tengiliðir þínir, tengiliðir þeirra, og eitt stig þar umfram). Engin hnattræn bálkakeðja er nauðsynleg — netið myndar eðlilega samfélög með skörun inn í önnur samfélög.
>
> Algrímið er ófyrirsjáanlegt: það reiknar hash af fullyrðingarskjali þínu, varpar hash-inu á staðsetningu á hring þekktra auðkenna innan þessa hóps, og velur það nálægasta sem staðfestingaraðila til greina. Þú getur ekki spáð fyrir um eða haft áhrif á hver mun staðfesta fullyrðingu þína.

Höfnun hvers staðfestingaraðila stækkar skjalið þitt og eykur vinnslukostnað þess — það er fyrsta kostnaðarrásin (stækkun skjals). Hver nýr staðfestingaraðili tekur gjald sem byggist á gagnamagni, orðspori þínu, og hversu langt efni fullyrðingar þinnar víkur frá yfirlýstri staðfestingarstefnu hans — það er önnur kostnaðarrásin (áhættuálag). Og hver ítrun kostar tíma og orku — þriðja kostnaðarrásin.

> [!note] Hvað staðfestingaraðilinn athugar, í röð
> Þegar staðfestingaraðili hefur verið valinn metur hann fullyrðingu í um það bil fjórum röðuðum skrefum — ódýrustu síurnar fyrst, dýrar efnisathuganir síðast:
>
> 1. **Stefnusíun.** Fellur þessi tegund fullyrðingar yfirhöfuð innan þess sem staðfestingaraðilinn staðfestir opinberlega? Ef ekki er beiðninni hafnað umsvifalaust.
> 2. **Traust á álitsaðila.** Er álitsaðilinn sem staðfesti fullyrðinguna nægilega traustur samkvæmt yfirlýstri stefnu staðfestingaraðilans sjálfs? Álitsaðili undir traustsþröskuldi staðfestingaraðilans er ástæða til höfnunar óháð efni fullyrðingarinnar.
> 3. **Orðspor útgefanda.** Uppfyllir útgefandinn þá orðsporsþröskulda sem staðfestingaraðilinn hefur lýst yfir fyrir þessa tegund fullyrðingar? Lágt orðspor getur annaðhvort hækkað gjaldið eða kallað fram höfnun.
> 4. **Efnisathugun.** Aðeins þegar fyrstu þrjú hliðin standast metur staðfestingaraðilinn fullyrðinguna sjálfa — undirskriftir, innra samræmi, formlegan réttleika, og hversu langt hún víkur frá stefnu staðfestingaraðilans. Gjaldið sem tekið er fyrir þetta síðasta skref endurspeglar þá raunverulegu áhættu sem tekin er.
>
> Staðfestingaraðilinn birtir þá stefnu sem stýrir hverju þessara hliða, svo skrefin eru ekki háð geðþótta hans — hann er bundinn af því sem hann hefur þegar lýst yfir. Frávik frá birtri stefnu er sjálft birtanleg fullyrðing gegn honum, og hann borgar fyrir hana með orðspori sínu.

Niðurstaðan: að birta trúverðuga og gagnlega fullyrðingu kostar nánast ekki neitt. Að birta öfgakennda fullyrðingu kostar meira. Að birta lygi verður óheyrilega dýrt — þú verður að ítra í gegnum hvern staðfestingaraðilann á fætur öðrum, og hver sá sem hafnar þér bætir við kostnaði. Markaðurinn verðleggur fullyrðingu þína, og verðið segir þér hvar þú stendur gagnvart þeim samfélögum sem þú ferð um.

Það nægir ekki að lýsa því yfir að þú fylgir reglu þegar þú gerir það í raun ekki. Í því tilviki á DID þitt á hættu birtingu neikvæðrar færslu sem afhjúpar hræsnina — sem gerir þig að áhættu fyrir alla aðra. Niðurstaðan ætti að vera færri en samræmdar fylgt reglur, og hreinsun á þeim frumskógi laga og reglugerða sem jafnvel lögfræðingar rata varla um.

![HRÆSNI ER DÝRASTA HEGÐUNIN](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Samstaða gegn ábyrgðarskyldu
> Til að netið þjóni sem verðmæt heimild upplýsinga ætti DID ekki að vera of öfgakennt — annars munu hin hafna því. Félagslegur þrýstingur mun leita jafnvægis, og tilraunir til að grafa undan því verða líklega refsað.

![LÝSTU YFIR REGLUM ÞÍNUM, BORGAÐU VERÐIÐ](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Fjöldi atkvæða er ekki það sama og vægi raddar
> Juraj Karpiš segir að „peningar séu minning góðra verka." Ég myndi bæta við að orðspor sé minning hinna slæmu.
>
> Af því leiðir að, á grundvelli verðleikaræðis, á sá sem leggur meira af mörkum og hefur ekkert slæmt orðspor skilið meira vægi raddar í samfélaginu. Skoðað í ljósi tvíhliða sambanda: þegar ég veg og met hvaða samstöðuþrýsting ég komi til móts við, fer mesta vægið til þeirra sambanda sem ég hef mestan efnahagslegan ávinning af. Tíu manns sem ég á engin virk viðskipti við munu hafa miklu minni áhrif á mig en einn fastur viðskiptafélagi. Þetta viðmið takmarkast ekki við verslun — það nær til félagslegra, stjórnmálalegra og annarra sambanda.
