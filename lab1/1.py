import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return np.cos(520*np.pi*t+(np.pi/3))
def y(t):
    return np.cos(280*np.pi*t-(np.pi/3))
def z(t):
    return np.cos(120*np.pi*t+(np.pi/3))
t=np.linspace(0,0.03,60)
fig,axs=plt.subplots(3)
axs[0].plot(t,x(t))
axs[1].plot(t,y(t))
axs[2].plot(t,z(t))
fig.savefig(fname='./plots/1b.pdf',format='pdf')
t=np.linspace(0,0.03,200)
fig1,axs1=plt.subplots(3)
axs1[0].stem(t,x(t))
axs1[1].stem(t,y(t))
axs1[2].stem(t,z(t))
fig1.savefig(fname='./plots/1c.pdf',format='pdf')
plt.show()