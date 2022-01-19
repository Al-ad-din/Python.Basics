class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self._speed = float(speed)
        self._color = color
        self._name = name
        self._is_police = False

    def __str__(self):
        return f'{self._speed} {self._color} {self._name} {self._is_police}'

    def go(self):
        return f'{self._name} двигается.'

    def stop(self):
        return f'{self._name} остановился.'

    def turn(self, direction):
        if direction == '<':
            return f'{self._name} повернул налево.'
        elif direction == '>':
            return f'{self._name} повернул направо.'
        else:
            raise ValueError('wrong symbol!')

    def show_speed(self):
        return f'{self._speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self._speed > 60:
            return f'{self._speed} км/ч, over speed!'
        return f'{self._speed} км/ч'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self._speed > 40:
            return f'{self._speed} км/ч, превышение скорости!'
        return f'{self._speed} км/ч'


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._is_police = True


if __name__ == '__main__':
    Ford = WorkCar('140', 'Серебристый', 'ФОРД')
    print(Ford)
    print(Ford.go())
    print(Ford.show_speed())
    print(Ford.turn('<'))
    print(Ford.turn('>'))
    print(Ford.stop())

    lexus = SportCar('310', 'Розовый', 'Лексус')
    print(lexus)

    bmw = PoliceCar('230', 'Сине-белый', 'БМВ')
    print(bmw)