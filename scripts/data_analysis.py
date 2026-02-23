import os
from matplotlib.pylab import yscale
from matplotlib.pyplot import xscale
import numpy as np
import matplotlib.pyplot as plt

N = 5 # Number of measurements
air_list = []
vac_list = []

for i in range(N):
    data_air = np.loadtxt(f'../resources/data/{i+1}_air.csv', delimiter=',')
    data_vac = np.loadtxt(f'../resources/data/{i+1}_vac.csv', delimiter=',')

    air_list.append(data_air)
    vac_list.append(data_vac)

array_3d_air = np.array(air_list)
array_3d_vac = np.array(vac_list)

# Slice from index 359 (t=0) to the end of the arrays
array_3d_air_pos = array_3d_air[:, 359:, :]
array_3d_vac_pos = array_3d_vac[:, 359:, :]

fig, ax = plt.subplots(N, 2, figsize=(16, 32), dpi=300)

for j in range(N):
    ax[j, 0].plot(array_3d_air_pos[j,:,0], -array_3d_air_pos[j,:,1])
    ax[j, 1].plot(array_3d_vac_pos[j,:,0], -array_3d_vac_pos[j,:,1])
    ax[j,0].set(title=f'Measurement #{j+1} for Air', xlabel='Time [s]', ylabel='Intensity [A]')
    ax[j,1].set(title=f'Measurement #{j+1} for Vacuum', xlabel='Time [s]', ylabel='Intensity [A]')

fig.tight_layout()
fig.savefig('plot.png')
