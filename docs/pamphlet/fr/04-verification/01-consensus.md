---
title: "Le consensus et le processus de vérification"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# Le consensus et le processus de vérification

Pour construire un consensus sur les règles qu’une société devrait, en moyenne, respecter et faire respecter, le mécanisme suivant peut aider. En tant que participant DID, je déclare les règles auxquelles je souscris et selon lesquelles je vivrai, et je les publie. (Voyez cela comme les statuts et le règlement qui, à mes yeux, composent mon monde idéal — un monde où je ne me sens pas restreint, mais en sécurité.)

Je peux estimer à l’avance comment mes contacts DID réagiraient — et évaluer avec quelle force, et par qui, je serais sanctionné dans des interactions sociales ou commerciales ordinaires, si elles devaient hypothétiquement survenir.

L’évaluation définitive se produit lorsque vous demandez une information à une autre DID, ou lui demandez de vérifier une assertion (ou demandez un service à une autorité, et ainsi de suite) que vous voulez publier dans le réseau de réputation. Cela devrait aboutir de la même manière que lorsque vous exécutez l’évaluation vous-même, à blanc, par rapport à la politique déclarée de la contrepartie — et si ce n’est pas le cas, quelque chose cloche du côté de la contrepartie : elle tente de jouer un jeu malhonnête.

Le résultat est soit une acceptation, avec un prix indiqué pour la vérification (dans le cas des services d’un vérificateur ou d’une autorité), soit un rejet. Tant les sanctions que les bonus pour écart par rapport à la politique de l’évaluateur sont intégrés au prix indiqué. Le demandeur décide ensuite d’accepter les conditions, ou de passer à la ronde suivante de vérification dans l’algorithme d’attribution — en répétant le processus jusqu’à satisfaction, ou jusqu’à ce que l’économie rende inutile de continuer.

> [!note] Le graphe social
> Le réseau de réputation est, avant tout, un réseau social. Vous ajoutez des contacts — des personnes qui consentent à la connexion. Elles ont des contacts, et ces contacts ont des contacts. L’algorithme cherche des vérificateurs dans une profondeur configurable (par ex. trois niveaux : vos contacts directs, leurs contacts, et un niveau au-delà). Aucune chaîne de blocs mondiale n’est nécessaire — le réseau forme naturellement des communautés avec des chevauchements vers d’autres communautés.
>
> L’algorithme est non déterministe : il hache votre document d’assertion, projette le hash sur une position d’un anneau d’identités connues au sein de ce cercle, et sélectionne la plus proche comme vérificateur candidat. Vous ne pouvez ni prédire ni influencer qui vérifiera votre assertion.

Chaque rejet d’un vérificateur agrandit votre document et augmente son coût de traitement — c’est le premier canal de coût (croissance du document). Chaque nouveau vérificateur facture des frais fondés sur le volume de données, votre réputation et l’ampleur de l’écart entre le contenu de votre assertion et sa politique de vérification déclarée — c’est le deuxième canal de coût (prime de risque). Et chaque itération coûte du temps et de l’énergie — le troisième canal de coût.

> [!note] Ce que le vérificateur contrôle, dans l’ordre
> Une fois sélectionné, un vérificateur évalue une assertion en gros en quatre étapes ordonnées — les filtres les moins chers d’abord, les contrôles de contenu coûteux en dernier :
>
> 1. **Filtrage par politique.** Ce genre d’assertion entre-t-il seulement dans le champ de ce que le vérificateur vérifie publiquement ? Sinon, la demande est rejetée d’emblée.
> 2. **Confiance dans l’autorité.** L’autorité qui a avalisé l’assertion est-elle suffisamment digne de confiance au regard de la propre politique déclarée du vérificateur ? Une autorité sous le seuil de confiance du vérificateur est un motif de rejet, quel que soit le contenu de l’assertion.
> 3. **Réputation de l’émetteur.** L’émetteur atteint-il les seuils de réputation que le vérificateur a déclarés pour ce type d’assertion ? Une réputation faible peut soit augmenter les frais, soit déclencher un rejet.
> 4. **Contrôle du contenu.** Ce n’est que lorsque les trois premières barrières sont franchies que le vérificateur évalue l’assertion elle-même — signatures, cohérence interne, correction formelle, et ampleur de l’écart par rapport à sa politique. Les frais facturés pour cette dernière étape reflètent le risque réellement pris.
>
> Le vérificateur publie la politique qui régit chacune de ces barrières, de sorte que les étapes ne relèvent pas de son bon vouloir — il est lié par ce qu’il a déjà déclaré. Un écart par rapport à la politique publiée est lui-même une assertion publiable à son encontre, et il la paie de sa réputation.

Le résultat : publier une assertion crédible et utile ne coûte presque rien. Publier une assertion radicale coûte davantage. Publier un mensonge devient prohibitivement cher — vous devez itérer de vérificateur en vérificateur, et chacun qui vous rejette ajoute des coûts. Le marché fixe le prix de votre assertion, et le prix vous dit où vous vous situez par rapport aux communautés dans lesquelles vous évoluez.

Il ne suffit pas de déclarer que vous respectez une règle quand, en réalité, vous ne la respectez pas. Dans ce cas, votre DID risque la publication d’un enregistrement négatif exposant l’hypocrisie — ce qui fait de vous un risque pour tous les autres. Le résultat devrait être des règles moins nombreuses mais plus systématiquement suivies, et un défrichage de cette jungle de lois et de règlements dans laquelle même les professionnels du droit se repèrent à peine.

![L’HYPOCRISIE EST LE COMPORTEMENT LE PLUS CHER](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Consensus vs responsabilité
> Pour que le réseau serve de source d’information précieuse, une DID ne devrait pas être trop radicale — sinon les autres la rejetteront. La pression sociale cherchera l’équilibre, et les tentatives de le déstabiliser seront vraisemblablement punies.

![DÉCLAREZ VOS RÈGLES, PAYEZ LE PRIX](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Le nombre de voix n’est pas la même chose que le poids d’une voix
> Juraj Karpiš dit que « l’argent est la mémoire des bonnes actions ». J’ajouterais que la réputation est la mémoire des mauvaises.
>
> Il s’ensuit que, méritocratiquement, celui qui contribue davantage et n’a pas de mauvaise réputation mérite un plus grand poids de voix dans la communauté. Vu à travers le prisme des relations bilatérales : quand je pèse quelles pressions de consensus accommoder, le plus grand poids revient aux relations dont je tire le plus grand bénéfice économique. Dix personnes avec qui je n’ai aucun échange commercial actif m’influenceront bien moins qu’un partenaire d’affaires permanent. Ce paradigme ne se limite pas au commerce — il s’étend aux relations sociales, politiques et autres.
