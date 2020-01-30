import random
# import pygame
from math import *

from graphic_with_network.ConstantVariables import ConstantVariables


class Apple:
    def __init__(self, x_tile_max, y_tile_max):
        self._x_tile = random.randint(0, x_tile_max)
        self._y_tile = random.randint(0, y_tile_max)

    @property
    def x(self):
        return self._x_tile

    @property
    def y(self):
        return self._y_tile

    def set_new_coordinates(self, x_tile_max, y_tile_max):
        self._x_tile = random.randint(0, x_tile_max)
        self._y_tile = random.randint(0, y_tile_max)

    def get_coordinate(self):
        return [self._x_tile, self._y_tile]
