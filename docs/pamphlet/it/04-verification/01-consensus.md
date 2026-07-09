---
title: "Consensus and the Verification Process"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# Il consenso e il processo di verifica

Per costruire il consenso su quali regole una società dovrebbe, in media, sostenere e far rispettare, può essere d'aiuto il meccanismo seguente. Come partecipante DID, dichiaro le regole che sottoscrivo e secondo cui vivrò, e le pubblico. (Pensale come lo statuto e i regolamenti che, a mio avviso, compongono il mio mondo ideale — un mondo in cui non mi sento limitato, ma al sicuro.)

Posso stimare in anticipo come reagirebbero i miei contatti DID — e valutare quanto fortemente, e da chi, verrei sanzionato in ordinarie interazioni sociali o commerciali, qualora si verificassero ipoteticamente.

La valutazione definitiva avviene quando richiedi informazioni a un'altra DID, o le chiedi di verificare un reclamo (o chiedi un servizio a un'autorità, e così via) che vuoi pubblicare nella rete di reputazione. Dovrebbe risultare uguale a come risulta quando esegui tu stesso la valutazione, in prova a vuoto, rispetto alla politica dichiarata della controparte — e se non è così, qualcosa non va dalla parte della controparte: sta cercando di giocare una partita disonesta.

L'esito è o l'accettazione, con un prezzo quotato per la verifica (nel caso di servizi di verifica o di autorità), oppure il rifiuto. Sia le sanzioni sia i bonus per lo scostamento dalla politica del valutatore sono ripiegati nel prezzo quotato. Il richiedente decide poi se accettare le condizioni, oppure passare al giro successivo di verifica nell'algoritmo di allocazione — ripetendo il processo fino a soddisfazione, o fino a quando l'economia rende inutile continuare.

> [!note] Il grafo sociale
> La rete di reputazione è, prima di tutto, una rete sociale. Aggiungi contatti — persone che acconsentono al collegamento. Loro hanno contatti, e quei contatti hanno contatti. L'algoritmo cerca i verificatori entro una profondità configurabile (per esempio tre livelli: i tuoi contatti diretti, i loro contatti, e un livello oltre). Non serve alcuna blockchain globale — la rete forma naturalmente comunità con sovrapposizioni in altre comunità.
>
> L'algoritmo è non deterministico: applica un hash al documento del tuo reclamo, mappa l'hash a una posizione su un anello di identità note all'interno di questa cerchia, e seleziona come candidato verificatore quella più vicina. Non puoi prevedere né influenzare chi verificherà il tuo reclamo.

Ogni rifiuto di un verificatore ingrandisce il tuo documento e ne aumenta il costo di elaborazione — è il primo canale di costo (crescita del documento). Ogni nuovo verificatore addebita un compenso basato sul volume di dati, sulla tua reputazione e su quanto il contenuto del tuo reclamo si scosta dalla sua politica di verifica dichiarata — è il secondo canale di costo (premio per il rischio). E ogni iterazione costa tempo ed energia — è il terzo canale di costo.

> [!note] Cosa controlla il verificatore, nell'ordine
> Una volta selezionato, un verificatore valuta un reclamo in circa quattro passi ordinati — prima i filtri più economici, per ultimi i controlli di contenuto costosi:
>
> 1. **Filtro di politica.** Questo tipo di reclamo rientra affatto in ciò che il verificatore verifica pubblicamente? In caso contrario, la richiesta viene rifiutata senza altro.
> 2. **Fiducia nell'autorità.** L'autorità che ha avallato il reclamo è abbastanza fidata secondo la politica dichiarata dal verificatore? Un'autorità al di sotto della soglia di fiducia del verificatore è motivo di rifiuto indipendentemente dal contenuto del reclamo.
> 3. **Reputazione dell'emittente.** L'emittente soddisfa le soglie di reputazione che il verificatore ha dichiarato per questo tipo di reclamo? Una reputazione bassa può o alzare il compenso o innescare il rifiuto.
> 4. **Controllo del contenuto.** Solo quando i primi tre filtri passano il verificatore valuta il reclamo in sé — firme, coerenza interna, correttezza formale, e quanto si scosta dalla politica del verificatore. Il compenso addebitato per quest'ultimo passo riflette il rischio effettivamente assunto.
>
> Il verificatore pubblica la politica che governa ciascuno di questi filtri, così che i passi non siano a sua discrezione — è vincolato da ciò che ha già dichiarato. Lo scostamento dalla politica pubblicata è esso stesso un reclamo pubblicabile contro di lui, e lo paga con la propria reputazione.

Il risultato: pubblicare un reclamo credibile e utile non costa quasi nulla. Pubblicare un reclamo radicale costa di più. Pubblicare una menzogna diventa proibitivamente costoso — devi iterare di verificatore in verificatore, e ognuno che ti rifiuta aggiunge costi. Il mercato mette un prezzo al tuo reclamo, e il prezzo ti dice dove ti collochi rispetto alle comunità in cui ti muovi.

Non basta dichiarare di aderire a una regola quando in realtà non lo fai. In quel caso, la tua DID rischia la pubblicazione di un record negativo che smaschera l'ipocrisia — cosa che ti trasforma in un rischio per tutti gli altri. L'esito dovrebbe essere regole meno numerose ma seguite con più coerenza, e uno sfoltimento di quella giungla di leggi e regolamenti in cui persino i professionisti del diritto riescono a malapena a orientarsi.

![L'IPOCRISIA È IL COMPORTAMENTO PIÙ COSTOSO](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Consenso vs responsabilità
> Perché la rete serva da fonte preziosa di informazioni, una DID non dovrebbe essere troppo radicale — altrimenti gli altri la rifiuteranno. La pressione sociale cercherà l'equilibrio, e i tentativi di destabilizzarlo saranno probabilmente puniti.

![DICHIARA LE TUE REGOLE, PAGA IL PREZZO](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Il numero di voti non è la stessa cosa del peso di una voce
> Juraj Karpiš dice che "il denaro è la memoria delle buone azioni." Io aggiungerei che la reputazione è la memoria di quelle cattive.
>
> Ne consegue che, meritocraticamente, chi contribuisce di più e non ha cattiva reputazione merita un maggior peso di voce nella comunità. Vista attraverso la lente dei rapporti bilaterali: quando soppeso a quali pressioni di consenso venire incontro, il peso maggiore va ai rapporti da cui traggo il maggior beneficio economico. Dieci persone con cui non ho alcun commercio attivo mi influenzeranno molto meno di un partner d'affari permanente. Questo paradigma non si limita al commercio — si estende ai rapporti sociali, politici e di altro tipo.
