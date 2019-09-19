from collections import deque

class Counter:
    '''Класс счётчик всего подряд!'''
    count_1 = []
    def __init__(self, count=0):
        self.value = count

    def increment(self):
        self.value += 1
        self.count_1.append(self.value)

    def get(self):
        return self.value

    def get_accum(self):
        return self.count_1


class MemorizingDict(dict):
    ''' Класс делает ограниченный стэк'''
    history = deque(maxlen=10)

    def set(self, key, value):
        self.history.append(key)
        self[key] = value

    def get_history(self):
        return self.history

class CountSuper(Counter):
    def get(self):
        return f'наследованая функция:{self.value}'
