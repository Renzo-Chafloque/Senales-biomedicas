
## Introducción
El electrocardiograma (ECG) es un procedimiento diagnóstico no invasivo que registra la actividad eléctrica del corazón. Este examen es fundamental para evaluar el ritmo y la frecuencia cardíaca, así como para detectar diversas patologías como arritmias, insuficiencia cardíaca, hipertrofia y otras alteraciones cardíacas. Mediante el ECG, se obtiene una representación gráfica de los impulsos eléctricos generados durante el ciclo cardíaco, lo cual permite a los médicos obtener información clave sobre el estado funcional del corazón.

La adquisición de señales ECG se realiza mediante la colocación de electrodos en puntos específicos del cuerpo, y el análisis de las señales obtenidas ofrece patrones característicos que corresponden a las fases del ciclo cardíaco. En este estudio, se empleó el sistema BITalino (r)evolution para registrar señales de ECG en diferentes condiciones fisiológicas, como reposo, actividad física y respiración controlada. El objetivo principal de este estudio es analizar cómo la ubicación de los electrodos afecta la calidad de las señales adquiridas y cómo esto influye en el análisis de la función cardíaca [1].

---

## Objetivos
**Objetivo general:**
- Explorar las señales electrocardiográficas adquiridas mediante el sistema **BITalino (r)evolution** en diferentes condiciones fisiológicas, evaluando el impacto de la ubicación de los electrodos sobre la calidad de las señales obtenidas.

**Objetivos específicos:**
1. **Adquisición de señales:**
   - Registrar señales ECG en tiempo real utilizando el sistema **BITalino (r)evolution** en diferentes condiciones fisiológicas (reposo, actividad física, respiración controlada).
   
2. **Análisis de datos:**
   - Procesar las señales adquiridas para identificar los componentes del ECG, como la onda P, el complejo QRS, el segmento ST y la onda T.
   - Comparar las señales obtenidas en diferentes derivaciones y ubicaciones de los electrodos para evaluar la variabilidad y la influencia de la posición sobre la calidad de los datos.

3. **Procesamiento:**
   - Filtrar y procesar las señales ECG para reducir el ruido y artefactos (por ejemplo, ruido muscular, interferencia eléctrica).
   - Generar gráficas y tablas comparativas que muestren las características de las señales de ECG en distintas condiciones experimentales.
   
4. **Comprensión fisiológica:**
   - Entender los procesos fisiológicos que originan las señales ECG, a partir de la propagación de los impulsos eléctricos a través del sistema de conducción cardíaco.

5. **Detección de anomalías:**
   - Identificar posibles patrones atípicos o anormales en las señales adquiridas, relacionados con la función cardíaca, que puedan indicar posibles alteraciones o enfermedades.
  
---

## Metodología

### Componentes:
| Componente | Descripción |
|-----------|------------|
| BITalino | Sistema de adquisición de señales biomédicas |
| Electrodos EKG | Electrodos de superficie para registro |
| Cables | Conexión de electrodos al dispositivo |
| Computadora | Registro y visualización de datos |


### Ubicación de electrodos

<img width="450" height="800" alt="Ubicacion_electrodos" src="https://github.com/user-attachments/assets/ae494443-164e-4ded-bd1e-e41eda7c7e81" />

### Protocolo experimental

La adquisición de señales ECG se realizó utilizando el sistema BITalino y electrodos de superficie. Antes del registro, se colocaron los electrodos en las posiciones correspondientes a las derivaciones I, II y III, considerando la configuración de Einthoven. En estas derivaciones, la señal se obtiene mediante la diferencia de potencial eléctrico registrada entre dos electrodos, mientras que un tercer electrodo funciona como referencia [2].

Para cada condición experimental, se registraron señales en las derivaciones I, II y III. La frecuencia de muestreo utilizada fue de **1000 Hz**. Durante la adquisición, se procuró reducir el movimiento corporal para disminuir la presencia de artefactos musculares y variaciones no deseadas en la señal [2].

### Condiciones de registro

Las mediciones se realizaron en el siguiente orden:

| Código | Condición experimental | Descripción | Derivaciones registradas |
|-------|------------------------|-------------|--------------------------|
| P1 | Reposo basal inicial | Registro de la señal ECG durante 30 segundos en estado de reposo. | I, II y III |
| P2 | Hiperventilación | Registro durante un ciclo de inhalación, retención y exhalación. | I, II y III |
| P3 | Segundo reposo basal | Registro de una segunda señal basal durante 30 segundos después de 2 minutos de descanso. | I, II y III |
| P4 | Actividad física | Ejecución de burpees durante 4 minutos antes del registro de la señal. | I, II y III |
| P5 | Hipoventilación | Registro inmediato posterior a la actividad física mientras el participante mantenía la respiración. | I, II y III |


