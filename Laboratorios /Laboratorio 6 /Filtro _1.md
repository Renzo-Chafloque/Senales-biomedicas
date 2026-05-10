# Filtro Butterworth aplicado a señales biomédicas EMG, EKG y EEG

El filtro Butterworth es de respuesta infinita al impulso (IIR) 
caracterizado por no presentar rizado ni en la banda de paso ni en la banda de rechazo.
Su función de transferencia de magnitud al cuadrado es:
|H(jω)|² = 1 / (1 + (ω/ωc)^(2n))
ω = frecuencia angular de la señal
ωc = frecuencia de corte (-3 dB)
n = orden del filtro
Mayor orden n, más abrupta es la caída en la banda de transición. 
Puede ser pasa-bajas, pasa-altas, pasa-banda o rechaza-banda[1].
Ruido que elimina en cada señal:

EKG, electrocardiograma:
Rango fisiológico útil: 0.05 – 100 Hz
*Ruido de línea base, causado por respiración y movimiento
de los electrodos. Suele estar en frecuencias de menos de 0.5Hz.
*Ruido por artefactos musculares, actividad EMG no deseada durante el registro.
Usualmente menores a 100 Hz.[2]

EMG, electromiograma:
Rango fisiológico útil: 20 – 500 Hz
*Ruido por artefactos, desplazamiento de electrodos por la piel. Usualmente 
menores a 20Hz.
*Ruido de alta frecuencia, interferencia electromagnética y ruido térmico del 
amplificador, estas se presentan en frecuencias mayores a 500Hz.[3]

EEG, electroencefalograma:
Rango fisiológico útil: 0.5 – 70 Hz
*Ruido por artefactos oculares, parapadeos y movimiento ocular.
Usualmente menores a 1Hz.
*Ruido muscular, contraccion de músculos fasciales y del cuero cabelludo.
Estos son de frecuencias mayores a 50Hz.[4]

[1] L. Sörnmo and P. Laguna, Bioelectrical Signal Processing in Cardiac and Neurological Applications. Burlington, MA, USA: Elsevier Academic Press, 2005.
[2] J. Pan and W. J. Tompkins, "A real-time QRS detection algorithm," IEEE Trans. Biomed. Eng., vol. 32, no. 3, pp. 230–236, Mar. 1985, doi: 10.1109/TBME.1985.325532.
[3] C. J. De Luca, L. D. Gilmore, M. Kuznetsov, and S. H. Roy, "Filtering the surface EMG signal: Movement artifact and baseline noise contamination," J. Biomech., vol. 43, no. 8, pp. 1573–1579, May 2010, doi: 10.1016/j.jbiomech.2010.01.027.
[4] E. Niedermeyer and F. L. da Silva, Eds., Electroencephalography: Basic Principles, Clinical Applications, and Related Fields, 5th ed. Philadelphia, PA, USA: Lippincott Williams & Wilkins, 2005.
