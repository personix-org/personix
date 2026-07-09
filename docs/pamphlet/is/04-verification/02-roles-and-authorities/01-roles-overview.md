---
title: "Yfirlit hlutverka"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Yfirlit hlutverka

Við snertum þegar stuttlega á sumum þessara hlutverka í kaflanum um netið og grunneiginleika þess. Nú er kominn tími til að skoða þau aftur nánar og bæta við þeim sem við þurfum til að gera netið traustara. Hver staðfestingarfærsla felur í sér nokkur hlutverk — sjáum hvernig þau haga sér.

> [!note] Hlutverk í staðfestingarfærslu
> Hver staðfesting felur í sér allt að sex aðgreind hlutverk, sem eru tekin saman í töflunni hér að neðan. Þau geta öll haft sitt eigið DID í dreifstýrða orðsporsnetinu.

| Hlutverk | Lýsing |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Útgefandi** | Sá sem birtir upplýsingar í netinu — fullyrðir að eitthvað hafi gerst (DID var búið til, breytt eða leyst upp, fullyrðing, stefna tiltekins DID, o.s.frv.) |
| **Viðfang** | Sá sem upplýsingarnar fjalla um — viðtakandi fullyrðingarinnar |
| **Álitsaðili** | Traustur aðili sem leggur nafn sitt að veði fyrir gæðum fullyrðingarinnar með því að rannsaka hana og annaðhvort fara yfir framlögð gögn eða safna þeim með virkum hætti |
| **Eftirlitsaðili** | Óháður þriðji aðili sem heldur skrá yfir það hvernig staðfestingaraðilinn fer með fullyrðinguna — sem tryggir að staðfestingaraðilinn hvorki þegi né víki frá þeirri stefnu sem hann lýsti yfir |
| **Staðfestingaraðili** | Þátttakandi valinn með algrími sem vinnur úr færslunni |
| **Umboðsaðili** | Einstaklingur sem kemur fram fyrir hönd annars þátttakanda |
