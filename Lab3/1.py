
import numpy as np
from matplotlib import pyplot as plt

N = 8

k = np.arange(N).reshape(-1, 1)
n = np.arange(N).reshape(1, -1)
fm = np.exp(-2j * np.pi * k * n / N)

fhm = np.transpose(np.conjugate(fm))

fhfm = np.matmul(fhm, fm)
fhfm = np.subtract(fhfm, np.diag(np.full(N, fhfm[0, 0])))

eps = 1e-5
fro_norm = np.linalg.norm(fhfm, ord="fro")
print(f"Norm: {fro_norm}")
print(f"Is unitary: {0 - eps <= fro_norm <= 0 + eps}")
print(f"Is unitary (allclose): {np.allclose(np.matmul(fhm, fm), N * np.eye(N))}")

fig, axs = plt.subplots(N, 2, figsize=(10, 8), sharex=True)
fig.suptitle("Fourier Components (Real vs Imaginary)")

components_numbered = [i for i in range(N)]

for i in range(N):
    axs[i, 0].plot(components_numbered, fm[i].real, marker="o", color="tab:blue")
    axs[i, 0].set_ylabel(f"k = {i}")
    axs[i, 0].grid(True, linestyle="--", alpha=0.5)

    axs[i, 1].plot(components_numbered, fm[i].imag, marker="o", linestyle="dashed", color="tab:orange")
    axs[i, 1].grid(True, linestyle="--", alpha=0.5)

axs[0, 0].set_title("Real Part")
axs[0, 1].set_title("Imaginary Part")
axs[N - 1, 0].set_xlabel("n")
axs[N - 1, 1].set_xlabel("n")

plt.tight_layout()
plt.savefig("ex1.pdf", format="pdf")
plt.show()