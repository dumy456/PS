import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,1,1600)
signal1=np.sin(2*np.pi*400*t)
fig1,axs1=plt.subplots()
axs1.stem(t,signal1)
fig1.savefig(fname='./plots/2a.pdf',format='pdf')

fig2,axs2=plt.subplots()
t2=np.linspace(0,3,800)
signal2=np.sin(2*np.pi*800*t2)
axs2.stem(t2,signal2)
fig2.savefig(fname='./plots/2b.pdf',format='pdf')

fig3,axs3=plt.subplots()
t3=np.linspace(0,0.02,2000)
signal3=2*(240*t3- np.floor(240*t3))-1
axs3.plot(t3,signal3)
fig3.savefig(fname='./plots/2c.pdf',format='pdf')

fig4,axs4=plt.subplots()
t4=np.linspace(0,0.1,10000)
signal4=np.sign(np.sin(300*t4))
axs4.plot(t4,signal4)
fig4.savefig(fname='./plots/2d.pdf',format='pdf')

fig5, axs5 = plt.subplots()
t5=np.random.rand(128,128)
mat=axs5.imshow(t5)
fig5.savefig(fname='./plots/2e.pdf',format='pdf')

fig6, axs6 = plt.subplots()
t6=np.ones((128,128))
for i in range(128):
    t6[64][i]=0;
    t6[i][64]=0;
mat2=axs6.imshow(t6)
fig6.savefig(fname='./plots/2f.pdf',format='pdf')
plt.show()