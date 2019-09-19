import math

class Pizza:
    def __init__(self, ingredients, radius):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return f'(Pizza{self.ingredients!r},{self.radius!r})'

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r**2 *math.pi


    @classmethod
    def marghrita(cls):
        return cls(['моцарелла', 'помидоры'],62)

    @classmethod
    def prosciutto(cls):
        return cls(['моцарелла','помидоры','ветчина'],64)

print(Pizza(['сыр','помидоры'],12))
print(Pizza.marghrita(),12)
print(Pizza.prosciutto(),24)

print('==============')
p = Pizza(['сало','сясо'],4)
print(p)
print(p.radius,p.area())