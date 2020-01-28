import random


class Apple:
    def __init__(self, x_max, y_max):
        self._x = random.randint(0, x_max)
        self._y = random.randint(0, y_max)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def new_coordinates(self, x_max, y_max):
        self._x = random.randint(0, x_max)
        self._y = random.randint(0, y_max)

    def get_coordinate(self):
        return [self._x, self._y]