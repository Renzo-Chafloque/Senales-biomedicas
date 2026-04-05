# Optimización de comandos simples en laringe electrónica mediante señales EMG para una comunicación clara y precisa

## Introducción

La laringectomía total implica la pérdida de la voz natural, lo que afecta profundamente la comunicación y la calidad de vida de los pacientes. Como alternativa, la laringe electrónica ofrece una solución al permitir la articulación del habla mediante vibraciones mecánicas transmitidas a través del cuello.
Sin embargo, la voz obtenida a través de la laringe electrónica presenta importantes limitaciones, tales como un tono monótono, la presencia de ruido mecánico y una falta de naturalidad. Estas características no solo afectan la percepción de la voz, sino que también dificultan la correcta diferenciación de palabras en situaciones cotidianas.

En este contexto, el procesamiento digital de señales emerge como una herramienta clave para analizar, mejorar y facilitar la interpretación de la señal de voz generada.

## Problemática a abordar

La señal de **EMG** de los músculos cervicales, como el esternocleidomastoideo, presenta varias limitaciones que dificultan la discriminación precisa de comandos simples. Estas señales suelen tener baja variabilidad en su frecuencia y estar contaminadas con ruido mecánico proveniente de otros movimientos del cuerpo, lo que complica la correcta identificación de comandos como "sí" y "no".

El principal desafío consiste en extraer características claras y confiables de las señales EMG, como la frecuencia de activación, amplitud y duración de contracción muscular, que permitan una clasificación correcta de los comandos sin confusión.

La pregunta clave que se busca resolver es:

**¿Cómo procesar la señal EMG para mejorar la discriminación de comandos simples, específicamente de la activación muscular en el cuello?**

## Propuesta de solución

Este proyecto propone el desarrollo de un sistema  que tiene control mediante las señales biologicas para transformar la voz electrolaríngea robótica en una voz cercana a la natural del usuario. La solución se separa en 2 partes:

Procesamiento digital: Se intercepta la señal acústica producida por la electrolaringe y se procesa para mejorar su calidad antes de que sea escuchada. Los filtros adaptativos eliminan el ruido mecanico del dispositivo, se extraen parámetros acústicos y modelos de enmascaramiento auditivo para la optimización de la inteligibilidad. Todo esto ocurre con una latencia baja para la fluidez del habla.

Conversión de voz: Implementa un sistema de conversión de voz basado en una base de datos que toma como entrada la voz electrolaríngea procesada y la transforma en una voz sintetizada. Un codificador acústico extrae representaciones de la señal, un módulo de conversión mapea esas características hacia la voz natural mediante la base de datos y un vocoder sintetiza la forma de onda, produciendo una voz que suene natural.

Todo el sistema se implementa en un dispositivo portátil y discreto que el usuario lleva en el cuello. El procesamiento ocurre localmente en hardware. La latencia total del sistema sera baja y la autonomía de la batería debera ser suficiente para aguantar un dia laboral.

## Plan te actividades
## Referencias
[1] J. Wu. et al., “A novel silent speech recognition approach based on parallel inception CNN using surface electromyography,” Frontiers in Neurorobotics, vol. 16, 2022. https://www.frontiersin.org/articles/10.3389/fnbot.2022.971446/full  
[2] J. T. Heaton et al., “Development of a Wireless Electromyographically Controlled Electrolarynx Voice Prosthesis,” 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC8981260/  
[3] X. Chen, et al., “Decoding silent speech based on high-density surface electromyography using spatiotemporal neural network,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 31, pp. 1234–1245, 2023. https://doi.org/10.1109/TNSRE.2023.3266299  
[4] L. Zhang, M. Li y Y. Chen, “Decoding silent speech: A machine learning perspective,” Neural Computing and Applications, 2025. https://link.springer.com/article/10.1007/s00521-024-10456-z  
[5] T. Ikeda, K. Yamamoto y H. Kato, “Classification of silent speech words considering walking using VMD applied facial EMG” en Proc. International Symposium on Affective Science and Engineering (ISASE), 2023. https://doi.org/10.5057/isase.2023-C000013
