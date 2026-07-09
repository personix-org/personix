---
title: "Reputation-Based Social Network"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Xarxa social basada en la reputació

Per dur a terme el canvi, necessitem una eina dissenyada amb cura. Primer l'esbossarem breument; en capítols posteriors n'examinarem cada peça amb més detall i n'hi afegirem més. Imagina una xarxa social incensurable, global i descentralitzada on poguessis crear i gestionar amb seguretat la teva identitat delegada: una anomenada Identitat Descentralitzada (DID). Una DID és una identitat digital que crees i controles tu mateix, sense dependre de cap autoritat central. Ningú no la pot prendre ni falsificar, perquè està signada criptogràficament amb la teva clau privada (o claus, mitjançant multisig).

> [!note] Note
> Una implicació és que una identitat així podria substituir gradualment els documents d'identificació emesos per l'estat, però ja en parlarem al capítol sobre la transició.

![YOUR IDENTITY, YOUR KEYS, YOUR RULES](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

En una xarxa així, podries informar a través de la teva identitat que algú t'ha causat un dany (i, més endavant, potencialment, que l'ha reparat o que hi ha estat obligat). Perquè aquesta retroacció —adreçada a l'originador del dany— tingui valor com a font rellevant, introduir informació a la xarxa ha de costar temps, energia i diners, i, a més, cal produir per als altres una prova verificable que no es tracta de xerrameca ociosa.

Llegir informació seria fàcil i relativament barat, però crear un registre individual seria costós i exigent. Escriure seguiria un protocol clar, en què el càlcul segons l'algorisme escollit determina estrictament a quina DID demanar la verificació de la informació presentada i com procedir perquè el participant seleccionat processi la informació en nom teu, la publiqui i n'esdevingui el verificador.

> [!note] Algorithm vs radicalism
> La selecció algorísmica de verificadors assegura que els publicadors d'informació no radicals mantindran, amb el temps, un equilibri gairebé neutre entre els costos de la informació publicada i les recompenses per la verificació.

