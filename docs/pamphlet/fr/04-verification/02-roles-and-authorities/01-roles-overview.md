---
title: "Vue d’ensemble des rôles"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Vue d’ensemble des rôles

Nous avons déjà brièvement abordé certains de ces rôles dans le chapitre sur le réseau et ses propriétés fondamentales. Le moment est venu de les examiner à nouveau, plus en détail, et d’ajouter les rôles supplémentaires dont nous avons besoin pour rendre le réseau plus robuste. Chaque transaction de vérification implique plusieurs rôles — voyons comment ils se comportent.

> [!note] Les rôles dans une transaction de vérification
> Chaque vérification implique jusqu’à six rôles distincts, résumés dans le tableau ci-dessous. Tous peuvent disposer de leur propre DID dans le réseau de réputation décentralisé.

| Rôle | Description |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Émetteur** | La personne qui publie l’information dans le réseau — affirme que quelque chose s’est produit (une DID a été créée, modifiée ou dissoute, une assertion, la politique d’une DID donnée, etc.) |
| **Sujet** | La personne dont parle l’information — le destinataire de l’assertion |
| **Autorité** | Une entité de confiance qui engage son nom sur la qualité de l’assertion, en l’examinant et en passant en revue les preuves présentées ou en les recueillant activement |
| **Observateur** | Un tiers indépendant qui tient un registre de la manière dont le vérificateur traite l’assertion — s’assurant que le vérificateur ne reste ni silencieux ni ne s’écarte de la politique qu’il a déclarée |
| **Vérificateur** | Un participant sélectionné algorithmiquement qui traite la transaction |
| **Délégué** | Une personne agissant au nom d’un autre participant |
