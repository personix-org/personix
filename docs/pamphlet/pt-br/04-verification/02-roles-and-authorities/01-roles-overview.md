---
title: "Roles Overview"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Panorama dos Papéis

Já tocamos brevemente em alguns desses papéis no capítulo sobre a rede e as suas propriedades básicas. Agora é a hora de olhá-los de novo com mais detalhe e acrescentar os outros de que precisamos para tornar a rede mais robusta. Toda transação de verificação envolve vários papéis — vejamos como eles se comportam.

> [!note] Papéis numa Transação de Verificação
> Cada verificação envolve até seis papéis distintos, resumidos na tabela abaixo. Todos eles podem ter a sua própria DID na rede de reputação descentralizada.

| Papel | Descrição |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Emissor** | A pessoa que publica informação na rede — alega que algo aconteceu (uma DID foi criada, editada ou dissolvida, uma alegação, a política de uma dada DID etc.) |
| **Sujeito** | A pessoa a quem a informação diz respeito — o destinatário da alegação |
| **Autoridade** | Uma entidade de confiança que põe o seu nome em jogo pela qualidade da alegação, investigando-a e, ou revisando as provas apresentadas, ou reunindo-as ativamente |
| **Observador** | Um terceiro independente que mantém um registro de como o verificador lida com a alegação — garantindo que o verificador não fique em silêncio nem se desvie da política que declarou |
| **Verificador** | Um participante algoritmicamente selecionado que processa a transação |
| **Delegado** | Uma pessoa que age em nome de outro participante |
