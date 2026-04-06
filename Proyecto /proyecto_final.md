# Mejora de la discriminación de comandos simples en dispositivos de voz asistida mediante señales EMG

## Introducción

La laringectomía total implica la pérdida de la voz natural, lo que afecta profundamente la comunicación y la calidad de vida de los pacientes. Como alternativa, la laringe electrónica ofrece una solución al permitir la articulación del habla mediante vibraciones mecánicas transmitidas a través del cuello [1]. Sin embargo, la voz obtenida a través de la laringe electrónica presenta importantes limitaciones, tales como un tono monótono, la presencia de ruido mecánico y una falta de naturalidad [2]. Estas características no solo afectan la percepción de la voz, sino que también dificultan la correcta diferenciación de palabras en situaciones cotidianas [3].

En este contexto, el procesamiento digital de señales emerge como una herramienta clave para analizar, mejorar y facilitar la interpretación de la señal de voz generada [4].

## Problemática a abordar

La señal de EMG de los músculos cervicales ha demostrado ser eficaz para diagnosticar afecciones médicas como la disfagia, estimando la actividad muscular del cuello y midiendo vibraciones de las cuerdas vocales [1]. En los últimos años, se ha comenzado a utilizar esta técnica para la traducción del habla en personas con condiciones como la disfonía y frente a las consecuencias de procedimientos como las laringectomías [2]. Sin embargo, la difícil obtención de una señal clara sigue siendo un obstáculo significativo para la discriminación precisa de comandos simples.

La señal EMG de estos músculos suele tener baja variabilidad en su frecuencia y se encuentra contaminada con ruido mecánico proveniente de otros movimientos corporales, lo que dificulta la correcta identificación de comandos como "sí" y "no" [3].

El principal desafío consiste en extraer características claras y confiables de las señales EMG, como la frecuencia de activación, la amplitud y la duración de la contracción muscular, para permitir la correcta clasificación de los comandos sin confusión.

La pregunta clave que se busca resolver es:

**¿Cómo procesar la señal EMG para mejorar la discriminación de comandos simples, específicamente de la activación muscular en el cuello?**

## Propuesta de solución

La propuesta consiste en desarrollar un sistema que capture señales electromiográficas (EMG) de los músculos del cuello y las procese para distinguir entre sílabas o palabras específicas, permitiendo así controlar y modular la laringe electrónica de forma intuitiva y sin intervención manual.

Captura de la intención: Aunque el paciente ha perdido la laringe, aun conserva la musculatura orofacial y cervical que normalmente participa en la articulación del habla. Cuando intenta pronunciar una palabra, esos músculos generan señales de activación eléctrica. El sistema captura esas señales mediante electrodos de superficie ubicados en zonas del cuello, registrando la actividad muscular, sin sonido, que acompaña al intento de habla.

Diferenciación entre sílabas y palabras: Se extraen características de la señal en el dominio del tiempo y la frecuencia, y se entrena un modelo de clasificación capaz de identificar a qué sílaba o palabra corresponde cada patrón muscular. 

Activación de la laringe electrónica: Una vez que el sistema reconoce la intención articulatoria del usuario, traduce esa información en señales de control para la electrolaringe. Activa la vibración en el momento preciso, ajusta la frecuencia según el patrón detectado y controla la duración del pulso de acuerdo con la extensión de la sílaba o palabra identificada. 

En síntesis, la propuesta transforma los movimientos residuales del cuello en una interfaz de control natural para la laringe electrónica, con el objetivo de que el paciente pueda comunicarse de forma más fluida.


## Plan te actividades
### Detalle de Tareas por Fase del Proyecto

**Fase 1: Investigación, Diseño y Setup (Semanas 1-2)**
| Tarea | Descripción Breve | Hito / Entregable |
| :--- | :--- | :--- |
| **Selección de tema** | Formalización del proyecto y creación del repositorio. | Hito S1 (27/mar) |
| **Setup de entorno** | Configuración del entorno virtual y estructura de carpetas. | Hito S2 (03/abr) |
| **Revisión de literatura** | Estado del arte en voz electrolaríngea y adquisición EMG. | - |
| **Estudio anatómico** | Ubicación óptima de electrodos en el esternocleidomastoideo. | - |
| **Selección de hardware** | Cotización de electrodos, módulo EMG, DSP y alimentación. | - |
| **Arquitectura** | Definición del flujo de datos y software del sistema. | - |

