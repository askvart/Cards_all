from collections import namedtuple

Car = namedtuple('Auto',['color','milleage'])
class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'красный':
            return '#ff0000'
        else:
            return '#000000'

c = MyCarWithMethods('красный',1234)
b = MyCarWithMethods('сизый',12121)
print(c.hexcolor())
print(c.hexcolor())

Car1 = namedtuple('Авто','цвет пробег')
ElectricCar = namedtuple('Электрическийавтомобиль',Car1._fields + ('заряд',))
print(ElectricCar('красный',98676,55.00))
mycar = Car('красненький',222222)
print(mycar._asdict())
