---
title: "Observer"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Observador

El rol de observador elimina el incentivo del verificador para torcer las reglas. En situaciones en las que a un verificador no le gusta la solicitud del emisor o de la autoridad, podría sencillamente guardar silencio: no responder y bloquear la secuencia algorítmica. El observador —o un conjunto de observadores— pone su reputación en juego por documentar cómo se consultó al verificador. Si el verificador guarda silencio pese a una política declarada que dice lo contrario, puede ser condenado por violar el protocolo.

![THE OBSERVER — KEEPS A RECORD OF THE VERIFIER](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## El mecanismo: sello de tiempo y código de desafío

Antes de enviar una afirmación al verificador, la haces pasar por observadores: personas en las que confías, o proveedores especializados de servicios de observación que cobran una pequeña comisión. Cada observador recibe tu envío, le pone un sello de tiempo, firma que lo vio salir, y genera un código de desafío: un hash criptográfico de su firma. Los códigos se adjuntan a tu solicitud. El verificador los ve pero no tiene ni idea de quiénes son los observadores, ni de si los códigos son siquiera reales. Los observadores actúan así como intermediarios entre el emisor y el verificador, guardando un registro independiente de que la afirmación se presentó y de qué contenía. Puede haber de cero a N.

Cuando el verificador se comporta con honestidad —aceptando o rechazando en línea con su política declarada—, los códigos permanecen opacos. Nadie queda expuesto.

Pero si el verificador guarda silencio pese a una política acomodaticia, o responde de un modo que contradice lo que publicó, tú conservas las firmas originales de los observadores. Puedes publicarlas como testimonio delegado de que la afirmación se presentó y de que el verificador no siguió el protocolo. Cualquiera puede verificar que las firmas coinciden con los códigos de desafío.

## El remate: no necesitas observadores reales

Y aquí está la parte más elegante: **no necesitas observadores reales en absoluto.** Puedes generar números aleatorios que se parezcan exactamente a los códigos de desafío. El verificador no puede notar la diferencia: tiene que jugarse a los dados si arriesgar o no su reputación. Detrás de cada solicitud que recibe podría haber un observador respetado vigilando de incógnito, o podría ser puro ruido. El verificador no lo sabe. Y esa incertidumbre es el mecanismo.

El costo de mantener la presión honesta: casi cero (los números aleatorios son gratis). El costo potencial de la deshonestidad para el verificador: catastrófico. El comportamiento honesto se incentiva incluso cuando nadie está vigilando de verdad.

El sistema funciona porque todos son un poco paranoicos. La incertidumbre es más barata que la vigilancia.

![THE BLUFF THAT KEEPS THE VERIFIER HONEST](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Varios verificadores en una sola iteración
> Una regla acompañante que refuerza la disponibilidad de verificadores puede ser una extensión algorítmica que devuelva, en una sola iteración, un conjunto de verificadores candidatos en lugar de uno solo.
