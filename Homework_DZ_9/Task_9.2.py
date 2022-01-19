class Road:
    _lenght, _widht = 0, 0

    def __init__(self, lenght, widht, weight_sq_mt, thickness):
        self._weight_sq_mt, self._thickness, self._lenght, self._widht = weight_sq_mt / 1000, thickness, lenght, widht

    def asphalt(self):
        return self._lenght * self._widht * self._weight_sq_mt * self._thickness


calc = Road(5000, 20, 25, 5)
print(calc.asphalt())