### Descripción de las derivaciones utilizadas

Las derivaciones **I**, **II** y **III** corresponden a **derivaciones bipolares** de las extremidades, basadas en el principio de **Einthoven**. Estas derivaciones permiten registrar la actividad eléctrica cardíaca desde diferentes orientaciones del plano frontal. A continuación, se describen las configuraciones de los electrodos para cada derivada, de acuerdo con la variabilidad en la ubicación de los cables para cada medición:

| **Derivación** | **Electrodo negativo** | **Electrodo positivo** | **Referencia** |
|----------------|------------------------|------------------------|----------------|
| **I**          | Muñeca derecha | Muñeca izquierda | Cresta ilíaca |
| **II**         | Muñeca derecha  | Cresta ilíaca  | Muñeca izquierda |
| **III**        | Muñeca izquierda | Cresta ilíaca  | Muñeca derecha |

> **Nota**: La ubicación de los electrodos fue modificada según la derivación registrada, siguiendo el principio de las derivaciones de **Einthoven** y la configuración experimental indicada durante la práctica.

Este ajuste en la colocación de los electrodos permite registrar la actividad eléctrica desde distintas posiciones y obtener la señal correcta para cada derivada, facilitando el análisis de la señal ECG obtenida.

### Evidencia

https://github.com/user-attachments/assets/ea8e0b36-9857-44ae-b0b9-dde45d93514b




https://github.com/user-attachments/assets/b71cae5c-a8d5-4de6-b925-48eda6271c79




https://github.com/user-attachments/assets/3cfb054f-5927-4bb1-b711-67ab932f18a4




https://github.com/user-attachments/assets/2fc9228b-5f31-4108-9e86-77ae058d8f68




https://github.com/user-attachments/assets/4ac9b222-08c8-4948-98f0-f994afa26411




---

## Resultados

Las señales EKG fueron adquiridas con el sistema BITalino a una frecuencia de muestreo de 1000Hz. Se analizaron los canales correspondientes a las muñecas y cresta ilíaca.

### Comportamiento general de la señal

- Se registraron dos patrones diferenciados entre los canales.
- Se identificaron ciclos repetitivos de activación (picos) y relajación.
- La señal presenta variabilidad incluso en periodos de reposo.

## Pruebas realizadas a Gustavo:
### Prueba 1.1: Reposo - Derivada 1

<img width="2071" height="1769" alt="GustavoBASAL1" src="https://github.com/user-attachments/assets/f75a9588-30ee-45bb-8c40-a50dab12942a" />
<img width="505" height="223" alt="GustavoBASAL1 Resultado " src="https://github.com/user-attachments/assets/34687b63-8792-4371-94a3-8208a38dde7a" />


- Características observadas
  - En esta primera prueba, donde se registró la señal ECG mientras el participante estaba en reposo, la señal se mostró bastante estable. Los picos de la onda R fueron claramente visibles, con una amplitud definida, lo que sugiere una señal de buena calidad. La variabilidad de los intervalos **RR** era moderada, lo que es normal en un estado de reposo. A pesar de la regularidad, se observó una leve fluctuación en la línea base, lo que podría estar relacionado con algunos pequeños movimientos del cuerpo, pero no hubo interferencias significativas. En general, la señal fue bastante limpia, lo que permitió obtener una buena lectura del ritmo cardíaco y la frecuencia.
  
### Prueba 1.2: Reposo - Derivada 2
<img width="2071" height="1769" alt="GustavoBASAL2" src="https://github.com/user-attachments/assets/bdd82a81-5662-4b8d-97ef-5c586b428c4c" />
<img width="467" height="227" alt="GustavoBASAL2 Resultado" src="https://github.com/user-attachments/assets/5b34250a-e03c-44c1-b0b1-a6b161218536" />


- Características observadas:
  - Para la segunda derivada, también realizada en reposo, la señal mostró algunas diferencias. Aunque los picos **R** seguían siendo visibles, su amplitud era un poco más baja en comparación con la primera derivada, lo que podría indicar una ligera pérdida de calidad en la señal. La variabilidad entre los intervalos RR fue más pronunciada en esta derivada, lo que podría estar relacionado con pequeños cambios en la respiración o el movimiento del cuerpo. Además, se notaron algunas fluctuaciones en la línea base, que en su mayoría se debieron a interferencias menores. A pesar de estos pequeños ruidos, la señal seguía siendo suficientemente clara para permitir el análisis de la frecuencia cardíaca, aunque con una menor claridad que la derivada anterior.


