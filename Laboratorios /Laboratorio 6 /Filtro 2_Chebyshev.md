# Chebyshev filter
## ¿Qué es?
Es un filtro IIR definido por una función de transferencia racional. La respuesta de los filtros Chebyshev representa una estrategia matemática para obtener una transición en la banda de paso y la de rechazo más rápida a expensas de permitir ondas en la repuesta en frecuencia. Se trata de un trade off entre roll-off y ripple puesto que a medida que la onda (ripple) crece en amplitud, el roll-off que es la rapidez con la que el filtro atenúa será mayor [1].
Este tipo de filtro es usado en el procesamiento de señales y telecomunicaciones en las que se requiere una separación rápida y precisa entre bandas
de frecuencia. Es más preciso que un Butterworth y menos complejo que un filtro Elíptico [2].

## Función en señales biomédicas
### ECG
Este tipo de filtro para ECG permite atenuar interferencia eléctrica de 50/60 Hz y artefactos de movimiento. Ello permite preservar las ondas P, QRS y T sin perder información diagnóstica relevante generalmente encontrada entre los 0.5 y 100 Hz por lo que suele emplearse como pasa-banda dejando pasar ese rango. Como ventajas de diseño se encuentran una atenuación rápida del ruido, menor carga computacional y un buen desempeño en tiempo real.

Respecto a las aplicaciones, en un estudio elaborado en Bulgaria en el año 2025 se propuso el diseño de filtros digitales inversos activos, tanto pasa-altas como pasa-bajas, capaces de compensar las distorsiones causadas por los filtros analógicos RC agresivos en la etapa de adquisición de los electrocardiógrafos. En este contexto, el filtro Chebyshev no se usó para limpiar el ruido, sino como un modelo para recuperar la fidelidad de la onda ECG restaurando el segmento ST y los picos R y S. Con esta investigación se demostró que es posible recuperar la calidad diagnóstica de forma digital lo cual facilita un análisis automático más preciso [3].

### EEG

Este tipo de filtro para EEG permite una separación drástica de bandas de frecuencia útil para ondas alba, beta, delta, theta y gamma con un menor costo computacional que los filtros FIR. Esto se debe a la característica de caída abrupta del filtro pues a diferencia del filtro Butterworth, que es "plano", pero tiene una transición lenta, el Chebyshev alcanza la banda de rechaz mucho más rápido. La limitante más expresada de este tipo de señal biomédica es la ondulación que puede alterar amplitudes pequeñas, por lo que en algunos análisis clínicos prefieren Butterworth o FIR lineales. Para controlar ello es prudente realizar una optimización de parámetros del filtro.

Respecto a las aplicaciones, en un estudio elaborado en Israel en el año 2025 se buscó encontrar el cálculo automatizado de la potencia promedio de señales EEG con particular atención en la banda de frecuencia beta (13-30 Hz) para la obtención de una señal clara e interpretable. Los resultados indicaron que el filtro digital Chebyshev tipo I de cuarto orden con ondulaciones de 0.5% superó a filtros FIR y Butterworth IIR. Entre las razones principales se encuentra que el valor de 0.5 permite mantener una señal fiel y conseguir una banda de transición más abrupta de mayor selectividad con distorsión mínima. Con ello, se mejora la precisión de la visualización de señales neuronales facilitando la creación de mapas de la actividad cerebral [4].


### EMG


## Referencias
[1] “Chebyshev Filter - an overview,” ScienceDirect Topics, Elsevier, 2026. Disponible en: https://www.sciencedirect.com/topics/engineering/chebyshev-filter [Accedido: 7-may-2026].

[2] “Chebyshev Filters,” Analog Devices, 1999. Disponible en: https://www.analog.com/media/en/technical-documentation/dsp-book/dsp_book_Ch20.pdf [Accedido: 7-may-2026].‌

[3] D. Dobrev, T. Neycheva, V. Krasteva e I. Jekova, "Diseño de filtros inversos activos pasa-altas y pasa-bajas para compensar distorsiones en electrocardiogramas filtrados por RC" Technologies, vol. 13, n.º 4, p. 159, abr. 2025, doi: 10.3390/technologies13040159.

[4] N. Avital, N. Shulkin y D. Malka, «Cálculo automático de la potencia media en señales de electroencefalografía para la detección mejorada de la actividad cerebral y patrones de comportamiento», Biosensors, vol. 15, n.º 5, p. 314, mayo 2025, doi: 10.3390/bios15050314.
