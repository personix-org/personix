---
title: "Réseau social fondé sur la réputation"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Réseau social fondé sur la réputation

Pour provoquer le changement, il nous faut un outil soigneusement conçu. Nous allons d’abord l’esquisser brièvement ; dans les chapitres suivants, nous examinerons chaque pièce plus en détail et en ajouterons d’autres. Imaginez un réseau social incensurable, mondial et décentralisé, dans lequel vous pourriez créer et gérer en toute sécurité votre identité mandataire — une identité dite décentralisée (DID). Une DID est une identité numérique que vous créez et contrôlez vous-même, sans dépendre d’aucune autorité centrale. Personne ne peut vous la retirer ni la falsifier, car elle est signée cryptographiquement avec votre clé privée (ou vos clés, via multisig).

> [!note] Note
> Une implication est qu’une telle identité pourrait progressivement remplacer les documents d’identification émis par l’État — mais nous y reviendrons dans le chapitre sur la transition.

![VOTRE IDENTITÉ, VOS CLÉS, VOS RÈGLES](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

Dans un tel réseau, vous pourriez signaler à travers votre identité que quelqu’un vous a causé un préjudice (et plus tard, éventuellement, qu’il l’a réparé ou a été contraint de le faire). Pour que ce retour — dirigé vers l’auteur du préjudice — ait de la valeur en tant que source pertinente, l’inscription d’une information dans le réseau doit coûter du temps, de l’énergie et de l’argent — et par-dessus le marché, une preuve vérifiable doit être produite pour les autres, attestant qu’il ne s’agit pas de bavardage oiseux.

Lire une information serait facile et relativement bon marché, mais créer un enregistrement individuel serait coûteux et exigeant. L’écriture suivrait un protocole clair, dans lequel un calcul selon l’algorithme choisi détermine strictement quelle DID solliciter pour vérifier l’information soumise, et comment procéder pour que le participant sélectionné traite l’information en votre nom, la publie et en devienne le vérificateur.

> [!note] Algorithme vs radicalisme
> La sélection algorithmique des vérificateurs garantit que les émetteurs d’informations non radicales maintiendront, avec le temps, un équilibre quasi neutre entre les coûts des informations publiées et les récompenses pour la vérification.

![PUBLIER COÛTE DU TEMPS, DE L’ÉNERGIE ET DE L’ARGENT](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Voyons comment l’algorithme sélectionne un vérificateur.

> [!note] Algorithme
> La sélection algorithmique choisit de manière non déterministe un vérificateur différent (ou un ensemble de vérificateurs possibles) pour différentes informations. Un hash (une fonction mathématique à sens unique qui produit une « empreinte » unique à partir de n’importe quelle entrée — comme l’empreinte digitale d’un document) du document DID complet détermine la position sur un anneau de hachage cohérent et sélectionne les vérificateurs candidats.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> En clair : l’algorithme prend l’ensemble de votre document DID, en calcule une empreinte, et cette empreinte détermine votre vérificateur.

![COMMENT L’ALGORITHME SÉLECTIONNE VOTRE VÉRIFICATEUR](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Avec le premier vérificateur que l’algorithme sélectionne, vous, en tant qu’émetteur, pouvez ne pas aboutir — votre réputation ou vos paramètres déclarés peuvent ne pas satisfaire ses exigences. Vous poursuivriez algorithmiquement la recherche du suivant en effectuant une nouvelle itération récursive, qui vous attribue un vérificateur supplémentaire. À chaque étape, la « distance » jusqu’au vérificateur cible croît, tout comme les métadonnées d’accompagnement qui doivent être publiées. À mesure que les données croissent, les coûts augmentent naturellement (non seulement à cause de la taille initiale de l’assertion, mais aussi à cause des métadonnées qui s’accumulent à chaque rejet). Une information crédible passe bien plus aisément que des lubies dénuées de sens. Il appartient à chacun de décider quel prix il est prêt à supporter et à quel point l’enregistrement lui importe — le radicalisme finit à coup sûr par coûter cher.

![COMMENT LE VÉRIFICATEUR RÉPOND](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Quoi que le vérificateur décide en réponse à votre demande de vérification, la balle est de nouveau dans le camp de l’émetteur : il peut accepter l’offre de services de vérification du vérificateur, intégrer la réponse dans la chronologie et réessayer (à un coût plus élevé), ou renoncer et encaisser le coût irrécupérable.

![LE CHOIX DE L’ÉMETTEUR](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Pour donner à votre information un poids accru et une meilleure chance d’acceptation auprès des vérificateurs, vous — en tant qu’émetteur ayant un intérêt dans l’information à émettre — pourriez recourir aux services d’une **autorité de confiance**. L’autorité soit rejette l’information soumise, soit l’accepte et engage sa bonne réputation dessus. L’autorité demande généralement des preuves du monde réel, les vérifie et les classe. Le produit est un protocole de son évaluation du cas donné à l’instant donné. Voyez une autorité comme un spécialiste d’un certain type de service, dans le monde réel comme numérique — par exemple un enquêteur, un auditeur, un assureur, un fournisseur d’une certaine classe de biens (en somme, n’importe quel acteur économique du marché).

![COMMENT NAÎT UN ENREGISTREMENT DANS LE RÉSEAU](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Au moment où vous tenterez de publier une information dans le réseau, celui-ci contiendra probablement déjà des informations sur ses acteurs — ce sont des signaux de réputation. Savoir comment lire les signaux de réputation — ce qu’ils signifient pour vous dans différentes situations et quels risques ils comportent — peut ne pas être trivial. Chaque participant peut regarder les enregistrements de réputation différemment à travers sa DID, selon la situation à laquelle il fait face vis-à-vis de sa contrepartie. La contrepartie est-elle un payeur fiable, ou dois-je exiger l’argent d’avance pour une transaction commerciale ? Le produit proposé fait-il l’objet d’avis signalant une fraude ou des défauts cachés ? Cherche-t-elle à se soustraire à sa responsabilité contractuelle lorsque quelque chose tourne mal ? Parfois, une vue plus complexe de la cohérence globale de la contrepartie est utile — cela dépend des préférences de celui qui demande l’aperçu. Le marché pourrait offrir des produits et services qui simplifient, traitent et clarifient la lecture de la réputation dans le contexte de la situation en cause. Diverses autorités et les services qu’elles proposent peuvent aussi servir à cette fin.

![COMMENT SE LIT LA RÉPUTATION](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Exemples
> Les informations qui intéressent typiquement les émetteurs — et qui ont de la valeur pour les autres — concernent des événements dépassant la communication interpersonnelle ordinaire, dans le monde réel ou virtuel.
>
> Exemples négatifs :
> - preuve d’actes criminels (par ex. audités par un organe d’enquête de confiance)
> - preuve indirecte (faible en elle-même, mais statistiquement cumulative) — par ex. présence répétée à proximité de plusieurs vols en peu de temps → toujours une coïncidence ?
> - rupture de contrat
>
> Exemples positifs :
> - préjudice réparé (volontairement ou sous la pression de la communauté à titre de sanction)
> - acceptation et exécution d’une peine proposée par l’autorité X
> - l’autorité X a révoqué la reconnaissance des droits de propriété de l’auteur dans une certaine mesure
>
> Il appartient à chacun de rassembler les informations disponibles sur la contrepartie et d’en évaluer les risques selon ses préférences.

![QUE POUVEZ-VOUS CONSIGNER DANS LE RÉSEAU ?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Le fait que des informations sur vous apparaissent dans le réseau dépend exclusivement de votre propre comportement.
> Vous n’êtes jamais obligé de rejoindre un tel réseau, et pourtant des informations sur vous peuvent tout de même y apparaître. Cela dépend exclusivement de vos actes et de l’impact qu’ils ont sur les autres.

![LA COMMUNAUTÉ PEUT EN OUVRIR UNE POUR VOUS](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Ce que je viens d’esquisser brièvement, c’est la manière dont pourrait fonctionner un réseau social inspiré de l’identité décentralisée (DID). L’objectif premier des concepts de DID est de renforcer la vie privée et la liberté par le principe de souscription aux règles que je vais suivre et selon lesquelles je vais vivre — en donnant aux utilisateurs la capacité de décider quelles informations partager et à quelles conditions.

Je propose de relier davantage les DID en un réseau de communication où leurs détenteurs échangent des retours au-delà même des situations où quelque chose est arrivé à quelqu’un et où la communauté ou un individu doit réagir. Une telle comparaison préventive des règles auxquelles nous avons souscrit — avec la possibilité de calculer les conséquences économiques et autres des écarts mutuels dans nos attentes sur la façon dont l’autre partie devrait opérer — pourrait être considérée comme une motivation à trouver un consensus. Au lieu de la liberté, un tel système mettrait l’accent sur la prise de décision volontaire combinée à la responsabilité du comportement réel.

Un individu ne peut pas briser le système à lui seul — un groupe de personnes a de meilleures chances, et un groupe de personnes disposant d’un consensus négocié et de motivations à tirer dans le même sens sur de nombreux sujets a des chances encore plus grandes de résister aux tendances autoritaires. La condition d’organisation du premier chapitre sera remplie une fois deux conditions réunies : le réseau de réputation DID couvre les communautés de façon suffisamment représentative pour que son usage cesse d’être exotique. Et, en même temps, ce segment communautaire devient une minorité économiquement significative, capable de négocier avec assurance avec le reste de la société.

> [!note] Volontariat vs liberté
> La liberté — au sens positif — serait un effet secondaire de l’équilibrage de deux facteurs : le volontariat et la pression de l’entourage vers la responsabilité.

> [!note] L’ère de l’IA et la valeur de la réputation
> À l’ère de l’intelligence artificielle, tout ce qui touche à la pensée cognitive est en train d’être automatisé — et cela pourrait aller encore plus loin. Que reste-t-il alors, dans l’activité humaine, comme avantage concurrentiel ? La réponse est difficile, et l’on trouvera sûrement quelque chose, mais une chose est certaine : la réputation décidera. Un historique vérifiable de votre comportement, de vos engagements et de leur tenue — voilà quelque chose que l’IA ne bâtira pas à votre place.

![L’IA NE PEUT PAS BÂTIR VOTRE RÉPUTATION — VOUS SEUL LE POUVEZ](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![L’ÉCONOMIE DE LA VÉRITÉ](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