### Prueba 1.3: Reposo - Derivada 3
<img width="2084" height="1769" alt="GustavoBASAL3" src="https://github.com/user-attachments/assets/9459df6a-834b-4f15-846a-9add634127df" />
<img width="480" height="225" alt="GustavoBASAL3 Resultado" src="https://github.com/user-attachments/assets/f9078352-20c7-4381-a5c9-b0324472e620" />


- Características observadas:
  - En la tercera derivada, también tomada en reposo, la calidad de la señal fue un poco más afectada. Aunque los picos **R** seguían presentes, fueron menos definidos y la señal mostró más variabilidad en su amplitud. Además, se notaron más fluctuaciones en la línea base, lo que sugiere que hubo más movimiento o interferencias externas durante la medición. La señal en general se veía más "suave", lo que dificultó un poco la identificación precisa de cada latido. Esto podría haber sido causado por el mal contacto de los electrodos o algún pequeño movimiento involuntario del participante. A pesar de la menor claridad, la señal aún era útil para el análisis general, aunque no tan precisa como las derivadas anteriores.


### Prueba 2.1: Hiperventilación - Derivada 1
<img width="2071" height="1769" alt="GustavoINH1" src="https://github.com/user-attachments/assets/5c7eceb9-1f71-4136-9c73-dbd63ae5e9f0" />
<img width="458" height="221" alt="GustavoINH1 Resultado" src="https://github.com/user-attachments/assets/cfdccb34-2ac9-402a-bbc5-1933d4b4c03f" />


- Características observadas:
  - En esta prueba, realizada bajo hiperventilación, la señal muestra un patrón similar al de las pruebas anteriores, pero con una mayor frecuencia cardíaca debido a la respiración acelerada. Los picos R son más frecuentes, lo que refleja el aumento en la frecuencia cardíaca. A pesar de la aceleración, los picos siguen siendo visibles, pero con algunas fluctuaciones que indican que la señal está siendo afectada por el movimiento respiratorio. El ruido es mayor en esta condición, especialmente entre los picos, lo que podría ser causado por pequeños movimientos o interferencias externas. La señal muestra variabilidad en los intervalos **RR**, con algunos intervalos más largos que otros, lo que es típico durante la hiperventilación.

### Prueba 2.2: Hiperventilación - Derivada 2
<img width="2084" height="1769" alt="GustavoINH2" src="https://github.com/user-attachments/assets/9fdc26b8-0f09-4bdd-bafa-6ca6669bc284" />
<img width="481" height="226" alt="GustavoINH2 Resultado" src="https://github.com/user-attachments/assets/89c4b049-3cfa-4714-9016-26f8c84f4b3a" />


- Características observadas:
  - Para esta segunda derivada, la señal muestra un patrón similar al de la primera derivada, con picos **R** más rápidos y frecuentes debido a la hiperventilación. A pesar de la alta frecuencia de los latidos, los picos siguen siendo visibles, pero algunos están menos definidos, probablemente debido a la mayor variabilidad en los intervalos RR. El ruido también es más prominente, lo que sugiere que la respiración acelerada está causando pequeñas interferencias. La variabilidad en los intervalos es algo irregular, lo que puede reflejar fluctuaciones normales debido a la respiración rápida.

### Prueba 2.3: Hiperventilación - Derivada 3
<img width="2084" height="1769" alt="GustavoINH3" src="https://github.com/user-attachments/assets/85e122a8-3fbc-471f-b66d-9bc89e9cc591" />
<img width="482" height="198" alt="GustavoINH3 Resultados" src="https://github.com/user-attachments/assets/c0e9f8cf-9120-415d-85a4-1877d45af531" />


- Características observadas:
  - En la tercera derivada, la señal muestra una mayor suavidad, aunque todavía es posible observar los picos R. Al igual que en las otras derivadas, la frecuencia cardíaca aumentó debido a la hiperventilación. Sin embargo, la señal no tiene la misma claridad que en las pruebas de reposo. Se observa una variabilidad en los intervalos RR más pronunciada, lo que indica que el ritmo cardíaco está siendo afectado por la respiración rápida. El ruido sigue siendo un factor importante en la señal, aunque los picos aún son identificables. La calidad de la señal disminuyó un poco en comparación con las pruebas en reposo debido al mayor movimiento y la interferencia generada por la respiración acelerada.

    
