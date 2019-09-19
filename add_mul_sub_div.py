class Inters():
    def __init__(self, one):
        self.one = one

    def __add__(self, other):
        return self.one + other.one

    def __sub__(self, other):
        return self.one - other.one

    def __mul__(self, other):
        return self.one * other.one

    def __floordiv__(self, other):
        return self.one // other.one

    def __truediv__(self, other):
        return self.one / other.one

    def __mod__(self, other):
        return self.one % other.one

    def __pow__(self, power, modulo=None):
        return self.one ** power.one

    def __str__(self):
        return f'{self.one}'

a = Inters(10)
b = Inters(3)
print('Первое число:',a)
print('Второе число',b)
print('Сложение:',a+b)
print('Вычитание:',a-b)
print('Умножение:',a*b)
print('Деление по модулю:',a // b)
print('Деление:',a / b)
print('Деление по модулю(остаток от деления):', a % b)
print('Возведение в степень',a ** b)
