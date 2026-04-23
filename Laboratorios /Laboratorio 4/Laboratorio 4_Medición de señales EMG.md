# Electromiografía (EMG) – Análisis de señales musculares

## Introducción
La electromiografía (EMG) es una técnica utilizada para medir la actividad eléctrica generada por los músculos durante su contracción. Esta señal refleja la suma de los potenciales de acción de las fibras musculares, permitiendo evaluar el funcionamiento neuromuscular [1].

Las señales EMG pueden ser registradas mediante electrodos de superficie, lo que permite analizar la activación muscular de manera no invasiva en diferentes condiciones, como reposo y contracción [2]. Estas mediciones son ampliamente utilizadas tanto en el ámbito clínico como en investigación, para el estudio del control muscular y la evaluación de trastornos neuromusculares [3].

En este laboratorio se adquirieron señales EMG de distintos grupos musculares, como el bíceps y el trapecio superior, utilizando el sistema BITalino, con el objetivo de analizar sus características en el dominio del tiempo y su relación con la actividad muscular.

---

## Objetivos
*   **Adquisición de señales:** Capturar biopotenciales de EMG utilizando el kit BITalino bajo tres condiciones fisiológicas: reposo, contracción leve y contracción con carga.
*   **Análisis de datos:** Comprender el uso de software especializado para la visualización de resultados y realizar el análisis de las señales obtenidas.
*   **Procesamiento:** Identificar componentes de ruido y evaluar la importancia del filtrado en bioseñales.

## Metodología

### Componentes:
| Componente | Descripción |
|-----------|------------|
| BITalino | Sistema de adquisición de señales biomédicas |
| Electrodos EMG | Electrodos de superficie para registro muscular |
| Cables | Conexión de electrodos al dispositivo |
| Computadora | Registro y visualización de datos |


### Ubicación de electrodos

Se utilizó una configuración bipolar:

- Dos electrodos activos colocados sobre el músculo de interés  
- Un electrodo de referencia en una zona neutra (estructura ósea)

Los electrodos se colocaron alineados con la dirección de las fibras musculares y con una separación aproximada de 2 cm entre centros.


#### Bíceps braquial

Los electrodos activos se colocaron sobre el músculo bíceps, siguiendo la orientación de las fibras musculares.  
El electrodo de referencia se ubicó en el codo.

<img width="567" height="273" alt="Biceps_electrodos" src="https://github.com/user-attachments/assets/3a756d08-90c9-427a-9ec5-e47b86f60e68" />

Fig 1. Posicionamiento de electrodos en el bíceps braquial. Extraído de BITalino (r)evolution Home Guide [4]

#### Trapecio superior

Los electrodos activos se colocaron en la región superior del músculo trapecio, sobre el vientre muscular.  
El electrodo de referencia se ubicó en una zona neutra, específicamente en la apófisis mastoides (región ósea detrás de la oreja).

<img width="567" height="273" alt="Trapecio_electrodos" src="https://github.com/user-attachments/assets/a382c9c9-8c1d-4341-99c0-1d35957a83e9" />

Fig 2. Posicionamiento de electrodos en el trapecio descendente. Extraído de BITalino (r)evolution Home Guide [4]

---

## Resultados

Las señales EMG fueron adquiridas con el sistema BITalino a una frecuencia de muestreo de 1000Hz. Se analizaron dos canales correspondientes al músculo bíceps braquial y al trapecio superior.

### Comportamiento general de la señal

- Se registraron dos patrones diferenciados entre los canales.
- Se identificaron ciclos repetitivos de activación (picos) y relajación.
- La señal presenta variabilidad incluso en periodos de reposo.

### Canal 1 – Bíceps braquial
### Prueba 1: Reposo

- Valores aproximados:
  - Máximos: 
  - Mínimos: 

- Características observadas:
  - FALTA 

### Canal 2 – Trapecio superior

- Valores aproximados:
  - Rango:

- Características observadas:
  - FALTA
 
---


---

## Discusión

### Análisis de resultados

ACA HAGAN UN ANALISIS DE LOS RESULTADOS

### Respuestas a las preguntas

### **P1. ¿Cuáles son las frecuencias significativas para las adquisiciones de EMG?**

Desde una perspectiva fisiológica y de análisis de señales, el espectro de potencia de una señal EMG de superficie se distribuye predominantemente en el rango de los **$20 \text{ Hz}$ a los $500 \text{ Hz}$**. 

