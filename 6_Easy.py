# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar:

    def __init__(self, color, speed, name):
        self.color = color
        self.speed = speed
        self.name = name
        self.is_police = False

    def go(self):
        print('Автомобиль начал движение.')

    def stop(self):
        print('Автомобиль остановился.')

    def turn(self):
        direction = input('Введите, куда поворачивать?')
        print('Автомобиль совершил поворот {}.'.format(direction))

    def speed(self):
        return self.speed


class SportCar:

    def __init__(self, color, speed, name):
        self.color = color
        self.speed = speed
        self.name = name
        self.is_police = False

    def go(self):
        print('Автомобиль начал движение.')

    def stop(self):
        print('Автомобиль остановился.')

    def turn(self):
        direction = input('Введите, куда поворачивать?')
        print('Автомобиль совершил поворот {}.'.format(direction))

    def speed(self):
        return self.speed


class WorkCar:

    def __init__(self, color, speed, name):
        self.color = color
        self.speed = speed
        self.name = name
        self.is_police = False

    def go(self):
        print('Автомобиль начал движение.')

    def stop(self):
        print('Автомобиль остановился.')

    def turn(self):
        direction = input('Введите, куда поворачивать?')
        print('Автомобиль совершил поворот {}.'.format(direction))

    def speed(self):
        return self.speed


class PoliceCar:

    def __init__(self, color, speed, name):
        self.color = color
        self.speed = speed
        self.name = name
        self.is_police = True

    def go(self):
        print('Автомобиль начал движение.')

    def stop(self):
        print('Автомобиль остановился.')

    def turn(self):
        direction = input('Введите, куда поворачивать?')
        print('Автомобиль совершил поворот {}.'.format(direction))

    def speed(self):
        return self.speed


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, color, speed, name):
        self.color = color
        self.speed = speed
        self.name = name
        self.is_police = False

    def go(self):
        print('Автомобиль начал движение.')

    def stop(self):
        print('Автомобиль остановился.')

    def turn(self):
        direction = input('Введите, куда поворачивать?')
        print('Автомобиль совершил поворот {}.'.format(direction))

    def speed(self):
        return self.speed


class TownCar(Car):
    pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, color, speed, name):
        self.is_police = True


