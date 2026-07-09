---
title: "Authority"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Autorité

L'autorité joue un double rôle : elle peut être un **auditeur** (vérifiant la qualité des preuves avant qu'une assertion soit publiée) ou un **garant** (engageant sa réputation sur la véracité d'une assertion). Dans les deux cas, elle renforce l'assertion de l'émetteur. Ces deux services sont dissociables — une autorité peut offrir l'un, l'autre, ou les deux à la fois. L'hypothèse de travail est que la plupart des services fournis par les autorités peuvent l'être sur une base de marché libre. Cela vaut même dans des domaines qu'on imagine mal privatisés, comme la justice, où des services spécialisés — enquête, évaluation des preuves, jusqu'aux services aujourd'hui fournis par des armées centralisées (planification stratégique, entraînement standardisé, approvisionnement et gestion des stocks, etc.) — peuvent être efficacement livrés par des acteurs du marché. Il n'y a guère de chose qui, après restructuration, ne puisse être rendue plus efficace par les incitations du marché libre.

> [!warning] L'autorité, l'émetteur et l'observateur ne doivent jamais être le vérificateur de leur propre cause.
> La sélection algorithmique du vérificateur garantit l'indépendance. Personne ne peut vérifier sa propre assertion, ou une assertion dans laquelle il a un intérêt direct. C'est une des règles de base que toute la communauté des DID a intérêt à faire respecter.

Les graphiques suivants montrent des vues complémentaires de l'étendue de l'activité que couvrent les autorités (le terme « autorité » peut se lire de façon interchangeable avec « fournisseur de services »).

![L'AUTORITÉ — QUI ENGAGE SON NOM](../../../Info%20Graphics/v5/v5-08d-role-authority.webp)

![LES DEUX VISAGES DE L'AUTORITÉ](../../../Info%20Graphics/v5/v5-08a-autorita-auditor-garant.webp)

> [!note] L'autorité comme observateur incognito
> Une autorité réputée — pense à un notaire dont les affaires reposent uniquement sur son track record — peut, à côté de ses fonctions principales (auditeur / garant), en offrir une troisième : le rôle d'observateur incognito pendant la vérification. Elle tient un registre horodaté de l'assertion soumise pour que le vérificateur ne puisse pas discrètement l'abandonner. Le mécanisme du rôle d'observateur est décrit plus loin, dans la section sur le rôle de l'Observateur.
