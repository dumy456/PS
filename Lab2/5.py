import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf

fs=44100
t=np.linspace(0,1,fs)
signal1=np.sin(2*np.pi*400*t)
signal2=np.sin(2*np.pi*800*t)
concat=np.concatenate((signal1,signal2))

sd.play(concat,fs)
sd.wait()
# Programul reda sunetele in secventa
