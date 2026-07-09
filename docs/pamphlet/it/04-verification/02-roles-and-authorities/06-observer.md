---
title: "Observer"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Osservatore

Il ruolo dell'osservatore elimina l'incentivo del verificatore a piegare le regole. In situazioni in cui a un verificatore non piace la richiesta dell'emittente o dell'autorità, potrebbe semplicemente tacere — non rispondere, e bloccare la sequenza algoritmica. L'osservatore — o un insieme di osservatori — mette in gioco la propria reputazione nel documentare come il verificatore è stato interpellato. Se il verificatore tace nonostante una policy dichiarata che afferma il contrario, può essere condannato per violazione del protocollo.

![L'OSSERVATORE — TIENE TRACCIA DEL VERIFICATORE](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Il meccanismo: marca temporale e codice di sfida

Prima di inviare un reclamo al verificatore, lo instradi attraverso gli osservatori — persone di cui ti fidi, o fornitori specializzati di servizi di osservazione che addebitano un piccolo compenso. Ogni osservatore riceve la tua sottomissione, vi appone una marca temporale, firma di averla vista partire, e genera un codice di sfida — un hash crittografico della propria firma. I codici vengono accodati alla tua richiesta. Il verificatore li vede ma non ha idea di chi siano gli osservatori, né se i codici siano reali. Gli osservatori agiscono così da proxy tra l'emittente e il verificatore, custodendo un record indipendente del fatto che il reclamo è stato sottomesso e di cosa conteneva. Possono essere da zero a N.

Quando il verificatore si comporta onestamente — accettando o rifiutando in linea con la propria policy dichiarata — i codici restano opachi. Nessuno viene esposto.

Ma se il verificatore tace nonostante una policy accomodante, o risponde in un modo che contraddice ciò che ha pubblicato, tu detieni le firme originali degli osservatori. Puoi pubblicarle come testimonianza per procura del fatto che il reclamo è stato sottomesso e che il verificatore non ha seguito il protocollo. Chiunque può verificare che le firme corrispondano ai codici di sfida.

## Il colpo di scena: non ti servono osservatori reali

Ed ecco la parte più elegante: **non ti servono affatto osservatori reali.** Puoi generare numeri casuali che assomigliano esattamente ai codici di sfida. Il verificatore non può distinguere la differenza — deve tirare i dadi sul rischiare o meno la propria reputazione. Dietro ogni richiesta che riceve potrebbe esserci un rispettato osservatore che guarda in incognito — oppure potrebbe essere puro rumore. Il verificatore non lo sa. Ed è quell'incertezza il meccanismo.

Il costo per mantenere una pressione onesta: quasi zero (i numeri casuali sono gratis). Il costo potenziale della disonestà per il verificatore: catastrofico. Il comportamento onesto è incentivato anche quando nessuno sta davvero guardando.

Il sistema funziona perché tutti sono un po' paranoici. L'incertezza è più economica della sorveglianza.

![IL BLUFF CHE TIENE ONESTO IL VERIFICATORE](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Più verificatori in una singola iterazione
> Una regola di rinforzo che accompagna la disponibilità del verificatore può essere un'estensione algoritmica che restituisce, in una singola iterazione, un insieme di candidati verificatori anziché uno solo.
