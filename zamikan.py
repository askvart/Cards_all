print('Hello amigo')
numbers = [8,3,1,2,5,4,7,6]
group={2,3,5,7}

def sort_prior(values, group):
    def inner(x):
        if x in group:
            return (0,x)
        return (1,x)
    values.sort(key=inner)

def sort_prior2(values, group):
    found = False
    def inner(x):
        nonlocal found
        if x in group:
            found = True
            return (0,x)
        return (1,x)
    values.sort(key=inner)
    return found

class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self,x):
        if x in self.group:
            self.found = True
            return (0,x)
        return (1,x)


sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True


sort_prior(numbers, group)
print(numbers)
print('=============')
result = sort_prior2(numbers, group)
print(numbers, result)