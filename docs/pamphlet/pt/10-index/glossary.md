---
title: "Glossary"
part: "Appendix"
lang: en
version: v6
---

# Glossário

| Termo | Português | Significado |
|------|-------|---------|
| **Authority** | Autoridade | Uma entidade de confiança (pessoa, organização) que verifica informação e põe nela a sua reputação em jogo. Pode ser especializada (investigativa, jurídica, técnica). |
| **Claim** | Alegação | Em geral: qualquer afirmação verificável. Aqui: um registo publicado na rede de reputação — uma asserção sobre um acontecimento, propriedade ou relação, assinada e verificada criptograficamente. Por exemplo, “sou residente do município X” ou “esta pessoa quebrou um contrato.” |
| **Compartmentalization** | Compartimentação | Em geral: separar a informação em unidades isoladas, de modo a que expor uma unidade não comprometa as outras. Um princípio conhecido dos serviços de informações. Aqui: identidades DID paralelas nas ditaduras — comprometer uma não revela as outras. |
| **Consistent Hash Ring** | Anel de hash | Um mecanismo algorítmico para selecionar verificadores — uma posição no anel é determinada pelo hash do documento DID dentro do grafo social. Garante uma seleção não determinística, mas verificável. |
| **DID** | DID (Identidade descentralizada) | Uma identidade digital que o próprio cria e controla, sem uma autoridade central. Assinada criptograficamente com a sua chave privada — ninguém a pode revogar nem falsificar. |
| **DID Document** | Documento DID | Um ficheiro de dados publicamente disponível que descreve a sua identidade DID — contém chaves públicas, endereços de rede e metainformação. Usado para verificar a sua identidade na rede. |
| **Due Diligence** | Due diligence | Em geral: verificação aprofundada de uma contraparte antes de entrar numa relação de negócio ou jurídica — verificar o seu histórico, finanças, reputação e riscos. Aqui: na rede de reputação, acontece de forma mais rápida e mais automática graças à disponibilidade de registos verificados. |
| **Economic Neutrality Principle** | Princípio da neutralidade económica | O comportamento honesto na rede é economicamente próximo de zero — os custos de publicação são devolvidos como recompensas de verificação. O comportamento desonesto é uma perda líquida. |
| **Emergent** | Emergente | Que surge espontaneamente das interações de partes mais simples, sem que ninguém o desenhe ou dirija. Um bando de aves voa em formação sem um plano — a formação emerge de regras simples seguidas por cada indivíduo. |
| **Emergent Social Contract** | Contrato social emergente | Regras de comportamento que surgem não de cima (a lei) mas de baixo — de interações repetidas e do consenso dentro de uma comunidade. |
| **ESR** | Electronic Spending Register | Um sistema proposto para o rastreio transparente das despesas públicas — cada despesa realizada do estado é feita corresponder a um pagamento planeado. Inspirado na EET checa, mas virado contra o estado. |
| **Hash** | Hash (impressão) | Em geral: uma função matemática unidirecional que produz uma “impressão digital” única de comprimento fixo a partir de qualquer entrada — como a impressão digital do documento. A mesma entrada produz sempre a mesma saída, mas a entrada não pode ser derivada da saída. Aqui: usada para determinar uma posição no anel de hash e para verificar a integridade do documento. |
| **Just-in-Time Funding** | Financiamento just-in-time | Financiamento do estado condicionado à transparência — o dinheiro só flui quando o estado aceita o ESR e faz corresponder as suas despesas. Uma alavanca para forçar a cooperação. |
| **Meritocracy** | Meritocracia | Em geral: um sistema onde a posição é determinada pelo mérito efetivo e pela capacidade comprovada, não por títulos formais, contactos ou privilégio herdado. Aqui: a rede de reputação favorece naturalmente aqueles que demonstravelmente contribuem para a comunidade — a sua voz tem mais peso pelo track record, não pelo cargo. |
| **Onion Gateway** | Onion gateway | O endereço de rede de uma identidade DID na rede onion. Separado do documento DID — pode ser mudado sem perder a identidade (semelhante a mudar o endereço IP por trás de um domínio). |
| **Onion Routing** | Onion routing (Tor) | Um protocolo de comunicação que garante a incensurabilidade da rede. As mensagens são cifradas em camadas — cada nó retira uma camada, mas não conhece o caminho completo. |
| **Oracle Problem** | Problema do oráculo | Em geral: como garantir que os dados que entram num sistema digital correspondem fielmente ao que realmente aconteceu no mundo físico. O termo tem origem no domínio da blockchain. Aqui: resolvido através de autoridades que põem a sua reputação em jogo como garantia de que um registo digital corresponde à realidade física. |
| **Phenomenological** | Fenomenológico | Em geral: uma abordagem que estuda os fenómenos tal como se manifestam na experiência direta, observando o que deles decorre, sem teorias pré-dadas. Aqui: a liberdade, o contrato social e as normas de comportamento são fenómenos observados — consequências de milhares de microinterações entre pessoas, não princípios definidos de cima. |
| **Policy** | Policy (política) | Em geral: um conjunto de regras ou princípios que regem o comportamento num dado contexto. Aqui: cada participante na rede DID declara a sua política — como responde a comportamentos específicos dos outros, que regras segue e que penalizações considera proporcionadas. O agregado das políticas forma o contrato social emergente. |
| **Proxy** | Proxy | Em geral: um substituto ou intermediário — um sistema ou entidade a atuar em nome de outro. Usado aqui em dois contextos: (1) o ESR como proxy que faz corresponder as despesas públicas aos pagamentos planeados; (2) os observadores como proxy entre publicador e verificador no truque do observador. |
| **Publisher** | Publicador | Um participante da rede que cria e publica um registo (uma alegação sobre uma injustiça, uma reparação, e assim por diante). Suporta o custo da publicação. |
| **Reputation-Based Social Network (RSN)** | Rede de reputação | Uma rede social descentralizada onde os participantes trocam feedback sobre o comportamento no mundo real. Os registos são dispendiosos de criar, baratos de ler. |
| **Reputation Signal** | Sinal de reputação | Um registo individual na rede — positivo (reparação de um dano, cumprimento de uma obrigação) ou negativo (injustiça, quebra de contrato). Cumulativamente, os sinais formam um perfil de reputação. |
| **Social Graph** | Grafo social | A rede dos seus contactos e dos contactos dos seus contactos. O algoritmo procura verificadores a uma profundidade configurável (por exemplo, 3 níveis). Sem blockchain global — a rede forma naturalmente comunidades com sobreposições. |
| **Tax Allocation** | Alocação de impostos | Um mecanismo pelo qual o contribuinte decide para onde vai parte dos seus impostos. A percentagem alocável cresce ano após ano. |
| **Track Record** | Track record | Em geral: o histórico de resultados passados, êxitos e fracassos de uma pessoa ou organização. Aqui: a soma de todas as interações passadas de uma dada identidade DID na rede — alegações verificadas, registos aceites e rejeitados — de onde se deriva a sua reputação. |
| **Verifier** | Verificador | Um participante algoritmicamente selecionado para verificar e publicar um registo. Põe o seu bom nome em jogo na veracidade da informação. |
