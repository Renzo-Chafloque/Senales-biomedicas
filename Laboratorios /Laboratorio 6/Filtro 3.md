# Filtro Elíptico (Cauer) — Procesamiento de Señales Biomédicas (EMG, EKG, EEG)

> **Semana 06 · Filtros Digitales para Bioseñales**  
> Tipo de filtro presentado: **Filtro Elíptico (Cauer)**

---

## 1. Descripción General

El **filtro elíptico**, también denominado **filtro de Cauer** en honor al matemático alemán Wilhelm Cauer, es un filtro IIR (*Infinite Impulse Response*) que se distingue por poseer el *roll-off* más pronunciado posible para un orden dado, entre todos los filtros clásicos de aproximación racional [1]. Su característica definitoria es el comportamiento **equiripple** simultáneo tanto en la banda de paso como en la banda de rechazo: los rizos (*ripples*) en ambas bandas son de amplitud constante y controlable de forma independiente [2].

Esta propiedad lo diferencia fundamentalmente del filtro de Butterworth (passband plano, sin ceros de transmisión finitos) y del filtro de Chebyshev (equiripple únicamente en una banda). Al admitir ripple en **ambas** bandas, el filtro elíptico logra la transición más estrecha posible entre la banda de paso y la de rechazo para un mismo orden de filtro, lo que resulta esencial cuando los recursos computacionales o de hardware son limitados [1][3].

---

## 2. Fundamento Matemático

### 2.1 Función de Transferencia

La función de transferencia general del filtro elíptico se expresa como:

$$H(s) = k \cdot \frac{\prod_{i=1}^{r}(s - z_i)}{\prod_{i=1}^{n}(s - p_i)}$$

donde $z_i$ son los **ceros de transmisión** (ubicados sobre el eje $j\omega$, en la banda de rechazo), $p_i$ son los **polos** (en el semiplano izquierdo del plano $s$, garantizando estabilidad), $k$ es la ganancia y $n$ el orden del filtro [2][3].

A diferencia de Butterworth y Chebyshev, el filtro elíptico posee **ceros finitos** en su numerador. Estos ceros generan atenuación infinita en frecuencias discretas de la banda de rechazo, produciendo las características "notch" que contribuyen a su pronunciada selectividad [2].

### 2.2 Respuesta en Magnitud al Cuadrado

$$|H(j\omega)|^2 = \frac{1}{1 + \varepsilon^2 R_n^2(\omega, \xi)}$$

donde $R_n(\omega, \xi)$ es la **función racional elíptica de Chebyshev** de orden $n$ (construida a partir de funciones elípticas de Jacobi), $\varepsilon$ controla la amplitud del ripple en la banda de paso, y $\xi$ es el factor de selectividad que determina la relación entre las frecuencias de corte del passband y stopband [2][3].

### 2.3 Parámetros Clave de Diseño

| Parámetro | Símbolo | Descripción |
|---|---|---|
| Orden del filtro | $n$ | Determina el número de polos/ceros |
| Ripple en passband | $R_p$ (dB) | Variación máxima en banda de paso |
| Atenuación en stopband | $R_s$ (dB) | Rechazo mínimo en banda de rechazo |
| Frecuencia de corte passband | $\omega_p$ | Límite superior de la banda de paso |
| Frecuencia de corte stopband | $\omega_s$ | Inicio de la banda de rechazo |

> **Ventaja de orden mínimo:** Para las mismas especificaciones de $R_p$, $R_s$, $\omega_p$ y $\omega_s$, el filtro elíptico requiere el **menor orden** de todos los filtros IIR clásicos, reduciendo así la latencia computacional y el consumo de recursos en implementaciones embebidas [1][4].

---

## 3. Tipos de Ruido que Elimina

El filtro elíptico puede configurarse como **pasa-bajas, pasa-altas, pasa-banda o rechaza-banda**, lo que le permite atacar prácticamente cualquier tipo de interferencia presente en señales biomédicas. Los artefactos más relevantes que elimina son:

### 3.1 Interferencia de Línea de Alimentación (Power Line Interference — PLI)
- **Frecuencia:** 50 Hz (Europa/Perú) o 60 Hz (Norteamérica), con armónicos a 100/120 Hz, 150/180 Hz, etc.
- **Aplicación:** Configurado como filtro **rechaza-banda (notch)** centrado en 50/60 Hz con transición muy estrecha, el filtro elíptico elimina la PLI sin deteriorar las componentes espectrales adyacentes de la señal biológica, algo crítico en EKG donde el intervalo QRS tiene energía entre 5–40 Hz [4].

