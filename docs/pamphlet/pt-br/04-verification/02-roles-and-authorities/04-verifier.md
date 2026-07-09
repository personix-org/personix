---
title: "Verifier"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Verificador

Qualquer DID pode atuar como verificador, seja diretamente, seja por meio de direitos de verificação delegados a uma terceira DID. Para que eu — ou o meu delegado — consiga verificar, eu deveria estar acessível na rede (online). Nem todos vão querer se comprometer com isso, e é por isso que um registro de DID pode listar, em ordem de prioridade, os substitutos que desempenharão a função em seu nome enquanto ela estiver offline.

Toda DID ativa na rede declara publicamente a sua própria política. Por meio das regras definidas nessa política, ela julga, durante o processo de verificação, a reputação da contraparte e o conteúdo e a forma da alegação que o emissor sinalizou para publicação na rede de reputação. Parte da política é a fórmula de cálculo usada para computar as taxas dos serviços de verificação. Uma vez que isso esteja em vigor, ao longo de um número estatisticamente grande de alegações que fluem pela rede, eu espero que o algoritmo da rede me sorteie do lado do emissor e me atribua, numa dada iteração, verificar a informação a ser emitida. O emissor pode calcular de antemão como um verificador que se comporta corretamente reagiria, mas não pode evitar contatá-lo de fato (ou aos seus substitutos); a iteração com o verificador selecionado precisa ser realizada pelo emissor mesmo quando ele sabe de antemão que não vai passar.

Como sabemos que o emissor roda o algoritmo de seleção de verificadores sobre o conjunto correto de DIDs candidatas a verificadora? Junto com a sua política publicamente declarada, toda DID também publica a lista atual dos identificadores da sua rede social dentro da rede de reputação. Se um emissor define a sua rede social como uma bolha social que apenas ecoa e reforça as suas próprias visões, a informação publicada por meio dela dificilmente será recebida de forma mais ampla por outras comunidades. O fato de eu conseguir, a alto custo, empurrar uma alegação radical para dentro da rede não implica que, ao julgar a reputação da contraparte, eu vá lhe dar qualquer peso. Algumas alegações a minha comunidade me pressiona a levar em conta (penas e restrições impostas a infratores); outras ficam inteiramente a meu critério — eu decido por mim mesmo o valor econômico de incluir ou excluir uma dada informação.

![THE VERIFIER — CHOSEN BY THE ALGORITHM](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
