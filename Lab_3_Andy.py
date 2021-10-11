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
        w = np.zeros(self.p + 1)
        errors = []

        for _ in range(self.M):  # по эпохам
            err = 0

            for i in range(self.p, len(y_1ab)):  # обучение до 19 элемента
                target = y_1ab[i]
                get_y = np.dot(y_1ab[(i - self.p):i], w[1:]) + w[0]

                delta = target - get_y
                update = self.n * delta

                w[1:] += update * y_1ab[(i - self.p):i]
                w[0] += update
                err += delta ** 2
            errors.append(err)
        # print("target = ", y_1ab[-1])
        # print("get = ", y_1ab[-1])
        return w, errors

    def work(self, w):
        x = self.find_X(self.a, self.b)
        y = self.find_Y(self.a, self.b)
        print(y)
        print("длина = ", len(y))
        plt.plot(range(len(y)), y, '-o', c='r', label='Slide')
        plt.grid()
        plt.show()
        for i in range(self.N):
            y = np.append(y, self.net_input(y[len(y) - self.p:], w))
            x = np.append(x, x[-1] + x[-1] - x[-2])
        return x, y

    def net_input(self, Y, w):
        return np.dot(Y, w[1:]) + w[0]

    # def work(self, w):
    #     y = self.find_Y(self.a, self.b)[:self.p]
    #     for i in range(self.p, 2*self.N):
    #         temp = 0
    #         for k in range(1, self.p+1):
    #             temp += w[k] * y[i - self.p + k - 1]
    #         temp += w[0]
    #         y = np.append(y, temp)
    #
    #     return y

    def paint(self):
        x = self.find_X(self.a, 2 * self.b - self.a)
        y = self.find_Y(self.a, 2 * self.b - self.a)
        w, err = self.fit_NC()
        x_NC, y_NC = self.work(w)


        plt.title("График функции")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid()
        plt.plot(x, y, '-o', c='deepskyblue', label='x(t)')
        plt.plot(x_NC, y_NC, '-o', c='r', label='Slide')
        plt.legend()
        plt.show()

        plt.plot(range(len(err)), err, '--og', label='Ошибка')  # МНК
        plt.grid()
        plt.show()


# ----------------------------------------
# Запуск программы
# ----------------------------------------
Work = Lab(9, -1, 3, 0.01, 20, 6, 1000)
# Work = Lab(2, -0.5, 0.5, 0.01, 20, 4, 100)
Work.paint()

# ----------------------------------------
