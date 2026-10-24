import numpy as np
import matplotlib.pyplot as plt

fig,axs=plt.subplots(3)
f=400
t=np.linspace(0,1,100)
sins=np.sin(2*np.pi*f*t)
saws=2*(t*f-np.floor(0.5+t*f))
axs[0].plot(t,sins)
axs[1].plot(t,saws)
axs[2].plot(t,sins+saws)

plt.show()