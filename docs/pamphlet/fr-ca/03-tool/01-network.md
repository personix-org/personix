---
title: "Réseau social fondé sur la réputation"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Réseau social fondé sur la réputation

Pour provoquer le changement, il nous faut un outil soigneusement conçu. Nous l'esquisserons d'abord brièvement. Dans les chapitres suivants, nous examinerons chaque pièce plus en détail et nous en ajouterons d'autres. Imagine un réseau social incensurable, mondial et décentralisé où tu pourrais créer et gérer en toute sûreté ton identité mandataire — une identité dite décentralisée (DID). Un DID est une identité numérique que tu crées et contrôles toi-même, sans dépendre d'aucune autorité centrale. Personne ne peut te l'enlever ni la falsifier, parce qu'elle est signée cryptographiquement avec ta clé privée (ou tes clés, par multisignature).

> [!note] Note
> Une conséquence est qu'une telle identité pourrait remplacer progressivement les pièces d'identité émises par l'État — mais nous y reviendrons dans le chapitre sur la transition.

![TON IDENTITÉ, TES CLÉS, TES RÈGLES](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

Dans un tel réseau, tu pourrais signaler, par le biais de ton identité, que quelqu'un t'a causé un préjudice (et plus tard, éventuellement, qu'il l'a réparé ou a été contraint de le faire). Pour que ce retour — dirigé vers l'auteur du préjudice — ait de la valeur comme source pertinente, l'entrée d'information dans le réseau doit coûter du temps, de l'énergie et de l'argent — et par-dessus le marché, il faut produire pour les autres une preuve vérifiable qu'il ne s'agit pas de bavardage oiseux.

Lire l'information serait facile et relativement peu coûteux, mais créer un enregistrement individuel serait coûteux et exigeant. L'écriture suivrait un protocole clair, où le calcul selon l'algorithme choisi détermine strictement à quel DID demander la vérification de l'information soumise et comment procéder pour que le participant sélectionné traite l'information en ton nom, la publie et en devienne le vérificateur.

> [!note] Algorithme contre radicalisme
> La sélection algorithmique des vérificateurs garantit que les éditeurs d'information non radicaux maintiendront, avec le temps, un équilibre quasi neutre entre les coûts de l'information publiée et les récompenses de vérification.

![PUBLIER COÛTE DU TEMPS, DE L'ÉNERGIE ET DE L'ARGENT](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Voyons comment l'algorithme sélectionne un vérificateur.

> [!note] Algorithme
> La sélection algorithmique choisit de façon non déterministe un vérificateur différent (ou un ensemble de vérificateurs possibles) pour différentes informations. Un hash (une fonction mathématique à sens unique qui produit une « empreinte » unique à partir de n'importe quelle entrée — comme l'empreinte digitale d'un document) du document DID complet détermine la position sur un anneau de hachage cohérent et sélectionne les candidats vérificateurs.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> En clair : l'algorithme prend ton document DID complet, en calcule une empreinte, et cette empreinte détermine ton vérificateur.

![COMMENT L'ALGORITHME SÉLECTIONNE TON VÉRIFICATEUR](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Avec le premier vérificateur que l'algorithme sélectionne, toi, en tant qu'éditeur, tu peux ne pas aboutir — ta réputation ou tes paramètres déclarés peuvent ne pas satisfaire ses exigences. Tu poursuivrais alors algorithmiquement la recherche du suivant en effectuant une autre itération récursive, qui t'assigne un vérificateur de plus. À chaque étape, la « distance » jusqu'au vérificateur cible grandit, et avec elle les métadonnées d'accompagnement qui doivent être publiées. À mesure que les données croissent, les coûts augmentent naturellement (non seulement à cause de la taille initiale de l'assertion, mais aussi à cause des métadonnées qui s'accumulent à chaque rejet). Une information crédible passe bien plus facilement que des lubies absurdes. C'est à chacun de décider quel prix il est prêt à supporter et à quel point l'enregistrement lui importe — le radicalisme est garanti de coûter cher.

![COMMENT LE VÉRIFICATEUR RÉPOND](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Quoi que décide le vérificateur en réponse à ta demande de vérification, la balle revient dans le camp de l'éditeur : il peut accepter l'offre de services de vérification du vérificateur, intégrer la réponse à la chronologie et réessayer (plus cher), ou renoncer et encaisser la perte irrécupérable.

![LE CHOIX DE L'ÉMETTEUR](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Pour donner plus de poids à ton information et une meilleure chance d'acceptation auprès des vérificateurs, tu pourrais — en tant qu'éditeur ayant un intérêt dans l'information émise — recourir aux services d'une **autorité de confiance**. L'autorité rejette l'information soumise, ou l'accepte et engage son bon nom (sa réputation) dessus. L'autorité demande généralement des preuves du monde réel, les vérifie et les classe. Le résultat est un protocole de son évaluation du cas donné à un moment donné. Vois une autorité comme un spécialiste d'un certain type de service dans le monde réel comme numérique — par exemple un enquêteur, un auditeur, un assureur, un fournisseur d'une certaine catégorie de biens (au fond, n'importe quel acteur économique du marché).

![COMMENT NAÎT UN ENREGISTREMENT DANS LE RÉSEAU](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Au moment où tu essaieras de publier de l'information dans le réseau, celui-ci contiendra probablement déjà de l'information sur ses acteurs — ce sont des signaux de réputation. Savoir lire les signaux de réputation — ce qu'ils signifient pour toi dans différentes situations et quels risques ils comportent — n'est pas forcément trivial. Chaque participant peut regarder les enregistrements de réputation différemment à travers son DID, selon la situation qu'il gère à l'égard de la contrepartie. La contrepartie est-elle un payeur fiable, ou dois-je exiger l'argent d'avance pour une transaction commerciale ? Le produit offert traîne-t-il des avis sur une fraude ou des défauts cachés ? Cherche-t-il à se soustraire à sa responsabilité contractuelle quand quelque chose tourne mal ? Parfois, une vue plus complexe de la cohérence globale de la contrepartie est utile — cela dépend des préférences de qui demande l'aperçu. Le marché pourrait offrir des produits et services qui simplifient, traitent et clarifient la lecture de la réputation dans le contexte de la situation en cause. Diverses autorités et les services qu'elles offrent peuvent aussi servir à cette fin.

![COMMENT SE LIT LA RÉPUTATION](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Exemples
> Les informations qui intéressent typiquement les éditeurs — et qui ont de la valeur pour les autres — concernent des événements dépassant la communication interpersonnelle ordinaire dans le monde réel ou virtuel.
>
> Exemples négatifs :
> - preuves d'actes criminels (par ex. audités par un organisme d'enquête de confiance)
> - preuves indirectes (faibles isolément, mais statistiquement cumulatives) — par ex. présence répétée à proximité de plusieurs vols en peu de temps → toujours une coïncidence ?
> - rupture de contrat
>
> Exemples positifs :
> - préjudice réparé (volontairement ou sous la pression de la communauté à titre de punition)
> - acceptation et exécution d'une peine proposée par l'autorité X
> - l'autorité X a révoqué la reconnaissance des droits de propriété de l'auteur dans une certaine mesure
>
> C'est à chacun de rassembler l'information disponible sur la contrepartie et d'évaluer les risques selon ses préférences.

![QUE PEUX-TU ENREGISTRER DANS LE RÉSEAU ?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Que de l'information sur toi apparaisse ou non dans le réseau dépend exclusivement de ton propre comportement.
> Tu n'es jamais obligé de rejoindre un tel réseau, et pourtant de l'information sur toi peut tout de même y apparaître. Cela dépend exclusivement de tes actes et de l'impact qu'ils ont sur les autres.

![LA COMMUNAUTÉ PEUT EN OUVRIR UN POUR TOI](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Ce que je viens d'esquisser brièvement, c'est comment un réseau social inspiré de l'identité décentralisée (DID) pourrait fonctionner. La finalité première des concepts de DID est de renforcer la vie privée et la liberté par le principe de souscrire aux règles que je suivrai et selon lesquelles je vivrai — en donnant aux utilisateurs la capacité de décider quelle information partager et à quelles conditions.

Je propose de relier davantage les DID en un réseau de communication où leurs détenteurs échangent des retours même au-delà des situations où quelque chose est arrivé à quelqu'un et où la communauté ou un individu doit réagir. Une telle comparaison préventive des règles auxquelles nous avons souscrit — avec la possibilité de calculer les conséquences économiques et autres des écarts mutuels dans les attentes sur la façon dont l'autre partie devrait opérer — pourrait être considérée comme une motivation à trouver le consensus. Au lieu de la liberté, un tel système mettrait l'accent sur la décision volontaire combinée à la responsabilité du comportement dans le monde réel.

Un individu ne peut pas casser le système seul — un groupe de personnes a plus de chances, et un groupe de personnes doté d'un consensus négocié et de motivations à tirer dans le même sens sur beaucoup d'enjeux a encore plus de chances de résister aux tendances autoritaires. Le prérequis d'organisation du premier chapitre sera rempli une fois deux conditions réunies : le réseau de réputation DID couvre les communautés de façon assez représentative pour que son usage cesse d'être exotique. Et en même temps, ce segment communautaire devient une minorité économiquement significative, capable de négocier avec assurance avec le reste de la société.

> [!note] Caractère volontaire contre liberté
> La liberté — au sens positif — serait un effet secondaire de l'équilibre entre deux facteurs : le caractère volontaire et la pression de l'entourage vers la responsabilité.

> [!note] L'ère de l'IA et la valeur de la réputation
> À l'ère de l'intelligence artificielle, tout ce qui est lié à la pensée cognitive est en train d'être automatisé — et cela pourrait aller encore plus loin. Que reste-t-il alors dans l'activité humaine comme avantage compétitif ? La réponse est difficile, et on trouvera sûrement quelque chose, mais une chose est certaine : la réputation décidera. Un historique vérifiable de ton comportement, de tes engagements et de leur accomplissement — voilà quelque chose que l'IA ne bâtira pas à ta place.

![L'IA NE PEUT PAS BÂTIR TA RÉPUTATION — TOI SEUL LE PEUX](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![L'ÉCONOMIE DE LA VÉRITÉ](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
