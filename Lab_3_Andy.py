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

    def find_X(self, a, b):
        x = np.arange(a, b, (self.b - self.a) / self.N)
        return x

    def find_Y(self, a, b):
        y = np.array([], float)
        for i in range(len(self.find_X(a, b))):
            y = np.append(y, self.solve(self.find_X(a, b)[i]))
        return y

    def fit_NC(self):
        w = np.zeros(self.p + 1)
        errors = []

        for _ in range(self.M):  # по эпохам
            err = 0
            for i, target in enumerate(self.find_Y(self.a, self.b)[self.p:]):
                print(len(target))
                print(len((np.dot(self.find_Y(self.a, self.b)[i:self.p+1], w[1:]) + w[0])))
                delta = target - (np.dot(self.find_Y(self.a, self.b)[i:self.p+1], w[1:]) + w[0])
                update = self.n * delta

                w[1:] += update * self.find_Y(self.a, self.b)[i:self.p+1]
                w[0] += update
                err += delta ** 2
            errors.append(err)
        return w, errors

    # def work(self, y, w):
    #             return y

    def paint(self):
        x = self.find_X(self.a, 2 * self.b - self.a)
        y = self.find_Y(self.a, 2 * self.b - self.a)
        w, err = self.fit_NC()
        # print(w)
        # y_nc = self.work(y_new, w)
        plt.title("График функции")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid()
        plt.plot(x, y, '-o', c='deepskyblue', label='x(t)')
        # plt.plot(self.find_X(self.a, 2 * self.b - self.a), y_nc, '-o', c='r', label='Slide')
        plt.legend()
        plt.show()



# ----------------------------------------
# Запуск программы
# ----------------------------------------
Work = Lab(9, -1, 2, 0.01, 20, 4, 1)
# Work = Lab(2, -0.5, 0.5, 0.1, 20, 4, 100)
Work.paint()
# print(Work.find_Yslide(-1, 2, 20))

# ----------------------------------------
