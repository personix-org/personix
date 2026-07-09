---
title: "Verifier"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Verificador

Cualquier DID puede actuar como verificador, ya sea directamente o a través de derechos de verificación delegados en una tercera DID. Para que yo —o mi delegado— pueda verificar, debería estar localizable en la red (en línea). No todo el mundo querrá comprometerse a eso, y por eso un registro de DID puede listar, por orden de prioridad, los sustitutos que desempeñarán la función en su nombre mientras esté desconectada.

Cada DID activa en la red declara públicamente su propia política. Mediante las reglas definidas en esa política juzga, durante el proceso de verificación, la reputación de la contraparte y el contenido y la forma de la afirmación que el emisor ha marcado para su publicación en la red de reputación. Parte de la política es la fórmula de cálculo empleada para computar las comisiones por los servicios de verificación. Una vez eso está en su lugar, entonces, a lo largo de un número estadísticamente grande de afirmaciones que fluyen por la red, espero a que el algoritmo de la red me saque del lado del emisor y me asigne, en una iteración dada, verificar la información que se emite. El emisor puede calcular de antemano cómo reaccionaría un verificador que se comporta correctamente, pero no puede evitar contactarlo de verdad (o a sus sustitutos); la iteración con el verificador seleccionado ha de ser llevada a cabo por el emisor incluso cuando sabe de antemano que no pasará.

¿Cómo sabemos que el emisor ejecuta el algoritmo de selección de verificador sobre el conjunto correcto de DID candidatas a verificador? Junto con su política declarada públicamente, cada DID publica también la lista actual de identificadores de su red social dentro de la red de reputación. Si un emisor define su red social como una burbuja social que se limita a hacer eco y a reforzar sus propias opiniones, la información publicada a través de ella difícilmente será recibida de forma más amplia por otras comunidades. El hecho de que consiga, a alto costo, empujar una afirmación radical dentro de la red no implica que, al juzgar la reputación de la contraparte, vaya a darle ningún peso. Algunas afirmaciones mi comunidad me empuja a tenerlas en cuenta (condenas y restricciones impuestas a infractores); otras dependen enteramente de mí: decido yo mismo el valor económico de incluir o excluir una pieza de información dada.

![THE VERIFIER — CHOSEN BY THE ALGORITHM](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
