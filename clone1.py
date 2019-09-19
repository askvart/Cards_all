import copy
'''Глубокое копирование - это пример y
   поверхностное копирование это x1'''

x = [[1,2,3],[4,5,],[6,7]]
x1 = list(x)
y = copy.deepcopy(x)

x[0][0] = 19

print(x)
print(x1)
print(y)
