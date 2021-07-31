# procedure oriented programming
# a = 12
# b = 14
# print("The sum of a and b is", a+b)

class Number:
    def sum(self):
        return self.a + self.b


num = Number()
num.a = 12
num.b = 15
s = num.sum()
print(s)
