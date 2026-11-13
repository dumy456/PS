import time
import matplotlib.pyplot as plt
import numpy as np


def my_dft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


def my_fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = my_fft(x[0::2])
    odd = my_fft(x[1::2])

    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return np.concatenate([even + T, even - T])


N_values = [128, 256, 512, 1024, 2048, 4096, 8192]
times_dft = []
times_fft = []
times_np = []

for N in N_values:
    x = np.random.random(N)

    t0 = time.perf_counter()
    my_dft(x)
    times_dft.append(time.perf_counter() - t0)

    t0 = time.perf_counter()
    my_fft(x)
    times_fft.append(time.perf_counter() - t0)

    t0 = time.perf_counter()
    np.fft.fft(x)
    times_np.append(time.perf_counter() - t0)

plt.figure(figsize=(10, 6))
plt.plot(N_values, times_dft, 'o-', label='DFT propriu $O(N^2)$')
plt.plot(N_values, times_fft, 's-', label='FFT propriu $O(N \log N)$')
plt.plot(N_values, times_np, '^-', label='numpy.fft')

plt.yscale('log')
plt.xscale('log', base=2)
plt.xlabel('Dimensiunea vectorului (N)')
plt.ylabel('Timp de executie (secunde) - scara log')
plt.title('Comparatie timp de executie: DFT vs. FFT vs. numpy.fft')
plt.grid(True, which='both', ls='--')
plt.legend()
plt.savefig('ex1.pdf')
plt.show()