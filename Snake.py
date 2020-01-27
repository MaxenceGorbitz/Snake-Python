from math import *

class Snake:
    def __init__(self, x, y):
        self._length = 1
        self._x = floor(x)
        self._y = floor(y)

    def growth(self):
        self._length += 1

    def move(self):
        return

    #def has_lost(self):