### Prueba 3.1: Segundo reposo - Derivada 1
<img width="1536" height="754" alt="Gustavo2DABASAL1" src="https://github.com/user-attachments/assets/5b1ebba8-1500-445f-82aa-29563588fd12" />
<img width="468" height="198" alt="Gustavo2DABASAL1 resultados" src="https://github.com/user-attachments/assets/318a2d94-d8d7-4bda-99d3-bfec3804f515" />


- Características observadas:
  - 
En esta prueba, realizada durante el segundo reposo, la señal registrada fue muy débil, lo que resultó en solo 2 latidos detectados en un periodo de 30.6 segundos. Debido a esta debilidad en la señal, los picos R no fueron claramente identificables, lo que dificultó el análisis. La señal fue atenuada, y aunque los intervalos RR se detectaron, no hubo una variabilidad significativa entre ellos. Este tipo de señal probablemente se debió a problemas como el mal contacto de los electrodos o movimiento del participante, lo que afectó la precisión de la detección de los picos. Debido a esta falta de claridad, los valores de SDNN y RMSSD no fueron calculados correctamente, ya que los pocos picos detectados no fueron suficientes para obtener métricas representativas de la variabilidad de la frecuencia cardíaca.


### Prueba 3.2: Segundo reposo - Derivada 2
<img width="1536" height="754" alt="Gustavo2DABASAL2" src="https://github.com/user-attachments/assets/fc3804b9-ffd6-4cec-8da5-55a6faef98b0" />
<img width="502" height="203" alt="Gustavo2DABASAL2 resultados" src="https://github.com/user-attachments/assets/adf474ef-9030-477e-9956-aeb6ffcc9108" />


- Características observadas:
  - En esta segunda derivada durante el segundo reposo, la señal fue mucho más clara en comparación con la derivada 1. La frecuencia cardíaca aumentó y se detectaron 41 latidos en 30.9 segundos. Los picos R fueron claramente visibles, y la variabilidad en los intervalos RR fue mayor, lo que indica una frecuencia cardíaca más estable. La señal no estuvo completamente libre de fluctuaciones, pero la calidad fue lo suficientemente buena como para calcular correctamente los valores de SDNN y RMSSD, los cuales fueron representativos de la variabilidad de la frecuencia cardíaca.


### Prueba 3.3: Segundo reposo - Derivada 3
<img width="2084" height="1769" alt="Gustavo2DOBASAL3" src="https://github.com/user-attachments/assets/3221e1a6-4617-41ea-8e75-cd68e627c16a" />
<img width="473" height="197" alt="Gustavo2DOBASAL3 resultados" src="https://github.com/user-attachments/assets/4d8b8d09-23e1-4df1-bfa7-049d63eaaf4e" />


- Características observadas:
  - La tercera derivada también mostró una señal más estable en comparación con la derivada 1. Durante esta prueba, se detectaron 45 latidos en 30.9 segundos, con picos R más definidos. La señal mantuvo una variabilidad moderada en los intervalos RR, lo que refleja una frecuencia cardíaca estable durante el reposo. A pesar de algunas fluctuaciones en la señal, los resultados de SDNN y RMSSD fueron adecuados para el análisis, y los valores obtenidos son representativos de la variabilidad normal de la frecuencia cardíaca en reposo.


### Prueba 4.1: Actividad física - Derivada 1
<img width="2084" height="1769" alt="GustavoACTIVIDAD1" src="https://github.com/user-attachments/assets/75ee7bf3-67a1-4a84-a7df-5b10e463af39" />
<img width="482" height="198" alt="GustavoACTIVIDAD1 resultado" src="https://github.com/user-attachments/assets/081cced2-46b1-49fc-99c1-aff8181e8993" />

- Características observadas:
  - Durante esta prueba, realizada mientras el participante realizaba actividad física, la señal mostró una frecuencia cardíaca elevada, lo cual es típico durante el ejercicio. Aunque los picos **R** fueron identificables, la señal mostró más fluctuaciones debido a los movimientos corporales durante la actividad. La variabilidad de los intervalos RR aumentó considerablemente, lo que refleja un aumento en la frecuencia cardíaca debido al ejercicio físico. La señal, aunque buena en general, mostró un ruido moderado en los intervalos de relajación entre los latidos, lo cual puede ser una consecuencia de los movimientos del cuerpo.


