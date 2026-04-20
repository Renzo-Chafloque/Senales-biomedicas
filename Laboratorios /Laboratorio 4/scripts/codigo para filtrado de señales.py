import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, iirnotch

# 1. Definición de la función de filtrado
def filtrar_emg(signal, fs=1000.0, lowcut=20.0, highcut=450.0, notch_freq=60.0):
    # Eliminación de la media (DC Offset)
    signal_centered = signal - np.mean(signal)
    
    # Filtro Notch (60 Hz) para ruido de red eléctrica
    Q = 30.0 
    b_notch, a_notch = iirnotch(notch_freq, Q, fs)
    signal_notch = filtfilt(b_notch, a_notch, signal_centered)
    
    # Filtro Pasa-banda (20-450 Hz) para frecuencias musculares
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b_band, a_band = butter(4, [low, high], btype='band')
    signal_filtered = filtfilt(b_band, a_band, signal_notch)
    
    return signal_filtered

# 2. Carga de datos
# CAMBIAR 'NOMBRE_ARCHIVO.txt' por el nombre del archivo en OpenSignals
nombre_archivo = 'BASAL2_EMG_17042026.txt' 

try:
    # Cargamos ignorando las líneas de encabezado de BITalino
    data = np.loadtxt(nombre_archivo, comments='#')
    raw_emg = data[:, -1]  # Usualmente la última columna es la EMG
    fs = 1000.0            # Frecuencia de muestreo
    t = np.arange(len(raw_emg)) / fs

    # 3. Procesamiento
    filtered_emg = filtrar_emg(raw_emg, fs=fs)
    rectified_emg = np.abs(filtered_emg)

    # --- GRÁFICA 1: VISTA GENERAL (Todo el registro) ---
    plt.figure(figsize=(12, 10))

    plt.subplot(3, 1, 1)
    plt.plot(t, raw_emg, color='red', alpha=0.7, linewidth=0.5)
    plt.title("Señal EMG Cruda (Vista Completa)")
    plt.ylabel("Valor Digital")
    plt.grid(True, alpha=0.3)

    plt.subplot(3, 1, 2)
    plt.plot(t, filtered_emg, color='blue', linewidth=0.5)
    plt.title("Señal EMG Filtrada (Pasa-banda 20-450Hz + Notch 60Hz)")
    plt.ylabel("Amplitud")
    plt.grid(True, alpha=0.3)

    plt.subplot(3, 1, 3)
    plt.plot(t, rectified_emg, color='green', linewidth=0.5)
    plt.title("Señal EMG Rectificada (Valor Absoluto)")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    # --- GRÁFICA 2: VISTA CON ZOOM (Ajuste para ver la señal clara) ---
    # Definimos qué segundos queremos ver para el zoom (ejemplo: del 10 al 12)
    segundo_inicio = 10 
    segundo_fin = 12

    # Convertir segundos a índices
    idx_inicio = int(segundo_inicio * fs)
    idx_fin = int(segundo_fin * fs)

    plt.figure(figsize=(15, 6))

    # Graficamos el fragmento filtrado
    t_zoom = t[idx_inicio:idx_fin]
    signal_zoom = filtered_emg[idx_inicio:idx_fin]

    plt.plot(t_zoom, signal_zoom, color='blue', linewidth=1)
    plt.title(f"Zoom de la Señal Filtrada (Segundos {segundo_inicio} al {segundo_fin})")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True, alpha=0.5)

    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Error: {e}")