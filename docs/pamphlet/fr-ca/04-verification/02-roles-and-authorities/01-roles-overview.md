---
title: "Roles Overview"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Aperçu des rôles

Nous avons déjà effleuré certains de ces rôles dans le chapitre sur le réseau et ses propriétés de base. Le moment est venu de les revoir plus en détail et d'ajouter ceux dont nous avons besoin pour rendre le réseau plus robuste. Chaque transaction de vérification met en jeu plusieurs rôles — voyons comment ils se comportent.

> [!note] Les rôles dans une transaction de vérification
> Chaque vérification met en jeu jusqu'à six rôles distincts, résumés dans le tableau ci-dessous. Ils peuvent tous avoir leur propre DID dans le réseau de réputation décentralisé.

| Rôle | Description |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Émetteur** | La personne qui publie de l'information dans le réseau — affirme que quelque chose s'est produit (un DID a été créé, modifié ou dissous, une assertion, la politique d'un DID donné, etc.) |
| **Sujet** | La personne au sujet de laquelle porte l'information — le destinataire de l'assertion |
| **Autorité** | Une entité de confiance qui engage son nom sur la qualité de l'assertion en enquêtant dessus et en examinant les preuves présentées ou en les recueillant activement |
| **Observateur** | Un tiers indépendant qui tient un registre de la façon dont le vérificateur traite l'assertion — s'assurant que le vérificateur ne reste ni silencieux ni ne s'écarte de la politique qu'il a déclarée |
| **Vérificateur** | Un participant sélectionné algorithmiquement qui traite la transaction |
| **Délégué** | Une personne agissant au nom d'un autre participant |
