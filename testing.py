import numpy as np

N = 20
p = 4
w = np.ones(5)
a = np.arange(1, N+1)
print("a = ",a)
print("w = ",w)

temp = np.array([], float)
delta = np.array([], float)
for i in range(p, len(a)):  # строю матрицу двумерную
    temp = np.append(temp, np.dot(w[1:], a[(i - p):i]) + w[0])
    delta =
print(temp)
print("len = ", len(temp))