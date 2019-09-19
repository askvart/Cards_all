class Dog:

    def __init__(self, name):
        self.__name = name
        self.__age = 1
        self.tricks = []

    def add_trick(self,trick):
        self.tricks.append(trick)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1,100):
            self.__age = age
        else:
            print('ERROR')



d = Dog('Fido')
d.age = 10
e = Dog('Buddy')
e.age = 6
print(d.age,e.age)
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)