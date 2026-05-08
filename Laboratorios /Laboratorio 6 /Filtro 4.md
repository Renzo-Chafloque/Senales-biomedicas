# Filtro Notch aplicado a señales biomédicas EMG, EKG y EEG

## 1. ¿Qué es un filtro Notch?

En el procesamiento de señales biomédicas, los filtros digitales permiten reducir componentes no deseados de una señal sin eliminar la información fisiológica más importante. En señales como EMG, EKG y EEG, uno de los ruidos más frecuentes es la interferencia de la red eléctrica, conocida como *power line interference* o PLI.

Un filtro Notch es un tipo de filtro digital que elimina o atenúa fuertemente una banda muy estrecha de frecuencias, mientras deja pasar el resto de componentes de la señal. A diferencia de un filtro pasa baja, pasa alta o pasa banda, el filtro Notch se centra en rechazar una frecuencia puntual. Por ejemplo, si una señal biomédica está contaminada por ruido eléctrico de 60 Hz, se puede aplicar un filtro Notch centrado en 60 Hz para disminuir esa interferencia.

Este filtro es útil porque no elimina un rango amplio de frecuencias, sino solo una zona puntual, lo que lo hace especialmente útil en el tratamiento de señales como EMG, EKG y EEG, donde la interferencia de la red eléctrica puede ser un problema frecuente.

## 2. Ruido que elimina

El principal ruido que elimina el filtro Notch es la interferencia de la red eléctrica. Este ruido aparece porque los equipos biomédicos, electrodos, cables y amplificadores pueden captar campos electromagnéticos producidos por la corriente alterna de tomacorrientes, lámparas, computadoras u otros dispositivos eléctricos cercanos. Las frecuencias más comunes de este ruido son:

- 50 Hz: común en varios países de Europa, Asia y otras regiones [2].
- 60 Hz: común en países como Perú y Estados Unidos [3].
- Armónicos: pueden aparecer en 100 Hz, 120 Hz, 150 Hz, 180 Hz, etc., dependiendo de si la frecuencia base es 50 Hz o 60 Hz [4].

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

[1] Levkov, C., Mihov, G., Ivanov, R., Daskalov, I., Christov, I., & Dotsinsky, I. (2005). Removal of power-line interference from the ECG: a review of the subtraction procedure. *BioMedical Engineering OnLine*, 4, 50. https://doi.org/10.1186/1475-925X-4-50

[2] Leske, S., & Dalal, S. S. (2019). Reducing power line noise in EEG and MEG data via spectrum interpolation. *NeuroImage*, 189, 763-776. https://doi.org/10.1016/j.neuroimage.2019.01.026

[3] Li, X., Rymer, W. Z., Li, G., & Zhou, P. (2011). The effects of notch filtering on electrically evoked myoelectric signals and associated motor unit index estimates. *Journal of NeuroEngineering and Rehabilitation*, 8, 64. https://doi.org/10.1186/1743-0003-8-64

[4] Ládrová, M., Martínek, R., Nedoma, J., & Fajkus, M. (2019). Methods of Power Line Interference Elimination in EMG Signal. *Journal of Biomimetics, Biomaterials and Biomedical Engineering*, 40, 64-70. https://doi.org/10.4028/www.scientific.net/JBBBE.40.64

[5] Tyrpa, M., & Piskorowski, J. (2025). Rejection of Power-Line Interference in EMG Signals Using a Notch Filter Initialized with Non-Zero States. *Pomiary Automatyka Robotyka*, 3/2025. https://doi.org/10.14313/PAR_257/13