**Fase 2: Protocolo y Adquisición EMG (Semanas 2-4)**
| Tarea | Descripción Breve | Hito / Entregable |
| :--- | :--- | :--- |
| **Diseño de protocolo** | Definición de comandos vocales ("sí", "no", vocales). | - |
| **Consentimiento** | Redacción del consentimiento informado para toma de datos. | - |
| **Ensamble de circuito** | Conexión y verificación del módulo de instrumentación EMG. | - |
| **Pruebas de captura** | Calibración de ganancias para evitar saturación de señal. | - |
| **Base de datos** | Registro continuo y segmentado de señales de prueba. | - |
| **Revisión de avance I** | Presentación del estado de la adquisición de señales. | Hito S4 (17/abr) |

**Fase 3: Procesamiento Digital de Señales - DSP (Semanas 4-6)**
| Tarea | Descripción Breve | Hito / Entregable |
| :--- | :--- | :--- |
| **Importación de datos** | Ploteo de señales EMG en Python (Matplotlib, SciPy). | - |
| **Filtrado básico** | Filtros FIR/IIR para ruido de línea (60Hz) y movimiento. | - |
| **Filtrado avanzado** | Evaluación de Transformada Wavelet para ruido mecánico. | - |
| **Extracción temporal** | Cálculo de RMS, cruces por cero y amplitud máxima. | - |
| **Extracción frecuencial**| Análisis del espectro de potencia y frecuencia mediana. | - |

**Fase 4: Clasificación y Síntesis de Voz (Semanas 6-9)**
| Tarea | Descripción Breve | Hito / Entregable |
| :--- | :--- | :--- |
| **Estructuración de datos** | Creación de Dataframe con características extraídas. | - |
| **Entrenamiento ML/DL** | Modelos para clasificación de comandos neuromusculares. | - |
| **Evaluación de modelo** | Análisis de métricas (Accuracy, Precision) y ajuste. | - |
| **Codificador acústico** | Implementación para la parametrización del habla. | - |
| **Integración con vocoder** | Gatillado de voz natural a partir de la base de datos. | - |

**Fase 5: Integración en Hardware y Gestión de Energía (Semanas 9-11)**
| Tarea | Descripción Breve | Hito / Entregable |
| :--- | :--- | :--- |
| **Selección de lenguaje** | Definición entre C/C++ o MicroPython según hardware. | - |
| **Migración de algoritmos** | Traslado del filtrado, DSP y modelo ML al dispositivo. | - |
| **Optimización de latencia**| Medición de tiempos de ejecución en el microcontrolador. | - |
| **Diseño de alimentación** | Medición del perfil de consumo de corriente del circuito. | - |
| **Selección de batería** | Cálculo de autonomía y selección de batería Li-Po. | - |

**Fase 6: Pruebas del Sistema Integrado y Ajustes (Semanas 11-14)**
| Tarea | Descripción Breve | Hito / Entregable |
| :--- | :--- | :--- |
| **Diseño de case 3D** | Modelado e impresión del soporte anatómico (collarín). | - |
| **Ensamblaje final** | Integración física de todos los componentes del dispositivo. | - |
| **Pruebas de usabilidad** | Evaluaciones en tiempo real para verificar fluidez. | - |
| **Análisis de fallos** | Identificación de falsos positivos/negativos en uso. | - |
| **Ajuste fino** | Corrección de ganancias y umbrales según retroalimentación. | - |

**Fase 7: Documentación, Cierre y Presentaciones (Semanas 15-16)**
| Tarea | Descripción Breve | Hito / Entregable |
| :--- | :--- | :--- |
| **Revisión de avance III** | Muestra del prototipo funcional integrado. | Hito S15 (03/jul)|
| **Recopilación de anexos** | Organización de gráficos, códigos y esquemáticos. | - |
| **Informe Final** | Redacción estructurada (Intro, Metodología, Resultados). | Hito S16 (10/jul)|
| **Diseño de póster** | Diagramación visual de la problemática y resultados. | Hito S16 (10/jul)|
| **Preparación de pitch** | Creación de diapositivas y ensayo para exposiciones. | Hito S16 (10/jul)|

## Síntesis en una sola tabla:
### Cronograma Maestro de Actividades: Laringe Electrónica EMG

