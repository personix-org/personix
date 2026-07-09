---
title: "Roles Overview"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Panoràmica dels rols

Ja hem tocat breument alguns d'aquests rols al capítol sobre la xarxa i les seves propietats bàsiques. Ara és el moment de tornar-los a mirar amb més detall i afegir-hi els addicionals que necessitem per fer la xarxa més robusta. Cada transacció de verificació implica diversos rols: vegem com es comporten.

> [!note] Rols en una transacció de verificació
> Cada verificació implica fins a sis rols diferents, resumits a la taula de sota. Tots ells poden tenir la seva pròpia DID a la xarxa de reputació descentralitzada.

| Rol | Descripció |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Emissor** | La persona que publica informació a la xarxa: afirma que ha passat alguna cosa (una DID es va crear, editar o dissoldre, una afirmació, la política d'una DID determinada, etc.) |
| **Subjecte** | La persona de qui tracta la informació: el destinatari de l'afirmació |
| **Autoritat** | Una entitat de confiança que posa el seu nom en joc per la qualitat de l'afirmació investigant-la i, o bé revisant l'evidència presentada, o bé recollint-la activament |
| **Observador** | Una tercera part independent que porta un registre de com el verificador gestiona l'afirmació, assegurant-se que el verificador ni calla ni s'aparta de la política que va declarar |
| **Verificador** | Un participant seleccionat algorísmicament que processa la transacció |
| **Delegat** | Una persona que actua en nom d'un altre participant |
