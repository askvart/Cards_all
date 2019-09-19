class MyClass:
    cicle = 4

    def method(self):
        return 'вызов метода экземпляра',self

    @classmethod
    def classmethod(cls):
        return 'вызов метода класса',cls

    @staticmethod
    def staticmethod():
        return 'вызов статического метода'

a = MyClass()

print('======= Метод экземпляра =======')
print(a.method())
print(MyClass.method(a))
print(a.__class__.method(a))
a.cicle = 6
print(MyClass.cicle)
print(a.cicle)
print(MyClass.method(a))
print(a.__class__.cicle,'\n')


print('======= Метод класса =======')
print(a.classmethod())
print(MyClass.classmethod(),'\n')


print('======= Метод статический =======')
print(a.staticmethod())
print(MyClass.staticmethod())