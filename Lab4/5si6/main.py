import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

fs, signal = wavfile.read('vocale.wav')

if signal.ndim > 1:
    signal = signal[:, 0]

N = len(signal)

win_size = int(0.01 * N)
step_size = win_size // 2

spectrogram_cols = []

for start in range(0, N - win_size + 1, step_size):
    window = signal[start : start + win_size]


    fft_vals = np.fft.fft(window)

    fft_mag = np.abs(fft_vals[: win_size // 2])
    spectrogram_cols.append(fft_mag)

spec_matrix = np.array(spectrogram_cols).T

spec_matrix_db = 20 * np.log10(spec_matrix + 1e-10)

durata_secunde = N / fs
frecventa_maxima = fs / 2

plt.figure(figsize=(12, 6))
plt.imshow(
    spec_matrix_db,
    aspect='auto',
    origin='lower',
    extent=[0, durata_secunde, 0, frecventa_maxima],
    cmap='inferno',
)

plt.colorbar(label='Intensitate (dB)')
plt.xlabel('Timp (s)')
plt.ylabel('Frecventa (Hz)')
plt.title('Spectrograma vocalelor (a, e, i, o, u)')
plt.savefig('ex6.pdf')
plt.show()