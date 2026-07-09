---
title: "Observer"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Observador

O papel de observador retira ao verificador o incentivo para dobrar as regras. Em situações em que um verificador não gosta do pedido do emissor ou da autoridade, poderia simplesmente calar-se — não responder e bloquear a sequência algorítmica. O observador — ou um conjunto de observadores — põe a sua reputação em jogo ao documentar como o verificador foi consultado. Se o verificador se cala apesar de uma política declarada que diz o contrário, pode ser condenado por violar o protocolo.

![THE OBSERVER — KEEPS A RECORD OF THE VERIFIER](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## O mecanismo: carimbo temporal e código de desafio

Antes de enviar uma alegação ao verificador, encaminha-a através de observadores — pessoas em quem confia, ou prestadores especializados de serviços de observação que cobram uma pequena taxa. Cada observador recebe a sua submissão, carimba-a temporalmente, assina que a viu sair e gera um código de desafio — um hash criptográfico da sua assinatura. Os códigos são anexados ao seu pedido. O verificador vê-os, mas não faz ideia de quem são os observadores, ou sequer se os códigos são reais. Os observadores agem assim como intermediários entre o emissor e o verificador, mantendo um registo independente de que a alegação foi submetida e do que continha. Podem ser de zero a N.

Quando o verificador se comporta com honestidade — aceitando ou rejeitando em linha com a sua política declarada —, os códigos permanecem opacos. Ninguém fica exposto.

Mas se o verificador se cala apesar de uma política acomodatícia, ou responde de uma forma que contradiz aquilo que publicou, você detém as assinaturas originais dos observadores. Pode publicá-las como testemunho por procuração de que a alegação foi submetida e de que o verificador não seguiu o protocolo. Qualquer pessoa pode verificar que as assinaturas correspondem aos códigos de desafio.

## O remate: não precisa de observadores reais

E eis a parte mais elegante: **não precisa de observadores reais de todo.** Pode gerar números aleatórios que parecem exatamente códigos de desafio. O verificador não consegue notar a diferença — tem de lançar os dados sobre se arrisca ou não a sua reputação. Por trás de cada pedido que recebe poderia estar um observador respeitado a vigiar incógnito — ou poderia ser puro ruído. O verificador não sabe. E essa incerteza é o mecanismo.

O custo de manter a pressão honesta: quase zero (os números aleatórios são gratuitos). O custo potencial da desonestidade para o verificador: catastrófico. O comportamento honesto é incentivado mesmo quando ninguém está de facto a vigiar.

O sistema funciona porque toda a gente é um pouco paranoica. A incerteza é mais barata do que a vigilância.

![THE BLUFF THAT KEEPS THE VERIFIER HONEST](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Múltiplos verificadores numa única iteração
> Uma regra companheira reforçadora para a disponibilidade de verificadores pode ser uma extensão algorítmica que devolve, numa única iteração, um conjunto de verificadores candidatos em vez de apenas um.
