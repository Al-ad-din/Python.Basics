class Stationery:
    def __init__(self, title):
        self._title = title

    def __str__(self):
        return f'{self._title}'

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Рисуем чернильной пастой')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем графитным слоем')


class Handle(Stationery):
    def draw(self):
        print(f'Рисуем краской')


if __name__ == '__main__':
    crayon = Stationery('Мелок')
    print(crayon)
    crayon.draw()
    pen = Pen('Гелевая ручка')
    print(pen)
    pen.draw()
    pencil = Pencil('Графитовый карандаш')
    print(pencil)
    pencil.draw()
    handle = Handle('Маркер')
    print(handle)
    handle.draw()