### Prueba 4.2: Actividad física - Derivada 2
<img width="2073" height="1769" alt="GustavoACTIVIDAD2" src="https://github.com/user-attachments/assets/12f8d727-ec92-495f-ae65-da4128457faf" />
<img width="461" height="222" alt="GustavoACTIVIDAD2 resultados" src="https://github.com/user-attachments/assets/8d7fc660-a6fe-4b0a-9af4-f6ac8557db51" />

- Características observadas:
  - En esta segunda derivada, se observó una señal más estable en comparación con la derivada anterior. La frecuencia cardíaca seguía siendo alta, y los picos R eran claramente visibles. Sin embargo, los intervalos RR mostraron una mayor variabilidad debido al ejercicio. A pesar de algunas fluctuaciones en la señal, los resultados mostraron un comportamiento típico del ejercicio físico, con una frecuencia cardíaca elevada y una señal que refleja un aumento en la actividad física.


### Prueba 4.3: Actividad física - Derivada 3
<img width="2080" height="1769" alt="GustavoACTIVIDAD3" src="https://github.com/user-attachments/assets/dbac61b2-eccb-4043-a50b-8184b3be1a53" />
<img width="497" height="202" alt="GustavoACTIVIDAD3 resultado" src="https://github.com/user-attachments/assets/0526bb55-1b42-4700-881c-3f7a143d7c5b" />

- Características observadas:
  - Para la tercera derivada, se observó un aumento en la frecuencia cardíaca, pero la señal fue más estable que en las derivadas anteriores. Los picos R fueron bien definidos, aunque hubo algunas pequeñas fluctuaciones debido al movimiento durante el ejercicio. Los intervalos RR mostraron mayor dispersión que en las pruebas anteriores, lo que es típico en un estado de actividad física. A pesar de un leve aumento de ruido en la señal, los resultados son coherentes con lo esperado durante el ejercicio.


### Prueba 5.1: Hipoventilación - Derivada 1
<img width="2095" height="1769" alt="GustavoHIPOVENT1" src="https://github.com/user-attachments/assets/26095102-efc9-4387-8b4f-caca5027f3a2" />
<img width="518" height="228" alt="GustavoHIPOVENT1 resultado " src="https://github.com/user-attachments/assets/de7f499c-dfe9-40dd-b395-008eb2ea5111" />


- Características observadas:
  - .
### Prueba 5.2: Hipoventilación - Derivada 2
<img width="2084" height="1769" alt="GustavoHIPOVENT2" src="https://github.com/user-attachments/assets/aa7e1cfb-9b6d-40be-9c43-a44e76da4d4b" />
<img width="467" height="217" alt="GustavoHIPOVENT2 resultado" src="https://github.com/user-attachments/assets/000633e5-692e-4961-9a80-b9199a0e9c7b" />


- Características observadas:
### Prueba 5.3: Hipoventilación - Derivada 3
<img width="2084" height="1769" alt="GustavoHIPOVENT3" src="https://github.com/user-attachments/assets/7f8d41bf-228b-4203-887a-f9e3f0c34c59" />
<img width="467" height="222" alt="GustavoHIPOVENT3 resultado" src="https://github.com/user-attachments/assets/8ed0222c-b2cf-4340-b85b-c99b5bf8e6c7" />


- Características observadas:
  - .
## Discusión
1. ¿Cuáles son los tipos de ruidos más comunes que afectan la señal ECG?

Los tipos de ruido más comunes son la actividad muscular, el ruido blanco Gaussiano, baseline wander e interferencia de la red eléctrica [1]. La actividad muscular produce un ruido que se manifiesta como temblores irregulares en la línea base y para reducirlo se solicita al paciente permanecer inmóvil. Otras distorsiones en la señal son causadas por el ruido blanco Gaussiano que es caracterizado por ser aleatorio y tener distribución normal, es causado por fenómenos físicos aleatorios e independientes.

También, se van interferencias como el baseline wander a causa de la respiración, el movimiento del paciente o electrodos cargados negativamente. Su frecuencia suele estar en el rango de 0 a 0.5 Hz. Por último, tenemos la interferencia de la red eléctrica que es un artefacto común a varios tipos de mediciones y se produce típicamente entre 50-60 Hz generando ondas gruesas que distorsionan la señal y puede ser originada por una mala conexión a tierra, cables mal colocados o equipos cercanos

2. ¿Por qué el cambio de posición en los sensores (derivadas I-III) cambian los componentes de la señal ECG? ¿Cómo cambian estos componentes?

