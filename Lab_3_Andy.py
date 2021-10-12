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
        self.w = np.zeros(self.p + 1)

    def solve(self, t):
        return np.exp(t - 2) - np.sin(t)

    def find_X(self, a, b):
        x = np.arange(a, b, (self.b - self.a) / self.N)
        return x

    def find_Y(self, a, b):
        y = np.array([], float)
        for i in range(len(self.find_X(a, b))):
            y = np.append(y, self.solve(self.find_X(a, b)[i]))
        return y

    def fit_NC(self):
        self.errors = []
        y = self.find_Y(self.a, self.b)

        for _ in range(self.M):  # по эпохам
            err = 0

            temp = np.array([], float)
            update = np.array([], float)
            for i in range(self.p, len(y)):  # строю матрицу двумерную
                temp = np.append(temp, np.dot(self.w[1:], y[(i - self.p):i]) + self.w[0])
                delta = y[i] - temp[-1]
                update = self.n * delta
                self.w[1:] += update * y[(i - self.p):i]
                self.w[0] += update
                err += delta ** 2
            self.errors.append(err)
        return self

    def net_input(self, X):
        return np.dot(X, self.w[1:]) + self.w[0]

    def work(self):
        x = self.find_X(self.a, 2 * self.b - self.a)


    def paint(self):
        self.fit_NC()
        print(self.w)
        # self.work()
        for i in range(20):
            self.Y = np.append(self.Y, self.net_input(self.Y[len(self.Y) - self.p:]))
            self.X = np.append(self.X, self.X[-1] + self.X[-1] - self.X[-2])

        plt.title("График функции")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid()
        plt.plot(self.X, self.Y, '-o', c='deepskyblue', label='x(t)')
        plt.legend()
        plt.show()

        plt.plot(range(len(self.errors)), self.errors, '--og', label='Ошибка')  # МНК
        plt.grid()
        plt.show()


# ----------------------------------------
# Запуск программы
# ----------------------------------------
# Work = Lab(-1, 3, 0.01, 20, 6, 1000)  # Андрей
Work = Lab(-0.5, 0.5, 0.01, 20, 4, 1000)  # Аня
Work.paint()

# ----------------------------------------
