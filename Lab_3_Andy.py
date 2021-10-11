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
        self.X = self.find_X(self.a, self.b)
        self.Y = self.find_Y(self.a, self.b)

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
        elif (self.var == 1):
            return math.sin(t+2)

    def find_X(self, a, b):
        x = np.arange(a, b, (self.b - self.a) / self.N)
        return x

    def find_Y(self, a, b):
        y = np.array([], float)
        for i in range(len(self.find_X(a, b))):
            y = np.append(y, self.solve(self.find_X(a, b)[i]))
        return y

    def fit_NC(self):
        self.w = np.zeros(self.p + 1)
        self.errors = []

        for _ in range(self.M):  # по эпохам
            err = 0

            for i, target in enumerate(self.Y[self.p:]):
                delta = target - self.net_input(self.Y[i:self.p+i])
                update = self.n * delta
                self.w[1:] += update * self.Y[i:self.p+i]
                self.w[0] += update
                err += delta ** 2
            self.errors.append(err)
        return self

    def work(self):
        for i in range(self.N):
            self.Y = np.append(self.Y, self.net_input(self.Y[len(self.Y) - self.p:]))
            self.X = np.append(self.X, self.X[-1] + self.X[-1] - self.X[-2])
        plt.plot(self.X, self.Y, '--o', c='r', label='Slide')
        return self


    def net_input(self, Y):
        return np.dot(Y, self.w[1:]) + self.w[0]


    def paint(self):
        x = self.find_X(self.a, 2 * self.b - self.a)
        y = self.find_Y(self.a, 2 * self.b - self.a)
        self.fit_NC()
        self.work()


        plt.title("График функции")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid()
        plt.plot(x, y, '-o', c='deepskyblue', label='x(t)')
        plt.legend()
        plt.show()

        plt.plot(range(len(self.errors)), self.errors, '--og', label='Ошибка')  # МНК
        plt.grid()
        plt.show()


# ----------------------------------------
# Запуск программы
# ----------------------------------------
# Work = Lab(1, -1, 3, 0.01, 20, 6, 1000)
Work = Lab(2, -0.5, 0.5, 0.01, 20, 6, 1000)
Work.paint()

# ----------------------------------------