![PUBLISHING COSTS TIME, ENERGY, AND MONEY](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Vegem com l'algorisme selecciona un verificador.

> [!note] Algorithm
> La selecció algorísmica tria de manera no determinista un verificador diferent (o un conjunt de verificadors possibles) per a peces d'informació diferents. Un hash (una funció matemàtica unidireccional que produeix una «empremta» única a partir de qualsevol entrada, com l'empremta digital d'un document) del document DID complet determina la posició en un anell de hash consistent i selecciona els candidats a verificador.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> En llenguatge planer: l'algorisme pren tot el teu document DID, en calcula una empremta, i aquesta empremta determina el teu verificador.

![HOW THE ALGORITHM SELECTS YOUR VERIFIER](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Amb el primer verificador que l'algorisme seleccioni, tu com a publicador pots no reeixir: la teva reputació o la teva configuració declarada poden no complir els seus requisits. Continuaries algorísmicament la cerca del següent duent a terme una altra iteració recursiva, que t'assigna un altre verificador. A cada pas, la «distància» fins al verificador objectiu creix, i també ho fan les metadades acompanyants que cal publicar. A mesura que les dades creixen, els costos pugen naturalment (no només per la mida inicial de l'afirmació, sinó també per les metadades que s'acumulen a cada rebuig). La informació creïble passa molt més fàcilment que els capricis absurds. Depèn de cadascú fins a quin preu està disposat a suportar i quant li importa el registre: el radicalisme té garantit encarir-se.

![HOW THE VERIFIER ANSWERS](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Sigui el que sigui que decideixi el verificador en resposta a la teva sol·licitud de verificació, la pilota torna al camp del publicador: pot acceptar l'oferta del verificador pels serveis de verificació, incorporar la resposta a la cronologia i tornar-ho a intentar (més car), o plegar i empassar-se el cost enfonsat.

![THE ISSUER'S CHOICE](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Per donar més pes a la teva informació i una millor oportunitat que els verificadors l'acceptin, tu —com a publicador amb un interès que la informació s'emeti— podries utilitzar els serveis d'una **autoritat de confiança**. L'autoritat, o bé rebutja la informació presentada, o bé l'accepta i hi posa en joc el seu bon nom (la seva reputació). L'autoritat sol demanar evidència del món real, la verifica i la classifica. El resultat és un protocol de la seva avaluació del cas concret en el moment concret. Pensa en una autoritat com un especialista en un cert tipus de servei tant al món real com al digital: per exemple un investigador, un auditor, una asseguradora, un proveïdor d'una certa classe de béns (en essència, qualsevol actor econòmic del mercat).

![HOW A RECORD IS CREATED IN THE NETWORK](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Quan intentis publicar informació a la xarxa, probablement ja contindrà informació sobre els seus actors: són els senyals de reputació. Navegar com llegir els senyals de reputació —què signifiquen per a tu en situacions diferents i quins riscos comporten— pot no ser trivial. Cada participant pot mirar els registres de reputació de manera diferent a través de la seva DID, segons la situació que estigui tractant respecte de la contrapart. La contrapart és un pagador fiable, o necessito exigir els diners per endavant per a una transacció comercial? El producte ofert porta ressenyes sobre fraus o defectes amagats? Estan intentant escapolir-se de la responsabilitat contractual quan alguna cosa va malament? De vegades és útil una visió més complexa de la coherència global de la contrapart: depèn de les preferències de qui demana la panoràmica. El mercat podria oferir productes i serveis que simplifiquin, processin i aclareixin la lectura de la reputació en el context de la situació concreta. Diverses autoritats i els seus serveis oferts també poden servir per a aquest propòsit.

![HOW TO READ REPUTATION](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Examples
> La informació típica que interessa als publicadors —i que és valuosa per als altres— fa referència a esdeveniments que van més enllà de la comunicació interpersonal ordinària al món real o virtual.
>
> Exemples negatius:
> - evidència d'actes criminals (p. ex., auditada per un cos investigador de confiança)
> - evidència indirecta (feble per si mateixa, però estadísticament acumulativa): p. ex., presència repetida a prop de diversos robatoris en poc temps → encara és casualitat?
> - incompliment de contracte
>
> Exemples positius:
> - dany reparat (voluntàriament o sota pressió de la comunitat com a càstig)
> - acceptació i compliment d'una pena proposada per l'autoritat X
> - l'autoritat X ha revocat, fins a cert punt, el reconeixement dels drets de propietat de l'infractor
>
> Depèn de cadascú reunir la informació disponible sobre la contrapart i avaluar els riscos segons les seves preferències.

![WHAT CAN YOU RECORD IN THE NETWORK?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Que aparegui informació sobre tu a la xarxa depèn exclusivament del teu propi comportament.
> Mai no has d'unir-te a una xarxa així, i tot i això hi pot aparèixer informació sobre tu. Depèn exclusivament dels teus actes i de l'impacte que tenen sobre els altres.

![THE COMMUNITY CAN OPEN ONE FOR YOU](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

El que acabo d'esbossar breument és com podria funcionar una xarxa social inspirada en la Identitat Descentralitzada (DID). El propòsit primari dels conceptes de DID és reforçar la privacitat i la llibertat a través del principi de subscriure les regles que seguiré i per les quals viuré, donant als usuaris la capacitat de decidir quina informació comparteixen i sota quines condicions.

Proposo connectar més enllà les DID en una xarxa de comunicació on els seus titulars intercanviïn retroacció fins i tot més enllà de les situacions en què li ha passat alguna cosa a algú i la comunitat o un individu necessita reaccionar. Aquesta comparació preventiva de les regles que hem subscrit —amb l'opció de calcular les conseqüències econòmiques i d'altra mena de les desviacions mútues en les expectatives sobre com hauria d'actuar l'altra banda— podria considerar-se una motivació per trobar el consens. En comptes de la llibertat, un sistema així emfatitzaria la presa de decisions voluntària combinada amb la responsabilitat pel comportament al món real.

Un individu no pot trencar el sistema tot sol: un grup de persones té més possibilitats, i un grup de persones amb un consens negociat i motivacions per estirar plegats en molts assumptes té encara més possibilitats de resistir les tendències autoritàries. El requisit d'organització del primer capítol es complirà un cop es donin dues condicions: que la xarxa de reputació DID cobreixi les comunitats de manera prou representativa perquè fer-la servir deixi de ser exòtic. I, alhora, que aquest segment de la comunitat esdevingui una minoria econòmicament significativa capaç de negociar de manera assertiva amb la resta de la societat.

> [!note] Voluntariness vs freedom
> La llibertat —en el sentit positiu— seria un efecte secundari de l'equilibri entre dos factors: la voluntarietat i la pressió de l'entorn cap a la responsabilitat.

> [!note] The AI Era and the Value of Reputation
> En l'era de la intel·ligència artificial, tot allò connectat amb el pensament cognitiu s'està automatitzant, i encara pot anar més enllà. Què queda aleshores en l'activitat humana com a avantatge competitiu? La resposta és difícil, i segur que es trobarà alguna cosa, però una cosa la podem afirmar amb certesa: la reputació decidirà. Un historial verificable del teu comportament, dels teus compromisos i del seu compliment: això és una cosa que la IA no et construirà.

![AI CANNOT BUILD YOUR REPUTATION — ONLY YOU CAN](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![THE ECONOMICS OF TRUTH](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
