#Ex 2
import matplotlib.pyplot as plt
import numpy as np

t_cont = np.linspace(0, 0.03, 1000)

f1 = 220
fs = 200 
f2 = 20  
f3 = 420  

t_samp = np.arange(0, 0.03 + 1 / fs, 1 / fs)

s1_cont = np.cos(2 * np.pi * f1 * t_cont)
s2_cont = np.cos(2 * np.pi * f2 * t_cont)
s3_cont = np.cos(2 * np.pi * f3 * t_cont)

s1_samp = np.cos(2 * np.pi * f1 * t_samp)
s2_samp = np.cos(2 * np.pi * f2 * t_samp)
s3_samp = np.cos(2 * np.pi * f3 * t_samp)

fig, axs = plt.subplots(4, 1, figsize=(10, 8), sharex=True)

axs[0].plot(t_cont, s1_cont, color='blue')
axs[0].set_title(f'Semnal original continuu ($f_1 = {f1}$ Hz)')

axs[1].plot(t_cont, s1_cont, color='blue')
axs[1].plot(t_samp, s1_samp, 'yo', markersize=8, markeredgecolor='black')
axs[1].set_title(f'Semnalul $f_1 = {f1}$ Hz esantionat la $f_s = {fs}$ Hz')

axs[2].plot(t_cont, s2_cont, color='red')
axs[2].plot(t_samp, s2_samp, 'yo', markersize=8, markeredgecolor='black')
axs[2].set_title(f'Alias 1 ($f_2 = {f2}$ Hz) cu aceleasi esantioane')

axs[3].plot(t_cont, s3_cont, color='green')
axs[3].plot(t_samp, s3_samp, 'yo', markersize=8, markeredgecolor='black')
axs[3].set_title(f'Alias 2 ($f_3 = {f3}$ Hz) cu aceleasi esantioane')
axs[3].set_xlabel('Timp (s)')

for ax in axs:
    ax.grid(True)
    ax.set_ylabel('Amplitudine')

plt.tight_layout()
plt.savefig('ex2.pdf')
plt.show()


# Ex 3

fs_nyquist = 1000
t_samp_nyq = np.arange(0, 0.03 + 1 / fs_nyquist, 1 / fs_nyquist)

s1_samp_nyq = np.cos(2 * np.pi * f1 * t_samp_nyq)
s2_samp_nyq = np.cos(2 * np.pi * f2 * t_samp_nyq)
s3_samp_nyq = np.cos(2 * np.pi * f3 * t_samp_nyq)

fig, axs = plt.subplots(3, 1, figsize=(10, 7), sharex=True)

axs[0].plot(t_cont, s1_cont, color='blue')
axs[0].plot(t_samp_nyq, s1_samp_nyq, 'yo', markersize=6, markeredgecolor='black')
axs[0].set_title(f'Semnal $f_1 = {f1}$ Hz esantionat la $f_s = {fs_nyquist}$ Hz')

axs[1].plot(t_cont, s2_cont, color='red')
axs[1].plot(t_samp_nyq, s2_samp_nyq, 'yo', markersize=6, markeredgecolor='black')
axs[1].set_title(f'Semnal $f_2 = {f2}$ Hz esantionat la $f_s = {fs_nyquist}$ Hz')

axs[2].plot(t_cont, s3_cont, color='green')
axs[2].plot(t_samp_nyq, s3_samp_nyq, 'yo', markersize=6, markeredgecolor='black')
axs[2].set_title(f'Semnal $f_3 = {f3}$ Hz esantionat la $f_s = {fs_nyquist}$ Hz')
axs[2].set_xlabel('Timp (s)')

for ax in axs:
    ax.grid(True)
    ax.set_ylabel('Amplitudine')

plt.tight_layout()
plt.savefig('ex3.pdf')
plt.show()