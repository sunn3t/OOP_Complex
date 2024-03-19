class Real:
    def __init__(self, x):
        self.x = x

    def print(self):
        return f"{self.x}"

    def add(self, other):
        return Real(self.x + other.x)


class Complex(Real):

    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def printo(self):
        pass

    def all(self):
        pass


