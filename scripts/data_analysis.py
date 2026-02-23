import os
import numpy as np

N = 5 # Number of measurements

for i in range(N):
    data = np.loadtxt(r'../resources/data/measurement_{N}.csv', delimiter=',')


