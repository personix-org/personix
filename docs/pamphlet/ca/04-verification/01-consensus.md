---
title: "Consensus and the Verification Process"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# El consens i el procés de verificació

Per construir consens sobre quines regles hauria de sostenir i fer complir una societat, de mitjana, pot ajudar el mecanisme següent. Com a participant DID, declaro les regles que subscric i per les quals viuré, i les publico. (Pensa-hi com els estatuts i reglaments que, al meu parer, componen el meu món ideal, un món on no em sento restringit, sinó segur.)

Puc estimar per endavant com reaccionarien els meus contactes DID, i valorar com de fort, i per part de qui, seria sancionat en interaccions socials o comercials ordinàries, si es donessin hipotèticament.

L'avaluació definitiva es produeix quan sol·licites informació a una altra DID, o li demanes que verifiqui una afirmació (o demanes un servei a una autoritat, etcètera) que vols publicar a la xarxa de reputació. Hauria de resultar igual que quan executes l'avaluació tu mateix, en simulació en sec, contra la política declarada de la contrapart, i si no és així, alguna cosa va malament a la banda de la contrapart: està intentant jugar un joc deshonest.

El resultat és o bé l'acceptació, amb un preu cotitzat per a la verificació (en el cas dels serveis de verificador o d'autoritat), o bé el rebuig. Tant les sancions com les bonificacions per la desviació respecte de la política de l'avaluador s'incorporen al preu cotitzat. El sol·licitant aleshores decideix si accepta els termes, o passa a la ronda següent de verificació en l'algorisme d'assignació, repetint el procés fins que quedi satisfet, o fins que l'economia faci que no tingui sentit continuar.

> [!note] The Social Graph
> La xarxa de reputació és, abans de res, una xarxa social. Afegeixes contactes: persones que consenten la connexió. Ells tenen contactes, i aquells contactes tenen contactes. L'algorisme cerca verificadors dins d'una profunditat configurable (p. ex., tres nivells: els teus contactes directes, els seus contactes, i un nivell més enllà). No cal cap cadena de blocs global: la xarxa forma naturalment comunitats amb solapaments cap a altres comunitats.
>
> L'algorisme és no determinista: fa el hash del document de la teva afirmació, mapa el hash a una posició en un anell d'identitats conegudes dins d'aquest cercle, i selecciona la més propera com a candidat a verificador. No pots predir ni influir en qui verificarà la teva afirmació.

Cada rebuig d'un verificador engrandeix el teu document i n'augmenta el cost de processament: aquest és el primer canal de cost (creixement del document). Cada nou verificador cobra una tarifa basada en el volum de dades, la teva reputació i com de lluny s'aparta el contingut de la teva afirmació de la seva política de verificació declarada: aquest és el segon canal de cost (prima de risc). I cada iteració costa temps i energia: aquest és el tercer canal de cost.

> [!note] What the Verifier Checks, in Order
> Un cop seleccionat, un verificador avalua una afirmació en aproximadament quatre passos ordenats: primer els filtres més barats, i al final les comprovacions de contingut més cares:
>
> 1. **Filtre de política.** Aquest tipus d'afirmació entra dins del que el verificador verifica públicament? Si no, la sol·licitud es rebutja d'entrada.
> 2. **Confiança en l'autoritat.** L'autoritat que va avalar l'afirmació és prou de confiança segons la política declarada del verificador? Una autoritat per sota del llindar de confiança del verificador és motiu de rebuig independentment del contingut de l'afirmació.
> 3. **Reputació de l'emissor.** L'emissor compleix els llindars de reputació que el verificador ha declarat per a aquest tipus d'afirmació? Una reputació baixa pot o bé apujar la tarifa o bé provocar el rebuig.
> 4. **Comprovació del contingut.** Només quan les tres primeres barreres passen, el verificador avalua l'afirmació mateixa: signatures, coherència interna, correcció formal, i com de lluny s'aparta de la política del verificador. La tarifa cobrada per aquest darrer pas reflecteix el risc real assumit.
>
> El verificador publica la política que governa cadascuna d'aquestes barreres, de manera que els passos no queden a la seva discreció: està lligat pel que ja ha declarat. La desviació respecte de la política publicada és en si mateixa una afirmació publicable en contra seu, i la paga amb la seva reputació.

El resultat: publicar una afirmació creïble i útil no costa gairebé res. Publicar una afirmació radical costa més. Publicar una mentida esdevé prohibitivament car: has d'iterar verificador rere verificador, i cadascun que et rebutja hi afegeix costos. El mercat posa preu a la teva afirmació, i el preu et diu on estàs situat respecte de les comunitats en què et mous.

No n'hi ha prou de declarar que compleixes una regla quan en realitat no ho fas. En aquest cas, la teva DID s'arrisca a la publicació d'un registre negatiu que exposa la hipocresia, cosa que et converteix en un risc per a tothom. El resultat hauria de ser menys regles però seguides amb més coherència, i una esbrossada d'aquella jungla de lleis i reglaments per la qual fins i tot els professionals del dret amb prou feines es poden orientar.

![HYPOCRISY IS THE MOST EXPENSIVE BEHAVIOR](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Consensus vs Accountability
> Perquè la xarxa serveixi de font d'informació valuosa, una DID no hauria de ser massa radical, altrament la resta la rebutjaran. La pressió social buscarà l'equilibri, i els intents de desestabilitzar-lo probablement seran castigats.

![DECLARE YOUR RULES, PAY THE PRICE](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] El nombre de vots no és el mateix que el pes d'una veu
> Juraj Karpiš diu que «els diners són la memòria de les bones accions». Jo hi afegiria que la reputació és la memòria de les dolentes.
>
> D'aquí es desprèn que, meritocràticament, qui contribueix més i no té mala reputació mereix un pes de veu més gran a la comunitat. Mirat a través de la lent de les relacions bilaterals: quan sospeso quines pressions de consens acomodar, el pes més gran va a les relacions de les quals trec el benefici econòmic més gran. Deu persones amb qui no tinc comerç actiu m'influiran molt menys que un soci comercial permanent. Aquest paradigma no es limita al comerç: s'estén a les relacions socials, polítiques i d'altra mena.
