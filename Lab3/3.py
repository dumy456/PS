import matplotlib.pyplot as plt
import numpy as np

n = 1000
t = np.linspace(0, 1, n, endpoint=False)
x = (
    1.2 * np.cos(2 * np.pi * 4 * t)
    + 0.8 * np.sin(2 * np.pi * 12 * t)
    + 0.4 * np.cos(2 * np.pi * 28 * t)
)

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(14, 4))

ax[0].plot(t, x, color="navy")
ax[0].set_title("Semnal compus x(t)")
ax[0].set_xlabel("Timp (s)")
ax[0].set_ylabel("Amplitudine")
ax[0].grid(True, linestyle="--", alpha=0.5)

f_max = 60
frecvente = np.arange(f_max)
transformata = np.zeros(f_max, dtype=complex)

for m in frecvente:
    for k in range(n):
        transformata[m] += x[k] * np.exp(-2j * np.pi * m * k / n)

ax[1].stem(frecvente, np.abs(transformata), linefmt="b-", markerfmt="bo", basefmt="k-")
ax[1].set_title("Spectrul Fourier complet")
ax[1].set_xlabel("Frecvență (Hz)")
ax[1].set_ylabel("| X(ω) |")
ax[1].set_xlim(0, f_max)
ax[1].grid(True, linestyle="--", alpha=0.5)

omega_peaks = [4, 12, 28]
valori_omega = []

for w in omega_peaks:
    termeni_infasurare = [x[k] * np.exp(-2j * np.pi * w * k / n) for k in range(n)]
    valori_omega.append(np.sum(termeni_infasurare))

magnitudini_omega = np.abs(valori_omega)

ax[2].stem(omega_peaks, magnitudini_omega, linefmt="r-", markerfmt="ro", basefmt="k-")
ax[2].set_title("Componentele la frecvențele ω selectate")
ax[2].set_xlabel("Frecvență (Hz)")
ax[2].set_ylabel("| X(ω) |")
ax[2].set_xlim(0, f_max)
ax[2].grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
fig.savefig(fname="ex3.pdf", format="pdf")
plt.show()