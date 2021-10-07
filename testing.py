import numpy as np
import matplotlib.pyplot as plt
import math

class Lab:
    var = None  # Вариант
    a = None  # граница a
    b = None  # граница b
    n = None  # коэфф. обучения
    N = None  # кол-во point'ов
    p = None  # кол-во окон
    M = None  # кол-во эпох обучения

    def __init__(self, var, a, b, n, N, p, M):
        self.var = var
        self.a = a
        self.b = b
        self.n = n
        self.N = N
        self.p = p
        self.M = M

    def get_data(self):
        print("var = ", self.var, sep="")
        print("a = ", self.a, sep="")
        print("b = ", self.b, sep="")
        print("n = ", self.n, sep="")
        print("N = ", self.N, sep="")
        print("p = ", self.p, sep="")
        print("M = ", self.M, sep="")


    def solve(self, t):
        if (self.var == 9):
            return math.exp(t - 2) - math.sin(t)
        elif (self.var == 2):
            return t**4 - 2*t**3 + t

    def find_X(self):
        x_N = np.arange(self.a, self.b, (self.b - self.a) / self.N)
        x_2N = np.arange(self.a, 2 * self.b - self.a, (self.b - self.a) / self.N)
        return x_N, x_2N

    def find_Yist(self):
        yN = np.array([], float)
        y2N = np.array([], float)
        tempN = self.find_X()[0]
        temp2N = self.find_X()[1]
        for i in range(len(tempN)):
            yN = np.append(yN, self.solve(tempN[i]))
        for i in range(len(temp2N)):
            y2N = np.append(y2N, self.solve(temp2N[i]))
        return yN, y2N


    def find_Yslide(self, arr_x, arr_y):
        n = self.n
        w = np.zeros(self.p + 1)

        errors = []
        for _ in range(self.M):  # каждая эпоха
            err = 0
            for xi, yi in zip(arr_x, arr_y):
                for k in range(1, self.p + 1):  # формирую 'y' (3.1)
                    temp = 0
                    temp += w[k] * arr_y[self.N - self.p + k - 1]
                arr_y = np.append(arr_y, temp)
                delta = yi - temp
                update = self.n * delta
                for k in range(1, self.p + 1):
                    w[k] += update * arr_y[self.N - self.p + k - 1]
                    w[0] += update
                err += delta ** 2
            errors.append(err)
        return w, errors, k

    def paint(self):
        x = self.find_X()[1]
        y = self.find_Yist()[1]
        y_slide = self.find_Yslide(self.find_X()[1], self.find_Yist()[1])
        plt.title("График функции")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid()
        plt.plot(x, y, '-o', c='deepskyblue', label='x(t)')
        plt.plot(x, y_slide, '-o', c='r', label='Slide')
        plt.legend()
        plt.show()



# ----------------------------------------
# Запуск программы
# ----------------------------------------
Work = Lab(9, -1, 4, 0.01, 20, 4, 2)
# Work = Lab(2, -0.5, 0.5, 0.1, 20, 4, 100)
Work.paint()
# print(Work.find_Yslide(-1, 2, 20))

# ----------------------------------------