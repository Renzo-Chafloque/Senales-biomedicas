# Filtro Wavelet Discreto (Discrete Wavelet Transform, DWT)

## 1. Introducción y ¿Qué es un filtro Wavelet?

El filtro basado en Transformada Wavelet Discreta (DWT) es una técnica de procesamiento digital de señales que descompone una señal en diferentes niveles de frecuencia y tiempo mediante funciones llamadas wavelets. A diferencia de los filtros convencionales, permite analizar señales no estacionarias, como EMG, EKG y EEG, conservando simultáneamente información temporal y espectral [1], [4].

La señal se divide en:

### Coeficientes de aproximación: Bajas frecuencias.
### Coeficientes de detalle: Altas frecuencias.

Posteriormente, los coeficientes asociados al ruido pueden reducirse o eliminarse mediante técnicas de umbralización, reconstruyendo luego la señal limpia [1].

## 2. Ruido que elimina

El filtro wavelet permite eliminar distintos tipos de ruido dependiendo del nivel de descomposición seleccionado [2].

### Ruido de alta frecuencia
Frecuencia típica: > 100 Hz
Presente principalmente en EMG y EEG.
Interferencia electrónica, ruido térmico, movimiento brusco.

Este tipo de ruido puede reducirse eliminando coeficientes wavelet de alta frecuencia [2].

### Ruido muscular
Rango aproximado: 20–300 Hz
Artefactos EMG en EEG y EKG
Produce distorsiones especialmente en EEG [4].

### Baseline wander
Frecuencia: 0–0.5 Hz
Común en EKG y EEG.
Respiración, movimiento del paciente, desplazamiento de electrodos [2].

### Ruido electromagnético
Frecuencia: 50 Hz o 60 Hz
Proveniente de la red eléctrica [3].
Aunque el DWT no es específicamente un filtro notch, puede atenuar parcialmente este ruido dependiendo de la selección de niveles wavelet [3].

El filtrado wavelet es especialmente útil en EEG debido a que la señal cerebral es altamente no estacionaria y de muy baja amplitud [4].

## 3. Aplicación en señales EMG, EKG y EEG

### EMG
La señal EMG registra la actividad eléctrica de los músculos. Esta señal puede contaminarse fácilmente con interferencia eléctrica, especialmente cuando los electrodos o cables están cerca de fuentes de corriente alterna. El filtro Notch se usa para reducir el ruido de 50 Hz o 60 Hz. Sin embargo, debe aplicarse con cuidado, porque parte de la información útil del EMG también puede estar cerca de esas frecuencias [5].

### EKG
La señal EKG o ECG registra la actividad eléctrica del corazón. En esta señal, la interferencia de la red eléctrica puede aparecer como una oscilación rápida superpuesta al trazado cardíaco. El filtro Notch puede ayudar a reducir el ruido de 50 Hz o 60 Hz para que se observen mejor las ondas P, el complejo QRS y la onda T. Debe usarse con cuidado, porque algunos filtros pueden generar distorsiones si la banda de rechazo es muy amplia [6].

### EEG
La señal EEG registra la actividad eléctrica cerebral. Como esta señal tiene amplitudes muy pequeñas, es bastante sensible al ruido externo, especialmente al ruido de la red eléctrica. El filtro Notch se usa para reducir la interferencia de 50 Hz o 60 Hz, permitiendo observar ritmos cerebrales como alfa, beta, theta o delta con mayor claridad. Se recomienda revisar si la frecuencia eliminada no afecta componentes importantes del análisis [7].

## 4. Ventajas del filtro Notch

- Elimina frecuencias específicas como el ruido de 50 Hz o 60 Hz.
- Es fácil de implementar en Python, MATLAB o sistemas embebidos.
- No elimina un rango amplio de frecuencias, solo una zona puntual.
- Es útil para mejorar la visualización de señales biomédicas contaminadas por ruido eléctrico.

## 5. Limitaciones

Aunque el filtro Notch es muy usado, no siempre debe aplicarse automáticamente. Si la señal biomédica tiene información útil cerca de 50 Hz o 60 Hz, el filtro puede eliminar parte de esa información. Además, si el ruido eléctrico varía ligeramente, por ejemplo de 60 Hz a 59.5 Hz o 60.5 Hz, un filtro Notch muy estrecho podría no eliminarlo completamente [5].

## 6. Referencias
[1] S. Al-Zoubi, A. Al-Ali, and M. Al-Ayyoub, “EMG Signal Denoising Based on Wavelet Transform,” IEEE Access, vol. 8, pp. 210054–210067, 2020.

[2] M. A. Islam, A. K. M. F. Haque, and M. T. Islam, “Power Line Interference Removal from Biomedical Signals Using Adaptive and Wavelet Filters,” Biomedical Signal Processing and Control, vol. 68, 2021.

[3] Y. Luo, R. Wang, and X. Zhao, “ECG Signal Denoising and Baseline Wander Removal Using Wavelet Transform,” Healthcare Technology Letters, vol. 9, no. 2, pp. 45–52, 2022.

[4] H. Sharma and K. Pachori, “Automatic Identification and Removal of Ocular and Muscle Artifacts from EEG Signals Using Wavelet Transform,” Biomedical Signal Processing and Control, vol. 62, 2020.
