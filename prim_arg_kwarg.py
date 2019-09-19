import functools

def too(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


class Car:
    def __init__(self, color, milleage):
        self.color = color
        self.milleage = milleage

class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(func, args, kwargs)
        print(func(*args, **kwargs))
    return wrapper

@trace
def greet(greeting, name, s, f):
    return f'{greeting}, {name},{s},{f}'


too('Привет аргс и кваргс',1,2,3,4,5,6,67,8,key1=123,key2=9876,key3='qwerty')
car1 = AlwaysBlueCar('green',12323232)
print(car1.color)
print('=============')
greet('Добрый день!','Виталий',1,2)