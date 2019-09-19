from car import Car
from electrocar import ElectroCar

if __name__=='__main__':
    new_car = Car('suzuki',1987,'blue',90)
    print('Создан новый экземпляр автомобиля:', new_car)
    print(10*'=')
    print('Пробег нового автомобиля',new_car.mil_over)
    new_car.mil_over = 777
    print('THIS IS SECRET METHOD',new_car._Car__mile)

    print('Данные о пробеге:',new_car.mil_over)

    if new_car.mil_over > 0:
        print('Автомобиль с пробегом')
        print('Звук авто:',new_car.sound_f())
    else:
        print('Автомобиль без пробега')

    new_car.door_f = 2
    print('Кол-вл дверей а втомобиле:',new_car.door_f)
    print('Количество стекол в автомобиле:',new_car.count_window)

    print(20 * '=')


    electro = ElectroCar('tesla',2019,'red')
    print('Создан новый экземпляр Электрокара:',electro)
    print('Данные о пробеге в милчях:', electro.mil_over)
    electro.mil_over = 250
    print('Новые данные о пробеге', electro.mil_over)
    print("Определим атрибуты класса:")
    print(Car.__dict__.keys())
    print(vars(new_car))
    print(vars(electro))


    if electro.mil_over > 0:
        print('Электро-автомобиль с пробегом')
        print('Звук  электро-авто:',electro.sound_f())
    else:
        print('Автомобиль без пробега')

    print('Заряд новой батареи:',electro.battery)

    electro.battery.power_over = 80000
    electro.battery.describe_battery()
    print(electro.mil_over)
    print('Количество стекол в автомобиле:', electro.count_window)






