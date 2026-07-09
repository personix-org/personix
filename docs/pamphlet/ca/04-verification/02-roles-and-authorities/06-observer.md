---
title: "Observer"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Observador

El rol d'observador elimina l'incentiu del verificador per doblegar les regles. En situacions en què a un verificador no li agrada la sol·licitud de l'emissor o de l'autoritat, podria simplement callar: no respondre i bloquejar la seqüència algorísmica. L'observador —o un conjunt d'observadors— posa la seva reputació en joc per documentar com es va interpel·lar el verificador. Si el verificador calla malgrat una política declarada que diu el contrari, se'l pot condemnar per violació del protocol.

![THE OBSERVER — KEEPS A RECORD OF THE VERIFIER](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## El mecanisme: marca de temps i codi de repte

Abans d'enviar una afirmació al verificador, l'encamines a través d'observadors: persones de qui et refies, o proveïdors especialitzats de serveis d'observació que cobren una petita tarifa. Cada observador rep la teva tramesa, hi posa una marca de temps, signa que l'ha vist sortir, i genera un codi de repte: un hash criptogràfic de la seva signatura. Els codis s'afegeixen a la teva sol·licitud. El verificador els veu però no té cap idea de qui són els observadors, ni tan sols si els codis són reals. Els observadors actuen així de proxies entre l'emissor i el verificador, guardant un registre independent que l'afirmació es va presentar i què contenia. Poden ser de zero a N.

Quan el verificador es comporta honestament —acceptant o rebutjant d'acord amb la seva política declarada— els codis resten opacs. Ningú no queda exposat.

Però si el verificador calla malgrat una política acomodatícia, o respon d'una manera que contradiu el que va publicar, tu tens les signatures originals dels observadors. Les pots publicar com a testimoni per procuració que l'afirmació es va presentar i que el verificador no va seguir el protocol. Qualsevol pot verificar que les signatures corresponen als codis de repte.

## El desllorigador: no necessites observadors reals

I aquí ve la part més elegant: **no necessites observadors reals en absolut.** Pots generar nombres aleatoris que semblen exactament codis de repte. El verificador no pot distingir la diferència: ha de jugar-se-la a si arrisca o no la seva reputació. Darrere de cada sol·licitud que rep podria haver-hi un observador respectat mirant d'incògnit, o podria ser pur soroll. El verificador no ho sap. I aquesta incertesa és el mecanisme.

El cost de mantenir una pressió honesta: gairebé zero (els nombres aleatoris són gratis). El cost potencial de la deshonestedat per al verificador: catastròfic. El comportament honest queda incentivat fins i tot quan de fet no mira ningú.

El sistema funciona perquè tothom és una mica paranoic. La incertesa és més barata que la vigilància.

![THE BLUFF THAT KEEPS THE VERIFIER HONEST](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Múltiples verificadors en una sola iteració
> Una regla acompanyant que reforça la disponibilitat de verificadors pot ser una extensió algorísmica que retorni, en una sola iteració, un conjunt de candidats a verificador en comptes d'un de sol.
