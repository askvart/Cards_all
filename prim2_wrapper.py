import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper_new(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper_new


def strong(func):
    def wrapper1():
        return '<strong>'+func() +'</strong>'
    return wrapper1

def emphasis(func):
    def wrapper2():
        return '<em>'+func() +'</em>'
    return wrapper2


def trace(func):
    def wrapper4(*args, **kwargs):
        print(f'Трассировка: вызвана {func.__name__}')
        print(f'Трассировка вернула:{func(*args,**kwargs)}')
        return func(*args, **kwargs)
    return wrapper4

@uppercase
def greets():
    '''Это функция приветствия!!!'''
    return 'Hello world'


@trace
def say(name, line,f,s):
    ''' Это функция выводит имя и приветствие2222222222'''
    return f'{name}:{line} - {f}{s}'

name = 'Victor'
print(greets())
print(say('Vitaly','Hello world','Привет!','Мир!'))
print('=====================')
print(greets.__doc__)
print(say.__doc__)
