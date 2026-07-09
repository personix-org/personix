---
title: "Roles Overview"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Panorama de los roles

Ya rozamos brevemente algunos de estos roles en el capítulo sobre la red y sus propiedades básicas. Ahora es el momento de volver a mirarlos con más detalle y añadir los adicionales que necesitamos para hacer la red más robusta. Cada transacción de verificación involucra varios roles; veamos cómo se comportan.

> [!note] Roles en una transacción de verificación
> Cada verificación involucra hasta seis roles distintos, resumidos en la tabla siguiente. Todos ellos pueden tener su propia DID en la red de reputación descentralizada.

| Rol | Descripción |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Emisor** | La persona que publica información en la red: afirma que algo ocurrió (se creó, editó o disolvió una DID, una afirmación, la política de una DID dada, etc.) |
| **Sujeto** | La persona sobre la que trata la información: el destinatario de la afirmación |
| **Autoridad** | Una entidad de confianza que pone su nombre en juego por la calidad de la afirmación investigándola y bien revisando las pruebas presentadas, bien reuniéndolas activamente |
| **Observador** | Un tercero independiente que lleva registro de cómo el verificador gestiona la afirmación, asegurándose de que el verificador ni guarde silencio ni se desvíe de la política que declaró |
| **Verificador** | Un participante seleccionado algorítmicamente que procesa la transacción |
| **Delegado** | Una persona que actúa en nombre de otro participante |
