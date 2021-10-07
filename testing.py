import numpy as np
import matplotlib.pyplot as plt
import math

a_ref = 0
b_ref = 5
n_ref = 0.01
N_ref = 5
p_ref = 3
M_ref = 100

def solve(t):
        # return math.exp(t - 2) - math.sin(t)
        return t

def find_X(a, b, N):
    x_N = np.arange(a, b, (b - a) / N)
    x_2N = np.arange(a, 2 * b - a, (b - a) / N)
    return x_N, x_2N


def find_Yist(a, b, N):
    yN = np.array([], float)
    y2N = np.array([], float)
    tempN = find_X(a, b, N)[0]
    temp2N = find_X(a, b, N)[1]
    for i in range(len(tempN)):
        yN = np.append(yN, solve(tempN[i]))
    for i in range(len(temp2N)):
        y2N = np.append(y2N, solve(temp2N[i]))
    return yN, y2N

def find_Yslide(a, b, n, N, p, M):
    w = np.array([], float)
    for i in range(p + 1):
        w = np.append(w, 0)
    print("Массив X[0-4]", find_X(a, b, N)[0])
    print("Массив Y[0-4]", find_Yist(a, b, N)[0])
    print("Массив X[0-9]", find_X(a, b, N)[1])
    print("Массив Y[0-9]", find_Yist(a, b, N)[1])
    y_ist2N = find_Yist(a, b, N)[1]
    print(y_ist2N)
    for g in range(M):  # проход по эпохам обучения
        y = find_Yist(a, b, N)[0]
        print(y)
        for i in range(N):  # проход по каждому шагу функции
            y = np.append(y, 0)
            print(y, "and len = ", len(y))
            # print("y", i, " = ", y, sep="")
            # print("Обновляю y", self.N + 1 + i - 1)
            for j in range(1, p + 1):  # формирую 'y' (3.1)
                y[N + 1 + i - 1] += w[j] * y[(N + 1 + i - 1) - p + j - 1]
            print("y", N + 1 + i - 1, " = ", y[N + 1 + i - 1], sep="")
            delta = y_ist2N[N + 1 + i - 1] - y[N + 1 + i - 1]
            print("Delta:   y_ist2N", N + 1 + i - 1, " = ", y_ist2N[N + 1 + i - 1], sep="")
            print("Delta:   y", N + 1 + i - 1, " = ", y[N + 1 + i - 1], sep="")
            for j in range(1, p + 1):  # обновляю веса
                w[j] += n * delta * y[(N + 1 + i - 1) - p + j - 1]
                print("Внутри W:   y", (N + 1 + i - 1) - p + j - 1, " = ", y[(N + 1 + i - 1) - p + j - 1], sep="")
            print("Новые веса: ", w)
    plt.plot(find_X(a, b, N)[1], find_Yist(a, b, N)[1], '-o', c='deepskyblue', label='x(t)')
    plt.plot(find_X(a, b, N)[1], y, '-o', c='r', label='Slide')
    plt.legend()
    plt.show()
    return y


find_Yslide(a_ref, b_ref, n_ref, N_ref, p_ref, M_ref)