import random
import pygame
from math import *


class Apple:
    def __init__(self, x_max, y_max):
        self._x = random.randint(0, x_max)
        self._y = random.randint(0, y_max)
        self._height = floor(x_max / 50)
        self._width = floor(x_max / 50)
        self._rect = pygame.Rect(self._x, self._y, self._width, self._height)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def rect(self):
        self._rect = pygame.Rect(self._x, self._y, self._width, self._height)
        return self._rect

    def set_new_coordinates(self, x_max, y_max):
        self._x = random.randint(0, x_max)
        self._y = random.randint(0, y_max)

    def get_coordinate(self):
        return [self._x, self._y]