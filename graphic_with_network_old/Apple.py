import random
# import pygame
from math import *

from graphic_with_network_old.ConstantVariables import ConstantVariables


class Apple:
    def __init__(self, x_tile_max, y_tile_max):
        self._x_tile = random.randint(0, x_tile_max)
        self._y_tile = random.randint(0, y_tile_max)
        """self._tile_width = ConstantVariables.TILE_WIDTH
        # image
        self._image = pygame.image.load('../assets/apple.png')
        self._image = pygame.transform.scale(self._image, (self._tile_width, self._tile_width))
        # rect image
        self._rect_i = self._image.get_rect()
        self._rect_i.x = self._x_tile * self._tile_width
        self._rect_i.y = self._y_tile * self._tile_width"""

    @property
    def x(self):
        return self._x_tile

    @property
    def y(self):
        return self._y_tile

    """@property
    def rect(self):
        # self._rect = pygame.Rect(self._x, self._y, self._width, self._height)
        return self._rect_i"""

    def set_new_coordinates(self, x_tile_max, y_tile_max):
        self._x_tile = random.randint(0, x_tile_max)
        self._y_tile = random.randint(0, y_tile_max)
        """self._rect_i.x = self._x_tile * self._tile_width
        self._rect_i.y = self._y_tile * self._tile_width"""

    def get_coordinate(self):
        return [self._x_tile, self._y_tile]

    """@property
    def rect_i(self):
        return self._rect_i"""

    """@property
    def image(self):
        return self._image"""
