# Laboratorio de Electroencefalograma (EEG)

## Introducción
La electroencefalografía es el método o proceso científico mediante el cual se lleva a cabo el electroencefalograma. Este es una prueba que mide la actividad eléctrica en el cerebro [1]. Esta prueba está fundamentada por principios biológicos y físicos puesto que las neuronas se comunican mediante impulsos eléctricos en el orden de los microvoltios, los cuales son medidos por electrodos colocados en el cuero cabelludo de la persona evaluada. La señal detectada por los mismos será vista en forma de ondas en un registro.

Dependiendo de su frecuencia, estas señales pueden catalogarse en distintas ondas cerebrales, como ondas delta, theta, alfa, beta y gamma, las cuales se asocian con diferentes estados fisiológicos y cognitivos. Es pertinente agregar que, además de brindar información para comprender la actividad cerebral saludable, el EEG también sirve para diagnosticar o monitorear condiciones como problemas de sueño, convulsiones, epilepsia, encefaltitis, traumatismos y tumores [2].

<img width="643" height="217" alt="image" src="https://github.com/user-attachments/assets/98566a48-bc5d-4975-a26e-dded57590975" />

Características de las cinco ondas cerebrales básicas [3].

En el presente laboratorio se analizarán señales EEG mediante técnicas de procesamiento digital, con el fin de identificar características relevantes de la actividad cerebral y comprender el comportamiento de este tipo de señales biomédicas.

## Métodos
### BITalino y OpenSignals
Para la adquisición de señales se utilizó el kit de hardware BITalino, este ha sido diseñado especialmente para captar bioseñales. Este dispositivo cuenta con sensores de ECG, EMG, EDA y EEG, los cuales pueden emplearse en entornos de aprendizaje como aulas y laboratorios [4].
Para la visualización de la señal adquirida, se utilizó el software OpenSignals que permite conectar el BITalino a un computador mediante Bluetooth. Durante la configuración, se estableció una frecuencia de muestreo de 100 Hz, ya que las ondas cerebrales estudiadas presentan frecuencias menores a 50 Hz. Finalmente, los datos almacenados en archivos con formato .h5 y .txt para su posterior procesamiento.

### Colocación de electrodos
Los electrodos empleados para esta experiencia fueron el sistema integrado de tres derivaciones incluido en el kit BITalino y un sensor SnapBIT-DUO. El sistema de tres derivaciones se colocó en la frente del participante, ubicando un electrodo en la frente sobre cada ojo y el tercero sobre el hueso mastoideo que fue usado como referencia.

<img width="617" height="307" alt="image" src="https://github.com/user-attachments/assets/8df3f70d-d461-4682-8a7f-968f764bd243" />

Posicionamiento de electrodos para medir EEG en la posicion FP1 [5].


Por otro lado, el sensor SnapBIT-DUO se posicionó en la frente, sobre el ojo izquierdo del participante. En esta ocasión, no se usó un cable de referencia debido a que no se disponía del case necesario para integrar ambos sistemas.

<img width="463" height="347" alt="ELECTRODE" src="https://github.com/user-attachments/assets/c5da12d6-97fe-4fa4-bd0d-b96999100920" />

Posicionamiento del SnapBIT-DUO


### Procedimiento experimental
El procedimiento se realizó con distintas condiciones cognitivas. Inicialmente, se hizo una lectura basal con un minuto de duración en la que el participante permanecía con los ojos cerrados en reposo ningún esfuerzo cognitivo. Luego, se solicitó que este abriera los ojos y mirase a un punto fijo sin distracciones durante treinta segundos para su registro. Después de esta etapa se realizó nuevamente una medida basal de treinta segundos.


Seguidamente, el participante ejecutó movimientos de parpadeo y masticación con el fin de captar la señal EEG con artefactos de movimiento durante treinta segundos y se hizo una última medición basal con la misma duración. La actividad final consistió en que el sujeto respondiera preguntas simples y complejas basadas en [6]. Esto se realizó con el fin de analizar variaciones en la señal causadas por cargas cognitivas distintas.

### Evidencias


https://github.com/user-attachments/assets/b3c87407-4492-4d3a-845e-d5c07afa5f2b



https://github.com/user-attachments/assets/4dba657f-cb2d-4fc6-91a9-746c9d4f3541



https://github.com/user-attachments/assets/eb52988f-dc9e-4444-982d-087b08029633



