import numpy as np
import matplotlib.pyplot as plt

f0 = 3.0
fs = 1000.0          
T = 1.0              
t = np.arange(0, T, 1.0 / fs)
N_samples = len(t)
x = np.cos(2 * np.pi * f0 * t)

y = x * np.exp(-2j * np.pi * t)
sample_idx = int(0.62 * N_samples)

fig2_1, (ax_sig, ax_polar) = plt.subplots(1, 2)

ax_sig.plot(t, x)
ax_sig.plot(t[sample_idx], x[sample_idx],"ro")
ax_sig.vlines(t[sample_idx], 0, x[sample_idx], color="r")
ax_sig.axhline(0, color="black", linewidth=0.8)
ax_sig.set_title("Semnalul x(t) = cos(2π · 3 · t)")
ax_sig.set_xlabel("Timp (s)")
ax_sig.set_ylabel("Amplitudine")
ax_sig.grid(True)

dist_y = np.abs(y)
scatter = ax_polar.scatter(y.real, y.imag, c=dist_y, cmap="viridis", s=6)
fig2_1.colorbar(scatter, ax=ax_polar, label="Distanta de la origine |y|")
ax_polar.plot(y[sample_idx].real, y[sample_idx].imag, "ro", markersize=8)
ax_polar.plot([0, y[sample_idx].real], [0, y[sample_idx].imag], "r--")
ax_polar.axhline(0, color="black", linewidth=0.8)
ax_polar.axvline(0, color="black", linewidth=0.8)
ax_polar.set_xlim(-1.2, 1.2)
ax_polar.set_ylim(-1.2, 1.2)
ax_polar.set_title("Infasurarea pe cercul unitate (ω = 1 Hz)")
ax_polar.set_xlabel("Real")
ax_polar.set_ylabel("Imaginar")
ax_polar.set_aspect("equal")
ax_polar.grid(True)

fig2_1.tight_layout()
fig2_1.savefig("ex2_fig1.pdf")
plt.close(fig2_1)

omegas = [1.0, 2.0, 3.0, 5.0]
fig2_2, axes_om = plt.subplots(2, 2, figsize=(10, 10))

for idx, omega in enumerate(omegas):
    ax = axes_om[idx // 2, idx % 2]
    z_om = x * np.exp(-2j * np.pi * omega * t)
    dists = np.abs(z_om)
    
    sc = ax.scatter(z_om.real, z_om.imag, c=dists, cmap="plasma", s=5)
    mean_val = np.mean(z_om)
    ax.plot(mean_val.real, mean_val.imag, "ko", markersize=7, label="Centru de masă")
    
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_title(f"ω = {omega} Hz" + (" (frecvența semnalului)" if omega == f0 else ""))
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginar")
    ax.set_aspect("equal")
    ax.grid(True)
    ax.legend(loc="upper right")

fig2_2.tight_layout()
fig2_2.savefig("ex2_fig2.pdf")
plt.close(fig2_2)