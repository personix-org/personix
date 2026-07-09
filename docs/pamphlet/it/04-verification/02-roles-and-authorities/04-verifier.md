---
title: "Verifier"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Verificatore

Qualsiasi DID può fungere da verificatore, sia direttamente sia tramite diritti di verifica delegati a una terza DID. Perché io — o il mio delegato — possa verificare, dovrei essere raggiungibile sulla rete (online). Non tutti vorranno impegnarsi in questo, ed è per questo che un record DID può elencare, in ordine di priorità, i sostituti che svolgeranno la funzione per suo conto mentre è offline.

Ogni DID attiva nella rete dichiara pubblicamente la propria policy. Attraverso le regole definite in quella policy giudica, durante il processo di verifica, la reputazione della controparte e il contenuto e la forma del reclamo che l'emittente ha segnalato per la pubblicazione nella rete di reputazione. Parte della policy è la formula di calcolo usata per calcolare i compensi per i servizi di verifica. Una volta che questo è in atto, poi, attraverso un numero statisticamente ampio di reclami che scorrono nella rete, attendo che l'algoritmo della rete mi estragga dalla parte dell'emittente e mi assegni, in una data iterazione, a verificare l'informazione emessa. L'emittente può calcolare in anticipo come reagirebbe un verificatore che si comporta correttamente, ma non può evitare di contattarlo effettivamente (o i suoi sostituti); l'iterazione con il verificatore selezionato deve essere eseguita dall'emittente anche quando sa in anticipo che non passerà.

Come sappiamo che l'emittente esegue l'algoritmo di selezione del verificatore sul corretto insieme di DID candidate verificatrici? Insieme alla sua policy pubblicamente dichiarata, ogni DID pubblica anche l'elenco corrente degli identificatori della sua rete sociale all'interno della rete di reputazione. Se un emittente definisce la propria rete sociale come una bolla sociale che si limita a fare eco e a rinforzare le proprie opinioni, le informazioni pubblicate attraverso di essa saranno difficilmente accolte più ampiamente da altre comunità. Il fatto che io riesca, a caro prezzo, a spingere un reclamo radicale nella rete non implica che, nel giudicare la reputazione della controparte, gli darò alcun peso. Alcuni reclami sono spinto dalla mia comunità a prenderli in considerazione (pene e restrizioni imposte ai trasgressori); altri dipendono interamente da me — decido io stesso il valore economico dell'includere o escludere una data informazione.

![IL VERIFICATORE — SCELTO DALL'ALGORITMO](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
