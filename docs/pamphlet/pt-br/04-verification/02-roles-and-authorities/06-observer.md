---
title: "Observer"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Observador

O papel do observador remove o incentivo do verificador de burlar as regras. Em situações em que um verificador não gosta do pedido do emissor ou da autoridade, ele poderia simplesmente ficar em silêncio — não responder e bloquear a sequência algorítmica. O observador — ou um conjunto de observadores — põe a sua reputação em jogo ao documentar como o verificador foi consultado. Se o verificador fica em silêncio apesar de uma política declarada que diz o contrário, ele pode ser condenado por violar o protocolo.

![THE OBSERVER — KEEPS A RECORD OF THE VERIFIER](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## O mecanismo: marca de tempo e código de desafio

Antes de enviar uma alegação ao verificador, você a roteia por observadores — pessoas em quem confia, ou prestadores especializados de serviço de observação que cobram uma pequena taxa. Cada observador recebe a sua submissão, marca a hora dela, assina que a viu sair e gera um código de desafio — um hash criptográfico da sua assinatura. Os códigos são anexados ao seu pedido. O verificador os vê, mas não faz ideia de quem são os observadores, nem se os códigos são sequer reais. Os observadores atuam, assim, como proxies entre o emissor e o verificador, guardando um registro independente de que a alegação foi submetida e do que ela continha. Pode haver de zero a N deles.

Quando o verificador se comporta de forma honesta — aceitando ou rejeitando conforme a sua política declarada —, os códigos permanecem opacos. Ninguém é exposto.

Mas, se o verificador fica em silêncio apesar de uma política acomodatícia, ou responde de uma forma que contradiz o que publicou, você tem em mãos as assinaturas originais dos observadores. Você pode publicá-las como testemunho por procuração de que a alegação foi submetida e de que o verificador não seguiu o protocolo. Qualquer um pode verificar que as assinaturas batem com os códigos de desafio.

## O arremate: você não precisa de observadores reais

E aqui está a parte mais elegante: **você não precisa de observadores reais de forma alguma.** Você pode gerar números aleatórios que parecem exatamente códigos de desafio. O verificador não consegue distinguir — ele tem de jogar nos dados se arrisca ou não a sua reputação. Por trás de cada pedido que ele recebe poderia haver um observador respeitado assistindo incógnito — ou poderia ser puro ruído. O verificador não sabe. E essa incerteza é o mecanismo.

O custo de manter a pressão honesta: quase zero (números aleatórios são de graça). O custo potencial da desonestidade para o verificador: catastrófico. O comportamento honesto é incentivado mesmo quando ninguém está de fato assistindo.

O sistema funciona porque todo mundo é um pouco paranoico. A incerteza é mais barata do que a vigilância.

![THE BLUFF THAT KEEPS THE VERIFIER HONEST](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Vários verificadores numa única iteração
> Uma regra complementar de reforço para a disponibilidade de verificadores pode ser uma extensão algorítmica que retorne, numa única iteração, um conjunto de verificadores candidatos, em vez de apenas um.
