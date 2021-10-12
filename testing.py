import numpy as np

N = 20
p = 4

a = np.arange(0, N)
mass = np.array([[]], float)

for i in range(0, p):
    mass[i] = np.append(mass[i], 5)