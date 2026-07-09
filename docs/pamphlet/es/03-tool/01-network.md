---
title: "Reputation-Based Social Network"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Red social basada en la reputación

Para provocar el cambio necesitamos una herramienta cuidadosamente diseñada. Primero la esbozaremos brevemente; en capítulos posteriores examinaremos cada pieza con mayor detalle y añadiremos más. Imagina una red social incensurable, global y descentralizada donde pudieras crear y gestionar con seguridad tu identidad delegada, una llamada identidad descentralizada (DID). Una DID es una identidad digital que creas y controlas tú mismo, sin depender de ninguna autoridad central. Nadie puede quitártela ni falsificarla, porque está firmada criptográficamente con tu clave privada (o claves, mediante multisig).

> [!note] Nota
> Una de sus implicaciones es que semejante identidad podría reemplazar de forma gradual los documentos de identidad emitidos por el Estado, pero más sobre esto en el capítulo sobre la transición.

![YOUR IDENTITY, YOUR KEYS, YOUR RULES](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

En una red así, a través de tu identidad podrías comunicar que alguien te ha causado un daño (y más tarde, potencialmente, que lo ha reparado o ha sido obligado a hacerlo). Para que esta retroalimentación, dirigida al causante del daño, tenga valor como fuente relevante, introducir información en la red debe costar tiempo, energía y dinero, y además debe producirse una prueba verificable para los demás de que no se trata de una cháchara ociosa.

Leer información sería fácil y relativamente barato, pero crear un registro individual sería costoso y exigente. La escritura seguiría un protocolo claro, en el que el cálculo según el algoritmo elegido determina estrictamente a qué DID pedir la verificación de la información presentada y cómo proceder para que el participante seleccionado procese la información en tu nombre, la publique y se convierta en su verificador.

> [!note] Algoritmo frente a radicalismo
> La selección algorítmica de verificadores garantiza que los publicadores de información no radicales mantendrán, con el tiempo, un equilibrio casi neutro entre los costes de la información publicada y las recompensas por verificar.

![PUBLISHING COSTS TIME, ENERGY, AND MONEY](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Veamos cómo selecciona el algoritmo a un verificador.

> [!note] Algoritmo
> La selección algorítmica escoge de forma no determinista un verificador distinto (o un conjunto de posibles verificadores) para distintas piezas de información. Un hash (una función matemática de un solo sentido que produce una «huella» única a partir de cualquier entrada, como la huella dactilar de un documento) del documento DID completo determina la posición en un anillo de hash consistente y selecciona a los candidatos a verificador.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> En lenguaje llano: el algoritmo toma todo tu documento DID, calcula una huella a partir de él, y esa huella determina a tu verificador.

![HOW THE ALGORITHM SELECTS YOUR VERIFIER](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Con el primer verificador que el algoritmo selecciona, tú, como publicador, puedes no salir airoso: tu reputación o tus ajustes declarados quizá no cumplan sus requisitos. Continuarías algorítmicamente la búsqueda del siguiente realizando otra iteración recursiva, que te asigna un verificador más. Con cada paso crece la «distancia» al verificador de destino, y crecen también los metadatos que hay que publicar. A medida que los datos aumentan, los costes suben de forma natural (no solo por el tamaño inicial de la afirmación, sino también por los metadatos que se acumulan con cada rechazo). La información creíble pasa mucho más fácilmente que los caprichos sin sentido. Depende de cada persona qué precio está dispuesta a asumir y cuánto le importa el registro: el radicalismo, con toda seguridad, sale caro.

![HOW THE VERIFIER ANSWERS](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Sea lo que sea que el verificador decida en respuesta a tu solicitud de verificación, la pelota vuelve al tejado del publicador: puede aceptar la oferta del verificador por sus servicios de verificación, incorporar la respuesta a la cronología e intentarlo de nuevo (a mayor coste), o retirarse y asumir el coste ya hundido.

![THE ISSUER'S CHOICE](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Para dar mayor peso a tu información y una mejor probabilidad de que los verificadores la acepten, tú, como publicador con interés en que se emita la información, podrías recurrir a los servicios de una **autoridad de confianza**. La autoridad o bien rechaza la información presentada, o bien la acepta y pone en juego su buen nombre (su reputación) por ella. La autoridad suele solicitar pruebas del mundo real, las verifica y las clasifica. El producto resultante es un protocolo de su evaluación del caso dado en el momento dado. Piensa en una autoridad como en un especialista en cierto tipo de servicio, tanto en el mundo real como en el digital: por ejemplo, un investigador, un auditor, una aseguradora, un proveedor de cierta clase de bienes (en esencia, cualquier actor económico del mercado).

![HOW A RECORD IS CREATED IN THE NETWORK](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Para cuando intentes publicar información en la red, esta ya contendrá probablemente información sobre sus actores: son señales de reputación. Orientarse en cómo leer las señales de reputación, qué significan para ti en distintas situaciones y qué riesgos entrañan, puede no ser trivial. Cada participante puede mirar los registros de reputación de forma distinta a través de su DID, según la situación que esté afrontando respecto a la contraparte. ¿Es la contraparte un pagador fiable, o necesito exigir el dinero por adelantado en una transacción comercial? ¿El producto ofrecido carga con reseñas sobre fraudes o defectos ocultos? ¿Intenta escurrir el bulto de la responsabilidad contractual cuando algo sale mal? A veces viene bien una visión más compleja de la coherencia global de la contraparte: depende de las preferencias de quien solicite el panorama. El mercado podría ofrecer productos y servicios que simplifiquen, procesen y aclaren la lectura de la reputación en el contexto de la situación concreta. Diversas autoridades y los servicios que ofrecen también pueden servir a este fin.

![HOW TO READ REPUTATION](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Ejemplos
> La información que típicamente interesa a los publicadores, y que resulta valiosa para los demás, se refiere a hechos que van más allá de la comunicación interpersonal ordinaria en el mundo real o virtual.
>
> Ejemplos negativos:
> - pruebas de actos delictivos (p. ej., auditadas por un órgano de investigación de confianza)
> - pruebas indirectas (débiles por sí solas, pero estadísticamente acumulativas): p. ej., presencia repetida cerca de varios robos en poco tiempo → ¿sigue siendo casualidad?
> - incumplimiento de contrato
>
> Ejemplos positivos:
> - daño reparado (voluntariamente o bajo la presión de la comunidad como castigo)
> - aceptación y cumplimiento de una pena propuesta por la autoridad X
> - la autoridad X revocó, en cierta medida, el reconocimiento de los derechos de propiedad del infractor
>
> Depende de cada persona reunir la información disponible sobre la contraparte y evaluar los riesgos según sus preferencias.

![WHAT CAN YOU RECORD IN THE NETWORK?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Que aparezca información sobre ti en la red depende exclusivamente de tu propio comportamiento.
> Nunca tienes que unirte a semejante red, y aun así puede aparecer en ella información sobre ti. Depende exclusivamente de tus actos y del impacto que tengan sobre los demás.

![THE COMMUNITY CAN OPEN ONE FOR YOU](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Lo que acabo de esbozar brevemente es cómo podría funcionar una red social inspirada en la identidad descentralizada (DID). El propósito primario de los conceptos DID es reforzar la privacidad y la libertad mediante el principio de suscribir las reglas que voy a seguir y por las que voy a vivir, dando a los usuarios la capacidad de decidir qué información compartir y bajo qué condiciones.

Propongo conectar además las DID en una red de comunicación donde sus titulares intercambien retroalimentación incluso más allá de las situaciones en que algo le ha ocurrido a alguien y la comunidad o un individuo necesita reaccionar. Semejante comparación preventiva de las reglas a las que nos hemos suscrito, con la opción de calcular las consecuencias económicas y de otro tipo de las desviaciones mutuas en las expectativas sobre cómo debería operar la otra parte, podría considerarse una motivación para encontrar el consenso. En lugar de la libertad, un sistema así pondría el acento en la decisión voluntaria combinada con la responsabilidad por el comportamiento en el mundo real.

Un individuo no puede quebrar el sistema por sí solo: un grupo de personas tiene más posibilidades, y un grupo de personas con un consenso negociado y motivaciones para remar juntas en muchos asuntos tiene posibilidades aún mayores de resistir las tendencias autoritarias. El requisito de organización del primer capítulo se cumplirá una vez satisfechas dos condiciones: que la red de reputación DID cubra a las comunidades de forma suficientemente representativa como para que su uso deje de ser exótico. Y, a la vez, que este segmento comunitario se convierta en una minoría económicamente significativa capaz de negociar con asertividad con el resto de la sociedad.

> [!note] Voluntariedad frente a libertad
> La libertad, en sentido positivo, sería un efecto secundario del equilibrio entre dos factores: la voluntariedad y la presión del entorno hacia la responsabilidad.

> [!note] La era de la IA y el valor de la reputación
> En la era de la inteligencia artificial, todo lo conectado con el pensamiento cognitivo se está automatizando, y puede que aún vaya más lejos. ¿Qué queda entonces en la actividad humana como ventaja competitiva? La respuesta es difícil, y seguro que se encontrará algo, pero una cosa podemos afirmarla con certeza: la reputación decidirá. Un historial verificable de tu comportamiento, de tus compromisos y de su cumplimiento: eso es algo que la IA no construirá por ti.

![AI CANNOT BUILD YOUR REPUTATION — ONLY YOU CAN](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![THE ECONOMICS OF TRUTH](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