https://github.com/user-attachments/assets/43c7d335-b1f5-46b3-b4ad-b54cc518aaa7



## Resultados

• Evaluar incremento de β durante la tarea cognitiva (t‑test pareado).

• Detectar artefactos de parpadeo (> 80 μV) y contabilizar su número.

## Resultados — Sujeto 1 [Renzo] (Ambiente Silencioso)

### Señales crudas y filtradas


<img width="2388" height="2736" alt="fig1_senales" src="https://github.com/user-attachments/assets/b26fb70e-b477-44eb-853e-de0d98eb5153" />

Las señales crudas presentaron amplitudes de ±200 µV a lo largo de todas las condiciones. Tras aplicar el filtro pasa-banda 0.8–48 Hz más el notch a 50 Hz se eliminaron la deriva de línea base y los picos de interferencia eléctrica, resultando en señales de morfología oscilatoria más definida con amplitudes contenidas entre ±150 µV.

---

### Densidad Espectral de Potencia (PSD Welch)

<img width="1788" height="2736" alt="fig2_psd" src="https://github.com/user-attachments/assets/bf12b9cd-b2ee-48ab-9e76-b28f59724411" />

La inspección de los espectros permite identificar diferencias cualitativas entre condiciones:

- **Basal 1 (ojos abiertos):** concentración anómala de potencia en delta-theta (0–8 Hz), atribuible a un artefacto de contacto al inicio del registro, antes de que la impedancia electrodo-piel se estabilizara.
- **Ojos cerrados:** se observa un pico relativo en alpha (8–13 Hz), consistente con el estado de reposo visual.
- **Tarea cognitiva:** redistribución de potencia hacia beta y gamma, indicando mayor actividad cortical frontal.
- **Artefactos:** distribución similar al reposo; los artefactos de parpadeo se manifiestan en delta-theta por su naturaleza de baja frecuencia.

---

### Potencia relativa por banda

<img width="1935" height="880" alt="fig3_potencia_bandas" src="https://github.com/user-attachments/assets/17906ae5-37c0-41be-8977-3dd8bde57f80" />

| Condición | Delta (%) | Theta (%) | Alpha (%) | Beta (%) | Gamma (%) |
|---|---|---|---|---|---|
| Basal 1 (ojos abiertos) | **57.83** | 25.43 | 6.03 | 7.21 | 3.51 |
| Ojos cerrados | 6.83 | 15.78 | **10.99** | 33.73 | 32.67 |
| Basal 2 | 6.35 | 15.05 | 10.39 | **38.33** | 29.88 |
| Basal 3 | 6.18 | 16.56 | 10.30 | 32.10 | 34.85 |
| Tarea cognitiva | 6.65 | 15.56 | 10.29 | 34.79 | 32.71 |
| Artefactos | 6.68 | 17.55 | 10.47 | 32.80 | 32.51 |

> **Nota:** Los valores en negrita destacan la banda dominante de cada condición relevante.

El segmento Basal 1 presenta una dominancia delta del 57.83%, incompatible con un estado de vigilia normal (típicamente < 15%). Esto se explica por inestabilidad de impedancia en los primeros segundos del registro. En las cinco condiciones restantes la distribución es homogénea, con delta reducida al 6–7%, lo que confirma la estabilización del contacto electrodo-piel a partir del segundo segmento.

---

### Análisis estadístico

#### Alpha blocking: ojos abiertos vs. ojos cerrados

<img width="1934" height="740" alt="fig4_ttest" src="https://github.com/user-attachments/assets/907c6e89-ddfe-4de1-8511-2c9b48f356aa" />

| Parámetro | Valor |
|---|---|
| Media ojos abiertos | 7.55 % |
| Media ojos cerrados | 10.95 % |
| Incremento relativo | +45 % |
| Estadístico t | −4.27 |
| Valor p | 0.000189 |
| Significancia | p < 0.001 ✓ |

El t-test pareado revela una diferencia estadísticamente significativa (p < 0.001) en la potencia relativa alpha entre ambas condiciones. La potencia alpha fue un 45% mayor con ojos cerrados. Este resultado confirma el fenómeno de **alpha blocking**: al cerrar los ojos se suprime la entrada visual, los circuitos talamocorticales sincronizan en la frecuencia alpha (8–13 Hz) como reflejo de reposo sensorial, y esta sincronización se rompe en cuanto se retoma el procesamiento visual activo.

