import numpy as np
import matplotlib.pyplot as plt

fig,axs=plt.subplots(3)
f=1000
t=np.linspace(0,1,f)
signala=np.sin(2*np.pi*f/2*t)
signalb=np.sin(2*np.pi*f/4*t)
signalc=np.sin(2*np.pi*0*t)
axs[0].plot(t,signala)
axs[1].plot(t,signalb)
axs[2].plot(t,signalc)
plt.show()