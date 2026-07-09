---
title: "Eftirlitsaðili"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Eftirlitsaðili

Hlutverk eftirlitsaðilans fjarlægir hvata staðfestingaraðilans til að sveigja reglurnar. Í aðstæðum þar sem staðfestingaraðila líkar ekki beiðni útgefandans eða álitsaðilans gæti hann einfaldlega þagað — ekki svarað, og stíflað algrímsröðina. Eftirlitsaðilinn — eða mengi eftirlitsaðila — leggur orðspor sitt að veði fyrir því að skjalfesta hvernig staðfestingaraðilinn var beðinn. Ef staðfestingaraðilinn þegir þrátt fyrir yfirlýsta stefnu sem segir annað, má sakfella hann fyrir brot á samskiptareglunni.

![EFTIRLITSAÐILINN — HELDUR SKRÁ YFIR STAÐFESTINGARAÐILANN](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Ferlið: tímastimpill og áskorunarkóði

Áður en þú sendir fullyrðingu til staðfestingaraðilans, beinir þú henni í gegnum eftirlitsaðila — fólk sem þú treystir, eða sérhæfða eftirlitsþjónustuveitendur sem taka lítið gjald. Hver eftirlitsaðili tekur við innsendingu þinni, tímastimplar hana, undirritar að hann hafi séð hana fara út, og býr til áskorunarkóða — dulritað hash af undirskrift sinni. Kóðunum er bætt aftan við beiðni þína. Staðfestingaraðilinn sér þá en hefur enga hugmynd um hverjir eftirlitsaðilarnir eru, eða hvort kóðarnir séu yfirleitt raunverulegir. Eftirlitsaðilar virka þannig sem proxy milli útgefandans og staðfestingaraðilans, og halda óháða skrá um að fullyrðingin hafi verið send og hvað hún innihélt. Þeir geta verið frá núll upp í N.

Þegar staðfestingaraðilinn hegðar sér heiðarlega — samþykkir eða hafnar í samræmi við yfirlýsta stefnu sína — haldast kóðarnir ógegnsæir. Enginn er afhjúpaður.

En ef staðfestingaraðilinn þegir þrátt fyrir eftirgefanlega stefnu, eða svarar á hátt sem stangast á við það sem hann birti, þá hefur þú upprunalegu undirskriftir eftirlitsaðilanna. Þú getur birt þær sem staðgengilsvitnisburð um að fullyrðingin hafi verið send og að staðfestingaraðilinn hafi ekki fylgt samskiptareglunni. Hver sem er getur staðfest að undirskriftirnar passi við áskorunarkóðana.

## Aðalatriðið: þú þarft ekki raunverulega eftirlitsaðila

Og hér er glæsilegasti hlutinn: **þú þarft alls ekki raunverulega eftirlitsaðila.** Þú getur búið til slembitölur sem líta nákvæmlega út eins og áskorunarkóðar. Staðfestingaraðilinn getur ekki greint muninn — hann verður að kasta teningnum um það hvort hann áhætti orðspori sínu. Á bak við hverja beiðni sem hann fær gæti verið virtur eftirlitsaðili sem fylgist með undir dulnefni — eða það gæti verið hreinn hávaði. Staðfestingaraðilinn veit það ekki. Og sú óvissa er ferlið sjálft.

Kostnaðurinn við að viðhalda heiðarlegum þrýstingi: nánast enginn (slembitölur eru ókeypis). Hugsanlegur kostnaður óheiðarleika fyrir staðfestingaraðilann: skelfilegur. Heiðarleg hegðun er hvött jafnvel þegar enginn er í raun að fylgjast með.

Kerfið virkar vegna þess að allir eru pínulítið ofsóknaróðir. Óvissa er ódýrari en eftirlit.

![BLÖFFIÐ SEM HELDUR STAÐFESTINGARAÐILANUM HEIÐARLEGUM](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Margir staðfestingaraðilar í einni ítrun
> Styrkjandi fylgiregla fyrir aðgengi staðfestingaraðila getur verið algrímsviðbót sem skilar, í einni ítrun, mengi staðfestingaraðila sem koma til greina í stað aðeins eins.