Cabe señalar que el artefacto inicial en Basal 1 atenúa el valor de alpha en "ojos abiertos" al inflar el denominador de potencia total, por lo que la diferencia real podría ser aún mayor.

#### Beta en tarea cognitiva vs. reposo basal

<img width="1934" height="740" alt="fig4_ttest" src="https://github.com/user-attachments/assets/bbe9e317-713d-4c34-8821-5f59fa021ad3" />

| Parámetro | Valor |
|---|---|
| Media basal (ojos abiertos) | 24.74 % |
| Media tarea cognitiva | 35.62 % |
| Incremento relativo | +44 % |
| Estadístico t | −3.76 |
| Valor p | 0.000755 |
| Significancia | p < 0.001 ✓ |

La potencia beta durante la tarea cognitiva fue un 44% mayor que en reposo basal (p < 0.001). El incremento de la banda beta (13–30 Hz) en corteza prefrontal refleja la desincronización neuronal necesaria para integrar información distribuida durante la formulación de respuestas verbales, patrón asociado en la literatura a tareas de memoria de trabajo y razonamiento activo.

---

### Detección de artefactos

<img width="1934" height="583" alt="fig5_artefactos" src="https://github.com/user-attachments/assets/ce59fbe8-1a70-43df-953d-fe21b98a9779" />


| Parámetro | Valor |
|---|---|
| Duración del segmento | 31.5 s |
| Umbral de detección | ± 80 µV |
| Eventos detectados | 0 |

El algoritmo de umbral no registró eventos por encima de ± 80 µV. Esto se debe principalmente a que el filtro pasa-banda 0.8–48 Hz atenúa los transitorios del electrooculograma (EOG), cuya energía se concentra por debajo de 5 Hz. Si el parpadeo fue suave o la impedancia redujo la ganancia efectiva, la amplitud del artefacto pudo mantenerse por debajo del umbral aun siendo visible a simple vista en la señal cruda.

## Resultados — Sujeto 1 (Ambiente con Bulla)

### Señales crudas y filtradas

<img width="2388" height="2736" alt="fig1b_senales" src="https://github.com/user-attachments/assets/c72c9285-273a-496d-81fd-8282d48d4bfb" />


Las señales crudas presentaron amplitudes de ±200 µV con mayor variabilidad respecto a la sesión en silencio, especialmente en los segmentos Basal 3 y Tarea cognitiva. Tras el filtrado pasa-banda 0.8–48 Hz y el notch a 50 Hz se logró reducir la interferencia eléctrica, aunque la señal filtrada conservó mayor irregularidad morfológica que su contraparte en silencio, indicativa de mayor actividad de ruido fisiológico asociado al estado de alerta auditivo.

---

### Densidad Espectral de Potencia (PSD Welch)

<img width="1788" height="2736" alt="fig2b_psd" src="https://github.com/user-attachments/assets/cee06819-de3e-4f08-9de3-405f9d4075d3" />


La inspección espectral revela un patrón cualitativamente distinto al registrado en silencio:

- **Basal 1 y Ojos cerrados:** el espectro se distribuye con mayor energía en gamma (> 30 Hz), lo que puede reflejar tanto mayor activación cortical por el estímulo auditivo de fondo como contaminación por artefactos musculares (EMG), frecuentes cuando el sujeto está en estado de alerta o tensión.
- **Basal 3 y Tarea cognitiva:** aparece una concentración marcada de potencia en delta (< 4 Hz), similar a la anomalía observada en Basal 1 de la sesión silenciosa, atribuible a inestabilidad de contacto o artefactos de movimiento durante esos segmentos.
- **Artefactos:** a diferencia de la sesión silenciosa, aquí se aprecia un pico relativo en alpha (8–13 Hz) y mayor energía en beta, posiblemente asociado a la mayor inquietud motora del sujeto en ambiente ruidoso.

---

### Potencia relativa por banda

<img width="1935" height="880" alt="fig3b_potencia_bandas" src="https://github.com/user-attachments/assets/4c0588e1-3f83-47dd-96f8-42041ef62927" />


