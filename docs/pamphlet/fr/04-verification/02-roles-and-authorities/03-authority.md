---
title: "Autorité"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Autorité

L’autorité joue un double rôle : elle peut être **auditeur** (vérifier la qualité des preuves avant qu’une assertion ne soit publiée) ou **garant** (engager sa réputation sur la véracité d’une assertion). Dans les deux cas, elle renforce l’assertion de l’émetteur. Ces deux services sont dissociables — une autorité peut offrir l’un, l’autre, ou les deux à la fois. L’hypothèse de travail est que la plupart des services fournis par les autorités peuvent être rendus sur une base de marché libre. Cela vaut même dans des domaines qu’on imagine difficilement privatisés, comme la justice, où des services spécialisés — enquête, évaluation des preuves, jusqu’aux services aujourd’hui rendus par les armées centralisées (planification stratégique, entraînement standardisé, achats et gestion des stocks, etc.) — peuvent être efficacement fournis par des acteurs du marché. Il n’y a guère de chose qui, après restructuration, ne pourrait être rendue plus efficace par les incitations du marché libre.

> [!warning] L’autorité, l’émetteur et l’observateur ne doivent jamais être le vérificateur de leur propre cas.
> La sélection algorithmique du vérificateur garantit l’indépendance. Personne ne peut vérifier sa propre assertion, ni une assertion dans laquelle il a un intérêt direct. C’est l’une des règles fondamentales que toute la communauté des DID a intérêt à faire respecter.

Les graphiques suivants montrent des vues complémentaires de l’étendue de l’activité que couvrent les autorités (le terme « autorité » peut se lire de façon interchangeable avec « prestataire de services »).

![L’AUTORITÉ — QUI ENGAGE SON NOM](../../../Info%20Graphics/v5/v5-08d-role-authority.webp)

![LES DEUX VISAGES DE L’AUTORITÉ](../../../Info%20Graphics/v5/v5-08a-autorita-auditor-garant.webp)

> [!note] L’autorité comme observateur incognito
> Une autorité réputée — pensez à un notaire dont l’activité repose uniquement sur son historique — peut, à côté des fonctions principales (auditeur / garant), en offrir une troisième : le rôle d’observateur incognito pendant la vérification. Elle tient un registre horodaté de l’assertion soumise, de sorte que le vérificateur ne puisse pas la laisser tomber en silence. Le mécanisme du rôle d’observateur est décrit plus loin, dans la section sur le rôle de l’Observateur.
