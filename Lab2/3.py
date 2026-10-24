import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf

fs=44100
t=np.linspace(0,1,fs)
signal1=np.sin(2*np.pi*400*t)
fig1,axs1=plt.subplots()
axs1.stem(t,signal1)

fig2,axs2=plt.subplots()
t2=np.linspace(0,3,fs)
signal2=np.sin(2*np.pi*800*t2)
axs2.stem(t2,signal2)

fig3,axs3=plt.subplots()
t3=np.linspace(0,0.02,fs)
signal3=2*(240*t3- np.floor(240*t3))-1
axs3.plot(t3,signal3)

fig4,axs4=plt.subplots()
t4=np.linspace(0,0.1,fs)
signal4=np.sign(np.sin(300*t4))
axs4.plot(t4,signal4)

sd.play(signal1,fs)
sf.write('output.wav',signal1,fs)
sd.wait()