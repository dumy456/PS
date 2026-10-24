import numpy as np
import matplotlib.pyplot as plt

fig,axs=plt.subplots(4)
n=100
t=np.linspace(0,1,n)
signal=np.sin(2*np.pi*440*t)
signal1=np.sin(2*np.pi*440*t+1)
signal2=np.sin(2*np.pi*440*t+2)
signal3=np.sin(2*np.pi*440*t+3)
axs[0].plot(t,signal)
axs[1].plot(t,signal1)
axs[2].plot(t,signal2)
axs[3].plot(t,signal3)



fig1,axs1=plt.subplots(4)
SNR=[0.1,1,10,100]
x=signal
z=np.random.normal(size=n)
for i in range(4):
    y=np.sqrt(np.linalg.norm(x)**2/(SNR[i]*np.linalg.norm(z)**2))
    signalnew=x+y*z
    axs1[i].plot(signalnew)

plt.show()