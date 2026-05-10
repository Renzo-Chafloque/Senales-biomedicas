# Chebyshev filter
## ¿Qué es?
Es un filtro IIR definido por una función de transferencia racional.
La respuesta de los filtros Chebyshev representa una estrategia matemática para obtener una transición en la banda de paso y la de rechazo más rápida
a expensas de permitir ondas en la repuesta en frecuencia. Se trata de un trade off entre roll-off y ripple puesto que a medida que la onda (ripple) crece en amplitud,
el roll-off que es la rapidez con la que el filtro atenúa será mayor [1].
Este tipo de filtro es usado en el procesamiento de señales y telecomunicaciones en las que se requiere una separación rápida y precisa entre bandas
de frecuencia. Es más preciso que un Butterworth y menos complejo que un filtro Elíptico [2].

## Función en señales biomédicas
### ECG
Este tipo de filtro para ECG permite atenuar interferencia eléctrica de 50/60 Hz y artefactos de movimiento. Ello permite preservar las ondas P, QRS y T sin perder información diagnóstica relevante generalmente encontrada entre los 0.5 y 100 Hz por lo que suele emplearse como pasa-banda dejando pasar ese rango. Como ventajas de diseño se encuentran una atenuación rápida del ruido, menor carga computacional y un buen desempeño en tiempo real.

Respecto a las aplicaciones, en un estudio elaborado en Bulgaria en el año 2025 se propuso el diseño de filtros digitales inversos activos, tanto pasa-altas como pasa-bajas, capaces de compensar las distorsiones causadas por los filtros analógicos RC agresivos en la etapa de adquisición de los electrocardiógrafos. En este contexto, el filtro Chebyshev no se usó para limpiar el ruido, sino como un modelo para recuperar la fidelidad de la onda ECG restaurando el segmento ST y los picos R y S. Con esta investigación se demostró que es posible recuperar la calidad diagnóstica de forma digital lo cual facilita un análisis automático más preciso [3].

### EEG

### EMG


## Referencias
[1] “Chebyshev Filter - an overview,” ScienceDirect Topics, Elsevier, 2026. Disponible en: https://www.sciencedirect.com/topics/engineering/chebyshev-filter [Accedido: 7-may-2026].

[2] “Chebyshev Filters,” Analog Devices, 1999. Disponible en: https://www.analog.com/media/en/technical-documentation/dsp-book/dsp_book_Ch20.pdf [Accedido: 7-may-2026].‌

[3] D. Dobrev, T. Neycheva, V. Krasteva e I. Jekova, "Diseño de filtros inversos activos pasa-altas y pasa-bajas para compensar distorsiones en electrocardiogramas filtrados por RC" Technologies, vol. 13, n.º 4, p. 159, abr. 2025, doi: 10.3390/technologies13040159.
