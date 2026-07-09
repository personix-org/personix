---
title: "Staðfestingaraðili"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Staðfestingaraðili

Hvaða DID sem er getur gegnt hlutverki staðfestingaraðila, annaðhvort beint eða í gegnum staðfestingarréttindi sem framseld eru til þriðja DID. Til að ég — eða umboðsaðili minn — geti staðfest, ætti ég að vera aðgengilegur á netinu (tengdur). Ekki allir munu vilja skuldbinda sig til þess, og þess vegna getur DID-færsla talið upp, í forgangsröð, þá staðgengla sem sinna hlutverkinu fyrir hennar hönd meðan hún er ótengd.

Hvert DID sem er virkt í netinu lýsir opinberlega yfir sinni eigin stefnu. Í gegnum reglurnar sem skilgreindar eru í þeirri stefnu metur það, meðan á staðfestingarferlinu stendur, orðspor mótaðilans og efni og form fullyrðingarinnar sem útgefandinn hefur merkt til birtingar í orðsporsnetinu. Hluti af stefnunni er útreikningsformúlan sem notuð er til að reikna gjöld fyrir staðfestingarþjónustu. Þegar það er komið á sinn stað, þá bíð ég — yfir tölfræðilega stóran fjölda fullyrðinga sem flæða um netið — eftir því að algrím netsins dragi mig fram á hlið útgefandans og feli mér, í tiltekinni ítrun, að staðfesta upplýsingarnar sem verið er að gefa út. Útgefandinn getur reiknað fyrirfram hvernig rétt hegðandi staðfestingaraðili myndi bregðast við, en getur ekki komist hjá því að hafa raunverulega samband við hann (eða staðgengla hans). Ítrunina með völdum staðfestingaraðila verður útgefandinn að framkvæma jafnvel þegar hann veit fyrirfram að hún muni ekki standast.

Hvernig vitum við að útgefandinn keyrir algrímið sem velur staðfestingaraðila yfir rétta mengið af DID-um sem koma til greina sem staðfestingaraðilar? Samhliða opinberlega yfirlýstri stefnu sinni birtir hvert DID einnig núverandi lista yfir auðkenni samfélagsnets síns innan orðsporsnetsins. Ef útgefandi skilgreinir samfélagsnet sitt sem félagslega bólu sem aðeins bergmálar og styrkir eigin sjónarmið, munu upplýsingar birtar í gegnum hann varla berast víðar til annarra samfélaga. Sú staðreynd að mér tekst, gegn háum kostnaði, að ýta öfgakenndri fullyrðingu inn í netið felur ekki í sér að ég muni, þegar ég met orðspor mótaðilans, gefa henni nokkurt vægi. Sumar fullyrðingar ýtir samfélag mitt mér til að taka til greina (dómar og takmarkanir lagðar á brotamenn). Aðrar eru algjörlega undir mér komnar — ég ákveð sjálfur efnahagslegt gildi þess að taka tiltekna upplýsingu með eða sleppa henni.

![STAÐFESTINGARAÐILINN — VALINN AF ALGRÍMINU](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
