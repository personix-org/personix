---
title: "Reputation-Based Social Network"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Rede Social Baseada na Reputação

Para promover a mudança, precisamos de uma ferramenta cuidadosamente concebida. Primeiro vamos esboçá-la de forma breve; em capítulos posteriores examinaremos cada parte com maior detalhe e acrescentaremos mais. Imagine uma rede social incensurável, global e descentralizada, onde poderia criar e gerir com segurança a sua identidade delegada — uma chamada Identidade Descentralizada (DID). Uma DID é uma identidade digital que o próprio cria e controla, sem dependência de qualquer autoridade central. Ninguém a pode retirar ou falsificar, porque está assinada criptograficamente com a sua chave privada (ou chaves, via multisig).

> [!note] Nota
> Uma das implicações é que uma tal identidade poderia gradualmente substituir os documentos de identificação emitidos pelo estado — mas sobre isso mais adiante, no capítulo sobre a transição.

![YOUR IDENTITY, YOUR KEYS, YOUR RULES](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

Numa tal rede, poderia comunicar, através da sua identidade, que alguém lhe causou um dano (e, mais tarde, potencialmente, que o reparou ou foi obrigado a fazê-lo). Para que este feedback — dirigido a quem originou o dano — tenha valor como fonte relevante, introduzir informação na rede tem de custar tempo, energia e dinheiro — e, além disso, tem de ser produzida prova verificável para os outros de que não se trata de conversa fiada.

Ler informação seria fácil e relativamente barato, mas criar um registo individual seria dispendioso e exigente. A escrita seguiria um protocolo claro, no qual o cálculo segundo o algoritmo escolhido determina de forma estrita a que DID pedir a verificação da informação submetida e como proceder para que o participante selecionado processe a informação em seu nome, a publique e se torne o seu verificador.

> [!note] Algoritmo vs radicalismo
> A seleção algorítmica de verificadores garante que os publicadores de informação não radicais manterão, ao longo do tempo, um equilíbrio quase neutro entre os custos da informação publicada e as recompensas pela verificação.

![PUBLISHING COSTS TIME, ENERGY, AND MONEY](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Vejamos como o algoritmo seleciona um verificador.

> [!note] Algoritmo
> A seleção algorítmica escolhe de forma não determinística um verificador diferente (ou um conjunto de verificadores possíveis) para diferentes peças de informação. Um hash (uma função matemática unidirecional que produz uma “impressão digital” única a partir de qualquer entrada — como a impressão digital de um documento) do documento DID completo determina a posição num anel de hash consistente e seleciona os candidatos a verificador.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Em linguagem simples: o algoritmo pega em todo o seu documento DID, calcula dele uma impressão digital, e essa impressão digital determina o seu verificador.

![HOW THE ALGORITHM SELECTS YOUR VERIFIER](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Com o primeiro verificador que o algoritmo seleciona, o publicador pode não ter êxito — a sua reputação ou as suas definições declaradas podem não cumprir os requisitos dele. Prosseguiria algoritmicamente a busca pelo seguinte, executando outra iteração recursiva, que lhe atribui um verificador adicional. A cada passo, a “distância” até ao verificador-alvo cresce, tal como cresce a metainformação que a acompanha e que tem de ser publicada. À medida que os dados crescem, os custos sobem naturalmente (não só devido à dimensão inicial da alegação, mas também devido à metainformação que se acumula a cada rejeição). A informação credível passa muito mais facilmente do que caprichos disparatados. Cabe a cada pessoa decidir que preço está disposta a suportar e quanto lhe importa o registo — o radicalismo, com toda a certeza, torna-se caro.

![HOW THE VERIFIER ANSWERS](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

O que quer que o verificador decida em resposta ao seu pedido de verificação, a bola volta ao campo do publicador: este pode aceitar a oferta do verificador para os serviços de verificação, integrar a resposta na cronologia e tentar de novo (de forma mais cara), ou desistir e engolir o custo perdido.

![THE ISSUER'S CHOICE](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Para dar à sua informação maior peso e uma melhor hipótese de aceitação junto dos verificadores, poderia — enquanto publicador com interesse na informação a ser emitida — recorrer aos serviços de uma **autoridade de confiança**. A autoridade ou rejeita a informação submetida ou a aceita e põe nela o seu bom nome (reputação). A autoridade normalmente solicita prova do mundo real, verifica-a e classifica-a. O resultado é um protocolo da sua avaliação do caso em questão no momento em questão. Pense numa autoridade como um especialista num certo tipo de serviço, tanto no mundo real como no digital — por exemplo um investigador, um auditor, uma seguradora, um fornecedor de uma certa classe de bens (na essência, qualquer ator económico no mercado).

![HOW A RECORD IS CREATED IN THE NETWORK](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Quando tentar publicar informação na rede, esta já conterá provavelmente informação sobre os seus atores — são os sinais de reputação. Orientar-se em como ler os sinais de reputação — o que significam para si em diferentes situações e que riscos comportam — pode não ser trivial. Cada participante pode olhar para os registos de reputação de forma diferente, através da sua DID, consoante a situação com que está a lidar em relação à contraparte. É a contraparte um pagador fiável, ou preciso de exigir dinheiro adiantado para uma transação comercial? Traz o produto oferecido avaliações sobre fraude ou defeitos ocultos? Estão a tentar esquivar-se à responsabilidade contratual quando algo corre mal? Por vezes vem a calhar uma visão mais complexa da consistência global da contraparte — depende das preferências de quem pede a visão de conjunto. O mercado poderia oferecer produtos e serviços que simplificam, processam e clarificam a leitura da reputação no contexto da situação em causa. Várias autoridades e os serviços que oferecem também podem servir esse fim.

![HOW TO READ REPUTATION](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Exemplos
> A informação típica que interessa aos publicadores — e valiosa para os outros — diz respeito a acontecimentos que vão além da comunicação interpessoal comum no mundo real ou virtual.
>
> Exemplos negativos:
> - prova de atos criminosos (por exemplo, auditados por um órgão investigativo de confiança)
> - prova indireta (fraca por si só, mas estatisticamente cumulativa) — por exemplo, presença repetida perto de vários furtos num curto espaço de tempo → ainda é coincidência?
> - quebra de contrato
>
> Exemplos positivos:
> - dano reparado (voluntariamente ou sob pressão da comunidade como castigo)
> - aceitação e cumprimento de uma penalização proposta pela autoridade X
> - a autoridade X revogou, até certo ponto, o reconhecimento dos direitos de propriedade do infrator
>
> Cabe a cada pessoa reunir a informação disponível sobre a contraparte e avaliar os riscos segundo as suas preferências.

![WHAT CAN YOU RECORD IN THE NETWORK?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Que informação sobre si aparece na rede depende exclusivamente do seu próprio comportamento.
> Nunca tem de aderir a uma tal rede e, ainda assim, informação sobre si pode aparecer nela. Depende exclusivamente das suas ações e do impacto que elas têm sobre os outros.

![THE COMMUNITY CAN OPEN ONE FOR YOU](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

O que acabei de esboçar brevemente é como poderia funcionar uma rede social inspirada na Identidade Descentralizada (DID). O propósito primário dos conceitos de DID é reforçar a privacidade e a liberdade através do princípio de subscrever as regras que vou seguir e pelas quais vou viver — dando aos utilizadores a capacidade de decidir que informação partilhar e sob que condições.

Proponho ainda ligar as DIDs numa rede de comunicação onde os seus detentores trocam feedback mesmo para além das situações em que algo aconteceu a alguém e a comunidade ou um indivíduo precisa de reagir. Uma tal comparação preventiva das regras a que aderimos — com a opção de calcular as consequências económicas e outras dos desvios mútuos nas expectativas sobre como o outro lado deveria operar — poderia ser considerada uma motivação para encontrar consenso. Em vez de liberdade, um tal sistema realçaria a decisão voluntária combinada com a responsabilidade pelo comportamento no mundo real.

Um indivíduo não consegue quebrar o sistema sozinho — um grupo de pessoas tem maior hipótese, e um grupo de pessoas com consenso negociado e motivações para puxar em conjunto em muitas questões tem uma hipótese ainda maior de resistir a tendências autoritárias. O pressuposto da organização, do primeiro capítulo, será cumprido assim que duas condições forem satisfeitas: a rede de reputação DID cobre as comunidades de forma suficientemente representativa para que o seu uso deixe de ser exótico. E, ao mesmo tempo, este segmento comunitário torna-se uma minoria economicamente significativa que consegue negociar de forma assertiva com o resto da sociedade.

> [!note] Voluntariedade vs liberdade
> A liberdade — no sentido positivo — seria um efeito secundário do equilíbrio de dois fatores: a voluntariedade e a pressão do meio envolvente em direção à responsabilidade.

> [!note] A Era da IA e o Valor da Reputação
> Na era da inteligência artificial, tudo o que está ligado ao pensamento cognitivo está a ser automatizado — e pode ir ainda mais longe. O que resta então na atividade humana como vantagem competitiva? A resposta é difícil, e algo há de certamente encontrar-se, mas uma coisa podemos afirmar com certeza: a reputação decidirá. Um histórico verificável do seu comportamento, dos seus compromissos e do seu cumprimento — isso é algo que a IA não construirá por si.

![AI CANNOT BUILD YOUR REPUTATION — ONLY YOU CAN](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![THE ECONOMICS OF TRUTH](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
