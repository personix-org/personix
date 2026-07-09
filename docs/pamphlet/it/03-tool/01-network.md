---
title: "Rete sociale basata sulla reputazione"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Rete sociale basata sulla reputazione

Per portare il cambiamento ci serve uno strumento progettato con cura. Prima lo abbozzeremo brevemente; nei capitoli successivi esamineremo ogni pezzo in modo più dettagliato e ne aggiungeremo altri. Immagina una rete sociale incensurabile, globale e decentralizzata in cui tu possa creare e gestire in sicurezza la tua identità delegata — la cosiddetta Identità Decentralizzata (DID). Una DID è un'identità digitale che crei e controlli tu stesso, senza dipendere da alcuna autorità centrale. Nessuno può togliertela o falsificarla, perché è firmata crittograficamente con la tua chiave privata (o chiavi, tramite multisig).

> [!note] Nota
> Un'implicazione è che una simile identità potrebbe gradualmente sostituire i documenti di identità rilasciati dallo Stato — ma di questo parleremo nel capitolo sulla transizione.

![LA TUA IDENTITÀ, LE TUE CHIAVI, LE TUE REGOLE](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

In una simile rete potresti segnalare tramite la tua identità che qualcuno ti ha causato un danno (e, in seguito, eventualmente, che lo ha rimediato o è stato costretto a farlo). Perché questo feedback — rivolto all'autore del danno — abbia valore come fonte rilevante, l'immissione di informazioni nella rete deve costare tempo, energia e denaro — e in più deve essere prodotta una prova verificabile per gli altri che non si tratta di chiacchiere a vuoto.

Leggere le informazioni sarebbe facile e relativamente economico, ma creare un singolo record sarebbe costoso e impegnativo. La scrittura seguirebbe un protocollo chiaro, in cui il calcolo secondo l'algoritmo scelto determina rigorosamente quale DID interpellare per la verifica dell'informazione presentata e come procedere affinché il partecipante selezionato elabori l'informazione per tuo conto, la pubblichi e ne diventi il verificatore.

> [!note] Algoritmo vs radicalismo
> La selezione algoritmica dei verificatori garantisce che i pubblicatori di informazioni non radicali mantengano, nel tempo, un equilibrio pressoché neutro tra i costi delle informazioni pubblicate e le ricompense per la verifica.

![PUBBLICARE COSTA TEMPO, ENERGIA E DENARO](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Vediamo come l'algoritmo seleziona un verificatore.

> [!note] Algoritmo
> La selezione algoritmica sceglie in modo non deterministico un verificatore diverso (o un insieme di possibili verificatori) per diversi frammenti di informazione. Un hash (una funzione matematica unidirezionale che produce un'"impronta" unica a partire da qualsiasi input — come l'impronta digitale di un documento) del documento DID completo determina la posizione su un anello di hash consistente e seleziona i candidati verificatori.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> In parole semplici: l'algoritmo prende il tuo intero documento DID, ne calcola un'impronta, e quell'impronta determina il tuo verificatore.

![COME L'ALGORITMO SELEZIONA IL TUO VERIFICATORE](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Con il primo verificatore che l'algoritmo seleziona, tu come pubblicatore potresti non avere successo — la tua reputazione o le impostazioni dichiarate potrebbero non soddisfare i suoi requisiti. Proseguiresti algoritmicamente la ricerca del successivo eseguendo un'altra iterazione ricorsiva, che ti assegna un ulteriore verificatore. A ogni passo la "distanza" dal verificatore obiettivo cresce, e con essa i metadati di corredo che devono essere pubblicati. Man mano che i dati crescono, i costi naturalmente aumentano (non solo a causa della dimensione iniziale del reclamo, ma anche per i metadati che si accumulano a ogni rifiuto). Un'informazione credibile passa molto più facilmente di capricci privi di senso. Sta a ciascuno decidere quanto è disposto a pagare e quanto gli importa quel record — il radicalismo è garantito che diventi costoso.

![COME RISPONDE IL VERIFICATORE](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Qualunque cosa il verificatore decida in risposta alla tua richiesta di verifica, la palla torna al pubblicatore: può accettare l'offerta del verificatore per i servizi di verifica, ripiegare la risposta nella cronologia e riprovare (a un costo maggiore), oppure andarsene e ingoiare il costo sommerso.

![LA SCELTA DELL'EMITTENTE](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Per dare alla tua informazione maggiore peso e migliori possibilità di accettazione presso i verificatori, tu — come pubblicatore con un interesse nell'informazione emessa — potresti avvalerti dei servizi di un'**autorità di fiducia**. L'autorità o rifiuta l'informazione presentata, oppure la accetta e vi mette in gioco il proprio buon nome (reputazione). L'autorità in genere richiede prove del mondo reale, le verifica e le classifica. L'output è un protocollo della sua valutazione del caso dato in un dato momento. Pensa a un'autorità come a uno specialista di un certo tipo di servizio, sia nel mondo reale sia in quello digitale — per esempio un investigatore, un revisore, un assicuratore, un fornitore di una certa classe di beni (in sostanza, qualsiasi attore economico sul mercato).

![COME NASCE UN RECORD NELLA RETE](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Quando proverai a pubblicare un'informazione nella rete, questa probabilmente conterrà già informazioni sui suoi attori — sono i segnali di reputazione. Orientarsi su come leggere i segnali di reputazione — cosa significano per te in situazioni diverse e quali rischi comportano — potrebbe non essere banale. Ogni partecipante può guardare i record di reputazione in modo diverso attraverso la propria DID, a seconda della situazione che sta affrontando con la controparte. La controparte è un pagatore affidabile, oppure devo pretendere il denaro in anticipo per una transazione commerciale? Il prodotto offerto porta recensioni su frodi o difetti nascosti? Cerca di sottrarsi alla responsabilità contrattuale quando qualcosa va storto? A volte torna utile una visione più complessa della coerenza complessiva della controparte — dipende dalle preferenze di chi richiede il quadro d'insieme. Il mercato potrebbe offrire prodotti e servizi che semplificano, elaborano e chiariscono la lettura della reputazione nel contesto della situazione in questione. Anche varie autorità e i servizi da esse offerti possono servire a questo scopo.

![COME SI LEGGE LA REPUTAZIONE](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Esempi
> Le informazioni tipicamente di interesse per i pubblicatori — e di valore per gli altri — riguardano eventi che vanno oltre l'ordinaria comunicazione interpersonale nel mondo reale o virtuale.
>
> Esempi negativi:
> - prove di atti criminali (per esempio vagliate da un organo investigativo di fiducia)
> - prove indirette (deboli di per sé, ma statisticamente cumulative) — per esempio la presenza ripetuta in prossimità di più furti in breve tempo → ancora una coincidenza?
> - inadempimento contrattuale
>
> Esempi positivi:
> - danno rimediato (volontariamente o sotto la pressione della comunità come punizione)
> - accettazione e scontamento di una pena proposta dall'autorità X
> - l'autorità X ha revocato in una certa misura il riconoscimento dei diritti di proprietà del colpevole
>
> Sta a ciascuno raccogliere le informazioni disponibili sulla controparte e valutare i rischi secondo le proprie preferenze.

![COSA PUOI REGISTRARE NELLA RETE?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Che nella rete compaiano informazioni su di te dipende esclusivamente dal tuo comportamento.
> Non devi mai iscriverti a una simile rete, eppure informazioni su di te potrebbero comunque comparirvi. Dipende esclusivamente dalle tue azioni e dall'impatto che hanno sugli altri.

![LA COMUNITÀ PUÒ APRIRNE UNA PER TE](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Ciò che ho appena abbozzato brevemente è come potrebbe funzionare una rete sociale ispirata all'Identità Decentralizzata (DID). Lo scopo primario dei concetti di DID è rafforzare la privacy e la libertà attraverso il principio di sottoscrivere le regole che seguirò e secondo cui vivrò — dando agli utenti la capacità di decidere quali informazioni condividere e a quali condizioni.

Propongo di collegare ulteriormente le DID in una rete di comunicazione in cui i loro titolari si scambiano feedback anche oltre le situazioni in cui è accaduto qualcosa a qualcuno e la comunità o un individuo deve reagire. Un simile confronto preventivo delle regole che abbiamo sottoscritto — con la possibilità di calcolare le conseguenze economiche e di altro tipo delle reciproche deviazioni nelle aspettative su come dovrebbe operare l'altra parte — potrebbe essere considerato una motivazione per trovare il consenso. Invece della libertà, un simile sistema porrebbe l'accento sulla decisione volontaria unita alla responsabilità per il comportamento nel mondo reale.

Un individuo da solo non può rompere il sistema — un gruppo di persone ha maggiori possibilità, e un gruppo di persone con un consenso negoziato e la motivazione a tirare insieme su molte questioni ha possibilità ancora maggiori di resistere alle tendenze autoritarie. Il presupposto dell'organizzazione del primo capitolo sarà soddisfatto una volta soddisfatte due condizioni: la rete di reputazione DID copre le comunità in modo abbastanza rappresentativo da far sì che il suo uso cessi di essere esotico. E, al tempo stesso, questo segmento di comunità diventa una minoranza economicamente significativa capace di negoziare con assertività con il resto della società.

> [!note] Volontarietà vs libertà
> La libertà — nel senso positivo — sarebbe un effetto secondario del bilanciamento di due fattori: la volontarietà e la pressione dell'ambiente circostante verso la responsabilità.

> [!note] L'era dell'IA e il valore della reputazione
> Nell'era dell'intelligenza artificiale, tutto ciò che è connesso al pensiero cognitivo viene automatizzato — e potrebbe spingersi ancora oltre. Cosa resta allora nell'attività umana come vantaggio competitivo? La risposta è difficile, e qualcosa sicuramente si troverà, ma una cosa possiamo dirla con certezza: deciderà la reputazione. Una storia verificabile del tuo comportamento, dei tuoi impegni e del loro adempimento — è qualcosa che l'IA non costruirà al posto tuo.

![L'IA NON PUÒ COSTRUIRE LA TUA REPUTAZIONE — SOLO TU PUOI](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![L'ECONOMIA DELLA VERITÀ](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
