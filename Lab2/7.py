import numpy as np
import matplotlib.pyplot as plt

fs = 1000

t = np.linspace(0, 1, fs)

signal = np.sin(2*np.pi*200*t)
signal2 = signal[::4]
signal3 = signal[1::4]

fig, axs1 = plt.subplots(3)

for ax in axs1.flat:
    ax.set_xlim([0, 0.1])

axs1[0].plot(t, signal)
axs1[1].plot(t[::4], signal2) 
axs1[2].plot(t[1::4], signal3)

fig.savefig(fname='./plots/7.pdf', format = 'pdf')
plt.show()