Esto sucede porque cada derivación nos da una perspectiva distinta del vector eléctrico del corazón. Al mover el sitio de electrodos cambiamos la observación por ello cuando el impulso va hacia el polo positivo se registra hacia arriba mientras que si se aleja irá hacia abajo. Respecto a las características en D-I, se muestran ondas P positivas pequeñas y la onda R modesta. Para D-II se observan en general amplitudes más altas especialmente en R, una morfología redondeada en P y una onda T mayor en comparación con D-I. Finalmente, en D-III se muestran ondas T más bajas o invertidas y ondas R variables.

3. Existen grandes diferencias en la señal cuando se adquiere de distintas partes del cuerpo ¿Cuál puede ser la causa? ¿Se esperan estos cambios en la señal?
- Orientación del vector eléctrico cardíaco [1]
  Cada derivación registra la proyección del vector desde un ángulo distinto.
- Posición relativa al corazón [1]
  Electrodos más cercanos o alineados con el eje cardíaco captan señales de mayor amplitud.
- Conductividad de los tejidos [1]
  Músculo, grasa, hueso y piel afectan la propagación de la señal, lo cual varía en distintas partes del cuerpo.
Debido a estas causas, es muy común esperar cambios para analizar distintos puntos de vista para el análisis de las señales del corazón.

4. ¿Los diferentes tipos de respiración (p. ej., más rápida, más profunda) influyen en las señales del ECG? En base a las señales del ECG mostradas anteriormente en diferentes circunstancias respiratorias, se describen las variaciones.
Sí influyen en las señales, se tienen las siguientes variaciones:
### Frecuencia cardíaca
Reposo: Frecuencia estable con ligera arritmia sinusal respiratoria normal.
Hipoventilación: Disminuye la frecuencia cardíaca debido a mayor actividad parasimpática y retención de CO₂.
Hiperventilación: Aumenta la frecuencia cardíaca por activación simpática y disminución de CO₂.
### Intervalos (RR)
Reposo: Intervalos regulares con pequeñas variaciones fisiológicas.
Hipoventilación: Intervalos RR más largos por latidos más separados.
Hiperventilación: Intervalos RR más cortos por latidos más frecuentes.
### Amplitud del QRS
Reposo: Amplitud estable.
Hipoventilación: Puede aumentar ligeramente por menor movimiento torácico y posición más estable del corazón.
Hiperventilación: Varía por cambios rápidos en la posición del corazón y en la impedancia torácica.
### Artefactos
Reposo: Bajos.
Hipoventilación: Muy bajos.
Hiperventilación: Aumentan debido al movimiento, tensión muscular y respiración forzada.


5. ¿Cómo influye el movimiento en la señal ECG?

El movimiento introduce artefactos de movimiento, que son de las principales fuentes de ruido en el ECG:
Los electrodos se desplazan ligeramente sobre la piel, cambiando la impedancia en la interfaz electrodo-piel y generando variaciones de voltaje no cardíacas.
La contracción muscular(EMG) produce señales eléctricas propias que se superponen a la señal ECG, distorsionando la forma de onda.
El resultado es que las ondas P, QRS y T pueden quedar distorsionadas, dificultando su interpretación.

6. ¿Cómo detectar bradicardia y taquicardia en el ECG?

Ambas se detectan midiendo la frecuencia cardíaca (FC) a partir del intervalo R-R:
| Condición | Frecuencia cardíaca | Intervalo R-R |
|-----------|-------------------|---------------|
| *Normal* | 60–100 bpm | ~0.6–1.0 s |
| *Bradicardia* | < 60 bpm | > 1.0 s (intervalos más largos) |
| *Taquicardia* | > 100 bpm | < 0.6 s (intervalos más cortos) |

En bradicardia: los complejos QRS están muy separados entre sí, el corazón late lento.
En taquicardia: los complejos QRS están muy juntos, el corazón late rápido.

## Limitaciones

## Referencias
[1] MedlinePlus. Electrocardiograma. Disponible en: https://medlineplus.gov/spanish/pruebas-de-laboratorio/electrocardiograma/
[2] PLUX. BITalino Home Guide: Electrocardiography ECG. Disponible en: https://www.plux.info/docs/bitalino-home-guide
[3] A. Azzouz et al. , “Una técnica eficiente de eliminación de ruido en señales de ECG basada en la combinación de optimización por enjambre de partículas y transformada wavelet”, Heliyon , vol. 10, n.º 5, pág. e26171, marzo de 2024, doi: https://doi.org/10.1016/j.heliyon.2024.e26171.
‌
