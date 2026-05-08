# Filtro Notch aplicado a señales biomédicas EMG, EKG y EEG

## 1. Introducción

En el procesamiento de señales biomédicas, los filtros digitales permiten reducir componentes no deseados de una señal sin eliminar la información fisiológica más importante. En señales como EMG, EKG y EEG, uno de los ruidos más frecuentes es la interferencia de la red eléctrica, conocida como power line interference o PLI.

Para esta actividad se describe el filtro Notch, también conocido como filtro rechaza banda estrecho. Este filtro se utiliza para atenuar una frecuencia específica, normalmente 50 Hz o 60 Hz, dependiendo de la frecuencia eléctrica del país. En Perú, la red eléctrica trabaja a 60 Hz, por lo que este filtro suele configurarse alrededor de 60 Hz.

## 2. ¿Qué es un filtro Notch?

Un filtro Notch es un tipo de filtro digital que elimina o atenúa fuertemente una banda muy estrecha de frecuencias, mientras deja pasar el resto de componentes de la señal.

A diferencia de un filtro pasa baja, pasa alta o pasa banda, el filtro Notch se centra en rechazar una frecuencia puntual. Por ejemplo, si una señal biomédica está contaminada por ruido eléctrico de 60 Hz, se puede aplicar un filtro Notch centrado en 60 Hz para disminuir esa interferencia.

También puede considerarse como un caso específico de filtro rechaza banda, pero con una banda de rechazo mucho más angosta.

## 3. Ruido que elimina

El principal ruido que elimina el filtro Notch es la interferencia de la red eléctrica.

Este ruido aparece porque los equipos biomédicos, electrodos, cables y amplificadores pueden captar campos electromagnéticos producidos por la corriente alterna de tomacorrientes, lámparas, computadoras u otros dispositivos eléctricos cercanos.

Las frecuencias más comunes de este ruido son:

- 50 Hz: común en varios países de Europa, Asia y otras regiones.
- 60 Hz: común en países como Perú y Estados Unidos.
- Armónicos: pueden aparecer en 100 Hz, 120 Hz, 150 Hz, 180 Hz, etc., dependiendo de si la frecuencia base es 50 Hz o 60 Hz.

Por ejemplo, si la frecuencia base es 60 Hz, sus armónicos serían 120 Hz, 180 Hz y 240 Hz. Si la frecuencia base es 50 Hz, sus armónicos serían 100 Hz, 150 Hz y 200 Hz.

## 4. Aplicación en señales EMG

La señal EMG registra la actividad eléctrica de los músculos. Esta señal puede contaminarse fácilmente con interferencia eléctrica, especialmente cuando los electrodos o cables están cerca de fuentes de corriente alterna.

En EMG, el filtro Notch se usa para reducir el ruido de 50 Hz o 60 Hz. Sin embargo, se debe aplicar con cuidado, porque parte de la información útil del EMG también puede estar cerca de esas frecuencias. Por eso, si se usa un Notch demasiado ancho, puede eliminar información muscular real.

Ejemplo:

- Señal útil EMG: actividad muscular.
- Ruido frecuente: interferencia eléctrica de 60 Hz.
- Filtro aplicado: Notch centrado en 60 Hz.
- Resultado esperado: señal EMG más limpia para analizar contracciones musculares.

## 5. Aplicación en señales EKG

La señal EKG o ECG registra la actividad eléctrica del corazón. En esta señal, la interferencia de la red eléctrica puede aparecer como una oscilación rápida superpuesta al trazado cardíaco.

El filtro Notch puede ayudar a reducir el ruido de 50 Hz o 60 Hz para que se observen mejor las ondas P, el complejo QRS y la onda T. Sin embargo, debe usarse con cuidado, porque algunos filtros pueden generar distorsiones si la banda de rechazo es muy amplia o si el filtro produce efectos transitorios.

Ejemplo:

- Señal útil EKG: ondas P, QRS y T.
- Ruido frecuente: interferencia eléctrica de 60 Hz.
- Filtro aplicado: Notch centrado en 60 Hz.
- Resultado esperado: trazado cardíaco con menor ruido eléctrico.

## 6. Aplicación en señales EEG

La señal EEG registra la actividad eléctrica cerebral. Como esta señal tiene amplitudes muy pequeñas, es bastante sensible al ruido externo, especialmente al ruido de la red eléctrica.

En EEG, el filtro Notch se usa para reducir la interferencia de 50 Hz o 60 Hz. Esto permite observar con mayor claridad ritmos cerebrales como alfa, beta, theta o delta. Aun así, se recomienda revisar si la frecuencia eliminada no afecta componentes importantes del análisis, especialmente cuando se estudian señales cercanas a 50 Hz o 60 Hz.

Ejemplo:

- Señal útil EEG: ritmos cerebrales.
- Ruido frecuente: interferencia eléctrica de 60 Hz.
- Filtro aplicado: Notch centrado en 60 Hz.
- Resultado esperado: señal EEG con menor contaminación eléctrica.

## 7. Frecuencias de ruido asociadas

| Tipo de ruido | Frecuencia típica | Señales afectadas | Comentario |
|---|---:|---|---|
| Interferencia de red eléctrica | 50 Hz | EMG, EKG, EEG | Frecuencia común en algunos países |
| Interferencia de red eléctrica | 60 Hz | EMG, EKG, EEG | Frecuencia común en Perú |
| Armónicos de 50 Hz | 100 Hz, 150 Hz, 200 Hz | EMG, EKG, EEG | Pueden aparecer por equipos eléctricos |
| Armónicos de 60 Hz | 120 Hz, 180 Hz, 240 Hz | EMG, EKG, EEG | Pueden requerir filtros adicionales |

## 8. Ventajas del filtro Notch

- Es útil para eliminar una frecuencia específica.
- Puede mejorar la visualización de señales biomédicas contaminadas por ruido eléctrico.
- Es fácil de implementar en Python, MATLAB o sistemas embebidos.
- Puede aplicarse en EMG, EKG y EEG.
- No elimina todo un rango amplio de frecuencias, sino una zona puntual.

## 9. Limitaciones

Aunque el filtro Notch es muy usado, no siempre debe aplicarse automáticamente. Si la señal biomédica tiene información útil cerca de 50 Hz o 60 Hz, el filtro puede eliminar parte de esa información.

Además, si el ruido eléctrico varía ligeramente, por ejemplo de 60 Hz a 59.5 Hz o 60.5 Hz, un filtro Notch muy estrecho podría no eliminarlo completamente. Por eso, en algunos casos se usan filtros adaptativos o métodos alternativos.

## 10. Ejemplo básico en Python

```python
from scipy import signal

fs = 1000      # Frecuencia de muestreo en Hz
f0 = 60        # Frecuencia que se desea eliminar
Q = 30         # Factor de calidad del filtro

b, a = signal.iirnotch(f0, Q, fs)

# x representa la señal biomédica original
# y representa la señal filtrada
y = signal.filtfilt(b, a, x)
