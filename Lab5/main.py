import numpy as np
import matplotlib.pyplot as plt

try:
    data = np.genfromtxt('Train.csv', delimiter=',', skip_header=1)
    if data.ndim > 1:
        x = data[:, -1]
    else:
        x = data
except Exception:
    x = np.genfromtxt('Train.csv', delimiter=',')

x = x[~np.isnan(x)]
N = len(x)
Fs = 1 / 3600.0  
X_full = np.fft.fft(x)
X_mag = np.abs(X_full / N)
X_half = X_mag[:N // 2]
f = Fs * np.linspace(0, N // 2, N // 2) / N

plt.figure(figsize=(12, 4))
plt.plot(f, X_half)
plt.title('Modulul Transformatei Fourier (cu componenta continua)')
plt.xlabel('Frecventa (Hz)')
plt.ylabel('|X(f)|')
plt.grid(True)
plt.show()

dc_offset = np.mean(x)
print(f"Componenta continua (media semnalului): {dc_offset:.2f}")

x_zero_mean = x - dc_offset  

X_clean = np.fft.fft(x_zero_mean)
X_clean_half = np.abs(X_clean[:N // 2] / N)

plt.figure(figsize=(12, 4))
plt.plot(f, X_clean_half)
plt.title('Modulul Transformatei Fourier (fara componenta continua)')
plt.xlabel('Frecventa (Hz)')
plt.ylabel('|X(f)|')
plt.xlim([0, 0.3e-4])
plt.grid(True)
plt.show()

top_4_idx = np.argsort(X_clean_half)[::-1][:4]

print("\nTop 4 componente de frecventa (fără DC):")
for idx in top_4_idx:
    freq_hz = f[idx]
    period_hours = (1 / freq_hz) / 3600.0 if freq_hz > 0 else np.inf
    period_days = period_hours / 24.0
    print(f"Frecventa: {freq_hz:.8e} Hz | Amplitudine: {X_clean_half[idx]:.2f} | "
          f"Perioada: {period_hours:.1f} ore ({period_days:.2f} zile)")

plt.figure(figsize=(12, 4))
plt.plot(np.arange(1200, 1450), x[1200:1450])
plt.title('Identificarea zilei de luni (cautam minimul de weekend urmat de crestere)')
plt.xlabel('Index esantion')
plt.ylabel('Nr. masini')
plt.grid(True)
plt.show()

start_luni = 1224
o_luna = 30 * 24
plt.figure(figsize=(12, 4))
plt.plot(np.arange(start_luni, start_luni + o_luna), x[start_luni : start_luni + o_luna])
plt.title('Traficul pe parcursul unei luni (incepand de luni)')
plt.xlabel('Esantioane (ore)')
plt.ylabel('Nr. masini')
plt.grid(True)
plt.show()


f_cutoff = 1 / (12 * 3600.0)

X_filtered = X_full.copy()
freqs_full = np.fft.fftfreq(N, d=3600.0)
X_filtered[np.abs(freqs_full) > f_cutoff] = 0

x_filtered = np.real(np.fft.ifft(X_filtered))
plt.figure(figsize=(12, 4))
plt.plot(x[start_luni : start_luni + o_luna], label='Semnal original', alpha=0.6)
plt.plot(x_filtered[start_luni : start_luni + o_luna], label='Semnal filtrat (T >= 12h)', linewidth=2)
plt.title('Comparatie: Semnal original vs. Semnal filtrat trece-jos')
plt.xlabel('Esantioane (ore)')
plt.ylabel('Nr. masini')
plt.legend()
plt.grid(True)
plt.show()