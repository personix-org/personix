---
title: "Délégation"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Délégation

La civilisation a bâti sa croissance économique sur la capacité de division du travail et de spécialisation. Le monde, dans toute sa splendeur, est complexe, et nos chances de le saisir dans toute sa complexité sont proches de zéro. La voie naturelle est de déléguer un large éventail d’activités qui soutiennent une vie confortable à des prestataires spécialisés, qui nous font gagner du temps, de l’énergie et de l’argent, et nous laissent nous spécialiser à notre tour — en fournissant les services que nous savons faire le mieux, ou que le marché valorise le plus chez nous.

La même logique de délégation s’étend au réseau de réputation. Dans le chapitre L’interrupteur liberté–totalitarisme (et la délégation), nous avons exposé les principes de sauvegarde d’une société libre en limitant le nombre d’assertions pouvant être publiées dans le réseau au sein d’une fenêtre de temps donnée (pensez, en termes simplifiés, à quelques droits de publication par an, de sorte que la société reste maximalement libre). Ce principe peut s’étendre à plusieurs dimensions. Nous ne sommes pas obligés de n’avoir qu’un seul nombre — nous pouvons avoir plusieurs limites, s’appliquant à différents types d’assertions. Nous pouvons utiliser un nombre différent pour signaler l’hypocrisie d’autrui que pour les fautes dans les affaires commerciales, et, disons, une modification du document DID comme un changement de mot de passe est une chose dont la communauté ne se souciera guère, et ainsi de suite. Tout dépend de la manière dont la communauté définit, au fil du temps évolutif, ce qui sert ses intérêts pour trouver le bon équilibre entre son niveau cible de liberté et de responsabilité.

Pourquoi le nombre de droits de publication que la communauté m’accorde devrait-il être suffisamment petit ? Signaler une DID (sujet) par une assertion négative détruit une réputation qui a mis longtemps à se construire, et le dommage perdure. Une réputation détruite fait face à une échelle de sanctions croissantes de la part de la communauté pour chaque nouvelle infraction ou récidive, jusqu’à l’élimination complète de l’entité perturbatrice (le cas extrême). Une échelle de punition croissant de façon exponentielle n’a pas besoin d’un grand volume d’assertions, pourvu qu’elles soient étayées par des preuves vérifiables. Cela vaut pour l’état stationnaire paisible, quand la société n’est pas secouée par une catastrophe (externe ou interne).

Pour les événements de très faible probabilité, la fréquence statistique est volatile lorsqu’elle est appliquée à un individu. À l’échelle de la population de la communauté, elle ne l’est pas. C’est là la valeur de déléguer ses droits de publication à des autorités agrégatrices spécialisées, qui — un peu comme une assurance mutuelle en cas de sinistre — utilisent votre droit et l’exercent en votre nom. Parlons de manière moins abstraite et donnons quelques exemples :
- détecter et combattre le crime organisé
- faire respecter les accords commerciaux
- gérer les privilèges (preuves de formation, acquisitions / cessions d’actifs, etc.)
- et ainsi de suite

![LE DÉLÉGUÉ — AGISSANT AU NOM D’UN AUTRE](../../../Info%20Graphics/v5/v5-08h-role-delegate.webp)

> [!note] Comment fonctionnent réellement les « droits de publication »
> Le graphique du délégué représente les droits de publication comme des jetons physiques, par souci de clarté, mais dans le système aucun objet de ce genre n’existe. Ce qui se passe réellement est ceci : les politiques des personnes avec qui vous voulez rester en bons termes — votre communauté — s’agrègent en une règle émergente sur le nombre d’assertions par an qu’elles accepteront de vous comme pertinentes avant de commencer à vous traiter comme du bruit. Le plafond existe pour que le réseau ne soit pas noyé sous des assertions triviales du type « et si », et qu’il reste aussi libre que la communauté le souhaite (le signal préservé en limitant le volume).
>
> Vous lisez ce que votre communauté vous autorise. Il y a une fourchette, avec une certaine dispersion selon les personnes auxquelles vous accordez le plus de poids. Vous décidez ensuite — dans le cadre de cette allocation — combien d’assertions publier vous-même, et combien déléguer à des services professionnels qui publieront en votre nom uniquement lorsque des événements entrent dans leur champ. C’est ce qui vous maintient en bons termes sans vous forcer à déposer une assertion pour chaque petite chose qui vous arrive.
>
> Les « jetons » du graphique sont une représentation visuelle de cette boucle lire-et-décider, non un artefact littéral.

Il est utile de pouvoir révoquer les droits de publication délégués dans le réseau de réputation. Cela peut se faire à tout moment, tant que le délégué n’a pas encore utilisé le droit délégué.
