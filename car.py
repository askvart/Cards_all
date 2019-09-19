''' модуль классов автомобилей'''

class Car():
    ''' Базовый класс автомобиля'''
    def __init__(self, model, year, color, mile=0):
        self.model = model
        self.year = year
        self.color = color
        self.__mile = mile
        self.__doors = 4
        self.sound = 'BommZOOM'

    def __repr__(self):
        return f'{self.__class__.__name__}{self.model, self.year,self.color, self.__mile}'

    def __str__(self):
        return f'{self.model, self.year, self.color, self.__mile}'

    @property
    def mil_over(self):
        return self.__mile

    @mil_over.setter
    def mil_over(self, new_mile):
        self.__mile = new_mile

    @mil_over.deleter
    def mil_over(self):
        del self.__mile

    '''  Свойство вычисляемо количество стекол'''
    @property
    def count_window(self):
        return 1.5 * self.__doors

    '''Свойство количесвто дверей'''
    @property
    def door_f(self):
        return self.__doors

    @door_f.setter
    def door_f(self, new_count_doors):
        self.__doors = new_count_doors

    @door_f.deleter
    def door_f(self):
        del self.__doors


    def sound_f(self):
        '''Method call sound'''
        return self.sound