### 3.2 Artefactos de Movimiento de Electrodo (Baseline Wander)
- **Frecuencia:** 0.05 – 0.5 Hz
- **Aplicación:** Configurado como **pasa-altas** con $f_c$ ≈ 0.5 Hz (EKG) o ≈ 0.1 Hz (EMG), elimina las derivas de línea de base producidas por la respiración o el movimiento del sujeto, preservando el contenido diagnóstico de la señal [4].

### 3.3 Ruido de Alta Frecuencia / Ruido Muscular (EMG como artefacto en EEG/EKG)
- **Frecuencia:** > 100 Hz (para EKG), > 50 Hz (para EEG)
- **Aplicación:** Configurado como **pasa-bajas**, rechaza el ruido de alta frecuencia generado por contracciones musculares involuntarias (EMG noise) que se superponen sobre la señal de interés. En EKG, por ejemplo, el rango diagnóstico es 0.5–150 Hz, por lo que el filtro pasa-bajas se diseña con $f_c$ = 150 Hz y alta atenuación para frecuencias mayores [4].

### 3.4 Ruido Gaussiano Blanco Aditivo (AWGN)
- **Frecuencia:** Distribución espectral plana (wideband)
- **Aplicación:** Un filtro elíptico pasa-banda con banda ajustada al espectro de la señal de interés suprime el ruido de fondo de instrumentación, el ruido térmico de los amplificadores y el ruido cuántico del ADC. En implementaciones FPGA se ha demostrado una mejora de SNR de hasta **81.11%** sobre bases de datos MIT-BIH [4].

---

## 4. Rangos de Frecuencia Relevantes por Señal

| Señal | Banda de interés | Artefactos dominantes | Configuración típica del filtro elíptico |
|---|---|---|---|
| **EKG** | 0.5 – 150 Hz | PLI (50/60 Hz), baseline wander (<0.5 Hz), EMG noise (>150 Hz) | BP elíptico: $f_{low}$ = 0.5 Hz, $f_{high}$ = 150 Hz; Notch en 50 Hz [4] |
| **EEG** | 0.5 – 50 Hz | PLI, artefactos de movimiento ocular (EOG, <4 Hz), ruido muscular (>40 Hz) | BP elíptico: 0.5–50 Hz, orden 4, implementado en secciones de segundo orden (SOS) [5] |
| **EMG** | 20 – 500 Hz | PLI (50/60 Hz), ruido de movimiento (<20 Hz), ruido electrónico (>500 Hz) | HP: 20 Hz + LP: 500 Hz, con notch en 50/60 Hz |

---

## 5. Aplicación en Señales Biomédicas

### 5.1 EKG — Eliminación Multiruido en FPGA

Makkapati y Rao (2024) propusieron un sistema de tres filtros IIR elípticos en cascada (estructura Direct Form II) implementado sobre FPGA Xilinx Zynq 7000 para eliminar simultáneamente Baseline Wander (BW), Electrode Motion (EM), Power Line Interference (PLI), ruido EMG y AWGN en señales EKG. El sistema fue validado con **376 registros** de las bases de datos ECG-ID, MIT-BIH Normal Sinus Rhythm y MIT-BIH Arrhythmia, alcanzando mejoras de SNR de 81.11%, 88.89% y 85.41% respectivamente, con un consumo de solo **0.321 W** en chip [4]. La eficiencia de recursos fue del 3.87%, lo que evidencia la ventaja del orden mínimo del filtro elíptico frente a otros tipos.

```
Cascada de filtros elípticos para EKG:
  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
  │  High-Pass  │───▶│   Low-Pass  │───▶│  Band-Stop  │
  │  fc=0.5 Hz  │    │ fc=150 Hz   │    │  fc=50 Hz   │
  │  orden=4    │    │  orden=4    │    │  orden=4    │
  └─────────────┘    └─────────────┘    └─────────────┘
        ↑ Elimina          ↑ Elimina         ↑ Elimina
    Baseline Wander    EMG + AWGN alto     PLI (50 Hz)
```

### 5.2 EEG — Comparación Cuantitativa de Filtros