No obstante, el intervalo de mayor relevancia diagnóstica, donde se concentra la máxima densidad espectral y la mayor información de las unidades motoras, se encuentra entre los **$50 \text{ Hz}$ y $150 \text{ Hz}$**. Las componentes de frecuencia por debajo de los $20 \text{ Hz}$ suelen ser descartadas en el procesamiento, ya que generalmente corresponden a:
* Artefactos de movimiento (ruido mecánico).
* Inestabilidad en la interfaz electrodo-piel.

---

### **P2. ¿Qué tipo de filtro es esencial al trabajar con señales EMG?**

Para el procesamiento de señales EMG, es imperativo implementar una arquitectura de filtrado digital que combine dos etapas críticas:

1.  **Filtro Notch (Elimina-banda):** Sintonizado específicamente a **$60 \text{ Hz}$** (frecuencia de la red eléctrica local). Su función es suprimir la interferencia electromagnética captada por el cuerpo humano, el cual actúa como antena receptora del ruido de línea.
2.  **Filtro Pasa-banda (Band-pass):** Generalmente un filtro *Butterworth* de orden superior con frecuencias de corte entre **$20 \text{ Hz}$ y $450 \text{ Hz}$**. Este filtro es esencial para delimitar la ventana de información biológica, atenuando tanto el ruido de baja frecuencia (movimiento) como el ruido térmico de alta frecuencia ajeno a la actividad muscular.

---

### **P3. ¿En qué se diferencia la amplitud en cada contracción muscular?**

La variación en la amplitud de la señal (medida en $\mu V$ o $mV$ pico a pico) es el reflejo de dos mecanismos neurofisiológicos de control:

* **Reclutamiento de unidades motoras:** A mayor demanda de carga, el sistema nervioso activa un mayor número de fibras musculares siguiendo el *principio de tamaño de Henneman*.
* **Frecuencia de disparo (Rate Coding):** El incremento en la cadencia de los impulsos nerviosos genera una sumación espacial y temporal de los potenciales de acción.

Una contracción contra carga máxima presentará ráfagas de amplitud significativamente superiores y una mayor densidad de picos comparada con una contracción leve o isométrica sin carga.

---

### **P4. Muestre una porción de la señal EMG y explíquela.**

*(Referencia al segmento de activación o "burst" observado en la sección de Resultados).*

En una ventana de tiempo reducida durante la fase de contracción, se aprecia una **actividad de interferencia compleja**. 
* **Los picos de voltaje:** Representan la despolarización asincrónica de las membranas de las fibras musculares en respuesta a los potenciales de acción. La densidad y magnitud de estos picos son indicadores directos de la intensidad del esfuerzo y el reclutamiento de fibras.
* **Segmentos de línea base:** Los periodos de retorno a la línea base o baja amplitud indican los periodos de reposo relativo o la repolarización celular previa a un nuevo ciclo de activación voluntaria.

---

### **P5. ¿La amplitud de la EMG es igual a la fuerza muscular?**

Científicamente, **no existe una equivalencia lineal o igualdad absoluta** entre ambos parámetros. 

* **EMG:** Mide exclusivamente la **actividad eléctrica** (el comando neural y la respuesta electroquímica de la membrana).
* **Fuerza:** Es un **resultado mecánico** influenciado por variables biomecánicas como el ángulo articular, la velocidad de contracción, la longitud del sarcómero y la fatiga muscular. 

**Ejemplo crítico:** En estado de fatiga, la señal EMG puede mostrar una amplitud elevada debido a un intento del sistema nervioso por compensar la pérdida de eficiencia muscular mediante más reclutamiento, mientras que la fuerza mecánica producida disminuye drásticamente.

#### Q5. Does EMG amplitude equal muscle force?

No. La amplitud de la señal EMG está relacionada con la activación muscular, pero no es una medida directa de la fuerza generada.

---

## Limitaciones
FALTA

---

## Referencias

[1] MedlinePlus. “Electromiografía y estudios de conducción nerviosa.” Disponible en: https://medlineplus.gov/spanish/pruebas-de-laboratorio/electromiografia-y-estudios-de-conduccion-nerviosa/

[2] Merletti R., Parker P. “Electromyography: physiology, engineering, and noninvasive applications.” Disponible en: https://pmc.ncbi.nlm.nih.gov/articles/PMC1455479/

[3] Farina D. et al. “The extraction of neural strategies from the surface EMG.” Disponible en: https://pmc.ncbi.nlm.nih.gov/articles/PMC7755956/

[4] “BITalino (r)evolution Lab Guide.” Disponible en: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf
