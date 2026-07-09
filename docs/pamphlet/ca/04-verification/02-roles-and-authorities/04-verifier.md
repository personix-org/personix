---
title: "Verifier"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Verificador

Qualsevol DID pot actuar de verificador, ja sigui directament o a través de drets de verificació delegats a una tercera DID. Perquè jo —o el meu delegat— pugui verificar, hauria de ser accessible a la xarxa (en línia). No tothom voldrà comprometre's a això, i és per això que un registre DID pot llistar, per ordre de prioritat, els substituts que exerciran la funció en nom seu mentre estigui fora de línia.

Cada DID activa a la xarxa declara públicament la seva pròpia política. A través de les regles definides en aquella política jutja, durant el procés de verificació, la reputació de la contrapart i el contingut i la forma de l'afirmació que l'emissor ha marcat per publicar a la xarxa de reputació. Part de la política és la fórmula de càlcul que s'utilitza per computar les tarifes dels serveis de verificació. Un cop això està en marxa, aleshores, al llarg d'un nombre estadísticament gran d'afirmacions que flueixen per la xarxa, espero que l'algorisme de la xarxa em tregui a mi al costat de l'emissor i m'assigni, en una iteració donada, a verificar la informació que s'està emetent. L'emissor pot calcular per endavant com reaccionaria un verificador que es comportés correctament, però no pot evitar contactar-lo realment (o els seus substituts); la iteració amb el verificador seleccionat l'ha de dur a terme l'emissor fins i tot quan sap per endavant que no passarà.

Com sabem que l'emissor executa l'algorisme de selecció de verificadors sobre el conjunt correcte de DID candidates a verificador? Juntament amb la seva política declarada públicament, cada DID també publica la llista actual d'identificadors de la seva xarxa social dins la xarxa de reputació. Si un emissor defineix la seva xarxa social com una bombolla social que es limita a fer d'eco i a reforçar les seves pròpies opinions, la informació publicada a través seu amb prou feines serà rebuda més àmpliament per altres comunitats. El fet que aconsegueixi, a alt cost, empènyer una afirmació radical a la xarxa no implica que, a l'hora de jutjar la reputació de la contrapart, li doni cap pes. Algunes afirmacions la meva comunitat m'empeny a tenir-les en compte (sentències i restriccions imposades als infractors); d'altres depenen enterament de mi: decideixo per mi mateix el valor econòmic d'incloure o excloure una informació determinada.

![THE VERIFIER — CHOSEN BY THE ALGORITHM](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
