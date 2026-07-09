---
title: "Verifier"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Verificador

Qualquer DID pode atuar como verificador, diretamente ou através de direitos de verificação delegados a uma terceira DID. Para que eu — ou o meu delegado — consiga verificar, devo estar acessível na rede (online). Nem todos vão querer comprometer-se com isso, e é por isso que um registo DID pode listar, por ordem de prioridade, os substitutos que desempenharão a função em seu nome enquanto estiver offline.

Cada DID ativa na rede declara publicamente a sua própria política. Através das regras definidas nessa política, avalia, durante o processo de verificação, a reputação da contraparte e o conteúdo e a forma da alegação que o emissor sinalizou para publicação na rede de reputação. Parte da política é a fórmula de cálculo usada para calcular as taxas dos serviços de verificação. Uma vez isto assente, então, ao longo de um número estatisticamente grande de alegações a fluir pela rede, espero que o algoritmo da rede me puxe para o lado do emissor e me atribua, numa dada iteração, a verificação da informação a ser emitida. O emissor pode calcular antecipadamente como reagiria um verificador de comportamento correto, mas não pode evitar contactá-lo de facto (ou aos seus substitutos); a iteração com o verificador selecionado tem de ser realizada pelo emissor mesmo quando sabe de antemão que não vai passar.

Como sabemos que o emissor corre o algoritmo de seleção de verificador sobre o conjunto correto de DIDs candidatas a verificador? Juntamente com a sua política publicamente declarada, cada DID também publica a lista atual dos identificadores da sua rede social dentro da rede de reputação. Se um emissor definir a sua rede social como uma bolha social que apenas ecoa e reforça as suas próprias visões, a informação publicada através dela dificilmente será recebida mais amplamente por outras comunidades. O facto de eu conseguir, a alto custo, empurrar uma alegação radical para a rede não implica que, ao avaliar a reputação da contraparte, lhe atribua qualquer peso. Algumas alegações sou empurrado pela minha comunidade a tê-las em conta (sentenças e restrições impostas a infratores); outras ficam inteiramente ao meu critério — decido eu próprio o valor económico de incluir ou excluir uma dada peça de informação.

![THE VERIFIER — CHOSEN BY THE ALGORITHM](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
