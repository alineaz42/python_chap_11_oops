class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The valu of {self.number} square is {self.number**2}")

    def cube(self):
        print(
            f"The valu of {self.number} cube is {self.number**3}")

    def sqRoot(self):
        print(f"The valu of {self.number} sqRoot is {self.number**0.5}")


a = Calculator(9)
a.square()
a.cube()
a.sqRoot()
