import numpy as np
import matplotlib.pyplot as plt
import math

class Lab:
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
        self.errors = []

    def solve(self, t):
        if self.var == 9:
            return np.exp(t - 2) - np.sin(t)
        elif self.var == 2:
            return (t ** 4) - (2 * (t ** 3)) + t
        else:
            return np.sin(t -2)

    def find_X(self, a, b):
        x = np.arange(a, b, (self.b - self.a) / self.N)
        return x

    def find_Y(self, a, b):
        y = np.array([], float)
        for i in range(len(self.find_X(a, b))):
            y = np.append(y, self.solve(self.find_X(a, b)[i]))
        return y

    def fit_NC(self):
        for _ in range(self.M):
            error = 0
            y_ist = self.find_Y(self.a, self.b)
            for i in range(self.p, self.N):  # 4-19 обучение за окном
                net = self.net_input(y_ist[(i - self.p):i])
                delta = y_ist[i] - net
                update = self.n * delta
                for k in range(1, self.p+1):
                    self.w[k] += update * y_ist[i - self.p + k - 1]
                self.w[0] += update
                error += delta ** 2
            self.errors.append(error)
        return self

    def net_input(self, X):
        return np.dot(X, self.w[1:]) + self.w[0]

    def work(self):
        for i in range(self.N, 2 * self.N):
            self.Y = np.append(self.Y, self.net_input(self.Y[(len(self.Y) - self.p):]))
            self.X = np.append(self.X, self.X[-1] + self.X[-1] - self.X[-2])


    def paint(self):
        self.fit_NC()
        print(self.w)
        # self.work()
        self.work()

        plt.title("График функции")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid()
        plt.plot(self.find_X(self.a, 2*self.b - self.a), self.find_Y(self.a, 2*self.b - self.a), '-o', c='deepskyblue', label='Y_ist')
        plt.plot(self.X, self.Y, '--o', c='red', label='Y_predict')
        plt.legend()
        plt.show()

        plt.plot(range(len(self.errors)), self.errors, '--og', label='Ошибка')  # МНК
        plt.grid()
        plt.show()


# ----------------------------------------
# Запуск программы
# ----------------------------------------
# Work = Lab(9, 0.5, 2.5, 0.1, 20, 6, 200)  # Андрей
Work = Lab(2, 0, 0.73, 1, 20, 6, 1180)  # Аня
# Work = Lab(1, -1, 1, 0.1, 20, 6, 5000)  # Синус

Work.paint()

# ----------------------------------------
