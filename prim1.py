def uppercase(func):
    def wrapper():
        original = func()
        modify = original.upper()
        return modify
    return wrapper

def lowercase(func):
    def wrapper():
        return func().lower()
    return wrapper

def strong(func):
    def wrapper():
        return '<strong>' + func() +'</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasis
@uppercase
def greet():
    return 'Hello world!'

a = greet()
print(a)

print('================================')

@lowercase
def greet():
    return 'Привет Мир!!!'

print(greet())

