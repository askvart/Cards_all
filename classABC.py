class A:
    def f(self):
        print("A.f")

class B:
    def f(self):
        print("B.f")

class C(A,B):
    def cf(self):
        print('C.f')

    def __repr__(self):
        return 'C({})'.format(self.f())

    def __str__(self):
        return f'{self.f()}'

c = C()
print(C.mro())
print('экземпляр:',c)