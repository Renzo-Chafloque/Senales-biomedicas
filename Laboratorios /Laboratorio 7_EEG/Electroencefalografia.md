# Laboratorio de Electroencefalograma (EEG)

## Introducción
La electroencefalografía es el método o proceso científico mediante el cual se lleva a cabo el electroencefalograma. Este es una prueba que mide la actividad eléctrica en el cerebro [1]. Esta prueba está fundamentada por principios biológicos y físicos puesto que las neuronas se comunican mediante impulsos eléctricos en el orden de los microvoltios, los cuales son medidos por electrodos colocados en el cuero cabelludo de la persona evaluada. La señal detectada por los mismos será vista en forma de ondas en un registro.

Dependiendo de su frecuencia, estas señales pueden catalogarse en distintas ondas cerebrales, como ondas delta, theta, alfa, beta y gamma, las cuales se asocian con diferentes estados fisiológicos y cognitivos. Es pertinente agregar que, además de brindar información para comprender la actividad cerebral saludable, el EEG también sirve para diagnosticar o monitorear condiciones como problemas de sueño, convulsiones, epilepsia, encefaltitis, traumatismos y tumores [2].

<img width="643" height="217" alt="image" src="https://github.com/user-attachments/assets/98566a48-bc5d-4975-a26e-dded57590975" />

Características de las cinco ondas cerebrales básicas [3].

En el presente laboratorio se analizarán señales EEG mediante técnicas de procesamiento digital, con el fin de identificar características relevantes de la actividad cerebral y comprender el comportamiento de este tipo de señales biomédicas.

## Métodos
### BITalino y OpenSignals
Para la adquisición de señales se utilizó el kit de hardware BITalino, este ha sido diseñado especialmente para captar bioseñales. Este dispositivo cuenta con sensores de ECG, EMG, EDA y EEG, los cuales pueden emplearse en entornos de aprendizaje como aulas y laboratorios [a].
Para la visualización de la señal adquirida, se utilizó el software OpenSignals que permite conectar el BITalino a un computador mediante Bluetooth. Durante la configuración, se estableció una frecuencia de muestreo de 100 Hz, ya que las ondas cerebrales estudiadas presentan frecuencias menores a 50 Hz. Finalmente, los datos almacenados en archivos con formato .h5 y .txt para su posterior procesamiento.

### Colocación de electrodos
Los electrodos empleados para esta experiencia fueron el sistema integrado de tres derivaciones incluido en el kit BITalino y un sensor SnapBIT-DUO. El sistema de tres derivaciones se colocó en la frente del participante, ubicando un electrodo en la frente sobre cada ojo y el tercero sobre el hueso mastoideo que fue usado como referencia.

<img width="617" height="307" alt="image" src="https://github.com/user-attachments/assets/8df3f70d-d461-4682-8a7f-968f764bd243" />

Posicionamiento de electrodos para medir EEG en la posicion FP1 [4].


Por otro lado, el sensor SnapBIT-DUO se posicionó en la frente, sobre el ojo izquierdo del participante. En esta ocasión, no se usó un cable de referencia debido a que no se disponía del case necesario para integrar ambos sistemas.

<img width="463" height="347" alt="ELECTRODE" src="https://github.com/user-attachments/assets/c5da12d6-97fe-4fa4-bd0d-b96999100920" />

Posicionamiento del SnapBIT-DUO

## Resultados

• Evaluar incremento de β durante la tarea cognitiva (t‑test pareado).

• Detectar artefactos de parpadeo (> 80 μV) y contabilizar su número.
## Discusión

• ¿Qué banda de frecuencia predomina al cerrar los ojos?

• ¿Qué filtro es imprescindible para EEG y por qué?

• ¿Puedes modular conscientemente tu señal EEG? Da un ejemplo.

• ¿Se observan diferencias entre Fp1 y Fp2? ¿Por qué podrían ocurrir?

## Referencias

[1]	“Electroencefalografía (EEG)”, Mayoclinic.org, 2024. [En línea]. Disponible en: https://www.mayoclinic.org/es/tests-procedures/eeg/about/pac-20393875. [Consultado: 17-may-2026].

[2]	“Electroencefalograma”, Medlineplus.gov, 13-ene-2025. [En línea]. Disponible en: https://medlineplus.gov/spanish/ency/article/003931.htm. [Consultado: 17-may-2026].

[3]	Priyanka A. Abhang, Bharti W. Gawali, Suresh C. Mehrotra, “Technological Basics of EEG Recording and Operation of Apparatus”, ScienceDirect, 2016. [En línea]. Disponible en: https://www.sciencedirect.com/science/chapter/monograph/abs/pii/B9780128044902000026. [Consultado: 17-may-2026].

[a] “BITalino”, PLUX Biosignals. [En línea]. Disponible en: https://www.pluxbiosignals.com/collections/bitalino?srsltid=AfmBOoqSQHArGd9wQ5qW7GMdWWOrt3JAuqIjVuxrgDUkuIQw2IilsLKP. [Consultado: 17-may-2026].