| Fase (Semanas) | Tareas y Descripción | Hitos y Entregables |
| :--- | :--- | :--- |
| **F1: Investigación y Setup**<br>*(Semanas 1-2)* | **1.** Selección de tema y formalización del proyecto.<br>**2.** Creación de repositorio y setup de entorno virtual.<br>**3.** Revisión de literatura sobre adquisición EMG cervical.<br>**4.** Selección de hardware, electrodos y arquitectura. | • **Hito S1 (27/mar):** Selección de proyecto.<br>• **Hito S2 (03/abr):** Setup del entorno. |
| **F2: Adquisición EMG**<br>*(Semanas 2-4)* | **1.** Diseño de protocolo de comandos y consentimiento.<br>**2.** Ensamble y verificación del circuito de instrumentación.<br>**3.** Pruebas de calibración para evitar saturación.<br>**4.** Levantamiento de la base de datos de señales EMG. | • **Hito S4 (17/abr):** Revisión de avance I (Adquisición). |
| **F3: Procesamiento (DSP)**<br>*(Semanas 4-6)* | **1.** Importación y ploteo de señales en Python.<br>**2.** Diseño de filtros FIR/IIR (ruido de 60Hz y movimiento).<br>**3.** Evaluación de filtros avanzados (Transformada Wavelet).<br>**4.** Extracción de características (tiempo y frecuencia). | - |
| **F4: Síntesis de Voz**<br>*(Semanas 6-9)* | **1.** Creación de Dataframe con características extraídas.<br>**2.** Entrenamiento y evaluación de modelos ML/DL.<br>**3.** Implementación del codificador acústico.<br>**4.** Integración de clasificación con el vocoder. | - |
| **F5: Hardware y Energía**<br>*(Semanas 9-11)* | **1.** Migración de algoritmos al dispositivo portátil.<br>**2.** Optimización de latencia en el microcontrolador.<br>**3.** Medición de consumo de corriente del circuito.<br>**4.** Cálculo de autonomía y selección de batería Li-Po. | - |
| **F6: Pruebas y Ajustes**<br>*(Semanas 11-14)* | **1.** Diseño e impresión 3D del soporte anatómico (collarín).<br>**2.** Ensamblaje físico del dispositivo completo.<br>**3.** Pruebas de usabilidad en tiempo real (Live testing).<br>**4.** Análisis de fallos y ajuste fino de umbrales/ganancias. | - |
| **F7: Documentación y Cierre**<br>*(Semanas 15-16)* | **1.** Recopilación de gráficos, códigos y esquemáticos.<br>**2.** Redacción estructurada del Informe Final.<br>**3.** Diagramación del póster científico.<br>**4.** Ensayo y preparación para exposiciones orales. | • **Hito S15 (03/jul):** Revisión de avance III.<br>• **Hito S16 (10/jul):** Informe Final.<br>• **Hito S16 (10/jul):** Póster y Presentación. |

## Referencias
[1] J. T. Heaton et al., “Development of a Wireless Electromyographically Controlled Electrolarynx Voice Prosthesis,” 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC8981260/ 

[2] R. B. Siqueira et al., “Laryngeal electromyography in dysphonic patients with incomplete glottic closure,” Int. Arch. Otorhinolaryngol., 2022. https://doi.org/10.1055/s-0041-1733867

[3] J. Wu. et al., “A novel silent speech recognition approach based on parallel inception CNN using surface electromyography,” Frontiers in Neurorobotics, vol. 16, 2022. https://www.frontiersin.org/articles/10.3389/fnbot.2022.971446/full 

[4] P. Wu et al., "Towards EMG-to-Speech with a Necklace Form Factor," in Proc. Interspeech 2024, Kos, Grecia, 2024, pp. 402-406.

[5] X. Chen, et al., “Decoding silent speech based on high-density surface electromyography using spatiotemporal neural network,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 31, pp. 1234–1245, 2023. https://doi.org/10.1109/TNSRE.2023.3266299

[6] L. Zhang, M. Li y Y. Chen, “Decoding silent speech: A machine learning perspective,” Neural Computing and Applications, 2025. https://link.springer.com/article/10.1007/s00521-024-10456-z

[7] T. Ikeda, K. Yamamoto y H. Kato, “Classification of silent speech words considering walking using VMD applied facial EMG” en Proc. International Symposium on Affective Science and Engineering (ISASE), 2023. https://doi.org/10.5057/isase.2023-C000013
