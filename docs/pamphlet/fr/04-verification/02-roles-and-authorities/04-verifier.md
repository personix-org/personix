---
title: "Vérificateur"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Vérificateur

Toute DID peut agir comme vérificateur, soit directement, soit via des droits de vérification délégués à une DID tierce. Pour que moi — ou mon délégué — puisse vérifier, je devrais être joignable sur le réseau (en ligne). Tout le monde ne voudra pas s’y engager, c’est pourquoi un enregistrement DID peut lister, par ordre de priorité, les suppléants qui exerceront la fonction en son nom pendant qu’elle est hors ligne.

Chaque DID active dans le réseau déclare publiquement sa propre politique. À travers les règles définies dans cette politique, elle juge, pendant le processus de vérification, la réputation de la contrepartie ainsi que le contenu et la forme de l’assertion que l’émetteur a marquée pour publication dans le réseau de réputation. La formule de calcul utilisée pour déterminer les frais des services de vérification fait partie de la politique. Une fois cela en place, alors, sur un nombre statistiquement grand d’assertions circulant dans le réseau, j’attends que l’algorithme du réseau me tire du côté de l’émetteur et m’assigne, dans une itération donnée, à vérifier l’information émise. L’émetteur peut calculer à l’avance comment un vérificateur au comportement correct réagirait, mais ne peut pas éviter de le contacter effectivement (lui ou ses suppléants) ; l’itération avec le vérificateur sélectionné doit être menée par l’émetteur, même lorsqu’il sait d’avance qu’elle n’aboutira pas.

Comment savons-nous que l’émetteur exécute l’algorithme de sélection des vérificateurs sur le bon ensemble de DID vérificatrices candidates ? En même temps que sa politique déclarée publiquement, chaque DID publie aussi la liste courante des identifiants de son réseau social au sein du réseau de réputation. Si un émetteur définit son réseau social comme une bulle sociale qui ne fait que faire écho à ses propres vues et les renforcer, l’information publiée à travers lui ne sera guère mieux reçue par d’autres communautés. Le fait que je parvienne, à grands frais, à pousser une assertion radicale dans le réseau n’implique pas que, lorsque je juge la réputation de la contrepartie, je lui accorderai le moindre poids. Certaines assertions, ma communauté me pousse à en tenir compte (peines et restrictions imposées aux contrevenants) ; d’autres relèvent entièrement de moi — je décide moi-même de la valeur économique d’inclure ou d’exclure une information donnée.

![LE VÉRIFICATEUR — CHOISI PAR L’ALGORITHME](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
