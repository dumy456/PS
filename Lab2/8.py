import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi/2, np.pi/2, 10000)

sin = np.sin(t)
pade = (t - (7 * t**3) /60)/(1 + (t**2)/20)

eroare = np.abs(sin - pade)
eroare_pade = np.abs(t - pade)

fig, axs = plt.subplots(3)
fig1, axs1 = plt.subplots(4)

for ax in axs.flat:
    ax.set_xlim([-np.pi/2, np.pi/2])

for ax in axs1.flat:
    ax.set_xlim([-np.pi/2, np.pi/2])

axs[0].plot(t, pade)
axs[0].plot(t, sin)
axs[0].set_title('Pade vs Sin')
axs[0].legend(['Pade', 'Sin'])

axs[1].plot(t, sin)
axs[1].plot(t, pade)
axs[1].set_title('Pade vs t')
axs[1].legend(['Pade', 't'])

axs[2].plot(t, t)
axs[2].plot(t, sin)
axs[2].set_title('t vs Sin')
axs[2].legend(['t', 'Sin'])

axs1[0].plot(t, eroare)
axs1[0].set_title('Eroare Pade vs Sin')

axs1[1].plot(t, eroare_pade)
axs1[1].set_title('Eroare Pade vs t') 

axs1[2].plot(t, eroare)
axs1[2].set_yscale('log')
axs1[2].set_title('Eroare Pade vs Sin (log)')

axs1[3].plot(t, eroare_pade)
axs1[3].set_yscale('log')
axs1[3].set_title('Eroare Pade vs t (log)')

fig.tight_layout()
fig1.tight_layout()


plt.show()