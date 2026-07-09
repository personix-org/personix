---
title: "Consensus and the Verification Process"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# O Consenso e o Processo de Verificação

Para construir consenso sobre quais as regras que uma sociedade deveria, em média, defender e fazer cumprir, o seguinte mecanismo pode ajudar. Enquanto participante DID, declaro as regras a que adiro e pelas quais vou viver, e publico-as. (Pense nelas como os regulamentos e estatutos que, na minha ótica, compõem o meu mundo ideal — um mundo onde não me sinto limitado, mas seguro.)

Consigo estimar antecipadamente como reagiriam os meus contactos DID — e avaliar com que intensidade, e por quem, seria sancionado em interações sociais ou de negócio comuns, caso hipoteticamente ocorressem.

A avaliação definitiva acontece quando pede informação a outra DID, ou lhe pede que verifique uma alegação (ou pede um serviço a uma autoridade, e assim por diante) que quer publicar na rede de reputação. Deveria dar o mesmo resultado que dá quando faz você próprio a avaliação, em simulação, contra a política declarada da contraparte — e, se não der, algo está errado do lado da contraparte: está a tentar jogar um jogo desonesto.

O resultado é ou a aceitação, com um preço cotado pela verificação (no caso dos serviços de verificador ou de autoridade), ou a rejeição. Tanto as sanções como os bónus pelo desvio face à política do avaliador estão incorporados no preço cotado. O requerente decide então se aceita as condições, ou se avança para a ronda seguinte de verificação no algoritmo de afetação — repetindo o processo até ficar satisfeito, ou até a economia tornar inútil continuar.

> [!note] O Grafo Social
> A rede de reputação é, antes de mais, uma rede social. Adiciona contactos — pessoas que consentem na ligação. Elas têm contactos, e esses contactos têm contactos. O algoritmo procura verificadores dentro de uma profundidade configurável (por exemplo, três níveis: os seus contactos diretos, os contactos deles e um nível além). Não é preciso nenhuma blockchain global — a rede forma naturalmente comunidades com sobreposições noutras comunidades.
>
> O algoritmo é não determinístico: faz o hash do seu documento de alegação, mapeia o hash para uma posição num anel de identidades conhecidas dentro deste círculo, e seleciona a mais próxima como verificador candidato. Não pode prever nem influenciar quem verificará a sua alegação.

Cada rejeição de um verificador aumenta o seu documento e eleva o seu custo de processamento — é o primeiro canal de custo (o crescimento do documento). Cada novo verificador cobra uma taxa baseada no volume de dados, na sua reputação e em quanto o conteúdo da sua alegação se desvia da política de verificação declarada dele — é o segundo canal de custo (o prémio de risco). E cada iteração custa tempo e energia — o terceiro canal de custo.

> [!note] O que o Verificador Verifica, por Ordem
> Uma vez selecionado, um verificador avalia uma alegação em cerca de quatro passos ordenados — os filtros mais baratos primeiro, as verificações de conteúdo dispendiosas por último:
>
> 1. **Filtragem por política.** Este tipo de alegação insere-se sequer naquilo que o verificador publicamente verifica? Se não, o pedido é rejeitado logo à partida.
> 2. **Confiança na autoridade.** Será a autoridade que respaldou a alegação suficientemente digna de confiança segundo a política declarada do próprio verificador? Uma autoridade abaixo do limiar de confiança do verificador é motivo de rejeição, independentemente do conteúdo da alegação.
> 3. **Reputação do emissor.** Cumpre o emissor os limiares de reputação que o verificador declarou para este tipo de alegação? Uma reputação baixa pode elevar a taxa ou desencadear a rejeição.
> 4. **Verificação de conteúdo.** Só quando os três primeiros filtros são ultrapassados é que o verificador avalia a própria alegação — assinaturas, consistência interna, correção formal e quanto se desvia da política do verificador. A taxa cobrada por este último passo reflete o risco efetivamente assumido.
>
> O verificador publica a política que rege cada um destes filtros, pelo que os passos não ficam ao seu critério — está vinculado por aquilo que já declarou. O desvio face à política publicada é, ele próprio, uma alegação publicável contra ele, e paga-a com a sua reputação.

O resultado: publicar uma alegação credível e útil não custa quase nada. Publicar uma alegação radical custa mais. Publicar uma mentira torna-se proibitivamente caro — tem de iterar por verificador após verificador, e cada um que o rejeita acrescenta custos. O mercado põe preço à sua alegação, e o preço diz-lhe onde está em relação às comunidades em que se move.

Não basta declarar que adere a uma regra quando, na verdade, não adere. Nesse caso, a sua DID arrisca a publicação de um registo negativo que expõe a hipocrisia — o que o transforma num risco para todos os outros. O resultado deveria ser menos regras, mas seguidas de forma mais consistente, e uma limpeza daquela selva de leis e regulamentos em que nem os profissionais do direito conseguem navegar.

![HYPOCRISY IS THE MOST EXPENSIVE BEHAVIOR](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Consenso vs Responsabilização
> Para que a rede sirva de fonte valiosa de informação, uma DID não deveria ser demasiado radical — caso contrário os outros rejeitá-la-ão. A pressão social procurará o equilíbrio, e as tentativas de o desestabilizar serão provavelmente castigadas.

![DECLARE YOUR RULES, PAY THE PRICE](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] O Número de Votos Não é o Mesmo que o Peso de uma Voz
> Juraj Karpiš diz que "o dinheiro é a memória das boas ações." Eu acrescentaria que a reputação é a memória das más.
>
> Daqui decorre que, meritocraticamente, quem contribui mais e não tem má reputação merece um maior peso de voz na comunidade. Visto pela lente das relações bilaterais: quando peso quais as pressões de consenso a acomodar, o maior peso vai para as relações de que retiro o maior benefício económico. Dez pessoas com quem não tenho comércio ativo influenciar-me-ão muito menos do que um parceiro de negócios permanente. Este paradigma não se limita ao comércio — estende-se às relações sociais, políticas e outras.
