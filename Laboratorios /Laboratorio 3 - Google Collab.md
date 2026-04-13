## Interpretación de base de datos en Google Colab
Esta base de datos de registros de ECG de dos canales se ha creado para su uso en el concurso Computers in Cardiology Challenge 2004 , una competición abierta cuyo objetivo es desarrollar métodos automatizados para predecir la terminación espontánea de la fibrilación auricular (FA). Consulte el anuncio del concurso para obtener más información.

Se analizan 3 señales de un [dataset](https://physionet.org/content/aftdb/1.0.0/test-set-a/#files-panel) de Physionet en el siguiente enlace:
[Ejemplo con dataset](https://colab.research.google.com/drive/1-igcuozq0SuaBVytrwyafnOKihajNob0?usp=sharing) 

Cada registro corresponde a un segmento de un minuto de fibrilación auricular, que contiene dos señales de ECG, cada una muestreada a 128 muestras por segundo. Los segmentos se extrajeron de registros de ECG de larga duración (20-24 horas). Cada registro incluye un conjunto de anotaciones QRS generadas por un detector automatizado, en las que todos los latidos detectados, incluidos los latidos ectópicos, se etiquetan como normales. Estas anotaciones no han sido auditadas y pueden contener algunos errores.