Russell et al. (2026) realizaron un estudio comparativo con datos de **49 adultos sanos** (EEG de 256 canales a 512 Hz) aplicando filtros pasa-banda de 0.5–50 Hz con cuatro diseños: Butterworth, Chebyshev I, Elíptico y "Reza". Los resultados mediante ANOVA de medidas repetidas (con corrección Bonferroni) mostraron que el filtro **elíptico y el Chebyshev produjeron el mayor SNR** (sin diferencia estadística entre sí), superando significativamente a Butterworth ($p < 0.001$) [5]. El filtro elíptico fue implementado en forma de **secciones de segundo orden (SOS)** — metodología recomendada para evitar inestabilidades numéricas en órdenes altos [5].

> *"Chebyshev and elliptic yielded the highest mean SNR and did not differ from each other, while both exceeded Butterworth."* — Russell et al., Sensors (MDPI), 2026 [5]

### 5.3 Ventaja del Filtro Elíptico: Trade-off Óptimo

El filtro elíptico representa el compromiso matemáticamente óptimo entre orden del filtro, ancho de la banda de transición y ripple: al permitir ripple en ambas bandas, maximiza la selectividad frecuencial con el mínimo número de polos/ceros, reduciendo la carga computacional sin sacrificar el rendimiento de filtrado [1][2]. En el procesamiento biomédico en tiempo real —donde la latencia y el consumo energético son críticos— esta ventaja es determinante.

---

## 6. Comparación con Otros Filtros IIR Clásicos

| Característica | Butterworth | Chebyshev I | Chebyshev II | **Elíptico (Cauer)** |
|---|---|---|---|---|
| Passband | Plano (maximalmente) | Equiripple | Plano | Equiripple |
| Stopband | Monótono | Monótono | Equiripple | **Equiripple** |
| Roll-off para mismo orden | Más suave | Moderado | Moderado | **Más pronunciado** |
| Orden mínimo requerido | Mayor | Menor | Menor | **Mínimo** |
| Ceros de transmisión finitos | No | No | Sí | **Sí** |
| Fase no lineal | Baja | Moderada | Moderada | **Alta** |
| Complejidad de diseño | Baja | Media | Media | **Alta** |

> ⚠️ **Limitación:** El filtro elíptico presenta la respuesta de fase más no lineal de todos los filtros IIR clásicos. En aplicaciones donde la distorsión de fase es crítica (p.ej., análisis de morfología de onda en EKG o latencia de pico en EEG), puede requerirse aplicación bidireccional (`filtfilt`) o compensación de fase para preservar la forma de onda [5].

---

## Referencias

[1] "Elliptic Filters — an overview," *ScienceDirect Topics*, Elsevier, 2026. Disponible en: https://www.sciencedirect.com/topics/engineering/elliptic-filters [Accedido: 8-may-2026].

[2] P. Prommee, N. Wongprommoon, M. Kumngern y W. Jaikla, "Low-Voltage Low-Pass and Band-Pass Elliptic Filters Based on Log-Domain Approach Suitable for Biosensors," *Sensors*, vol. 19, no. 24, art. 5581, MDPI, dic. 2019, doi: 10.3390/s19245581. Disponible en: https://www.mdpi.com/1424-8220/19/24/5581 [Accedido: 8-may-2026].

[3] K. Srilakshmi y D. Venkata Lakshmi, "Design and Implementation of Butterworth, Chebyshev-I and Elliptic Filter for Speech Signal Analysis," *arXiv preprint*, arXiv:2002.03130, 2020. Disponible en: https://arxiv.org/pdf/2002.03130 [Accedido: 8-may-2026].

[4] S. S. Makkapati y N. Nagamalleswara Rao, "FPGA implementation of IIR elliptic filters for de-noising ECG signal," *Biomedical Signal Processing and Control*, vol. 96, parte B, art. 106636, 2024, doi: 10.1016/j.bspc.2024.106636. Disponible en: https://www.sciencedirect.com/science/article/abs/pii/S1746809424006025 [Accedido: 8-may-2026].

[5] D. M. Russell, D. C. Monroe y C. K. Rhea, "EEG and IMU Gait Signal Processing: A Comparative Assessment of the 'Reza' Exponential Filter and Classical Filters," *Sensors*, vol. 26, no. 5, art. 1719, MDPI, mar. 2026, doi: 10.3390/s26051719. Disponible en: https://www.mdpi.com/1424-8220/26/5/1719 [Accedido: 8-may-2026].
