---
title: "Observer"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Observateur

Le rôle d'observateur retire au vérificateur l'incitation à contourner les règles. Dans les situations où un vérificateur n'aime pas la demande de l'émetteur ou de l'autorité, il pourrait simplement rester silencieux — ne pas répondre, et bloquer la séquence algorithmique. L'observateur — ou un ensemble d'observateurs — engage sa réputation à documenter la façon dont le vérificateur a été interrogé. Si le vérificateur reste silencieux malgré une politique déclarée qui dit le contraire, il peut être convaincu d'avoir violé le protocole.

![L'OBSERVATEUR — TIENT UN REGISTRE DU VÉRIFICATEUR](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Le mécanisme : horodatage et code de défi

Avant d'envoyer une assertion au vérificateur, tu la fais transiter par des observateurs — des gens en qui tu as confiance, ou des fournisseurs spécialisés de services d'observation qui facturent de petits frais. Chaque observateur reçoit ta soumission, l'horodate, signe qu'il l'a vue partir, et génère un code de défi — un hash cryptographique de sa signature. Les codes sont ajoutés à ta demande. Le vérificateur les voit mais n'a aucune idée de qui sont les observateurs, ni même si les codes sont réels. Les observateurs agissent ainsi comme des mandataires entre l'émetteur et le vérificateur, détenant un registre indépendant que l'assertion a été soumise et de ce qu'elle contenait. Il peut y en avoir de zéro à N.

Quand le vérificateur se comporte honnêtement — acceptant ou rejetant conformément à sa politique déclarée — les codes restent opaques. Personne n'est exposé.

Mais si le vérificateur reste silencieux malgré une politique accommodante, ou répond d'une façon qui contredit ce qu'il a publié, tu détiens les signatures originales des observateurs. Tu peux les publier comme témoignage par mandataire que l'assertion a été soumise et que le vérificateur n'a pas suivi le protocole. N'importe qui peut vérifier que les signatures correspondent aux codes de défi.

## La chute : tu n'as pas besoin de vrais observateurs

Et voici la partie la plus élégante : **tu n'as pas du tout besoin de vrais observateurs.** Tu peux générer des nombres aléatoires qui ressemblent exactement à des codes de défi. Le vérificateur ne peut pas faire la différence — il doit jouer aux dés pour savoir s'il risque sa réputation. Derrière chaque demande qu'il reçoit pourrait se cacher un observateur respecté qui surveille incognito — ou ce pourrait être du pur bruit. Le vérificateur ne le sait pas. Et c'est cette incertitude qui est le mécanisme.

Le coût du maintien d'une pression honnête : quasi nul (les nombres aléatoires sont gratuits). Le coût potentiel de la malhonnêteté pour le vérificateur : catastrophique. Le comportement honnête est incité même quand personne ne surveille réellement.

Le système fonctionne parce que tout le monde est un peu paranoïaque. L'incertitude coûte moins cher que la surveillance.

![LE BLUFF QUI GARDE LE VÉRIFICATEUR HONNÊTE](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Plusieurs vérificateurs dans une seule itération
> Une règle compagne qui renforce la disponibilité des vérificateurs peut être une extension algorithmique qui renvoie, dans une seule itération, un ensemble de vérificateurs candidats plutôt qu'un seul.
