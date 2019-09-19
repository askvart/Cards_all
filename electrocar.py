from car import Car

''' Модуль батарея'''
class Battery():
    '''Класс батарея питания для электроавтомобиля'''
    def __init__(self, power=75):
        self._power = power

    def describe_battery(self):
        print('Замена батареи(аккумуляьтора):',self._power)

    def __repr__(self):
        return f'Battery.__class__{self._power}'

    def __str__(self):
        return f'{self._power}'

    @property
    def power_over(self):
        return self._power

    @power_over.setter
    def power_over(self, new_power):
        self._power = new_power

    @power_over.deleter
    def power_over(self):
        del self._power

'''Класс Электрокар'''
class ElectroCar(Car):
    '''Класс электромобиль'''
    def __init__(self, model, year, color):
        super().__init__(model, year, color)
        self.battery = Battery()

    def sound_f(self):
        '''Метод извлечения звука из ЭЛЕКТРОмобиля'''
        return self.sound + ' ++++ RRRRRR'











