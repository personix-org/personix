---
title: "Consensus and the Verification Process"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# O Consenso e o Processo de Verificação

Para construir consenso sobre quais regras uma sociedade deveria, em média, sustentar e fazer cumprir, o mecanismo a seguir pode ajudar. Como participante DID, eu declaro as regras que subscrevo e pelas quais vou viver, e as publico. (Pense nisso como os estatutos e regulamentos que, na minha visão, compõem o meu mundo ideal — um mundo em que eu não me sinto restringido, mas seguro.)

Eu consigo estimar de antemão como os meus contatos DID reagiriam — e avaliar com que intensidade, e por quem, eu seria sancionado em interações sociais ou comerciais comuns, caso elas hipoteticamente ocorressem.

A avaliação definitiva acontece quando você solicita informação a outra DID, ou pede a ela que verifique uma alegação (ou pede a uma autoridade um serviço, e assim por diante) que você quer publicar na rede de reputação. O resultado deveria ser o mesmo que quando você mesmo faz a avaliação, em simulação, contra a política declarada da contraparte — e, se não for, algo está errado do lado da contraparte: ela está tentando jogar um jogo desonesto.

O desfecho é ou a aceitação, com um preço cotado pela verificação (no caso de serviços de verificador ou de autoridade), ou a rejeição. Tanto as sanções quanto os bônus por desvio em relação à política do avaliador estão embutidos no preço cotado. O solicitante, então, decide se aceita os termos, ou se avança para a próxima rodada de verificação no algoritmo de alocação — repetindo o processo até ficar satisfeito, ou até que a economia torne inútil continuar.

> [!note] O Grafo Social
> A rede de reputação é, antes de tudo, uma rede social. Você adiciona contatos — pessoas que consentem com a conexão. Elas têm contatos, e esses contatos têm contatos. O algoritmo busca verificadores dentro de uma profundidade configurável (por exemplo, três níveis: os seus contatos diretos, os contatos deles e um nível além). Nenhuma blockchain global é necessária — a rede forma naturalmente comunidades com sobreposições em outras comunidades.
>
> O algoritmo é não determinístico: ele faz o hash do documento da sua alegação, mapeia o hash para uma posição num anel de identidades conhecidas dentro desse círculo e seleciona a mais próxima como candidata a verificadora. Você não consegue prever nem influenciar quem vai verificar a sua alegação.

Cada rejeição de um verificador aumenta o seu documento e eleva o seu custo de processamento — esse é o primeiro canal de custo (crescimento do documento). Cada novo verificador cobra uma taxa com base no volume de dados, na sua reputação e em quanto o conteúdo da sua alegação se desvia da política de verificação declarada dele — esse é o segundo canal de custo (prêmio de risco). E cada iteração custa tempo e energia — o terceiro canal de custo.

> [!note] O Que o Verificador Checa, e em Que Ordem
> Uma vez selecionado, um verificador avalia uma alegação em cerca de quatro passos ordenados — os filtros mais baratos primeiro, as checagens caras de conteúdo por último:
>
> 1. **Filtro de política.** Esse tipo de alegação cai dentro daquilo que o verificador de fato verifica publicamente? Se não, o pedido é rejeitado de imediato.
> 2. **Confiança na autoridade.** A autoridade que endossou a alegação é confiável o bastante sob a própria política declarada do verificador? Uma autoridade abaixo do limiar de confiança do verificador é motivo de rejeição independentemente do conteúdo da alegação.
> 3. **Reputação do emissor.** O emissor atende aos limiares de reputação que o verificador declarou para esse tipo de alegação? Uma reputação baixa pode elevar a taxa ou disparar a rejeição.
> 4. **Checagem de conteúdo.** Só quando os três primeiros filtros passam é que o verificador avalia a própria alegação — assinaturas, consistência interna, correção formal e quanto ela se desvia da política do verificador. A taxa cobrada por esse último passo reflete o risco de fato assumido.
>
> O verificador publica a política que rege cada um desses filtros, de modo que os passos não ficam a critério dele — ele está vinculado ao que já declarou. O desvio em relação à política publicada é, em si, uma alegação publicável contra ele, e ele paga por isso com a sua reputação.

O resultado: publicar uma alegação crível e útil custa quase nada. Publicar uma alegação radical custa mais. Publicar uma mentira se torna proibitivamente caro — você precisa iterar de verificador em verificador, e cada um que o rejeita acrescenta custos. O mercado precifica a sua alegação, e o preço lhe diz onde você está em relação às comunidades em que circula.

Não basta declarar que você adere a uma regra quando, na realidade, não adere. Nesse caso, a sua DID arrisca a publicação de um registro negativo que expõe a hipocrisia — o que transforma você num risco para todos os demais. O desfecho deveria ser menos regras, porém seguidas de forma mais consistente, e uma limpeza daquela selva de leis e regulamentos que nem os profissionais do direito conseguem navegar direito.

![HYPOCRISY IS THE MOST EXPENSIVE BEHAVIOR](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Consenso vs Responsabilização
> Para que a rede sirva como fonte valiosa de informação, uma DID não deve ser radical demais — caso contrário, as outras a rejeitarão. A pressão social buscará o equilíbrio, e as tentativas de desestabilizá-lo provavelmente serão punidas.

![DECLARE YOUR RULES, PAY THE PRICE](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] O Número de Votos Não é o Mesmo que o Peso de uma Voz
> Juraj Karpiš diz que "o dinheiro é a memória das boas ações." Eu acrescentaria que a reputação é a memória das más.
>
> Segue-se que, meritocraticamente, quem contribui mais e não tem má reputação merece um peso maior de voz na comunidade. Visto pela lente das relações bilaterais: quando eu peso quais pressões de consenso acomodar, o maior peso vai para as relações das quais eu derivo o maior benefício econômico. Dez pessoas com quem eu não tenho comércio ativo vão me influenciar bem menos do que um parceiro de negócios permanente. Esse paradigma não se limita ao comércio — ele se estende às relações sociais, políticas e outras.
