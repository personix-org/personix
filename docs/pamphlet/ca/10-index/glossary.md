---
title: "Glossary"
part: "Appendix"
lang: en
version: v6
---

# Glossari

| Terme | Català | Significat |
|------|-------|---------|
| **Authority** | Autoritat | Una entitat de confiança (persona, organització) que verifica informació i hi posa la seva reputació en joc. Pot ser especialitzada (investigadora, jurídica, tècnica). |
| **Claim** | Afirmació | En general: qualsevol declaració verificable. Aquí: un registre publicat a la xarxa de reputació, una asseveració sobre un esdeveniment, una propietat o una relació que està signada criptogràficament i verificada. P. ex., «sóc resident del municipi X» o «aquesta persona ha incomplert un contracte». |
| **Compartmentalization** | Compartimentació | En general: separar la informació en unitats aïllades de manera que exposar una unitat no comprometi les altres. Un principi conegut dels serveis d'intel·ligència. Aquí: identitats DID paral·leles en dictadures, comprometre'n una no revela les altres. |
| **Consistent Hash Ring** | Anell de hash | Un mecanisme algorísmic per seleccionar verificadors: una posició a l'anell es determina pel hash del document DID dins del graf social. Assegura una selecció no determinista però verificable. |
| **DID** | DID (Identitat descentralitzada) | Una identitat digital que crees i controles tu mateix, sense una autoritat central. Signada criptogràficament amb la teva clau privada: ningú no la pot revocar ni falsificar. |
| **DID Document** | Document DID | Un fitxer de dades disponible públicament que descriu la teva identitat DID: conté claus públiques, adreces de xarxa i metadades. S'utilitza per verificar la teva identitat a la xarxa. |
| **Due Diligence** | Due diligence | En general: la verificació en profunditat d'una contrapart abans d'entrar en una relació comercial o jurídica, comprovant-ne l'historial, les finances, la reputació i els riscos. Aquí: a la xarxa de reputació, passa més ràpid i més automàticament gràcies a la disponibilitat de registres verificats. |
| **Economic Neutrality Principle** | Principi de neutralitat econòmica | El comportament honest a la xarxa és econòmicament proper a zero: els costos de publicació es retornen com a recompenses de verificació. El comportament deshonest és una pèrdua neta. |
| **Emergent** | Emergent | Que sorgeix espontàniament de les interaccions de parts més simples, sense que ningú el dissenyi ni el dirigeixi. Un vol d'ocells vola en formació sense un pla: la formació emergeix de regles simples seguides per cada individu. |
| **Emergent Social Contract** | Contracte social emergent | Regles de comportament que sorgeixen no des de dalt (la llei) sinó des de baix: de les interaccions repetides i el consens dins d'una comunitat. |
| **ESR** | Registre Electrònic de Despesa | Un sistema proposat per al rastreig transparent de les despeses públiques: cada despesa realitzada de l'estat es casa amb un pagament planificat. Inspirat en l'EET txec, però girat contra l'estat. |
| **Hash** | Hash (empremta) | En general: una funció matemàtica unidireccional que produeix una «empremta» única de longitud fixa a partir de qualsevol entrada, com l'empremta digital del document. La mateixa entrada produeix sempre la mateixa sortida, però l'entrada no es pot derivar de la sortida. Aquí: s'utilitza per determinar una posició a l'anell de hash i per verificar la integritat del document. |
| **Just-in-Time Funding** | Finançament just a temps | Finançament de l'estat condicionat a la transparència: els diners flueixen només quan l'estat accepta l'ESR i casa les seves despeses. Una palanca per forçar la cooperació. |
| **Meritocracy** | Meritocràcia | En general: un sistema on la posició es determina pel mèrit real i la capacitat demostrada, no pels títols formals, les connexions o el privilegi heretat. Aquí: la xarxa de reputació afavoreix naturalment els qui contribueixen demostrablement a la comunitat: la seva veu té més pes pel seu historial, no pel càrrec. |
| **Onion Gateway** | Onion gateway | L'adreça de xarxa d'una identitat DID a la xarxa onion. Separada del document DID: es pot canviar sense perdre la identitat (semblant a canviar l'adreça IP darrere d'un domini). |
| **Onion Routing** | Onion routing (Tor) | Un protocol de comunicació que assegura la incensurabilitat de la xarxa. Els missatges s'encripten en capes: cada node en treu una capa però no coneix el camí complet. |
| **Oracle Problem** | Problema de l'oracle | En general: com garantir que les dades que entren en un sistema digital corresponen fidelment al que va passar realment al món físic. El terme s'origina en l'àmbit de la cadena de blocs. Aquí: s'aborda a través d'autoritats que posen la seva reputació en joc com a garantia que un registre digital correspon a la realitat física. |
| **Phenomenological** | Fenomenològic | En general: un enfocament que estudia els fenòmens tal com es manifesten en l'experiència directa, observant què se'n desprèn, sense teories donades per endavant. Aquí: la llibertat, el contracte social i les normes de comportament són fenòmens observats, conseqüències de milers de microinteraccions entre persones, no principis definits des de dalt. |
| **Policy** | Policy (política) | En general: un conjunt de regles o principis que governen el comportament en un context donat. Aquí: cada participant de la xarxa DID declara la seva política, com respon a comportaments concrets dels altres, quines regles segueix i quines penes considera proporcionades. L'agregat de les polítiques forma el contracte social emergent. |
| **Proxy** | Proxy | En general: un substitut o intermediari, un sistema o entitat que actua en nom d'un altre. S'utilitza aquí en dos contextos: (1) l'ESR com a proxy que casa les despeses públiques amb els pagaments planificats; (2) els observadors com a proxy entre el publicador i el verificador en el truc de l'observador. |
| **Publisher** | Publicador | Un participant de la xarxa que crea i publica un registre (una afirmació sobre una injustícia, una reparació, etcètera). Suporta el cost de la publicació. |
| **Reputation-Based Social Network (RSN)** | Xarxa de reputació | Una xarxa social descentralitzada on els participants intercanvien retroacció sobre el comportament al món real. Els registres són costosos de crear, barats de llegir. |
| **Reputation Signal** | Senyal de reputació | Un registre individual a la xarxa: positiu (reparació d'un dany, compliment d'una obligació) o negatiu (injustícia, incompliment de contracte). Acumulativament, els senyals formen un perfil de reputació. |
| **Social Graph** | Graf social | La xarxa dels teus contactes i dels contactes dels teus contactes. L'algorisme cerca verificadors a una profunditat configurable (per exemple, 3 nivells). Sense cadena de blocs global: la xarxa forma naturalment comunitats amb solapaments. |
| **Tax Allocation** | Assignació dels impostos | Un mecanisme pel qual el contribuent decideix on va a parar part dels seus impostos. El percentatge assignable creix any rere any. |
| **Track Record** | Track record (historial) | En general: l'historial de resultats, èxits i fracassos passats d'una persona o organització. Aquí: la suma de totes les interaccions passades d'una identitat DID determinada a la xarxa —afirmacions verificades, registres acceptats i rebutjats— a partir de la qual es deriva la seva reputació. |
| **Verifier** | Verificador | Un participant seleccionat algorísmicament per verificar i publicar un registre. Posa el seu bon nom en joc per la veracitat de la informació. |
