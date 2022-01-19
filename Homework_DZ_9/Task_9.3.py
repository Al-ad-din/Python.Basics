from decimal import Decimal


class Worker:
    def __init__(self, name, surname, position, wade, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wade': wade, 'bonus': bonus}

    def __str__(self):
        return f'{self.name} {self.surname} {self.position} {self._income["wade"]} {self._income["bonus"]}'


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        result = Decimal(self._income['wade']) + Decimal(self._income['bonus'])
        return f'{result} рублей'


if __name__ == '__main__':
    clerk = Position("Петрова", "Ирина", "Секретарь", 1800, 900)
    print(clerk)
    print(clerk.get_full_name())
    print(clerk.get_total_income())
    