| Condición | Delta (%) | Theta (%) | Alpha (%) | Beta (%) | Gamma (%) |
|---|---|---|---|---|---|
| Basal 1 (ojos abiertos) | 12.49 | 12.29 | 9.68 | 19.69 | **45.86** |
| Ojos cerrados | 13.20 | 12.39 | 8.24 | 18.38 | **47.79** |
| Basal 2 | 14.85 | 12.66 | 8.64 | 20.29 | 43.57 |
| Basal 3 | **45.08** | 14.52 | 7.71 | 10.21 | 22.48 |
| Tarea cognitiva | **43.42** | 11.53 | 5.08 | 9.72 | 30.26 |
| Artefactos | 13.41 | 13.54 | **14.44** | 26.22 | 32.38 |

> **Nota:** Los valores en negrita destacan la banda dominante de cada condición relevante.

Tres observaciones estructurales destacan en esta distribución. Primero, gamma domina en las condiciones de reposo (Basal 1, Ojos cerrados, Basal 2), con valores superiores al 43%, lo que contrasta con la sesión silenciosa donde gamma no superó el 35% en reposo. Segundo, los segmentos Basal 3 y Tarea cognitiva repiten el patrón de dominancia delta anómala (> 43%) ya descrito en Basal 1 de la sesión anterior, sugiriendo que las condiciones de registro en estas tomas fueron afectadas por artefactos de movimiento o inestabilidad de impedancia. Tercero, el segmento de artefactos muestra el valor de alpha más alto de toda la sesión (14.44%), lo que es contraintuitivo y se discute en la sección 3.5.

---

### Análisis estadístico

#### Alpha blocking: ojos abiertos vs. ojos cerrados

<img width="1934" height="740" alt="fig4b_ttest" src="https://github.com/user-attachments/assets/f8685169-929f-4694-87fe-e7c9ab441b3d" />


| Parámetro | Valor |
|---|---|
| Media ojos abiertos | 10.66 % |
| Media ojos cerrados | 8.24 % |
| Variación relativa | −23 % |
| Estadístico t | 2.49 |
| Valor p | 0.0189 |
| Significancia | p < 0.05 ✓ |

El t-test pareado detecta una diferencia estadísticamente significativa (p < 0.05), pero con una dirección opuesta a la esperada: la potencia alpha fue un 23% **menor** con ojos cerrados que con ojos abiertos. Este hallazgo constituye una inversión del fenómeno clásico de alpha blocking.

La interpretación más consistente con la literatura es que el ruido ambiental sostenido actuó como un estímulo sensorial auditivo constante que mantuvo el sistema nervioso autónomo en un estado de alerta, impidiendo que los circuitos talamocorticales sincronizaran en la frecuencia alpha incluso al cerrar los ojos. En condiciones normales, cerrar los ojos elimina la entrada visual y permite la sincronización alpha. Sin embargo, cuando existe un estímulo auditivo suficientemente intenso, el sistema de activación reticular ascendente (SARA) sostiene la vigilia cortical independientemente de la modalidad visual, suprimiendo la aparición del ritmo alpha. El cerebro, en otras palabras, no puede "desconectarse" sensorialmente aunque no haya procesamiento visual activo.

#### Beta en tarea cognitiva vs. reposo basal

<img width="1934" height="740" alt="fig4b_ttest" src="https://github.com/user-attachments/assets/c095baf2-b6fd-4a97-9a96-d323a2e7e92d" />


| Parámetro | Valor |
|---|---|
| Media basal (ojos abiertos) | 20.12 % |
| Media tarea cognitiva | 9.81 % |
| Variación relativa | −51 % |
| Estadístico t | 9.82 |
| Valor p | < 0.0001 |
| Significancia | p < 0.001 ✓ |

La potencia beta durante la tarea cognitiva fue un 51% menor que en reposo basal, resultado estadísticamente significativo pero de dirección opuesta al hallazgo de la sesión silenciosa, donde beta aumentó durante la tarea. Esta inversión tiene dos explicaciones no excluyentes.

La primera y más probable es metodológica: los segmentos Basal 3 y Tarea cognitiva presentan una dominancia delta anómala superior al 43%, que infla el denominador de la potencia total y comprime artificialmente las potencias relativas de las bandas altas, incluida beta. Esto significa que la caída de beta no refleja necesariamente una reducción real de la actividad atencional, sino un artefacto de cálculo derivado de la contaminación de esos segmentos.

La segunda explicación es fisiológica: en un ambiente ruidoso, la sobrecarga sensorial puede saturar los recursos atencionales disponibles, reduciendo la capacidad del sujeto para sostener el procesamiento ejecutivo prefrontal característico de la banda beta. Esta hipótesis es coherente con modelos de carga cognitiva que postulan que el ruido de fondo actúa como tarea secundaria implícita, restando recursos a la tarea principal.

