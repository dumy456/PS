import numpy as np
import matplotlib.pyplot as plt


fig1,axs1=plt.subplots(2)
t=np.linspace(0,1,50)
signalsin=np.sin(2*np.pi*240*t)
axs1[0].plot(t,signalsin)
signalcos=np.cos(2*np.pi*240*t-np.pi/2)
axs1[1].plot(t,signalcos)
fig1.savefig(fname='./plots/1.pdf',format='pdf')

plt.show()