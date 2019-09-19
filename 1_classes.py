class Car:
    cicle = 4
    def __init__(self,color,milleage):
        self.color = color
        self.milleage = milleage
    #def __str__(self):
    #    return f'{self.color}->{self.milleage}'

    def __repr__(self):
        return f'{self.color}:{self.milleage}'

class CounterInstance:
    num_instance = 0

    def __init__(self):
        self.__class__.num_instance += 1

    def __repr__(self):
        return f'Экземпляр создан:{self.__class__.num_instance}'

for i in range(0,10):
    n = CounterInstance()
    print(n.num_instance)
print(n)


m = Car('red',1234)
x = Car('blue',999)
x.cicle = 3
print(m)
print(m.cicle,m.color,m.milleage,Car.cicle)
print(x.cicle,x.__class__.cicle,x.color,x.milleage)
