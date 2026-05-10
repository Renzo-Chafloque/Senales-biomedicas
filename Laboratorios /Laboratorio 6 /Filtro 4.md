# Filtro Notch aplicado a señales biomédicas EMG, EKG y EEG

## 1. ¿Qué es un filtro Notch?

Un filtro Notch es un filtro digital que elimina o atenúa fuertemente una banda muy estrecha de frecuencias, mientras deja pasar el resto de componentes de la señal. A diferencia de un filtro pasa baja, pasa alta o pasa banda, el filtro Notch se centra en rechazar una frecuencia puntual. Por ejemplo, si una señal biomédica está contaminada por ruido eléctrico de 60 Hz, se puede aplicar un filtro Notch centrado en 60 Hz para disminuir esa interferencia [1].

Este filtro es útil porque no elimina un rango amplio de frecuencias, sino solo una zona puntual, lo que lo hace especialmente útil en el tratamiento de señales como EMG, EKG y EEG, donde la interferencia de la red eléctrica puede ser un problema frecuente [2].

## 2. Ruido que elimina

El principal ruido que elimina el filtro Notch es la interferencia de la red eléctrica. Este ruido aparece cuando los equipos biomédicos, electrodos, cables o amplificadores captan campos eléctricos generados por tomacorrientes, lámparas, computadoras u otros dispositivos cercanos. Las frecuencias más comunes de este ruido son 50 Hz y 60 Hz [4]. También pueden aparecer armónicos como 100 Hz, 120 Hz, 150 Hz o 180 Hz [4].

## 3. Aplicación en señales EMG, EKG y EEG

### EMG
La señal EMG registra la actividad eléctrica de los músculos. Esta señal puede contaminarse fácilmente con interferencia eléctrica, especialmente cuando los electrodos o cables están cerca de fuentes de corriente alterna [3]. El filtro Notch se usa para reducir el ruido de 50 Hz o 60 Hz. Sin embargo, debe aplicarse con cuidado, porque parte de la información útil del EMG también puede estar cerca de esas frecuencias [5].

### EKG
La señal EKG o ECG registra la actividad eléctrica del corazón. La interferencia de la red eléctrica puede aparecer como una oscilación rápida superpuesta al trazado cardíaco. El filtro Notch ayuda a reducir ese ruido para mejorar la visualización de las ondas P, el complejo QRS y la onda T [1].

### EEG
La señal EEG registra la actividad eléctrica cerebral. Como esta señal tiene amplitudes muy pequeñas, es bastante sensible al ruido externo. El filtro Notch se usa para reducir la interferencia de 50 Hz o 60 Hz, permitiendo observar ritmos cerebrales como alfa, beta, theta o delta con mayor claridad. Se recomienda revisar si la frecuencia eliminada no afecta componentes importantes del análisis [2].

## 4. Ventajas del filtro Notch

- Elimina frecuencias específicas como el ruido de 50 Hz o 60 Hz [1].  
- Es fácil de implementar en Python, MATLAB o sistemas embebidos [3].  
- No elimina un rango amplio de frecuencias, solo una zona puntual [2].  
- Mejora la visualización de señales biomédicas contaminadas por ruido eléctrico [5].

## 5. Limitaciones

Aunque el filtro Notch es muy usado, no siempre debe aplicarse automáticamente [3]. Si la señal biomédica tiene información útil cerca de 50 Hz o 60 Hz, el filtro puede eliminar parte de esa información [5]. Además, si la interferencia eléctrica varía ligeramente, por ejemplo de 60 Hz a 59.5 Hz o 60.5 Hz, un filtro Notch muy estrecho podría no eliminarlo completamente [4].

## 6. Conclusión

El filtro Notch es un filtro digital utilizado para reducir la interferencia de la red eléctrica en señales biomédicas como EMG, EKG y EEG [1]. Su función principal es atenuar una frecuencia específica, generalmente 50 Hz o 60 Hz, sin modificar demasiado el resto de la señal [2].  

En EMG ayuda a reducir ruido eléctrico que puede confundirse con actividad muscular [3]. En señales EKG mejora la visualización del trazado cardíaco [1]. En señales EEG permite disminuir la contaminación externa para observar mejor la actividad cerebral [2]. Sin embargo, debe utilizarse con cuidado, porque también puede eliminar información útil si la señal fisiológica tiene componentes cercanos a la frecuencia filtrada [5].

## 7. Referencias

[1] Levkov, C., Mihov, G., Ivanov, R., Daskalov, I., Christov, I., & Dotsinsky, I. (2005). Removal of power-line interference from the ECG: a review of the subtraction procedure. *BioMedical Engineering OnLine*, 4, 50. https://doi.org/10.1186/1475-925X-4-50

[2] Leske, S., & Dalal, S. S. (2019). Reducing power line noise in EEG and MEG data via spectrum interpolation. *NeuroImage*, 189, 763-776. https://doi.org/10.1016/j.neuroimage.2019.01.026

[3] Li, X., Rymer, W. Z., Li, G., & Zhou, P. (2011). The effects of notch filtering on electrically evoked myoelectric signals and associated motor unit index estimates. *Journal of NeuroEngineering and Rehabilitation*, 8, 64. https://doi.org/10.1186/1743-0003-8-64

[4] Ládrová, M., Martínek, R., Nedoma, J., & Fajkus, M. (2019). Methods of Power Line Interference Elimination in EMG Signal. *Journal of Biomimetics, Biomaterials and Biomedical Engineering*, 40, 64-70. https://doi.org/10.4028/www.scientific.net/JBBBE.40.64

[5] Tyrpa, M., & Piskorowski, J. (2025). Rejection of Power-Line Interference in EMG Signals Using a Notch Filter Initialized with Non-Zero States. *Pomiary Automatyka Robotyka*, 3/2025. https://doi.org/10.14313/PAR_257/13
