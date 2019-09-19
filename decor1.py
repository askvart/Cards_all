import time
from decor import decor, strong, emphasis, trace, clock

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


def greet():
    return 'hello world'


@strong
@emphasis
@decor
def greet():
    return 'hello world'

@trace
def say(name,old):
    return name,old

if __name__== '__main__':
    gr = greet()
    print('Hey',gr)
    print('======================')
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))


    gr = say('vasja','hot')
    print(gr)