---

### Detección de artefactos

<img width="1934" height="583" alt="fig5b_artefactos" src="https://github.com/user-attachments/assets/863435af-9635-40e3-9645-3618949e61c5" />


| Parámetro | Valor |
|---|---|
| Duración del segmento | 33.3 s |
| Umbral de detección | ± 80 µV |
| Eventos detectados | 4 |

A diferencia de la sesión silenciosa donde no se detectó ningún evento, aquí se registraron 4 transientes que superaron el umbral de ±80 µV. Esto es consistente con la mayor inquietud motora esperada en un ambiente ruidoso: el sujeto tiende a realizar más microgestos faciales, movimientos oculares y tensión muscular involuntaria al procesar un estímulo auditivo continuo, todos ellos fuentes de artefactos de alta amplitud en electrodos frontales como Fp1/Fp2.

El hecho de que el segmento de artefactos muestre además la mayor potencia alpha de la sesión (14.44%) puede explicarse por el efecto de los propios parpadeos controlados: el movimiento palpebral lento y sostenido genera una onda corneoretiniana de baja frecuencia que, al ser atenuada parcialmente por el filtro, puede traslapar con la banda alpha en el análisis espectral.

---

## Análisis Comparativo: Silencio vs. Bulla

### Tabla resumen de indicadores clave

| Indicador | Silencio | Bulla | Diferencia |
|---|---|---|---|
| Alpha (ojos abiertos) | 7.55 % | 10.66 % | Bulla → +41 % |
| Alpha (ojos cerrados) | 10.95 % | 8.24 % | Bulla → −25 % |
| Efecto alpha blocking | ↑ al cerrar ojos ✓ | ↓ al cerrar ojos ✗ | **Inversión** |
| Beta (basal) | 24.74 % | 20.12 % | Bulla → −19 % |
| Beta (tarea cognitiva) | 35.62 % | 9.81 % | Bulla → −72 % |
| Efecto beta cognitivo | ↑ con tarea ✓ | ↓ con tarea ✗ | **Inversión** |
| Artefactos detectados | 0 eventos | 4 eventos | Bulla → mayor ruido motor |
| Gamma en reposo | < 35 % | > 45 % | Bulla → mayor activación |





## Discusión

• ¿Qué banda de frecuencia predomina al cerrar los ojos?

• ¿Qué filtro es imprescindible para EEG y por qué?

• ¿Puedes modular conscientemente tu señal EEG? Da un ejemplo.

• ¿Se observan diferencias entre Fp1 y Fp2? ¿Por qué podrían ocurrir?

## Referencias

[1]	“Electroencefalografía (EEG)”, Mayoclinic.org, 2024. [En línea]. Disponible en: https://www.mayoclinic.org/es/tests-procedures/eeg/about/pac-20393875. [Consultado: 17-may-2026].

[2]	“Electroencefalograma”, Medlineplus.gov, 13-ene-2025. [En línea]. Disponible en: https://medlineplus.gov/spanish/ency/article/003931.htm. [Consultado: 17-may-2026].

[3]	Priyanka A. Abhang, Bharti W. Gawali, Suresh C. Mehrotra, “Technological Basics of EEG Recording and Operation of Apparatus”, ScienceDirect, 2016. [En línea]. Disponible en: https://www.sciencedirect.com/science/chapter/monograph/abs/pii/B9780128044902000026. [Consultado: 17-may-2026].

[4] “BITalino”, PLUX Biosignals. [En línea]. Disponible en: https://www.pluxbiosignals.com/collections/bitalino?srsltid=AfmBOoqSQHArGd9wQ5qW7GMdWWOrt3JAuqIjVuxrgDUkuIQw2IilsLKP. [Consultado: 17-may-2026].

[5] EXPERIMENTAL GUIDES TO MEET y L. Y. Biosignals, “BITalino (r)evolution Lab Guide”, Pluxbiosignals.com. [En línea]. Disponible en: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf?utm_source=chatgpt.com. [Consultado: 17-may-2026].

[6] J. Molina Del Río, M. A. Guevara, M. Hernández González, R. M. Hidalgo Aguirre, y M. A. Cruz Aguilar, “EEG correlation during the solving of simple and complex logical-mathematical problems”, Cogn. Affect. Behav. Neurosci., vol. 19, núm. 4, pp. 1036–1046, 2019.

