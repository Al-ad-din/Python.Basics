import time

class TrafficLight:
    __color = [('КРАСНЫЙ', 7), ('ЖЕЛТЫЙ', 2), ('ЗЕЛЕНЫЙ', 5)]
    def running(self):
        for c, t in self.__color:
            print(f'{c}...включен на {t} секунд...')
            time.sleep(t)

a = TrafficLight
TrafficLight.running(a)
