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

La propuesta consiste en desarrollar un sistema que capture señales electromiográficas (EMG) de los músculos del cuello y las procese para distinguir entre sílabas o palabras específicas, permitiendo así controlar y modular la laringe electrónica de forma intuitiva y sin intervención manual.

Captura de la intención: Aunque el paciente ha perdido la laringe, aun conserva la musculatura orofacial y cervical que normalmente participa en la articulación del habla. Cuando intenta pronunciar una palabra, esos músculos generan señales de activación eléctrica. El sistema captura esas señales mediante electrodos de superficie ubicados en zonas del cuello, registrando la actividad muscular, sin sonido, que acompaña al intento de habla.

Diferenciación entre sílabas y palabras: Se extraen características de la señal en el dominio del tiempo y la frecuencia, y se entrena un modelo de clasificación capaz de identificar a qué sílaba o palabra corresponde cada patrón muscular. 

Activación de la laringe electrónica: Una vez que el sistema reconoce la intención articulatoria del usuario, traduce esa información en señales de control para la electrolaringe. Activa la vibración en el momento preciso, ajusta la frecuencia según el patrón detectado y controla la duración del pulso de acuerdo con la extensión de la sílaba o palabra identificada. 

En síntesis, la propuesta transforma los movimientos residuales del cuello en una interfaz de control natural para la laringe electrónica, con el objetivo de que el paciente pueda comunicarse de forma más fluida.


## Plan te actividades
| Semana | Fecha | F1: Diseño y Setup | F2: Adquisición EMG | F3: Procesamiento (DSP) | F4: Síntesis de Voz | F5: Hardware y Energía | F6: Pruebas y Ajustes | F7: Hitos del Curso y Cierre |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **S1** | 27/mar | **X** | | | | | | **X** |
| **S2** | 03/abr | **X** | **X** | | | | | |
| **S3** | 10/abr | | **X** | | | | | |
| **S4** | 17/abr | | **X** | **X** | | | | **X** |
| **S5** | 24/abr | | | **X** | | | | |
| **S6** | 01/may | | | **X** | **X** | | | |
| **S7** | 08/may | | | | **X** | | | |
| **S8** | 15/may | | | | **X** | | | |
| **S9** | 22/may | | | | **X** | **X** | | |
| **S10**| 29/may | | | | | **X** | | |
| **S11**| 05/jun | | | | | **X** | **X** | |
| **S12**| 12/jun | | | | | | **X** | |
| **S13**| 19/jun | | | | | | **X** | |
| **S14**| 26/jun | | | | | | **X** | |
| **S15**| 03/jul | | | | | | | **X** |
| **S16**| 10/jul | | | | | | | **X** |

## Referencias
[1] J. Wu. et al., “A novel silent speech recognition approach based on parallel inception CNN using surface electromyography,” Frontiers in Neurorobotics, vol. 16, 2022. https://www.frontiersin.org/articles/10.3389/fnbot.2022.971446/full  
[2] J. T. Heaton et al., “Development of a Wireless Electromyographically Controlled Electrolarynx Voice Prosthesis,” 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC8981260/  
[3] X. Chen, et al., “Decoding silent speech based on high-density surface electromyography using spatiotemporal neural network,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 31, pp. 1234–1245, 2023. https://doi.org/10.1109/TNSRE.2023.3266299  
[4] L. Zhang, M. Li y Y. Chen, “Decoding silent speech: A machine learning perspective,” Neural Computing and Applications, 2025. https://link.springer.com/article/10.1007/s00521-024-10456-z  
[5] T. Ikeda, K. Yamamoto y H. Kato, “Classification of silent speech words considering walking using VMD applied facial EMG” en Proc. International Symposium on Affective Science and Engineering (ISASE), 2023. https://doi.org/10.5057/isase.2023-C000013
