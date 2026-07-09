---
title: "Consensus and the Verification Process"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# El consenso y el proceso de verificación

Para construir consenso sobre qué reglas debería, en promedio, sostener y hacer cumplir una sociedad, puede ayudar el siguiente mecanismo. Como participante DID, declaro las reglas a las que me suscribo y por las que voy a vivir, y las publico. (Piénsalo como los estatutos y reglamentos que, en mi opinión, componen mi mundo ideal: un mundo donde no me siento restringido, sino seguro.)

Puedo estimar de antemano cómo reaccionarían mis contactos DID, y evaluar con qué fuerza, y por quién, sería sancionado en las interacciones sociales o comerciales ordinarias, en caso de que llegaran a producirse hipotéticamente.

La evaluación definitiva ocurre cuando solicitas información a otra DID, o le pides que verifique una afirmación (o pides un servicio a una autoridad, y así sucesivamente) que quieres publicar en la red de reputación. Debería resolverse igual que cuando ejecutas tú mismo la evaluación, en simulacro, contra la política declarada de la contraparte; y si no es así, algo va mal del lado de la contraparte: está intentando jugar un juego deshonesto.

El resultado es o bien la aceptación, con un precio cotizado por la verificación (en el caso de los servicios de un verificador o de una autoridad), o bien el rechazo. Tanto las sanciones como las bonificaciones por desviarse de la política del evaluador se incorporan al precio cotizado. El solicitante decide entonces si acepta las condiciones, o pasa a la siguiente ronda de verificación del algoritmo de asignación, repitiendo el proceso hasta quedar satisfecho, o hasta que la economía haga inútil continuar.

> [!note] El grafo social
> La red de reputación es, ante todo, una red social. Añades contactos: personas que consienten la conexión. Ellas tienen contactos, y esos contactos tienen contactos. El algoritmo busca verificadores dentro de una profundidad configurable (p. ej., tres niveles: tus contactos directos, sus contactos y un nivel más allá). No se necesita ninguna cadena de bloques global: la red forma comunidades de manera natural, con solapamientos hacia otras comunidades.
>
> El algoritmo es no determinista: aplica un hash a tu documento de afirmación, mapea el hash a una posición en un anillo de identidades conocidas dentro de este círculo, y selecciona a la más cercana como verificador candidato. No puedes predecir ni influir en quién verificará tu afirmación.

Cada rechazo de un verificador agranda tu documento y aumenta su coste de procesamiento: es el primer canal de coste (el crecimiento del documento). Cada nuevo verificador cobra una comisión basada en el volumen de datos, tu reputación, y cuánto se desvía el contenido de tu afirmación de su política de verificación declarada: es el segundo canal de coste (la prima de riesgo). Y cada iteración cuesta tiempo y energía: el tercer canal de coste.

> [!note] Qué comprueba el verificador, en orden
> Una vez seleccionado, un verificador evalúa una afirmación en aproximadamente cuatro pasos ordenados: primero los filtros más baratos, y al final las costosas comprobaciones de contenido:
>
> 1. **Filtro de política.** ¿Este tipo de afirmación cae, en absoluto, dentro de lo que el verificador verifica públicamente? Si no, la solicitud se rechaza de plano.
> 2. **Confianza en la autoridad.** ¿La autoridad que avaló la afirmación goza de suficiente confianza según la propia política declarada del verificador? Una autoridad por debajo del umbral de confianza del verificador es motivo de rechazo, con independencia del contenido de la afirmación.
> 3. **Reputación del emisor.** ¿El emisor cumple los umbrales de reputación que el verificador ha declarado para este tipo de afirmación? Una reputación baja puede o bien elevar la comisión, o bien desencadenar el rechazo.
> 4. **Comprobación del contenido.** Solo cuando los tres primeros filtros se superan, el verificador evalúa la afirmación en sí: firmas, coherencia interna, corrección formal, y cuánto se desvía de la política del verificador. La comisión cobrada por este último paso refleja el riesgo realmente asumido.
>
> El verificador publica la política que gobierna cada uno de estos filtros, de modo que los pasos no quedan a su discreción: está vinculado por lo que ya ha declarado. Desviarse de la política publicada es en sí mismo una afirmación publicable en su contra, y la paga con su reputación.

El resultado: publicar una afirmación creíble y útil no cuesta casi nada. Publicar una afirmación radical cuesta más. Publicar una mentira se vuelve prohibitivamente caro: debes iterar de verificador en verificador, y cada uno que te rechaza añade costes. El mercado pone precio a tu afirmación, y el precio te dice dónde te sitúas respecto a las comunidades en las que te mueves.

No basta con declarar que te atienes a una regla cuando en realidad no lo haces. En ese caso, tu DID se arriesga a la publicación de un registro negativo que exponga la hipocresía, lo cual te convierte en un riesgo para todos los demás. El resultado debería ser reglas menos numerosas pero seguidas con más coherencia, y un desbroce de esa jungla de leyes y reglamentos por la que apenas saben orientarse ni los profesionales del derecho.

![HYPOCRISY IS THE MOST EXPENSIVE BEHAVIOR](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Consenso frente a rendición de cuentas
> Para que la red sirva como fuente valiosa de información, una DID no debería ser demasiado radical, de lo contrario los demás la rechazarán. La presión social buscará el equilibrio, y los intentos de desestabilizarlo probablemente serán castigados.

![DECLARE YOUR RULES, PAY THE PRICE](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] El número de votos no es lo mismo que el peso de una voz
> Juraj Karpiš dice que «el dinero es la memoria de las buenas acciones». Yo añadiría que la reputación es la memoria de las malas.
>
> De ello se sigue que, meritocráticamente, quien más aporta y no tiene mala reputación merece un mayor peso de voz en la comunidad. Visto a través de la lente de las relaciones bilaterales: cuando sopeso a qué presiones de consenso acomodarme, el mayor peso lo tienen las relaciones de las que obtengo el mayor beneficio económico. Diez personas con las que no tengo comercio activo me influirán mucho menos que un socio comercial permanente. Este paradigma no se limita al comercio: se extiende a las relaciones sociales, políticas y de otro tipo.
