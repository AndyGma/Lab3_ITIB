class Lab:
    a = None
    b = None

    def set_data(self, a, b):
        self.a = a
        self.b = b
    def get_data(self):
        print("a = ", self.a, "\tb = ", self.b, sep="")

Andy = Lab()
Andy.set_data(-1, 2)  # ввод a, b
Andy.get_data()