---
title: "Observateur"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Observateur

Le rôle d’observateur supprime l’incitation du vérificateur à contourner les règles. Dans les situations où un vérificateur n’aime pas la demande de l’émetteur ou de l’autorité, il pourrait simplement rester silencieux — ne pas répondre et bloquer la séquence algorithmique. L’observateur — ou un ensemble d’observateurs — engage sa réputation en documentant la manière dont le vérificateur a été sollicité. Si le vérificateur reste silencieux malgré une politique déclarée qui affirme le contraire, il peut être convaincu d’avoir violé le protocole.

![L’OBSERVATEUR — TIENT UN REGISTRE DU VÉRIFICATEUR](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Le mécanisme : horodatage et code de défi

Avant d’envoyer une assertion au vérificateur, vous la faites transiter par des observateurs — des personnes en qui vous avez confiance, ou des prestataires spécialisés de services d’observation qui facturent de modestes frais. Chaque observateur reçoit votre soumission, l’horodate, signe qu’il l’a vue partir, et génère un code de défi — un hash cryptographique de sa signature. Les codes sont annexés à votre demande. Le vérificateur les voit, mais n’a aucune idée de qui sont les observateurs, ni même si les codes sont réels. Les observateurs agissent ainsi comme des mandataires entre l’émetteur et le vérificateur, détenant un registre indépendant attestant que l’assertion a été soumise et ce qu’elle contenait. Il peut y en avoir de zéro à N.

Lorsque le vérificateur se comporte honnêtement — en acceptant ou en rejetant conformément à sa politique déclarée — les codes restent opaques. Personne n’est exposé.

Mais si le vérificateur reste silencieux malgré une politique accommodante, ou répond d’une manière qui contredit ce qu’il a publié, vous détenez les signatures originales des observateurs. Vous pouvez les publier comme un témoignage par mandataire attestant que l’assertion a été soumise et que le vérificateur n’a pas suivi le protocole. Quiconque peut vérifier que les signatures correspondent aux codes de défi.

## La chute : vous n’avez pas besoin de vrais observateurs

Et voici la partie la plus élégante : **vous n’avez pas besoin de vrais observateurs du tout.** Vous pouvez générer des nombres aléatoires qui ressemblent exactement à des codes de défi. Le vérificateur ne peut pas faire la différence — il doit jouer aux dés pour décider s’il risque sa réputation. Derrière chaque demande qu’il reçoit pourrait se tenir un observateur respecté qui surveille incognito — ou ce pourrait être du pur bruit. Le vérificateur ne le sait pas. Et cette incertitude est le mécanisme.

Le coût du maintien d’une pression honnête : quasi nul (les nombres aléatoires sont gratuits). Le coût potentiel de la malhonnêteté pour le vérificateur : catastrophique. Le comportement honnête est incité même quand personne ne surveille réellement.

Le système fonctionne parce que chacun est un peu paranoïaque. L’incertitude coûte moins cher que la surveillance.

![LE BLUFF QUI GARDE LE VÉRIFICATEUR HONNÊTE](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Plusieurs vérificateurs dans une seule itération
> Une règle compagne renforçant la disponibilité des vérificateurs peut être une extension algorithmique qui renvoie, dans une seule itération, un ensemble de vérificateurs candidats plutôt qu’un seul.
