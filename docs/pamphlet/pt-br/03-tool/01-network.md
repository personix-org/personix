---
title: "Reputation-Based Social Network"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Rede Social de Reputação

Para promover a mudança, precisamos de uma ferramenta cuidadosamente projetada. Primeiro vamos esboçá-la brevemente; nos capítulos seguintes examinaremos cada peça com mais detalhe e acrescentaremos outras. Imagine uma rede social incensurável, global e descentralizada, na qual você possa criar e gerenciar com segurança a sua identidade proxy — a chamada Identidade Descentralizada (DID). Uma DID é uma identidade digital que você mesmo cria e controla, sem depender de nenhuma autoridade central. Ninguém pode tirá-la de você nem falsificá-la, porque ela é assinada criptograficamente com a sua chave privada (ou chaves, via multisig).

> [!note] Nota
> Uma implicação disso é que uma identidade dessas poderia substituir aos poucos os documentos de identificação emitidos pelo estado — mas falaremos disso no capítulo sobre a transição.

![YOUR IDENTITY, YOUR KEYS, YOUR RULES](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

Numa rede assim, você poderia reportar, por meio da sua identidade, que alguém lhe causou um dano (e depois, potencialmente, que essa pessoa o reparou ou foi obrigada a repará-lo). Para que esse retorno — direcionado a quem originou o dano — tenha valor como fonte relevante, inserir informação na rede precisa custar tempo, energia e dinheiro — e, além disso, uma prova verificável precisa ser produzida para os demais de que aquilo não é conversa fiada.

Ler a informação seria fácil e relativamente barato, mas criar um registro individual seria custoso e exigente. A escrita seguiria um protocolo claro, no qual um cálculo conforme o algoritmo escolhido determina de forma estrita a qual DID pedir a verificação da informação submetida e como proceder para que o participante selecionado processe a informação em seu nome, a publique e se torne o seu verificador.

> [!note] Algoritmo vs radicalismo
> A seleção algorítmica de verificadores garante que os publicadores de informação não radicais mantenham, ao longo do tempo, um equilíbrio quase neutro entre os custos da informação publicada e as recompensas pela verificação.

![PUBLISHING COSTS TIME, ENERGY, AND MONEY](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Vejamos como o algoritmo seleciona um verificador.

> [!note] Algoritmo
> A seleção algorítmica escolhe de forma não determinística um verificador diferente (ou um conjunto de verificadores possíveis) para diferentes informações. Um hash (uma função matemática unidirecional que produz uma “impressão digital” única a partir de qualquer entrada — como a impressão digital de um documento) do documento DID completo determina a posição num anel de hash e seleciona os candidatos a verificador.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Em linguagem simples: o algoritmo pega todo o seu documento DID, calcula uma impressão digital a partir dele, e essa impressão digital determina o seu verificador.

![HOW THE ALGORITHM SELECTS YOUR VERIFIER](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Com o primeiro verificador que o algoritmo seleciona, você, como publicador, pode não ter êxito — a sua reputação ou as suas configurações declaradas podem não atender aos requisitos dele. Você prosseguiria algoritmicamente a busca pelo próximo, executando outra iteração recursiva, que lhe atribui um verificador adicional. A cada passo, a “distância” até o verificador-alvo cresce, assim como cresce a metainformação que a acompanha e que precisa ser publicada. À medida que os dados crescem, os custos sobem naturalmente (não só por causa do tamanho inicial da alegação, mas também por causa da metainformação que se acumula a cada rejeição). A informação crível passa muito mais facilmente do que caprichos disparatados. Cabe a cada pessoa decidir qual preço está disposta a suportar e quanto o registro lhe importa — o radicalismo, com toda a certeza, fica caro.

![HOW THE VERIFIER ANSWERS](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Seja o que for que o verificador decida em resposta ao seu pedido de verificação, a bola volta para o campo do publicador: ele pode aceitar a oferta do verificador pelos serviços de verificação, integrar a resposta à cronologia e tentar de novo (de forma mais cara), ou desistir e engolir o custo perdido.

![THE ISSUER'S CHOICE](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Para dar à sua informação maior peso e uma chance melhor de aceitação junto aos verificadores, você — como publicador com interesse na informação a ser emitida — poderia recorrer aos serviços de uma **autoridade de confiança**. A autoridade ou rejeita a informação submetida, ou a aceita e põe nela o seu bom nome (reputação). A autoridade normalmente solicita provas do mundo real, as verifica e as classifica. O resultado é um protocolo da sua avaliação do caso em questão no momento em questão. Pense numa autoridade como um especialista em certo tipo de serviço, tanto no mundo real quanto no digital — por exemplo, um investigador, um auditor, uma seguradora, um fornecedor de certa classe de bens (na essência, qualquer ator econômico no mercado).

![HOW A RECORD IS CREATED IN THE NETWORK](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Quando você tentar publicar informação na rede, ela provavelmente já conterá informação sobre os seus atores — são os sinais de reputação. Saber como ler os sinais de reputação — o que eles significam para você em diferentes situações e quais riscos carregam — pode não ser trivial. Cada participante pode olhar os registros de reputação de forma diferente por meio da sua DID, dependendo da situação com que está lidando em relação à contraparte. A contraparte é um pagador confiável, ou preciso exigir dinheiro adiantado para uma transação comercial? O produto oferecido carrega avaliações sobre fraude ou defeitos ocultos? Ela tenta se esquivar da responsabilidade contratual quando algo dá errado? Às vezes uma visão mais complexa da consistência geral da contraparte vem a calhar — depende das preferências de quem solicita o panorama. O mercado poderia oferecer produtos e serviços que simplificam, processam e esclarecem a leitura da reputação no contexto da situação em questão. Diversas autoridades e os serviços que oferecem também podem servir a esse propósito.

![HOW TO READ REPUTATION](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Exemplos
> A informação típica de interesse para os publicadores — e valiosa para os demais — diz respeito a acontecimentos que vão além da comunicação interpessoal comum no mundo real ou virtual.
>
> Exemplos negativos:
> - provas de atos criminosos (por exemplo, auditadas por um órgão investigativo de confiança)
> - provas indiretas (fracas por si só, mas estatisticamente cumulativas) — por exemplo, presença repetida perto de vários furtos em pouco tempo → ainda é coincidência?
> - quebra de contrato
>
> Exemplos positivos:
> - dano reparado (voluntariamente ou sob pressão da comunidade como punição)
> - aceitação e cumprimento de uma pena proposta pela autoridade X
> - a autoridade X revogou, em certa medida, o reconhecimento dos direitos de propriedade do infrator
>
> Cabe a cada pessoa reunir a informação disponível sobre a contraparte e avaliar os riscos conforme as suas preferências.

![WHAT CAN YOU RECORD IN THE NETWORK?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Se uma informação sobre você aparece na rede depende exclusivamente do seu próprio comportamento.
> Você nunca é obrigado a entrar numa rede dessas e, ainda assim, uma informação sobre você pode aparecer nela. Isso depende exclusivamente das suas ações e do impacto que elas têm sobre os outros.

![THE COMMUNITY CAN OPEN ONE FOR YOU](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

O que acabei de esboçar brevemente é como uma rede social inspirada na Identidade Descentralizada (DID) poderia funcionar. O propósito primário dos conceitos de DID é fortalecer a privacidade e a liberdade pelo princípio de subscrever as regras que vou seguir e pelas quais vou viver — dando aos usuários a capacidade de decidir qual informação compartilhar e sob quais condições.

Eu proponho conectar ainda mais as DIDs numa rede de comunicação em que os seus portadores troquem retorno até mesmo além das situações em que algo aconteceu a alguém e a comunidade ou um indivíduo precisa reagir. Essa comparação preventiva das regras que assinamos — com a opção de calcular as consequências econômicas e de outra ordem dos desvios mútuos nas expectativas sobre como o outro lado deveria operar — poderia ser considerada uma motivação para encontrar consenso. Em vez de liberdade, um sistema desses enfatizaria a decisão voluntária combinada com a responsabilidade pelo comportamento no mundo real.

Um indivíduo não consegue quebrar o sistema sozinho — um grupo de pessoas tem uma chance maior, e um grupo de pessoas com consenso negociado e motivações para puxar juntas em muitas questões tem uma chance ainda maior de resistir a tendências autoritárias. O pressuposto da organização, do primeiro capítulo, será cumprido assim que duas condições forem atendidas: a rede de reputação DID cobrir comunidades de forma representativa o bastante para que o seu uso deixe de ser exótico. E, ao mesmo tempo, esse segmento comunitário se tornar uma minoria economicamente significativa, capaz de negociar de forma assertiva com o restante da sociedade.

> [!note] Voluntariedade vs liberdade
> A liberdade — no sentido positivo — seria um efeito secundário do equilíbrio de dois fatores: a voluntariedade e a pressão do entorno rumo à responsabilidade.

> [!note] A Era da IA e o Valor da Reputação
> Na era da inteligência artificial, tudo o que está ligado ao pensamento cognitivo está sendo automatizado — e pode ir ainda mais longe. O que então resta na atividade humana como vantagem competitiva? A resposta é difícil, e algo com certeza será encontrado, mas de uma coisa podemos ter certeza: a reputação vai decidir. Um histórico verificável do seu comportamento, dos seus compromissos e do cumprimento deles — isso é algo que a IA não vai construir por você.

![AI CANNOT BUILD YOUR REPUTATION — ONLY YOU CAN](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![THE ECONOMICS OF TRUTH](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
