---
title: "Observer"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Observatören

Observatörsrollen tar bort verifierarens incitament att böja på reglerna. I situationer där en verifierare inte gillar utfärdarens eller auktoritetens begäran skulle de helt enkelt kunna tiga — inte svara, och blockera den algoritmiska sekvensen. Observatören — eller en uppsättning observatörer — sätter sitt anseende på spel för att dokumentera hur verifieraren förfrågades. Om verifieraren tiger trots en deklarerad policy som säger annat, kan de fällas för att ha kränkt protokollet.

![THE OBSERVER — KEEPS A RECORD OF THE VERIFIER](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Mekanismen: tidsstämpel och utmaningskod

Innan du skickar ett påstående till verifieraren dirigerar du det genom observatörer — människor du litar på, eller specialiserade observatörstjänsteleverantörer som tar ut en liten avgift. Varje observatör tar emot din inlämning, tidsstämplar den, signerar att de såg den gå ut, och genererar en utmaningskod — en kryptografisk hash av sin signatur. Koderna fogas till din begäran. Verifieraren ser dem men har ingen aning om vilka observatörerna är, eller om koderna ens är äkta. Observatörer agerar därmed som mellanhänder mellan utfärdaren och verifieraren, och håller en oberoende anteckning om att påståendet lämnades in och vad det innehöll. Det kan finnas noll till N av dem.

När verifieraren beter sig hederligt — accepterar eller avvisar i linje med sin deklarerade policy — förblir koderna ogenomskinliga. Ingen exponeras.

Men om verifieraren tiger trots en tillmötesgående policy, eller svarar på ett sätt som motsäger det de publicerat, håller du de ursprungliga observatörssignaturerna. Du kan publicera dem som ombudsvittnesmål om att påståendet lämnades in och att verifieraren inte följde protokollet. Vem som helst kan verifiera att signaturerna matchar utmaningskoderna.

## Poängen: du behöver inga riktiga observatörer

Och här är den mest eleganta delen: **du behöver inga riktiga observatörer alls.** Du kan generera slumptal som ser ut precis som utmaningskoder. Verifieraren kan inte se skillnaden — de måste slå tärningen om huruvida de ska riskera sitt anseende. Bakom varje begäran de tar emot skulle det kunna finnas en ansedd observatör som tittar på inkognito — eller så kan det vara rent brus. Verifieraren vet inte. Och den osäkerheten är mekanismen.

Kostnaden för att upprätthålla ärligt tryck: nära noll (slumptal är gratis). Den potentiella kostnaden av ohederlighet för verifieraren: katastrofal. Hederligt beteende uppmuntras även när ingen faktiskt tittar.

Systemet fungerar för att alla är lite paranoida. Osäkerhet är billigare än övervakning.

![THE BLUFF THAT KEEPS THE VERIFIER HONEST](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Flera verifierare i en enda iteration
> En förstärkande följeslagarregel för verifierartillgänglighet kan vara en algoritmisk utvidgning som returnerar, i en enda iteration, en uppsättning kandidatverifierare snarare än bara en.
