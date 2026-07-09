---
title: "Roles Overview"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Panorama dos Papéis

Já aflorámos brevemente alguns destes papéis no capítulo sobre a rede e as suas propriedades básicas. É agora o momento de os olhar de novo com mais detalhe e de acrescentar os adicionais de que precisamos para tornar a rede mais robusta. Cada transação de verificação envolve vários papéis — vejamos como se comportam.

> [!note] Papéis numa Transação de Verificação
> Cada verificação envolve até seis papéis distintos, resumidos na tabela abaixo. Todos eles podem ter a sua própria DID na rede de reputação descentralizada.

| Papel | Descrição |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Emissor** | A pessoa que publica informação na rede — alega que algo aconteceu (uma DID foi criada, editada ou dissolvida, uma alegação, a política de uma dada DID, etc.) |
| **Sujeito** | A pessoa sobre quem a informação é — o destinatário da alegação |
| **Autoridade** | Uma entidade de confiança que põe o seu nome em jogo na qualidade da alegação, investigando-a e ou analisando a prova apresentada ou reunindo-a ativamente |
| **Observador** | Um terceiro independente que mantém registo de como o verificador trata a alegação — assegurando que o verificador nem se cala nem se desvia da política que declarou |
| **Verificador** | Um participante algoritmicamente selecionado que processa a transação |
| **Delegado** | Uma pessoa a atuar em nome de outro participante |
