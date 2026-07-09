---
title: "Verifier"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Vérificateur

N'importe quel DID peut agir comme vérificateur, soit directement, soit par des droits de vérification délégués à un tiers DID. Pour que moi — ou mon délégué — puisse vérifier, je devrais être joignable sur le réseau (en ligne). Tout le monde ne voudra pas s'y engager, et c'est pourquoi un enregistrement DID peut lister, par ordre de priorité, les suppléants qui rempliront la fonction en son nom pendant qu'il est hors ligne.

Chaque DID actif dans le réseau déclare publiquement sa propre politique. À travers les règles définies dans cette politique, il juge, pendant le processus de vérification, la réputation de la contrepartie ainsi que le contenu et la forme de l'assertion que l'émetteur a signalée pour publication dans le réseau de réputation. La formule de calcul servant à calculer les frais des services de vérification fait partie de la politique. Une fois cela en place, à travers un grand nombre statistique d'assertions circulant dans le réseau, j'attends que l'algorithme du réseau me tire du côté de l'émetteur et m'assigne, dans une itération donnée, à vérifier l'information émise. L'émetteur peut calculer à l'avance comment un vérificateur au comportement correct réagirait, mais il ne peut pas éviter de le contacter réellement (lui ou ses suppléants) ; l'itération avec le vérificateur sélectionné doit être menée par l'émetteur même lorsqu'il sait d'avance qu'elle ne passera pas.

Comment sait-on que l'émetteur exécute l'algorithme de sélection du vérificateur sur le bon ensemble de DID candidats vérificateurs ? En même temps que sa politique publiquement déclarée, chaque DID publie aussi la liste courante des identifiants de son réseau social au sein du réseau de réputation. Si un émetteur définit son réseau social comme une bulle sociale qui ne fait qu'écho à ses propres vues et les renforce, l'information publiée à travers lui ne sera guère mieux reçue par les autres communautés. Le fait que je réussisse, à grand coût, à pousser une assertion radicale dans le réseau n'implique pas que, lorsque je jugerai la réputation de la contrepartie, je lui accorderai le moindre poids. Certaines assertions, ma communauté me pousse à les prendre en compte (peines et restrictions imposées aux fautifs) ; d'autres relèvent entièrement de moi — je décide par moi-même de la valeur économique d'inclure ou d'exclure une information donnée.

![LE VÉRIFICATEUR — CHOISI PAR L'ALGORITHME](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
