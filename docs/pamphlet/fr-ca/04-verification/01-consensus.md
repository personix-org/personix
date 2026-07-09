---
title: "Consensus and the Verification Process"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# Le consensus et le processus de vérification

Pour bâtir un consensus sur les règles qu'une société devrait, en moyenne, respecter et faire respecter, le mécanisme suivant peut aider. En tant que participant DID, je déclare les règles auxquelles je souscris et selon lesquelles je vivrai, et je les publie. (Vois cela comme les statuts et règlements qui, à mes yeux, composent mon monde idéal — un monde où je ne me sens pas restreint, mais en sécurité.)

Je peux estimer à l'avance comment mes contacts DID réagiraient — et évaluer à quel point, et par qui, je serais sanctionné dans des interactions sociales ou commerciales ordinaires, si elles avaient hypothétiquement lieu.

L'évaluation définitive se produit quand tu demandes de l'information à un autre DID, ou que tu lui demandes de vérifier une assertion (ou que tu demandes un service à une autorité, et ainsi de suite) que tu veux publier dans le réseau de réputation. Cela devrait aboutir de la même façon que lorsque tu exécutes l'évaluation toi-même, à blanc, par rapport à la politique déclarée de la contrepartie — et si ce n'est pas le cas, quelque chose ne va pas du côté de la contrepartie : elle essaie de jouer un jeu malhonnête.

Le résultat est soit une acceptation, avec un prix indiqué pour la vérification (dans le cas des services de vérificateur ou d'autorité), soit un rejet. Tant les sanctions que les primes pour l'écart par rapport à la politique de l'évaluateur sont intégrées au prix indiqué. Le demandeur décide alors s'il accepte les conditions, ou s'il passe au tour de vérification suivant dans l'algorithme d'allocation — répétant le processus jusqu'à satisfaction, ou jusqu'à ce que l'économie rende inutile de continuer.

> [!note] Le graphe social
> Le réseau de réputation est, avant tout, un réseau social. Tu ajoutes des contacts — des gens qui consentent à la connexion. Ils ont des contacts, et ces contacts ont des contacts. L'algorithme cherche des vérificateurs à une profondeur configurable (par ex. trois niveaux : tes contacts directs, leurs contacts, et un niveau au-delà). Aucune chaîne de blocs mondiale n'est nécessaire — le réseau forme naturellement des communautés avec des chevauchements vers d'autres communautés.
>
> L'algorithme est non déterministe : il hache ton document d'assertion, mappe le hash à une position sur un anneau d'identités connues à l'intérieur de ce cercle, et sélectionne la plus proche comme candidat vérificateur. Tu ne peux ni prédire ni influencer qui vérifiera ton assertion.

Chaque rejet d'un vérificateur agrandit ton document et augmente son coût de traitement — c'est le premier canal de coût (croissance du document). Chaque nouveau vérificateur facture des frais fondés sur le volume de données, ta réputation, et l'ampleur de l'écart entre le contenu de ton assertion et sa politique de vérification déclarée — c'est le deuxième canal de coût (prime de risque). Et chaque itération coûte du temps et de l'énergie — le troisième canal de coût.

> [!note] Ce que le vérificateur contrôle, dans l'ordre
> Une fois sélectionné, un vérificateur évalue une assertion en gros en quatre étapes ordonnées — les filtres les moins coûteux d'abord, les vérifications de contenu coûteuses en dernier :
>
> 1. **Filtrage par politique.** Ce type d'assertion entre-t-il seulement dans ce que le vérificateur vérifie publiquement ? Sinon, la demande est rejetée d'emblée.
> 2. **Confiance envers l'autorité.** L'autorité qui a endossé l'assertion est-elle assez digne de confiance selon la politique déclarée du vérificateur ? Une autorité en dessous du seuil de confiance du vérificateur est un motif de rejet, quel que soit le contenu de l'assertion.
> 3. **Réputation de l'émetteur.** L'émetteur atteint-il les seuils de réputation que le vérificateur a déclarés pour ce type d'assertion ? Une réputation faible peut soit majorer les frais, soit déclencher un rejet.
> 4. **Vérification du contenu.** Ce n'est que lorsque les trois premiers filtres sont franchis que le vérificateur évalue l'assertion elle-même — signatures, cohérence interne, exactitude formelle, et ampleur de l'écart par rapport à sa politique. Les frais facturés pour cette dernière étape reflètent le risque réellement pris.
>
> Le vérificateur publie la politique qui régit chacun de ces filtres, de sorte que les étapes ne relèvent pas de son bon vouloir — il est lié par ce qu'il a déjà déclaré. Un écart par rapport à la politique publiée est lui-même une assertion publiable contre lui, et il la paie de sa réputation.

Le résultat : publier une assertion crédible et utile ne coûte presque rien. Publier une assertion radicale coûte plus cher. Publier un mensonge devient prohibitivement coûteux — tu dois itérer de vérificateur en vérificateur, et chacun qui te rejette ajoute des coûts. Le marché tarife ton assertion, et le prix te dit où tu te situes par rapport aux communautés dans lesquelles tu évolues.

Il ne suffit pas de déclarer que tu respectes une règle alors qu'en réalité tu ne la respectes pas. Dans ce cas, ton DID risque la publication d'un enregistrement négatif exposant l'hypocrisie — ce qui fait de toi un risque pour tous les autres. Le résultat devrait être des règles moins nombreuses mais plus systématiquement suivies, et un défrichage de cette jungle de lois et de règlements dans laquelle même les juristes peinent à se retrouver.

![L'HYPOCRISIE EST LE COMPORTEMENT LE PLUS COÛTEUX](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Consensus contre reddition de comptes
> Pour que le réseau serve de source d'information précieuse, un DID ne devrait pas être trop radical — sinon les autres le rejetteront. La pression sociale cherchera l'équilibre, et les tentatives de le déstabiliser seront vraisemblablement punies.

![DÉCLARE TES RÈGLES, PAIE LE PRIX](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Le nombre de votes n'est pas la même chose que le poids d'une voix
> Juraj Karpiš dit que « l'argent est la mémoire des bonnes actions ». J'ajouterais que la réputation est la mémoire des mauvaises.
>
> Il s'ensuit que, méritocratiquement, quiconque contribue davantage et n'a aucune mauvaise réputation mérite un poids de voix plus grand dans la communauté. Vu à travers le prisme des relations bilatérales : quand je pèse quelles pressions consensuelles accommoder, le plus grand poids va aux relations dont je tire le plus grand bénéfice économique. Dix personnes avec qui je n'ai aucun commerce actif m'influenceront bien moins qu'un seul partenaire d'affaires permanent. Ce paradigme ne se limite pas au commerce — il s'étend aux relations sociales, politiques et autres.
