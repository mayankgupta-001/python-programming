#operator Overloading
'+'

class customNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, customNumber):
            return customNumber(self.value + other.value)
        else:
            return customNumber(self.value + other)

    def __sub__(self, other):
        if isinstance(other, customNumber):
            return customNumber(self.value - other.value)
        else:
            return customNumber(self.value - other)

    def __mul__(self, other):
        if isinstance(other, customNumber):
            return customNumber(self.value * other.value)
        else:
            return customNumber(self.value * other)

    def __truediv__(self, other):
        if isinstance(other, customNumber):
            return customNumber(self.value / other.value)
        else:
            return customNumber(self.value / other)

    def __str__(self):
        return f'{self.value}'


o1 = customNumber(4)
o2 = customNumber(5)
# c = o1 + o2
c = o1 / 44.9
print(c, type(c))
